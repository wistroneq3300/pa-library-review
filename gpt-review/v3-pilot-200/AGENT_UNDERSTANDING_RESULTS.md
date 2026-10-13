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

## AMD GPU UMC OD-ECC replay-correctable validation: sequence 119

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|192|Wistron-GPU RAS-00837-V004`.
- It preserved one host-side UMC block-0/sub-block-2/type-4 replay-correctable
  injection on one stable-identity-mapped GPU and rejected another GPU, host
  DDR, OOB injection, another subtype or any retry.
- It refused to infer Device 0 or choose among source `0x800`, command
  `0x800000000` and the decoded ACA address until the signed recipe reconciles
  the address domains.
- It required a zero source baseline, fresh target-correlated UMC CE/ACA
  evidence, the approved query/new/total relationship, no UE/poison/reset and
  final HBM/compute/telemetry health; tool success, a generic error line or a
  stale total were rejected as completion.
- Failure attribution: missing mapping, private subtype/address semantics,
  counter/ACA matrix and approvals are provider-closable
  `PLATFORM_HANDOFF_DEFECT` conditions; guessing them or declaring partial
  evidence PASS would be `MODEL_PLANNING_ERROR`. No proposed-contract defect
  was found. This is not independent-model validation and is not DUT hardware
  validation.

## fio QD1 destructive sequential-write validation: sequence 122

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Performance|7|Wistron-Performance Storage-00006-V004`.
- It preserved one bounded sacrificial target, 100% sequential write, 512-byte
  blocks, one job, effective QD1 and a full 43200-second measured window.
- It rejected bare `/dev/sdX` or `/dev/nvmeXnY` identity, omitted or widened
  range, QD64, a 60-minute substitute, unverified `./fio`, package/cache/
  preconditioning changes and automatic rerun.
- It required two-view target exclusion, achieved-depth distribution, exact
  fio/job evidence, full runtime, performance thresholds, health/endurance
  telemetry and restore/reprovision completion; fio exit success alone was not
  completion.
- Failure attribution: missing target/range/profile/spec/approval are
  provider-closable `PLATFORM_HANDOFF_DEFECT` gates; choosing a device,
  shortening duration or widening scope would be `MODEL_PLANNING_ERROR`. No
  proposed-contract defect was found. This is not independent-model validation
  and is not DUT hardware validation.

## fio QD1 destructive M.2 random-write validation: sequence 124

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Performance|12|Wistron-Performance Storage-00015-V004`.
- It preserved one bounded destructive randwrite run with 512-byte blocks, one
  job, effective QD1 and the full 43200-second measured interval.
- It correctly treated M.2 as a form factor and required proof of NVMe/PCIe
  versus SATA/AHCI transport, plus logical-block and 512-byte `O_DIRECT`
  alignment.
- It required random/preconditioning/steady-state evidence, host and NAND write
  accounting, write amplification/endurance budget and final health; a
  60-minute sample, setup-only run, transient target or vendor headline was not
  completion.
- Failure attribution: missing target/profile/spec/approval are
  `PLATFORM_HANDOFF_DEFECT`; guessing transport/range, shortening, ignoring
  alignment/endurance or retrying is `MODEL_PLANNING_ERROR`. Unsupported 512B
  alignment or an unprovable safe target can legitimately block execution. No
  proposed-contract defect was found. This is not independent-model validation
  and is not DUT hardware validation.

## fio QD1 random-read validation: sequence 123

Status: `PASSED AFTER ONE DOCUMENT REVISION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Performance|9|Wistron-Performance Storage-00008-V004`.
- The first validation preserved QD1, 512-byte randread, one job, bounded target
  and 43200 seconds, but found a real document defect: a filesystem read may
  update atime/journal metadata, and 512-byte `O_DIRECT` support/alignment was
  not explicitly gated.
- V3 was revised to distinguish zero fio-issued writes/trims from filesystem
  metadata, require a signed mount/atime/journal policy and observed metadata
  delta, and require logical-block/direct-I/O alignment proof for the exact raw
  device or file profile.
- Revalidation was CLEAR. The contract still rejects a 60-minute substitute,
  transient/default target, file creation, write/trim/preconditioning,
  unverified `./fio`, wrong effective depth and automatic retry.
- Failure attribution after correction: missing alignment or metadata policy is
  `PLATFORM_HANDOFF_DEFECT`; ignoring it is `MODEL_PLANNING_ERROR`. No remaining
  proposed-contract defect was found. This is not independent-model validation
  and is not DUT hardware validation.

## AMD GPU GFX poison-consumption validation: sequence 120

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|203|Wistron-GPU RAS-00013-V003`.
- It preserved exactly one ordered producer-to-GFX-consumer transaction on one
  UUID/BDF/DRM/tool-selector-mapped GPU and rejected independent execution,
  reordering, splitting, OOB injection and retry.
