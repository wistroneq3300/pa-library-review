# Engineering Decision Re-review Handoff

- Completed formal queue: **409 / 942**; append-only review events: **560**.
- Last formal review: `Functionality|2245|Wistron-BMC Sanity-00027-V001` / `082a24ce32a1e9dc` (formal queue sequence 409; review event 560).
- Next source-verified pending identity: `Functionality|2246|Wistron-BMC Sanity-00028-V001` / `27790cef3fc6c7eb` (first missing formal queue sequence 410).
- Latest disposition: row-2245 is resolved using authoritative IPMI Diagnostic Interrupt semantics as a one-shot high-risk NMI/crashdump test with platform-specific OS oracle, workload isolation, console/dump readiness and recovery; prior read-only claims are rejected. No DUT action ran.
- Integrity disposition: formal checkpoint 200 was fully validated and pushed at `4185ff58`; the locked 942 queue hash is unchanged. Forty-nine initial formal records plus events 201-355 are authoritative; 151 out-of-scope records remain historical.
- Protected sources: unchanged.
- DUT execution: none.
