# Engineering Decision Re-review Handoff

- Completed formal queue: **82 / 942**; append-only review events: **233**.
- Last formal review: `Functionality|1205|Wistron-BMC-00495-V002` / `0b80bfd6fd426cca` (formal queue sequence 82; review event 233).
- Next source-verified pending identity: `Functionality|1206|Wistron-BMC-00496-V002` / `30095b90395e299a` (first missing formal queue sequence 83).
- Latest disposition: Get SEL Time UTC Offset (OOB) is removed from Pending/Conflict/BLOCKED using standard Storage 0Ah/5Ch, an exact two-byte signed-minute decode, 07FFh sentinel handling and a timestamped Project timezone/DST oracle. OOB transport errors are not unsupported evidence; IB credit, log clearing, setters and retry are prohibited. No DUT action ran.
- Integrity disposition: the event-0200 checkpoint reproduced the locked 942 queue hash. Forty-nine initial formal records plus events 201-233 are authoritative; 151 out-of-scope records remain historical and do not affect metrics. Push is withheld until 200 formal identities pass the overlay validator.
- Protected sources: unchanged.
- DUT execution: none.
