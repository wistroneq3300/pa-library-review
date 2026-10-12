# Rule Precedence and Conflict Report

## Controlling distinction

The repository contains several generations of rules that answer different
questions. V3 keeps them separate instead of merging their vocabulary.

| Evidence class | What it controls | V3 treatment |
| --- | --- | --- |
| Original XLSX row | Test identity, stated procedure, criteria, duration, loop, and source facts | Highest factual authority. Contradictions among `Items`, `Procedure`, and `Criteria` become `SOURCE_CONFLICT`. |
| User-confirmed decisions | Classification boundaries and specifically adjudicated cases | Binding unless new source or official technical evidence proves the premise changed. |
| GPT V2 logic | Source preservation, one-row review, safety, four formal classifications, and comparison history | Retained where consistent with V3; not treated as a technical answer. |
| DeepSeek / old YES-PARTIAL-NO rules | Historical execution advice and legacy UI meaning | Reference only. Mapped explicitly; never copied as the V3 verdict. |
| Historical review records | What previous reviewers concluded and why | Auditable comparison baseline; preserved even when wrong. |
| V3 requirements | Intent accuracy, readiness, execution contract, evidence, and validation | Applied prospectively in the separate V3 overlay. |

## Confirmed user boundaries

The following five decisions from
`BLOCKED_FEEDBACK_REREVIEW_001.json` are locked calibration boundaries:

- `Wistron-HW-00032-V004`: missing CRPS PMBus specification and decoder are
  prerequisites; they do not by themselves make the identifiable read-only
  offset test permanently BLOCKED.
- `Wistron-HW-00070-V004`: PSU firmware/image/flash procedure and approval are
  execution prerequisites. Firmware risk is handled with identity,
  compatibility, maintenance, evidence, and recovery gates.
- `Wistron-HW-00153-V002`: the BIOS/OS-install portion is manual or gated and
  post-install TPM verification can be automated. The row also contains an
  Items-versus-Procedure/Criteria conflict that V3 must preserve.
- `Wistron-HW-00207-V002`: the serial cable/terminal activity is a manual
  boundary. Missing settings and payload are required inputs, not proof that
  the physical communication purpose is unknowable.
- `Wistron-HW-00210-V002`: USB attachment/BIOS observation plus OS enumeration
  is a hybrid workflow. One `lsusb` snapshot cannot prove all-port coverage.

These boundaries do not authorize copying the five historical conclusions;
each selected row must still be re-read and independently analyzed.

## Material conflicts found

### 1. Legacy verdict vocabulary versus V2 classifications

The locked 2026-09-18 YES/PARTIAL/NO definition asks whether a human must act
mid-run after one-time inputs are supplied. V2 asks about broader automation
capability using `FULLY AUTOMATABLE`, `REQUIRES PACKAGE / USER CONFIRMATION`,
`MANUAL ONLY`, and `BLOCKED`. These are not interchangeable.

V3 preserves the formal V2 four-class taxonomy. Legacy verdicts may explain a
historical record but do not populate V3 classification fields.

### 2. Old conservative archetypes versus corrected BLOCKED boundary

Earlier material sometimes treated missing proprietary packages, vendor
specifications, firmware images, physical steps, or high risk as NO/BLOCKED.
The confirmed correction states that obtainable artifacts and manual setup are
prerequisites when purpose and operation are identifiable. V3 separates:

- automation capability;
- execution readiness;
- safety/approval; and
- irreducible semantic blockers.

### 3. `second_review_outcome` versus automation classification

Historical `second_review_outcome=BLOCKED` describes a comparison result. It
does not mean the current `automation_classification` is BLOCKED. V3 adds its
own `review_outcome` and never overwrites the V2 field.

### 4. Title-first legacy guidance versus source-field conflict handling

The old workflow often says `Items` is authoritative. The V3 task explicitly
requires contradictions among Items, Procedure, and Criteria to be exposed.
V3 uses Items to locate the stated subject but will not rewrite conflicting
Procedure/Criteria to fit the title. The row receives `SOURCE_CONFLICT` and a
specific engineer decision request when the conflict changes the requested
operation or acceptance rule.

### 5. Command completeness versus concise execution contract

The old library workflow emphasized fully runnable SSH/job-file wrappers. V2
later states that `Test Command` is concise intent and the receiving agent owns
environment-specific execution planning. V3 follows the latter for revision
candidates while retaining target, scope, duration, repetition, evidence,
safety, approval, and recovery requirements.

### 6. Global pre-execution approval versus capability

V2 requires an explicit `OK` before actual testcase execution. This is an
execution policy, not evidence that every row is technically non-automatable.
V3 records approval independently under readiness and the execution contract.

### 7. Generic cross-platform assumptions

Historical commands may assume one BMC path, sensor name, device index,
firmware layout, Linux distribution, or GPU vendor. V3 permits vendor slots
only when the source intent remains intact and the slot owner/closure test is
explicit. An official document is applicable only to the identified
platform/tool version.

## Preserved safety rules

V3 retains the prohibitions against guessing destructive storage targets,
GPU indices/BDFs, firmware compatibility, management interfaces, vendor
commands, power/reboot parameters, and recovery paths. It also retains log
preservation, read-only pre-checks, explicit approval for gated actions, and
the Wistron-specific default that I2C/I3C is BMC/platform-management scope.

## New V3 quality requirements

- Four distinct layers: intent, capability, readiness, and agent contract.
- Explicit `SOURCE_CONFLICT` handling.
- An evidence-backed statement of what is objectively better than V2.
- Source-specific closure criteria for every missing input or blocker.
- Isolated agent-understanding validation and failure attribution.
- Per-case regression status and exact immutable source hashes.
- Calibration gate before expansion from 20 to 200 cases.

This report is interpretive documentation. Per-case conclusions remain in the
V3 review records.
