#!/usr/bin/env python3
"""Build a GPT-active testcase library without changing either source JSON.

The output keeps the sheet/item layout and original testcase fields from
data/tests.json.  The prior AI fields are moved into previous_ai_review, and
the normalized GPT second review becomes the active ai_review.
"""

from __future__ import annotations

import copy
import datetime as dt
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TESTS_PATH = ROOT / "data" / "tests.json"
GPT_REVIEW_PATH = ROOT / "gpt-review" / "test_gpt_review.json"
OUTPUT_PATH = ROOT / "data" / "tests_gpt_merged.json"

OLD_AI_KEYS = (
    "ai_can_execute",
    "ai_packages_needed",
    "ai_commands",
    "ai_logs_output",
    "risk",
    "remark",
)

LIST_FIELDS = {
    "preconditions",
    "pre_check_commands",
    "safety_checks",
    "required_packages",
    "risk_notes",
    "expected_evidence",
    "post_check_commands",
    "logs_to_collect",
    "blocked_conditions",
    "manual_steps",
    "end_user_decides",
}

CANONICAL_CLASSIFICATIONS = {
    "FULLY AUTOMATABLE",
    "REQUIRES PACKAGE / USER CONFIRMATION",
    "MANUAL ONLY",
    "BLOCKED",
}

