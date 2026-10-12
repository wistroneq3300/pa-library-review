#!/usr/bin/env python3
"""List historical V2 rows for manual V3 sampling; never decides a verdict."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
GPT_V2 = ROOT / "gpt-review" / "test_gpt_review.json"


def parse_ref(value: Any) -> tuple[str | None, int | None]:
    if isinstance(value, dict):
        return value.get("sheet"), int(value.get("source_row"))
    if isinstance(value, str):
        match = re.match(r"@\{sheet=(.*?);\s*source_row=(\d+)(?:;.*?)?\}", value)
        if match:
            return match.group(1), int(match.group(2))
    return None, None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sheet")
    parser.add_argument("--classification")
    parser.add_argument("--risk")
    parser.add_argument("--text")
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    cases = json.loads(GPT_V2.read_text(encoding="utf-8"))["cases"]
    selected = []
    summary: Counter[tuple[str | None, str | None]] = Counter()
    pattern = re.compile(args.text, re.IGNORECASE) if args.text else None
    for case in cases:
        sheet, row = parse_ref(case.get("source_ref"))
        summary[(sheet, case.get("automation_classification"))] += 1
        if args.sheet and sheet != args.sheet:
            continue
        if args.classification and case.get("automation_classification") != args.classification:
            continue
        if args.risk and case.get("risk_level") != args.risk:
            continue
        searchable = " ".join(
            str(case.get(key, ""))
            for key in ("code", "test_name", "purpose", "test_command")
        )
        if pattern and not pattern.search(searchable):
            continue
        selected.append(
            {
                "sheet": sheet,
                "source_row": row,
                "code": case.get("code"),
                "test_name": case.get("test_name"),
                "automation_classification": case.get("automation_classification"),
                "second_review_outcome": case.get("second_review_outcome"),
                "risk_level": case.get("risk_level"),
                "destructive_actions": case.get("destructive_actions"),
            }
        )
        if len(selected) >= args.limit:
            break
    if args.summary:
        print(
            json.dumps(
                [
                    {"sheet": key[0], "automation_classification": key[1], "count": count}
                    for key, count in sorted(summary.items(), key=lambda item: str(item[0]))
                ],
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(json.dumps(selected, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
