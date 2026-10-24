# Engineering Decision Re-review Handoff

- Completed formal queue: **99 / 942**; append-only review events: **250**.
- Last formal review: `Functionality|1583|Wistron-BMC-00853-V004` / `225a021cf739cbff` (formal queue sequence 99; review event 250).
- Next source-verified pending identity: `Functionality|1622|Wistron-BMC-00893-V002` / `f2599d0a0fe990d3` (first missing formal queue sequence 100).
- Latest disposition: Power Restore Policy - Always off remains genuine Engineering Decision Pending and BLOCKED. Items/Procedure require AlwaysOff and remain-off after AC restoration, while Criterion 1 literally requires AlwaysOn and the same remain-off result; choosing a presumed typo would redefine the source-controlled variable and oracle. The separately required CPU swap/boot checkpoint is retained, but awaits an owner policy/result ruling, approved physical service/power/recovery contract and fresh review. No DUT action ran.
- Integrity disposition: the event-0200 checkpoint reproduced the locked 942 queue hash. Forty-nine initial formal records plus events 201-250 are authoritative; 151 out-of-scope records remain historical and do not affect metrics. Push is withheld until 200 formal identities pass the overlay validator.
- Protected sources: unchanged.
- DUT execution: none.
