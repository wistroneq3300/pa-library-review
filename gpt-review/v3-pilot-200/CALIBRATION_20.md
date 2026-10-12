# V3 Calibration Review — First 20 Cases

Status: `CALIBRATION PASSED; CONTINUATION TO CASE 21 APPROVED`

Date: 2026-10-13

## Scope and integrity

- Reviewed records: 20 of 20 fixed calibration cases.
- Unique source keys: 20.
- Unique case variant IDs: 20.
- Sheet coverage: Functionality 8, Reliability 2, Performance 3,
  Compatibility 3, Stability 2, and `(No Main Function)` 2.
- Immutable XLSX, `tests.json`, and GPT V2 hashes match the baseline.
- The mechanical validator found no illegal classifications/outcomes/readiness
  labels, missing required record sections, exact duplicate change reasons, or
  objective-improvement pairs above the 0.85 similarity audit threshold.
- Mechanical integrity does not constitute semantic or hardware validation.

## Calibration distribution

| Measure | Distribution |
| --- | --- |
| V2 automation classification, normalized | BLOCKED 6; FULLY AUTOMATABLE 2; MANUAL ONLY 3; REQUIRES PACKAGE / USER CONFIRMATION 9 |
| V3 automation classification | BLOCKED 1; FULLY AUTOMATABLE 1; MANUAL ONLY 1; REQUIRES PACKAGE / USER CONFIRMATION 17 |
| V3 review outcome | IMPROVED 5; RECLASSIFIED 7; REWRITE_REQUIRED 2; SOURCE_CONFLICT 5; NEED_ENGINEER_DECISION 1; KEEP 0 |

The calibration set intentionally over-represents known boundary and defect
cases. These counts are not an improvement-rate estimate for the 3,112-case
library.

## Case-by-case calibration result

| Seq. | Source key | V3 outcome | V3 classification | Calibration-specific result |
| ---: | --- | --- | --- | --- |
| 1 | `Functionality\|29\|Wistron-HW-00032-V004` | RECLASSIFIED | REQUIRES PACKAGE / USER CONFIRMATION | Treats CRPS offset specification/decoder as provisionable inputs rather than permanent inability. |
| 2 | `Functionality\|67\|Wistron-HW-00070-V004` | RECLASSIFIED | REQUIRES PACKAGE / USER CONFIRMATION | Preserves the five N/N-1 firmware cycles and requires image/command/recovery approval. |
| 3 | `Functionality\|150\|Wistron-HW-00153-V002` | SOURCE_CONFLICT | REQUIRES PACKAGE / USER CONFIRMATION | Preserves the OS-install versus TPM procedure/criteria conflict instead of inventing one coherent test. |
| 4 | `Functionality\|198\|Wistron-HW-00207-V002` | RECLASSIFIED | MANUAL ONLY | Identifies the actual physical serial path and treats serial parameters as missing inputs. |
| 5 | `Functionality\|201\|Wistron-HW-00210-V002` | SOURCE_CONFLICT | REQUIRES PACKAGE / USER CONFIRMATION | Preserves BIOS-plus-OS versus OS-only acceptance conflict and requires per-port evidence. |
| 6 | `Functionality\|79\|Wistron-HW-00082-V004` | IMPROVED | REQUIRES PACKAGE / USER CONFIRMATION | Keeps exactly 225 CPU workers for eight hours and rejects the 600-second replacement. |
| 7 | `Functionality\|87\|Wistron-HW-00090-V004` | REWRITE_REQUIRED | REQUIRES PACKAGE / USER CONFIRMATION | Official stress-ng semantics prove `-m 15` and `--vm 9` are conflicting aliases; owner must choose one. |
| 8 | `Functionality\|2260\|Wistron-BMC-00848-V003` | RECLASSIFIED | REQUIRES PACKAGE / USER CONFIRMATION | Restores mandatory BIOS/WebUI observations that V2 had reduced to supplemental evidence. |
| 9 | `Reliability\|2\|Wistron-System RAS-00374-V003` | NEED_ENGINEER_DECISION | FULLY AUTOMATABLE | Separates ACPI table presence, kernel recognition, and end-to-end RAS behavior; requires a platform table matrix. |
| 10 | `Reliability\|4\|Wistron-System RAS-00378-V003` | RECLASSIFIED | REQUIRES PACKAGE / USER CONFIRMATION | Represents manual BIOS/injection plus automated host/BMC correlation and exposes the missing injection step. |
| 11 | `Performance\|3\|Wistron-Performance CPU-00002-V003` | SOURCE_CONFLICT | REQUIRES PACKAGE / USER CONFIRMATION | Prevents AMD CCX scripts from becoming a Common/Intel path and requires a matched HPL baseline. |
| 12 | `Performance\|4\|Wistron-Performance DIMM-00003-V004` | IMPROVED | REQUIRES PACKAGE / USER CONFIRMATION | Defines the 9.61-GiB footprint, thread/NUMA scope and comparable STREAM reference; rejects per-core labeling. |
| 13 | `Performance\|15\|Wistron-Performance Networking-00030-V004` | REWRITE_REQUIRED | REQUIRES PACKAGE / USER CONFIRMATION | Corrects `ib_write_bw -t 300` (TX depth) to version-validated duration mode (`-D 300` upstream). |
| 14 | `Compatibility\|76\|Wistron-Storage-00059-V004` | IMPROVED | REQUIRES PACKAGE / USER CONFIRMATION | Adds fio per-clone 4-GiB semantics, stable target/range review, per-drive traceability and protected evidence storage. |
| 15 | `Compatibility\|251\|Wistron-NV GPU-00244-V002` | IMPROVED | REQUIRES PACKAGE / USER CONFIRMATION | Removes an invented NVDiag module assumption and requires complete UUID/BDF/upstream-path evidence. |
| 16 | `Compatibility\|257\|Wistron-NV GPU-00250-V002` | IMPROVED | REQUIRES PACKAGE / USER CONFIRMATION | Shows that identical 144-link totals can represent different H100/H200 and B200/B300 NVSwitch graphs. |
| 17 | `Stability\|68\|Wistron-Long Term Stress-00067-V004` | RECLASSIFIED | REQUIRES PACKAGE / USER CONFIRMATION | Treats qualified PDU setup plus automated 1000-cycle validation as hybrid and replaces device count with stable identities. |
| 18 | `Stability\|9\|Wistron-Margin-00008-V002` | SOURCE_CONFLICT | REQUIRES PACKAGE / USER CONFIRMATION | Finds the 12-hour versus 240-minute conflict and separates 5 V/3.3 V DC margin from AC input. |
| 19 | `(No Main Function)\|3\|Wistron---00356-V002` | SOURCE_CONFLICT | BLOCKED | Retains a genuine blocker: PCIe lane margin and LTSSM sequence validation are materially different tests with no disambiguating source. |
| 20 | `(No Main Function)\|7\|Wistron---00842-V003` | RECLASSIFIED | REQUIRES PACKAGE / USER CONFIRMATION | Normalizes the class, preserves WebUI downgrade scope and rejects a fabricated universal Redfish upload action. |

