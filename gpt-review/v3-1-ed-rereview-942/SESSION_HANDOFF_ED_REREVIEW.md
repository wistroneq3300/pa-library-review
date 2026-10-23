# Engineering Decision Re-review Handoff

- Completed: **184 / 942**
- Last reviewed: `Functionality|998|Wistron-BMC-00288-V004` / `faed2e965c6593f4`
- Next source-verified pending identity: `Functionality|999|Wistron-BMC-00289-V004` / `4bbb9618d214e206`
- Latest disposition: Get ACPI Power State (IB) is removed from Pending as a parameterized FULLY AUTOMATABLE read. Raw 0x06/0x07 must return and decode both standard state bytes; the BMC-recorded value is compared to, not substituted for, actual host state, and the source's host-On condition requires S0/00. No action ran.
- Protected sources: unchanged.
- DUT execution: none.
