# V3.1 Blocked Reclassification Analysis

## Result

- V3 BLOCKED: **22**
- V3.1 BLOCKED: **22**
- Reclassified out of BLOCKED: **0**
- Reclassified into BLOCKED: **0**

V3.1 does not reduce BLOCKED merely to improve a metric. Missing package, version, project Expected, device count or tool path is modeled as execution readiness when the test intent remains known. The 22 cases below remain BLOCKED because the intended operation, target, command semantics or mutually contradictory normative requirements cannot yet be executed safely.

## Retained BLOCKED cases

| Seq | Source key | Specific semantic blocker |
|---:|---|---|
| 19 | `(No Main Function)\|3\|Wistron---00356-V002` | GDS/non-GDS case lacks a safe target and a defined paired comparison method. |
| 45 | `Functionality\|746\|Wistron-BMC-00036-V002` | Source command/intent mismatch prevents a defensible BMC operation. |
| 54 | `Functionality\|988\|Wistron-BMC-00278-V002` | Get versus write, CPU versus chassis, and enforcement semantics conflict; only the Machine Time conflict was removed. |
| 62 | `Functionality\|1180\|Wistron-BMC-00470-V003` | Private command target/meaning is not established. |
| 64 | `Functionality\|1237\|Wistron-BMC-00527-V003` | Mutating BMC action cannot be selected from the contradictory source. |
| 67 | `Functionality\|1352\|Wistron-BMC-00642-V004` | Source does not define a safe, verifiable BMC test transaction. |
| 73 | `Functionality\|1577\|Wistron-BIOS-00423-V002` | BIOS item, procedure and acceptance do not establish one test intent. |
| 79 | `Functionality\|1800\|Wistron-HW-00002-V003` | Hardware operation is not recoverable from source text. |
| 80 | `Functionality\|1827\|Wistron-HW-00449-V002` | `FIO_BD` target, operation and acceptance are undefined; storage access is prohibited. |
| 92 | `Functionality\|2292\|Wistron-HW-00451-V002` | Board/operation semantics are missing. |
| 103 | `Reliability\|100\|Wistron-System RAS-00820-V002` | Processor correctable-error target and stimulus are absent. |
| 104 | `Reliability\|103\|Wistron-System RAS-00823-V003` | Memory UENF target, injection and containment are absent. |
| 105 | `Reliability\|106\|Wistron-System RAS-00826-V003` | Bad-TLP generator and PCIe hierarchy locus are absent. |
| 106 | `Reliability\|108\|Wistron-System RAS-00828-V003` | Replay/rollover stimulus and expected retrain behavior are absent. |
| 107 | `Reliability\|111\|Wistron-System RAS-00831-V002` | Surprise Down locus, DPC/AER containment and recovery are absent. |
| 162 | `Compatibility\|368\|Wistron-NV GPU-00361-V002` | “NVTOP CPU Monitor” does not identify the required field or function. |
| 163 | `Compatibility\|372\|Wistron-NV GPU-00365-V002` | GPU power domain/statistic, fixture and 10-minute acceptance are undefined. |
| 186 | `Stability\|78\|Wistron-Margin-00068-V002` | AMD Memeye meaning and referenced AMD specification are missing. |
| 190 | `Stability\|85\|Wistron-Long Term Stress-00016-V001` | AC/DC WAT tokens, i2cPoll mapping and safe HMC/BMC bus scope conflict. |
| 191 | `Stability\|88\|Wistron-Long Term Stress-00019-V001` | AC/DC WAT tokens, cpldPoll mapping and CPLD target scope conflict. |
| 199 | `(No Main Function)\|12\|Wistron---00007-V002` | `PDB_BD` is only a label; target and activity are unknown. |
| 200 | `(No Main Function)\|13\|Wistron---00014-V002` | `E1S_BD1` mapping and intended storage action are unknown. |

## Guardrail conclusion

Cases 76 and 194 demonstrate the opposite boundary: safe read-only Actual collection is automatable even when Expected is missing. Cases 80, 186, 199 and 200 remain BLOCKED because their test meaning is missing, not merely their Expected value. This distinction prevents both over-blocking and unsafe deblocking.
