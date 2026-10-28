# Engineering Decision Re-review Handoff

- Completed formal queue: **567 / 942**; append-only active review events: **718**.
- Last valid formal review: `Reliability|140|Wistron-HW Robust-00018-V002` / `dfcfe4a97400f3b1` (formal queue sequence 567; review event 718).
- Next directly verified pending identity: `Reliability|141|Wistron-HW Robust-00019-V002` / `6ff6fafa8eacf83c` (first missing formal queue sequence 568).
- Latest valid disposition: Reliability row140 remains Pending/Requires Confirmation: three IO-expander routes, part/register maps and pin masks are required; two offsets from one0x74 cannot prove three devices. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
