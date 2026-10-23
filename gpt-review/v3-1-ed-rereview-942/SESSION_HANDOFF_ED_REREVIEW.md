# Engineering Decision Re-review Handoff

- Completed: **170 / 942**
- Last reviewed: `Functionality|983|Wistron-BMC-00273-V003` / `0ec7148b04e4c61a`
- Next source-verified pending identity: `Functionality|984|Wistron-BMC-00274-V003` / `b68f0e7394ae9672`
- Latest disposition: Power on/off is removed from Pending as a parameterized REQUIRES CONFIRMATION case. It preserves one explicitly authorized hard Power Down and one Power Up, stable Off proof, then POST/OS Ready/service recovery; the separate Power Soft, reset, cycle and AC semantics cannot substitute. No action ran.
- Protected sources: unchanged.
- DUT execution: none.
