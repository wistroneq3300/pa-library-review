#!/usr/bin/env python3
"""Build deterministic pilot indexes/statistics from completed review records."""

from __future__ import annotations

import collections
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORD_DIR = ROOT / "REVIEW_RECORDS"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


records = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(RECORD_DIR.glob("*.json"))]

proposals = {
    "schema_version": "v3-proposed-changes-1.0",
    "record_count": len(records),
    "note": "Derived index only. REVIEW_RECORDS are the authoritative per-case semantic records; no production source is modified.",
    "changes": [
        {
            "sequence": r["sequence"],
            "source_key": r["source_key"],
            "case_variant_id": r["case_variant_id"],
            "original_row_sha256": r["source_integrity"]["original_row_sha256"],
            "v2_automation_classification": r["v2_review_conclusion"]["automation_classification"],
            "v3_review_outcome": r["v3_review_conclusion"]["review_outcome"],
            "v3_automation_classification": r["v3_review_conclusion"]["automation_classification"],
            "execution_readiness": r["v3_review_conclusion"]["execution_readiness"],
            "identified_defects": r.get("identified_defects", []),
            "changed_fields": r.get("changed_fields", []),
            "objective_improvement_over_v2": r["objective_improvement_over_v2"],
            "resolved_blockers": r.get("resolved_blockers", []),
            "remaining_blockers": r.get("remaining_blockers", []),
            "agent_understanding_status": r.get("agent_understanding_result", {}).get("status"),
            "regression_status": r.get("regression_status", {}).get("status"),
            "revision_candidate": r["revision_candidate"],
        }
        for r in records
    ],
}
(ROOT / "V3_PROPOSED_CHANGES.json").write_text(
    json.dumps(proposals, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

normalize_v2 = {
    "REQUIRES PACKAGE": "REQUIRES PACKAGE / USER CONFIRMATION",
    "USER CONFIRMATION": "REQUIRES PACKAGE / USER CONFIRMATION",
}
v2_counter = collections.Counter(
    normalize_v2.get(r["v2_review_conclusion"]["automation_classification"], r["v2_review_conclusion"]["automation_classification"])
    for r in records
)
stats = {
    "schema_version": "v3-pilot-stats-1.0",
    "record_count": len(records),
    "sheet_distribution": dict(collections.Counter(r["source_ref"]["sheet"] for r in records)),
    "v2_automation_distribution_normalized": dict(v2_counter),
    "v3_automation_distribution": dict(collections.Counter(r["v3_review_conclusion"]["automation_classification"] for r in records)),
    "v3_outcome_distribution": dict(collections.Counter(r["v3_review_conclusion"]["review_outcome"] for r in records)),
    "v2_blocked_to_nonblocked": [r["sequence"] for r in records if r["v2_review_conclusion"]["automation_classification"] == "BLOCKED" and r["v3_review_conclusion"]["automation_classification"] != "BLOCKED"],
    "v3_blocked": [r["sequence"] for r in records if r["v3_review_conclusion"]["automation_classification"] == "BLOCKED"],
    "agent_understanding_status": dict(collections.Counter(r.get("agent_understanding_result", {}).get("status") for r in records)),
    "all_hardware_tested_false": all(r.get("regression_status", {}).get("hardware_tested") is False for r in records),
    "all_pass_claimed_false": all(r.get("regression_status", {}).get("pass_claimed") is False for r in records),
}
(ROOT / "AUDIT_STATS.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")

for count in (180, 200):
    subset = records[:count]
    checkpoint = {
        "checkpoint": count,
        "reviewed_count": count,
        "unique_source_keys": len({r["source_key"] for r in subset}),
        "unique_case_variant_ids": len({r["case_variant_id"] for r in subset}),
        "last_completed": subset[-1]["source_ref"],
        "review_record_sha256": {f"{r['sequence']:04d}": digest(sorted(RECORD_DIR.glob(f"{r['sequence']:04d}_*.json"))[0]) for r in subset[-20:]},
        "hardware_tested": False,
        "semantic_validation_claimed_by_mechanical_checkpoint": False,
    }
    (ROOT / "checkpoints" / f"{count:04d}.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"records": len(records), "outputs": ["V3_PROPOSED_CHANGES.json", "AUDIT_STATS.json", "checkpoints/0180.json", "checkpoints/0200.json"]}))
