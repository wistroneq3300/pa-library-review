# Engineering Decision Re-review Handoff

- Completed formal queue: **827 / 942**; append-only active review events: **978**.
- Last valid formal review: Compatibility|403|Wistron-AMD GPU-00469-V003 / 123048d3a1f296eb (formal queue sequence 827; review event 978).
- Next directly verified pending identity: Compatibility|404|Wistron-AMD GPU-00469-V003 / c5c7730f9585f9bb (first missing formal queue sequence 828).
- Latest valid disposition: Compatibility row403 remains Engineering Decision Pending because AMD errata and release notes prove that zero-margin handling and AMDXIO method are build/platform-specific; receiver=6 schema, equality/numeric oracle and safe ASPM restore authority are still missing. No AMDXIO or DUT action ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
