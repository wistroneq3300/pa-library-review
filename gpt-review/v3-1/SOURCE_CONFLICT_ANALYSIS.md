# V3.1 Source Conflict Analysis

## Result

- V3 records with `SOURCE_CONFLICT`: **80**
- V3.1 records with `SOURCE_CONFLICT`: **58**
- Conflicts removed after source-specific review: **22**
- New conflicts introduced: **0**

The 22 removals are not blanket conflict suppression. Each was re-read against the XLSX. The conflicting value was either Machine Time/Attended Time planning metadata or a non-normative field, while the Procedure/Criteria retained the Master test requirement.

## Removed conflicts

| Seq | Source key | V3 conflict removed in V3.1 |
|---:|---|---|
| 5 | `Functionality\|201\|Wistron-HW-00210-V002` | Scheduling metadata no longer overrides the functional procedure. |
| 10 | `Reliability\|4\|Wistron-System RAS-00378-V003` | Timing metadata is separated from the BIOS/injection scope; topology and stimulus gates remain. |
| 18 | `Stability\|9\|Wistron-Margin-00008-V002` | 12-hour Procedure versus 240-minute Machine Time; 12 hours remains Master. |
| 96 | `Reliability\|26\|Wistron-System RAS-00746-V003` | Planning time is not treated as a second normative RAS requirement. |
| 97 | `Reliability\|33\|Wistron-System RAS-00753-V003` | Same correction after independent case review; case-specific RAS inputs remain. |
| 108 | `Reliability\|114\|Wistron-GPU RAS-00835-V004` | Machine Time removed from normative conflict analysis. |
| 110 | `Reliability\|127\|Wistron-HW Robust-00005-V002` | Schedule estimate separated from the source procedure. |
| 123 | `Performance\|9\|Wistron-Performance Storage-00008-V004` | Machine Time-only conflict removed; safe file/target and benchmark inputs remain. |
| 124 | `Performance\|12\|Wistron-Performance Storage-00015-V004` | Machine Time-only conflict removed; destructive-data protections remain. |
| 126 | `Performance\|18\|Wistron-Performance Networking-00033-V004` | Planning duration separated from the project-selected network plan. |
| 129 | `Performance\|26\|Wistron-Performance GPU-00042-V003` | Planning time no longer conflicts with the benchmark requirement. |
| 131 | `Performance\|32\|Wistron-Performance GPU-00048-V003` | Same rule, with benchmark-specific model/scenario evidence retained. |
| 155 | `Compatibility\|234\|Wistron-AMD GPU-00227-V002` | Timing metadata removed; lifecycle/count decision remains explicit. |
| 170 | `Stability\|2\|Wistron-Margin-00001-V003` | 12-hour Procedure versus 240-minute Machine Time. |
| 171 | `Stability\|6\|Wistron-Margin-00005-V002` | 12-hour storage stress versus 240-minute Machine Time. |
| 172 | `Stability\|10\|Wistron-Margin-00009-V002` | >12-hour BMC stress versus 7200-minute planning value. |
| 173 | `Stability\|18\|Wistron-Margin-00017-V002` | 12-hour PCIe/network stress versus 240-minute Machine Time. |
| 174 | `Stability\|25\|Wistron-Margin-00024-V002` | 12-hour GPU burn versus 240-minute Machine Time. |
| 176 | `Stability\|32\|Wistron-Margin-00031-V003` | 24-hour idle soak versus 720-minute Machine Time. |
| 177 | `Stability\|40\|Wistron-Margin-00039-V002` | 12-hour DIMM stress versus 240-minute Machine Time. |
| 179 | `Stability\|53\|Wistron-Margin-00052-V002` | 12-hour USB stress versus 48-minute Machine Time. |
| 180 | `Stability\|54\|Wistron-Margin-00053-V002` | 12-hour storage stress versus 240-minute Machine Time. |

## Genuine conflicts retained

- Seq 54: BMC Get/write and CPU/chassis enforcement semantics conflict.
- Seq 122: storage workload requires QD1 and QD64 in different normative fields.
- Seq 143: source asks both 70/30 mixed I/O and randwrite.
- Seq 183: title requires 500 reboots while Procedure defines 12 hours; both are normative, not Machine Time.
- Seq 185: Ethernet label and `ib_read write` wording do not select Ethernet, RoCE or InfiniBand or a valid endpoint command.
- Seq 190/191: WAT commands mix AC/DC tokens and omit the named i2cPoll/cpldPoll selector.
- Seq 197: BIOS downgrade item still says to start an upgrade; vendor downgrade policy is required.

A project engineer may resolve a retained conflict for one run. That resolution is stored as project scope and does not silently rewrite the Master source.
