# Engineering Decision Re-review Handoff

- Completed formal queue: **511 / 942**; append-only review events: **662**.
- Last formal review: `Reliability|70|Wistron-System RAS-00790-V002` / `cb06cc47b636c48a` (formal queue sequence 511; review event 662).
- Next source-verified pending identity: `Reliability|71|Wistron-System RAS-00791-V002` / `77f8846ef212bef7` (first missing formal queue sequence 512).
- Latest disposition: RETAINED_PENDING_IOHUB_PARITY_ECC_UNCORRECTABLE_ERROR_0511; An immediate reset removes volatile error context, so the result needs firmware-reserved or OOB evidence tied to the selected IOHUB source. A retained BERT record can predate the injection unless baseline identity and freshness are established. The threshold change may alter when escalation occurs; without decoding FF5/FFE, the test could validate threshold behavior rather than a single UCE. The remaining project decision is case-specific: Resolve Reliability row 70 Wistron-System RAS-00790-V002: map IOHUB instance/group7/struct1 and prove errortype=1 ECC-UCE/reset semantics; define MCA threshold FF5/FFE encoding, raw before/target/restore and interaction with SyncFlood; specify exact fresh MCA/BERT/CPER source/severity for each OS, reset/firmware/boot deadlines, supported OS/kernel, aborts, OOB recovery, RDIMM relevance and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
