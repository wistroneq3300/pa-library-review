# Engineering Decision Re-review Handoff

- Completed formal queue: **474 / 942**; append-only review events: **625**.
- Last formal review: `Reliability|29|Wistron-System RAS-00749-V003` / `4f2925a37f403917` (formal queue sequence 474; review event 625).
- Next source-verified pending identity: `Reliability|30|Wistron-System RAS-00750-V003` / `00083be1e440aa34` (first missing formal queue sequence 475).
- Latest disposition: RETAINED_PENDING_MEMORY_CONTROLLER_1~N_0474; A leaky bucket is defined by threshold, time base and decay behavior. None can be established from a single CE log, and the source itself disclaims the BIOS values as inaccurate. The injection count must be calculated with margin from the real threshold and every counter sample tied to a monotonic clock. Because an FAE can provide those parameters and the test purpose is otherwise clear, this is a gated RPUC case with a source conflict, not BLOCKED or a license to invent values. The remaining project decision is case-specific: Resolve Reliability row 29 Wistron-System RAS-00749-V003: provide authoritative correctable-threshold/time-window values and units, counter source/decay rule, controller 1~N tuple/rank coverage, ITP/CScripts version/hash and CE semantics, safe below-threshold count/margin/timing, expected Windows/BMC/UEFI/indicator/health evidence, aborts, recovery and BIOS restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
