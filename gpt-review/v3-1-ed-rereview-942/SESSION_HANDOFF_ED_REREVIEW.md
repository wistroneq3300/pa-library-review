# Engineering Decision Re-review Handoff

- Completed formal queue: **593 / 942**; append-only active review events: **744**.
- Last valid formal review: `Reliability|172|Wistron-System RAS-00129-V003` / `74b787611d7bc143` (formal queue sequence 593; review event 744).
- Next directly verified pending identity: `Reliability|173|Wistron-System RAS-00130-V002` / `a93a3a5aabfd3309` (first missing formal queue sequence 594).
- Latest valid disposition: Reliability row172 remains critical Pending: the ADDDC negative case requires an attested predecessor VLS map, same-bank/different-device proof, threshold and unchanged-region/copy=0/counter-clear oracle. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
