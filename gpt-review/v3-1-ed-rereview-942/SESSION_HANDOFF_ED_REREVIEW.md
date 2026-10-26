# Engineering Decision Re-review Handoff

- Completed formal queue: **507 / 942**; append-only review events: **658**.
- Last formal review: `Reliability|65|Wistron-System RAS-00785-V002` / `5193fa789d14b164` (formal queue sequence 507; review event 658).
- Next source-verified pending identity: `Reliability|67|Wistron-System RAS-00787-V002` / `233717a503ada0c6` (first missing formal queue sequence 508).
- Latest disposition: RETAINED_PENDING_PCIE_SLOT_1~N_0507; ACS capability may reside on an upstream bridge rather than the NIC function, and capability presence does not show that the control relevant to the test is enabled. Because the host resets immediately, pre-reset OS buffers are unreliable; a new CPER record must be distinguished from retained BERT data and tied to the injected hierarchy. Reusing one NBIO tuple cannot demonstrate slot 1~N coverage without a physical-to-logical matrix. The remaining project decision is case-specific: Resolve Reliability row 65 Wistron-System RAS-00785-V002: provide per-slot NIC/BDF/upstream-to-NBIO/core/port mapping; identify the exact ACS-capable function and required ACS control bits; prove errortype=4 ACS-fatal semantics and justify ECC RDIMM; decode/approve 7EF6030, masks, DPC/SyncFlood/reset policy; define fresh target-correlated BERT/CPER fields, supported OS/kernel, reset/boot timeout, aborts, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
