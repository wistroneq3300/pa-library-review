# Engineering Decision Re-review Handoff

- Completed formal queue: **443 / 942**; append-only active review events: **594**.
- Last valid formal review: `Functionality|2281|Wistron-HW-00247-V003` / `d920c0ce3b5110fc` (formal queue sequence 443; review event 594).
- Next directly verified pending identity: `Functionality|2282|Wistron-BMC-00878-V003` / `ccfb07e841fda008` (first missing formal queue sequence 444).
- Latest valid disposition: row-2281 remains pending for a reproducible known-good-to-corrupt capsule diff, explicit active/recovery target, AST1060 rejection gate and immutable both-region no-write evidence. No update attempt ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
