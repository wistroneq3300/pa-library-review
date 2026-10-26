# Engineering Decision Re-review Handoff

- Completed formal queue: **481 / 942**; append-only review events: **632**.
- Last formal review: `Reliability|37|Wistron-System RAS-00757-V003` / `58b1c86f67ce3aca` (formal queue sequence 481; review event 632).
- Next source-verified pending identity: `Reliability|38|Wistron-System RAS-00758-V003` / `36a4e3d67dba63bd` (first missing formal queue sequence 482).
- Latest disposition: RETAINED_PENDING_UNCORRECTABLE_ERROR_0481; The expected CTE bit is the core oracle, yet the source directs an uncorrectable event to a corrected-status register while the detailed eDPC row names ERRUNCSTS. That is not a harmless placeholder: reading the wrong register could falsely report failure or conceal another bit. The exact register, severity and PCH target must be owner-approved before one destructive injection. Since these are resolvable platform inputs, RPUC remains correct instead of BLOCKED. The remaining project decision is case-specific: Resolve Reliability row 37 Wistron-System RAS-00757-V003: decide the authoritative completion-timeout CTE register/bit (source ERRCORSTS versus row-34 ERRUNCSTS), severity/mask and expected recovery; approve PCH endpoint/BDF to port/X/Y mapping, ITP/CScripts version/hash and `uce` semantics, mandatory Windows AER/link/device evidence, optional BMC/UEFI/LED behavior, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
