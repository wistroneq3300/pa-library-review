# Engineering Decision Re-review Handoff

- Completed formal queue: **454 / 942**; append-only active review events: **605**.
- Last valid formal review: `Reliability|7|Wistron-System RAS-00727-V003` / `1f3fc7fc06bcb8db` (formal queue sequence 454; review event 605).
- Next directly verified pending identity: `Reliability|8|Wistron-System RAS-00728-V003` / `f72d30c680184561` (first missing formal queue sequence 455).
- Latest valid disposition: Reliability row 7 remains Pending for physical UPI target mapping, Intel harness semantics, deterministic standard/advanced RAS SKU oracle and recovery; its one-shot injection is not executed. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
