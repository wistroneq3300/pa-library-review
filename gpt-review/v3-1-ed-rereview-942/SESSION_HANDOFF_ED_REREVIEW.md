# Engineering Decision Re-review Handoff

- Completed formal queue: **514 / 942**; append-only review events: **665**.
- Last formal review: `Reliability|73|Wistron-System RAS-00793-V002` / `3f1f72228616e30a` (formal queue sequence 514; review event 665).
- Next source-verified pending identity: `Reliability|74|Wistron-System RAS-00794-V002` / `2a8c31f315fd8149` (first missing formal queue sequence 515).
- Latest disposition: RETAINED_PENDING_NBIF_PARITY_UNCORRECTABLE_ERROR_0514; nBIF faults may affect several downstream PCIe paths, including boot or management, so recovery must enumerate dependencies rather than only confirm OS return. The comment marker with a mandatory reset creates a direct source contradiction. Since immediate reset discards volatile context, a fresh persistent record and OOB timeline are required to prove the selected nBIF source caused the event. The remaining project decision is case-specific: Resolve Reliability row 73 Wistron-System RAS-00793-V002: state whether the commented --nbionbif errortype=1 command is intended; map nBIF links/dependencies and define iohub_instance/group11/struct4; prove UCE/reset semantics; define FF5/FFE threshold raw values and restoration; specify fresh MCA/BERT/CPER source/severity, reset/boot and attached-I/O recovery deadlines for each OS, aborts, OOB recovery and RDIMM relevance. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