- It required distinct fresh producer evidence before the consumer, bounded
  poison lifetime, the same target GPU, GFX CRC-write consumer/PASID
  correlation and the prescribed ACA/CPER/counter/client/reset evidence.
- It treated the Device-0 UMC query only as a separate control, stopped before
  the consumer after a failed or uncorrelated producer, and rejected injection
  success or generic dmesg output as completion.
- Failure attribution: missing signed block/mode semantics, poison identity,
  lifetime, consumer, event matrix and recovery are provider-closable
  `PLATFORM_HANDOFF_DEFECT` conditions; guessing them or running a partial pair
  would be `MODEL_PLANNING_ERROR`. If the owner determines independent variants,
  the testcase must be revised/split before execution. No proposed-contract
  defect was found. This is not independent-model validation and is not DUT
  hardware validation.

## SPEC CPU2017 performance-contract validation: sequence 121

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Performance|2|Wistron-Performance CPU-00001-V003`.
- It preserved licensed SPEC CPU2017, the selected canonical
  intrate/fprate/intspeed/fpspeed scope, base tuning, exactly three measured
  iterations and the 120/2880-minute planning estimates.
- It rejected test-size, individual-benchmark, peak-only, one-iteration,
  legacy `buildspec`/`runspectest` and unlike-metric substitutions.
- It required `runcpu` build/integrity evidence, raw `.rsf` and reports, the
  complete SUT/copies/threads/affinity state and long-run health telemetry; it
  allowed Actual collection but withheld PASS without same-metric reference
  IDs and tolerance.
- Failure attribution: missing licensed media, canonical profile, config,
  thresholds, references and approvals are `PLATFORM_HANDOFF_DEFECT`
  conditions; shortening the run, changing the metric/profile or claiming
  unmatched PASS would be `MODEL_PLANNING_ERROR`. No proposed-contract defect
  was found. This is not independent-model validation and is not DUT hardware
  validation.

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

## Physical CPU swap traceability validation: sequence 115

Status: `PASSED AFTER REVISION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|156|Wistron-System RAS-00113-V002`.
- The first validation preserved the manual physical boundary, firmware gate,
  single swap, BIOS/OS evidence and full socket/core/thread/NUMA comparison, but
  found a document contradiction: unique CPU traceability was required while
  physical identifiers were requested only “where available.”
- V3 was revised before acceptance. Exchange now requires proof that both CPUs
  moved to the specified opposite sockets; replacement distinguishes removed
  and installed parts; reseat proves the same part returned to the same socket.
  When unique serials are unavailable, socket-labelled package photos plus a
  witnessed or owner-controlled chain-of-custody are mandatory.
- Revalidation found Required Inputs, Expected Evidence, Acceptance Reference
  and Stop Conditions consistent, and rejected model-name output or operator
  recollection as proof of the physical operation.
- Missing concrete matrix, identifiers/photos, witnesses/labels, compatibility,
  firmware, topology and recovery remain `PLATFORM_HANDOFF_MISSING`; guessing
  identity or declaring partial-evidence PASS would be `MODEL_PLANNING_ERROR`.
  No document defect remains. This is not independent-model validation and is
  not DUT hardware validation.

## Intel GNR SPDI3C/I3C HALT recovery validation: sequence 116

Status: `PASSED AFTER REVISION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|159|Wistron-System RAS-00116-V002`.
- It correctly kept `halt()` and `go()` inside the CScripts target-control
  context, preserved exactly one err_type 0x13 injection and rejected generic
  SMBus recovery, other controllers, automatic retry or partial-evidence PASS.
- The first validation found a document ambiguity: `transfer_err_stat bit 9`
  and `intr_status bit 9` could appear to name different registers.
- V3 was revised to use the single fully qualified field
  `sb_i3c_0.intr_status.transfer_err_stat[9]` for the pre-injection,
  post-injection and owner-defined post-recovery reads. Revalidation confirmed
  that `intr_status` is the register and `transfer_err_stat[9]` its field.
- Missing SMBus/I3C scope resolution, target map, recipe, settings, signatures,
  states and recovery remain `PLATFORM_HANDOFF_MISSING`; selecting a different
  field, using OS halt/go or generic logs would be `MODEL_PLANNING_ERROR`. No
  document defect remains. This is not independent-model validation and is not
  DUT hardware validation.

## Intel GNR single-device multi-bit CE validation: sequence 117

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|170|Wistron-System RAS-00127-V002`.
- It preserved exactly one CScripts `halt()`/injection/`go()` sequence at the
  source coordinates, confirmed that zero-masked `dev1` is not a second
  injected device and required signed physical/API device-DQ mapping.
- It required 128b ECC, clean baseline, `uc=0`, `mscod=0x80`, the signed runtime
  demand-log set, address/parity correlation and exact logical-rank counter +1;
  it rejected generic CE, injector return or counter-only completion.
