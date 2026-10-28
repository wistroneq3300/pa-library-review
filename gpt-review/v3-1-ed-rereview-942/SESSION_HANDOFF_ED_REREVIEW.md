# Engineering Decision Re-review Handoff

- Completed formal queue: **573 / 942**; append-only active review events: **724**.
- Last valid formal review: `Reliability|148|Wistron-HW Robust-00465-V002` / `86b45f60a13c8df2` (formal queue sequence 573; review event 724).
- Next directly verified pending identity: `Reliability|150|Wistron-HW Robust-00028-V002` / `07ab156210bd7335` (first missing formal queue sequence 574; row149 is baseline-completed).
- Latest valid disposition: Reliability row148 remains Pending/Requires Confirmation: always-on controller domain, GPIO semantics, standby/rail/POST/OS timing and no-retry recovery are required; host SSH cannot originate from standby. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
