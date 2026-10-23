# Engineering Decision Re-review Handoff

- Completed formal queue: **72 / 942**; append-only review events: **223**.
- Last formal review: `Functionality|1078|Wistron-BMC-00368-V002` / `9d062674246f0ffb` (formal queue sequence 72; review event 223).
- Next source-verified pending identity: `Functionality|1079|Wistron-BMC-00369-V002` / `2f9b3065b6642849` (first missing formal queue sequence 73).
- Latest disposition: Get SEL Time UTC Offset (IB) is removed from Pending/Conflict/BLOCKED using official read-only Storage 0Ah/5Ch. The response is exactly two little-endian bytes decoded as signed minutes in -1440..+1440, except 07FFh means unspecified; Project timezone/DST expectation and optional chronology skew remain runtime parameters. No host-time inference, setter, log clear, retry or DUT action is allowed.
- Integrity disposition: the event-0200 checkpoint reproduced the locked 942 queue hash. Forty-nine initial formal records plus events 201-223 are authoritative; 151 out-of-scope records remain historical and do not affect metrics. Push is withheld until 200 formal identities pass the overlay validator.
- Protected sources: unchanged.
- DUT execution: none.
