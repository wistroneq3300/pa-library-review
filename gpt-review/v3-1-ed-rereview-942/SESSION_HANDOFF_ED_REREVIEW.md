# Engineering Decision Re-review Handoff

- Completed formal queue: **584 / 942**; append-only active review events: **735**.
- Last valid formal review: `Reliability|162|Wistron-System RAS-00119-V002` / `ad9caa9142f750a5` (formal queue sequence 584; review event 735).
- Next directly verified pending identity: `Reliability|163|Wistron-System RAS-00120-V002` / `bb5c8d8401bf531d` (first missing formal queue sequence 585).
- Latest valid disposition: Reliability row162 remains critical Pending: two same-row CEs must prove 1/2-to-threshold Runtime Soft PPR without reboot, with exact FTrace tokens and separately approved issue120 workaround. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
