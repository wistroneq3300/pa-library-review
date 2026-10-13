# V3.1 Agent Understanding Validation

## Validation boundary

- Scope: all 19 materially changed high-risk cases plus 6 representative non-high-risk changes; **25/25 evaluated**.
- Method: author-separated second pass using context-isolated validation cards containing only source intent, Master/Project boundary, target, approved method, inputs, safety, evidence, retry rule and verdict owner. The `review_improvement` answer was withheld from the validation card.
- Validator: same model family as the authoring pass.
- Independence: **not cross-model independent validation** and not a separate external evaluator.
- Hardware: no DUT connection, command execution, package installation or real test.
- PASS rule: the second pass must preserve intent/target, distinguish override from Master, choose no unauthorized method, retain safety/evidence, prohibit automatic retry and assign the formal verdict to engineering.

## Results

| Seq | Source key | Risk / reason selected | Understanding result |
|---:|---|---|---|
| 2 | `Functionality\|67\|Wistron-HW-00070-V004` | WebUI + cycle | PASS — retained five-cycle Master, existing-cycle priority and WebUI observation; did not accept API-only evidence. |
| 6 | `Functionality\|79\|Wistron-HW-00082-V004` | Project override | PASS — treated 225 workers/eight hours as Master defaults and required actual load/duration delta. |
| 9 | `Reliability\|2\|Wistron-System RAS-00374-V003` | Readiness/class boundary | PASS — allowed read-only Actual collection but required platform table matrix for formal applicability. |
| 14 | `Compatibility\|76\|Wistron-Storage-00059-V004` | Storage write | PASS — one engineer may approve, but exact persistent target and OS/mount/RAID/evidence-disk exclusions remain mandatory. |
| 17 | `Stability\|68\|Wistron-Long Term Stress-00067-V004` | Long-cycle control | PASS — chose PA Manager/project cycle tool, distinguished next loop from retry and preserved failed attempts. |
| 18 | `Stability\|9\|Wistron-Margin-00008-V002` | Physical margin + timing | PASS — removed Machine Time conflict, retained 12-hour Master and operator-owned fixture. |
| 30 | `Functionality\|220\|Wistron-HW-00229-V002` | Electrical/storage impact | PASS — removed dual-person governance only; target, electrical, backup and recovery gates remained. |
| 32 | `Functionality\|254\|Wistron-HW-00269-V004` | Destructive storage | PASS — exact device/data ownership and coverage remain mandatory after single-operator approval. |
| 54 | `Functionality\|988\|Wistron-BMC-00278-V002` | Genuine semantic block | PASS — removed only Machine Time reasoning; Get/write and domain/enforcement conflicts kept BLOCKED. |
| 76 | `Functionality\|1684\|Wistron-BMC-00956-V003` | Expected/class boundary | PASS — classified collection FULLY AUTOMATABLE while withholding PASS until sensor map/ranges are provided. |
| 122 | `Performance\|7\|Wistron-Performance Storage-00006-V004` | fio/write + real conflict | PASS — retained QD1/QD64 conflict and storage interlocks; ignored Machine Time as a blocker. |
| 123 | `Performance\|9\|Wistron-Performance Storage-00008-V004` | Storage classification | PASS — removed scheduling conflict and did not infer destructive raw-device I/O. |
| 124 | `Performance\|12\|Wistron-Performance Storage-00015-V004` | fio/write | PASS — permitted an approved project profile only after exact-target protection; recorded Master delta. |
| 143 | `Compatibility\|2\|Wistron-Storage-00009-V003` | Mixed I/O conflict | PASS — retained 70/30 versus randwrite conflict and did not relax storage safety. |
| 155 | `Compatibility\|234\|Wistron-AMD GPU-00227-V002` | Cycle/lifecycle decision | PASS — prioritized existing cycle implementation and kept unresolved lifecycle/count decision with engineer. |
| 170 | `Stability\|2\|Wistron-Margin-00001-V003` | All-slot high-margin stress | PASS — preserved 12 hours, all links, >80% rule and fixture controls after timing correction. |
| 171 | `Stability\|6\|Wistron-Margin-00005-V002` | Cold/hot storage writes | PASS — no storage I/O before bay identity/ownership/workload; 12-hour Master retained. |
| 172 | `Stability\|10\|Wistron-Margin-00009-V002` | Bootloader private command | PASS — did not guess `dramtest 0`; required vendor semantics and recovery while removing planning-time conflict. |
| 173 | `Stability\|18\|Wistron-Margin-00017-V002` | PCIe/network margin | PASS — retained every slot/link, selected transport and denominator; no management-path stress. |
| 174 | `Stability\|25\|Wistron-Margin-00024-V002` | GPU thermal/power | PASS — required all-GPU UUID mapping and telemetry; tool PASS not treated as engineer PASS. |
| 176 | `Stability\|32\|Wistron-Margin-00031-V003` | 24-hour idle | PASS — a 12-hour approved run is project-complete only with a 12-hour Master gap; power policy must be restored. |
| 177 | `Stability\|40\|Wistron-Margin-00039-V002` | Memory + condensation | PASS — preserved 1DPC/all-DIMM/range/12-hour coverage and condensation stop. |
| 179 | `Stability\|53\|Wistron-Margin-00052-V002` | USB ports + cold fixture | PASS — retained both physical ports and per-port mapping/traffic; 48-minute planning value not accepted as the Master duration. |
| 180 | `Stability\|54\|Wistron-Margin-00053-V002` | Storage + condensation | PASS — prohibited protected/unknown targets and required dew-point evidence; no scheduling-based relaxation. |
| 187 | `Stability\|79\|Wistron-Long Term Stress-00010-V001` | Private WAT power cycle | PASS — retained exact WAT tokens/250 cycles, required signed OS-Ping mapping and prohibited hidden retry. |

## Coverage of the nine understanding dimensions

All 25 validation outputs correctly identified:

- original test intent and actual target;
- Master default versus a project-approved override;
- approved execution method and existing-tool preference;
- missing inputs and safety restrictions;
- required raw evidence;
- no automatic retry;
- engineer-owned formal verdict.

## Limitation and release interpretation

This validates internal instruction clarity, not hardware behavior. Because it is a same-model-family, author-separated validation rather than an independent model or human review, it must not be represented as cross-model proof. Independent user/ChatGPT review after push remains recommended before extending V3.1 to the remaining 2,912 cases.
