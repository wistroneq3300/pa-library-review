# Engineering Decision Re-review Handoff

- Completed formal queue: **836 / 942**; append-only active review events: **987**.
- Last valid formal review: Compatibility|412|Wistron-AMD GPU-00470-V002 / ece6aa849af9a141 (formal queue sequence 836; review event 987).
- Next directly verified pending identity: Compatibility|413|Wistron-AMD GPU-00132-V002 / 9dfdce9c6d5a1951 (first missing formal queue sequence 837).
- Latest valid disposition: Compatibility row412 is review-resolved as the exact AMD-documented all-device CoralGEMM command for 1800 seconds with pre-trigger power capture. Per-GPU power is checked directly against the source 1000-W ceiling; chassis PSU/BMC readings remain independent and are never divided into invented per-card values. No build, load or DUT action ran.
- Integrity disposition: formal sequences 436-600 / events 587-751 were invalidated on 2026-10-27 because a mechanical generator violated the mandatory one-case-at-a-time reasoning rule. Their exact files are preserved under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; active progress is restored to formal 435 and re-review resumes at 436.
- Formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
