# Engineering Decision Re-review Handoff

- Completed formal queue: **605 / 942**; append-only active review events: **756**.
- Last valid formal review: `Reliability|185|Wistron-GPU RAS-00014-V002` / `3053d9edb2a2b2d8` (formal queue sequence 605; review event 756).
- Next directly verified pending identity: `Reliability|186|Wistron-GPU RAS-00034-V002` / `7ce1818bc61867e3` (first missing formal queue sequence 606).
- Latest valid disposition: Reliability row185 remains critical Pending: in-band MMHUB requires omitted-device target proof, block3 semantics, MMHUB/VM dmesg oracle and GPU recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
