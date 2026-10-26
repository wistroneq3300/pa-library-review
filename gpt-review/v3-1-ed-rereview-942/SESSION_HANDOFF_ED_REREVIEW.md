# Engineering Decision Re-review Handoff

- Completed formal queue: **427 / 942**; append-only review events: **578**.
- Last formal review: `Functionality|2264|Wistron-HW-00370-V004` / `1018a2d020a1c6b2` (formal queue sequence 427; review event 578).
- Next source-verified pending identity: `Functionality|2265|Wistron-HW-00371-V004` / `52c3c9d42d9c3ad1` (first missing formal queue sequence 428).
- Latest disposition: row-2264 retains the explicit graceful-shutdown versus remain-On short-press conflict; every physical/LED/forced-off checkpoint is preserved and the long hold is not a recovery action. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged. Forty-nine initial formal records plus events 201-355 are authoritative; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
