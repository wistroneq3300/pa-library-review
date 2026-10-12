# Review Workflow Logic V3

Status: pilot working contract, 2026-10-13

This document is the entry point for V3 testcase review. It does not replace
`REVIEW_WORKFLOW_LOGIC_GPT_SECOND_REVIEW.md`; V2 remains historical and usable
for V2 tasks. V3 review records are separate overlays and never rewrite the
source workbook, DeepSeek data, V2 overlay, or merged production preview.

## 1. Rule precedence

Apply rules in this order. A lower source cannot silently override a higher
source.

1. Original row facts from `data/REVISED_commands_merged_with_raw.xlsx`:
   `Code`, `Items`, `Procedure`, `Criteria`, timing, and other row fields.
2. Explicit user-confirmed technical and classification-boundary decisions,
   including the five feedback cases in
   `BLOCKED_FEEDBACK_REREVIEW_001.json`.
3. V3 requirements in this document and the current task specification.
4. Still-valid V2 safety, source-preservation, and one-row-at-a-time rules.
5. Applicable official technical documentation. It may establish tool or
   platform semantics, but not an undocumented testcase-specific target or
   acceptance value.
6. GPT V2 and follow-up review records as historical comparison evidence.
7. DeepSeek review and old YES/PARTIAL/NO material as historical reference.

When `Items`, `Procedure`, and `Criteria` disagree about the requested test,
record `SOURCE_CONFLICT`. Do not synthesize a replacement test from the title,
neighboring rows, a generic domain pattern, or an external document.

## 2. Source preservation and atomic unit

- The atomic unit is one unique `(sheet, physical XLSX source_row, code,
  case_variant_id)` record.
- Reopen and read that exact XLSX row with an XLSX/XML reader before every
  review. Read `Items`, `Procedure`, `Criteria`, timing, script, and the six
  DeepSeek columns from the same row.
- Read the matching V2 overlay and applicable history/user decisions.
- Write and quality-check exactly one permanent V3 record before opening the
  next selected case.
- Mechanical tools may locate rows, hash sources, validate schemas, count,
  compare, and detect duplicate text. They must not decide intent,
  classification, readiness, risk, evidence, or revision content.
- Similar rows, shared commands, a common test set, or an existing verdict do
  not authorize copied reasoning.
- The source XLSX, `data/tests.json`, `data/tests_gpt_merged.json`, and
  `gpt-review/test_gpt_review.json` remain unchanged during this pilot.

## 3. Four-layer V3 review

### Layer 1: Test Intent Accuracy

Establish only what the source row actually requests:

- purpose, target, scope, action, execution location, duration, repetitions,
  conditions, expected result, and required evidence;
- platform-specific applicability and any required vendor/model qualification;
- whether the procedure and criteria support the item or conflict with it.

Do not reduce stress to inventory, firmware upgrade/downgrade to version
readback, all-device coverage to one device, hours to minutes, loops to one
run, functional validation to enumeration, or one OS's evidence to another.
Do not claim an unobservable hardware behavior was verified.

If intent is incomplete, name the exact missing facts. If the source fields
contradict each other, preserve each fact and use `SOURCE_CONFLICT` rather than
inventing a coherent replacement.

### Layer 2: Automation Capability

Use exactly one current classification:

- `FULLY AUTOMATABLE`
- `REQUIRES PACKAGE / USER CONFIRMATION`
- `MANUAL ONLY`
- `BLOCKED`

`FULLY AUTOMATABLE` means the complete requested test activity can be carried
out by the agent after ordinary engineering checks, with known dependencies
and machine-verifiable evidence. Read-only is often, but not automatically,
fully automatable.

`REQUIRES PACKAGE / USER CONFIRMATION` means the intent and operation are
identifiable and the activity is technically executable after an engineer
supplies a package, vendor tool, license, image, SOP, target, parameter,
fixture step, maintenance window, or approval. It also covers hybrid manual
setup plus automated evidence collection.

`MANUAL ONLY` means the requested acceptance activity is physical or visual
and has no reasonable automated substitute. Supporting logs do not turn a
manual visual criterion into an automated one.

