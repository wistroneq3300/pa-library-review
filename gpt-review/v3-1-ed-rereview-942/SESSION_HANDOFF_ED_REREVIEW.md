# Engineering Decision Re-review Handoff

- Completed formal queue: **477 / 942**; append-only review events: **628**.
- Last formal review: `Reliability|32|Wistron-System RAS-00752-V003` / `4338611024ae469f` (formal queue sequence 477; review event 628).
- Next source-verified pending identity: `Reliability|34|Wistron-System RAS-00754-V002` / `239b61fa50b51e50` (first missing formal queue sequence 478).
- Latest disposition: RETAINED_PENDING_PCIE_SLOT_1~N_0477; PCIe uncorrectable is a class, not a severity guarantee. Whether an injected bit is non-fatal depends on AER severity/mask and DPC/firmware ownership for the current root port. The target chain and pre-state registers must therefore be captured before a single injection, and recovery must prove the endpoint and host remain usable. Since those mappings and policies can be supplied by the FAE, the case remains gated RPUC rather than BLOCKED. The remaining project decision is case-specific: Resolve Reliability row 32 Wistron-System RAS-00752-V003: approve PCIe slot-to-endpoint/root-port BDF and Cscript socket/port coverage, ITP/CScripts version/hash and exact `uce` AER bit; define current mask/severity/DPC policy proving non-fatal behavior, mandatory Windows WHEA/AER and link/device recovery when management logs/LED are optional, aborts, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
