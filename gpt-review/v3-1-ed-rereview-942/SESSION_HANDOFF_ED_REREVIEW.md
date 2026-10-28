# Engineering Decision Re-review Handoff

- Completed formal queue: **613 / 942**; append-only active review events: **764**.
- Last valid formal review: `Reliability|194|Wistron-GPU RAS-00027-V002` / `adae559041a1d7cb` (formal queue sequence 613; review event 764).
- Next directly verified pending identity: `Reliability|195|Wistron-GPU RAS-00838-V006` / `577c9e1b9d3a0810` (first missing formal queue sequence 614).
- Latest valid disposition: Reliability row194 remains Pending: CRC-read replay requires subtype0/type4 authority, exact ext15 EndToEndCrcErr CPER, quiet-window/deferred oracle and recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
