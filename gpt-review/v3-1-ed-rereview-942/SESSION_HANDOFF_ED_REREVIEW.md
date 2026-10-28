# Engineering Decision Re-review Handoff

- Completed formal queue: **611 / 942**; append-only active review events: **762**.
- Last valid formal review: `Reliability|191|Wistron-GPU RAS-00836-V004` / `caa2828e190665cb` (formal queue sequence 611; review event 762).
- Next directly verified pending identity: `Reliability|193|Wistron-GPU RAS-00026-V002` / `67a5309fdf7cd6bb` (first missing formal queue sequence 612).
- Latest valid disposition: Reliability row191 remains Pending: in-band UMC ODECC requires exact address/ACA mapping, approved multi-array counter delta, quiet window and recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
