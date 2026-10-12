# Agent Understanding Validation

Status: `CALIBRATION 20 VALIDATED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

Date: 2026-10-13

## Validation boundary

- Input was limited to the agent-facing V3 contract in
  `VALIDATION_INPUTS/CALIBRATION_20_CONTRACTS.json`.
- Validators did not receive the source workbook, DeepSeek review, GPT V2
  conclusion, reviewer findings, or this comparison report.
- Three isolated reviewer contexts covered sequences 1-7, 8-14, and 15-20.
- The validators answered the ten required understanding questions and checked
  the eleven requested misinterpretation risks. Full responses are preserved in
  `VALIDATION_OUTPUTS/agent_a.json`, `agent_b.json`, and `agent_c.json`.
- All validators are from the same model family as the primary reviewer. This is
  isolated-context validation, not independent-model validation.
- No DUT command, workload, firmware action, physical action, or hardware test
  was performed.

## Result summary

| Result | Count | Meaning |
| --- | ---: | --- |
| `VALIDATED_CLEAR` | 16 | The validator recovered the intended purpose, target, scope, missing inputs, safe read-only work, operation, evidence, approval, stop, completion, and engineer-judgment boundaries. |
| `VALIDATED_AMBIGUITY_HANDLED` | 4 | The validator correctly detected an intentional source ambiguity and refused to invent a resolution or unsafe executable flow. |
| Document-caused understanding failure | 0 | No calibration contract caused a material scope, device, location, duration, iteration, command, evidence, safety, completion, BLOCKED, or PASS misunderstanding. |
| Platform-handoff failure | 0 | No missing contract transport or field omission was observed in the isolated inputs. |
| Model-planning failure | 0 | No validator proposed an unsafe or materially incorrect execution plan. |

The risk flags in the raw validator outputs are adversarial checks describing
what a future executor must avoid; they are not evidence that those errors were
committed. The comparison below uses the validator's answers, not the count of
flagged hazards.

## Case comparison

| Seq. | Source key | Result | Comparison with confirmed intent |
| ---: | --- | --- | --- |
| 1 | `Functionality\|29\|Wistron-HW-00032-V004` | VALIDATED_CLEAR | Preserved the CRPS offset field, one-block scope, vendor decoder/spec dependency, and read-only boundary. |
| 2 | `Functionality\|67\|Wistron-HW-00070-V004` | VALIDATED_CLEAR | Preserved five N/N-1 PSU firmware transitions through BMC HPM and per-cycle recovery evidence. |
| 3 | `Functionality\|150\|Wistron-HW-00153-V002` | VALIDATED_AMBIGUITY_HANDLED | Kept OS installation and TPM state conditionally visible but refused destructive execution until the owner resolves the source conflict. |
| 4 | `Functionality\|198\|Wistron-HW-00207-V002` | VALIDATED_CLEAR | Identified the physical serial path, peer, electrical/framing inputs and manual connection boundary. |
| 5 | `Functionality\|201\|Wistron-HW-00210-V002` | VALIDATED_CLEAR | Preserved every required USB port in BIOS and the installed OS with topology-mapped evidence. |
| 6 | `Functionality\|79\|Wistron-HW-00082-V004` | VALIDATED_CLEAR | Preserved exactly 225 CPU workers for eight hours and continuous platform-health/recovery evidence. |
| 7 | `Functionality\|87\|Wistron-HW-00090-V004` | VALIDATED_AMBIGUITY_HANDLED | Preserved host DDR, eight hours and 90 percent while refusing to choose between 15 and 9 conflicting worker values. |
| 8 | `Functionality\|2260\|Wistron-BMC-00848-V003` | VALIDATED_CLEAR | Required all five BIOS, in-band IPMI, OOB IPMI, WebUI and Redfish observations at their proper locations. |
| 9 | `Reliability\|2\|Wistron-System RAS-00374-V003` | VALIDATED_CLEAR | Distinguished required ACPI table presence, OS recognition and end-to-end RAS behavior. |
| 10 | `Reliability\|4\|Wistron-System RAS-00378-V003` | VALIDATED_CLEAR | Preserved every mapped second-DIMM target and the manual-injection plus automated-correlation boundary. |
| 11 | `Performance\|3\|Wistron-Performance CPU-00002-V003` | VALIDATED_CLEAR | Kept HPL vendor-appropriate and configuration-matched without applying the AMD CCX path to Intel/Common. |
| 12 | `Performance\|4\|Wistron-Performance DIMM-00003-V004` | VALIDATED_CLEAR | Recovered the fixed STREAM profile, 9.61-GiB footprint, NUMA/thread scope and comparable reference requirement. |
| 13 | `Performance\|15\|Wistron-Performance Networking-00030-V004` | VALIDATED_CLEAR | Understood a 300-second per-port IB write-bandwidth test and did not treat TX depth as duration. |
| 14 | `Compatibility\|76\|Wistron-Storage-00059-V004` | VALIDATED_CLEAR | Preserved twelve-hour 4-KiB mixed I/O on every allowlisted M.2 target and the destructive-data boundary. |
| 15 | `Compatibility\|251\|Wistron-NV GPU-00244-V002` | VALIDATED_CLEAR | Preserved qualified FCT and the full GPU UUID/BDF/upstream-link matrix without inventing a diagnostic module. |
| 16 | `Compatibility\|257\|Wistron-NV GPU-00250-V002` | VALIDATED_CLEAR | Treated 144 as a generation-specific GPU-to-NVSwitch graph, not a portable scalar. |
| 17 | `Stability\|68\|Wistron-Long Term Stress-00067-V004` | VALIDATED_CLEAR | Preserved 1000 physical AC cycles in 48 hours, full population, stable identities and manual PDU boundaries. |
| 18 | `Stability\|9\|Wistron-Margin-00008-V002` | VALIDATED_AMBIGUITY_HANDLED | Preserved GPU burn, 40 C, +5 percent 5 V/3.3 V DC margins and identified the 720-versus-240-minute conflict. |
| 19 | `(No Main Function)\|3\|Wistron---00356-V002` | VALIDATED_AMBIGUITY_HANDLED | Refused to equate PCIe LTSSM state validation with lane-margin measurement and kept execution blocked. |
| 20 | `(No Main Function)\|7\|Wistron---00842-V003` | VALIDATED_CLEAR | Preserved WebUI BMC downgrade, exact compatible `.ima`, configuration preservation and no fabricated Redfish upload. |

## Misunderstanding and repair outcome

No calibration contract produced an actual scope reduction, wrong device or
execution location, lost duration/iteration, wrong operation, missing required
evidence, unsafe interpretation, false completion, incorrect BLOCKED outcome,
or unjustified PASS claim. Therefore no document repair/revalidation loop was
required for these 20 contracts.

Sequences 3, 7, 18 and 19 returned `AMBIGUOUS` because the contracts faithfully
surface unresolved source conflicts. Their validators named the exact conflict,
limited activity to safe read-only preparation, and stopped state-changing work.
That behavior is the intended acceptance result, not a validation failure.

## Gate decision

The calibration understanding gate passes for continuation to sequence 21.
This establishes semantic interpretability only for the twenty supplied
contracts under isolated same-model-family review. It does not establish
independent-model validation, execution readiness closure, final engineering
acceptance, or DUT hardware validation.

## Post-calibration validation through sequence 50

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- Thirty contract-only inputs (sequences 21-50) were divided across three
  isolated reviewers. The reviewers did not receive source rows, V2 findings,
  root-review conclusions or other validation outputs.
- Full responses are preserved in
  `VALIDATION_OUTPUTS/post_0021_0030_agent_a.json`,
  `VALIDATION_OUTPUTS/post_0031_0040_agent_b.json`, and
  `VALIDATION_OUTPUTS/post_0041_0050_agent_c.json`.
- Twenty-nine contracts were `VALIDATED_CLEAR`. Sequence 45 was
  `VALIDATED_AMBIGUITY_HANDLED`: the validator distinguished reversible virtual
  media mounting from a destructive boot/install workflow and refused to invent
  a result while the owner decision is absent.
- Root comparison found no scope reduction, wrong target or location, lost
  duration/iteration, substituted command, omitted evidence, unsafe execution,
  false completion, incorrect BLOCKED interpretation or unjustified PASS claim.
- No contract repair was required. These results validate semantic understanding
  only; they do not close required inputs, authorize execution, constitute an
  independent-model check, or provide DUT hardware evidence.

| Sequences | Result | Key recovered boundaries |
| --- | --- | --- |
| 21-30 | 10 clear | Physical seating/cabling/LED/CPU/jumper work, TPM OS boundary, one bounded fault, and exact 50-cycle ROM programming were preserved. |
| 31-40 | 10 clear | AST1060 SVN rejection, 12-hour all-SSD fio, CX7 link properties, all-GPU DCGM, BIOS interaction/lifecycle/default ordering and SMBIOS mappings were preserved. |
| 41-44 | 4 clear | SMBIOS cache/memory/PSU references and destructive GPUBB firmware plus AC activation remained distinct and complete. |
| 45 | Ambiguity handled | Mount-only and boot/install interpretations remained blocked pending owner correction. |
| 46-50 | 5 clear | SNMP MIB scope, NVMe thermal, GPU power, three BMC cable states and every callout method were recovered without unsafe expansion. |