- It stopped rather than switching retry-log sets when `en_patspr` differs and
  required no UE/fatal/unrelated event, successful resume, final health and
  complete injector/BIOS/GRUB restoration.
- Missing recipe, topology/device semantics, register decodes, retry set,
  counter index, settings and recovery are `PLATFORM_HANDOFF_MISSING`; guessing
  them or changing mask/set/coordinates would be `MODEL_PLANNING_ERROR`. No
  document defect was found. This is not independent-model validation and is
  not DUT hardware validation.

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

## Physical-topology BMC KVM validation: sequence 89

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|2206|Wistron-BMC-00486-V002`.
- It recovered one session on the exact SUT/BMC, the owner-defined USB
  hub/peripheral chain, separate physical VGA reference, remote live video and
  harmless input, without treating five minutes as an acceptance duration.
- It required a trusted operator for the physical and visual boundary,
  preserved logs, demanded complete capture/restoration evidence and rejected
  reachability, enumeration or one visible frame as completion.
- It kept power, reset, virtual media, firmware actions and unapproved input out
  of scope and required stops on wrong target/topology, video/input/USB faults,
  evidence loss or failed restoration.
- Failure attribution: missing identities, topology, fixtures, checklist and
  dwell rule are `PLATFORM_HANDOFF_DEFECT`; guessing them or reducing the test
  to remote reachability would be `MODEL_PLANNING_ERROR`. No contract-document
  defect occurred. This is not independent-model validation and is not DUT
  hardware validation.

## PDB multi-interface sensor validation: sequence 90

Status: `PASSED AFTER ONE DOCUMENT CORRECTION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|2274|Wistron-HW-00483-V002`.
- The first pass found a genuine contract defect: treating every cross-path
  disagreement as a collection stop could prevent acquisition of the remaining
  safe IB, OOB or Web evidence.
- The contract was corrected to stop collection immediately only for wrong
  target, credential, health, availability or mutation hazards. Missing,
  ambiguous, stale or disagreeing data now stops PASS interpretation while the
  other bounded read-only views continue when target/security/health are sound.
- Revalidation recovered complete IB/OOB SDR and Sensor List plus BMC Web,
  every mapped PDB sensor, one collection per interface, raw-evidence retention,
  SPEC-dependent acceptance, secret safety and no-write/no-reset boundaries.
- Failure attribution after correction: absent target data, PDB SPEC/map,
  equivalence rules, endpoints or Web path are `PLATFORM_HANDOFF_DEFECT`;
  filtering away evidence, guessing aliases, premature collection stop or
  partial PASS would be `MODEL_PLANNING_ERROR`. No material document defect
  remains. This is not independent-model validation and is not DUT hardware
  validation.

## High-risk board-jumper validation: sequence 91

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Functionality|2286|Wistron-HW-00164-V003`.
- It limited scope to the exact recipe-enumerated jumper(s) and recovered one
  alternate-position power-on/function observation plus one photographed
  restored-default power-on/log verification for each named target.
- It rejected another board revision's diagram, nearby unlisted headers,
  energized movement, alternate-only completion, unexported log clearing and
  the 5/5-minute estimates as discharge, dwell or boot timing.
- It required physical position evidence, exact function/page, configuration
  and security/boot/storage comparison, safe power/ESD handling, final healthy
  deployed state and no improvised retry/recovery.
- Failure attribution: absent board recipe, pin/function/state/timing data,
  operator and approvals are `PLATFORM_HANDOFF_DEFECT`; inventing or expanding
  them would be `MODEL_PLANNING_ERROR`. Current execution gating does not alter
  the `MANUAL ONLY` capability class. This is not independent-model validation
  and is not DUT hardware validation.

## Genuine semantic blocker validation: sequence 92

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed blocked contract for
  `Functionality|2292|Wistron-HW-00451-V002`.
- It recovered definition closure as the sole current activity and did not
  select a cable, board, bus, address, pins, controller, power state, physical
  continuity test or software probe.
- It prohibited manipulation, measurement, enumeration, register access,
  voltage injection, analyzer use and power transition while preserving the
  2/2-minute values only as non-executable planning estimates.
- It correctly treated signed owner clarification as completion of definition
  work only; a new execution contract and capability review remain mandatory,
  and no testcase PASS/FAIL is possible.
- Failure attribution: the underlying TBD target/procedure/criteria are a
  `TEST_CASE_DOCUMENT_DEFECT`; absent platform/cable mapping is a
  `PLATFORM_HANDOFF_DEFECT`; inventing either would be a
  `MODEL_PLANNING_ERROR`. This is not independent-model validation and is not
  DUT hardware validation.

## ECC leaky-bucket hybrid RAS validation: sequence 93

