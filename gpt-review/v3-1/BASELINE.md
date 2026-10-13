# V3.1 Baseline Manifest

Captured: 2026-10-13

## Git baseline

- Repository: `https://github.com/wistroneq3300/pa-library-review`
- Fetched remote branch: `origin/codex/testcase-review-v3-pilot-200`
- Base commit: `5556f9db25c9ac2c0c329eca367eb9cabd72f508`
- Base subject: `Correct V3 pilot artifact commit SHA`
- New branch: `codex/testcase-review-v3-1`
- Fetch result: no newer V3 Pilot remote commit existed.
- Working tree at branch creation: clean.
- Stale ignored lock: `v3-pilot-200-20261013` had no matching active
  process and referenced the completed Pilot; it was explicitly replaced by
  the V3.1 run lock and was not committed.

## Immutable source hashes

| Artifact | SHA-256 |
| --- | --- |
| `data/REVISED_commands_merged_with_raw.xlsx` | `e2e737beb9cc4141f89a353813a48ab8034f55da56facba86a72fb9501a114d8` |
| `data/tests.json` | `5eefd664be9ed794e4429095f9d8e0c969d392a688b787af71f4f319526fdd37` |
| `data/tests_gpt_merged.json` | `34d0133ce0bab7647179f9822174838ecdfd5ee90e766eb9802eb8672dcfe4a2` |
| `gpt-review/test_gpt_review.json` | `5776cf96ff65219ca8d0dce07631914a9f45a98c0bccae8390f076ec67e25869` |
| V3 Pilot selection manifest | `55c915d7c91d2e4340353e881a85e1f0ff236f62a858106a19c05751f31a086d` |

## Review versions

- Legacy workflow: `REVIEW_WORKFLOW_LOGIC.md` (historical).
- GPT second review/V2: `gpt-review/REVIEW_WORKFLOW_LOGIC_GPT_SECOND_REVIEW.md`.
- V3: `gpt-review/REVIEW_WORKFLOW_LOGIC_V3.md`; 200-case Pilot complete.
- V3.1: `gpt-review/REVIEW_WORKFLOW_LOGIC_V3_1.md`; current controlling
  prospective contract.

## Fixed selection

- Canonical manifest: `gpt-review/v3-pilot-200/SELECTION_MANIFEST.json`.
- Count: exactly 200 unique source keys and 200 unique `case_variant_id` values.
- Selection order and identities are immutable for this re-review.
- `REVIEW_SELECTION_MANIFEST.json` is an immutable-reference manifest rather
  than a duplicated copy, so a byte-for-byte hash proves the exact Pilot
  selection without creating a second editable source.

## Original classification and result baseline

V2 normalized distribution: FULLY AUTOMATABLE 18; REQUIRES PACKAGE / USER
CONFIRMATION 102; MANUAL ONLY 39; BLOCKED 41.

V3 distribution: FULLY AUTOMATABLE 12; REQUIRES PACKAGE / USER CONFIRMATION
133; MANUAL ONLY 33; BLOCKED 22.

V3 review outcomes: KEEP 16; IMPROVED 74; RECLASSIFIED 43;
REWRITE_REQUIRED 12; SOURCE_CONFLICT 49; NEED_ENGINEER_DECISION 6.

## Known pending matters

- Original wording of Engineering Questions 01–28 is not present; current
  handoff decisions are authoritative and the missing wording is disclosed.
- Project-specific platform specifications, expected values, target mappings,
  private tool manuals, safety limits, and approved overrides remain pending
  per testcase.
- V3 validation used isolated same-model-family reviewers, not an independent
  model, and no hardware testing occurred.
- PA Manager compatibility is read-only analysis only.
