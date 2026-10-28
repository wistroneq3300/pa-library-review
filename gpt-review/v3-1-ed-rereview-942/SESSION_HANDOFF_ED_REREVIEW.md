# Engineering Decision Re-review Handoff

- Completed formal queue: **722 / 942**; append-only active review events: **873**.
- Last valid formal review: `Compatibility|240|Wistron-AMD GPU-00233-V002` / `87819a2c90daa27e` (formal queue sequence 722; review event 873).
- Next directly verified pending identity: `Compatibility|241|Wistron-AMD GPU-00234-V002` / `ac8e6e27c5384c9e` (first missing formal queue sequence 723).
- Latest valid disposition: Compatibility row240 retains Engineering Decision Pending because the 10C loop excludes width16/readback and lacks authoritative AGT width, condensation and restoration semantics. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
