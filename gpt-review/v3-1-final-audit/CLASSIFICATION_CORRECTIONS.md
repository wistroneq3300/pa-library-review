# Classification Corrections

## Distribution

| Classification | V3.1 before | Final Audit effective | Change |
|---|---:|---:|---:|
| FULLY AUTOMATABLE | 12 | 12 | 0 |
| REQUIRES PACKAGE / USER CONFIRMATION | 132 | 139 | +7 |
| MANUAL ONLY | 34 | 27 | -7 |
| BLOCKED | 22 | 22 | 0 |

## ED-31: core WebUI observation

| Seq | Code | Before | After | Case-specific reason |
|---:|---|---|---|---|
| 51 | Wistron-BMC-00175-V003 | REQUIRES | MANUAL ONLY | Ten HSC rows must be human-readable in both Dashboard and Sensor Reading; IPMI/API is corroboration only. |
| 52 | Wistron-BMC-00236-V002 | REQUIRES | MANUAL ONLY | The System panel's rendered fields and readability are the acceptance surface. |
| 53 | Wistron-BMC-00238-V002 | REQUIRES | MANUAL ONLY | The Chassis EROT row/detail and its visible mapping are the function under test. |
| 70 | Wistron-BMC-00056-V003 | REQUIRES | MANUAL ONLY | GPU Name, Version and Power must be observed on BMC WebUI for every GPU. |
| 74 | Wistron-BMC-00889-V002 | REQUIRES | MANUAL ONLY | Link labels, targets and successful WebUI navigation require human-visible page evidence. |

## ED-30: manual setup plus automated core

Each case below was reviewed independently. They share a classification rule,
not an interchangeable execution contract.

| Seq | Code | Automated core after manual setup |
|---:|---|---|
| 170 | Wistron-Margin-00001-V003 | SST network workload, per-link bandwidth and platform telemetry. |
| 171 | Wistron-Margin-00005-V002 | Safe per-bay storage workload, integrity and health collection. |
| 172 | Wistron-Margin-00009-V002 | Vendor-verified U-Boot DRAM diagnostic and BMC service checks. |
| 173 | Wistron-Margin-00017-V002 | All-slot network traffic, counters and error telemetry. |
| 174 | Wistron-Margin-00024-V002 | All-GPU burn and continuous thermal/power/error collection. |
| 175 | Wistron-Margin-00026-V003 | Bounded sandboxed upload/remove script with hash/free-space/BMC health evidence. |
| 176 | Wistron-Margin-00031-V003 | Nonintrusive 24-hour liveness, idle-state and log collection. |
| 177 | Wistron-Margin-00039-V002 | SST memory coverage and ECC/system telemetry. |
| 178 | Wistron-Margin-00046-V002 | Approved cold-cycle controller and per-cycle inventory/log validation. |
| 179 | Wistron-Margin-00052-V002 | Port-mapped USB traffic/integrity and reset/error collection. |
| 180 | Wistron-Margin-00053-V002 | Safe per-target storage workload, integrity and health evidence. |
| 181 | Wistron-Margin-00061-V002 | PA Manager/project warm-reboot cycle control and per-cycle evidence. |

All twelve change from `MANUAL ONLY` to
`REQUIRES PACKAGE / USER CONFIRMATION`. No change authorizes a chamber, rail,
storage write, power operation or workload without the recorded project and
safety gates.

## Resolved case-specific decision

Sequence 182 remains `MANUAL ONLY` under ED-32. The source requires ten
physical AC cable removals after five minutes of combined CPU/DIMM/HDD stress.
An agent may assist with an approved stress plan, monitoring, evidence
collection and reporting, but cannot claim the physical removal. A PDU, BMC
power off, software reboot, or another remote power action is not an equivalent
substitute for this testcase. This ruling is limited to sequence 182 and does
not change the classification of other AC-cycle cases.
