# Engineering Decision Re-review Handoff

- Completed formal queue: **719 / 942**; append-only active review events: **870**.
- Last valid formal review: `Compatibility|232|Wistron-AMD GPU-00225-V002` / `d3fc716f2bd9c073` (formal queue sequence 719; review event 870).
- Next directly verified pending identity: `Compatibility|238|Wistron-AMD GPU-00231-V002` / `2b3ab8f92c6bfd49` (first missing formal queue sequence 720).
- Latest valid disposition: Compatibility row232 retains Engineering Decision Pending because AGT width/status syntax is malformed, width acceptance is absent and value mappings/25C baseline restoration are not authoritative; no OEM correction or unsupported retrain may be guessed. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
