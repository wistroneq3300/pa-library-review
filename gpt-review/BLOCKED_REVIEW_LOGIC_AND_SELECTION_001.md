# BLOCKED Review Logic and Selection 001

## Purpose

This file governs the follow-up review of selected BLOCKED cases after the
first 200 testcase reviews. It supplements the existing GPT second-review
workflow and does not replace it.

The original testcase overlay remains the historical result. Follow-up results
must be appended to a separate history artifact and must not mutate the
original record merely because new logic was introduced.

## Reopening Gates

A BLOCKED case may be reclassified only when the review has enough evidence to
pass every applicable gate below:

1. **Exact target identity**: the device, port, controller, firmware family,
   setting, or state being tested is uniquely identified.
2. **Exact operation semantics**: the permitted operation, tool, API, payload,
   image, or physical action is specified. A generic command substitute is not
   evidence that the required operation is defined.
3. **Parameters and acceptance criteria**: values, sequence, timing, retries,
   expected output, and pass/fail thresholds are explicit.
4. **Dependencies**: required packages, licenses, images, drivers, firmware,
   credentials, cables, fixtures, or vendor utilities are identified and
   available or explicitly assigned to the operator.
5. **Safety and recovery**: destructive effects, abort conditions, rollback,
   backup, power/redundancy constraints, and recovery ownership are defined.
6. **Evidence mapping**: every acceptance criterion has a concrete evidence
   source such as a command result, log, screenshot, measurement, or physical
   observation.
7. **Source/reference conflict resolution**: conflicts between the testcase
   source and DeepSeek material are resolved using the source and verified
   product information. DeepSeek is reference input, never the answer.

Missing a package alone normally leads to `REQUIRES PACKAGE / USER
CONFIRMATION`; missing semantics, identity, acceptance criteria, or safe
recovery keeps the case `BLOCKED` only when the missing information prevents
the operation from being safely defined even as a user/vendor prerequisite.

## Automation-boundary correction

The following distinction is mandatory and supersedes an overly conservative
interpretation of the reopening gates:

1. A missing vendor document, application note, firmware image, flash command,
   decoder, package, license, or operator-provided parameter is normally a
   prerequisite for `REQUIRES PACKAGE / USER CONFIRMATION`, not a `BLOCKED`
   verdict, when the testcase purpose and operation are identifiable.
2. A required physical action, BIOS interaction, cable insertion/removal, or
   manual visual check is not by itself `BLOCKED`. Use `MANUAL ONLY` when the
   whole testcase has no reasonable automated portion. Use
   `REQUIRES PACKAGE / USER CONFIRMATION` when a manual setup step is followed
   by an automatable readback or verification step.
3. OS installation, firmware flashing, BIOS changes, reboot, reset, and
   power-cycle steps remain executable test activities with explicit safety
   gates. Their destructive or service-impacting nature requires a target,
   operator confirmation, and recovery plan; it does not automatically make
   them `BLOCKED`.
4. Use `BLOCKED` only when the testcase purpose, target, operation semantics,
   acceptance criteria, or recovery cannot be made safe and deterministic even
   after the expected vendor artifact or user input is identified as a
   prerequisite. Do not convert an obtainable dependency into a permanent
   semantic blocker.

## Second-review outcome field for follow-up records

Every newly written follow-up record must include the fixed
`second_review_outcome` enum. It is separate from
`automation_classification`:

- `AGREE`: the DeepSeek conclusion is accepted as-is; optional explanation
  does not materially alter the decision.
- `IMPROVED`: the conclusion/classification stays the same, while GPT adds
  material procedure, evidence, safety, recovery, thermal, blackbox,
  interface, or fault-stimulus detail.
- `CHANGED`: GPT changes the automation classification or another material
  execution conclusion.
- `BLOCKED`: the second review finds that safe execution remains impossible
  because of an irreducible semantic, identity, criteria, or recovery blocker.
  A missing package or operator input alone is not enough.
- `UNRESOLVED`: available material is insufficient to decide whether DeepSeek
  should be accepted, improved, or changed, without enough evidence to claim a
  safety blocker.

Choose exactly one value from the current testcase's own source and DeepSeek
comparison, and explain it in the testcase-specific findings. Do not backfill
completed historical records solely for this field; apply it from the next
newly written follow-up record onward.

## Follow-up Procedure

For each selected case, one case is handled at a time:

1. Read the exact source row again.
2. Read the matching DeepSeek record again for reference only.
3. Read the original GPT overlay record and identify what remains unresolved.
4. Apply each reopening gate independently.
5. Record the new decision, unresolved gates, safety implications, and required
   evidence in the follow-up history artifact.