Status: `PASSED AFTER ONE DOCUMENT CORRECTION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|3|Wistron-System RAS-00377-V003`.
- The first pass found a genuine contract defect: a one-reset scope conflicted
  with an optional threshold restoration that may require another BIOS
  save/reset.
- The contract was corrected to allow one test-setting save/reset and, only
  after stimulus evidence is preserved, one separately approved restoration
  save/reset when required by the signed final-state policy.
- Revalidation recovered the exact threshold/register, physical/logical
  DIMM_B, bounded event count/spacing/decay/timeout, system plus BMC SEL
  evidence, manual BIOS boundary, automated correlation and final health.
- Failure attribution after correction: absent recipe, map, register semantics,
  injection capability, timing and approvals are `PLATFORM_HANDOFF_DEFECT`;
  guessing values, wrong-DIMM injection, premature restoration, extra reset or
  partial PASS would be `MODEL_PLANNING_ERROR`. No material document defect
  remains. This is not independent-model validation and is not DUT hardware
  validation.

## Critical multi-socket UPI CRC validation: sequence 94

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|5|Wistron-System RAS-00725-V003`.
- It preserved the unresolved Windows-WHEA versus Linux-dmesg source conflict
  and required one owner-selected native OS evidence path before execution.
- It recovered one `num_crcs=1` invocation for every signed
  socket/port/link/peer tuple, controlled-client ITP execution, unique full logs
  and halt/inject/resume plus health go/no-go before the next tuple.
- It excluded adjacent same-title infinite CRC, failover, link-layer,
  Three-Strike, MCERR, IERR and I3C patterns and rejected partial matrix, BMC-only
  evidence or normal boot alone as completion.
- Failure attribution: mixed OS requirements are an underlying
  `TEST_CASE_DOCUMENT_DEFECT`; absent topology, tool semantics, BIOS values and
  approvals are `PLATFORM_HANDOFF_DEFECT`; selecting or inventing them would be
  `MODEL_PLANNING_ERROR`. Current execution gating does not alter the
  `REQUIRES PACKAGE / USER CONFIRMATION` class. This is not independent-model
  validation and is not DUT hardware validation.

## Correctable x4 SDDC controller-matrix validation: sequence 95

Status: `PASSED AFTER ONE DOCUMENT CORRECTION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|16|Wistron-System RAS-00736-V003`.
- It recovered one rank-0 `x4sddc` injection for every signed controller tuple,
  Windows-native rather than Linux evidence, exact logical-to-physical x4 DIMM
  mapping, per-target go/no-go, both LED-off criteria and full restoration.
- The first pass found a genuine contract defect: Acceptance Reference made
  uEFI SEL conditional on platform support, but Stop Conditions made any
  absent uEFI record an unconditional stop.
- V3 corrected the rule so missing or mismatched uEFI SEL stops only when the
  signed platform matrix declares that evidence supported and required. Fresh
  isolated revalidation recovered this distinction and rejected treating mere
  record absence as proof that the capability is unsupported.
- Failure attribution after correction: absent topology/population, BIOS,
  proprietary command, event and approval data are `PLATFORM_HANDOFF_DEFECT`;
  guessing them, auto-looping, importing an adjacent fault pattern or claiming
  partial-matrix PASS would be `MODEL_PLANNING_ERROR`. No material document
  defect remains in the proposed contract. This is not independent-model
  validation and is not DUT hardware validation.

## ADDDC rank-with-plus1 hybrid validation: sequence 96

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|26|Wistron-System RAS-00746-V003`.
- It recovered the exact rank-with-plus1 variant, the signed 64 GB x4
  population and argument map, and one authorized harasser invocation for each
  explicit recipe target rather than inventing rank, controller or plus1 values.
- It preserved the manual DIMM/BIOS/LED boundaries while recognizing that the
  exact bounded Cscript invocation and evidence correlation can be automated
  after package, recipe and approval handoff.
- It required Windows-native evidence, a complete unfiltered harness log,
  independent slot/LED/health criteria, conditional uEFI evidence and final
  restoration; `sparing_harasser PASSED` alone was insufficient.
- Failure attribution: missing platform, package, target, argument, event and
  timing values are `PLATFORM_HANDOFF_DEFECT`; guessing them, reducing a target
  matrix, retrying automatically or declaring partial PASS would be
  `MODEL_PLANNING_ERROR`. No intrinsic proposed-contract defect was found.
  This is not independent-model validation and is not DUT hardware validation.

