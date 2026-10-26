# Engineering Decision Re-review Handoff

- Completed formal queue: **440 / 942**; append-only review events: **591**.
- Last formal review: `Functionality|2278|Wistron-HW-00245-V003` / `e3e7b3795f1858bb` (formal queue sequence 440; review event 591).
- Next source-verified pending identity: `Functionality|2279|Wistron-HW-00246-V003` / `b2b7e9abe2a97edb` (first missing formal queue sequence 441).
- Latest disposition: RETAINED_PENDING_PFR_BMC_UPDATE_PROVISIONING_AND_UNPROVISION_RECOVERY; This row combines BMC capsule flashing with AST1060 provisioning and destructive unprovisioning. Exact lifecycle, key provenance, capsule compatibility, activation oracle and programmer/golden recovery are core OEM security semantics; ED-07 requires separate flash authorization and they cannot be guessed. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
