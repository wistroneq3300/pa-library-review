# Engineering Decision Re-review Handoff

- Completed formal queue: **522 / 942**; append-only review events: **673**.
- Last formal review: `Reliability|82|Wistron-System RAS-00802-V003` / `0f95914a22d01f24` (formal queue sequence 522; review event 673).
- Next source-verified pending identity: `Reliability|83|Wistron-System RAS-00803-V003` / `879daa9193f1fab6` (first missing formal queue sequence 523).
- Latest disposition: RETAINED_PENDING_MP1_(SMU)_UNCORRECTABLE_ERROR_0522; The OS cannot collect volatile evidence while the UCE resets the host, so BERT/CPER, SEL and OOB timing must be the correlation chain. Because MP1 manages platform controls, returning to a login prompt is insufficient: sensor publication and power/thermal/clock functions must operate normally. Index and mode semantics remain vendor-defined and cannot be inferred from the adjacent CE case. The remaining project decision is case-specific: Resolve Reliability row 82 Wistron-System RAS-00802-V003: define MP1 block/errorindex0, socket coverage and smupsp errormode1/enablemcapolling0/errortype1 semantics; specify FF5/FFE and SyncFlood relevance, fresh MP1-specific MCA/BERT/CPER/WHEA plus reset-cause evidence, reset/firmware/boot/OS deadlines, SMU telemetry/power/thermal/clock recovery, aborts, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
