# Engineering Decision Re-review Handoff

- Completed formal queue: **709 / 942**; append-only active review events: **860**.
- Last valid formal review: `Compatibility|170|Wistron-AMD GPU-00163-V002` / `b40f429d444af331` (formal queue sequence 709; review event 860).
- Next directly verified pending identity: `Compatibility|181|Wistron-AMD GPU-00174-V002` / `ad4ef26f982fe161` (first missing formal queue sequence 710).
- Latest valid disposition: Compatibility row170 retains Engineering Decision Pending because the OS-booted title and standby/do-not-power-on Procedure specify non-equivalent PLDM firmware states; any BMC-Web flash remains separately authorized with visual evidence, exact image/target versions and rescue path. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
