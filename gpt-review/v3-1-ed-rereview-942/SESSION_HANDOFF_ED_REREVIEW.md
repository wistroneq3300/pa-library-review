# Engineering Decision Re-review Handoff

- Completed: **117 / 942**
- Last reviewed: `Functionality|928|Wistron-BMC-00218-V002` / `1a253502f6adcc41`
- Next source-verified pending identity: `Functionality|929|Wistron-BMC-00219-V002` / `e667fde9ca47b711`
- Latest disposition: Secure LDAP is removed from Pending as a parameterized two-write contract: approved LDAP CA installation/active trust, then one complete `ldaps://` object with certificate identity, live auth/role/local-fallback and restoration proof. NonSecure remains separate. No CA or LDAP change was executed.
- Protected sources: unchanged.
- DUT execution: none.
