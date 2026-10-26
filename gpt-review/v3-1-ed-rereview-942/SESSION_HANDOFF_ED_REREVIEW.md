# Engineering Decision Re-review Handoff

- Completed formal queue: **505 / 942**; append-only review events: **656**.
- Last formal review: `Reliability|63|Wistron-System RAS-00783-V002` / `1a962f5e681757c6` (formal queue sequence 505; review event 656).
- Next source-verified pending identity: `Reliability|64|Wistron-System RAS-00784-V002` / `575cc488fa99e7d5` (first missing formal queue sequence 506).
- Latest disposition: RETAINED_PENDING_PCIE_SLOT_1~N_0505; Immediate reset destroys volatile context, so evidence must be captured by firmware/BMC or OOB console before relying on post-boot logs. TX and RX cannot be run as one sequence unless the first boot and link state are fully restored, or the second result inherits an unknown fault state. The reuse of errortype 2 in another command family means numeric equality alone cannot establish identical ECRC severity semantics. The remaining project decision is case-specific: Resolve Reliability row 63 Wistron-System RAS-00783-V002: prove pcieerror errortype 2/3 TX/RX semantics and reconcile their use with einjbiopcie errortype 2; decide correctable Criteria versus mandatory immediate reset; provide slot/NIC-to-NBIO/core/port coverage; approve 7EF6030/masks/DPC/SyncFlood policy, durable ECRC source/severity evidence, separate TX/RX reset/boot/link deadlines, supported OS, aborts, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
