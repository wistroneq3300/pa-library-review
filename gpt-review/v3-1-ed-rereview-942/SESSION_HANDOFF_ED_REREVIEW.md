# Engineering Decision Re-review Handoff

- Completed formal queue: **558 / 942**; append-only review events: **709**.
- Last formal review: `Reliability|129|Wistron-HW Robust-00007-V003` / `4b2d8ba600afe2f2` (formal queue sequence 558; review event 709).
- Next source-verified pending identity: `Reliability|130|Wistron-HW Robust-00465-V004` / `7c586734242c154f` (first missing formal queue sequence 559).
- Latest disposition: RETAINED_PENDING_TEST_SSIF_CONNECTION_BETWEEN_FPGA_AND_BMC_I2C-1_0558; `ipmitool bmc info` is a valid application-level request but its success is transport-agnostic unless the OS IPMI device and driver are mapped. The row's unique claim is not merely that the BMC answers; it is that the exchange traverses FPGA and BMC I2C-1 via SSIF. That can be evidenced through interface identity and transport error telemetry without mandatory probing, provided alternate IPMI routes are excluded. The remaining project decision is case-specific: Resolve Reliability row129 Wistron-HW Robust-00007-V003: provide the authoritative mapping from the OS IPMI device/driver through FPGA to BMC I2C-1 SSIF, approved ipmitool interface and sudo policy, expected `bmc info` identity fields, proof that no KCS/BT/LAN/alternate fallback was used, and SSIF/I2C/FPGA timeout/retry/error criteria. Confirm physical probing/photos are not core acceptance unless separately approved. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
