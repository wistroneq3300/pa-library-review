# V3 versus V3.1 Quality Comparison

## Quantitative result

| Metric | V3 | V3.1 | Objective change |
|---|---:|---:|---|
| FULLY AUTOMATABLE | 12 | 12 | Net zero; case 76 moved in, case 9 moved out. |
| REQUIRES PACKAGE / USER CONFIRMATION | 133 | 132 | Net -1. |
| MANUAL ONLY | 33 | 34 | Net +1 from case 10, where core BIOS/injection activity is operator-owned. |
| BLOCKED | 22 | 22 | No metric-driven deblocking. |
| SOURCE_CONFLICT | 80 | 58 | 22 Machine Time/non-normative false conflicts removed. |
| KEEP | n/a | 175 | V3 retained where already technically correct. |
| IMPROVED | n/a | 22 | Same class but materially clearer engineering boundary. |
| RECLASSIFIED | n/a | 3 | Cases 9, 10 and 76 only. |
| NEEDS_ENGINEER_DECISION readiness | 6 | 6 | Decisions remain explicit; none was fabricated. |

## Classification changes

| Seq | Test case | V3 | V3.1 | Technical reason |
|---:|---|---|---|---|
| 9 | ACPI BERT/ERST/HEST | FULLY AUTOMATABLE | REQUIRES PACKAGE / USER CONFIRMATION | Read-only collection is ready, but platform applicability determines whether absent tables are acceptable; capability and verdict readiness are now explicit. |
| 10 | ECC Leaky Bucket / DIMM_B injection | REQUIRES PACKAGE / USER CONFIRMATION | MANUAL ONLY | Agent log collection does not automate the core BIOS change, physical target selection and hazardous vendor injection. |
| 76 | CPU temperature monitoring | REQUIRES PACKAGE / USER CONFIRMATION | FULLY AUTOMATABLE | Missing platform Expected affects verdict readiness, not safe automated sensor collection. |

## Required 14-point comparison

1. **Automation classification:** only three evidence-backed changes; 197 cases keep their V3 class.
2. **BLOCKED count:** unchanged at 22. Cases 80, 186, 190, 191, 199 and 200 demonstrate true semantic/safety blocks.
3. **SOURCE_CONFLICT:** reduced from 80 to 58. Cases 170–174 and 176–180 remove scheduling-only conflicts; cases 54, 122, 143, 183 and 185 retain genuine conflicts.
4. **Master/project parameter confusion:** cases 2, 6, 17, 18, 155, 176, 178 and 183 now state Master default, approved project run and coverage difference separately.
5. **Machine Time misclassification:** 22 case-specific removals are listed in `SOURCE_CONFLICT_ANALYSIS.md`; source Procedure duration remains unchanged.
6. **Manual preparation versus MANUAL ONLY:** case 10 is MANUAL ONLY because its core BIOS/injection action is manual; cases 17, 185 and 187 remain automatable after human inputs/setup because setup alone does not define capability.
7. **Missing Expected/SPEC:** case 76 becomes FULLY AUTOMATABLE for Actual collection; case 194 remains FULLY AUTOMATABLE. Cases 199/200 stay BLOCKED because intent/target are unknown, not because a numeric Expected is missing.
8. **Legacy tools/commands:** case 193 maps gdsio to version-matched official documentation; cases 195–198 retain WebUI/OEM paths and allow advertised update interfaces only when equivalent; private WAT/MODS semantics are never invented.
9. **Original test purpose:** all 200 records have `intent_preserved=true`; WebUI, BIOS display, network mode and MLPerf model/scenario functions are not substituted.
10. **Original command:** all 200 have `original_command_preserved=true`; malformed or conflicting commands remain in provenance instead of being silently repaired.
11. **Official basis:** public recommendations cite DMTF, NVIDIA, fio, stress-ng and linux-rdma sources; private tools require their actual manuals/SOPs.
12. **Project override boundary:** every record includes Master, project inputs, Actual and coverage difference; no record claims an execution occurred.
13. **Agent understanding:** 25/25 changed cases passed the context-isolated same-family second pass across intent, target, approval, safety, evidence, retry and verdict ownership.
14. **Safety/coverage regression:** 200/200 record gates report no safety or coverage regression. Storage, error injection, power/firmware and environmental cases retain their strict stops.

## Concrete quality improvements

- Case 14 removes a two-person rule not required by engineering, while keeping exact storage identity and protection checks.
- Case 18 no longer blocks on 240-minute Machine Time, yet still retains 12-hour 40C margin coverage.
- Case 54 shows restraint: only the timing error was removed; semantic conflicts keep it BLOCKED.
- Case 76 stops treating provisionable Expected data as a partial-automation requirement.
- Case 122 distinguishes a real QD conflict from a false timing conflict.
- Case 143 retains a real 70/30 versus randwrite conflict rather than suppressing every SOURCE_CONFLICT.
- Case 170 preserves all-slot network coverage and physical fixture control.
- Case 176 makes a shorter approved run auditable without claiming the 24-hour Master requirement.
- Case 185 explicitly separates Ethernet, RoCE and InfiniBand modes.
- Case 193 retains the original gdsio parameters while replacing unsafe path ambiguity with an approved mounted-file requirement.
- Cases 195–198 keep BMC, BIOS downgrade and CPLD component behaviors separate; no generic firmware endpoint is invented.

## Anti-template evidence

- 200 unique source keys and 200 unique `case_variant_id` values.
- Exact duplicate groups: `original_test_intent` 0, `review_improvement` 0, `safety_boundaries` 0, `expected_evidence` 0.
- Every source row was directly reopened and matched by code/hash.
- Programs were used for reading, integrity, duplicate and difference checks only; they did not assign the 200 technical conclusions.
