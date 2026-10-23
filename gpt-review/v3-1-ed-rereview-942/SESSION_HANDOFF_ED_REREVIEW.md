# Engineering Decision Re-review Handoff

- Completed: **171 / 942**
- Last reviewed: `Functionality|984|Wistron-BMC-00274-V003` / `b68f0e7394ae9672`
- Next source-verified pending identity: `Functionality|985|Wistron-BMC-00275-V003` / `6dadbb370df2544e`
- Latest disposition: Power Soft is removed from Pending as a parameterized REQUIRES CONFIRMATION case. Standard optional ACPI soft-shutdown semantics are used, but PASS requires normal OS shutdown, stable Off and passive SOL evidence; completion, SOL loss, hard fallback or retry cannot pass. No action ran.
- Protected sources: unchanged.
- DUT execution: none.
