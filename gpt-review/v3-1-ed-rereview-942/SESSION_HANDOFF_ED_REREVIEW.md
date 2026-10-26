# Engineering Decision Re-review Handoff

- Completed formal queue: **440 / 942**; append-only active review events: **591**.
- Last valid formal review: `Functionality|2278|Wistron-HW-00245-V003` / `e3e7b3795f1858bb` (formal queue sequence 440; review event 591).
- Next directly verified pending identity: `Functionality|2279|Wistron-HW-00246-V003` / `b2b7e9abe2a97edb` (first missing formal queue sequence 441).
- Latest valid disposition: row-2278 remains pending for the target AST1060 lifecycle/key/capsule/final-state and external recovery authority. Valid signed capsule update coverage is retained; corrupt/downgrade rejection is not substituted. No PFR mutation or Flash ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