CLASSIFICATION_ALIASES = {
    "USER CONFIRMATION": "REQUIRES PACKAGE / USER CONFIRMATION",
    "REQUIRES PACKAGE": "REQUIRES PACKAGE / USER CONFIRMATION",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_source_ref(value: object) -> dict[str, object]:
    if isinstance(value, dict):
        sheet = value.get("sheet")
        source_row = value.get("source_row")
    elif isinstance(value, str):
        match = re.match(
            r"@\{sheet=([^;]+);\s*source_row=(\d+)(?:;[^}]*)?\}", value.strip()
        )
        if not match:
            raise ValueError(f"Unrecognized source_ref: {value!r}")
        sheet, source_row = match.group(1), match.group(2)
    else:
        raise TypeError(f"source_ref must be an object or string, got {type(value)}")

    if not isinstance(sheet, str) or not sheet:
        raise ValueError(f"Invalid source_ref sheet: {sheet!r}")
    try:
        row_number = int(source_row)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid source_ref row: {source_row!r}") from exc
    if row_number < 2:
        raise ValueError(f"Invalid testcase source row: {row_number}")
    return {"sheet": sheet, "source_row": row_number}


def normalize_list(value: object, field: str) -> list[object]:
    if isinstance(value, list):
        return copy.deepcopy(value)
    if value is None:
        return []
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return []
        if field == "end_user_decides":
            decisions = re.findall(r"PASS|FAIL|BLOCKED", text.upper())
            if decisions:
                return list(dict.fromkeys(decisions))
        return [text]
    return [copy.deepcopy(value)]


def normalize_gpt_case(case: dict[str, object]) -> tuple[dict[str, object], bool]:
    result: dict[str, object] = {"provider": "gpt-second-review"}
    source_ref = parse_source_ref(case.get("source_ref"))
    result["source_ref"] = source_ref

    original_classification = str(case.get("automation_classification", "")).strip()
    classification = CLASSIFICATION_ALIASES.get(
        original_classification, original_classification
    )
    if classification not in CANONICAL_CLASSIFICATIONS:
        raise ValueError(
            f"Unsupported automation_classification {original_classification!r} "
            f"for {case.get('code')!r}"
        )
    result["automation_classification"] = classification
    classification_changed = classification != original_classification
    if classification_changed:
        result["source_automation_classification"] = original_classification

    for key, value in case.items():
        if key in {
            "code",
            "source_ref",
            "automation_classification",
            "deepseek_original_review",
        }:
            continue
        if key in LIST_FIELDS:
            result[key] = normalize_list(value, key)
        else:
            result[key] = copy.deepcopy(value)

    return result, classification_changed


def main() -> None:
    source_hashes_before = {
        "tests_json_sha256": sha256(TESTS_PATH),
        "gpt_review_json_sha256": sha256(GPT_REVIEW_PATH),
    }

    tests = json.loads(TESTS_PATH.read_text(encoding="utf-8"))
    gpt_review = json.loads(GPT_REVIEW_PATH.read_text(encoding="utf-8"))

    cases = gpt_review.get("cases")
    if not isinstance(cases, list):
        raise ValueError("GPT review must contain a cases array")

    gpt_index: dict[tuple[str, int, str], dict[str, object]] = {}
    for case in cases:
        if not isinstance(case, dict):
            raise TypeError("Every GPT case must be an object")
        source_ref = parse_source_ref(case.get("source_ref"))
        code = str(case.get("code", "")).strip()
        key = (str(source_ref["sheet"]), int(source_ref["source_row"]), code)
        if not code:
            raise ValueError(f"GPT case has no code at {source_ref}")
        if key in gpt_index:
            raise ValueError(f"Duplicate GPT source key: {key}")
        gpt_index[key] = case

    output = copy.deepcopy(tests)
    output["schema_version"] = "tests-gpt-merged-v1"
    output["generated_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    output["active_ai_review"] = "gpt-second-review"

    used_keys: set[tuple[str, int, str]] = set()
    normalized_string_records = 0
    normalized_classifications = 0
    merged_count = 0

    sheets = output.get("sheets")
    if not isinstance(sheets, dict):
        raise ValueError("tests.json must contain a sheets object")

    for sheet in sheets.values():
        if not isinstance(sheet, dict):
            raise TypeError("Every sheet must be an object")
        sheet_name = str(sheet.get("name", ""))
        items = sheet.get("items")
        if not isinstance(items, list):
            raise ValueError(f"Sheet {sheet_name!r} has no items array")

        for source_row, item in enumerate(items, start=2):
            if not isinstance(item, dict):
                raise TypeError(f"{sheet_name} row {source_row} is not an object")
            code = str(item.get("code", "")).strip()
            key = (sheet_name, source_row, code)
            case = gpt_index.get(key)
            if case is None:
                raise KeyError(f"No GPT review for source testcase {key}")

            previous_ai_review = {
                "provider": "deepseek",
                **{name: copy.deepcopy(item[name]) for name in OLD_AI_KEYS if name in item},
            }
            for name in OLD_AI_KEYS:
                item.pop(name, None)

            active_review, classification_changed = normalize_gpt_case(case)
            if classification_changed:
                normalized_classifications += 1
            if any(
                isinstance(case.get(field), str)
                for field in LIST_FIELDS | {"source_ref", "deepseek_original_review"}
            ):
                normalized_string_records += 1

            item["ai_review"] = active_review
            item["previous_ai_review"] = previous_ai_review
            used_keys.add(key)
            merged_count += 1

    unused_keys = set(gpt_index) - used_keys
    if unused_keys:
        sample = sorted(unused_keys)[:10]
        raise ValueError(f"Unmatched GPT cases: {sample} (total {len(unused_keys)})")
    if merged_count != tests.get("total") or merged_count != len(cases):
        raise ValueError(
            f"Count mismatch: merged={merged_count}, tests_total={tests.get('total')}, "
            f"gpt_cases={len(cases)}"
        )

    output["merge_metadata"] = {
        "source_tests_json": str(TESTS_PATH.relative_to(ROOT)).replace("\\", "/"),
        "source_gpt_review_json": str(GPT_REVIEW_PATH.relative_to(ROOT)).replace(
            "\\", "/"
        ),
        **source_hashes_before,
        "join_key": ["sheet", "source_row", "code"],
        "merged_case_count": merged_count,
        "normalized_string_record_count": normalized_string_records,
        "normalized_classification_count": normalized_classifications,
        "classification_aliases": CLASSIFICATION_ALIASES,
        "source_generated_at": tests.get("generated_at"),
    }

    OUTPUT_PATH.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    source_hashes_after = {
        "tests_json_sha256": sha256(TESTS_PATH),
        "gpt_review_json_sha256": sha256(GPT_REVIEW_PATH),
    }
    if source_hashes_after != source_hashes_before:
        OUTPUT_PATH.unlink(missing_ok=True)
        raise RuntimeError("A source JSON changed during the merge; output was removed")

    print(
        json.dumps(
            {
                "output": str(OUTPUT_PATH),
                "merged_case_count": merged_count,
                "normalized_string_record_count": normalized_string_records,
                "normalized_classification_count": normalized_classifications,
                "output_sha256": sha256(OUTPUT_PATH),
                "source_hashes_unchanged": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
