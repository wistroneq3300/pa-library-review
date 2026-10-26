# Engineering Decision Re-review Handoff

- Completed formal queue: **503 / 942**; append-only review events: **654**.
- Last formal review: `Reliability|61|Wistron-System RAS-00781-V002` / `8b33d1a15b1f2567` (formal queue sequence 503; review event 654).
- Next source-verified pending identity: `Reliability|62|Wistron-System RAS-00782-V002` / `85fa301eae7f07e3` (first missing formal queue sequence 504).
- Latest disposition: RETAINED_PENDING_PCIE_SLOT_1~N_0503; An LCRC fault is detected by the receiving link partner and normally drives replay, so the injection-side label alone does not prove where evidence should appear. TX and RX coverage requires traffic in the corresponding direction plus counters tied to the mapped port. An OS may not emit a generic AER message for every corrected link replay, making link/NIC counters and packet integrity more reliable than a broad log grep. The remaining project decision is case-specific: Resolve Reliability row 61 Wistron-System RAS-00781-V002: provide PCIe slot/NIC-to-socket/die/NBIO/core/port coverage and vendor proof errortype 0/1 mean LCRC TX/RX with observing-side semantics; justify ECC RDIMM; define isolated bidirectional traffic, direction-specific link/AER/NIC counters and packet/replay/retrain thresholds; approve 7EF6030/masks/DPC/SyncFlood relevance, supported OS, timeout, aborts, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
