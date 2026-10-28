# Engineering Decision Re-review Handoff

- Completed formal queue: **654 / 942**; append-only active review events: **805**.
- Last valid formal review: `Performance|57|Wistron-Performance GPU-00029-V002` / `eedd23ffd84e05b0` (formal queue sequence 654; review event 805).
- Next directly verified pending identity: `Performance|59|Wistron-Performance GPU-00031-V002` / `c87f3b1adca3a55c` (first missing formal queue sequence 655).
- Latest valid disposition: Performance row57 is Review-resolved under ED-10 as v5.0 Mixtral-8x7B Server inference with MoE/model and LoadGen validity gates. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
