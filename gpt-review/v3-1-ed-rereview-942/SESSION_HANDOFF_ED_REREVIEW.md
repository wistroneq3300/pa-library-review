# Engineering Decision Re-review Handoff

- Completed formal queue: **591 / 942**; append-only active review events: **742**.
- Last valid formal review: `Reliability|169|Wistron-System RAS-00126-V002` / `70b23c02588795fe` (formal queue sequence 591; review event 742).
- Next directly verified pending identity: `Reliability|171|Wistron-System RAS-00128-V002` / `1a4fc7cdfbf005ec` (first missing formal queue sequence 592).
- Latest valid disposition: Reliability row169 remains critical Pending: persistent partial-mirror UCE requires exact ARM/TAD-to-MC0/ch0 mapping, deterministic injector clear before go, B2CMI1 bit0/extlog oracle and degraded-channel recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
