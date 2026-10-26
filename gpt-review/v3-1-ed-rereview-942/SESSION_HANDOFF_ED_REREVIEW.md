# Engineering Decision Re-review Handoff

- Completed formal queue: **385 / 942**; append-only review events: **536**.
- Last formal review: `Functionality|2221|Wistron-BMC Sanity-00493-V003` / `98be56b3354f27d7` (formal queue sequence 385; review event 536).
- Next source-verified pending identity: `Functionality|2222|Wistron-BMC Sanity-00005-V001` / `433ac289d56786f1` (first missing formal queue sequence 386).
- Latest disposition: row-2221 is resolved as separate parameterized GPU firmware Upgrade and Downgrade Flash transactions, each retaining real Flash, before/after active-version, no-AC and health evidence and requiring its own one-shot authorization. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged. Forty-nine initial formal records plus events 201-355 are authoritative; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