6. Preserve the original record, assert source hashes, run `git diff --check`,
   commit the single follow-up case, and push it.

No automatic downgrade is allowed because a case looks similar to another
case, because a command exists, or because a package might be installable.
Repeated reasoning must be written from the current case's exact source and
evidence.

## Run quota and continuation rule

- A manually requested review run defaults to at least 200 sequentially
  unreviewed cases unless the user explicitly changes the quota.
- The daily scheduled run is configured for 50 cases per day.
- `REQUIRES PACKAGE / USER CONFIRMATION` and `MANUAL ONLY` are review
  classifications, not automatic stop conditions. Missing execution inputs
  must be recorded while the reviewer continues to the next source row.
- Stop only for a decision required to determine the review itself, an
  unresolvable purpose/identity/operation/recovery question, or a hard safety
  blocker. If a run stops before its quota, persist the exact stop reason and
  the verified next source key.

## Initial Selection

The first five selected cases provide different blocker patterns:

### `Wistron-HW-00032-V004` - CRPS latch offset to next block

Required evidence includes the vendor configuration layout, field/address,
block boundaries, byte order, expected offset, read-only access method, and
recovery if a write is involved. Without those details, a generic SMBus or
IPMI read is not a valid implementation.

### `Wistron-HW-00070-V004` - Firmware upgrade/downgrade

Required evidence includes the exact PSU identity, current and target image
versions, image hashes, signed-image rules, update method, the exact five-cycle
sequence, redundancy and power constraints, abort behavior, and recovery
procedure. A firmware command without those controls is unsafe and
non-deterministic.

### `Wistron-HW-00153-V002` - OS installing

Required evidence includes the exact TPM setting and expected state transition,
OS image and version, installation target, storage and boot mode, backup and
key handling, reboot checkpoints, and recovery. The DeepSeek record's copied
TPM-oriented flow does not define the OS installation testcase.

### `Wistron-HW-00207-V002` - Serial communication

Required evidence includes the physical serial port and electrical standard,
pin/cable mapping, baud/data/parity/stop/flow settings, client/server role,
test payload, expected response, timeout, retry, and alternate-console or
recovery plan. A physical cable check alone does not define communication.

### `Wistron-HW-00210-V002` - Device detection

Required evidence includes the complete USB port, controller, device, driver,
power, BIOS/security, and operating-system matrix, plus the required coverage
and pass criteria. The phrase "all USB port/device/detected" is not a
deterministic test plan.

## User-feedback correction and re-review scope (2026-09-26)

The first five selected cases must be re-reviewed one at a time under the
automation-boundary correction above. The previous follow-up conclusions are
historical and must not be copied forward:

- `Wistron-HW-00032-V004`: vendor PMBus Application Note/Firmware Spec and
  decoder/command are prerequisites; do not call the case `BLOCKED` solely
  because they are not yet attached.
- `Wistron-HW-00070-V004`: vendor PSU firmware and validated flash command are
  prerequisites; firmware risk requires confirmation and recovery, not an
  automatic `BLOCKED` verdict.
- `Wistron-HW-00153-V002`: BIOS/OS installation may require manual operation,
  while post-install TPM verification can be automated; this is a hybrid
  case, not `BLOCKED`.
- `Wistron-HW-00207-V002`: serial cable handling is a physical execution
  boundary; classify as `MANUAL ONLY` when the communication purpose is clear.
- `Wistron-HW-00210-V002`: BIOS port checks may be manual and OS USB evidence
  can be automated; classify the hybrid workflow accordingly, not `BLOCKED`.

Each case still requires its own source reread, DeepSeek comparison, purpose,
command/evidence check, risk decision, and separate saved review record.

The user's five-case decisions are persisted in
`gpt-review/BLOCKED_FEEDBACK_REREVIEW_001.json`; the original BLOCKED records
remain historical evidence and must not override the confirmed boundary above.

## Re-review Outcome Rules

- `BLOCKED` remains correct when any safety-critical or determinism-critical
  gate is still missing.
- `REQUIRES PACKAGE / USER CONFIRMATION` is appropriate only when the
  operation and acceptance criteria are defined and the remaining gap is an
  identified package, license, credential, or explicit operator confirmation.
- `MANUAL ONLY` is appropriate when the exact physical observation/action is
  defined but cannot be safely or reliably delegated to the supported
  automation environment.
- `FULLY AUTOMATABLE` requires a complete, deterministic, non-destructive or
  explicitly approved procedure with machine-verifiable evidence and no
  unresolved human-only step.
