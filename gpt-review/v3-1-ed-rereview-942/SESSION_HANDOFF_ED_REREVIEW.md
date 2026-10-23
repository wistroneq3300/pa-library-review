# Engineering Decision Re-review Handoff

- Completed: **166 / 942**
- Last reviewed: `Functionality|979|Wistron-BMC-00269-V003` / `b2633d7f0c511699`
- Next source-verified pending identity: `Functionality|980|Wistron-BMC-00270-V003` / `1692245e76e444b5`
- Latest disposition: AlwaysOff AC power policy is removed from Pending as a parameterized REQUIRES CONFIRMATION case. It separately verifies WebUI/Redfish persistence after BMC reboot and human-controlled complete AC loss from required On/Off pre-states, then restores policy and reaches OS Ready; no write, reboot or power action ran.
- Protected sources: unchanged.
- DUT execution: none.
