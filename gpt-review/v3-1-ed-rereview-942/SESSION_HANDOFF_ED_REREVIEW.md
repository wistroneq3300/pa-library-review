# Engineering Decision Re-review Handoff

- Completed formal queue: **73 / 942**; append-only review events: **224**.
- Last formal review: `Functionality|1079|Wistron-BMC-00369-V002` / `2f9b3065b6642849` (formal queue sequence 73; review event 224).
- Next source-verified pending identity: `Functionality|1084|Wistron-BMC-00374-V002` / `c24d080be22f3673` (first missing formal queue sequence 74).
- Latest disposition: Set SEL Time UTC Offset (IB) is removed from Pending/Conflict/BLOCKED using official Storage 0Ah/5Dh and exact 5Ch target/restore readback. It requires a distinct approved two-byte target, immutable SEL chronology, containment of DST/49h writers, explicit confirmation and exact baseline restore; 49h resets the offset to 07FFh and is prohibited. No command, clock change, clear, retry or DUT action ran.
- Integrity disposition: the event-0200 checkpoint reproduced the locked 942 queue hash. Forty-nine initial formal records plus events 201-224 are authoritative; 151 out-of-scope records remain historical and do not affect metrics. Push is withheld until 200 formal identities pass the overlay validator.
- Protected sources: unchanged.
- DUT execution: none.