## Intel OCP non-fatal UCE matrix validation: sequence 97

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|33|Wistron-System RAS-00753-V003`.
- It recovered every signed OCP 1~N matrix row and required physical slot,
  device/serial/BDF, root-port and ITP socket/port correlation rather than one
  representative slot or numerical inference.
- It did not infer non-fatal severity from `errType='uce'`; it required the
  signed subtype/severity recipe and Windows WHEA/CPER evidence decoded as
  recoverable/non-fatal for the exact target.
- It preserved per-platform BMC/uEFI/LED expectations: conditional evidence
  cannot be made universal or silently omitted, and API success alone cannot
  prove target, severity, recovery or completion.
- Failure attribution: absent matrices, recipe, BIOS values, expected records,
  timing and recovery are `PLATFORM_HANDOFF_DEFECT`; guessed topology or
  severity, automatic iteration/retry and partial PASS are
  `MODEL_PLANNING_ERROR`. No material proposed-contract defect was found. This
  is not independent-model validation and is not DUT hardware validation.

## AMD fatal DRAM slot/address validation: sequence 98

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|44|Wistron-System RAS-00764-V002`.
- It recovered the unresolved DRAM-versus-MCA profile contradiction and would
  not combine the conflicting settings; both profiles require separate signed
  phases if the owner determines both are in scope.
- It selected exactly one native OS evidence branch and required every memory
  slot to have an independently proven UMC/channel/DIMM/rank/address/mask row;
  fixed `0x1000`, cross-OS evidence and representative coverage were rejected.
- It preserved tool PASS, timely native-OS fatal evidence and the specified
  shutdown/restart as three independent per-slot gates, followed by restoration
  and a health gate before the next separately approved target.
- Failure attribution: absent profile resolution, OS branch, address matrix,
  tool semantics, timeout and recovery remain `PLATFORM_HANDOFF_DEFECT`;
  combining settings, guessing/reusing an address, auto-looping or accepting a
  reboot as proof of a wrong target would be `MODEL_PLANNING_ERROR`. No proposed
  contract defect was found. This is not independent-model validation and is
  not DUT hardware validation.

## AMD PCIe correctable LCRC slot/locus validation: sequence 99

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|55|Wistron-System RAS-00775-V003`.
- It recovered every owner-required slot/locus entry and kept endpoint and
  upstream-root-port BDFs distinct; a row requiring both could not be satisfied
  by one locus or one representative slot.
- It required fresh enumeration, verified `errortype 0` correctable-LCRC
  semantics, target-correlated Linux AER/counter evidence and preserved
  link/device/platform health with no unexpected SyncFlood or reset.
- It rejected copied/stale BDFs, arithmetic topology inference, tool-only PASS,
  automatic looping/retry and the 30/60-minute estimates as timeout values.
- Failure attribution: absent matrix, OS/kernel, package, BIOS/HDT, evidence,
  timeout and recovery data are `PLATFORM_HANDOFF_DEFECT`; guessing loci/BDFs,
  reducing coverage or accepting reset/degradation would be
  `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This is not
  independent-model validation and is not DUT hardware validation.

## Immediate GPIO power-off and recovery validation: sequence 113

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|146|Wistron-HW Robust-00024-V002`.
- It placed `/usr/bin/powerctrl.sh power_off` in the signed BMC/platform
  management shell and explicitly rejected the prior host-SSH assumption.
- It preserved exactly one immediate power-off and one separately authorized
  power-on; 15/15 minutes remained estimates and any minimum Off dwell was
  correctly treated as a platform handoff value.
- It rejected command submission, session loss, UART text, Off state alone or
  successful boot alone as completion, requiring independent Off proof plus
  restored storage, devices, network/GPU, services and expected logs.
- Failure attribution: missing script semantics, GPIO target, shell, timeouts,
  power-on method, dwell and health matrix are `PLATFORM_HANDOFF_MISSING`;
  guessing host SSH, substituting actions, retrying or early PASS would be
  `MODEL_PLANNING_ERROR`. No intrinsic document defect was found. This is not
  independent-model validation and is not DUT hardware validation.

## AMD OCP ACS-fatal reset/BERT validation: sequence 100

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|66|Wistron-System RAS-00786-V002`.
- It recovered every signed OCP matrix row, required powered-off manual phases
  for NIC relocation and required revalidation of BDF and AMD target tuple
  after each move rather than copying the source example.
- It preserved the immediate warm reset, but required a fresh current-slot
  BERT/CPER fatal record and healthy NIC/link/network/system recovery; reset or
  a stale record alone could not complete a slot.
- It required ACS capability at the recipe-defined locus, verified tool-build
  `errortype 4` semantics, per-slot approvals and no production, boot-critical
  or management-critical networking.
- Failure attribution: missing matrices, ACS expectations, tool semantics,
  BIOS/HDT values, timeout and recovery are `PLATFORM_HANDOFF_DEFECT`; inferred
  tuples/ACS, stale BERT, reset-only PASS or automatic iteration/retry are
  `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This is not
  independent-model validation and is not DUT hardware validation.

## AMD WAFL correctable dual-location validation: sequence 101

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|77|Wistron-System RAS-00797-V002`.
- It recovered Socket 1/`errorlocation 0` and Socket 0/`errorlocation 1` as
  separate asymmetric source cases and required signed proof rather than
  normalizing the location numbers to their socket numbers.
