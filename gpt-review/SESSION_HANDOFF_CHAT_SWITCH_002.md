# GPU Server SIT GPT Second Review — Chat Switch Handoff 002

## Repository

- Repository: `https://github.com/wistroneq3300/pa-library-review.git`
- Branch: `main`
- Workspace: `gpu-server-sit-test-library-review`
- Original sources (never modify):
  - `data/REVISED_commands_merged_with_raw.xlsx`
  - `data/tests.json`
- GPT overlay: `gpt-review/test_gpt_review.json`

## Current state — PAUSED

- `gpt-review/progress.json` status: `PAUSED_INVALID_NEEDS_USER_DIRECTION`
- Valid overlay records: 16
- Last valid checkpoint: `Functionality/row-1816/Wistron-HW-00015-V002`
- `next_key`: `Functionality/Wistron-HW-00017-V002`
- Invalid/discarded range: source rows 17–47, 31 records
- Invalid notice: `gpt-review/INVALID_RUN_NOTICE_002.md`
- Do not select or review the next testcase until the user explicitly authorizes
  the re-review of rows 17–47.

## Why the run was invalid

The records from source row 17 through source row 47 reused an analysis
scaffold. They were removed from the active overlay and do not count as
reviewed. This was an integrity failure, not a source-data failure.

The anti-template causes and stop behavior are recorded in:

- `gpt-review/REVIEW_WORKFLOW_LOGIC_GPT_SECOND_REVIEW.md`
- `C:\Users\kobei\.codex\skills\gpu-server-sit-review\ANTI_TEMPLATE_CONTROLS.md`

When `invalid` is detected: persist the affected range/reason/checkpoint,
commit and push, then stop and ask the user. Never auto-restart.

## Mandatory review method after user approval

1. Read the exact selected source row's `Items`, `Procedure`, and `Criteria`.
2. Read only that row's matching DeepSeek review for comparison.
3. Independently derive purpose, command alignment, package/dependency,
   safety, blast radius, evidence, recovery, and classification.
4. Write exactly one English overlay record.
5. Verify one record, one count increment, one `next_key` advance, and zero
   diff in the original XLSX and `data/tests.json`.
6. Commit and push only that one testcase plus checkpoint metadata.
7. Before the next row, prove that the reasoning contains a source-specific
   purpose finding, DeepSeek comparison, and safety/evidence decision.

The schema may be consistent, but copied reasoning, risk text, command text, or
recovery text is not allowed. If independent reasoning cannot be maintained,
mark invalid, pause, and ask the user.

## User message to resume

The new conversation must wait for this explicit user instruction:

```text
同意重做第 17～47 條，從第 17 條開始逐條獨立 review。
```

Until that message (or an equivalent explicit direction), do not review, delete,
restart, or generate any additional overlay records.

## Language and execution boundary

- Conversation with the user: Chinese.
- Testcase overlay: English.
- PASS / FAIL / BLOCKED: decided by the end user; the agent reports evidence.
- The reviewing agent does not execute the DUT test.
- Any later execution agent must perform read-only pre-checks, report facts and
  the resolved command in Chinese, wait for exact `OK`, then execute.
