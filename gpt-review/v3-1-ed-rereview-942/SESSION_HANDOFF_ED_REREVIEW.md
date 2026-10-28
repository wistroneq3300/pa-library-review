# Engineering Decision Re-review Handoff

- Completed formal queue: **572 / 942**; append-only active review events: **723**.
- Last valid formal review: `Reliability|147|Wistron-HW Robust-00025-V002` / `e1305427b0c24287` (formal queue sequence 572; review event 723).
- Next directly verified pending identity: `Reliability|148|Wistron-HW Robust-00465-V002` / `86b45f60a13c8df2` (first missing formal queue sequence 573).
- Latest valid disposition: Reliability row147 remains Pending/Requires Confirmation: the surviving power-status script domain, GPIO polarity/tokens, approved off transition and independent recovery oracle are required. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
