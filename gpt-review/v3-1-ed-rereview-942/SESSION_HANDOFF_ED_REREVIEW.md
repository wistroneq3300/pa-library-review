# Engineering Decision Re-review Handoff

- Completed formal queue: **521 / 942**; append-only review events: **672**.
- Last formal review: `Reliability|81|Wistron-System RAS-00801-V003` / `cc1bc275ad782f03` (formal queue sequence 521; review event 672).
- Next source-verified pending identity: `Reliability|82|Wistron-System RAS-00802-V003` / `0f95914a22d01f24` (first missing formal queue sequence 522).
- Latest disposition: RETAINED_PENDING_MP1_(SMU)_CORRECTABLE_ERROR_0521; MP1 is the SMU controller, so a nominally correctable injected event can affect firmware services even when Linux continues running. The linked script name references GMI3, which could drive a different injection path. Errorindex0 and mcapolling mode require vendor decoding, and acceptance must include no reset/UCE escalation plus continued sensor, thermal and power control—not just tool PASS. The remaining project decision is case-specific: Resolve Reliability row 81 Wistron-System RAS-00801-V003: reconcile the GMI3-correctable Script URL with MP1/SMU coverage; define MP1 block/errorindex0, socket coverage and smupsp errormode1/enablemcapolling0/errortype0 semantics; state whether UCE/BERT Criteria is escalation-only; specify exact fresh CE/no-reset evidence, SMU telemetry/power/thermal/clock health, FFE/debug-setting relevance, OS timeout, aborts and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
