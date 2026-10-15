# Retrospective Impact Audit — 2026-10-15

Scope: targeted re-check of the valid 891 completed reviews against ED-33 through ED-52.
This is not a recount or a full re-review. `completed_count` remains 891.

## Affected review records

| Source key | Decision | Active classification | Correction reason |
|---|---|---|---|
| `Functionality|340|Wistron-BIOS-00007-V003` | ED-39 | `REQUIRES PACKAGE / USER CONFIRMATION` | BIOS upgrade remains the functional intent; AFULnx, AFUEFI, BMC Flash or another approved method is selected by Project SPEC without erasing the AFULnx/AFUEFI source mismatch. |
| `Functionality|341|Wistron-BIOS-00008-V003` | ED-39 | `REQUIRES PACKAGE / USER CONFIRMATION` | BIOS downgrade remains the functional intent; project approval binds the downgrade-capable tool and anti-rollback policy while preserving the same-version AFUEFI source text as a conflict. |
| `Functionality|342|Wistron-BIOS-00009-V003` | ED-39 | `REQUIRES PACKAGE / USER CONFIRMATION` | Same-version BIOS reflash is the retained purpose; Project SPEC selects the supported tool and records whether AFULnx or the source AFUEFI path was actually covered. |
| `Functionality|343|Wistron-BIOS-00010-V005` | ED-39 | `REQUIRES PACKAGE / USER CONFIRMATION` | The case is an upgrade/downgrade cycle test. Project Test Plan must define whether 100 means flash operations or upgrade/downgrade pairs, version order, per-round checks, stop conditions and recovery. |
| `Functionality|347|Wistron-BIOS-00014-V002` | ED-40 | `REQUIRES PACKAGE / USER CONFIRMATION` | Corrupt-image rejection and downgrade/anti-rollback rejection are separate mechanisms and separate evidence checkpoints; the project may select one or both but cannot cross-credit a single rejection. |
| `Functionality|375|Wistron-BIOS-00042-V002` | ED-41 | `REQUIRES PACKAGE / USER CONFIRMATION` | One testcase may contain PCI Hot-Plug and SR-IOV, but each function has independent state, behavior and evidence; VF success never proves actual hot-plug behavior. |
| `Functionality|387|Wistron-BIOS-00054-V002` | ED-42 | `MANUAL ONLY` | Both User and Administrator Password roles are required, with separate set/authentication/privilege/clear/recovery evidence; Administrator success cannot substitute for User coverage. |
| `Functionality|388|Wistron-BIOS-00055-V002` | ED-43 | `MANUAL ONLY` | Use a project Secure Boot matrix whose enabled/disabled, signed/unsigned OS, PK and MOK states align with the expected boot result; do not mutate keys or MOK without approval. |
| `Functionality|391|Wistron-BIOS-00058-V003` | ED-44 | `MANUAL ONLY` | Quiet Boot and Boot Device remain in one testcase with separate visible-presentation, enumeration, order-configuration and actual-boot checkpoints; no universal timing or initialization meaning is assumed. |
| `Functionality|397|Wistron-BIOS-00064-V002` | ED-45 | `MANUAL ONLY` | Discard Changes and Exit is accepted only when an unsaved edit is discarded and the previously saved value remains after exit; the contradictory save criterion is not used. |
| `Functionality|399|Wistron-BIOS-00066-V002` | ED-45 | `MANUAL ONLY` | Discard Changes and Reset must discard the pending edit across reset and retain the prior saved value; a saved edit is not PASS evidence. |
| `Functionality|401|Wistron-BIOS-00068-V002` | ED-45 | `MANUAL ONLY` | The standalone Discard Changes control removes the pending edit and leaves the prior saved value intact; it does not prove that the edited value can be saved. |
| `Functionality|404|Wistron-BIOS-00071-V002` | ED-45 | `MANUAL ONLY` | Restore User Defaults must recall the approved stored user-default profile and prove its values; merely completing Save is insufficient. |
| `Functionality|429|Wistron-BIOS-00096-V003` | ED-46 | `MANUAL ONLY` | This is Firmware Image Selection, not proof of update. Validate browse/select/cancel or staging behavior without crediting firmware-update coverage unless a separately approved commit occurs. |
| `Functionality|430|Wistron-BIOS-00097-V003` | ED-46 | `MANUAL ONLY` | Firmware Update requires pre-version, an approved update, required activation/reset, BIOS-homepage target-version readback and normal boot; version equality alone does not validate all regions. |
| `Functionality|432|Wistron-BIOS-00099-V003` | ED-47 | `MANUAL ONLY` | The SMBIOS Event Log viewer is reviewed as read-only: enter the page, verify logs/fields/records and navigation; unrelated setting changes, defaults or clearing do not count. |
| `Functionality|435|Wistron-BIOS-00102-V003` | ED-47 | `MANUAL ONLY` | The BMC self-test log is read-only first: page access, displayed records/fields and UI navigation are the acceptance scope unless Project SPEC identifies a separate writable control. |
| `Functionality|437|Wistron-BIOS-00104-V003` | ED-47 | `MANUAL ONLY` | View System Event Log is a read-only viewer check; preserve and inspect records and navigation without substituting setting persistence, Load Default or log clearing. |
| `Functionality|453|Wistron-BIOS-00120-V003` | ED-48 | `MANUAL ONLY` | AMD Memory Configuration Status follows actual platform capability: approved change/save/reboot/readback/restore when writable, or authoritative display comparison when read-only, with unequal coverage recorded. |
| `Functionality|458|Wistron-BIOS-00125-V003` | ED-49 | `MANUAL ONLY` | Retain the source-required PCIe Compliance Mode functional change. A default/read-only observation is partial evidence only and cannot complete the setting-change objective. |
| `Functionality|464|Wistron-BIOS-00131-V003` | ED-46 | `MANUAL ONLY` | This variant covers Firmware Image Selection and its browse/cancel/stage boundary; do not infer or credit an update unless a separately approved commit lifecycle runs. |
| `Functionality|465|Wistron-BIOS-00132-V003` | ED-46 | `MANUAL ONLY` | Update Image is a complete firmware lifecycle with pre-version, approved flash, activation/reset, BIOS target-version confirmation and boot health; extra regions/configuration remain Project SPEC scope. |
| `Functionality|467|Wistron-BIOS-00134-V003` | ED-47 | `MANUAL ONLY` | The SMBIOS Event Log viewer is read-only first; verify presentation, fields, records and navigation without changing settings, loading defaults or clearing evidence. |
| `Functionality|470|Wistron-BIOS-00137-V003` | ED-47 | `MANUAL ONLY` | BMC self-test log acceptance is read-only page/record/field/navigation evidence. Any actual writable page control is a separate Project SPEC-defined extension. |
| `Functionality|472|Wistron-BIOS-00139-V003` | ED-47 | `MANUAL ONLY` | View System Event Log is read-only first; settings changes, Load Default and Clear Log are excluded from viewer acceptance and existing evidence is preserved. |
| `Functionality|477|Wistron-BIOS-00144-V002` | ED-50 | `BLOCKED` | Define AMD Secure Processor Version through the applicable vendor field/path and expected value source; the review must not invent a utility, offset or value and the TBD source still lacks executable semantics. |
| `Functionality|557|Wistron-BIOS-00224-V005` | ED-50 | `BLOCKED` | Cache SRAM Type must map to an exact SMBIOS or vendor-defined field rather than being guessed from adjacent Supported/Current SRAM fields; empty grep is not evidence. |
| `Functionality|628|Wistron-BIOS-00295-V005` | ED-50 | `BLOCKED` | The Reserved-field case requires an exact structure/offset/length and applicable SMBIOS version; do not silently move Type 17 scope to Type 32 or accept an empty grep. |
| `Functionality|629|Wistron-BIOS-00296-V005` | ED-50 | `BLOCKED` | Boot Status is a Type 32 concept, not a Type 17 Memory Device field. The Master conflict remains until the owner approves Type 32 correction or names a real Type 17 target; no empty grep PASS. |
| `Functionality|659|Wistron-BIOS-00326-V005` | ED-50 | `BLOCKED` | The Type 38 label BYTE is not a defined acceptance field. Require exact offset/length/semantics and Vendor SPEC; do not substitute a neighboring byte or accept blank grep output. |
| `Functionality|708|Wistron-BIOS-00376-V002` | ED-51 | `BLOCKED` | ENGINEER DECISION PENDING remains controlling: do not choose TSEG range coverage or SmiHandler4 trace and do not authorize debug BIOS flash or undocumented register operations. |
| `Functionality|713|Wistron-BMC-00003-V008` | ED-52 | `REQUIRES PACKAGE / USER CONFIRMATION` | Target remains BMC. Project SPEC binds versions, direction, host state, activation/reset, approved update method, criteria and recovery; these are readiness inputs rather than an irreducible blocker. |
| `Functionality|714|Wistron-BMC-00004-V007` | ED-52 | `REQUIRES PACKAGE / USER CONFIRMATION` | Target remains BMC and the actual Redfish or other update path is Project SPEC-selected. Fixed credentials, untrusted TLS and unadvertised actions are excluded from the formal recommendation. |
| `Functionality|718|Wistron-BMC-00008-V007` | ED-52 | `REQUIRES PACKAGE / USER CONFIRMATION` | Target remains FPGA. Project SPEC binds the update path and host/reset/activation state; a BMC update path or powered-state assumption cannot silently replace FPGA coverage. |
| `Functionality|720|Wistron-BMC-00010-V007` | ED-52 | `REQUIRES PACKAGE / USER CONFIRMATION` | Target is HIB-CPLD as named by the testcase; the source's FPGA wording remains recorded as a conflict and cannot redirect the image. Project SPEC binds the approved method and lifecycle. |
| `Functionality|722|Wistron-BMC-00012-V008` | ED-52 | `REQUIRES PACKAGE / USER CONFIRMATION` | Target is DCSCM-CPLD as named by the testcase; do not substitute FPGA. Preserve the source conflict while Project SPEC binds device selector, approved update path, activation and independent recovery. |

## Result

- Affected records: **36**
- Completed-count change: **0**
- Active classification after correction: 336 Manual Only, 180 Requires Package / User Confirmation, 315 Fully Automatable, 60 Blocked.
- Remaining explicit engineer decision: BIOS 00376 only.
- Master XLSX, `data/tests.json`, Source Identity, hashes, source snapshots and historical review text remain unchanged.
- Each changed record contains a source-key-bound `engineering_decision_update` overlay with checkpoints, readiness inputs, coverage and verdict boundaries.
