# Engineering Decision Re-review Handoff

- Completed: **24 / 942**
- Last reviewed: `Functionality|834|Wistron-BMC-00124-V004` / `72a5207cbca9f808`
- Next source-verified pending identity: `Functionality|835|Wistron-BMC-00125-V003` / `a7e1b4b0465f05c2`
- Latest disposition: COM0-to-SOL is removed from Pending as a parameterized IPMI SOL routing and bounded-session test. It remains distinct from physical COM: BMC payload/channel, UART mux, end-to-end serial parameters, session ownership and clean deactivation must be proven, with no unapproved boot/reboot or session takeover.
- Protected sources: unchanged.
- DUT execution: none.
