# V3.1 Quality Summary — 200 Cases

## Completion and integrity

- Records: 200/200
- Unique source keys: 200
- Unique case variants: 200
- Manifest sequence mismatches: 0
- Direct XLSX row/hash/code mismatches: 0
- JSON/schema validation failures: 0
- Original source/V2/V3-history files modified: 0

## V3.1 result distribution

- KEEP: 175
- IMPROVED: 22
- RECLASSIFIED: 3
- FULLY AUTOMATABLE: 12
- REQUIRES PACKAGE / USER CONFIRMATION: 132
- MANUAL ONLY: 34
- BLOCKED: 22
- SOURCE_CONFLICT: 58 (V3: 80)
- NEEDS_ENGINEER_DECISION: 6

## Independent-case quality checks

- Exact duplicate `original_test_intent`: 0 groups
- Exact duplicate `review_improvement`: 0 groups
- Exact duplicate `safety_boundaries`: 0 groups
- Exact duplicate `expected_evidence`: 0 groups
- Case-specific direct re-review: XLSX, DeepSeek, GPT V2 and V3 flags true in all 200 records

Early short-form safety/evidence notes that were textually identical were expanded with device-, operation- and evidence-specific boundaries before release. Programs performed integrity and duplicate checks only; they did not assign conclusions.

## Technical calibration

- Machine Time-only false conflicts were removed in 22 individually identified cases without changing Procedure duration.
- Genuine title/procedure, command/intent, workload or transport conflicts remain.
- BLOCKED stayed at 22; no safety condition was relaxed to improve statistics.
- Three classifications changed: cases 9, 10 and 76.
- All material high-risk changes and representative other changes received a 25-case context-isolated same-model-family understanding pass; this is not cross-model validation.
- No DUT was connected and no test was executed.
