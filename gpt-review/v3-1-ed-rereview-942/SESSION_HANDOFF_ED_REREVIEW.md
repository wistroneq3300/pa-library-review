# Engineering Decision Re-review Handoff

- Completed formal queue: **579 / 942**; append-only active review events: **730**.
- Last valid formal review: `Reliability|155|Wistron-HW Robust-00466-V003` / `526093343e6480cc` (formal queue sequence 579; review event 730).
- Next directly verified pending identity: `Reliability|157|Wistron-System RAS-00114-V008` / `dd33fd3204879c4e` (first missing formal queue sequence 580; row156 is baseline-completed).
- Latest valid disposition: Reliability row155 remains critical Pending: full-SEL stress requires vendor-decoded raw event, preserved real logs, capacity-bound full oracle, approved MC reset and post-evidence cleanup/recovery. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
