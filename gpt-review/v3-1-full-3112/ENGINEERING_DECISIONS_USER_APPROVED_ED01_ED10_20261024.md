# User Engineering Decisions ED-01 to ED-10 (2026-10-24)

Status: USER DECISIONS RECORDED; IMPLEMENTATION / INDEPENDENT QA PENDING.
Scope: 10 selected case-level questions in the 942-item pending queue.
These decisions do not authorize DUT execution, automatic reclassification, modification of the protected Master XLSX/JSON, or merge.

| Decision | Source Key | User selection | Rule / scope |
|---|---|---|---|
| ED-01 | Compatibility|130|Wistron-OS-00113-V003 | A | RAID0 objective governs the review-layer procedure. Do not execute RAID rebuild operations on RAID0. Preserve the original source. |
| ED-02 | Compatibility|139|Wistron-AMD GPU-00122-V002 | A | Preserve distinct source rows using Source Key + Variant ID; never collapse separate coverage just because the code matches. |
| ED-03 | Functionality|1001|Wistron-BMC-00291-V003 | A | Draft standard-based command contracts with evidence; leave target-specific/OEM parameters pending and prohibit execution until verified. Do not invent vendor payloads. |
| ED-04 | Compatibility|3|Wistron-Storage-00010-V003 | A | Draft a 50/50 mixed read/write FIO plan matching the test objective; destructive target, authorization and safety gates remain mandatory. |
| ED-05 | Compatibility|51|Wistron-Networking-00034-V003 | C | Treat Ethernet and InfiniBand as distinct subtest coverage, with separate interfaces, profiles, evidence and acceptance. |
| ED-06 | Stability|71|Wistron-Long Term Stress-00070-V003 | C | Cold/full-power and warm OS reboot are distinct test mechanisms and cannot substitute for one another. |
| ED-07 | Functionality|1436|Wistron-BIOS-00004-V003 | B | User selects a complete BIOS flash with before/after version verification for this row. This broadens mutation scope and requires an approved image, exact target, activation, safety gate and recovery; cross-check distinct duplicate-code variant before implementation. |
| ED-08 | Functionality|2237|Wistron-BMC Sanity-00019-V001 | C | Cover both BMC WebUI authentication/session and KVM console persistence; API evidence does not substitute for required visual WebUI/KVM evidence. |
| ED-09 | Compatibility|100|Wistron-Storage-00083-V003 | C | Separate Present LED from genuine RAID Rebuild LED coverage. Physical LED observation remains human-confirmed; no simulated Locate substitute. |
| ED-10 | Functionality|2273|Wistron-HW-00475-V002 | A | Retain MLPerf Inference v5.0 RetinaNet Offline as the intended case; correct copied BERT/training text in review overlay, not Master. |

## Application guardrails
1. Generalize only safe decision principles; source-specific choices remain case-scoped.
2. Before updating reusable review logic, compare every decision against original XLSX rows, prior approved ED records and locked audit policy.
3. Preserve protected Master XLSX, formal JSON, prior review records, invalidated runs and decision history.
4. Re-review each of the 942 Source Keys individually from its original XLSX row; no keyword/batch reclassification, template-generated verdict or inferred next identity.
5. Reconcile the 927 source conflicts and 214 blocked cases without double counting or silently waiving safety.
6. Report changed / unchanged / unresolved / blocked counts, case-level evidence, Validator and independent QA results. Do not claim QA ACCEPTED before independent QA.
7. No merge or DUT execution is authorized by this decision record.
