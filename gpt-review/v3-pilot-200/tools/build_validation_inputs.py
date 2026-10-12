#!/usr/bin/env python3
"""Build contract-only inputs for isolated agent-understanding validation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "REVIEW_RECORDS"
OUTPUT_DIR = ROOT / "VALIDATION_INPUTS"
DEFAULT_OUTPUT = OUTPUT_DIR / "CALIBRATION_20_CONTRACTS.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int)
    parser.add_argument("--end", type=int)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if (args.start is None) != (args.end is None):
        raise SystemExit("--start and --end must be supplied together")
    output = args.output or DEFAULT_OUTPUT
    contracts = []
    for path in sorted(RECORDS.glob("*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if args.start is None:
            if not record.get("calibration"):
                continue
        elif not args.start <= record["sequence"] <= args.end:
            continue
        contracts.append(
            {
                "sequence": record["sequence"],
                "source_key": record["source_key"],
                "contract": record["revision_candidate"],
            }
        )
    contracts.sort(key=lambda item: item["sequence"])
    expected = (
        list(range(1, 21))
        if args.start is None
        else list(range(args.start, args.end + 1))
    )
    if [item["sequence"] for item in contracts] != expected:
        raise SystemExit(f"Contract sequences do not match expected range: {expected}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
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
    print(f"wrote {output} with {len(contracts)} contracts")


if __name__ == "__main__":
    main()
