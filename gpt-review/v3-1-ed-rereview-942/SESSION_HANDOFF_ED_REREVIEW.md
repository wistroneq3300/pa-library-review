# Engineering Decision Re-review Handoff

- Completed: **26 / 942**
- Last reviewed: `Functionality|836|Wistron-BMC-00126-V004` / `2b0c8075417c3767`
- Next source-verified pending identity: `Functionality|837|Wistron-BMC-00127-V004` / `fe77cf6bf08ded24`
- Latest disposition: The ipmitool volatile-rate case is removed from Pending as two non-substitutable checkpoints: full `sol info` must show the bound channel's `Volatile Bit Rate (kbps): 115.2`, and one separately authorized bounded live session must show target-specific readable output and close cleanly. The source's 115200 bps and Criteria's 115.2 kbps are equivalent units, not a conflict.
- Protected sources: unchanged.
- DUT execution: none.
