# Engineering Decision Re-review Handoff

- Completed formal queue: **561 / 942**; append-only review events: **712**.
- Last formal review: `Reliability|133|Wistron-HW Robust-00011-V002` / `82d53149b8d3e7f7` (formal queue sequence 561; review event 712).
- Next source-verified pending identity: `Reliability|134|Wistron-HW Robust-00012-V002` / `f70a1f1bf17fcdd2` (first missing formal queue sequence 562).
- Latest disposition: RETAINED_PENDING_TEST_CONNECTIONS_BETWEEN_HMC_I2C-3_AND_FPGA_2_0561; The exact same0x11/register tuple appears on a different HMC controller for FPGA1, showing that address alone cannot identify the target. This case succeeds only if bus0 is proven to represent HMC I2C-3 and the reply is decoded as FPGA2 data. A bounded transaction plus controller-specific telemetry provides that functional evidence; mandatory probing would be an unsourced change of method. The remaining project decision is case-specific: Resolve Reliability row133 Wistron-HW Robust-00011-V002: provide PID1114953 mapping from HMC I2C-3 to bus0 and FPGA2 at0x11, define register0x0400 combined-read safety and expected three-byte decoder, ownership/exclusive access, timeout/NACK/retry criteria, HMC I2C-3/FPGA2 telemetry and recovery. Confirm physical probing/photos are not core acceptance unless separately scoped. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
