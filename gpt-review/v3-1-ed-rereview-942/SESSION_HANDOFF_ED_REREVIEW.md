# Engineering Decision Re-review Handoff

- Completed formal queue: **615 / 942**; append-only active review events: **766**.
- Last valid formal review: `Reliability|196|Wistron-GPU RAS-00028-V002` / `0c15ba8dbb4159d9` (formal queue sequence 615; review event 766).
- Next directly verified pending identity: `Reliability|197|Wistron-GPU RAS-00840-V004` / `917eee152ea50b06` (first missing formal queue sequence 616).
- Latest valid disposition: Reliability row196 remains Pending: OOB GFX correctable requires block2-to-GC mapping, exact ext58 corrected CPER, no-escalation quiet oracle and recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
