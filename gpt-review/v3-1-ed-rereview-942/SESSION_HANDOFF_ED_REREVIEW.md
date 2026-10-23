# Engineering Decision Re-review Handoff

- Completed: **183 / 942**
- Last reviewed: `Functionality|997|Wistron-BMC-00287-V004` / `60db580bf4d4ce5a`
- Next source-verified pending identity: `Functionality|998|Wistron-BMC-00288-V004` / `faed2e965c6593f4`
- Latest disposition: Set ACPI Power State (IB) is removed from Pending as a parameterized REQUIRES CONFIRMATION notification matrix. IPMI states raw 0x06/0x06 records/reports ACPI state and does not itself control actual power; every source S/D/7F mapping is retained, Get 0x07 readback and management/thermal safeguards are required. No action ran.
- Protected sources: unchanged.
- DUT execution: none.
