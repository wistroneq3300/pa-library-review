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

## Material-change validation: sequence 67

Status: `PASSED AFTER DOCUMENT REPAIR IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed PA execution contract for
  `Functionality|1352|Wistron-BMC-00642-V004`; it did not receive the source,
  V2 conclusion or root review rationale.
- First-pass understanding correctly prohibited `InsertMedia` POST and limited
  current work to VirtualMedia/ActionInfo GET discovery. It also exposed three
  contract defects: an occupied slot was over-broadly listed as a discovery
  stop condition, discovery completion was underspecified, and post-decision
  wording could be misread as permission to execute.
- The document was repaired so an occupied slot is discovery evidence but a
  future insertion blocker; discovery has explicit completion criteria; and
  owner resolution may only close discovery or lead to a separate execution
  contract, never authorize POST under this contract.
- Revalidation recovered the exact purpose, resource-instance scope, missing
  inputs, safe GETs, mutation approval boundary, evidence, stop conditions and
  completion. The validator returned `PASS` and stated that no POST is part of
  completion.
- Failure attribution: first-pass testcase-document defects, corrected. No
  remaining platform-handoff or model-planning failure was identified. This is
  not independent-model validation and is not DUT hardware validation.

## High-risk validation: sequence 69

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the execution contract for
  `Functionality|1422|Wistron-BMC-00714-V002`.
- It preserved the exact one-CPU/socket, one-event and platform-specific scope;
  identified shutdown-versus-reset, thresholds, sensor map, SOP, calibration,
  hard limits, operator and approval as missing; and limited current safe work
  to preserved read-only baseline evidence.
- It assigned all fixture/heatsink manipulation, thermal stimulus, emergency
  stop, physical inspection and restoration to the qualified operator. The
  agent was limited to authorized telemetry/log correlation.
- It correctly treated unresolved power semantics, missed protection, hard
  limit, probe divergence, lost monitoring and abnormal recovery as stops. It
  did not infer thresholds, continue heating after response, repeat the event,
  or treat successful recovery as proof that protection passed.
- No document, platform-handoff or model-planning failure was identified. This
  is not independent-model validation and is not DUT hardware validation.

## Reclassification validation: sequence 71

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed hybrid execution contract for
  `Functionality|1533|Wistron-HW-00350-V002`.
- It recovered one connector zone and one wet/assert/dry/recover cycle, all
  missing vendor/SOP/policy/timer inputs and the current safe dry-baseline work.
- It reserved stimulus application/removal, physical inspection, isolation,
  objective dry/electrical clearance and recovery approval to the qualified
  operator. The agent was limited to read-only sensor/event/timing correlation.
- It rejected universal use of the source's one-minute example, agent safety
  certification, visual wiping or sensor deassertion as proof of dryness,
  alarm-only completion, log clearing and automatic retry.
- No document, platform-handoff or model-planning failure was identified. The
  hybrid reclassification did not relax execution readiness or safety. This is
  not independent-model validation and is not DUT hardware validation.

## High-risk/source-conflict validation: sequence 75

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|1677|Wistron-BMC-00949-V003`.
- It recovered one approved three-byte tuple, one verified SUT/BMC pair and the
  separate in-band and out-of-band command paths without interpreting the title
  as proof of a BIOS setup or NVRAM operation.
- It identified the OEM request/response definition, byte encoding, affected
  state, first-send result, duplicate-send safety, readback and recovery as
  missing platform handoff inputs. It performed no raw command and allowed only
  identity, tool, interface, reachability, health and documentation checks.
- It correctly required a known first-send result before the second path,
  rejected shell exit status or unrelated LAN output as proof, and reserved
  command semantics, idempotency, readback, restoration and final judgment to
  the OEM/BIOS engineer.
- Failure attribution: the unresolved vendor-specific inputs are a
  `PLATFORM_HANDOFF_DEFECT`, not a testcase-document defect. Ignoring the
  explicit gates would be a model-planning error; no such execution occurred.
  This is not independent-model validation and is not DUT hardware validation.

