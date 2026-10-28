# Engineering Decision Re-review Handoff

- Completed formal queue: **635 / 942**; append-only active review events: **786**.
- Last valid formal review: `Performance|27|Wistron-Performance GPU-00043-V003` / `d0f31d301dcaaaa3` (formal queue sequence 635; review event 786).
- Next directly verified pending identity: `Performance|28|Wistron-Performance GPU-00044-V003` / `5f543642b7ffbd66` (first missing formal queue sequence 636).
- Latest valid disposition: Performance row27 is Review-resolved under ED-10 as GPT-J99.9 high-accuracy Server; GPT-J99, Offline and copied BERT evidence cannot substitute. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
