# Engineering Decision Re-review Handoff

- Completed formal queue: **711 / 942**; append-only active review events: **862**.
- Last valid formal review: `Compatibility|201|Wistron-AMD GPU-00194-V002` / `24acdc09070652bb` (formal queue sequence 711; review event 862).
- Next directly verified pending identity: `Compatibility|202|Wistron-AMD GPU-00195-V002` / `39ab341d907499f3` (first missing formal queue sequence 712).
- Latest valid disposition: Compatibility row201 retains Engineering Decision Pending because equal/below-reference and non-zero-only PASS criteria conflict; no generic rule may invent the SI oracle, and all eight BDF-bound links plus transactional ASPM restoration remain mandatory. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
