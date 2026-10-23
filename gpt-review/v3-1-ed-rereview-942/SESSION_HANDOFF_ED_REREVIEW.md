# Engineering Decision Re-review Handoff

- Completed: **37 / 942**
- Last reviewed: `Functionality|847|Wistron-BMC-00137-V002` / `7c585d8afd245108`
- Next source-verified pending identity: `Functionality|848|Wistron-BMC-00138-V002` / `535ea15699a8f181`
- Latest disposition: Power is removed from Pending as a strict navigation-only WebUI test. It requires semantic separation of the Power link from all destructive controls, one click to the rendered Server power operations view, and proof that no selection, action request, confirmation, power/reachability or event transition occurred; no power operation is authorized.
- Protected sources: unchanged.
- DUT execution: none.
