# Engineering Decision Re-review Handoff

- Completed formal queue: **560 / 942**; append-only review events: **711**.
- Last formal review: `Reliability|131|Wistron-HW Robust-00466-V003` / `4b4b2cf161c4b4f6` (formal queue sequence 560; review event 711).
- Next source-verified pending identity: `Reliability|133|Wistron-HW Robust-00011-V002` / `82d53149b8d3e7f7` (first missing formal queue sequence 561).
- Latest disposition: RETAINED_PENDING_TEST_CONNECTIONS_BETWEEN_FPGA_1_AND_HMC_I2C-2_0560; This row can be exercised remotely because it supplies a precise HMC-side combined transaction. Its engineering uncertainty is not physical access but semantic attribution: bus3 must be HMC I2C-2,0x11 must be FPGA1, and0x0400 must safely return meaningful three-byte status. The unrelated same-code SEL row makes variant-bound evidence essential. Once those facts are supplied, one bounded read plus path-specific counters is appropriate coverage. The remaining project decision is case-specific: Resolve Reliability row131 variant4b4b2cf161c4b4f6 (not same-code row155): provide PID1114953 mapping from HMC I2C-2 to bus3 and FPGA1 at0x11, define register0x0400 combined-read safety and expected three-byte decoder, bus ownership, timeout/NACK/retry criteria, HMC/FPGA telemetry and recovery. Confirm physical probing/photos are not core acceptance unless separately scoped. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
