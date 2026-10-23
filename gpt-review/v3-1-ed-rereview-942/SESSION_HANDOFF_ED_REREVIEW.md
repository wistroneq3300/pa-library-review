# Engineering Decision Re-review Handoff

- Completed: **180 / 942**
- Last reviewed: `Functionality|994|Wistron-BMC-00284-V004` / `b804dc50fc09ee4a`
- Next source-verified pending identity: `Functionality|995|Wistron-BMC-00285-V004` / `7f821fe8f0c3434d`
- Latest disposition: BMC Warm Reset (IB) is removed from Pending as a parameterized REQUIRES CONFIRMATION case. Raw 0x06/0x03 retains warm internal/interface cleanup semantics and requires independently staged IPMI/Redfish/WebUI/SOL recovery, stable MAC/IP/config and unchanged host boot/power, without borrowing Cold Reset evidence. No action ran.
- Protected sources: unchanged.
- DUT execution: none.
