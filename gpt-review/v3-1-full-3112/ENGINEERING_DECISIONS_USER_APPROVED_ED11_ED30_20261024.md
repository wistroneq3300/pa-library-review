# User-approved engineering decisions ED-11 through ED-30 (2026-10-24)

Status: USER DECISIONS RECORDED; INDEPENDENT ORIGINAL-SOURCE RECONCILIATION AND 942-CASE RE-REVIEW NOT YET COMPLETE.

These are selected decisions from the existing 942-case pending queue, on the existing branch only. They are not a blanket removal of pending status, approval to execute on a DUT, independent QA acceptance, or authorization to change protected original XLSX/JSON.

### ED-11 (A)

- Source Key: `Functionality|2176|Wistron-BIOS-00493-V004`
- Approved intent: Only safe reversible BIOS settings, one setting at a time, with approved target/profile and pre/post evidence; never iterate all/random; no unapproved security/provisioning values.

### ED-12 (A)

- Source Key: `Compatibility|19|Wistron-Processor-00002-V003`
- Approved intent: Retain CPU frequency purpose, correct review-layer measurement and acceptance; do not silently substitute core count.

### ED-13 (A)

- Source Key: `Functionality|1003|Wistron-BMC-00293-V002`
- Approved intent: Draft documented standard BMC Set/Get contract; OEM/vendor bit mappings and target policy remain PENDING until authoritative evidence; no guessed writes.

### ED-14 (A)

- Source Key: `Compatibility|264|Wistron-NV GPU-00257-V002`
- Approved intent: Preserve upgrade and downgrade branches, independently confirm vendor support, image/hardware identity, activation, rollback/recovery; unsupported direction must not be executed.

### ED-15 (A)

- Source Key: `Functionality|2113|Wistron-GB NV PVP HW-00034-V003`
- Approved intent: Perform Gen6 change only when supported capability is verified. N/A must be documented with authoritative platform applicability evidence; defects, missing prerequisites or incompatible firmware are not automatically N/A.

### ED-16 (A)

- Source Key: `Performance|10|Wistron-Performance Storage-00013-V004`
- Approved intent: Retain original 12-hour acceptance, optional separately labeled shorter exploratory/smoke profile cannot replace or PASS the 12-hour coverage.

### ED-17 (A)

- Source Key: `Stability|31|Wistron-Margin-00030-V002`
- Approved intent: Qualified operator establishes and confirms thermal/voltage fixture; agent may read-only verify/collect evidence and run approved planned automation only with explicit pre-execution approval, safety thresholds and OOB recovery.

### ED-18 (A)

- Source Key: `Stability|76|Wistron-Long Term Stress-00075-V002`
- Approved intent: Prepare plan and non-disruptive data collection; numeric PASS/FAIL thresholds require an approved Project SPEC. No PASS, invented 80%-of-line-rate threshold, or workload execution absent approval.

### ED-19 (A)

- Source Key: `Functionality|1072|Wistron-BMC-00362-V003`
- Approved intent: Preserve pre-delete SEL export/hash/evidence; only individually scoped deletion after explicit separate approval and proven single-record semantics/retention/recovery; no full SEL clear substitution.

### ED-20 (A)

- Source Key: `Functionality|2235|Wistron-BMC Sanity-00017-V001`
- Approved intent: Require actual WebUI operation and visual evidence, supplemented by API/task/version/health correlation; no API-only substitution and no unapproved firmware update.

### ED-21 (C)

- Source Key: `Functionality|1781|Wistron-HW-00414-V002`
- Approved intent: Keep both H.265 and HEVC source cases independently identifiable and separately executable/verifiable even if textual content overlaps; do not merge/delete, but still determine each case's intended coverage; no duplicate execution on DUT without safety/readiness approvals.

### ED-22 (A)

- Source Key: `Compatibility|100|Wistron-Storage-00083-V003`
- Approved intent: Human performs required hardware/array preparation; agent monitors true rebuild states and gathers evidence; LED visual confirmation remains human, destructive RAID protection mandatory.

### ED-23 (A)

- Source Key: `Functionality|2223|Wistron-BMC Sanity-00006-V002`
- Approved intent: Correlate API/BMC power state and KVM/visual output; avoid false PASS from blank stale console or successful request only.

### ED-24 (A)

- Source Key: `Functionality|2183|Wistron-BIOS-00500-V003`
- Approved intent: Separately identify Factory Default versus Project Recipe default according to intended case; never use factory default as equivalent to project values without explicit approval; backup and recovery mandatory.

### ED-25 (A)

- Source Key: `Functionality|2269|Wistron-HW-00025-V003`
- Approved intent: Human performs physical CX7 removal/reseat under approved power/ESD procedures; agent collects before/after PCIe/NIC identity, link and health evidence and report; no automated physical-step substitution.

### ED-26 (A)

- Source Key: `Compatibility|150|Wistron-AMD GPU-00135-V002`
- Approved intent: Preserve separate DGEMM stress and distinct dmesg-check variant despite duplicate display code; separate workload/evidence/error criteria, no conclusion from exit code or dmesg alone.

### ED-27 (A)

- Source Key: `Compatibility|424|Wistron-L12 Cluster-00006-V002`
- Approved intent: Separately check fabric traffic/bandwidth, health, alert lifecycle and recovery with independent evidence and approval; avoid a single-dashboard PASS.

### ED-28 (A)

- Source Key: `Reliability|70|Wistron-System RAS-00790-V002`
- Approved intent: RAS injection only with vendor-authorized tool, confirmed exact fault semantics and isolated DUT, explicit approval, aborts, logs and OOB recovery; no speculative injection.

### ED-29 (A)

- Source Key: `Functionality|986|Wistron-BMC-00276-V003`
- Approved intent: Verify full OFF -> ON -> OS Ready state transition, timing and identity/evidence; request success or ping alone cannot confer PASS.

### ED-30 (A)

- Source Key: `Performance|59|Wistron-Performance GPU-00031-V002`
- Approved intent: Preserve RGAT Server MLPerf execution contract and evidence; numeric PASS threshold needs authoritative approved project/spec reference; no self-invented comparator.

## Mandatory application conditions

- Cross-check all 30 approved decisions against the precise original XLSX row, historical engineering decisions, Final Audit and prior review logic. If an irreducible contradiction remains, preserve and report it; do not invent test facts.
- Generalize only reusable principles and preserve source-key/variant-specific approvals separately; do not convert an example into a universal exception.
- Existing execution gates remain unchanged: explicit OK, validated nonproduction targets, device/image compatibility, read-only evidence preservation, recovery and safety controls.
- For unsupported functions, distinguish documented N/A from FAIL, missing information and platform defects. Short smoke tests do not satisfy full-duration qualifications.
- Preserve original Master XLSX and JSON, existing historical records and checkpoints. Do not merge, reset or force push.
- Re-review 942 Source Keys individually from original data, record evidence and per-case disposition; do not falsely force every case to resolved. Report exact remaining pending reasons, independent QA and validator results.
