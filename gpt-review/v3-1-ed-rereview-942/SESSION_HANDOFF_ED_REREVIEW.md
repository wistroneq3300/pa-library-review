# Engineering Decision Re-review Handoff

- Completed formal queue: **516 / 942**; append-only review events: **667**.
- Last formal review: `Reliability|75|Wistron-System RAS-00795-V002` / `adb4d5710dedca6b` (formal queue sequence 516; review event 667).
- Next source-verified pending identity: `Reliability|76|Wistron-System RAS-00796-V002` / `b78909bbfec7fe5d` (first missing formal queue sequence 517).
- Latest disposition: RETAINED_PENDING_DF_CCM_WDT_ERROR_0516; CCM participates in coherent memory/fabric behavior, so successful reboot alone cannot demonstrate recovery; memory and inter-socket error state must be checked. A sticky SyncFlood bit and generic watchdog message look identical across several source cases. Therefore the test needs errortype mapping and CPER/MCA identifiers that specifically distinguish CCM from IOM and CPU watchdogs. The remaining project decision is case-specific: Resolve Reliability row 75 Wistron-System RAS-00795-V002: map DF CCM per socket and prove --dferror errortype=1; define FF5/FFE threshold relevance/raw values; provide S5_RESET_STATUS SyncFlood pre-state/clear/freshness semantics; specify CCM-specific MCA/BERT/CPER fields distinct from IOM/CPU, supported OS, reset/boot deadlines, memory/xGMI/coherency recovery, aborts, OOB recovery, RDIMM relevance and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
