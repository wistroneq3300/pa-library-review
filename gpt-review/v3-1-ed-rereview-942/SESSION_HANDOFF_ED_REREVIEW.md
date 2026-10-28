# Engineering Decision Re-review Handoff

- Completed formal queue: **644 / 942**; append-only active review events: **795**.
- Last valid formal review: `Performance|41|Wistron-Performance GPU-00061-V004` / `68b0a9a4450fd093` (formal queue sequence 644; review event 795).
- Next directly verified pending identity: `Performance|43|Wistron-Performance GPU-00063-V003` / `2d99a0d79506a3cc` (first missing formal queue sequence 645).
- Latest valid disposition: Performance row41 is Review-resolved under ED-10 as MLPerf v3.0 RNN-T99 Server with speech accuracy, streaming latency and validity gates; copied BERT/Offline evidence is rejected. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
