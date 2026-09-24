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

## Mandatory one-testcase-at-a-time review

- The atomic review unit is exactly one source testcase row.
- Review each testcase independently from its own `Items`, `Procedure`,
  `Criteria`, and matching DeepSeek record before writing its overlay record.
- Do not review by batch, category, keyword rule, regex, copy-forward template,
  or generated classification table.
- Do not infer that similar-looking testcases have the same purpose, command,
  risk, package, or approval requirement.
- After each individual testcase, persist its record and checkpoint. If the
  next testcase is unclear, stop before reviewing it and ask the user.
- A scheduled run may process up to 200 sequentially unreviewed testcases per
  daily run, but every testcase must be independently reviewed and checkpointed
  before the next one is selected. The 200-case value is only a run quota; it
  must never become a batch template or grouped classification.
- During normal uninterrupted review, do not send per-testcase progress,
  checkpoint, commit, or push narration to the user. Continue silently.
- Notify the user only when a testcase requires a decision, reaches a hard
  safety blocker, or the run reaches its planned quota/completion point.

## Review integrity and auditability

- Review decisions must be made by reading the selected source row and its
  matching DeepSeek record, not by running a generator, classifier, range map,
  keyword rule, regex, copy-forward operation, or bulk-writing script.
- One completed testcase must produce exactly one new overlay record. The
  checkpoint `reviewed_count` must increase by exactly one and `next_key` must
  advance to the next source row.
- The per-testcase record must retain its sheet/source row, original testcase
  identity, DeepSeek comparison, and a testcase-specific GPT finding. A generic
  sentence copied across cases is not evidence of independent review.
- The commit for a normal testcase must contain only that testcase overlay,
  the progress checkpoint, and the current handoff/audit metadata. A commit
  that changes many unreviewed cases is invalid.
- Before continuing, verify the original XLSX and `data/tests.json` have no
  diff and verify that the overlay/reference counts increased by one only.
- If any invariant fails, mark the run invalid, stop, and do not present the
  generated records as reviewed. Preserve the invalid-run notice separately.
- The user can audit the work from `progress.json`, per-case `source_ref`, and
  the one-case Git commits without relying on chat narration.

## Self-detection and restart rule

Before and after every testcase, perform an internal integrity check:

1. Did I read this exact source row and its matching DeepSeek record?
2. Did I reason from this testcase's own purpose, procedure, criteria, target,
   and risks rather than from a category or neighboring case?
3. Is the GPT finding specific to this testcase, or could it be copied into a
   different testcase unchanged?
4. Did exactly one overlay record, one progress count, and one `next_key`
   advance occur?

If any answer is no, or if I notice an attempt to optimize for speed by using a
template, generator, mapping, or bulk write, I must immediately stop. The
affected run is invalid; its records must be removed from the active overlay,
the last valid checkpoint must be restored, and an invalid-run notice must be
preserved. Invalid records never count as reviewed.

The next run must restart from the last valid `next_key` and independently
re-review every testcase from the invalid run. The agent must notify the user
that it stopped because the integrity check failed.

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

## Mandatory pre-execution confirmation gate

Before every testcase execution, the agent must complete the applicable
read-only pre-checks and report the findings to the user. The report must state
the detected DUT facts, resolved parameters, required packages, risk level,
planned test command, and any stop conditions.

The agent must not start the test until the user explicitly replies `OK` after
reviewing that pre-execution summary. A request to run a testcase starts the
pre-check phase; it does not bypass this final confirmation gate.

The agent must ask targeted confirmation when a parameter is material or
uncertain, including CPU worker count, memory target, duration, storage target,
network interface, firmware image/version, reboot/reset/cycle count, or any
other setting that can materially affect the DUT.

If the user does not reply `OK`, replies ambiguously, or a pre-check finds a
hard safety blocker, the test must remain `NOT STARTED`. The agent must report
the evidence and the reason; it must not infer approval.

## Stop-and-ask persistence rule

Whenever review must stop for a user decision, the agent must first persist the
completed work, progress checkpoint, exact question, and the current handoff in
`gpt-review/`. It must verify that the original XLSX and `data/tests.json` have
no diff, then commit and push the checkpoint before asking the user.

Only generalizable review rules belong in this policy and the reusable skill.
Case-specific facts and unresolved questions belong in the per-testcase overlay
record and session handoff. The next run must resume from the persisted
single-testcase checkpoint. A run stops immediately on a user question or hard
safety blocker, otherwise it stops after approximately 200 completed individual
testcases.

The confirmation interaction is:

```text
Pre-check completed.

Detected facts:
<facts>

Resolved parameters:
<parameters>

Planned test command:
<test command>

Risks and warnings:
<risks>

Reply OK to start the test.
```

After an explicit `OK`, the agent may execute the approved command with the
approved parameters. If the command or parameters change, the agent must show a
new summary and wait for a new `OK`.

## Conversation and testcase language

- The agent's conversation, pre-check summary, confirmation request, execution
  report, warnings, and simulated/raw log explanation are in Chinese.
- The testcase content itself remains in English, including `Purpose`,
  `Required Package`, `Test Command`, `Risk Notes`, and `Expected Evidence`.
- Linux commands, package names, variables, paths, and raw logs remain
  unchanged.

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

### I2C and I3C ownership (Wistron project rule)

- For this Wistron GPU Server SIT library, I2C and I3C are treated as BMC or
  platform-management scope by default.
- This company-specific rule overrides the generic assumption that I3C may be
  host-side. A testcase may override it only when its supplied platform
  specification explicitly identifies a different ownership path.
- The review must still identify the BMC controller/bus, target address, BMC or
  OOB access path, vendor tool/specification, and expected output.
- A Linux `/sys/bus/i3c` listing alone does not prove that the required BMC
  target was reached or that the expected address/response is correct.

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

1. Read the current single-testcase checkpoint and select exactly its `next_key`.
2. Read that one source row and its matching DeepSeek record independently.
3. Write one English overlay record with the actual purpose, concise command or
   physical action, dependencies, safety gates, evidence, and classification.
4. Verify that the original XLSX and `data/tests.json` have no diff.
5. Commit and push that single-case checkpoint before selecting the next row.
6. Repeat steps 1-5 until a user question/hard blocker occurs or the run quota
   reaches approximately 200 completed individual testcases.
7. Never use the quota as evidence that individual review quality is sufficient.
