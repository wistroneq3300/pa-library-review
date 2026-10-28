# Engineering Decision Re-review Handoff

- Completed formal queue: **723 / 942**; append-only active review events: **874**.
- Last valid formal review: `Compatibility|241|Wistron-AMD GPU-00234-V002` / `ac8e6e27c5384c9e` (formal queue sequence 723; review event 874).
- Next directly verified pending identity: `Compatibility|242|Wistron-AMD GPU-00235-V002` / `681b579fda4db98d` (first missing formal queue sequence 724).
- Latest valid disposition: Compatibility row241 retains Engineering Decision Pending because every 25C loop may request width16 without its status readback and lacks authoritative AGT width/restore semantics. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
