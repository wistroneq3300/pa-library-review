# Engineering Decision Re-review Handoff

- Completed formal queue: **715 / 942**; append-only active review events: **866**.
- Last valid formal review: `Compatibility|213|Wistron-AMD GPU-00206-V002` / `2dbaf5f750e028ba` (formal queue sequence 715; review event 866).
- Next directly verified pending identity: `Compatibility|215|Wistron-AMD GPU-00208-V002` / `91960fc6ad6aae9f` (first missing formal queue sequence 716).
- Latest valid disposition: Compatibility row213 retains Engineering Decision Pending because rocBLAS title/build and literal clBLAS/OpenCL SROT procedure are different APIs; no global OpenCL symlink or generic smoke substitution is allowed, and matching numerical/linkage authority is required. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
