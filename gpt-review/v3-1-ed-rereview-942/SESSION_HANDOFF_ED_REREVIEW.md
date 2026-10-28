# Engineering Decision Re-review Handoff

- Completed formal queue: **714 / 942**; append-only active review events: **865**.
- Last valid formal review: `Compatibility|212|Wistron-AMD GPU-00205-V002` / `9350deb8cd5f9dca` (formal queue sequence 714; review event 865).
- Next directly verified pending identity: `Compatibility|213|Wistron-AMD GPU-00206-V002` / `2dbaf5f750e028ba` (first missing formal queue sequence 715).
- Latest valid disposition: Compatibility row212 retains Engineering Decision Pending because ROCm SMI title/test-set and DCT-only Procedure/Criteria are non-equivalent and overlap row211; scope must be chosen or split before command/oracle/recovery can be defined. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