- It did not expand scope to every enumerated WAFL link or assume the same link
  number applied to both locations; signed coverage and per-location mapping
  remain mandatory.
- It selected one native OS evidence branch and required separate tool PASS,
  corrected event, counter and link-health evidence; any first-location anomaly
  prevented the second injection.
- Failure attribution: absent mapping, tool semantics, OS branch, BIOS values,
  timeout and recovery are `PLATFORM_HANDOFF_DEFECT`; inferred/reversed mapping,
  mixed OS evidence, link expansion or automatic continuation/retry would be
  `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This is not
  independent-model validation and is not DUT hardware validation.

## AMD DDR5 PMIC SWB fatal matrix validation: sequence 102

Status: `PASSED AFTER DOCUMENT CORRECTION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|89|Wistron-System RAS-00809-V002`.
- It recovered the complete `2 × approved-DIMM-count` matrix, rejected reuse of
  the source example tuple and required signed SWB, rail-type and voltage-type
  semantics before any injection.
- It preserved one approved native OS branch, independent approval and evidence
  for every fatal-reset row, post-reset recipe-state revalidation and final
  PMIC, memory and system health restoration.
- The first pass found a document defect: the contract mentioned a BMC record
  without defining whether it was mandatory, conditional or supporting-only.
  Required Inputs, Expected Evidence, Acceptance and Stop Conditions were
  corrected so the signed platform recipe controls that applicability and its
  fields/timeout. Revalidation found no remaining document defect.
- Failure attribution: missing matrix, semantics, BMC applicability, OS query,
  timeout, health limits, approvals or recovery are `PLATFORM_HANDOFF_DEFECT`;
  guessed targets, reduced coverage, automatic looping/retry, mixed OS evidence
  or partial-evidence PASS would be `MODEL_PLANNING_ERROR`. This is not
  independent-model validation and is not DUT hardware validation.

## NVIDIA CPU processor-correctable definition gate: sequence 103

Status: `PASSED BLOCKER RECOGNITION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|100|Wistron-System RAS-00820-V002`.
- It did not infer Grace, BlueField, generic EINJ, a target identifier, command,
  target count or iteration count from the test title. It correctly identified
  all of those as owner-authored inputs that must replace the source TBD fields.
- It separated non-mutating platform/capability inventory from execution and
  rejected inventory, a generic corrected event or tool discovery as completion.
- It confirmed that BLOCKED is appropriate because the source document lacks
  executable and acceptance semantics; after a signed replacement, the case
  requires a fresh review rather than automatic unblocking.
- Failure attribution: literal TBD Procedure/Criteria are `DOCUMENT_DEFECT`;
  missing platform, injector, target coverage, event and recovery are
  `PLATFORM_HANDOFF_DEFECT`; selecting a mechanism, target or command by analogy
  would be `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This
  is not independent-model validation and is not DUT hardware validation.

## AMD GPU SDMA Type-4 UE recovery validation: sequence 118

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|181|Wistron-GPU RAS-00010-V002`.
- It preserved exactly one SDMA block-1/sub-block-0/type-4 uncorrectable
  injection on one UUID/BDF/serial/OAM/DRM/tool-index-mapped GPU and rejected
  Device-0 guessing, a UMC block-0 query or address/command parity as a
  substitute.
- It required the actual loaded `ras_enable`, `ras_mask` and SDMA feature state,
  kept the UMC query only as a separate control baseline, and required a target
  SDMA UE baseline plus a fresh SDMA ACA record and counter delta.
- It preserved the complete reset/MODE1/resume/VRAM-handling sequence and final
  enumeration, memory, compute and telemetry health gate; tool success, reset
  text, a UMC counter or re-enumeration alone were rejected as completion.
- Failure attribution: missing signed semantics, target/default mapping,
  version-specific ACA/reset expectations, recovery and approvals are
  `PLATFORM_HANDOFF_DEFECT`; guessing a target, substituting another fault,
  changing the loaded driver unsafely, retrying or declaring partial-evidence
  PASS would be `MODEL_PLANNING_ERROR`. No proposed-contract defect was found.
  This is not independent-model validation and is not DUT hardware validation.

## BMC I2C-7 fan, leak and PDB endpoint validation: sequence 112

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|138|Wistron-HW Robust-00016-V002`.
- It preserved independent evidence for every PID-listed fan-controller,
  leak-sensor and PDB endpoint on both boards; it rejected one 0x2c byte, ACK or
  generic bus presence as completion of that matrix.
- It treated `i2ctransfer -f` as exactly one conditionally authorized operation
  after endpoint ownership, selector safety, necessity and quiesce are proven,
  and preferred the bound driver's supported telemetry when sufficient.
