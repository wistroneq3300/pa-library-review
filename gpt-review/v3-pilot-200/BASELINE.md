# V3 Pilot Baseline

Captured: 2026-10-13 (Asia/Taipei)

## Git baseline

- Repository: `https://github.com/wistroneq3300/pa-library-review`
- Fetch result: `origin/main` remained at the supplied baseline; no newer
  upstream commit was present.
- Baseline commit: `770c2bd81d329414f308999faa55d20212210fab`
- Baseline commit date: `2026-10-04T18:55:10+08:00`
- Subject: `Add GPT merged testcase library`
- Working branch: `codex/testcase-review-v3-pilot-200`
- Baseline source delta: none for the original XLSX, DeepSeek JSON, GPT V2
  overlay, or merged preview.

## Immutable source hashes

| File | SHA-256 |
| --- | --- |
| `data/REVISED_commands_merged_with_raw.xlsx` | `e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8` |
| `data/tests.json` | `5eefd664be9ed794e4429095f9d8e0c969d392a688b787af71f4f319526fdd37` |
| `data/tests_gpt_merged.json` | `34d0133ce0bab7647179f9822174838ecdfd5ee90e766eb9802eb8672dcfe4a2` |
| `gpt-review/test_gpt_review.json` | `5776cf96ff65219ca8d0dce07631914a9f45a98c0bccae8390f076ec67e25869` |
| `gpt-review/BLOCKED_FEEDBACK_REREVIEW_001.json` | `66a8045c82cb216a33de3501e4408242e5bd35721e1240896b78f113b4931b5f` |
| `gpt-review/BLOCKED_FEEDBACK_REREVIEW_002.json` | `f38bdcae8bbf247911acdbe99da653f9e9e357eda12a717021bc2375899f5907` |
| `gpt-review/blocked_re_reviews_001.json` | `57273bc1c1aa1705bd90e68b35d5ed5435bd044f7db9ad11adb306ec94af9733` |

## Workbook structure

The source workbook contains 3,112 data rows across six sheets:

| Sheet | Data rows |
| --- | ---: |
| Functionality | 2,291 |
| Reliability | 202 |
| Performance | 60 |
| Compatibility | 459 |
| Stability | 88 |
| (No Main Function) | 12 |

All sheets use the same 18-column layout. The original fields are columns 1-12
and the historical DeepSeek review is columns 13-18. V3 does not write to any
of those cells.

## Historical V2 population

`gpt-review/test_gpt_review.json` contains 3,112 historical GPT records. Its
classification field includes 23 legacy aliases (`REQUIRES PACKAGE` and
`USER CONFIRMATION`) in addition to the four current canonical labels. V3
normalizes aliases only in its own analysis; it does not modify V2 history.

No DUT, PA Cycle Lab, OpenHands system, vLLM service, or production test
library is in scope for mutation or execution.
