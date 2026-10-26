# Engineering Decision Re-review Handoff

- Completed formal queue: **442 / 942**; append-only active review events: **593**.
- Last valid formal review: `Functionality|2280|Wistron-HW-00248-V003` / `9bca37010e03e569` (formal queue sequence 442; review event 593).
- Next directly verified pending identity: `Functionality|2281|Wistron-HW-00247-V003` / `d920c0ce3b5110fc` (first missing formal queue sequence 443).
- Latest valid disposition: row-2280 remains pending for an otherwise valid signed capsule that specifically violates approved SVN policy, the anti-rollback rejection oracle and proof of zero firmware/trust mutation. Generic corruption cannot satisfy it. No update attempt ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
