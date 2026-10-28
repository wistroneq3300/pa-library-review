# Engineering Decision Re-review Handoff

- Completed formal queue: **840 / 942**; append-only active review events: **991**.
- Last valid formal review: Compatibility|416|Wistron-AMD GPU-00135-V002 / 51ad508a8c292dca (formal queue sequence 840; review event 991).
- Next directly verified pending identity: Compatibility|417|Wistron-AMD GPU-00136-V002 / d821e95a1ddebf09 (first missing formal queue sequence 841).
- Latest valid disposition: Compatibility row416 is review-resolved as fully automatable immutable raw kernel-log capture plus a time-bound MI350/amdgpu error-severity view. Log clearing and insecure SSH are rejected, and no-match is distinguished from access/truncation failure; same-code row150 DGEMM remains separate. No DUT command or log mutation ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
