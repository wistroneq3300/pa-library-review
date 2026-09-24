# Review Restart Notice

The previous automated Batch 002 output was a triage artifact and is not a
valid GPT second review. It must not be used by System Manager or OpenHands.

The active review overlay and checkpoint were reset on 2026-09-25. The review
now restarts at `Functionality/Wistron-HW-00001-V006` and processes exactly one
source testcase at a time with independent reasoning and no templates.

The invalid artifact remains recoverable in Git history at commit
`4aad54a`, but is intentionally absent from the active `test_gpt_review.json`.
