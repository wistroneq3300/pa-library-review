# Engineering Decision Re-review Handoff

- Completed formal queue: **555 / 942**; append-only review events: **706**.
- Last formal review: `Reliability|125|Wistron-HW Robust-00003-V002` / `4aa07058f5d51da0` (formal queue sequence 555; review event 706).
- Next source-verified pending identity: `Reliability|126|Wistron-HW Robust-00004-V002` / `c1d8780b110e71c9` (first missing formal queue sequence 556).
- Latest disposition: RETAINED_PENDING_TEST_CONNECTIONS_BETWEEN_BMC_I2C-6_AND_UPHY0_FROM_FIRST_PG548_0555; The stated objective is a connection and the Procedure operationalizes it through a BMC mux selection followed by expected bus replies. Therefore physical probing is not intrinsically required. Port0 selection is only an intermediate state change: coverage depends on exact UPHY0 downstream responses, mapping proof and restoration without disrupting the same mux's port2 path. The remaining project decision is case-specific: Resolve Reliability row125 Wistron-HW Robust-00003-V002: provide PID1114953 mapping from BMC I2C-6 to bus5, first-PG548 mux0x71 port0 and exact UPHY0 endpoints/replies; define initial/readback values,0x01 bit-preservation semantics, owner/exclusive access, bounded timeout/NACK criteria, exact restore and BMC recovery. Confirm no mandatory physical probe/photo coverage unless separately approved. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
