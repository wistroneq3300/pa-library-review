# BLOCKED and SOURCE_CONFLICT Final Audit

## Result

- BLOCKED: **22 before, 22 after**.
- SOURCE_CONFLICT: **58 before, 48 after**.
- No BLOCKED case was released to improve a metric.
- Ten SOURCE_CONFLICT flags were corrected because the actual condition is
  unclear intent, missing private semantics, missing project bound, or absent
  external specification—not two contradictory source requirements.

## All BLOCKED cases

| Seq | Category | Technical basis |
|---:|---|---|
| 19 | A | Intel SSV procedure is absent; LTSSM, lane-margin, or combined intent cannot be selected. |
| 45 | B | Mount-only and auto-installer behavior are incompatible acceptance scopes. |
| 54 | B | Get/write, CPU/chassis and enforcement semantics conflict. |
| 62 | B | Three reset commands target materially different reset domains. |
| 64 | B | Get Sensor Type conflicts with Set/Get mutation. |
| 67 | B | GET discovery conflicts with POST InsertMedia. |
| 73 | A | xGMI title has no target, action or criterion. |
| 79 | A | Missing I2C BMC_BD specification contains the complete contract. |
| 80 | A/H | FIO_BD has no identifiable storage target or operation. |
| 92 | A | Cable could mean fit, continuity, signal or enumeration. |
| 103 | A/H | Processor CE injection has no target, stimulus or acceptance. |
| 104 | A/H | NVIDIA host-memory UENF topology/containment is undefined. |
| 105 | A/H | Bad-TLP generator and PCIe locus are undefined. |
| 106 | A/H | Replay-rollover generator and expected retrain are undefined. |
| 107 | A/H | Surprise Down locus, containment and recovery are undefined. |
| 162 | A | NVTOP CPU Monitor does not identify a metric or display field. |
| 163 | A | GPU power domain/statistic, fixture and sampling contract are absent. |
| 186 | A/F | AMD Memeye external SPEC contains the entire unknown activity. |
| 190 | B/F/H | WAT mixes AC/DC tokens, omits i2cPoll selection and leaves safe bus scope unresolved. |
| 191 | B/F/H | WAT mixes AC/DC tokens, omits cpldPoll mapping and leaves CPLD scope unresolved. |
| 199 | A | PDB_BD is only a label and external-spec pointer. |
| 200 | A/H | E1S_BD1 does not define storage target ownership or operation. |

Categories: A unclear intent; B contradictory source requirements; F private
tool/specification dependency; H genuine safety block.

## Corrected SOURCE_CONFLICT flags

| Seq | Before | After and reason |
|---:|---|---|
| 19 | SOURCE_CONFLICT | `UNCLEAR_TEST_INTENT`; absent delegated procedure does not contradict another requirement. |
| 69 | SOURCE_CONFLICT | Project method choice; peltier or approved heatsink method is selected under one bounded thermal contract. |
| 162 | SOURCE_CONFLICT | `UNCLEAR_TEST_INTENT`; a TBD metric is missing, not contradictory. |
| 175 | SOURCE_CONFLICT | Missing loop/duration is a project input; upload/remove intent is coherent. |
| 186 | SOURCE_CONFLICT | Missing entire vendor SPEC; retain BLOCKED but do not claim two source statements disagree. |
| 187 | SOURCE_CONFLICT | Private WAT token mapping is readiness; DC reboot/OS-ping intent is coherent. |
| 188 | SOURCE_CONFLICT | Private pciePoll mapping is readiness; no contradictory power mode is present. |
| 189 | SOURCE_CONFLICT | Private usbPoll mapping is readiness; no contradictory source operation is present. |
| 199 | SOURCE_CONFLICT | Missing external SPEC/intent; retain BLOCKED without false contradiction. |
| 200 | SOURCE_CONFLICT | Missing external SPEC/storage action; retain BLOCKED and all storage prohibitions. |

The remaining 48 flags were individually reviewed and retained for concrete
conflicts such as command aliases, vendor/workload identity, UI/command scope,
RAS locus/evidence branch, MLPerf copied criteria, QD/I/O-mix, power mode, or
normative count-versus-duration. Full case conclusions are in `AUDIT_RECORDS`.

## Existing report defect

The V3.1 `BLOCKED_RECLASSIFICATION.md` description for sequence 19 incorrectly
describes a GDS/non-GDS case. Sequence 19 is LTSSM/Intel SSV. The historical
report is not overwritten; this Final Audit document is the correction overlay.

