# Engineering Decision Re-review Handoff

- Completed formal queue: **716 / 942**; append-only active review events: **867**.
- Last valid formal review: `Compatibility|215|Wistron-AMD GPU-00208-V002` / `91960fc6ad6aae9f` (formal queue sequence 716; review event 867).
- Next directly verified pending identity: `Compatibility|227|Wistron-AMD GPU-00220-V002` / `24a56321dae9d9b9` (first missing formal queue sequence 717).
- Latest valid disposition: Compatibility row215 retains Engineering Decision Pending because rocFFT title/build and literal clFFT/OpenCL `fft1d.c` procedure are different APIs; matching transform direction, normalization, numerical tolerance and runtime linkage authority are required. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
