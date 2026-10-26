# Engineering Decision Re-review Handoff

- Completed formal queue: **585 / 942**; append-only review events: **736**.
- Last formal review: `Reliability|163|Wistron-System RAS-00120-V002` / `bb5c8d8401bf531d` (formal queue sequence 585; review event 736).
- Next source-verified pending identity: `Reliability|164|Wistron-System RAS-00121-V002` / `60ca12f10d68558c` (first missing formal queue sequence 586).
- Latest disposition: RETAINED_PENDING_DDR_TRANSIENT_C_A_PARITY_ERROR_0585; A DDR C/A parity event is identified by the channel-local alert and MCA path, not by a generic parity string. FTrace must be armed before injection or the transient event can be missed. Clean-to-set register deltas, serial handling and bank13 extlog timing together establish causality; trying alternative injector configurations or repeating the event would destroy that attribution and increase crash risk. The remaining project decision is case-specific: Resolve Reliability row163 Wistron-System RAS-00120-V002: approve GNR/BIOS/BMC/OS, CScripts version/hash/license, socket0/MC0/ch0/DIMM topology and exact platform `injectCMDParity` configuration; map/restore all BIOS/GRUB/DFX/C-A-parity/FTrace knobs; define clean/asserted mc_status_shadow and alertsignal fields, expected severity, MC bank13/status, serial retry/recovery and extlog_mem_event timing; provide OOB crash/no-retry recovery. ED-16 therefore prohibits executing or declaring PASS until the named vendor authority, isolated target, deterministic oracle and recovery are approved. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
