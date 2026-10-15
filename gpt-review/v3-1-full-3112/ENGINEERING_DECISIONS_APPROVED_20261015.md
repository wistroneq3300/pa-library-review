# V3.1 Engineering Decisions Approved 2026-10-15

Authority: user-provided engineering rulings for the shared 3,112-case Server /
GPU Server SIT Master Test Case Library.

## General rules

- **ED-33 — Immutable Master Source.** Preserve the exact source key, variant,
  Procedure, Criteria, Command, source hash, history and evidence. Corrections
  are additive V3.1 recommendations only.
- **ED-34 — Project-selected tools and bounded overrides.** Preserve a source-
  named tool. A project may use an engineer-approved AFULnx, AFUEFI, BMC Flash,
  Redfish UpdateService, vendor tool or later approved method, but must record
  original/actual tools, reason, approval, equivalence and uncovered original
  method. An absent tool-list entry is not a permanent blocker.
- **ED-35 — No silent coverage reduction.** A read-only check may be partial or
  preflight evidence; it never completes a source-required flash, setting write,
  compliance-mode change or other functional action.
- **ED-36 — Review/readiness/execution/verdict separation.** Distinguish review
  completion, engineering recommendation, execution-readiness inputs, pending
  engineering decisions, test execution and final PASS/FAIL. Missing image,
  version, SPEC, Expected, address, package, parameter or approved environment
  is normally readiness, not permanent `BLOCKED`.
- **ED-37 — BIOS writable/read-only behavior.** Writable fields use an approved
  value, Save, any required reboot, readback and restoration. Read-only fields
  are compared with Project SPEC or another authority and retain evidence;
  read-only is neither automatic FAIL nor equivalent to write coverage.
- **ED-38 — Engineer owns DUT verdict.** Static Review PASS never means DUT
  PASS. Do not auto-retry or perform unapproved flash, BIOS change, power,
  destructive storage or credential mutation.

## Case-bound rulings

- **ED-39 — BIOS 00007–00010.** Preserve the conflicting AFULnx/AFUEFI and
  same-version text. The functional intents are upgrade, downgrade, same-version
  reflash and upgrade/downgrade cycling. Project SPEC selects the approved tool.
  BIOS 00010 also binds what "100" counts, image order, per-round evidence,
  stop criteria and recovery.
- **ED-40 — BIOS 00014.** Corrupt-image rejection and downgrade/anti-rollback
  rejection are separate checkpoints. The project selects one or both; one
  rejection cannot prove both.
- **ED-41 — BIOS 00042.** Keep one Master row but independently verify Hot-Plug
  Enabled/Disabled, actual hot-plug behavior, SR-IOV VF creation/enumeration,
  guest evidence and per-function Expected results.
- **ED-42 — BIOS 00054.** Test User and Administrator Password separately,
  including set, authentication, privilege distinction, clear and recovery.
- **ED-43 — BIOS 00055.** Use a project Secure Boot matrix covering Enabled /
  Disabled, signed / unsigned OS, PK, MOK, approved image and expected boot.
  Do not change keys or MOK without approval.
- **ED-44 — BIOS 00058.** Quiet Boot and Boot Device may remain one testcase,
  with distinct presentation, enumeration, order configuration and actual boot
  checkpoints. Quiet Boot semantics come from Project SPEC, not a universal
  boot-time or initialization assumption.
- **ED-45 — BIOS 00064/00066/00068/00071.** Discard proves the previously saved
  value remains after an unsaved edit is discarded. Restore User Defaults proves
  the approved user-default profile was actually recalled; Save alone is not
  acceptance.
- **ED-46 — BIOS 00096/00097/00131/00132.** Separate image selection from
  update. Update evidence includes pre-version, approved flash, required
  activation/reset, BIOS-homepage target-version readback and normal boot.
  Version equality alone does not prove every firmware region.
- **ED-47 — BIOS 00099/00102/00104/00134/00137/00139.** Viewer scope is
  read-only first: page entry, log visibility, fields, expected records and UI /
  navigation. Unrelated settings, Load Default or log clearing are not evidence.
- **ED-48 — BIOS 00120.** Follow actual platform capability: bounded change /
  Save / reboot / readback / restore when writable; authoritative value
  comparison when read-only. Preserve the coverage difference.
- **ED-49 — BIOS 00125.** Retain the source-required PCIe Compliance Mode
  functional change. Project SPEC binds port, setting, Expected, safe exit and
  restoration. Default/read-only inspection is partial only.
- **ED-50 — BIOS 00144/00224/00295/00296/00326.** Correct recommendations using
  the applicable SMBIOS standard and Vendor SPEC for AMD Secure Processor
  version, cache SRAM fields, Reserved fields, Type 32 versus Type 17 Boot
  Status and the Type 38 byte. Never guess offset/value/vendor fields or accept
  an empty grep as PASS.
- **ED-51 — BIOS 00376.** Keep `ENGINEER DECISION PENDING`. Do not choose TSEG
  range versus SmiHandler4 trace and do not flash debug BIOS or perform an
  unapproved register operation.
- **ED-52 — BMC 00003/00004/00008/00010/00012.** Preserve title targets BMC,
  FPGA, HIB-CPLD and DCSCM-CPLD. Project SPEC selects the approved update path.
  Record component, versions, image, direction, host state, activation/reset,
  tool/API, criteria and recovery. Do not substitute CPLD with FPGA or recommend
  unapproved Redfish actions, fixed credentials or insecure TLS.

These rulings change review guidance and readiness/classification where noted;
they do not modify Master Source and do not assign a DUT PASS/FAIL verdict.
