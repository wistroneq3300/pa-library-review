# Engineering Decision Re-review Handoff

- Completed formal queue: **549 / 942**; append-only review events: **700**.
- Last formal review: `Reliability|119|Wistron-GPU RAS-00020-V003` / `b6f9efdf842a9ac9` (formal queue sequence 549; review event 700).
- Next source-verified pending identity: `Reliability|120|Wistron-GPU RAS-00021-V003` / `b1180b1e17ab0beb` (first missing formal queue sequence 550).
- Latest disposition: RETAINED_PENDING_DECODE_UNCORRECTABLE_ERROR_(FATAL)_RECORD_0549; A fatal record can end in-band access, so the test cannot rely solely on running the decoder afterward. More importantly, a GFX type4 command and an SDMA-named Script represent different component coverage until proven equivalent. Device1 must be mapped stably and its own preexisting records tracked; a device0 UMC query cannot establish freshness. The remaining project decision is case-specific: Resolve Reliability row119 Wistron-GPU RAS-00020-V003: confirm Fatal rather than the copied Correctable step label; decide GFX block2 as command/sample show versus SDMA as Script path names; prove type4 and explicit UUID/BDF/device1 target; explain or replace device0 UMC baseline; approve table6.3 Fatal/MCE fields, dynamic identity/freshness, containment/reset and persistent OOB evidence, no-retry recovery, boot/GPU health and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
