# Engineering Decision Re-review Handoff

- Completed formal queue: **445 / 942**; append-only active review events: **596**.
- Last valid formal review: `Functionality|2283|Wistron-HW-00176-V003` / `59142a34afc1e1d7` (formal queue sequence 445; review event 596).
- Next directly verified pending identity: `Functionality|2284|Wistron-HW-00165-V003` / `25186206e90927a8` (first missing formal queue sequence 446).
- Latest valid disposition: row-2283 is resolved as a parameterized manual switch-location-only inspection tied to board revision and visual evidence; lever setting and actuation are explicitly outside this row. No hardware access occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
