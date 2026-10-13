#!/usr/bin/env python3
"""Read-only release validator for the V3.1 200-case review artifacts."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
V31 = ROOT / "gpt-review" / "v3-1"
RECORDS = V31 / "REVIEW_RECORDS"
MANIFEST = ROOT / "gpt-review" / "v3-pilot-200" / "SELECTION_MANIFEST.json"
EXPECTED_MANIFEST_SHA256 = "55c915d7c91d2e4340353e881a85e1f0ff236f62a858106a19c05751f31a086d"
VALID_CLASSES = {
    "FULLY AUTOMATABLE",
    "REQUIRES PACKAGE / USER CONFIRMATION",
    "MANUAL ONLY",
    "BLOCKED",
}
REQUIRED = {
    "source_key",
    "case_variant_id",
    "source_ref",
    "source_integrity",
    "original_test_intent",
    "original_procedure_criteria",
    "historical_reviews",
    "v3_1_conclusion",
    "applicable_engineering_decisions",
    "master_vs_project_parameters",
    "original_method",
    "modernized_recommendation",
    "missing_inputs",
    "safety_boundaries",
    "expected_evidence",
    "no_automatic_retry",
    "engineer_owned_verdict",
    "review_improvement",
    "regression_result",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    failures: list[str] = []
    if sha256(MANIFEST) != EXPECTED_MANIFEST_SHA256:
        failures.append("canonical selection manifest hash changed")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    files = sorted(RECORDS.glob("*.json"))
    records = []
    for path in files:
        try:
            records.append(json.loads(path.read_text(encoding="utf-8")))
        except Exception as exc:  # explicit release diagnostic
            failures.append(f"{path.name}: invalid JSON: {exc}")

    if len(files) != 200 or len(records) != 200:
        failures.append(f"expected 200 parseable records, found {len(files)}/{len(records)}")

    records.sort(key=lambda item: item.get("sequence", -1))
    expected_sequences = list(range(1, 201))
    if [item.get("sequence") for item in records] != expected_sequences:
        failures.append("record sequences are not exactly 1..200")

    source_keys = [item.get("source_key") for item in records]
    variants = [item.get("case_variant_id") for item in records]
    if len(set(source_keys)) != 200:
        failures.append("source keys are not unique")
    if len(set(variants)) != 200:
        failures.append("case_variant_id values are not unique")

    for expected, record in zip(manifest["cases"], records):
        seq = record.get("sequence")
        missing = sorted(REQUIRED - set(record))
        if missing:
            failures.append(f"sequence {seq}: missing fields {missing}")
        for key in ("sequence", "source_key", "case_variant_id"):
            if record.get(key) != expected.get(key):
                failures.append(f"sequence {seq}: manifest mismatch for {key}")
        ref = record.get("source_ref", {})
        for key in ("sheet", "source_row", "code"):
            if ref.get(key) != expected.get(key):
                failures.append(f"sequence {seq}: source_ref mismatch for {key}")
        integrity = record.get("source_integrity", {})
        for key in ("exact_xlsx_row_read", "deepseek_row_read", "gpt_v2_read", "v3_record_read"):
            if integrity.get(key) is not True:
                failures.append(f"sequence {seq}: source_integrity.{key} is not true")
        conclusion = record.get("v3_1_conclusion", {})
        if conclusion.get("automation_classification") not in VALID_CLASSES:
            failures.append(f"sequence {seq}: invalid automation classification")
        regression = record.get("regression_result", {})
        if regression.get("status") not in {"PASS", "PASS_WITH_SOURCE_CONFLICT"}:
            failures.append(f"sequence {seq}: invalid regression status")
        for key in ("intent_preserved", "original_command_preserved"):
            if regression.get(key) is not True:
                failures.append(f"sequence {seq}: regression {key} is not true")
        for key in ("coverage_regression", "safety_regression", "pass_claimed", "hardware_tested"):
            if regression.get(key) is not False:
                failures.append(f"sequence {seq}: regression {key} is not false")

    classes = Counter(item["v3_1_conclusion"]["automation_classification"] for item in records)
    outcomes = Counter(item["v3_1_conclusion"]["review_outcome"] for item in records)
    source_conflicts = sum(
        "SOURCE_CONFLICT" in item["v3_1_conclusion"].get("execution_readiness", [])
        for item in records
    )
    summary = {
        "status": "PASS" if not failures else "FAIL",
        "record_count": len(records),
        "unique_source_keys": len(set(source_keys)),
        "unique_case_variant_ids": len(set(variants)),
        "manifest_mismatches": sum("manifest mismatch" in item for item in failures),
        "automation_classification": dict(sorted(classes.items())),
        "review_outcome": dict(sorted(outcomes.items())),
        "source_conflict_count": source_conflicts,
        "failures": failures,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
