# Engineering Decision Re-review Handoff

- Completed formal queue: **520 / 942**; append-only review events: **671**.
- Last formal review: `Reliability|80|Wistron-System RAS-00800-V002` / `66acc6e9e349cd5a` (formal queue sequence 520; review event 671).
- Next source-verified pending identity: `Reliability|81|Wistron-System RAS-00801-V003` / `cc1bc275ad782f03` (first missing formal queue sequence 521).
- Latest disposition: RETAINED_PENDING_TXWAFL_UNCORRECTABLE_ERROR_AT_CCD_0520; A TXWAFL fault at a CCD is materially different from the adjacent IOD case: the failure may leave the OS booted while cores, a NUMA node or memory paths are degraded. The location bit and numeric link are vendor encodings, not a topology proof. Therefore acceptance needs a CCD-specific durable source record and post-event CPU/NUMA validation, after the duplicated correctable wording is resolved. The remaining project decision is case-specific: Resolve Reliability row 80 Wistron-System RAS-00800-V002: correct or approve both copies of the correctable acceptance text in this TXWAFL CCD Uncorrectable case; map linknumber0/errorlocation1 to exact socket/CCD/core/NUMA coverage and prove errortype1; define FF5/FFE relevance, containment/reset, fresh CCD-specific MCA/CPER/BERT/SEL fields, OS timeout, compute/NUMA/memory/fabric recovery, aborts, OOB recovery and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
