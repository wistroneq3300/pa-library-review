#!/usr/bin/env python3
"""Read-only integrity gates for the append-only 942-case ED re-review overlay."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
OVERLAY = ROOT / "gpt-review" / "v3-1-ed-rereview-942"
RECORDS = OVERLAY / "REVIEW_RECORDS"
FULL = ROOT / "gpt-review" / "v3-1-full-3112"

PROTECTED = {
    ROOT / "data" / "REVISED_commands_merged_with_raw.xlsx": "e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8",
    ROOT / "data" / "tests.json": "5eefd664be9ed794e4429095f9d8e0c969d392a688b787af71f4f319526fdd37",
    ROOT / "data" / "tests_gpt_merged.json": "34d0133ce0bab7647179f9822174838ecdfd5ee90e766eb9802eb8672dcfe4a2",
    ROOT / "gpt-review" / "test_gpt_review.json": "5776cf96ff65219ca8d0dce07631914a9f45a98c0bccae8390f076ec67e25869",
}
BASE_METRICS = {
    "review_cases": 3112,
    "engineering_decision_pending": 942,
    "source_conflict": 927,
    "blocked": 214,
    "fully_automatable": 495,
    "requires_package_user_confirmation": 1863,
    "manual_only": 540,
}
CLASS_KEYS = {
    "FULLY AUTOMATABLE": "fully_automatable",
    "REQUIRES PACKAGE / USER CONFIRMATION": "requires_package_user_confirmation",
    "MANUAL ONLY": "manual_only",
    "BLOCKED": "blocked",
}
REQUIRED_TOP = {
    "schema_version", "rereview_sequence", "source_key", "case_variant_id",
    "source_ref", "source_snapshot", "historical_review_record", "old_problem",
    "new_disposition", "disposition_reason", "decision_basis", "test_case",
    "source_conflict", "blocked", "pending", "external_authorities",
    "traceability", "review_quality",
}
REQUIRED_TEST = {
    "test_name", "automation_classification", "purpose", "required_package",
    "test_command", "expected_result", "pass_fail_basis", "safety_gate",
    "expected_evidence", "recovery",
}
ANTI_TEMPLATE = (
    "old_problem", "disposition_reason", "test_case.purpose",
    "test_case.test_command", "test_case.pass_fail_basis", "test_case.recovery",
)


def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_strict(path: Path, failures: list[str]) -> Any:
    duplicates: list[str] = []

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                duplicates.append(key)
            result[key] = value
        return result

    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)
    except (OSError, json.JSONDecodeError) as exc:
        failures.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return None
    for key in duplicates:
        failures.append(f"{path.relative_to(ROOT)}: duplicate JSON key {key!r}")
    return value


def nested(record: dict[str, Any], dotted: str) -> Any:
    value: Any = record
    for part in dotted.split("."):
        value = value.get(part) if isinstance(value, dict) else None
    return value


def main() -> int:
    failures: list[str] = []
    for path, expected in PROTECTED.items():
        if not path.exists() or digest_file(path) != expected:
            failures.append(f"protected source hash changed: {path.relative_to(ROOT)}")

    full_progress = load_strict(FULL / "PROGRESS.json", failures) or {}
    manifest = (load_strict(FULL / "SELECTION_MANIFEST.json", failures) or {}).get("cases", [])
    progress = load_strict(OVERLAY / "PROGRESS.json", failures) or {}
    recon = load_strict(OVERLAY / "SCOPE_RECONCILIATION.json", failures) or {}
    pending_keys = {
        item.get("source_key") for item in full_progress.get("engineering_decisions_pending", [])
        if isinstance(item, dict)
    }
    queue = [case for case in manifest if case.get("source_key") in pending_keys]
    queue_text = "\n".join(f"{case['source_key']}\t{case['case_variant_id']}" for case in queue)
    queue_hash = digest_text(queue_text)
    if len(queue) != 942 or queue_hash != progress.get("queue_sha256") or queue_hash != recon.get("formal_queue", {}).get("sha256"):
        failures.append(f"formal queue mismatch: count={len(queue)} sha256={queue_hash}")
    queue_by_key = {case["source_key"]: (index + 1, case) for index, case in enumerate(queue)}
    manifest_by_key = {case["source_key"]: case for case in manifest}

    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(RECORDS.glob("*.json")):
        value = load_strict(path, failures)
        if isinstance(value, dict):
            records.append((path, value))
    event_sequences = [record.get("rereview_sequence") for _, record in records]
    if event_sequences != list(range(1, len(records) + 1)):
        failures.append("append-only review-event sequences are not contiguous from 1")

    in_scope: list[tuple[Path, dict[str, Any], int]] = []
    out_scope: list[tuple[Path, dict[str, Any]]] = []
    seen_scope: set[str] = set()
    for path, record in records:
        key = record.get("source_key")
        variant = record.get("case_variant_id")
        case = manifest_by_key.get(key)
        if not case:
            failures.append(f"{path.name}: Source Key absent from manifest")
            continue
        if variant != case.get("case_variant_id"):
            failures.append(f"{path.name}: Variant ID mismatch")
        source_ref = record.get("source_ref", {})
        if source_ref.get("original_row_sha256") != case.get("original_row_sha256"):
            failures.append(f"{path.name}: original row hash mismatch")
        if key in queue_by_key:
            if key in seen_scope:
                failures.append(f"duplicate formal queue review: {key}")
            seen_scope.add(key)
            in_scope.append((path, record, queue_by_key[key][0]))
        else:
            out_scope.append((path, record))

    out_text = "\n".join(f"{path.name}\t{record['source_key']}\t{record['case_variant_id']}" for path, record in out_scope)
    if len(out_scope) != recon.get("checkpoint_audit", {}).get("out_of_scope_records_retained_as_history") or digest_text(out_text) != recon.get("identity_digests", {}).get("out_of_scope_sha256"):
        failures.append("acknowledged out-of-scope historical set changed")
    adopted_text = "\n".join(
        f"{sequence}\t{record['source_key']}\t{record['case_variant_id']}\t{path.name}"
        for path, record, sequence in sorted(in_scope, key=lambda item: item[2])
    )
    initial_sequences = set(range(1, 14)) | {15} | set(range(22, 57))
    initial_adopted = sorted(
        (item for item in in_scope if item[2] in initial_sequences),
        key=lambda item: item[2],
    )
    initial_text = "\n".join(
        f"{sequence}\t{record['source_key']}\t{record['case_variant_id']}\t{path.name}"
        for path, record, sequence in initial_adopted
    )
    if digest_text(initial_text) != recon.get("identity_digests", {}).get("adopted_sha256"):
        failures.append("initial adopted formal-queue set changed")

    legacy_missing_project = []
    repeats: dict[str, defaultdict[str, list[str]]] = {field: defaultdict(list) for field in ANTI_TEMPLATE}
    pending_delta = conflict_delta = blocked_delta = 0
    class_delta: Counter[str] = Counter()
    resolved = retained = project_required = 0
    for path, record, formal_sequence in in_scope:
        missing = sorted(REQUIRED_TOP - set(record))
        if missing:
            failures.append(f"{path.name}: missing top-level fields {missing}")
        missing_test = sorted(REQUIRED_TEST - set(record.get("test_case", {})))
        if missing_test:
            failures.append(f"{path.name}: missing test-case fields {missing_test}")
        if "project_authority" not in record:
            legacy_missing_project.append(path.name)
        if record.get("formal_queue_sequence") not in (None, formal_sequence):
            failures.append(f"{path.name}: formal queue sequence mismatch")
        historical_path = ROOT / str(record.get("historical_review_record", ""))
        historical = load_strict(historical_path, failures) if historical_path.is_file() else None
        old_class = historical.get("automation_classification") if isinstance(historical, dict) else None
        new_class = record.get("test_case", {}).get("automation_classification")
        if old_class not in CLASS_KEYS or new_class not in CLASS_KEYS:
            failures.append(f"{path.name}: invalid/missing old or new automation class")
        else:
            class_delta[old_class] -= 1
            class_delta[new_class] += 1
        for field in ("pending", "source_conflict", "blocked"):
            state = record.get(field, {})
            if not isinstance(state.get("before"), bool) or not isinstance(state.get("after"), bool):
                failures.append(f"{path.name}: {field} before/after are not booleans")
        pending_delta += int(record["pending"]["after"]) - int(record["pending"]["before"])
        conflict_delta += int(record["source_conflict"]["after"]) - int(record["source_conflict"]["before"])
        blocked_delta += int(record["blocked"]["after"]) - int(record["blocked"]["before"])
        resolved += int(not record["pending"]["after"])
        retained += int(record["pending"]["after"])
        project_required += int(bool(record["pending"].get("remaining_project_configuration")))
        for field in ANTI_TEMPLATE:
            repeats[field][json.dumps(nested(record, field), sort_keys=True, ensure_ascii=False)].append(record["source_key"])

    legacy_text = "\n".join(sorted(legacy_missing_project))
    legacy_rule = recon.get("legacy_schema_exception", {})
    if len(legacy_missing_project) != legacy_rule.get("record_count") or digest_text(legacy_text) != legacy_rule.get("filename_sha256"):
        failures.append("legacy project_authority exception set changed or a new record omitted the field")
    anti_template = [
        {"field": field, "source_keys": keys}
        for field, groups in repeats.items() for keys in groups.values() if len(keys) > 1
    ]
    if anti_template:
        failures.append(f"exact anti-template duplicates found: {anti_template[:5]}")

    missing_queue = [case for case in queue if case["source_key"] not in seen_scope]
    next_case = missing_queue[0] if missing_queue else None
    expected_metrics = dict(BASE_METRICS)
    expected_metrics["engineering_decision_pending"] += pending_delta
    expected_metrics["source_conflict"] += conflict_delta
    expected_metrics["blocked"] += blocked_delta
    for old_or_new, delta in class_delta.items():
        if old_or_new != "BLOCKED":
            expected_metrics[CLASS_KEYS[old_or_new]] += delta
    expected_dispositions = {
        "RESOLVED": resolved,
        "RETAINED_ENGINEERING_DECISION_PENDING": retained,
        "RETAINED_PROJECT_SPEC_REQUIRED": project_required,
    }
    actual_dispositions = {key: progress.get("disposition_counts", {}).get(key) for key in expected_dispositions}
    if progress.get("reviewed_count") != len(in_scope) or progress.get("remaining_count") != len(missing_queue):
        failures.append("formal queue reviewed/remaining count mismatch")
    if progress.get("review_event_count") != len(records):
        failures.append("review_event_count mismatch")
    if progress.get("effective_metrics") != expected_metrics:
        failures.append(f"effective metrics mismatch: expected {expected_metrics}")
    if actual_dispositions != expected_dispositions:
        failures.append(f"disposition counts mismatch: expected {expected_dispositions}")
    if next_case and (progress.get("next_source_key"), progress.get("next_case_variant_id")) != (next_case["source_key"], next_case["case_variant_id"]):
        failures.append("next identity is not the first missing formal queue case")

    result = {
        "status": "PASS" if not failures else "FAIL",
        "formal_queue_count": len(queue),
        "formal_queue_sha256": queue_hash,
        "review_event_count": len(records),
        "reviewed_formal_queue_count": len(in_scope),
        "out_of_scope_historical_count": len(out_scope),
        "remaining_formal_queue_count": len(missing_queue),
        "next_formal_queue_sequence": queue_by_key[next_case["source_key"]][0] if next_case else None,
        "next_source_key": next_case.get("source_key") if next_case else None,
        "next_case_variant_id": next_case.get("case_variant_id") if next_case else None,
        "effective_metrics": expected_metrics,
        "disposition_counts": expected_dispositions,
        "anti_template_exact_duplicate_group_count": len(anti_template),
        "protected_source_hashes": "PASS" if all(digest_file(path) == expected for path, expected in PROTECTED.items()) else "FAIL",
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
