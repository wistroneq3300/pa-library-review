# Engineering Decision Re-review Handoff

- Completed formal queue: **609 / 942**; append-only active review events: **760**.
- Last valid formal review: `Reliability|189|Wistron-GPU RAS-00834-V005` / `9a4aa5d38b13c82e` (formal queue sequence 609; review event 760).
- Next directly verified pending identity: `Reliability|190|Wistron-GPU RAS-00025-V002` / `b67a36a53a50f884` (first missing formal queue sequence 610).
- Latest valid disposition: Reliability row189 is RESOLVED as a parameterized package/version gate: exact `-v` query and >=1.6.3 oracle are complete; signed artifact, OS compatibility and rollback remain runtime configuration. No package or DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
