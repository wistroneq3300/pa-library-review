# Engineering Decision Re-review Handoff

- Completed formal queue: **548 / 942**; append-only review events: **699**.
- Last formal review: `Reliability|117|Wistron-GPU RAS-00009-V003` / `940dc8de2a333670` (formal queue sequence 548; review event 699).
- Next source-verified pending identity: `Reliability|119|Wistron-GPU RAS-00020-V003` / `b6f9efdf842a9ac9` (first missing formal queue sequence 549).
- Latest disposition: RETAINED_PENDING_ADDRESS_COMMAND_PARITY_UNCORRECTABLE_ERROR_INJECTION_0548; A query against device0 does not prove a later command without `-d` targets that device. Because an uncorrectable event can disrupt collection, target identity must be fixed before injection and corroborated by BDF/socket/die in fresh ACA evidence. A merely nonzero total is also insufficient when the source sample already contains prior counts. The remaining project decision is case-specific: Resolve Reliability row117 Wistron-GPU RAS-00009-V003: prove amdgpuras block0/subblock4/type4/method1 means single-shot UMC address/command parity UCE; define the explicit UUID/BDF/device target and why injection omits `-d 0`; reconcile sample 38:00.0 versus 0c:00.0/socket2 and one-versus-two total errors; approve ras_enable activation, exact counter delta, ACA raw-field/severity/containment oracle, dedicated-SUT aborts, recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
