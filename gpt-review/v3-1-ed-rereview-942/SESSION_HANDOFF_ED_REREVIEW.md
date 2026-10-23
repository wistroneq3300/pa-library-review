# Engineering Decision Re-review Handoff

- Completed formal queue: **90 / 942**; append-only review events: **241**.
- Last formal review: `Functionality|1433|Wistron-BIOS-00001-V003` / `937cfeeea4f3936c` (formal queue sequence 90; review event 241).
- Next source-verified pending identity: `Functionality|1436|Wistron-BIOS-00004-V003` / `69759b3dcd2307c2` (first missing formal queue sequence 91).
- Latest disposition: BIOS Menu FW Version is removed from Pending/Conflict through a full-source union: FW/BIOS Version, Compliancy and Core Version are separately captured from the actual Main page and independently compared with a Project build-manifest matrix; no field equivalence is guessed. UI evidence is primary, mapped SMBIOS/BMC is corroboration only, and the separate row-1436 flash plus row-365 Core Version identities remain intact. No DUT action ran.
- Integrity disposition: the event-0200 checkpoint reproduced the locked 942 queue hash. Forty-nine initial formal records plus events 201-241 are authoritative; 151 out-of-scope records remain historical and do not affect metrics. Push is withheld until 200 formal identities pass the overlay validator.
- Protected sources: unchanged.
- DUT execution: none.
