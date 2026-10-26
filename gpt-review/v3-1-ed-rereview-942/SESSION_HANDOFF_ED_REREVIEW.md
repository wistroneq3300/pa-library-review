# Engineering Decision Re-review Handoff

- Completed formal queue: **453 / 942**; append-only active review events: **604**.
- Last valid formal review: `Reliability|6|Wistron-System RAS-00726-V003` / `b118ca7ea8664615` (formal queue sequence 453; review event 604).
- Next directly verified pending identity: `Reliability|7|Wistron-System RAS-00727-V003` / `1f3fc7fc06bcb8db` (first missing formal queue sequence 454).
- Latest valid disposition: Reliability row 6 remains Pending and is now explicitly BLOCKED: sustained UPI CRC injection lacks a positive stop/recovery path and has Windows/dmesg plus UPI/LCD oracle conflicts. No RAS or DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