- It rejected adapter-number assumptions, broad scans, control writes,
  automatic retries and physical probing, and required restored ownership plus
  final cooling, leak, power and BMC health.
- Failure attribution: missing topology, endpoint matrix, protocol, expected
  values, ownership, thresholds, approvals and recovery are
  `PLATFORM_HANDOFF_MISSING`; shortcut coverage or unsafe forced access would be
  `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This is not
  independent-model validation and is not DUT hardware validation.

## NVIDIA CPU memory UCE non-fatal definition gate: sequence 104

Status: `PASSED BLOCKER RECOGNITION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|103|Wistron-System RAS-00823-V003`.
- It preserved host-memory UCE non-fatal intent while refusing to assume a
  removable DIMM/channel topology, Grace, BlueField, generic EINJ or any target
  address before an exact product and memory architecture are signed.
- It identified protected address ownership, the trigger/consumer, required
  targets/iterations and the prescribed page/process/service containment as
  necessary inputs, and did not treat inventory or a generic event as execution.
- It confirmed BLOCKED is correct while Procedure and Criteria remain TBD and
  that a completed replacement contract still requires fresh review rather than
  completing or passing the testcase.
- Failure attribution: literal TBD fields are `DOCUMENT_DEFECT`; missing
  topology, tool, address ownership, consumer, coverage, event and recovery are
  `PLATFORM_HANDOFF_DEFECT`; inferred DIMMs/addresses, copied recipes, generic
  injection or partial-evidence PASS would be `MODEL_PLANNING_ERROR`. No
  proposed-contract defect was found. This is not independent-model validation
  and is not DUT hardware validation.

## NVIDIA CPU PCIe Bad TLP definition gate: sequence 105

Status: `PASSED BLOCKER RECOGNITION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|106|Wistron-System RAS-00826-V003`.
- It independently kept the traffic endpoint/origin, receiving component and
  AER reporting Root Port/RCEC distinct and required all corresponding BDFs in
  a signed per-hierarchy matrix.
- It rejected substituting Bad LCRC, selecting `aer-inject`/EINJ/vendor tools,
  assuming representative or all-slot coverage, or treating existing AER
  capability/counter data as completion.
- It preserved correctable severity and the no-unexpected-reset/retrain plus
  link/device/service health gate, while limiting current work to non-mutating
  topology, ownership, counter and health discovery.
- Failure attribution: label-only Procedure and TBD Criteria are
  `DOCUMENT_DEFECT`; missing topology, generator, locus map, timing, recovery
  and approvals are `PLATFORM_HANDOFF_DEFECT`; inferred tools/BDFs, wrong-locus
  injection or unjustified PASS would be `MODEL_PLANNING_ERROR`. No proposed-
  contract defect was found. This is not independent-model validation and is
  not DUT hardware validation.

## NVIDIA CPU PCIe Replay Number Rollover definition gate: sequence 106

Status: `PASSED BLOCKER RECOGNITION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|108|Wistron-System RAS-00828-V003`.
- It kept Replay Number Rollover distinct from Bad TLP and required traffic
  origin, transmitter, receiver, AER reporter and every BDF to be mapped for
  each approved hierarchy locus.
- It refused to transfer NVIDIA GPU telemetry semantics to an unidentified CPU
  PCIe component or decide that link retraining was universally required or
  forbidden; the signed component recipe must define the transition.
- It rejected a counter increment, AER bit, retrain or restored link alone as
  completion and required full target correlation, prescribed transition and
  restored link/device/traffic/service/system health for every signed locus.
- Failure attribution: label-only Procedure and TBD Criteria are
  `DOCUMENT_DEFECT`; missing components, traffic, generator, counter semantics,
  retrain rule and recovery are `PLATFORM_HANDOFF_DEFECT`; reused Bad TLP logic,
  inferred BDFs/GPU semantics or partial-evidence PASS would be
  `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This is not
  independent-model validation and is not DUT hardware validation.

## NVIDIA CPU PCIe Surprise Down fatal definition gate: sequence 107

Status: `PASSED BLOCKER RECOGNITION IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|111|Wistron-System RAS-00831-V002`.
- It required proof that a future stimulus exercises the requested Surprise
  Down path and did not equate a synthetic fatal AER bit with actual/equivalent
  link disappearance and containment.
- It independently separated endpoint, affected link, upstream/downstream
  ports, DPC containment port and AER Root Port/RCEC, with all BDFs and critical
  data/traffic dependencies mapped per hierarchy.
- It rejected DPC disablement, an AER message, reset, reboot or crash alone as
  success and required target correlation, prescribed containment, integrity,
  approved recovery and restored topology/device/service/system health.
