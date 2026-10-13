# V3.1 Full 3,112-Case Review Baseline

Baseline date: 2026-10-14

## Repository and branch

- Repository: `https://github.com/wistroneq3300/pa-library-review`
- Required Final Audit branch: `origin/codex/testcase-review-v3-1-final-audit`
- Verified remote Final Audit HEAD:
  `f337ec8e0a506e06cbd940d1781e7f484493d43c`
- Full Review branch: `codex/testcase-review-v3-1-full-3112`
- Seq 182 baseline decision commit:
  `510ca6be55cf31c52cdd784c39b54f5edb1b6828`
- The working tree was clean before branch creation. No newer Final Audit
  commit existed after `git fetch origin --prune`.

## Immutable source hashes

| Artifact | SHA-256 |
|---|---|
| `data/REVISED_commands_merged_with_raw.xlsx` | `e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8` |
| `data/tests.json` | `5eefd664be9ed794e4429095f9d8e0c969d392a688b787af71f4f319526fdd37` |
| `data/tests_gpt_merged.json` | `34d0133ce0bab7647179f9822174838ecdfd5ee90e766eb9802eb8672dcfe4a2` |
| `gpt-review/test_gpt_review.json` | `5776cf96ff65219ca8d0dce07631914a9f45a98c0bccae8390f076ec67e25869` |
| V3 Pilot selection manifest | `55c915d7c91d2e4340353e881a85e1f0ff236f62a858106a19c05751f31a086d` |
| Full 3,112-row selection manifest | `1e5a2bd7c4db039c309098529726e0e7ceae1b66aea168f7207ab05fd032c596` |

## Population and identity result

- Total source rows: **3,112**.
- Completed Final Audit baseline: **200**.
- Rows requiring new independent Full Review: **2,912**.
- Source keys: **3,112 unique**.
- `case_variant_id` values: **3,112 unique**.
- All 200 Pilot/Final Audit source keys and variants match the direct XLSX
  identity calculation.
- Full Review order is workbook sheet order and physical source-row order,
  skipping the 200 completed baseline cases. Final Audit sequence remains a
  separate field and is not rewritten.

| Sheet | Source rows |
|---|---:|
| Functionality | 2,291 |
| Reliability | 202 |
| Performance | 60 |
| Compatibility | 459 |
| Stability | 88 |
| (No Main Function) | 12 |

The first unreviewed source row is
`Functionality|3|Wistron-HW-00002-V005`, variant
`c41f3bde2fe9e892`.

## Locked review authority

The controlling order is immutable XLSX source facts, confirmed engineering
decisions including ED-32, Review Logic V3.1 Final Audit, the additive overlay
retention rule, then V3/GPT V2/DeepSeek history as challengeable reference.
No Full Review record may alter this order or create a new global policy.

Seq 182 is locked `MANUAL ONLY`: the engineer physically removes and restores
the AC cable. PDU control, BMC power off, software reboot, and other remote
actions are not equivalent coverage for that case. This is not a global rule
for other AC-cycle cases.

## Review and execution boundary

This task performs static review only. It does not connect to a DUT, execute a
test, install a package, alter firmware, clear logs, or set a formal testcase
verdict. Each new row must be read directly from the XLSX and completed as one
independent record before the next row is opened. Mechanical tools may verify
identity, hashes, schemas, counts, and duplicate-text candidates; they may not
decide intent, classification, readiness, risk, evidence, or recommendations.

Formal testcase content is written in technical English. Progress and handoff
communication to the user is written in Traditional Chinese.

