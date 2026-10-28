# Engineering Decision Re-review Handoff

- Completed formal queue: **698 / 942**; append-only active review events: **849**.
- Last valid formal review: `Compatibility|142|Wistron-AMD GPU-00126-V002` / `6607ec9307e9e775` (formal queue sequence 698; review event 849).
- Next directly verified pending identity: `Compatibility|143|Wistron-AMD GPU-00127-V002` / `9b5c21f7251f69be` (first missing formal queue sequence 699).
- Latest valid disposition: Compatibility row142 is Review-resolved under ED-02 as the distinct IOMMU-enabled driver-binding variant, requiring aligned firmware/cmdline/runtime mode and complete eight-GPU per-BDF binding rather than token or grep evidence. No DUT action occurred.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
