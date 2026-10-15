# Review Workflow Logic V3.1

Status: final review contract for the fixed 200-case V3.1 re-review, 2026-10-13

V3.1 is a prospective overlay. It preserves `REVIEW_WORKFLOW_LOGIC_V3.md`, the
V2 overlay, DeepSeek history, source workbook, and production JSON. It changes
how a reviewer distinguishes a reusable master testcase from a project run.

## 1. Authority and preservation

Apply evidence in this order:

1. Exact original XLSX row facts and provenance.
2. Explicit engineering decisions in the current handoff and
   `V3_1_ENGINEERING_DECISIONS.md`.
3. This V3.1 contract.
4. Still-compatible V3 and V2 source-integrity and safety rules.
5. Applicable official technical documentation for a named tool/platform
   version.
6. V3, GPT V2, DeepSeek, and older review results as challengeable history.

The atomic unit remains `(sheet, physical source row, code, case_variant_id)`.
The reviewer must reopen that XLSX row and independently read its original
fields, DeepSeek columns, GPT V2 result, and V3 record. No adjacent-row,
test-set, regex, or classification rule may replace the technical review.

The original XLSX, `data/tests.json`, `data/tests_gpt_merged.json`, GPT V2,
and V3 Pilot records are immutable in a V3.1 task.

## 2. Shared Master Library principle

The 3,112 rows form a shared Server SIT and GPU Server SIT Master Test
Library, not a fixed execution script for one project. Preserve all original
intent, procedure, command, tool, parameter, criteria, timing, and provenance.

The project test plan owns platform applicability, device targets, execution
method, tool/script, duration, iteration count, expected values, coverage, and
approved overrides. Missing project-specific values do not by themselves make
the master row permanently `BLOCKED`.

A V3.1 record must separate:

- `master_default`: every source value exactly as written;
- `project_inputs`: values the project must bind before execution;
- `approved_override`: an explicit engineer-approved deviation, if any;
- `actual_execution`: what was actually performed, if later supplied;
- `coverage_difference`: the exact unexecuted or differently executed master
  scope; and
- `engineering_verdict`: reserved for the engineer.

An override never edits or silently supersedes the Master Library.

## 3. Project override and completion semantics

Completion is evaluated against the approved project run, while coverage is
reported against both project and master requirements. Example: completing an
approved 100-reboot run means the 100-run project plan completed; it does not
mean the master default of 500 reboots was completed.

The agent must record approval identity/time, target, exact command/method,
parameters, count/duration, coverage delta, actual execution status, and raw
evidence. It must not issue a formal testcase PASS/FAIL/BLOCKED verdict.

## 4. Timing fields

Attended Time and Machine Time are normally planning/reference metadata.
Procedure durations and iteration counts are preserved separately. A mismatch
is not automatically `SOURCE_CONFLICT` or execution-blocking.

Use `SOURCE_CONFLICT` only when the source explicitly defines both timing
values as normative test requirements and they cannot simultaneously be
satisfied. Otherwise record `TIMING_DIFFERENCE_RETAINED` and require the
project plan to choose the execution value without rewriting the master.

## 5. Automation model

Use exactly one capability class:

- `FULLY AUTOMATABLE`
- `REQUIRES PACKAGE / USER CONFIRMATION`
- `MANUAL ONLY`
- `BLOCKED`

Also record independently:

1. automation capability;
2. execution readiness;
3. manual test activity;
4. required user inputs; and
5. safety approval.

Supplying a specification, parameter, package, or one-time `OK` does not make
the test activity partial. Physical setup, cabling, fixtures, or environment
configuration followed by automated execution/evidence is hybrid and normally
`REQUIRES PACKAGE / USER CONFIRMATION`. If the core acceptance requires a
human visual judgment, such as UID LED state, it may remain `MANUAL ONLY` even
when an agent can send a supporting command.

Missing vendor tools, images, expected values, or private specifications are
normally readiness gaps, not permanent blockers, when purpose, target class,
operation, safety boundary, and evidence can be defined. Retain `BLOCKED`
only for irreducible ambiguity that prevents a safe deterministic plan.

## 6. Approval authority

One authorized engineer may approve a defined run. V3.1 adds no two-person
signoff requirement. This does not waive target identity, impact scope,
storage protection, safety checks, recovery, or explicit execution approval.
An externally mandated project approval rule still applies when documented.

One run-level approval covers all loops within the unchanged approved plan.
Obtain a new approval before changing target, command, material parameters,
destructive scope, recovery action, retry, installation, or system change.

## 7. Existing validation tool first

Before proposing new automation, determine whether the project already has an
applicable PA Manager Cycle, project cycle script, approved GPU diagnostic,
vendor tool, or stress script. Prefer that tool when its version and coverage
match the approved project plan. Tool success alone does not prove testcase
completion; map every acceptance/evidence requirement to tool output and list
coverage gaps.

