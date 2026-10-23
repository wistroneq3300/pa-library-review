# Engineering Decision Re-review Handoff

- Completed: **116 / 942**
- Last reviewed: `Functionality|927|Wistron-BMC-00217-V002` / `3afda17902865d3c`
- Next source-verified pending identity: `Functionality|928|Wistron-BMC-00218-V002` / `1a253502f6adcc41`
- Latest disposition: NonSecure LDAP is removed from Pending and its certificate-upload conflict is reconciled using upstream openbmctool/RFC semantics: certificate trust belongs to secure LDAP. This row is isolated-lab-only with disposable secrets, auth/role/local-fallback proof and guaranteed restore. No LDAP change was executed.
- Protected sources: unchanged.
- DUT execution: none.
