#!/usr/bin/env python3
"""Materialize the 200 hand-authored Final Audit judgments.

This utility does not infer a technical conclusion.  NOTES, classification
overrides, conflict dispositions, and blocker categories below are the
auditor's row-by-row decisions after reading the XLSX row and V2/V3/V3.1
history.  The code only copies immutable identity/evidence fields and writes
ten incrementally reviewable JSON arrays.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
V31 = ROOT / "gpt-review" / "v3-1" / "REVIEW_RECORDS"
V3 = ROOT / "gpt-review" / "v3-pilot-200" / "REVIEW_RECORDS"
OUT = ROOT / "gpt-review" / "v3-1-final-audit" / "AUDIT_RECORDS"

# One independently written audit conclusion per selected testcase.
NOTES = {
1: "The proprietary CRPS offset intent, no-guess PMBus boundary, decoded-byte evidence and engineer-owned comparison remain complete.",
2: "The five N/N-1 PSU transitions, WebUI HPM function, activation/power-cycle recovery and immutable first-failure evidence remain intact.",
3: "OS installation and TPM-setting revision remain distinct source intents; the project may choose scope without repairing the Master row.",
4: "Physical serial cabling and two-way terminal observation remain operator-owned, with approved electrical mode and harmless payload required.",
5: "Every physical USB port still requires BIOS and OS evidence tied to the moved device; a one-port lsusb sample cannot complete coverage.",
6: "The 225-worker eight-hour stress-ng Master profile, thermal/power evidence and project-override delta are retained without clearing logs.",
7: "The conflicting stress-ng VM-worker aliases remain unresolved; eight hours, 90 percent memory pressure and ECC/MCE evidence are preserved.",
8: "BIOS, in-band IPMI, OOB IPMI, WebUI and Redfish BMC-version observations remain a five-interface comparison, not an API-only shortcut.",
9: "Read-only ACPI table collection is automatable, while platform applicability is an input and inspection is not promoted to end-to-end RAS proof.",
10: "BIOS leaky-bucket configuration, exact DIMM target, bounded injection, log correlation and recovery remain manual/high-risk rather than tool-owned.",
11: "The AMD-only HPL procedure versus Intel/AMD criterion remains a real vendor-path conflict; numerical validation and comparable reference are required.",
12: "STREAM retains all four kernels, NTIMES=100, the large memory footprint, NUMA/thread placement and the Solution Validates gate.",
13: "The InfiniBand case retains every mapped port and a real 300-second run; perftest -D is duration and -t is not silently treated as seconds.",
14: "All-drive 12-hour fio coverage remains gated by stable target identity, write exclusions, exact clone semantics and per-drive 80-percent comparison.",
15: "NVIDIA FCT remains private and gated; every GPU UUID/BDF/link path and the narrowly approved SKU exception require complete evidence.",
16: "The 144-link requirement remains topology-specific rather than count-only, with platform generation and per-edge NVLink/NVSwitch mapping required.",
17: "The 1000-cycle AC campaign correctly uses qualified physical setup plus existing cycle control, per-attempt inventory and no hidden retry.",
18: "The 12-hour 40C/+5-percent GPU burn remains hybrid; the four-hour Machine Time value is planning metadata and all-GPU safety telemetry is retained.",
19: "The source only delegates an absent Intel SSV LTSSM procedure, so intent is unclear; it is not a GDS case and not a contradictory-source conflict.",
20: "BMC downgrade remains a WebUI preserve-all workflow with signed image, supported downgrade path, activation, management recovery and no generic endpoint.",
21: "Mechanical seating remains direct visual/tactile inspection against a BOM, with safe access and no forced reseat inferred from software inventory.",
22: "Adapter install/remove fit remains per-slot physical acceptance; software enumeration is supporting evidence and does not replace handling judgment.",
23: "The CRPS configBlockType read remains tied to the exact vendor/OCP table and raw byte decode, with no blind scan or write.",
24: "PWM-high LED response remains a direct visual criterion under an owner-defined safe stimulus; telemetry is corroboration only.",
25: "CPU installation retains socket, thermal, torque and BIOS-recognition evidence; supporting OS inventory cannot replace physical service proof.",
26: "The node fault LED requires a mapped approved event and direct observation; unspecified injection and inferred visual results remain prohibited.",
27: "Every jumper location remains a revision-specific, no-movement physical audit with board drawing identity and ESD controls.",
28: "TPM enabled state remains a BIOS-plus-OS hybrid check with OS-native evidence and an explicit prohibition on clear, initialize or security-state changes.",
29: "The approved fan/power fault and front error indicator remain operator-controlled, with bounded dwell, redundancy protection and correlated SEL evidence.",
30: "SF100 retains exactly 50 Program/Verify cycles on one identified ROM/image plus electrical checks, immutable failures, reinstall and boot recovery.",
31: "The lower-SVN AST1060 negative update remains gated by signed fixture and anti-rollback policy, with unchanged security/boot state as evidence.",
32: "The all-SSD 12-hour randrw profile remains destructive and target-gated; per-clone size, scheduling, health and reference calculation are preserved.",
33: "ConnectX-7 PCIe collection remains read-only and all-function, with endpoint/upstream link mapping and no throughput claim from negotiated width.",
34: "DCGM memtest retains every recipe GPU, full result matrix, persistence/service restoration and active-workload exclusion.",
35: "The BIOS Enter-key case remains a visual interactive check on a pre-approved harmless item, with no unsafe selection or save.",
36: "The administrator-password lifecycle retains ordered wrong attempts, correct authentication, clear operation, secret redaction and recovery limits.",
37: "Advanced USB BIOS settings retain explicit field coverage, persistence and platform-default restoration; Load Default is not globally authorized by inference.",
38: "AMD CRB Board remains hybrid because BIOS mutation is manual and inventory/health comparison is automated; dependencies and rollback stay project-bound.",
39: "Every SMBIOS Type 2 handle remains mapped to expected baseboard Product Name before and after one approved reboot.",
40: "Type 7 Cache Speed retains DMTF encoding semantics, Type4-to-Type7 mapping and before/after persistence without invented frequency conversion.",
41: "Type 7 System Cache Type remains a read-only per-handle enum comparison plus one separately approved reboot.",
42: "Type 17 Device Locator remains tied to the physical DIMM slot/population map before and after reboot, with no reseat implied.",
43: "Type 39 Cooling Device Handle remains a relationship decode to Type 27 or approved no-device value, not a cooling reconfiguration test.",
44: "GPUBB upgrade/downgrade retains WebUI firmware function, separate image/target identities, operator AC activation and complete recovery evidence.",
45: "Virtual media remains blocked because mount-only and auto-installer behavior are different acceptance scopes; no attach, boot or install is inferred.",
46: "SNMPv3 validation retains a finite vendor MIB/OID matrix, secure account policy, receiver values and cleanup without v1/v2c fallback.",
47: "TEMP_NVME_1-16 retains per-index mapping, bounded thermal stimulus, thresholds, SEL assert/deassert and protection recovery.",
48: "GPU1-8 power sensors retain exact GPU mapping, approved load envelope, per-sensor trace and power/thermal stop limits.",
49: "Shared and dedicated BMC LAN retains three physical cable states and bound-path identity probes so a surviving path cannot mask failure.",
50: "Callout validation retains every signed event-to-method pair and receiver-side receipt; a single destination cannot stand for the matrix.",
51: "The core acceptance is human-visible WebUI sensor presentation; both Dashboard and Server Health views for HSC1-10 are restored as mandatory evidence.",
52: "The System-panel case is a human-readable WebUI field/value verification; backend data can corroborate but cannot replace page observation.",
53: "The Chassis EROT case tests the rendered WebUI row/detail and correct component mapping, so formal observation remains manual.",
54: "Get versus cap-write, CPU versus chassis domain and non-demonstrative enforcement remain genuine conflicts; only Machine Time was removed.",
55: "Get AuthCode remains conditional on owner confirmation of the IPMI operation and protected vectors; no secret material may enter evidence.",
56: "Master Write-Read retains one finite owner-approved I2C endpoint/register transaction, exact bytes and a prohibition on scanning or guessed MUX access.",
57: "Get System Restart Cause remains a bounded read with byte-accurate decode; the agent must not create a reset event for this row.",
58: "Set SEL Time retains one approved write, explicit UTC/local model, offset verification and preservation of pre/write/read timing evidence.",
59: "Get Auxiliary Log Status remains a selector-bounded read requiring owner log-type/OEM mapping, not brute-force probing.",
60: "Get Sensor Hysteresis remains automatable after a finite sensor/support matrix; a TBD row does not authorize unbounded sensor scanning.",
61: "Get User Access retains a finite channel/User-ID policy matrix, redaction and read-only per-pair decode.",
62: "Three different chassis/BMC reset commands remain mutually incompatible source operations; no reset is safe before source correction.",
63: "SEL Allocation Info remains a nine-byte, support-bit-aware read with geometry decode and no SEL clear/write.",
64: "Get Sensor Type and Set/Get mutation remain distinct tests; the blocked row cannot be normalized into read-only evidence.",
65: "Set Power Limit retains correct little-endian encoding, domain/value approval, configuration-versus-enforcement separation and exact restoration.",
66: "DCMI Get Temperature Readings retains source instance 01h and byte-accurate response validation without threshold or policy changes.",
67: "GET action discovery and POST InsertMedia remain incompatible operations; discovery is safe but no POST is authorized while blocked.",
68: "HostEthernetInterfaces remains one read-only collection GET with discovered URI, collection invariants, protected authentication and no per-member invention.",
69: "Peltier or heatsink method is a project-selected safe fixture choice rather than contradictory source requirements; hard thermal stops remain mandatory.",
70: "GPU Name, Version and Power are tested on the BMC WebUI for every mapped GPU; host/API data cannot replace human page observation.",
71: "Leak-sensor validation remains hybrid with operator-applied bounded fluid stimulus, automated event timeline and verified dry/normal recovery.",
72: "SMBIOS Type 25 remains a raw five-field schedule decode and comparison, with no power-schedule mutation.",
73: "The title-only xGMI setting row lacks target, operation and acceptance; no generic xGMI documentation can safely define the test.",
74: "Quick-link labels, targets and rendered navigation are human-visible WebUI behavior; API discovery cannot complete the case.",
75: "The OEM BIOS/NVRAM title conflicts with opaque payload/duplicate-send semantics, so the command remains preserved but not executable.",
76: "Mapped CPU sensor Actual collection is fully automated and read-only; missing expected ranges delay the engineer verdict rather than capability.",
77: "The source acceptance surface is BIOS Setup; save/reboot/persistence remains an owner decision and OS data is corroboration only.",
78: "All three physical LED states remain direct visual acceptance with state-specific stimulus proof and recovery.",
79: "The absent I2C BMC_BD specification contains the entire target/operation contract; no scan, read, write or force access is safe.",
80: "FIO_BD lacks a target and operation, so storage access remains blocked rather than guessed from the word FIO.",
81: "NVS1-4 remains a substantive five-view cross-interface comparison; WebUI is one required phase, not the sole acceptance surface.",
82: "Type 29 probe decoding remains valid while unrelated Type 3 text is a real scope conflict; no electrical probing is introduced.",
83: "amdxio receiver-margin search remains private and all-link, with BDF/receiver map, thresholds and retrain/link-loss stops.",
84: "Motherboard sensors remain a four-view cross-interface comparison against a complete MB matrix; no one view substitutes for another.",
85: "AMD GPU thermal stress retains all-GPU mapping, full 40 minutes, stabilization, telemetry, limits and process cleanup.",
86: "NVQual NT.2 remains package/SOP/manifest-gated with full owner-defined target coverage and no invented metrics.",
87: "BMC VGA, DP, USB and serial acceptance remains connector-specific physical observation using approved fixtures.",
88: "CPUDVFS remains a private module with explicit CPU domains, versioned recipe, thresholds and no insecure SSH or log clearing.",
89: "KVM with USB hub remains a manual interaction/display case tied to the exact peripheral/VGA topology.",
90: "PDB sensors remain a command-plus-WebUI cross-interface test; read-only collection and mandatory page evidence are both retained.",
91: "Jumper function retains only recipe-specified positions, both power-on phases, physical state evidence and exact final restoration.",
92: "Cable alone does not select fit, continuity, signal or enumeration, so no physical manipulation or signal test is authorized.",
93: "Leaky-bucket RAS remains hybrid: manual BIOS/target setup and bounded injection with automated register, host and SEL correlation.",
94: "UPI CRC remains one bounded event per signed socket/port tuple with an OS-native evidence decision and front-panel negative criterion.",
95: "Memory-controller x4sddc remains mapped controller-to-slot, native-log specific and stopped on UCE, wrong target or reset.",
96: "Rank-plus1 remains distinct from adjacent RAS variants and retains x4 population, ADDDC/BIOS state, exact harasser and physical observations through inherited V3 detail.",
97: "OCP 1-N remains an uncorrectable non-fatal PCIe campaign with signed tuples, conditional LED/uEFI expectations and per-slot recovery.",
98: "Memory-slot 1-N retains fatal uncorrectable severity, selected BIOS/OS branch, validated injectable addresses and separate tool/report/reset gates.",
99: "PCIe slot 1-N retains correctable LCRC semantics and an unresolved endpoint/root-port locus decision; every BDF is freshly validated.",
100: "OCP fatal ACS coverage retains every slot, exact tuple, immediate reset and fresh post-boot BERT/CPER correlation.",
101: "WAFL correctable coverage retains both unique source locations, current link number, separate PASS/report gates and per-location recovery.",
102: "Fatal SWB coverage retains every DIMM by both voltage points, one recovered run per matrix cell and native fatal/reset evidence.",
103: "Processor correctable error remains blocked because target, stimulus and acceptance are absent; architecture discovery alone cannot define injection.",
104: "NVIDIA host-memory UENF remains blocked until topology, poison consumption/containment, reporter and recovery are explicitly defined.",
105: "Correctable Bad TLP remains blocked without generator, endpoint/root-port locus and AER ownership/acceptance.",
106: "Replay Number Rollover remains blocked without component-specific generator, counters and expected retrain limits.",
107: "Fatal Surprise Down remains blocked without endpoint/link, DPC/AER containment, host-state and recovery contract.",
108: "GPU injection enablement remains an enable-only OEM/reset workflow; no actual error injection is authorized and final state must be explicit.",
109: "Replay AC Parity versus ODECC/address/flag semantics remain contradictory until AMD confirms one event mapping; only one exact GPU may be targeted.",
110: "BMC I2C-6 validation retains adapter/MUX/expander/FRU endpoint mapping and before/after route evidence; one reply is insufficient.",
111: "The named BMC-HMC-EROT-FPGA2 chain requires path attribution across every segment, not acceptance of a lone 0x11 transaction.",
112: "BMC I2C-7 requires both boards' fan, leak and PDB endpoint coverage plus driver-ownership-safe access; forced generic reads remain prohibited.",
113: "Immediate GPIO shutdown retains independent off-state observation and separately approved power-on/recovery; graceful SSH shutdown is not substituted.",
114: "CPU temperature retains both exact EntityManager object paths and read-only D-Bus evidence; expected property matrix is still engineer supplied.",
115: "CPU swap remains physical socket/thermal work with firmware state, BIOS/OS recognition and repeated-POST recovery.",
116: "SMBus Hang Recovery retains the exact I3C HALT/GO target, configuration, bit transition and serial recovery; domain semantics must be owner resolved.",
117: "Single-device multi-bit CE retains exact logical-rank coordinates, clean baseline, IMC codes, counter increment and CScripts resume/restoration.",
118: "SDMA UE remains distinct from the source's UMC query and requires SDMA-specific fresh evidence plus approved reset/VRAM recovery.",
119: "UMC OD-ECC Replay retains exact sub-block/type/address reconciliation, zero baseline and fresh correctable counter/event evidence.",
120: "GFX poison handling retains ordered producer/consumer commands on one GPU and requires proof of consumption rather than injection success alone.",
121: "SPEC CPU2017 retains licensed suite, explicit benchmark/tuning scope, three valid iterations and metric-matched comparable reference.",
122: "The write benchmark retains QD1-versus-QD64 as a true conflict, exact 43200-second source profile and non-waivable target protections.",
123: "The randread case remains non-writing, QD1/one-job/512B for 43200 seconds; planning time does not shorten the Master run.",
124: "The M.2 randwrite case retains QD1/one-job/512B, endurance and alignment gates plus exact destructive target approval.",
125: "Ethernet performance retains peer-to-SUT TCP direction, one stream, 300 seconds, BlueField path and endpoint/counter evidence.",
126: "Netperf remains unready until TCP/UDP semantics, endpoint roles, duration, NIC profile and threshold are frozen; no generic command is accepted.",
127: "DLRM-v2 99 Server remains distinct from copied BERT/Llama text and requires release-pinned accuracy, latency and compliance artifacts.",
128: "DLRM-v2 99.9 Offline retains high-accuracy and throughput semantics; adjacent model artifacts remain a real source conflict.",
129: "GPT-J 99 Offline retains GPT-J accuracy and valid LoadGen evidence; malformed BERT/Llama references cannot be normalized silently.",
130: "Llama 99.9 Server retains model/tokenizer, high-accuracy, latency and alias validation; the copied BERT criterion remains unresolved.",
131: "Stable Diffusion XL Offline retains image-quality and throughput evidence; BERT text is explicitly rejected.",
132: "BERT 99.9 remains unready until release, category, scenario, backend and comparable AMD reference are selected.",
133: "Minigo remains a training case with a real 90-minute profile and non-MLPerf baseline; inference or generic score substitution is prohibited.",
134: "3D-UNet 99 Offline retains KiTS19 accuracy, phase timing and performance/compliance evidence rather than the copied BERT criterion.",
135: "RNN-T 99 Offline retains speech accuracy, phase timing and throughput/compliance evidence, distinct from neighboring MLPerf rows.",
136: "BERT 99.9 Server retains its explicit release profile, SQuAD accuracy, server latency and full phase evidence.",
137: "Two-node NCCL remains a real collective correctness/performance benchmark, not password/package setup or SSH reachability.",
138: "Llama3.1-405B Server retains inference/model identity, multi-GPU plan and valid MLPerf reference after correcting training/BERT text.",
139: "ResNet-50 Server retains image accuracy and server latency/throughput; neither training nor BERT satisfies the row.",
140: "RetinaNet Offline retains detection accuracy and offline throughput; copied training/BERT text is not executable scope.",
141: "Mixtral-8x7B Offline retains MoE model/tokenizer identity, accuracy and token-throughput under pinned rules.",
142: "The second NCCL row likewise requires a complete two-node matrix and managed rollback, not an open-ended privileged setup fragment.",
143: "The storage profile retains 70/30 mixed intent versus randwrite as a true conflict, while Machine Time is only planning metadata.",
144: "CrystalDiskMark sequential read remains manual GUI acceptance and must prove all write subtests disabled on a safe target.",
145: "Linux CPU inventory remains fully automated, read-only and complete across identity, topology, speed and cache; Expected remains engineer supplied.",
146: "NIC-in-BIOS remains manual visual evidence for every device/port; OS inventory is optional corroboration only.",
147: "Driver reload retains five cycles per approved 1G port/module, disappearance/recovery and independent BMC management continuity.",
148: "ConnectX-7 sensor inventory retains complete local and OOB collections with slot/entity correlation, not grep or driver inventory.",
149: "IOmeter retains separately approved sacrificial volumes, QD16 profile and a full 48-hour active window with health evidence.",
150: "NVMe information in BIOS retains physical adapter/drive arrangements, cold power-on and direct page evidence.",
151: "SAS/SATA versus NVMe remains a genuine technology conflict; no drive moves until owner scope and slot matrix are signed.",
152: "rocHPL retains P=2, Q=4, N=256400, NB=512, rank/GPU mapping, residual correctness and performance as separate gates.",
153: "OAM_6 requires discovered Redfish identity and synchronized WebUI comparison; a fixed chassis index cannot be assumed.",
154: "PEQT retains exact private YAML/config, debug level, every configured action and per-link PCIe health.",
155: "BPS retains 100 distinct runs and source 50-hour campaign; setup-per-cycle ambiguity remains an engineer lifecycle decision with no hidden retry.",
156: "FPGA and HMC remain separate firmware targets/images with ordered tasks and real AC activation; one component cannot stand for both.",
157: "Every NVIDIA GPU serial remains collected with stable UUID/BDF and compared to an authoritative board/GPU serial policy.",
158: "Every GPU framebuffer total remains read-only and compared to driver/ECC-aware reported-memory values, not raw advertised capacity.",
159: "GPU power-limit mutation retains stable targets, supported range, requested/enforced readback and exact pre-state restoration.",
160: "NVSM storage retains all drives, controllers and volumes with topology reconciliation; an overall OK is insufficient.",
161: "DCGM level-4 retains explicit entities, full included/skipped test matrix, resource isolation and exact service/persistence restoration.",
162: "NVTOP CPU Monitor is undefined by a TBD row; this is unclear intent, not two contradictory source requirements.",
163: "NVTOP GPU Power Monitor remains blocked without power domain, statistic, GPU scope, load fixture, sampling and acceptance contract.",
164: "BF3 FRU validation retains full inventory first, unique record attribution and all approved identity/description fields.",
165: "UFM validation retains both endpoint traffic directions, raw counters, displayed color and saved-view restoration; RX versus combined coloring is unresolved.",
166: "Storage LED remains three direct visual states with bounded non-destructive activity; LED off is not removal authorization.",
167: "GDS retains a safe mounted file, stable GPU mapping and fair documented CPU-path control; malformed/raw paths and guessed modes are prohibited.",
168: "AMD Replay AC Parity retains exact flags and address/event reconciliation; neighboring ODECC semantics cannot be copied in.",
169: "GEMM remains unready until the missing SPEC supplies workload, correctness, duration, performance reference and limits; no SGEMM guess is allowed.",
170: "The chamber/rail/slot setup is manual, but SST network execution, telemetry and per-link bandwidth evidence are automated after approval.",
171: "Front-bay setup and target authorization are manual, while the safe 12-hour storage workload and health collection are automated.",
172: "Chamber and recovery-console setup are manual, while verified `dramtest 0` execution and service-health collection can be automated.",
173: "Physical -5-percent margin/cabling setup is manual, while the all-slot 12-hour network workload and telemetry are automated.",
174: "Thermal/rail establishment is manual, while the all-GPU 12-hour burn and continuous sensor/error collection are automated.",
175: "The operator owns margin setup, while a bounded sandboxed upload/remove script can automate the repeated core; missing loop bound is readiness, not conflict.",
176: "Chamber/rail and power-policy setup are manual, while 24-hour liveness, idle-state and log collection are automated without adding workload.",
177: "DIMM population and environmental setup are manual, while SST memory coverage and ECC/telemetry collection are automated.",
178: "Cold fixture setup is manual, while the approved 100-cycle controller and per-cycle validation are automated without warm substitution.",
179: "Port connection and cold-margin setup are manual, while mapped USB traffic/integrity and reset/error collection are automated.",
180: "Cold chamber/rail and safe target setup are manual, while the 12-hour storage workload, integrity and health collection are automated.",
181: "Environmental setup is manual, while PA Manager/project cycle control can automate all 100 warm reboots and per-cycle evidence.",
182: "Ten source-defined AC removals may remain core manual actions; hybrid classification needs an engineer to approve a programmable fixture as equivalent coverage.",
183: "The 500-cycle title versus 12-hour procedure remains a true normative conflict; existing cycle control may run only the engineer-selected contract.",
184: "The 24-hour awake idle soak retains OS-specific reversible no-sleep policy, continuous liveness and exact rollback.",
185: "All CX-7/BF3 data ports remain in scope, but Ethernet, RoCE and InfiniBand require one explicit mode-specific tool/endpoint contract.",
186: "AMD Memeye remains blocked because the external SPEC contains the entire unknown intent; absence is not itself a source contradiction.",
187: "WAT OS-Ping remains private-document gated but the title and 250-cycle DC intent do not contradict the command; token mapping is readiness.",
188: "WAT pciePoll retains 250 DC cycles and stable per-BDF/link evidence; missing token mapping is private-tool readiness, not source conflict.",
189: "WAT usbPoll retains 250 DC cycles and physical/sysfs/serial topology evidence; missing token mapping is not contradictory source text.",
190: "Mixed AC/DC tokens plus missing i2cPoll selector remain a genuine semantic and safety conflict; blind HMC/BMC bus scanning is prohibited.",
191: "Mixed AC/DC tokens plus absent cpldPoll mapping remain a genuine conflict; no power campaign or register probe is safe.",
192: "WAT with MODS retains exact scenario tokens and 250 cycles, with licensed package, signed semantics and per-cycle target evidence required.",
193: "GDS retains 1GiB, 1MiB I/O, one worker, 60 seconds and a fair paired control; current official gdsio semantics must match the installed version.",
194: "SMBIOS Type 46 remains a complete handle/parent/property/value read with a platform reference; Actual is never promoted to Expected.",
195: "BMC upgrade retains the advertised vendor path, preserve-all matrix, task/activation evidence and no invented Redfish URI.",
196: "BIOS upgrade retains the BIOS component identity, preserved settings, host boot and full inventory health after activation.",
197: "BIOS downgrade retains anti-rollback, vendor-supported ordered version path, per-hop health and no forced image or automatic retry.",
198: "CPLD flash retains exact physical component mapping, OEM path, dependency order, activation and platform recovery.",
199: "PDB_BD remains blocked because the missing SPEC defines all semantics; this is unclear intent rather than contradictory source statements.",
200: "E1S_BD1 remains blocked with non-waivable storage protections; absent semantics are not a source conflict.",
}

CLASSIFICATION_OVERRIDES = {
    51: "MANUAL ONLY", 52: "MANUAL ONLY", 53: "MANUAL ONLY",
    70: "MANUAL ONLY", 74: "MANUAL ONLY",
    170: "REQUIRES PACKAGE / USER CONFIRMATION",
    171: "REQUIRES PACKAGE / USER CONFIRMATION",
    172: "REQUIRES PACKAGE / USER CONFIRMATION",
    173: "REQUIRES PACKAGE / USER CONFIRMATION",
    174: "REQUIRES PACKAGE / USER CONFIRMATION",
    175: "REQUIRES PACKAGE / USER CONFIRMATION",
    176: "REQUIRES PACKAGE / USER CONFIRMATION",
    177: "REQUIRES PACKAGE / USER CONFIRMATION",
    178: "REQUIRES PACKAGE / USER CONFIRMATION",
    179: "REQUIRES PACKAGE / USER CONFIRMATION",
    180: "REQUIRES PACKAGE / USER CONFIRMATION",
    181: "REQUIRES PACKAGE / USER CONFIRMATION",
}

CONFLICT_REMOVALS = {19, 69, 162, 175, 186, 187, 188, 189, 199, 200}
BLOCKED_CATEGORIES = {
    19: "A_UNCLEAR_TEST_INTENT", 45: "B_PROCEDURE_CRITERIA_CONFLICT",
    54: "B_PROCEDURE_CRITERIA_CONFLICT", 62: "B_MUTUALLY_DIFFERENT_RESET_INTENTS",
    64: "B_READ_VERSUS_MUTATION_CONFLICT", 67: "B_DISCOVERY_VERSUS_INSERTION_CONFLICT",
    73: "A_UNCLEAR_TEST_INTENT", 79: "A_MISSING_COMPLETE_SPECIFICATION",
    80: "A_AND_H_UNDEFINED_STORAGE_TARGET_OPERATION", 92: "A_UNCLEAR_TEST_INTENT",
    103: "A_AND_H_UNDEFINED_RAS_INJECTION", 104: "A_AND_H_UNDEFINED_RAS_INJECTION",
    105: "A_AND_H_UNDEFINED_PCIE_STIMULUS", 106: "A_AND_H_UNDEFINED_PCIE_STIMULUS",
    107: "A_AND_H_UNDEFINED_FATAL_PCIE_STIMULUS", 162: "A_UNCLEAR_TEST_INTENT",
    163: "A_UNCLEAR_METRIC_AND_ACCEPTANCE", 186: "A_MISSING_ENTIRE_VENDOR_SPEC",
    190: "B_F_G_PRIVATE_TOOL_POWER_AND_BUS_CONFLICT", 191: "B_F_G_PRIVATE_TOOL_POWER_AND_TARGET_CONFLICT",
    199: "A_MISSING_COMPLETE_SPECIFICATION", 200: "A_AND_H_UNDEFINED_STORAGE_TARGET_OPERATION",
}

VALIDATION_SAMPLE = set(CLASSIFICATION_OVERRIDES) | CONFLICT_REMOVALS | {
    2, 14, 45, 54, 76, 96, 122, 145, 166, 183, 193, 197
}


def load_record(directory: Path, sequence: int) -> tuple[Path, dict]:
    path = next(directory.glob(f"{sequence:04d}_*.json"))
    return path, json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    if set(NOTES) != set(range(1, 201)):
        raise SystemExit("NOTES must contain exactly sequences 1..200")
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for sequence in range(1, 201):
        v31_path, v31 = load_record(V31, sequence)
        v3_path, _ = load_record(V3, sequence)
        before_class = v31["v3_1_conclusion"]["automation_classification"]
        after_class = CLASSIFICATION_OVERRIDES.get(sequence, before_class)
        before_conflict = "SOURCE_CONFLICT" in v31["v3_1_conclusion"].get("execution_readiness", [])
        after_conflict = before_conflict and sequence not in CONFLICT_REMOVALS
        corrected = after_class != before_class or before_conflict != after_conflict
        outcome = "NEED_ENGINEER_DECISION" if sequence == 182 else ("CORRECTED" if corrected else "PASS_UNCHANGED")
        before = {
            "automation_classification": before_class,
            "source_conflict": before_conflict,
            "v3_1_record": v31_path.relative_to(ROOT).as_posix(),
        }
        after = {
            "automation_classification": after_class,
            "source_conflict": after_conflict,
            "effective_record_rule": "XLSX + inherited V3 detail + V3.1 explicit changes + Final Audit explicit corrections",
        }
        record = {
            "schema_version": "v3-1-final-audit-record-1.0",
            "sequence": sequence,
            "source_key": v31["source_key"],
            "case_variant_id": v31["case_variant_id"],
            "source_ref": v31["source_ref"],
            "audit_outcome": outcome,
            "source_material_read": {
                "xlsx_row": True, "deepseek": True, "gpt_v2": True,
                "v3": v3_path.relative_to(ROOT).as_posix(),
                "v3_1": v31_path.relative_to(ROOT).as_posix(),
            },
            "independent_semantic_finding": NOTES[sequence],
            "audit_checks": {
                "original_test_intent_preserved": True,
                "scope_not_reduced_without_recorded_override": True,
                "v3_detail_retained_by_additive_overlay_rule": True,
                "original_method_and_command_provenance_preserved": True,
                "required_evidence_reviewed": v31["expected_evidence"],
                "safety_and_stop_reviewed": v31["safety_boundaries"],
                "no_automatic_retry_reviewed": v31["no_automatic_retry"],
                "engineer_owned_verdict_reviewed": v31["engineer_owned_verdict"],
            },
            "before": before,
            "after": after,
            "blocked_category": BLOCKED_CATEGORIES.get(sequence),
            "modernized_method_audit": {
                "status": "CONDITIONAL_OR_NOT_APPLICABLE_ACCEPTED",
                "original_method_retained": True,
                "project_version_and_applicability_required": True,
                "no_method_executed": True,
            },
            "reason": NOTES[sequence],
            "regression": {
                "found": sequence == 51,
                "corrected": sequence == 51,
                "detail": "Restored both source-required WebUI views and corrected the capability class." if sequence == 51 else "No unrepaired V3-to-V3.1 semantic loss after applying the additive overlay-retention rule.",
            },
            "agent_understanding_validation": "SELECTED_SAME_MODEL_FAMILY_NO_DUT" if sequence in VALIDATION_SAMPLE else "NOT_SELECTED_RISK_BASED_FINAL_SAMPLE",
            "hardware_tested": False,
            "formal_test_verdict": "ENGINEER OWNED; NOT SET",
        }
        records.append(record)

    for start in range(1, 201, 20):
        chunk = records[start - 1:start + 19]
        path = OUT / f"{start:04d}_{start + 19:04d}.json"
        path.write_text(json.dumps(chunk, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
