# Engineering Decision Re-review Handoff

- Completed formal queue: **551 / 942**; append-only review events: **702**.
- Last formal review: `Reliability|121|Wistron-GPU RAS-00022-V003` / `19a252634d5e7f05` (formal queue sequence 551; review event 702).
- Next source-verified pending identity: `Reliability|122|Wistron-GPU RAS-00023-V003` / `94064205fded68e5` (first missing formal queue sequence 552).
- Latest disposition: RETAINED_PENDING_DECODE_BAD_PAGE_THRESHOLD_EXCEED_RECORD_0551; A threshold testcase is about state transition, not the success of individual injections. Without initial count and threshold, three addresses may be too few, excessive or already beyond the boundary. Since retired-page state can persist and addresses may contain live data, each page must be proven disposable and the run must stop as soon as the expected transition occurs. The remaining project decision is case-specific: Resolve Reliability row121 Wistron-GPU RAS-00022-V003: reconcile device0 baseline versus device3 and UMC block0/method5/type4 versus SDMA Script; prove ownership/alignment/safety of 0x10000/0x11000/0x12000 or provide replacements; define initial bad-page count, threshold and per-event arithmetic; supply full table6.5 threshold fields/severity/action, early-stop rule, page-retirement persistence/cleanup, fatal/reset recovery, aborts and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
