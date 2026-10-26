# Engineering Decision Re-review Handoff

- Completed formal queue: **524 / 942**; append-only review events: **675**.
- Last formal review: `Reliability|84|Wistron-System RAS-00804-V003` / `ba085f1216ec7124` (formal queue sequence 524; review event 675).
- Next source-verified pending identity: `Reliability|85|Wistron-System RAS-00805-V003` / `3124da9422825039` (first missing formal queue sequence 525).
- Latest disposition: RETAINED_PENDING_MP5_UNCORRECTABLE_ERROR_0524; MP5 UCE is targeted at a CCD-scoped firmware path, so a platform may reboot while losing part of its compute topology or management telemetry. BERT must be proven fresh and associated with MP5/index0, not merely present after boot. Continuous OOB timing plus core/NUMA and sensor/control checks closes the gap between reset completion and actual recovery. The remaining project decision is case-specific: Resolve Reliability row 84 Wistron-System RAS-00804-V003: map MP5 to socket/CCD/core/NUMA and define smupsp errormode2/CCD0/mcapolling0/errorindex0/errortype1 semantics; specify FFE/debug/SyncFlood relevance, fresh MP5-specific MCA/BERT/CPER/WHEA/SEL and reset-cause evidence, reset/firmware/boot/OS deadlines, compute/memory/sensor/power/thermal recovery, aborts, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