- Failure attribution: label-only Procedure and TBD Criteria are
  `DOCUMENT_DEFECT`; missing topology, stimulus fidelity, fatal response,
  containment and recovery are `PLATFORM_HANDOFF_DEFECT`; inferred link actions,
  critical-path targeting or reset-only PASS would be `MODEL_PLANNING_ERROR`.
  No proposed-contract defect was found. This is not independent-model
  validation and is not DUT hardware validation.

## AMD GPU error-injection capability enablement validation: sequence 108

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|114|Wistron-GPU RAS-00835-V004`.
- It understood this as capability enablement for exactly one mapped OAM/GPU,
  one approved state-application transition, OOB state persistence, host RAS
  feature verification and explicit final-state custody or restoration.
- It repeatedly excluded every fault stimulus and rejected literal BMC/OAM
  examples, invented OEM actions, silent TLS bypass, both reset alternatives or
  assuming `modprobe` changes an already loaded driver.
- It required POST success, fresh persistent `EINJState=Enabled`, verified host
  parameters/features, no unintended injection, health and final-state
  disposition together; any subset was correctly identified as false completion.
- Failure attribution: missing live schema/mapping, driver/reset plan, feature
  expectations and final-state custody are `PLATFORM_HANDOFF_DEFECT`; injecting,
  bypassing TLS, using wrong targets or declaring state-only PASS would be
  `MODEL_PLANNING_ERROR`. No proposed-contract defect was found, and the gated
  reclassification from BLOCKED was judged clear. This is not independent-model
  validation and is not DUT hardware validation.

## AMD GPU UMC Replay AC Parity validation: sequence 109

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|115|Wistron-GPU RAS-00839-V004`.
- It preserved exactly one Replay AC Parity correctable injection on the signed
  GPU/UMC and explicitly rejected ODECC, an unsigned `0x800` address, an OOB-only
  variant or another ASIC generation's flags as substitutes.
- It required UUID/BDF/serial-to-tool-index and UMC mapping, stopped on a nonzero
  baseline unless a signed freshness/delta rule exists, and required a fresh
  subtype-specific event plus prescribed counter delta.
- It rejected tool success, a generic log or a stale nonzero counter as
  completion and preserved the no-reset/no-GPU-HBM-link-degradation health gate.
- Failure attribution: missing signed ASIC/tool/target/address/path/counter data
  are provider-closable `PLATFORM_HANDOFF_DEFECT` conditions; ODECC substitution,
  inferred address/index, mixed paths or partial-evidence PASS would be
  `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This is not
  independent-model validation and is not DUT hardware validation.

## BMC I2C-6 to Mezzanine Network Board 1 validation: sequence 110

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|127|Wistron-HW Robust-00005-V002`.
- It understood a BMC-side functional routed-bus check through MUX 0x72 port 1
  and explicitly excluded physical continuity, signal integrity, probing,
  soldering and host-OS execution.
- It required the exact I2C-6 adapter mapping, driver ownership, PID endpoint
  matrix, both IO-expander and FRU responses, one bounded MUX transition and
  exact restoration of the recorded original state.
- It rejected broad or quick-write scanning, forced access, an inferred 0x02
  meaning, one-endpoint or MUX-only completion and address presence as proof of
  electrical continuity; scan/MUX safety was judged clear after handoff.
- Failure attribution: missing adapter/MUX/endpoint/safe-operation/recovery data
  are `PLATFORM_HANDOFF_DEFECT`; guessed buses, broad scans, forced access,
  continuity claims or PASS before restoration would be `MODEL_PLANNING_ERROR`.
  No proposed-contract defect was found, and the gated reclassification from
  MANUAL ONLY was clear. This is not independent-model validation and is not
  DUT hardware validation.

## BMC-to-HMC/FPGA-2 I2C path validation: sequence 111

Status: `PASSED IN ISOLATED SAME-MODEL-FAMILY CONTEXT`

- The validator received only the proposed execution contract for
  `Reliability|132|Wistron-HW Robust-00010-V002`.
- It understood exactly one BMC-side combined write-then-read transaction to
  the signed adapter-1 endpoint at 0x11 and preserved the three-byte response,
  one-transaction limit and 15/5-minute estimates.
- It limited the result to the hops that PID 1114953 explicitly attributes to
  that endpoint and rejected ACK, exit status or arbitrary bytes as proof of
  the complete HMC/EROT/FPGA-2 chain or of physical continuity.
- It correctly prohibited broad quick-write scanning, forced access, automatic
  retry, inferred state neutrality and unapproved recovery, while allowing
  adapter listing, sysfs topology, binding and baseline-health collection.
- Failure attribution: missing PID, target mapping, reply semantics, ownership,
  state/restoration, timeout and recovery are `PLATFORM_HANDOFF_MISSING`;
  guessing them, widening the path claim or declaring partial-evidence PASS
  would be `MODEL_PLANNING_ERROR`. No proposed-contract defect was found. This
  is not independent-model validation and is not DUT hardware validation.
