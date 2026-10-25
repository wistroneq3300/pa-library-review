# Engineering Decision Re-review Handoff

- Completed formal queue: **185 / 942**; append-only review events: **336**.
- Last formal review: `Functionality|2016|Wistron-BMC-01036-V002` / `a78fba275501d201` (formal queue sequence 185; review event 336).
- Next source-verified pending identity: `Functionality|2017|Wistron-BMC-01037-V002` / `56b9d2b4274925b6` (first missing formal queue sequence 186).
- Latest disposition: NM Pending and Source Conflict are resolved without inventing an acronym: NM stays an opaque Master domain, while a signed Project crosswalk defines physical instances, TEMP_IBC_NM scope and companion records across complete IB/OOB/Web evidence. No ipmitool, authentication, NM/TEMP_IBC_NM read, Web login/capture, module/link action, log clear, BMC/host or DUT action ran.
- Integrity disposition: the event-0200 checkpoint reproduced the locked 942 queue hash. Forty-nine initial formal records plus events 201-336 are authoritative; 151 out-of-scope records remain historical and do not affect metrics. Push is withheld until 200 formal identities pass the overlay validator.
- Protected sources: unchanged.
- DUT execution: none.
