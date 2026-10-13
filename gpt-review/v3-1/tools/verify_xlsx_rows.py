#!/usr/bin/env python3
"""Read every selected XLSX row and verify it against the frozen V3 record hash.

This utility performs source integrity checks only.  It does not create or
modify review judgments.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import openpyxl


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "gpt-review" / "v3-pilot-200" / "SELECTION_MANIFEST.json"
RECORDS = ROOT / "gpt-review" / "v3-pilot-200" / "REVIEW_RECORDS"
XLSX = ROOT / "data" / "REVISED_commands_merged_with_raw.xlsx"


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    workbook = openpyxl.load_workbook(XLSX, read_only=True, data_only=False)
    mismatches: list[dict[str, object]] = []
    keys: list[str] = []
    for entry in manifest["cases"]:
        sheet = workbook[entry["sheet"]]
        headers = [cell.value for cell in sheet[1]]
        values = [cell.value for cell in sheet[entry["source_row"]]]
        row = dict(zip(headers, values, strict=True))
        digest = hashlib.sha256(
            json.dumps(
                row,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                default=str,
            ).encode("utf-8")
        ).hexdigest()
        record_path = RECORDS / f"{entry['sequence']:04d}_{entry['case_variant_id']}.json"
        record = json.loads(record_path.read_text(encoding="utf-8"))
        code_ok = str(values[0] or "").strip() == entry["code"]
        hash_ok = digest == record["source_integrity"]["original_row_sha256"]
        if not code_ok or not hash_ok:
            mismatches.append(
                {
                    "sequence": entry["sequence"],
                    "source_key": entry["source_key"],
                    "xlsx_code": values[0],
                    "calculated_sha256": digest,
                    "code_ok": code_ok,
                    "hash_ok": hash_ok,
                }
            )
        keys.append(entry["source_key"])
    print(
        json.dumps(
            {
                "direct_xlsx_rows_read": len(keys),
                "unique_source_keys": len(set(keys)),
                "hash_and_code_matches": len(keys) - len(mismatches),
                "mismatches": mismatches,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
