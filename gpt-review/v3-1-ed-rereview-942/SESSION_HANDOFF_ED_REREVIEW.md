# Engineering Decision Re-review Handoff

- Completed formal queue: **594 / 942**; append-only review events: **745**.
- Last formal review: `Reliability|173|Wistron-System RAS-00130-V002` / `a93a3a5aabfd3309` (formal queue sequence 594; review event 745).
- Next source-verified pending identity: `Reliability|174|Wistron-System RAS-00131-V003` / `98b00aacd79ce4bb` (first missing formal queue sequence 595).
- Latest disposition: RETAINED_PENDING_ONE_BANK_VLS_REGION_0594; The first CE only increments the rank counter; the second reaches threshold and sets overflow while halted. `go()` is the boundary where BIOS SMM consumes that state and programs VLS, so durable region/control fields and cleared threshold state are the decisive evidence. `copy_in_progress` may transition too quickly to sample and therefore cannot be mandatory. Exact rank/bank/device identity matters because later second-strike cases rely on this region. The remaining project decision is case-specific: Resolve Reliability row173 Wistron-System RAS-00130-V002: approve GNR/BIOS/BMC/OS, DIMM topology/POR exception, CScripts version/hash/license and Spare-SMI/threshold2/ADDDC mappings; prove the exact socket0/ch0/dimm0/rank0/subchannel0/bankgroup0/bank0/device target and mask0x3, define count0x2/overflow and ADDDC_REGION/CONTROL failed/buddy/clear oracle plus SMM timeout and OOB no-retry recovery/restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
