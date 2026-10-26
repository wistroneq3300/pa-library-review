# Engineering Decision Re-review Handoff

- Completed formal queue: **530 / 942**; append-only review events: **681**.
- Last formal review: `Reliability|91|Wistron-System RAS-00811-V002` / `7a4e314d622a0dd7` (formal queue sequence 530; review event 681).
- Next source-verified pending identity: `Reliability|92|Wistron-System RAS-00812-V002` / `6cb7ea1fd035c7f1` (first missing formal queue sequence 531).
- Latest disposition: RETAINED_PENDING_FATAL_ERROR_-_SWD_0530; SWD coverage cannot be inferred because adjacent rail types are separate tests that may produce the same reset. The meaningful discriminator is the PMIC SWD status/telemetry at the mapped address. Each voltage comparator and DIMM can have different electrical behavior, so one fixed tuple is insufficient; memory training and a clean workload after rail restoration are necessary before another fatal injection. The remaining project decision is case-specific: Resolve Reliability row 91 Wistron-System RAS-00811-V002: provide PMIC register proof railtype3=SWD and voltagetype0/1 semantics; map every DIMM to socket/die/UMC/channel/slot/dimm, PMIC part/address and Wistron BMC/platform I2C controller/bus/OOB path; approve command continuation and full tuple matrix; define SWD electrical limits/status, PMIC/CPER/BERT/SEL evidence, reset/boot/training deadlines, memory recovery, aborts and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
