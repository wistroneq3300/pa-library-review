# Engineering Decision Re-review Handoff

- Completed formal queue: **581 / 942**; append-only active review events: **732**.
- Last valid formal review: `Reliability|158|Wistron-System RAS-00115-V003` / `016c35c310637d21` (formal queue sequence 581; review event 732).
- Next directly verified pending identity: `Reliability|160|Wistron-System RAS-00117-V002` / `82aa7841306cc292` (first missing formal queue sequence 582).
- Latest valid disposition: Reliability row158 remains critical Pending: Demand Scrub injection requires Intel-approved harness/FAE, exact address/DIMM/register mapping, latent-before-read proof, decoded MC/retry/extlog oracle, crash recovery and complete BIOS/GRUB/DFX restoration. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
