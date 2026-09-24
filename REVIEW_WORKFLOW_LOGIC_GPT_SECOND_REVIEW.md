# GPT Second Review Logic for GPU Server SIT Test Library

Status: working review contract, 2026-09-25

This document defines the GPT second-review behavior for the 3112-case GPU
Server SIT test library. It supplements the historical DeepSeek review logic;
it does not replace or modify the original test library.

## Source and comparison rules

- `data/REVISED_commands_merged_with_raw.xlsx` is the original testcase source.
- `data/tests.json` contains the previous DeepSeek review and is reference data.
- The original testcase fields are `Code`, `Items`, `Procedure`, and `Criteria`
  in the XLSX, corresponding to `code`, `items`, `procedure`, and `criteria`
  in `data/tests.json`.
- GPT must independently review the testcase purpose and must not assume the
  DeepSeek result is correct.
- The original XLSX and `data/tests.json` are source-of-truth files and must
  never be modified, overwritten, renamed, deleted, or rewritten.
- GPT second-review results are stored separately and associated by the real
  testcase `code` key.

## Role and execution boundary

GPT reviews as a senior GPU Server SIT engineer, Linux/BMC/GPU/storage/network
engineer, safety reviewer, and OpenHands automation designer.

GPT does not directly execute the DUT test. GPT produces a concise, technically
correct test description for a later AI agent/OpenHands run.

The `Test Command` field tells the agent what test to run. It is not execution
permission. The receiving agent must independently generate and perform suitable
pre-checks, safety gates, logging, post-checks, and recovery before execution.

GPT must not replace the concise testcase command with a full SSH wrapper,
pre-check script, post-check script, or recovery bash program unless the user
explicitly asks for that implementation.

PASS / FAIL / BLOCKED are decided by the end user. The agent reports execution
status, raw test results, evidence, warnings, and reasons for not executing.

## Automation classification

Use only these four classifications:

### FULLY AUTOMATABLE

The test is read-only or otherwise low-risk, its dependencies and target are
known, and an agent can safely run it after normal checks.

### REQUIRES PACKAGE / USER CONFIRMATION

The test can technically be run, but requires a package, vendor tool, license,
operator-provided parameter, target confirmation, or explicit approval. This
includes stress, reboot, reset, cycle, firmware flash/update, BIOS/BMC/NIC
changes, destructive storage operations, and actions that may affect users,
jobs, the OS, or management connectivity.

### MANUAL ONLY

The test itself requires a physical human action with no reasonable automated
substitute, such as cable insertion/removal, component replacement, physical
inspection, or visual LED inspection.

### BLOCKED

The purpose, target, hardware identity, dependency, command semantics, success
criteria, or recovery path cannot be understood safely. GPT must not guess.

## Required analysis for every testcase

For each testcase, answer these questions:

1. What is the actual test purpose?
2. Does the proposed command really test that purpose?
3. Does the command match the original duration, target, worker count, and
   required path/tool?
4. Which packages, vendor tools, licenses, images, peers, or parameters are
   required?
5. Does the test read data, change state, interrupt service, write data, or
   destroy data?
6. Could it affect the OS, active users, active jobs, management connection, or
   other tests?
7. What evidence should the agent collect for the end user?
8. What must be confirmed before execution, and what conditions require
   BLOCKED?

## Mandatory safety rules

### Storage and destructive I/O

- Never guess a storage target.
- Never assume `/dev/sda`, `/dev/sdb`, `/dev/nvme0n1`, or any device number is
  safe.
- FIO, `dd`, format, filesystem, wipe, and destructive GDS tests require target
  identity and safety validation by the receiving agent.
- OS, boot, EFI, mounted, active filesystem, swap, LVM, RAID/member, device
  mapper, or unknown devices must never be used as destructive targets.
- If target safety cannot be proven, classify as `BLOCKED` or require explicit
  user confirmation according to the unresolved condition.

### GPU

- Do not assume GPU index or PCIe address mapping is stable.
- The receiving agent must verify GPU count, UUID, PCIe enumeration, topology,
  driver/CUDA/FW versions, active processes, XID/dmesg evidence, and BMC events
  when relevant.

### Firmware, BIOS, BMC, CPLD, NIC, SSD, and related updates

- Require hardware identity, device ID, PN/SKU where available, current
  firmware, target firmware, compatibility, upgrade/downgrade intent, required
  reset/reboot/power cycle, and recovery path.
- If image-to-hardware identity or recovery cannot be confirmed, classify as
  `BLOCKED` or `REQUIRES PACKAGE / USER CONFIRMATION`; never guess.

### Reboot, reset, power, and cycle actions

- Reboot, reset, AC/DC cycle, BMC power action, and PDU/Rack Manager actions
  require explicit user confirmation before execution.
- The receiving agent must check active jobs/users/tests, capture before/after
  evidence, use timeout/reconnect/retry behavior, and verify recovery.

### Network

- Do not assume an interface, route, VLAN, bond, or NIC is non-management.
- Any action that may disconnect the agent requires management-path validation
  and an out-of-band recovery path; otherwise it must stop or be `BLOCKED`.

### BMC and logs

- Do not change credentials, clear important logs, or reset the BMC without a
  backup/evidence plan, approval, timeout, reconnect, verification, and recovery
  strategy.
- Do not use `dmesg -c` merely to create a baseline; preserve existing evidence.

## Output format for each reviewed testcase

Formal testcase review output is written in English so it can be shown to and
copied for an AI agent. The conversation and discussion with the user may be in
Chinese.

```text
Test Code
Test Name

Automation Classification

Purpose

Required Package / Dependency

Test Command

User Confirmation Required

Risk Notes

Expected Evidence

Blocked Conditions

DeepSeek Original Review

GPT Second Review Findings

End-user decides PASS / FAIL / BLOCKED.
```

The `Test Command` is the concise command or procedure target from the
testcase, for example:

```bash
stress-ng --cpu 225 -t 8h
```

It does not grant permission to run. The receiving agent is responsible for
turning it into a safe execution plan.

## Pilot decisions recorded

### Wistron-HW-00082-V004

- Test: CPU Stress - Stress-NG
- Classification: `REQUIRES PACKAGE / USER CONFIRMATION`
- Test command: `stress-ng --cpu 225 -t 8h`
- Main findings: DeepSeek changed the original 8-hour/225-worker intent to
  `--cpu 0 --timeout 600s`; the duration and worker behavior do not match.
- The agent must confirm package availability, worker suitability, dedicated DUT
  status, active workloads/users, thermal/power risk, and explicit approval.

### Wistron-HW-00090-V004

- Test: Memory Stress - Stress-NG
- Classification: `REQUIRES PACKAGE / USER CONFIRMATION`
- Test command: `stress-ng -m 15 --vm 9 --vm-bytes 90% -t 8h`
- Main findings: DeepSeek supplied prose rather than a real test command; the
  memory worker/percentage combination requires safety confirmation; “badblock”
  is ambiguous for a memory test.
- If the memory criteria or command semantics cannot be clarified safely, the
  testcase is `BLOCKED`.

## Review process

1. Review the two pilot cases and confirm this contract.
2. Review the remaining cases in bounded batches.
3. Keep all GPT output in a separate overlay keyed by `code`.
4. After each batch, verify that the original XLSX and `data/tests.json` have no
   diff.
5. Do not begin full-library modification or System Manager integration until
   the user approves the pilot quality and schema.
