#!/usr/bin/env python3
"""Read-only structural, source-identity, and anti-template candidate checks."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import openpyxl


ROOT = Path(__file__).resolve().parents[3]
WORKSPACE = ROOT / "gpt-review" / "v3-1-full-3112"
MANIFEST_PATH = WORKSPACE / "SELECTION_MANIFEST.json"
PROGRESS_PATH = WORKSPACE / "PROGRESS.json"
RECORDS_PATH = WORKSPACE / "REVIEW_RECORDS"
XLSX = ROOT / "data" / "REVISED_commands_merged_with_raw.xlsx"
EXPECTED_SOURCE_HASH = "e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8"
CLASSES = {
    "FULLY AUTOMATABLE",
    "REQUIRES PACKAGE / USER CONFIRMATION",
    "MANUAL ONLY",
    "BLOCKED",
}
OUTCOMES = {
    "KEEP",
    "IMPROVED",
    "RECLASSIFIED",
    "SOURCE_CONFLICT",
    "NEED_ENGINEER_DECISION",
}
SECOND_REVIEW_OUTCOMES = {"AGREE", "IMPROVED", "CHANGED", "BLOCKED", "UNRESOLVED"}
REQUIRED_FIELDS = {
    "schema_version",
    "review_sequence",
    "library_sequence",
    "source_key",
    "case_variant_id",
    "source_ref",
    "source_integrity",
    "source_snapshot",
    "historical_reviews",
    "original_test_intent",
    "original_method",
    "automation_classification",
    "execution_readiness",
    "execution_status",
    "tool_result",
    "engineer_verdict",
    "manual_activity",
    "required_inputs",
    "safety_requirements",
    "agent_execution_scope",
    "engineer_actions",
    "command_applicability",
    "modernized_recommendation",
    "project_override_considerations",
    "expected_evidence",
    "source_conflict_analysis",
    "blocked_analysis",
    "review_improvement",
    "independent_technical_reasoning",
    "source_provenance",
    "no_automatic_retry",
    "review_outcome",
    "second_review_outcome",
    "regression_result",
    "per_case_quality_gate",
}
ANTI_TEMPLATE_FIELDS = (
    "original_test_intent",
    "manual_activity",
    "review_improvement",
    "independent_technical_reasoning",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []
    if sha256(XLSX) != EXPECTED_SOURCE_HASH:
        failures.append("immutable XLSX hash changed")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    progress = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
    cases = manifest["cases"]
    if len(cases) != 3112:
        failures.append(f"manifest count is {len(cases)}, expected 3112")
    by_key = {case["source_key"]: case for case in cases}
    if len(by_key) != 3112:
        failures.append("manifest source keys are not unique")
    if len({case["case_variant_id"] for case in cases}) != 3112:
        failures.append("manifest case variants are not unique")

    workbook = openpyxl.load_workbook(XLSX, read_only=True, data_only=False)
    direct_keys: list[str] = []
    for sheet_name in workbook.sheetnames:
        rows = workbook[sheet_name].iter_rows(values_only=True)
        next(rows)
        for physical_row, values in enumerate(rows, start=2):
            direct_keys.append(f"{sheet_name}|{physical_row}|{str(values[0] or '').strip()}")
    if direct_keys != [case["source_key"] for case in cases]:
        failures.append("manifest order or source identity differs from direct XLSX order")

    record_files = sorted(RECORDS_PATH.glob("*.json")) if RECORDS_PATH.exists() else []
    records: list[dict[str, Any]] = []
    seen_keys: set[str] = set()
    seen_variants: set[str] = set()
    seen_sequences: set[int] = set()
    repeated: dict[str, defaultdict[str, list[str]]] = {
        field: defaultdict(list) for field in ANTI_TEMPLATE_FIELDS
    }
    for path in record_files:
        record = json.loads(path.read_text(encoding="utf-8"))
        records.append(record)
        missing = sorted(REQUIRED_FIELDS - set(record))
        if missing:
            failures.append(f"{path.name}: missing fields {missing}")
        key = record.get("source_key")
        variant = record.get("case_variant_id")
        sequence = record.get("review_sequence")
        if key in seen_keys:
            failures.append(f"duplicate record source key: {key}")
        if variant in seen_variants:
            failures.append(f"duplicate record case variant: {variant}")
        if sequence in seen_sequences:
            failures.append(f"duplicate record review sequence: {sequence}")
        seen_keys.add(key)
        seen_variants.add(variant)
        seen_sequences.add(sequence)
        manifest_case = by_key.get(key)
        if not manifest_case:
            failures.append(f"{path.name}: source key not in manifest")
        else:
            if manifest_case["review_status"] != "PENDING_FULL_REVIEW":
                failures.append(f"{path.name}: overwrites a completed baseline case")
            if variant != manifest_case["case_variant_id"]:
                failures.append(f"{path.name}: case variant mismatch")
            integrity = record.get("source_integrity", {})
            if integrity.get("original_row_sha256") != manifest_case["original_row_sha256"]:
                failures.append(f"{path.name}: original row hash mismatch")
        if record.get("automation_classification") not in CLASSES:
            failures.append(f"{path.name}: invalid automation classification")
        if record.get("review_outcome") not in OUTCOMES:
            failures.append(f"{path.name}: invalid review outcome")
        if record.get("second_review_outcome") not in SECOND_REVIEW_OUTCOMES:
            failures.append(f"{path.name}: invalid second-review outcome")
        if record.get("execution_status") != "NOT EXECUTED":
            failures.append(f"{path.name}: review task must remain NOT EXECUTED")
        if record.get("tool_result") != "NOT RUN":
            failures.append(f"{path.name}: review task must keep tool result NOT RUN")
        if record.get("engineer_verdict") != "ENGINEER OWNED; PENDING":
            failures.append(f"{path.name}: engineer verdict boundary changed")
        quality = record.get("per_case_quality_gate", {})
        for flag in (
            "exact_xlsx_row_read",
            "deepseek_same_row_read",
            "gpt_v2_read",
            "history_searched",
            "reasoning_is_case_specific",
            "source_identity_verified",
            "no_hardware_pass_claimed",
        ):
            if quality.get(flag) is not True:
                failures.append(f"{path.name}: failed quality gate {flag}")
        for field in ANTI_TEMPLATE_FIELDS:
            value = record.get(field)
            normalized = json.dumps(value, sort_keys=True, ensure_ascii=False)
            repeated[field][normalized].append(str(key))

    expected_sequences = list(range(201, 201 + len(records)))
    if sorted(seen_sequences) != expected_sequences:
        failures.append("new review sequences are not contiguous from 201")
    if progress["new_full_review_records_count"] != len(records):
        failures.append("progress new-record count does not match record files")
    if progress["completed_count"] != 200 + len(records):
        failures.append("progress completed count does not match baseline plus new records")
    if progress["remaining_count"] != 2912 - len(records):
        failures.append("progress remaining count is inconsistent")

    for field, groups in repeated.items():
        for keys in groups.values():
            if len(keys) > 1:
                warnings.append(f"exact duplicate {field}: {keys}")

    result = {
        "status": "PASS" if not failures else "FAIL",
        "manifest_count": len(cases),
        "completed_baseline_count": 200,
        "new_record_count": len(records),
        "effective_completed_count": 200 + len(records),
        "remaining_count": 2912 - len(records),
        "new_classification": dict(Counter(r.get("automation_classification") for r in records)),
        "new_blocked_count": sum(r.get("automation_classification") == "BLOCKED" for r in records),
        "new_source_conflict_count": sum(bool(r.get("source_conflict_analysis", {}).get("is_source_conflict")) for r in records),
        "anti_template_exact_duplicate_candidates": warnings,
        "failures": failures,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
