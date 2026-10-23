# Engineering Decision Re-review Handoff

- Completed: **123 / 942**
- Last reviewed: `Functionality|934|Wistron-BMC-00224-V002` / `bf9e2cca700c8ffa`
- Next source-verified pending identity: `Functionality|935|Wistron-BMC-00225-V003` / `eaf5d18c97193323`
- Latest disposition: Replace LDAP certificate is removed from Pending after pinned source proved certificate-only Root-CA input, a Redfish ReplaceCertificate branch and a distinct non-atomic legacy DELETE/PUT branch. Exact target object, isolation, live trust/auth and mode-specific rollback are mandatory. No certificate was changed.
- Protected sources: unchanged.
- DUT execution: none.
