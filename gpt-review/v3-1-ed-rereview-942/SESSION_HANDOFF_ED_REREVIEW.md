# Engineering Decision Re-review Handoff

- Completed formal queue: **580 / 942**; append-only active review events: **731**.
- Last valid formal review: `Reliability|157|Wistron-System RAS-00114-V008` / `dd33fd3204879c4e` (formal queue sequence 580; review event 731).
- Next directly verified pending identity: `Reliability|158|Wistron-System RAS-00115-V003` / `016c35c310637d21` (first missing formal queue sequence 581).
- Latest valid disposition: Reliability row157 remains critical Pending: Patrol Scrub injection requires Intel-approved harness/FAE, exact DIMM/address/register mapping, expected MSCOD/retry/extlog oracle, crash recovery and complete BIOS/DFX restoration. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
