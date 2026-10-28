# Engineering Decision Re-review Handoff

- Completed formal queue: **604 / 942**; append-only active review events: **755**.
- Last valid formal review: `Reliability|184|Wistron-GPU RAS-00033-V002` / `a401d6ac253abf7a` (formal queue sequence 604; review event 755).
- Next directly verified pending identity: `Reliability|185|Wistron-GPU RAS-00014-V002` / `3053d9edb2a2b2d8` (first missing formal queue sequence 605).
- Latest valid disposition: Reliability row184 remains critical Pending: OOB GFX requires approved block2-to-GC CPER mapping, secure endpoint, unique ext59 decoder and recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
