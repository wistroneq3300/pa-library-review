# Engineering Decision Re-review Handoff

- Completed formal queue: **511 / 942**; append-only active review events: **662**.
- Last valid formal review: `Reliability|70|Wistron-System RAS-00790-V002` / `cb06cc47b636c48a` (formal queue sequence 511; review event 662).
- Next directly verified pending identity: `Reliability|71|Wistron-System RAS-00791-V002` / `77f8846ef212bef7` (first missing formal queue sequence 512).
- Latest valid disposition: Reliability row70 remains Pending/BLOCKED because IOHUB errortype1, group/structure, threshold encoding, reset behavior and fresh durable MCA/BERT/CPER oracle lack authority. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
