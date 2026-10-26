# Engineering Decision Re-review Handoff

- Completed formal queue: **493 / 942**; append-only review events: **644**.
- Last formal review: `Reliability|50|Wistron-System RAS-00770-V003` / `6e94b43be5b01832` (formal queue sequence 493; review event 644).
- Next source-verified pending identity: `Reliability|51|Wistron-System RAS-00771-V002` / `7e7d9547cc3c33f7` (first missing formal queue sequence 494).
- Latest disposition: RETAINED_PENDING_MEMORY_SLOT_1~N_0493; Persistent mode is not just a stronger one-shot; its safety depends on duration, access rate and interaction with corrected-error thresholds. A tool PASS at arm time says nothing about how many faults will be emitted or whether closing the process clears hardware state. The essential acceptance evidence is the transition from repeated expected events to no event after the documented clear, with counters stable during a verification access. The remaining project decision is case-specific: Resolve Reliability row 50 Wistron-System RAS-00770-V003: provide slot-to-tuple coverage and approve/correct 0:0:3; define persistent mode arm/status, synthetic trigger, maximum count/rate/duration below thresholds, vendor clear/emergency-stop command and post-clear negative test; decide DRAM-versus-MCA profile; approve tool/spec provenance, CE Linux/Windows/BMC oracle, timeout, aborts, recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
