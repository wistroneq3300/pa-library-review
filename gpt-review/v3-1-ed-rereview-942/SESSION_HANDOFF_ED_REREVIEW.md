# Engineering Decision Re-review Handoff

- Completed formal queue: **480 / 942**; append-only review events: **631**.
- Last formal review: `Reliability|36|Wistron-System RAS-00756-V003` / `36d6894753ea0c8d` (formal queue sequence 480; review event 631).
- Next source-verified pending identity: `Reliability|37|Wistron-System RAS-00757-V003` / `58b1c86f67ce3aca` (first missing formal queue sequence 481).
- Latest disposition: RETAINED_PENDING_CORRECTABLE_ERROR_0480; The source provides a strong register-level signature—ERRCORSTS.RE—but leaves the physical endpoint, PCH port and X/Y hierarchy runtime-dependent. It also assumes the package's generic CE token produces that specific bit. Those identities must be proven together because a PCH root port may host an essential device. With a verified map and package contract, one bounded injection is feasible under operator control, so RPUC is appropriate and the unresolved mapping is recorded as a source conflict. The remaining project decision is case-specific: Resolve Reliability row 36 Wistron-System RAS-00756-V003: approve the physical PCH endpoint/BDF to Cscript port and pcieX/portY map, endpoint/management dependencies, ITP/CScripts version/hash and proof `errType='ce'` selects Receiver Error; define mandatory ERRCORSTS.RE/Windows PCIe CE and link/device-health oracle, recovery and BIOS restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
