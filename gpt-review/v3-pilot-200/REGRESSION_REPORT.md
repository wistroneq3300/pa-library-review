# V3 Pilot Regression Report

## Scope

- 200 unique cases across six sheets were compared against the exact XLSX row, DeepSeek review, GPT V2 review and applicable history.
- Mechanical checks verify uniqueness, legal values, required fields, source hashes and duplicate-reason similarity. They do not claim semantic correctness.
- No DUT, BMC, switch, storage, GPU or environmental fixture was operated.

## Regression gates

- Test purpose preserved: no known V3 candidate replaces stress with inventory, firmware update with version read, full scope with one representative device, or long duration with a short smoke test.
- Duration/iteration preserved: conflicts are labeled `SOURCE_CONFLICT`; the agent may not choose one silently.
- Execution location preserved: host OS, BMC/HMC, Redfish, peer endpoint and physical operator boundaries are explicit.
- Stable target identity: GPU UUID/BDF, PCIe BDF, storage enclosure/slot/serial/namespace, NIC/RDMA port/peer and USB controller/path are required where applicable.
- Safety not relaxed: reclassified cases retain readiness/approval gates. No raw-device write, blind fault injection, firmware flash, AC/DC cycle or environmental margin action is made ready by classification alone.
- PASS not claimed: all 200 records have `pass_claimed=false` and `hardware_tested=false`.

## Agent-understanding regression findings

Isolated same-model-family validators found real document defects and forced revision in cases including:

- 51: ordinary sensor discrepancies incorrectly terminated the remaining required collection.
- 56: physical I2C bus/address identity was not separated from command-ready IPMI routing/address bytes.
- 60-61: sensor capability/routing and OOB user-access channel/ID/selector semantics were incomplete.
- 63: a blanket SEL allocation `0000h` rule confused field-specific sentinels and exhausted free space.
- 68: a one-page Redfish collection read could truncate pagination.
- 70: WebUI GPU identity and dynamic Power sampling/skew were not deterministic.
- 72: SMBIOS Type 25 lacked a raw-table source, handle correlation and absent-structure policy.
- 84: ordinary sensor discrepancies could truncate remaining safe cross-interface evidence collection.
- 164: non-portable `ipmitool fru list` assumption.
- 165: 15-minute planning metadata could be mistaken for traffic dwell.
- 175: loop boundary, canonical delete containment, storage-reserve evidence, rail definitions and mandatory end-to-end integrity.
- 180: every-bay disposition, immediate protected-device interlocks, full 12-hour scope and dew-point/rail controls.
- 187: boot/ping success, immutable failed-cycle policy and no retry replacement.
- 189: private `usbPoll` proof, BDF-anchored path identity and DC/evidence safety.
- 195: exhaustive preserve-all comparison and task timeout/stall/terminal semantics.
- 197: ordered intermediate-image manifest and per-hop BIOS security/health gates.

Each listed defect was corrected and revalidated CLEAR. Failures were attributed to the document, handoff or model-planning boundary instead of being automatically blamed on the model.

Across the pilot, 160 contracts received isolated same-model-family understanding validation and 40 were explicitly not selected/not required by the recorded risk-pattern policy. No `PENDING*`, `REVISION_REQUIRED`, `NOT_VALIDATED` or missing validation status remains.

## Residual limitations

- Validation used isolated agents from the same model family, not an independent model or hardware execution environment.
- Cases not selected for isolated material-change validation still received per-case semantic review and static regression checks, but their agent-understanding status is explicitly recorded as not selected/not required where applicable.
- Vendor-private tool semantics remain pending in the individual cases; V3 does not claim external proof where public documentation cannot establish them.

## Verdict

No known safety, automation-classification or Test Intent regression remains in the 200 proposed records. This is a document-review result only, not DUT validation.
