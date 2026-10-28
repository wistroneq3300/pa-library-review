# Engineering Decision Re-review Handoff

- Completed formal queue: **708 / 942**; append-only active review events: **859**.
- Last valid formal review: `Compatibility|159|Wistron-AMD GPU-00145-V002` / `d9c9baacd85e4c6c` (formal queue sequence 708; review event 859).
- Next directly verified pending identity: `Compatibility|170|Wistron-AMD GPU-00163-V002` / `b40f429d444af331` (first missing formal queue sequence 709).
- Latest valid disposition: Compatibility row159 retains Engineering Decision Pending because 12-hour title/720-minute coverage conflicts with a literal 30-minute RVS kill step; ED-14 forbids short-run substitution, but project authority must define the non-reduced continuous/repeated/segmented schedule. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