Do not duplicate PA Manager Cycle control logic.

## 8. Original and modernized methods

Always preserve the original procedure, command, tool, and parameters. A
separate `modernized_recommendation` may be supplied when verified and useful.
It must state:

- recommended tool/method;
- applicable platform;
- supported version;
- official technical reference;
- difference from the original;
- coverage difference;
- required inputs; and
- risks/limitations.

If the original remains correct, explicitly retain it. Never invent a command,
tool, specification, expected value, or supported version. Public official
documentation cannot replace a project-private acceptance specification.

Do not replace the function under test with a different observation path.
Redfish telemetry cannot by itself complete a WebUI display test, and a CLI
readback cannot replace a required physical LED observation.

## 9. Tool defaults

An official tool default may be a project-plan candidate only after recording
the tool version, documented default, applicability, functional impact, and
safety impact. The user must be told which defaults are proposed and confirm
them before execution. Unverified defaults must remain unresolved.

## 10. Storage safety

For fio, dd, format, filesystem, GDS, or any write workload, resolve a stable
exact target and prove it is not an OS/boot/EFI device, mounted or active
filesystem, swap, LVM/RAID/device-mapper member, user-data disk, evidence
destination, recovery media, or unidentified device. An engineer's `OK` does
not replace target safety validation.

The agent must not unmount, format, wipe, repartition, or reconfigure storage
to bypass a safety gate. Preserve the original fio profile; an approved
project override is separate. Missing vendor performance reference may permit
an approved safe workload to collect Actual data, but no performance PASS may
be claimed without a comparable reference.

## 11. Platform-specific expected values

GPU, PCIe, NVLink/NVSwitch, sensor, firmware, device-count, port-count, and
topology expectations belong to an identified platform/configuration and
approved specification. They are not global master constants. A historical
PASS report may be used only as an engineer-approved reference after platform,
version, configuration, workload, and evidence equivalence are checked.
Never convert the current Actual into Expected.

## 12. Source conflicts and project resolution

Preserve contradictions among Test Name, Procedure, Criteria, command, and
normative parameters. A project engineer may define the current project scope,
but that resolution does not permanently repair the master row and may not
merge or delete distinct test intents. Record both the original conflict and
the project decision.

## 13. WebUI and manual tests

WebUI interaction is normally engineer-operated. The agent may explain steps,
answer questions, analyze screenshots/logs, organize evidence, and identify
missing data. It must not claim it clicked, viewed, or verified a WebUI unless
an authorized supported UI-control execution actually occurred and produced
evidence; this review task performs none.

For UID LED and other core visual checks, the engineer supplies the formal
observation. Agent-sent commands and logs are supporting evidence only.

## 14. Continue-on-error and retry

Record ordinary warnings/errors and continue collecting data according to the
approved plan. A long stress run does not stop merely because of a non-safety
warning unless the plan says so. Stop the affected action for hardware safety,
data-integrity risk, loss of control, or an approved safety-stop condition.

Never add an automatic retry after failure. Preserve the first failure; a
later successful run cannot overwrite it. The next pre-approved cycle loop is
not a retry. Do not perform unapproved recovery merely to reach a loop count.

## 15. Package installation

Before installation, report package/tool, source, version, dependencies,
exact installation command, system impact, and rollback. Install only after
confirmation. Never independently change a driver, kernel, firmware, or other
critical component.

## 16. Engineer-owned verdict

The agent executes an approved plan, collects raw evidence, records actuals,
compares and flags differences, identifies risk/anomalies, and organizes the
report. Formal testcase PASS/FAIL/BLOCKED remains the engineer's decision.
Preserve tool-emitted PASS/FAIL as raw evidence without elevating it to the
engineering verdict.

## 17. Network mode

Treat InfiniBand, RoCE, and Ethernet as distinct project-selectable modes.
Record mode, endpoints, ports, topology, commands/tools, parameters, and
Expected independently. Do not merge evidence across modes.

## 18. Vendor-specific tools

WAT, NVDiag, NVQual, OEM flash utilities, and other private tools require the
applicable official manual, tool help, or approved SOP. Unavailable documents
do not make automation permanently impossible, but ambiguous command semantics
prohibit guessed execution, especially destructive or state-changing actions.

## 19. Per-case V3.1 review procedure

For each manifest entry, complete and persist one record before the next:

1. Reopen the exact XLSX row and record its row hash.
2. Read the same-row DeepSeek columns and matching `data/tests.json` entry.
3. Read the matching GPT V2 and V3 records and applicable decisions/history.
4. Restate the row-specific original intent, device/target, conditions,
   original parameters, and evidence requirement.
