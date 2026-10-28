# Engineering Decision Re-review Handoff

- Completed formal queue: **718 / 942**; append-only active review events: **869**.
- Last valid formal review: `Compatibility|230|Wistron-AMD GPU-00223-V002` / `c7b318f5b86e4cf2` (formal queue sequence 718; review event 869).
- Next directly verified pending identity: `Compatibility|232|Wistron-AMD GPU-00225-V002` / `d3fc716f2bd9c073` (first missing formal queue sequence 719).
- Latest valid disposition: Compatibility row230 retains Engineering Decision Pending because literal `apt -mccfg`, AGT metadata and DeepSeek `agt mccfg` conflict on executable identity and semantics; no typo or OEM syntax may be inferred, and row227 overlap must be resolved. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
