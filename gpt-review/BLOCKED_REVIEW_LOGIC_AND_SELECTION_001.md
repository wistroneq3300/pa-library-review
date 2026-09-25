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
recovery keeps the case `BLOCKED`.

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
