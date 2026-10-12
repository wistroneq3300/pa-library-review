#!/usr/bin/env python3
"""Build contract-only inputs for independent agent-understanding validation."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "REVIEW_RECORDS"
OUTPUT_DIR = ROOT / "VALIDATION_INPUTS"
OUTPUT = OUTPUT_DIR / "CALIBRATION_20_CONTRACTS.json"


def main() -> None:
    contracts = []
    for path in sorted(RECORDS.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if not record.get("calibration"):
            continue
        contracts.append(
            {
                "sequence": record["sequence"],
                "source_key": record["source_key"],
                "contract": record["revision_candidate"],
            }
        )
    contracts.sort(key=lambda item: item["sequence"])
    if [item["sequence"] for item in contracts] != list(range(1, 21)):
        raise SystemExit("Calibration contracts are not exactly sequences 1 through 20")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "schema_version": "agent-understanding-input-1.0",
                "input_boundary": "revision_candidate only; reviewer findings and source snapshots excluded",
                "cases": contracts,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT} with {len(contracts)} contracts")


if __name__ == "__main__":
    main()
