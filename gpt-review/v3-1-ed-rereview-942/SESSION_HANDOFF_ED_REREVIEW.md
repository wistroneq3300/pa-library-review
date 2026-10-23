# Engineering Decision Re-review Handoff

- Completed: **186 / 942**
- Last reviewed: `Functionality|1000|Wistron-BMC-00290-V003` / `dd1f49dd7900779a`
- Next source-verified pending identity: `Functionality|1001|Wistron-BMC-00291-V003` / `e8dadb024eea3985`
- Latest disposition: Reset Watchdog Timer (IB) is removed from Pending as a parameterized REQUIRES CONFIRMATION one-shot start/restart. Raw 0x06/0x22 is standard; complete 0x25 baseline/readback must prove safe policy and countdown reload, with no Set fallback, log clear or retry. No action ran.
- Protected sources: unchanged.
- DUT execution: none.
