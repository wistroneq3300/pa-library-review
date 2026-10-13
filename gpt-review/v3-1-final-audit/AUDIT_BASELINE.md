# V3.1 Final Audit Baseline

Audit date: 2026-10-13

## Git baseline

- Repository: `https://github.com/wistroneq3300/pa-library-review`
- Fetched branch: `origin/codex/testcase-review-v3-1`
- Remote HEAD and local starting commit:
  `f32a3a0cdfb5a82f2e065fb099cfbe09ebcb6981`
- Audit branch: `codex/testcase-review-v3-1-final-audit`
- Fetch result: remote HEAD exactly matched the user-provided commit.
- Starting working tree: clean.
- Previous ignored V3.1 run lock was stale and referred to the completed,
  pushed run. It was visibly replaced by the Final Audit lock; no concurrent
  writer was found.

## Immutable source baseline

| Artifact | SHA-256 |
|---|---|
| `data/REVISED_commands_merged_with_raw.xlsx` | `e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8` |
| `data/tests.json` | `5eefd664be9ed794e4429095f9d8e0c969d392a688b787af71f4f319526fdd37` |
| `data/tests_gpt_merged.json` | `34d0133ce0bab7647179f9822174838ecdfd5ee90e766eb9802eb8672dcfe4a2` |
| `gpt-review/test_gpt_review.json` | `5776cf96ff65219ca8d0dce07631914a9f45a98c0bccae8390f076ec67e25869` |
| V3 Pilot Selection Manifest | `55c915d7c91d2e4340353e881a85e1f0ff236f62a858106a19c05751f31a086d` |

## Audit population and method

- The frozen V3 Pilot selection was reused without substitution: exactly 200
  unique source keys and 200 unique `case_variant_id` values.
- Every audit record re-opened the exact XLSX row and compared DeepSeek, GPT
  V2, V3 Pilot and V3.1. The audit records point to both versioned JSON files.
- Programs were used only for workbook extraction, identity/hash verification,
  schema/count validation, similarity candidate discovery and record
  serialization. `independent_semantic_finding` and every override in the
  record materializer are hand-authored audit judgments.
- No DUT, PA Manager, OpenHands, cycle script, package install, firmware action
  or real testcase execution occurred.

## Effective overlay order

The release candidate is interpreted as immutable source and V3 history, then
explicit V3.1 changes, then explicit Final Audit corrections. Omission in a
shorter overlay does not delete a V3 command token, duration, target, safety
boundary, evidence item, stop condition or recovery requirement.

