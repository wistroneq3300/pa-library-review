# Engineering Decision Re-review Handoff

- Completed formal queue: **713 / 942**; append-only active review events: **864**.
- Last valid formal review: `Compatibility|211|Wistron-AMD GPU-00204-V002` / `458b3cf7f1870cc3` (formal queue sequence 713; review event 864).
- Next directly verified pending identity: `Compatibility|212|Wistron-AMD GPU-00205-V002` / `9350deb8cd5f9dca` (first missing formal queue sequence 714).
- Latest valid disposition: Compatibility row211 retains Engineering Decision Pending because DCT control property, bounds and recovery are core command semantics; read-only `rocm-smi` enumeration cannot substitute, and no GPU write property may be guessed. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
