# Engineering Decision Re-review Handoff

- Completed formal queue: **480 / 942**; append-only active review events: **631**.
- Last valid formal review: `Reliability|36|Wistron-System RAS-00756-V003` / `36d6894753ea0c8d` (formal queue sequence 480; review event 631).
- Next directly verified pending identity: `Reliability|37|Wistron-System RAS-00757-V003` / `58b1c86f67ce3aca` (first missing formal queue sequence 481).
- Latest valid disposition: Reliability row 36 is resolved as a parameterized PCH Receiver-Error CE test with live endpoint/port/register mapping, exact RE-bit and Windows evidence, dependency protection and recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
