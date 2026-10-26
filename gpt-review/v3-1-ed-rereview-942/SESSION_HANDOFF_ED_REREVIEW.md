# Engineering Decision Re-review Handoff

- Completed formal queue: **550 / 942**; append-only review events: **701**.
- Last formal review: `Reliability|120|Wistron-GPU RAS-00021-V003` / `b1180b1e17ab0beb` (formal queue sequence 550; review event 701).
- Next source-verified pending identity: `Reliability|121|Wistron-GPU RAS-00022-V003` / `19a252634d5e7f05` (first missing formal queue sequence 551).
- Latest disposition: RETAINED_PENDING_DECODE_UNCORRECTABLE_ERROR_(NON-FATAL)_RECORD_0550; Deferred poison is dangerous because failure may occur on later consumption rather than at injection. The returned addresses and VMID must belong to a disposable process, and the Bus error must be limited to that consumer. A header-only non-fatal JSON sample and unrelated device0 UMC count cannot prove device2 record freshness or safe recovery. The remaining project decision is case-specific: Resolve Reliability row120 Wistron-GPU RAS-00021-V003: prove block2/type8/device2 implements the intended deferred non-fatal poison and reconcile the SDMA Script name; explain device0 UMC baseline or replace with device2 freshness; provide disposable process/allocation with logical/physical/VMID provenance; complete table6.4 decoded fields; define Bus error scope, non-fatal/no-reset oracle, poison clear/recovery, data/GPU/host health, aborts and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