`BLOCKED` means a safe deterministic test still cannot be defined because the
purpose, target identity, operation semantics, acceptance criterion, or
recovery requirement is irreducibly ambiguous. A missing obtainable artifact
or one-time input alone is not enough.

Risk and automation capability are orthogonal. Destructive, service-impacting,
firmware, reboot, power, and fault-injection activities can be technically
automatable while still requiring explicit approval and recovery controls.

### Layer 3: Execution Readiness

Assign one or more readiness labels:

- `READY`
- `NEEDS_INPUT`
- `NEEDS_SPEC`
- `NEEDS_PACKAGE`
- `NEEDS_APPROVAL`
- `NEEDS_MANUAL_ACTION`
- `SOURCE_CONFLICT`
- `NOT_APPLICABLE`

For every row state:

1. what is available now;
2. what is missing;
3. who must provide it;
4. which safe read-only facts may be collected now;
5. which actions are prohibited until the gate is satisfied; and
6. how closure of each missing item will be verified.

Missing expected values do not prevent collection of actual values. Actual
collection does not constitute PASS or completion of a testcase whose
comparison, stimulus, duration, repetitions, or coverage remains outstanding.
`READY` never removes the receiving engineer's normal pre-execution check.

### Layer 4: Agent Execution Contract

The revision candidate must make these items unambiguous without turning every
case into a full remote-execution script:

- Test Purpose
- Applicable Platform / Environment
- Target Scope
- Required Inputs
- Test Command / Procedure Intent
- Preconditions
- Expected Evidence
- Acceptance Reference
- Safety Restrictions
- Human Approval Requirements
- Manual Boundaries
- Recovery Requirements
- Stop Conditions

The command remains concise and faithful to the source. The later agent may
plan SSH, logging, pre-checks, post-checks, and rollback for the actual DUT, but
must not redefine the test purpose, shrink scope, change duration, omit loops,
or substitute a different tool/path when that path is itself under test.

## 4. BLOCKED re-evaluation

For every historical `BLOCKED` case, answer independently:

1. Is the test purpose itself unintelligible?
2. Is the gap an engineer-supplied tool, parameter, specification, image,
   license, SOP, target, or expected value?
3. Is there a manual-stimulus plus automated-verification workflow?
4. Which read-only inventory, identity, state, topology, version, or log facts
   can be gathered before the gated action?
5. Which concrete condition advances the test to its next stage?
6. Which unresolved ambiguity would still make execution unsafe or
   non-deterministic after the expected input is supplied?

Do not use generic reasons such as `Missing SOP`, `Unsafe`, `Potential risk`,
or `Requires confirmation`. Name the testcase-specific target, missing
semantic, blast radius, evidence, and closure test. Reducing the number of
BLOCKED cases is not a quality target.

Historical `second_review_outcome=BLOCKED` is a V2 comparison outcome. It is
not the current automation classification and must not be counted as one.

## 5. Technical review boundaries

Apply only the domains present in the source row. Distinguish host OS, BMC/OOB,
Redfish, UEFI/BIOS, physical/KVM, and external peer execution locations.
Distinguish host DDR from GPU HBM; PCIe from NVLink/NVSwitch; InfiniBand from
Ethernet/RoCE; NVIDIA from AMD GPU tooling; Intel from AMD CPU/RAS behavior;
and standard commands from OEM/ODM vendor interfaces.

Never assume a feature, topology, device index, BDF, firmware layout, sensor
name, Redfish resource ID, network interface, storage target, or recovery path
is shared across white-box systems. Platform-specific expected values require
an identified applicable platform specification.

Safety invariants from V2 remain in force: never guess a destructive storage
target; never assume GPU indices/BDFs; preserve logs; require image-to-device
compatibility and recovery for firmware; validate management connectivity and
OOB recovery before disruptive network actions; and treat Wistron I2C/I3C as
BMC/platform-management scope unless an applicable platform specification says
otherwise.

## 6. External technical evidence

Use current official documentation when command syntax, version behavior, or
hardware capability is uncertain. Prefer NVIDIA, AMD, Intel, Linux kernel,
DMTF Redfish, UEFI, PCI-SIG, MLCommons, and the applicable component/server
vendor. A third-party source may identify a lead but cannot establish a
platform requirement.