## BLOCKED/manual-boundary validation: sequence 80

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|1827|Wistron-HW-00449-V002`.
- It recovered that `FIO_BD` plus TBD procedure/criteria does not define a
  physical continuity test, an I2C scan or any other executable operation.
- It allowed only non-invasive identity and documentation intake and explicitly
  rejected I2C enumeration/probing/register reads, continuity measurement,
  connector/cable manipulation, power changes and an assumed execution side.
- It defined current completion as a traceable BLOCKED handoff, not testcase
  PASS/FAIL, and reserved operation type and manual-versus-machine boundary to
  the owner after a complete platform-specific definition is supplied.
- Failure attribution: `DOCUMENT_DEFECT` and `PLATFORM_HANDOFF_DEFECT`; no
  model-planning error occurred. This is not independent-model validation and
  is not DUT hardware validation.

## PCIe automation reclassification validation: sequence 83

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|1972|Wistron-AMD SVM-00138-V004`.
- It recovered a software `amdxio` Receiver Lane Margining workflow over every
  actual lane of approved AMD/OAM links and did not require or substitute an
  external analyzer.
- It treated example BDFs and 128 CSV rows as non-executable illustrations,
  required the physical-to-BDF/lane/receiver map and six metric thresholds, and
  limited pre-gate work to read-only topology, link, ASPM and AER evidence.
- It preserved approval before ASPM changes, one bounded margin run, per-lane
  CSV reconciliation, threshold/no-downtrain checks, no automatic retry and
  restoration of every prior ASPM value before completion.
- Failure attribution: remaining `amdxio`, topology, receiver and threshold
  gaps are `PLATFORM_HANDOFF_DEFECT`. No document defect or model-planning error
  occurred. This is not independent-model validation and is not DUT hardware
  validation.

## Critical eight-GPU thermal-soak validation: sequence 85

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|2064|Wistron-AMD SVM-00018-V002`.
- It recovered eight exact UUID/BDF/ROCR/AGT-mapped GPUs, at least one minute
  of pre-idle, eight separately supervised 2400-second Coralgemm processes,
  synchronized AMD-SMI/AGT/Redfish/system telemetry and post-idle recovery.
- It rejected numeric index equivalence, launch-only completion, guessed limits
  or GFLOP rules, ignored sampling gaps, continued load after monitoring loss,
  overly broad process kills and automatic reset/reboot/rerun.
- It required per-process timing/status, complete thermal/power/cooling/RAS
  evidence, quantitative stop rules and all GPUs/services healthy before
  successful completion; an orderly safety abort remains an incident, not a
  completed soak.
- Failure attribution: missing mappings, rules, infrastructure certification
  and approvals are `PLATFORM_HANDOFF_DEFECT`; inventing or bypassing them would
  be `MODEL_PLANNING_ERROR`. No document defect occurred. This is not
  independent-model validation and is not DUT hardware validation.

## Proprietary BlueField network-suite validation: sequence 86

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|2123|Wistron-GB NV PVP HW-00042-V002`.
- It recovered the exact BlueField, port/function, host-or-embedded execution
  location and peer scope and treated 180 minutes as a planning estimate, not
  as a substitute for manifest-defined durations or iterations.
- It allowed secure read-only identity, mode, package, topology, link, health,
  monitoring and recovery checks, but rejected traffic before the package,
  signed manifest, mappings, isolation and approvals are supplied.
- It rejected help/capability output, a partial suite, an aggregate PASS line
  or elapsed machine time as completion and required complete per-subtest
  evidence, manifest reconciliation and healthy post-test restoration.
- Failure attribution: missing proprietary artifacts, mappings and approvals
  are `PLATFORM_HANDOFF_DEFECT`; inventing a command, port, execution location
  or threshold would be `MODEL_PLANNING_ERROR`. No contract-document defect
  occurred. This is not independent-model validation and is not DUT hardware
  validation.

## Proprietary CPU DVFS validation: sequence 88

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|2198|Wistron-HW-00479-V002`.
- It recovered an exact recipe-defined CPU package/core/frequency-policy scope,
  one bounded run and complete MODS/DVFS/log evidence without assuming Intel,
  AMD or Arm semantics or treating the 10-minute estimates as active duration.
- It preserved or timestamped baseline logs before any separately authorized
  clear, required host-key-verified access and rejected the tool name, exit
  status, one frequency transition or a vendor PASS label as sufficient proof.
- It required supplied criteria, complete domain coverage, telemetry, log
  deltas, restoration and final platform health and prohibited automatic rerun.
- Failure attribution: source `Criteria=TBD` is a
  `TEST_CASE_DOCUMENT_DEFECT`; absent recipe, command, mappings, limits and
  approval are `PLATFORM_HANDOFF_DEFECT`. The validator's statement that active
  execution is currently blocked is readiness gating, not an Automation
  Classification of `BLOCKED`. This is not independent-model validation and is
  not DUT hardware validation.
