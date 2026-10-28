# Engineering Decision Re-review Handoff

- Completed formal queue: **600 / 942**; append-only active review events: **751**.
- Last valid formal review: `Reliability|179|Wistron-GPU RAS-00030-V002` / `d34dd43dadd7c08d` (formal queue sequence 600; review event 751).
- Next directly verified pending identity: `Reliability|180|Wistron-GPU RAS-00467-V004` / `f2e753543277de69` (first missing formal queue sequence 601).
- Latest valid disposition: Reliability row179 remains critical Pending: AMD OOB single-shot UMC injection requires approved numeric target/tool semantics, secure OEM CPER endpoint, unique attachment attribution, exact decoder and fatal-error recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