For every technical correction record the URL or repository path, title,
version/date when available, applicable platform/tool version, supported
judgment, and remaining uncertainty. External sources must never receive
private specifications, firmware, credentials, or internal logs. If the web
is unavailable, record `WEB_UNAVAILABLE`; do not present memory as current
verification.

## 7. Per-case procedure

Complete these steps for exactly one case before selecting the next:

1. Resolve the unique source key and `case_variant_id`.
2. Directly read the exact XLSX row, including original and DeepSeek columns.
3. Read the matching DeepSeek JSON record as a cross-check.
4. Read the matching GPT V2 overlay.
5. Read applicable historical corrections and locked user decisions.
6. Write the source-grounded original test intent.
7. Identify specific V2 agreements, errors, omissions, or unsafe assumptions.
8. Decide automation capability and readiness labels independently.
9. Verify uncertain technical points against official public sources when
   needed.
10. Write the testcase-specific V3 revision candidate and execution contract.
11. State what is objectively better than V2. Longer English is not evidence.
12. Run the per-case integrity checks, persist the record, update the verified
   next key, and only then open another case.

## 8. V3 review result fields

Use one primary `review_outcome`:

- `KEEP`
- `IMPROVED`
- `RECLASSIFIED`
- `REWRITE_REQUIRED`
- `SOURCE_CONFLICT`
- `NEED_ENGINEER_DECISION`

Each record must include the original intent, V2 conclusion, V3 conclusion,
identified defects, changed fields, reason, new evidence, removed ambiguities,
resolved and remaining blockers, agent-understanding result, regression status,
source hashes, and a clear answer to: `What is objectively better than V2?`

`KEEP` is correct when V2 is technically sound. V3 does not overwrite
`second_review_outcome`.

## 9. Checkpoints and anti-template controls

- Save after every case. Save a checkpoint every 20 cases and a quality summary
  every 50 cases.
- Before and after each case, verify the source hashes and that exactly one V3
  record and progress key advanced.
- Reject a record if its core reason, intent, hazard, evidence, or improvement
  could be pasted into a different selected case without changing technical
  facts.
- Duplicate commands are allowed only when independently confirmed as correct.
  Duplicate rationale is an audit signal and must be investigated.
- If source mapping, next-key integrity, or independent reasoning fails, mark
  the affected range invalid, restore the last valid checkpoint, preserve an
  invalid-run notice, and re-review from the first affected case.

## 10. Calibration and continuation gate

Review the fixed 20-case calibration set first. It must include the five locked
boundary cases and cover read-only, GPU/PCIe, CPU/memory stress, firmware,
BIOS/BMC, destructive storage, physical work, missing specifications, hybrid
execution, and a genuine semantic blocker.

Before continuing to the remaining 180, confirm that V3:

- clarifies intent and agent action more than V2;
- separates missing inputs from genuine blockers;
- introduces no unsafe permission or target assumption;
- preserves duration, loop count, scope, path, and evidence;
- is concise enough for an execution agent;
- contains no copied or generic reasoning; and
- makes material improvements rather than stylistic rewrites.

Record the draft-to-calibrated rule changes. Failed calibration cases must be
fixed and revalidated before expansion.

## 11. Agent understanding validation

Use an isolated reviewer without DUT access and give it only the proposed
execution contract. Ask the ten questions defined by the pilot specification.
Compare its answer with the confirmed source intent and detect scope reduction,
wrong target/location/command, missing repetitions or duration, missing
evidence, unsafe action, false completion, incorrect BLOCKED, and unjustified
PASS.

Classify a failure as testcase-document defect, platform-handoff defect, or
model-planning defect. Revise and re-run when the testcase text caused the
failure. If no independent environment is available, record `NOT_VALIDATED`;
the authoring reviewer cannot self-certify independence.

## 12. Completion semantics

Keep these states separate:

- `Review completed`: a source-backed V3 record exists.
- `Semantically validated`: the record passed source and regression review.
- `Agent understanding validated`: an isolated reviewer interpreted the
  execution contract correctly.
- `Hardware tested`: actual authorized DUT execution occurred.

This pilot performs no DUT operations and must never claim hardware PASS.
