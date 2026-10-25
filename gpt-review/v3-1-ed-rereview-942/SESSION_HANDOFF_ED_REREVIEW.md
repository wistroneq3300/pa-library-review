# Engineering Decision Re-review Handoff

- Completed formal queue: **254 / 942**; append-only review events: **405**.
- Last formal review: `Functionality|2086|Wistron-AMD SVM-00130-V003` / `da153127ac6e8017` (formal queue sequence 254; review event 405).
- Next source-verified pending identity: `Functionality|2087|Wistron-AMD SVM-00131-V003` / `46555a2c93cd14fe` (first missing formal queue sequence 255).
- Latest disposition: row-2086 is resolved as a parameterized one-shot GFX CRC-write poison test that preserves m5/ext15/ext62, both UMC and GC evidence layers, protected complete CPER collection and signed recovery. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged. Forty-nine initial formal records plus events 201-355 are authoritative; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
