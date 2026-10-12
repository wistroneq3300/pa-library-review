#!/usr/bin/env python3
"""Mechanical integrity checks; this does not claim semantic review quality."""

from __future__ import annotations

import argparse
import hashlib
import json
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGAL_CLASSES = {
    "FULLY AUTOMATABLE",
    "REQUIRES PACKAGE / USER CONFIRMATION",
    "MANUAL ONLY",
    "BLOCKED",
}
LEGAL_OUTCOMES = {
    "KEEP",
    "IMPROVED",
    "RECLASSIFIED",
    "REWRITE_REQUIRED",
    "SOURCE_CONFLICT",
    "NEED_ENGINEER_DECISION",
}
LEGAL_READINESS = {
    "READY",
    "NEEDS_INPUT",
    "NEEDS_SPEC",
    "NEEDS_PACKAGE",
    "NEEDS_APPROVAL",
    "NEEDS_MANUAL_ACTION",
    "SOURCE_CONFLICT",
    "NOT_APPLICABLE",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    args = parser.parse_args()

    manifest = json.loads((ROOT / "SELECTION_MANIFEST.json").read_text(encoding="utf-8"))
    paths = sorted((ROOT / "REVIEW_RECORDS").glob("*.json"))
    records = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    errors: list[str] = []
    warnings: list[str] = []

    if len(records) != args.count:
        errors.append(f"record count {len(records)} != expected {args.count}")
    sequences = [record.get("sequence") for record in records]
    if sequences != list(range(1, args.count + 1)):
        errors.append(f"sequence mismatch: {sequences}")
    keys = [record.get("source_key") for record in records]
    if len(set(keys)) != len(keys):
        errors.append("duplicate source_key detected")
    variants = [record.get("case_variant_id") for record in records]
    if len(set(variants)) != len(variants):
        errors.append("duplicate case_variant_id detected")

    selected = manifest["cases"][: args.count]
    for record, selected_case in zip(records, selected):
        expected_key = (
            f"{selected_case['sheet']}|{selected_case['source_row']}|{selected_case['code']}"
        )
        if record.get("source_key") != expected_key:
            errors.append(
                f"sequence {record.get('sequence')} source mismatch: "
                f"{record.get('source_key')} != {expected_key}"
            )
        if record.get("case_variant_id") != selected_case.get("case_variant_id"):
            errors.append(f"sequence {record.get('sequence')} variant mismatch")
        conclusion = record.get("v3_review_conclusion", {})
        if conclusion.get("automation_classification") not in LEGAL_CLASSES:
            errors.append(f"sequence {record.get('sequence')} illegal classification")
        if conclusion.get("review_outcome") not in LEGAL_OUTCOMES:
            errors.append(f"sequence {record.get('sequence')} illegal outcome")
        illegal_readiness = set(conclusion.get("execution_readiness", [])) - LEGAL_READINESS
        if illegal_readiness:
            errors.append(
                f"sequence {record.get('sequence')} illegal readiness {sorted(illegal_readiness)}"
            )
        for required in (
            "original_test_intent",
            "v2_review_conclusion",
            "revision_candidate",
            "objective_improvement_over_v2",
            "per_case_integrity_check",
        ):
            if not record.get(required):
                errors.append(f"sequence {record.get('sequence')} missing {required}")
        if record.get("regression_status", {}).get("hardware_tested") is not False:
            errors.append(f"sequence {record.get('sequence')} hardware_tested is not false")
        if record.get("regression_status", {}).get("pass_claimed") is not False:
            errors.append(f"sequence {record.get('sequence')} pass_claimed is not false")

    exact_reason_groups: dict[str, list[int]] = {}
    for record in records:
        reason = record.get("reason_for_change", "").strip().lower()
        exact_reason_groups.setdefault(reason, []).append(record["sequence"])
    for reason, seqs in exact_reason_groups.items():
        if reason and len(seqs) > 1:
            errors.append(f"exact duplicate reason_for_change at {seqs}")

    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            a = left.get("objective_improvement_over_v2", "")
            b = right.get("objective_improvement_over_v2", "")
            ratio = SequenceMatcher(None, a, b).ratio()
            if ratio >= 0.85:
                warnings.append(
                    f"high objective similarity {ratio:.3f}: "
                    f"{left['sequence']} vs {right['sequence']}"
                )

    source_hashes = {
        "xlsx": sha256(ROOT.parents[1] / "data" / "REVISED_commands_merged_with_raw.xlsx"),
        "tests_json": sha256(ROOT.parents[1] / "data" / "tests.json"),
        "gpt_v2": sha256(ROOT.parent / "test_gpt_review.json"),
    }
    expected_hashes = json.loads((ROOT / "PROGRESS.json").read_text(encoding="utf-8"))[
        "immutable_source_sha256"
    ]
    if source_hashes != expected_hashes:
        errors.append(f"immutable source hash mismatch: {source_hashes}")

    output = {
        "checked_count": len(records),
        "expected_count": args.count,
        "unique_source_keys": len(set(keys)),
        "unique_case_variant_ids": len(set(variants)),
        "source_hashes": source_hashes,
        "errors": errors,
        "warnings": warnings,
        "status": "PASS" if not errors else "FAIL",
        "semantic_validation_claimed": False,
    }
    print(json.dumps(output, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
