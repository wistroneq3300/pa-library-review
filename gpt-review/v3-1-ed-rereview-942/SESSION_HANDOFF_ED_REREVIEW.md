# Engineering Decision Re-review Handoff

- Completed formal queue: **592 / 942**; append-only active review events: **743**.
- Last valid formal review: `Reliability|171|Wistron-System RAS-00128-V002` / `1a4fc7cdfbf005ec` (formal queue sequence 592; review event 743).
- Next directly verified pending identity: `Reliability|172|Wistron-System RAS-00129-V003` / `74b787611d7bc143` (first missing formal queue sequence 593).
- Latest valid disposition: Reliability row171 remains critical Pending: PFD requires verified125-bit mode, exact mask/target semantics, bounded continuous-injector abort, cross-surface correction oracle and recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
