# Engineering Decision Re-review Handoff

- Completed formal queue: **255 / 942**; append-only review events: **406**.
- Last formal review: `Functionality|2087|Wistron-AMD SVM-00131-V003` / `46555a2c93cd14fe` (formal queue sequence 255; review event 406).
- Next source-verified pending identity: `Functionality|2088|Wistron-AMD SVM-00132-V003` / `65478846b4398361` (first missing formal queue sequence 256).
- Latest disposition: row-2087 is resolved as a parameterized SDMA subblock-130 CRC-write poison test preserving its UMC ext15/CRC and SDMA ext62 evidence, full CPER set, containment and recovery gates. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged. Forty-nine initial formal records plus events 201-355 are authoritative; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