## Required calibration questions

### A. Is V3 clearer than V2?

Yes for the calibration set. Each contract now separates original purpose,
target, missing inputs, safe collection, prohibited actions, closure proof and
completion. Material examples include stress-ng alias resolution, perftest
duration correction, fio clone/range semantics and the generation-specific
144-link graph.

### B. Does it distinguish missing data from genuine BLOCKED?

Yes. Five of six V2 BLOCKED cases became provisionable hybrid/manual
classifications without relaxing execution gates. The remaining BLOCKED case
is retained because the source cannot distinguish LTSSM state validation from
lane-margin measurement, not merely because an Intel package is unavailable.

### C. Did V3 introduce a new safety vulnerability?

No safety regression was found in the source/contract comparison. Reclassified
high-risk cases still prohibit execution until target, approval, stop and
recovery gates close. This is a review conclusion, not a DUT safety test.

### D. Did V3 change original test intent?

No silent intent change was accepted. Source conflicts remain unresolved and
explicit. WebUI, BIOS, per-port, all-device, 12-hour, eight-hour, 1000-cycle,
five-cycle and 144-link requirements are preserved where present.

### E. Is the testcase contract too long for an execution agent?

The agent-facing `revision_candidate` is separated from the larger audit
record and is structured into thirteen bounded fields. High-risk firmware,
power, injection and destructive-storage cases remain deliberately detailed.
The isolated understanding run is the gate for whether any contract must be
shortened or clarified.

### F. Is there large-scale repetition, template text or empty rationale?

The mechanical audit found no exact duplicate `reason_for_change` and no pair
of objective-improvement fields above 0.85 similarity. Each record cites its
own command, duration, target, conflict or acceptance fact. Semantic duplicate
detection remains part of later 20-case checkpoints.

### G. Are the changes technical improvements or English polishing?

They are technical: two wrong command semantics were corrected; two timing or
command-source conflicts were exposed; several unsafe target/topology/count
assumptions were replaced with stable mappings; and hybrid/manual/BLOCKED
boundaries were changed with case-specific evidence. No case is marked
IMPROVED solely for prose style.

## Draft-to-calibrated V3 changes

The first 20 cases added explicit rules for:

1. preserving a named access path such as WebUI, BIOS or BMC web;
2. validating CLI aliases and versioned option semantics;
3. using stable identities and topology graphs instead of counts;
4. resolving clone address ranges, multi-target scheduling and evidence paths;
5. binding benchmark results to comparable profiles and references;
6. treating Procedure versus Machine Time mismatches as source conflicts;
7. recognizing programmable-fixture/manual-setup plus automated-evidence
   workflows as hybrid; and
8. retaining BLOCKED when plausible source labels denote materially different
   tests rather than merely missing an obtainable SOP.

These changes are incorporated in `REVIEW_WORKFLOW_LOGIC_V3.md` and apply only
when the individual testcase facts invoke them.

## Continuation gate

The semantic/source regression and mechanical portions of calibration pass.
Contract-only isolated validation recovered the intended meaning for all 20
contracts: 16 were clear and four correctly preserved unresolved source
ambiguities without inventing an executable answer. No document-caused,
platform-handoff, or model-planning failure required repair. Validation used
isolated same-model-family reviewers and is not independent-model or hardware
validation. Continuation to case 21 is approved.
