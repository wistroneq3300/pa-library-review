#!/usr/bin/env python3
"""Read-only release validator for the V3.1 Final Audit artifacts."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
AUDIT = ROOT / "gpt-review" / "v3-1-final-audit"
MANIFEST = ROOT / "gpt-review" / "v3-pilot-200" / "SELECTION_MANIFEST.json"
EXPECTED_HASHES = {
    "data/REVISED_commands_merged_with_raw.xlsx": "e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8",
    "data/tests.json": "5eefd664be9ed794e4429095f9d8e0c969d392a688b787af71f4f319526fdd37",
    "data/tests_gpt_merged.json": "34d0133ce0bab7647179f9822174838ecdfd5ee90e766eb9802eb8672dcfe4a2",
    "gpt-review/test_gpt_review.json": "5776cf96ff65219ca8d0dce07631914a9f45a98c0bccae8390f076ec67e25869",
    "gpt-review/v3-pilot-200/SELECTION_MANIFEST.json": "55c915d7c91d2e4340353e881a85e1f0ff236f62a858106a19c05751f31a086d",
}
VALID_OUTCOMES = {"PASS_UNCHANGED", "CORRECTED", "NEED_ENGINEER_DECISION", "REGRESSION_FOUND", "VALIDATION_PENDING"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    failures = []
    for rel, expected in EXPECTED_HASHES.items():
        actual = sha256(ROOT / rel)
        if actual != expected:
            failures.append(f"source hash changed: {rel}: {actual}")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))["cases"]
    records = []
    for path in sorted((AUDIT / "AUDIT_RECORDS").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            failures.append(f"{path.name}: expected JSON array")
        else:
            records.extend(data)
    records.sort(key=lambda item: item["sequence"])
    if len(records) != 200:
        failures.append(f"expected 200 records, found {len(records)}")
    if [r["sequence"] for r in records] != list(range(1, 201)):
        failures.append("sequences are not exactly 1..200")
    if len({r["source_key"] for r in records}) != 200:
        failures.append("source keys are not unique")
    if len({r["case_variant_id"] for r in records}) != 200:
        failures.append("case variants are not unique")
    if len({r.get("independent_semantic_finding") for r in records}) != 200:
        failures.append("semantic findings are not unique")
    for expected, record in zip(manifest, records):
        for key in ("sequence", "source_key", "case_variant_id"):
            if record.get(key) != expected.get(key):
                failures.append(f"seq {record.get('sequence')}: manifest mismatch {key}")
        if record.get("audit_outcome") not in VALID_OUTCOMES:
            failures.append(f"seq {record.get('sequence')}: invalid outcome")
        if not record.get("independent_semantic_finding"):
            failures.append(f"seq {record.get('sequence')}: missing semantic finding")
        material = record.get("source_material_read", {})
        for key in ("xlsx_row", "deepseek", "gpt_v2"):
            if material.get(key) is not True:
                failures.append(f"seq {record.get('sequence')}: missing {key} read")
        for key in ("v3", "v3_1"):
            if not material.get(key) or not (ROOT / material[key]).is_file():
                failures.append(f"seq {record.get('sequence')}: missing {key} record link")
        checks = record.get("audit_checks", {})
        for key in (
            "original_test_intent_preserved",
            "scope_not_reduced_without_recorded_override",
            "v3_detail_retained_by_additive_overlay_rule",
            "original_method_and_command_provenance_preserved",
        ):
            if checks.get(key) is not True:
                failures.append(f"seq {record.get('sequence')}: failed audit check {key}")
        if record.get("hardware_tested") is not False:
            failures.append(f"seq {record.get('sequence')}: invalid hardware claim")
        if record.get("formal_test_verdict") != "ENGINEER OWNED; NOT SET":
            failures.append(f"seq {record.get('sequence')}: invalid verdict owner")
    classes = Counter(r["after"]["automation_classification"] for r in records)
    outcomes = Counter(r["audit_outcome"] for r in records)
    conflicts = sum(bool(r["after"]["source_conflict"]) for r in records)
    expected_classes = {"FULLY AUTOMATABLE": 12, "REQUIRES PACKAGE / USER CONFIRMATION": 139, "MANUAL ONLY": 27, "BLOCKED": 22}
    expected_outcomes = {"PASS_UNCHANGED": 173, "CORRECTED": 26, "NEED_ENGINEER_DECISION": 1}
    if dict(classes) != expected_classes:
        failures.append(f"classification counts differ: {dict(classes)}")
    if dict(outcomes) != expected_outcomes:
        failures.append(f"outcome counts differ: {dict(outcomes)}")
    if conflicts != 48:
        failures.append(f"expected 48 source conflicts, found {conflicts}")
    result = {
        "status": "PASS" if not failures else "FAIL",
        "record_count": len(records),
        "unique_source_keys": len({r["source_key"] for r in records}),
        "unique_case_variant_ids": len({r["case_variant_id"] for r in records}),
        "unique_semantic_findings": len({r["independent_semantic_finding"] for r in records}),
        "audit_outcomes": dict(outcomes),
        "effective_classification": dict(classes),
        "source_conflict_count": conflicts,
        "source_hashes_unchanged": not any("source hash changed" in f for f in failures),
        "failures": failures,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
