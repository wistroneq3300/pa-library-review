# Engineering Decision Re-review Handoff

- Completed formal queue: **512 / 942**; append-only review events: **663**.
- Last formal review: `Reliability|71|Wistron-System RAS-00791-V002` / `77f8846ef212bef7` (formal queue sequence 512; review event 663).
- Next source-verified pending identity: `Reliability|72|Wistron-System RAS-00792-V002` / `7ec17283f36105cf` (first missing formal queue sequence 513).
- Latest disposition: RETAINED_PENDING_IOHUB_PARITY_UCP_ERROR_0512; A leading comment marker can mean an example, disabled feature or editorial artifact; all three have different execution authority. The sequence errortype 0/1/2 suggests related modes but does not define UCP severity. Because threshold and SyncFlood settings can change the outcome, guessing the acronym or uncommenting the line could convert a nominally correctable case into a reset-producing one. The remaining project decision is case-specific: Resolve Reliability row 71 Wistron-System RAS-00791-V002: state whether the commented errortype=2 command is intended for execution; define IOHUB UCP and its correctable/uncorrectable/reset semantics; map instance0/group7/struct1; define FF5/FFE threshold encoding and restoration; specify exact MCA/APEI/WHEA oracle for each OS, timeout, aborts, OOB recovery, RDIMM relevance and full restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