5. Determine whether V3.1 engineering decisions change V3.
6. Re-evaluate capability and readiness independently.
7. Separate master defaults, project inputs, approved overrides, and Actual.
8. Preserve the original method; add a verified modernization only if useful.
9. Record coverage, missing inputs, safety boundary, no-retry rule, and
   engineer-owned verdict boundary.
10. State the objective change from V3 or the concrete reason for `KEEP`.
11. Check for intent, coverage, safety, identity, command, and evidence
    regression.
12. Persist exactly one record and advance the source-verified checkpoint.

## 20. Required V3.1 record content

Each record must include: unique source key; original intent; original
procedure/criteria; DeepSeek/V2/V3 conclusions; V3.1 conclusion; applicable
decision IDs; capability class; readiness; manual activity; required inputs;
master/project/override/actual separation; original method; modernization;
coverage difference; missing inputs; safety boundaries; expected evidence;
no-retry behavior; engineer-verdict boundary; objective improvement; and
regression result.

Use one outcome: `KEEP`, `IMPROVED`, `RECLASSIFIED`, `SOURCE_CONFLICT`, or
`NEED_ENGINEER_DECISION`. A V3 `SOURCE_CONFLICT` may become `IMPROVED` when
V3.1 correctly downgrades a non-normative timing difference, but the underlying
source facts remain preserved.

## 21. Validation and release gates

All materially changed high-risk contracts and representative other changes
receive isolated no-DUT understanding validation for intent, override, target,
method, inputs, safety, evidence, no retry, and engineer verdict. Same-model
family validation must be labeled as such.

Completion requires exactly 200 manifest keys, correct XLSX mappings, no
source/history modifications, no invented test results, no hardware PASS,
no agent-owned formal verdict, no automatic retry, no unapproved method/tool
replacement, and traceable official references for every modernization.

This review never connects to a DUT and never merges `main`.

## 22. Final Audit clarifications (ED-30 and ED-31)

Manual establishment of a chamber, rail, fixture, cable, population, or other
physical precondition followed by automated workload execution, monitoring and
log collection is hybrid capability. Use the canonical classification
`REQUIRES PACKAGE / USER CONFIRMATION`; retain the operator-owned setup,
calibration, interlocks, stop authority and recovery. Do not apply this rule
when the repeated physical operation or human observation is itself the core
acceptance activity.

When the core test is BMC WebUI presentation, rendered sensor values, page
content, link navigation, or another human-visible UI state, use `MANUAL ONLY`.
An agent may explain steps, compare an engineer-supplied screenshot with a
specification, correlate Redfish/IPMI/log data and organize evidence. It may not
replace the required WebUI observation with backend telemetry or claim that AI
screenshot analysis made the test fully automated.

## 23. Additive overlay retention rule

V3.1 and the Final Audit are additive overlays over the exact source row and
its V3 record. An omitted V3 procedure detail, command token, duration,
iteration, target, evidence item, stop condition, safety boundary, or recovery
requirement is not deleted unless a later record explicitly identifies the
field, gives a reason, records the coverage effect and names the controlling
engineering decision. Concision is never an implicit override.

Effective review order is: immutable XLSX source and provenance; V2/V3 history;
V3.1 explicit changes; Final Audit explicit corrections. A conflict between
layers is surfaced for engineering resolution, never silently normalized.

`SOURCE_CONFLICT` is reserved for contradictory source requirements or
mutually incompatible source intents. Missing project values, absent vendor
documentation, undefined intent, and a missing external specification are
recorded respectively as readiness, private-document, unclear-intent, or
semantic-block conditions; they are not called source conflicts unless two
source statements actually disagree.

## 24. Approved engineering clarifications (ED-33 through ED-52)

The controlling register for the 2026-10-15 rulings is
`v3-1-full-3112/ENGINEERING_DECISIONS_APPROVED_20261015.md`.

The Master Source remains immutable. Tool choice, target values, firmware,
Expected, parameters and execution environment are project bindings. An
approved alternative method is recorded as an overlay with its coverage delta;
it cannot erase the source-named method or claim that unexecuted tool coverage
passed. A missing project binding is normally execution-readiness pending, not
permanent `BLOCKED`.

Read-only evidence may supplement a functional test but may not replace a
required write, flash, setting change or compliance-mode action. BIOS fields are
handled according to actual platform writability, with readback/restoration for
writable fields and authoritative comparison for read-only fields. Static review
completion remains separate from execution and engineer-owned DUT verdict.

Apply ED-39 through ED-52 only to their named source variants. Preserve every
original contradiction in the record while placing the approved engineering
interpretation in the additive V3.1 decision layer. BIOS 00376 remains the sole
explicitly unresolved case in this decision set.
