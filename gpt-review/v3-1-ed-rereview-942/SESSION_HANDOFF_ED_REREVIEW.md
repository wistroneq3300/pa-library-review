# Engineering Decision Re-review Handoff

- Completed formal queue: **513 / 942**; append-only review events: **664**.
- Last formal review: `Reliability|72|Wistron-System RAS-00792-V002` / `7ec17283f36105cf` (formal queue sequence 513; review event 664).
- Next source-verified pending identity: `Reliability|73|Wistron-System RAS-00793-V002` / `3f1f72228616e30a` (first missing formal queue sequence 514).
- Latest disposition: RETAINED_PENDING_NBIF_PARITY_CORRECTABLE_ERROR_0513; nBIF sits on PCIe-facing NBIO paths, so a parity event may affect multiple downstream devices even when classified correctable. The presence of iohub_instance in an nBIF command is not self-explanatory and must be decoded from the tool. A correctable record is only meaningful when source bank/count and dependent link health show containment without hidden retrain or reset. The remaining project decision is case-specific: Resolve Reliability row 72 Wistron-System RAS-00792-V002: map NBIO to nBIF instances/links and define iohub_instance under --nbionbif plus group11/struct4; prove errortype=0 CE semantics; define FF5/FFE threshold encoding, raw before/target/restore and rationale; specify exact CE MCA/APEI/WHEA source/count and attached-I/O no-reset oracle for each OS, timeout, aborts, OOB recovery, RDIMM relevance and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
