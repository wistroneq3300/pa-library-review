# Engineering Decision Re-review Handoff

- Completed formal queue: **510 / 942**; append-only review events: **661**.
- Last formal review: `Reliability|69|Wistron-System RAS-00789-V002` / `49a104626752f07f` (formal queue sequence 510; review event 661).
- Next source-verified pending identity: `Reliability|70|Wistron-System RAS-00790-V002` / `cb06cc47b636c48a` (first missing formal queue sequence 511).
- Latest disposition: RETAINED_PENDING_IOHUB_PARITY_ECC_CORRECTABLE_ERROR_0510; IOHUB group and structure identifiers are implementation-specific, so a syntactically valid tuple can inject the wrong internal block. Threshold encoding may invert intuitive numeric meaning; FF5 to FFE cannot be interpreted safely without register documentation. Correctable acceptance requires one new corrected bank/count event with continued service, not merely the absence of a crash. The remaining project decision is case-specific: Resolve Reliability row 69 Wistron-System RAS-00789-V002: map socket/die/NBIO to IOHUB instances and decode groupid 7/structid 1; prove errortype=0 correctable parity semantics; define MCA threshold FF5/FFE encoding, before/target/restore and rationale; specify exact CE MCA/APEI/WHEA source/status/count plus no-reset oracle for each supported OS, timeout, aborts, OOB recovery, RDIMM relevance and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
