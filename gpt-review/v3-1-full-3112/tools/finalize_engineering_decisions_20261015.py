#!/usr/bin/env python3
"""Finalize derived progress and audit documents after explicit decision migration."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "gpt-review" / "v3-1-full-3112"
MIGRATION = Path(__file__).with_name("apply_engineering_decisions_20261015.py")


def load_cases():
    spec = importlib.util.spec_from_file_location("decision_migration", MIGRATION)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.CASES


def main() -> None:
    cases = load_cases()
    progress_path = WORKSPACE / "PROGRESS.json"
    progress = json.loads(progress_path.read_text(encoding="utf-8"))
    if progress["completed_count"] != 891:
        raise RuntimeError("retrospective corrections must not change completed_count")
    progress["logic_version"] = "V3.1 Final Audit + ED-32 + ED-33..52"
    progress["classification_statistics"] = {
        "MANUAL ONLY": 336,
        "REQUIRES PACKAGE / USER CONFIRMATION": 180,
        "FULLY AUTOMATABLE": 315,
        "BLOCKED": 60,
    }
    progress["blocked_count"] = 60
    progress["engineering_decisions_pending"] = [
        {
            "source_key": "Functionality|708|Wistron-BIOS-00376-V002",
            "question": "Decide whether this case validates whole SMM TSEG range coverage or absence of SmiHandler4 in a debug SOL trace; align the purpose/evidence model and approve any debug BIOS, register access and rollback/recovery plan.",
        }
    ]
    progress["retrospective_audit_20261015"] = {
        "affected_record_count": len(cases),
        "completed_count_change": 0,
        "decision_register": "gpt-review/v3-1-full-3112/ENGINEERING_DECISIONS_APPROVED_20261015.md",
        "report": "gpt-review/v3-1-full-3112/RETROSPECTIVE_IMPACT_20261015.md",
        "remaining_engineer_decision_pending": ["Functionality|708|Wistron-BIOS-00376-V002"],
    }
    progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    pending = """# Engineering Decisions Pending

The 2026-10-15 rulings ED-33 through ED-52 resolve the earlier review-level
questions for their named variants except BIOS 00376. Project images, versions,
SPEC values, parameters, tool packages, environments, safety approval and
recovery remain per-case execution-readiness inputs; they are not global
engineering-decision blockers.

## Case-level decision pending

- `Functionality|708|Wistron-BIOS-00376-V002` — **ENGINEER DECISION PENDING**.
  Decide whether the testcase validates whole SMM TSEG range coverage or the
  absence of `SmiHandler4` in a debug SOL trace. Align the title, procedure and
  criteria; define the exact range/register model or handler stimulus/evidence;
  and approve any debug BIOS, read-only register/SOL method, rollback and OOB
  recovery. No debug BIOS flash or unapproved register operation is authorized.

See `ENGINEERING_DECISIONS_APPROVED_20261015.md` and
`RETROSPECTIVE_IMPACT_20261015.md` for applied decisions and affected records.
"""
    (WORKSPACE / "ENGINEERING_DECISIONS_PENDING.md").write_text(pending, encoding="utf-8", newline="\n")

    lines = [
        "# Retrospective Impact Audit — 2026-10-15",
        "",
        "Scope: targeted re-check of the valid 891 completed reviews against ED-33 through ED-52.",
        "This is not a recount or a full re-review. `completed_count` remains 891.",
        "",
        "## Affected review records",
        "",
        "| Source key | Decision | Active classification | Correction reason |",
        "|---|---|---|---|",
    ]
    for source_key, decision_id, new_class, _outcome, _second, interpretation, _checkpoints, _remaining in cases:
        reason = interpretation.replace("|", "\\|")
        lines.append(f"| `{source_key}` | {decision_id} | `{new_class}` | {reason} |")
    lines += [
        "",
        "## Result",
        "",
        f"- Affected records: **{len(cases)}**",
        "- Completed-count change: **0**",
        "- Active classification after correction: 336 Manual Only, 180 Requires Package / User Confirmation, 315 Fully Automatable, 60 Blocked.",
        "- Remaining explicit engineer decision: BIOS 00376 only.",
        "- Master XLSX, `data/tests.json`, Source Identity, hashes, source snapshots and historical review text remain unchanged.",
        "- Each changed record contains a source-key-bound `engineering_decision_update` overlay with checkpoints, readiness inputs, coverage and verdict boundaries.",
        "",
    ]
    (WORKSPACE / "RETROSPECTIVE_IMPACT_20261015.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(json.dumps({"affected_records": len(cases), "completed_count": progress["completed_count"], "blocked_count": progress["blocked_count"]}, indent=2))


if __name__ == "__main__":
    main()
