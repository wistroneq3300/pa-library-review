# Engineering Decision Re-review Handoff

- Completed formal queue: **515 / 942**; append-only review events: **666**.
- Last formal review: `Reliability|74|Wistron-System RAS-00794-V002` / `2a8c31f315fd8149` (formal queue sequence 515; review event 666).
- Next source-verified pending identity: `Reliability|75|Wistron-System RAS-00795-V002` / `adb4d5710dedca6b` (first missing formal queue sequence 516).
- Latest disposition: RETAINED_PENDING_DF_IOM_WDT_ERROR_0515; A watchdog reset can produce similar high-level symptoms for different DF blocks, so errortype/source decoding and persistent CPER fields are needed to distinguish IOM from CCM. Reset-cause registers are often sticky; reading one after boot without pre-state/clear semantics cannot attribute the bit to this run. Because DF IOM serves multiple data paths, recovery must include downstream I/O health, not only OS boot. The remaining project decision is case-specific: Resolve Reliability row 74 Wistron-System RAS-00794-V002: map DF IOM per socket and prove --dferror errortype=0 semantics; define FF5/FFE threshold relevance/raw values; provide S5_RESET_STATUS[SyncFlood] persistence and approved pre-state/clear/freshness method; specify IOM-specific fresh BERT/CPER fields, supported OS, reset/firmware/boot/OS deadlines, DF-I/O recovery, aborts, OOB recovery, RDIMM relevance and restoration. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
