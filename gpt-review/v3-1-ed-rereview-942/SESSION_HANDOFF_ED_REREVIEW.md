# Engineering Decision Re-review Handoff

- Completed formal queue: **614 / 942**; append-only active review events: **765**.
- Last valid formal review: `Reliability|195|Wistron-GPU RAS-00838-V006` / `577c9e1b9d3a0810` (formal queue sequence 614; review event 765).
- Next directly verified pending identity: `Reliability|196|Wistron-GPU RAS-00028-V002` / `0c15ba8dbb4159d9` (first missing formal queue sequence 615).
- Latest valid disposition: Reliability row195 retains Source Conflict: CRC-read and mode5 write scope plus variant-specific correctable/deferred/EEPROM oracles must be ruled before execution. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
