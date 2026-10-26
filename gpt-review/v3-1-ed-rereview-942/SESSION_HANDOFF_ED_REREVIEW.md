# Engineering Decision Re-review Handoff

- Completed formal queue: **566 / 942**; append-only review events: **717**.
- Last formal review: `Reliability|139|Wistron-HW Robust-00017-V002` / `37c95a4c4b78b4a9` (formal queue sequence 566; review event 717).
- Next source-verified pending identity: `Reliability|140|Wistron-HW Robust-00018-V002` / `dfcfe4a97400f3b1` (first missing formal queue sequence 567).
- Latest disposition: RETAINED_PENDING_TEST_CONNECTIONS_BETWEEN_BMC_I2C-9,_HMC-7_AND_M.2_0566; Nothing in the Procedure asks to touch the M.2 module; the test is framed as a BMC management-bus reply. The real coverage gap is attribution: the unexplained HMC-7 path and0x6a response must be bound to a specific installed device, since PCIe enumeration and sideband addressing are separate identities. A decoded bounded read can prove functional sideband reachability without risking reseat or data-path disturbance. The remaining project decision is case-specific: Resolve Reliability row139 Wistron-HW Robust-00017-V002: define HMC-7 and provide PID1114953 mapping from BMC I2C-9/bus8 through it to the exact M.2 slot/device at0x6a; define register0x00d5 combined-read safety and expected six-byte decoder, slot/BDF/serial correlation, ownership, safe scan policy, timeout/NACK criteria and BMC/HMC/M.2 recovery. Confirm no physical probing/reseat is required unless separately scoped. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
