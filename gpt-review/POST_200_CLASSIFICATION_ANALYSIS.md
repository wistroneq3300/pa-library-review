# Post-200 Classification Analysis

## Scope

This analysis covers the 200 overlay records currently reviewed in
`gpt-review/test_gpt_review.json`. The records map to the `Functionality`
sheet source rows 2 through 200. The original XLSX and `data/tests.json` are
unchanged.

Source integrity hashes at the end of the 200th review remain:

- XLSX: `e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8`
- `tests.json`: `5eefd664be9ed794e4429095f9d8e0c969d392a688b787af71f4f319526fdd37`

## Automation Classification

| Classification | Count |
|---|---:|
| `FULLY AUTOMATABLE` | 0 |
| `REQUIRES PACKAGE / USER CONFIRMATION` | 80 |
| `MANUAL ONLY` | 80 |
| `BLOCKED` | 40 |
| **Total** | **200** |

The absence of `FULLY AUTOMATABLE` is a finding, not a default. The reviewed
cases either require physical observation, licensed or platform-specific
packages, explicit operator confirmation, or lack enough specification to
define a safe executable procedure.

## PA Manager Display

| Display | Count |
|---|---:|
| `YES` | 3 |
| `PARTIAL` | 87 |
| `NO` | 110 |
| **Total** | **200** |

## DeepSeek Reference Field

The nested `deepseek_original_review.ai_can_execute` field is reference data
only and was not copied into the GPT decision.

| DeepSeek value | Count |
|---|---:|
| `YES` | 16 |
| `PARTIAL` | 77 |
| `NO` | 107 |
| **Total** | **200** |

## Risk and Approval Signals

| Field/value | Count |
|---|---:|
| `risk_level = CRITICAL` | 71 |
| `risk_level = HIGH` | 97 |
| `risk_level = MEDIUM` | 31 |
| `risk_level = LOW` | 1 |
| `destructive_actions = true` | 95 |
| `requires_human_approval = true` | 200 |

These fields are independent of the automation classification. A case can be
technically package-executable while still requiring human approval because it
changes firmware, power, network identity, storage, or recovery state.

## BLOCKED Population

There are 40 BLOCKED cases. BLOCKED means the testcase cannot yet be converted
into a safe, deterministic procedure from the available source and reference
material. It is not equivalent to `MANUAL ONLY`, and it is not a statement that
the underlying hardware feature is impossible.

The first blocked cases include:

- `Wistron-HW-00032-V002` CRPS latch offset to next block
- `Wistron-HW-00040-V002` LED behavior from PWM high state
- `Wistron-HW-00045-V002` input power cycling
- `Wistron-HW-00056-V002` APP_PROFILE_SUPPORT capability reporting
- `Wistron-HW-00070-V002` firmware upgrade/downgrade
- `Wistron-HW-00153-V002` OS installing
- `Wistron-HW-00207-V002` serial communication
- `Wistron-HW-00208-V002` BIOS update
- `Wistron-HW-00209-V002` BMC update
- `Wistron-HW-00210-V002` device detection

## Interpretation

The dominant blockers are missing identity and acceptance criteria, missing
vendor-specific operation details, missing package/image dependencies, and
missing safety or recovery definitions. The next phase therefore starts with
representative cases across configuration, firmware, OS installation, serial
I/O, and device enumeration. Each selected case is re-read independently and
its result is stored outside the original 200-record overlay.
