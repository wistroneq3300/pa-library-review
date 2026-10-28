# Engineering Decision Re-review Handoff

- Completed formal queue: **564 / 942**; append-only active review events: **715**.
- Last valid formal review: `Reliability|136|Wistron-HW Robust-00014-V002` / `33eca75d193fb45f` (formal queue sequence 564; review event 715).
- Next directly verified pending identity: `Reliability|137|Wistron-HW Robust-00015-V002` / `cbfd3cf419092b23` (first missing formal queue sequence 565).
- Latest valid disposition: Reliability row136 remains Pending/Requires Confirmation: RTC and IO-expander need separate device oracles and driver-safe access; default forced access, blind scan and physical-only substitution were rejected. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
