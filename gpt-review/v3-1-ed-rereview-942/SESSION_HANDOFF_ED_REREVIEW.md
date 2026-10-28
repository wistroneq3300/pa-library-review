# Engineering Decision Re-review Handoff

- Completed formal queue: **720 / 942**; append-only active review events: **871**.
- Last valid formal review: `Compatibility|238|Wistron-AMD GPU-00231-V002` / `2b3ab8f92c6bfd49` (formal queue sequence 720; review event 871).
- Next directly verified pending identity: `Compatibility|239|Wistron-AMD GPU-00232-V002` / `e86317965700e6eb` (first missing formal queue sequence 721).
- Latest valid disposition: Compatibility row238 retains Engineering Decision Pending because 24 hours conflicts with 10-minute metadata and the OEM raw ECC field/zero-delta semantics are not authoritative; no short smoke substitute or raw decoding was invented. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
