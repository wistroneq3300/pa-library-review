# Engineering Decision Re-review Handoff

- Completed formal queue: **835 / 942**; append-only active review events: **986**.
- Last valid formal review: Compatibility|411|Wistron-AMD GPU-00131-V003 / 13295c72aef69327 (formal queue sequence 835; review event 986).
- Next directly verified pending identity: Compatibility|412|Wistron-AMD GPU-00470-V002 / ece6aa849af9a141 (first missing formal queue sequence 836).
- Latest valid disposition: Compatibility row411 retains Engineering Decision Pending only for the authoritative RCCL band oracle: the source does not identify algbw versus busbw, in-place versus out-of-place, or aggregation semantics for its two GB/s ranges. The exact two collectives, 1-GiB/eight-GPU scope and safe parameterized method are preserved. No build, collective or DUT action ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
