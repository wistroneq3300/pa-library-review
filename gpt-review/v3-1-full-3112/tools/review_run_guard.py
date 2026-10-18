#!/usr/bin/env python3
"""Lease and checkpoint guard for bounded V3.1 review continuation turns.

This tool does not generate reviews.  It prevents overlapping writers and makes
the hand-off between finite Codex turns explicit.  An expired ACTIVE lease is
never removed or replaced automatically; a human/agent must first audit active
process/turn evidence and use a new run id after that audit.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parent
REVIEW_DIR = TOOLS_DIR.parent
REPO_ROOT = REVIEW_DIR.parents[1]
PROGRESS_PATH = REVIEW_DIR / "PROGRESS.json"
RECORDS_DIR = REVIEW_DIR / "REVIEW_RECORDS"
LOCK_PATH = REPO_ROOT / "gpt-review" / ".review_run_lock.json"


def now_local() -> datetime:
    return datetime.now().astimezone()


def iso(value: datetime | None) -> str | None:
    return value.isoformat(timespec="seconds") if value else None


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    os.replace(temporary, path)


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=REPO_ROOT, text=True, encoding="utf-8"
    ).strip()


def checkpoint() -> dict:
    progress = read_json(PROGRESS_PATH)
    records = list(RECORDS_DIR.glob("*.json"))
    expected_new = progress["new_full_review_records_count"]
    baseline = progress["completed_count"] - expected_new
    failures: list[str] = []
    if len(records) != expected_new:
        failures.append(
            f"record file count {len(records)} != progress new record count {expected_new}"
        )
    if baseline != 200:
        failures.append(f"derived baseline {baseline} != 200")
    if progress["remaining_count"] != progress["target_count"] - progress["completed_count"]:
        failures.append("remaining_count does not match target_count - completed_count")
    if sum(progress["classification_statistics"].values()) != progress["completed_count"]:
        failures.append("classification statistics do not sum to completed_count")
    return {
        "valid": not failures,
        "failures": failures,
        "completed_count": progress["completed_count"],
        "new_record_count": expected_new,
        "record_file_count": len(records),
        "next_source_key": progress["next_unreviewed_source_key"],
        "next_case_variant_id": progress["next_unreviewed_case_variant_id"],
        "head": git("rev-parse", "HEAD"),
        "branch": git("branch", "--show-current"),
    }


def lock_status() -> dict:
    current = now_local()
    if not LOCK_PATH.exists():
        return {"exists": False, "state": "ABSENT", "now": iso(current)}
    lock = read_json(LOCK_PATH)
    expires = parse_iso(lock.get("lease_expires_at"))
    expired = bool(expires and current > expires.astimezone(current.tzinfo))
    state = lock.get("status", "LEGACY")
    if state == "ACTIVE" and expired:
        state = "STALE_REQUIRES_AUDIT"
    return {
        "exists": True,
        "state": state,
        "expired": expired,
        "now": iso(current),
        "lock": lock,
    }


def base_lock(args: argparse.Namespace, status: str) -> dict:
    current = now_local()
    cp = checkpoint()
    return {
        "schema_version": "v3-1-review-run-lease-2.0",
        "status": status,
        "run_id": args.run_id,
        "owner_thread_id": args.thread_id,
        "owner_kind": "codex-bounded-turn",
        "host": os.environ.get("COMPUTERNAME", "unknown"),
        "process_model": "no persistent review worker; lease spans one finite Codex turn",
        "started_at": iso(current),
        "lease_updated_at": iso(current),
        "lease_expires_at": iso(current + timedelta(minutes=args.lease_minutes)) if status == "ACTIVE" else None,
        "branch": cp["branch"],
        "completed_count": cp["completed_count"],
        "next_source_key": cp["next_source_key"],
        "next_case_variant_id": cp["next_case_variant_id"],
        "last_commit": cp["head"],
        "target_completed_count": 3112,
        "turn_quota": args.turn_quota,
        "stop_reason": None,
    }


def acquire(args: argparse.Namespace) -> int:
    cp = checkpoint()
    if not cp["valid"]:
        print(json.dumps({"status": "CHECKPOINT_INVALID", "checkpoint": cp}, indent=2))
        return 4
    state = lock_status()
    if state["exists"] and state["state"] == "ACTIVE":
        old = state["lock"]
        if old.get("run_id") != args.run_id or old.get("owner_thread_id") != args.thread_id:
            print(json.dumps({"status": "ACTIVE_LEASE_CONFLICT", **state}, indent=2))
            return 2
    elif state["exists"] and state["state"] == "STALE_REQUIRES_AUDIT":
        print(json.dumps({"status": "STALE_REQUIRES_AUDIT", **state}, indent=2))
        return 3
    lease = base_lock(args, "ACTIVE")
    if state["exists"]:
        lease["previous_lock"] = state["lock"]
    atomic_write(LOCK_PATH, lease)
    print(json.dumps({"status": "ACQUIRED", "checkpoint": cp, "lease": lease}, indent=2))
    return 0


def refresh(args: argparse.Namespace, make_idle: bool = False) -> int:
    cp = checkpoint()
    if not cp["valid"]:
        print(json.dumps({"status": "CHECKPOINT_INVALID", "checkpoint": cp}, indent=2))
        return 4
    state = lock_status()
    if not state["exists"]:
        print(json.dumps({"status": "NO_LEASE"}, indent=2))
        return 2
    lock = state["lock"]
    if lock.get("run_id") != args.run_id or lock.get("owner_thread_id") != args.thread_id:
        print(json.dumps({"status": "LEASE_OWNER_MISMATCH", **state}, indent=2))
        return 2
    current = now_local()
    lock.update(
        {
            "status": "IDLE" if make_idle else "ACTIVE",
            "lease_updated_at": iso(current),
            "lease_expires_at": None if make_idle else iso(current + timedelta(minutes=args.lease_minutes)),
            "completed_count": cp["completed_count"],
            "next_source_key": cp["next_source_key"],
            "next_case_variant_id": cp["next_case_variant_id"],
            "last_commit": cp["head"],
            "turn_quota": args.turn_quota,
            "stop_reason": args.reason if make_idle else None,
        }
    )
    atomic_write(LOCK_PATH, lock)
    print(json.dumps({"status": "IDLE" if make_idle else "REFRESHED", "checkpoint": cp, "lease": lock}, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("status", "acquire", "refresh", "idle"))
    parser.add_argument("--run-id", default="")
    parser.add_argument("--thread-id", default="")
    parser.add_argument("--lease-minutes", type=int, default=30)
    parser.add_argument("--turn-quota", type=int, default=10)
    parser.add_argument("--reason", default="bounded turn completed")
    args = parser.parse_args()
    if args.action == "status":
        print(json.dumps({"checkpoint": checkpoint(), "lease": lock_status()}, indent=2))
        return 0
    if not args.run_id or not args.thread_id:
        parser.error("--run-id and --thread-id are required for lease mutations")
    if args.action == "acquire":
        return acquire(args)
    if args.action == "refresh":
        return refresh(args)
    return refresh(args, make_idle=True)


if __name__ == "__main__":
    sys.exit(main())
