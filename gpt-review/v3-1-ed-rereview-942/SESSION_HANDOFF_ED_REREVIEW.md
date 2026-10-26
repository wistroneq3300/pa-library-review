# Engineering Decision Re-review Handoff

- Completed formal queue: **509 / 942**; append-only review events: **660**.
- Last formal review: `Reliability|68|Wistron-System RAS-00788-V002` / `7491d7925bdf0274` (formal queue sequence 509; review event 660).
- Next source-verified pending identity: `Reliability|69|Wistron-System RAS-00789-V002` / `49a104626752f07f` (first missing formal queue sequence 510).
- Latest disposition: RETAINED_PENDING_OCP_SLOT_1~N_0509; Poison on an OCP device can traverse management, storage or fabric traffic, so the consumer and service boundary are part of the test, not optional post-checks. TX/RX direction is relative to the mapped port and must be tied to requester/completer roles. Without physical module identity, the identical PCIe tuple cannot prove a separate OCP target or coverage point. The remaining project decision is case-specific: Resolve Reliability row 68 Wistron-System RAS-00788-V002: provide OCP module/interface/service-to-NBIO/core/port coverage and distinct scope versus PCIe row 67; prove pcieerror errortype 6/7 TX/RX semantics and relation to einjbiopcie 6; decide correctable/nonfatal severity; define independent OOB path, isolated poison-consuming traffic and exact AER/process/packet/I/O/checksum plus service outcomes; approve 7EF6030/masks/DPC/SyncFlood, OS, timeout, aborts, RDIMM relevance and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
