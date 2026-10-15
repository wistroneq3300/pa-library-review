#!/usr/bin/env python3
"""Apply the explicit 2026-10-15 engineering rulings to completed records.

This is a deterministic migration of user-approved decisions, not a testcase
review generator. It reopens and verifies every affected XLSX row before
adding a source-key-bound decision overlay. It never changes completed_count.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import openpyxl


ROOT = Path(__file__).resolve().parents[3]
XLSX = ROOT / "data" / "REVISED_commands_merged_with_raw.xlsx"
RECORDS = ROOT / "gpt-review" / "v3-1-full-3112" / "REVIEW_RECORDS"


CASES = [
    ("Functionality|340|Wistron-BIOS-00007-V003", "ED-39", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "BIOS upgrade remains the functional intent; AFULnx, AFUEFI, BMC Flash or another approved method is selected by Project SPEC without erasing the AFULnx/AFUEFI source mismatch.", ["pre/target BIOS version", "approved upgrade tool and image", "activation and boot", "post-version and health", "coverage delta for the source-named method"], "tool/image/region policy, stable power and recovery"),
    ("Functionality|341|Wistron-BIOS-00008-V003", "ED-39", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "BIOS downgrade remains the functional intent; project approval binds the downgrade-capable tool and anti-rollback policy while preserving the same-version AFUEFI source text as a conflict.", ["current and lower target versions", "approved downgrade path", "anti-rollback state", "activation and boot", "source-tool coverage difference"], "signed image, downgrade permission, stable power and recovery"),
    ("Functionality|342|Wistron-BIOS-00009-V003", "ED-39", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "Same-version BIOS reflash is the retained purpose; Project SPEC selects the supported tool and records whether AFULnx or the source AFUEFI path was actually covered.", ["same pre/target version", "approved reflash tool/image", "flash task and activation", "post-version and boot health", "original-tool coverage"], "tool package, image hash, region policy and recovery"),
    ("Functionality|343|Wistron-BIOS-00010-V005", "ED-39", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "The case is an upgrade/downgrade cycle test. Project Test Plan must define whether 100 means flash operations or upgrade/downgrade pairs, version order, per-round checks, stop conditions and recovery.", ["approved count semantics", "ordered version matrix", "per-round flash/activation/readback", "failure stop rule", "recovery and final health"], "cycle definition, images, tool, service window and recovery"),
    ("Functionality|347|Wistron-BIOS-00014-V002", "ED-40", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "Corrupt-image rejection and downgrade/anti-rollback rejection are separate mechanisms and separate evidence checkpoints; the project may select one or both but cannot cross-credit a single rejection.", ["corrupt-image stimulus and rejection reason", "lower-version stimulus and anti-rollback reason", "separate logs/status for each selected mechanism", "unchanged active firmware", "recovery readiness"], "selected matrix, safe malformed image, lower image and acceptance codes"),
    ("Functionality|375|Wistron-BIOS-00042-V002", "ED-41", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "One testcase may contain PCI Hot-Plug and SR-IOV, but each function has independent state, behavior and evidence; VF success never proves actual hot-plug behavior.", ["Hot-Plug Enabled/Disabled states", "actual insertion/removal behavior", "SR-IOV VF creation and host enumeration", "guest OS VF evidence", "per-function Expected results"], "device/port, guest stack, safe service method and restoration"),
    ("Functionality|387|Wistron-BIOS-00054-V002", "ED-42", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Both User and Administrator Password roles are required, with separate set/authentication/privilege/clear/recovery evidence; Administrator success cannot substitute for User coverage.", ["User Password lifecycle", "Administrator Password lifecycle", "role-specific privilege difference", "clear verification", "recovery without exposing secrets"], "approved password policy, prompts, lockout behavior and recovery owner"),
    ("Functionality|388|Wistron-BIOS-00055-V002", "ED-43", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Use a project Secure Boot matrix whose enabled/disabled, signed/unsigned OS, PK and MOK states align with the expected boot result; do not mutate keys or MOK without approval.", ["state capture before each boot", "signed-image expected boot", "unsigned-image expected allow/reject", "PK/MOK evidence", "restored security state"], "approved images, state matrix, key/MOK authority and recovery"),
    ("Functionality|391|Wistron-BIOS-00058-V003", "ED-44", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Quiet Boot and Boot Device remain in one testcase with separate visible-presentation, enumeration, order-configuration and actual-boot checkpoints; no universal timing or initialization meaning is assumed.", ["Quiet Boot presentation", "device enumeration", "boot-order change/readback", "actual boot follows order", "restoration"], "platform meaning, approved devices/order and recovery"),
    ("Functionality|397|Wistron-BIOS-00064-V002", "ED-45", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Discard Changes and Exit is accepted only when an unsaved edit is discarded and the previously saved value remains after exit; the contradictory save criterion is not used.", ["record saved baseline", "make unsaved edit", "Discard Changes and Exit", "verify original saved value", "no unintended setting changes"], "writable field and safe temporary value"),
    ("Functionality|399|Wistron-BIOS-00066-V002", "ED-45", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Discard Changes and Reset must discard the pending edit across reset and retain the prior saved value; a saved edit is not PASS evidence.", ["saved baseline", "unsaved edit", "Discard Changes and Reset", "post-reset readback", "platform health"], "writable field, safe value, reset window and recovery"),
    ("Functionality|401|Wistron-BIOS-00068-V002", "ED-45", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "The standalone Discard Changes control removes the pending edit and leaves the prior saved value intact; it does not prove that the edited value can be saved.", ["saved baseline", "pending edit", "Discard control", "same-session readback", "exit without mutation"], "writable field and safe temporary value"),
    ("Functionality|404|Wistron-BIOS-00071-V002", "ED-45", "MANUAL ONLY", "SOURCE_CONFLICT", "IMPROVED", "Restore User Defaults must recall the approved stored user-default profile and prove its values; merely completing Save is insufficient.", ["approved user-default profile", "known differing current value", "Restore User Defaults", "readback of profile values", "final approved state"], "profile provenance, selected fields and recovery"),
    ("Functionality|429|Wistron-BIOS-00096-V003", "ED-46", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "This is Firmware Image Selection, not proof of update. Validate browse/select/cancel or staging behavior without crediting firmware-update coverage unless a separately approved commit occurs.", ["available approved image", "selection identity", "cancel/stage boundary", "no unintended write", "selection UI evidence"], "picker semantics, target and approved image"),
    ("Functionality|430|Wistron-BIOS-00097-V003", "ED-46", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Firmware Update requires pre-version, an approved update, required activation/reset, BIOS-homepage target-version readback and normal boot; version equality alone does not validate all regions.", ["pre-version", "approved flash/task", "activation/reset", "BIOS homepage target version", "normal boot and scoped region/config evidence"], "target/image/tool, preservation scope, stable power and recovery"),
    ("Functionality|432|Wistron-BIOS-00099-V003", "ED-47", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "The SMBIOS Event Log viewer is reviewed as read-only: enter the page, verify logs/fields/records and navigation; unrelated setting changes, defaults or clearing do not count.", ["page entry", "visible log records", "field correctness", "expected record correlation", "navigation without clear/mutation"], "expected records and authoritative field definitions"),
    ("Functionality|435|Wistron-BIOS-00102-V003", "ED-47", "MANUAL ONLY", "IMPROVED", "CHANGED", "The BMC self-test log is read-only first: page access, displayed records/fields and UI navigation are the acceptance scope unless Project SPEC identifies a separate writable control.", ["page entry", "self-test log visibility", "field accuracy", "expected record correlation", "UI navigation"], "expected self-test records and any separately approved writable scope"),
    ("Functionality|437|Wistron-BIOS-00104-V003", "ED-47", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "View System Event Log is a read-only viewer check; preserve and inspect records and navigation without substituting setting persistence, Load Default or log clearing.", ["page entry", "SEL records", "field/order correctness", "expected event correlation", "navigation with evidence preserved"], "expected SEL events and field schema"),
    ("Functionality|453|Wistron-BIOS-00120-V003", "ED-48", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "AMD Memory Configuration Status follows actual platform capability: approved change/save/reboot/readback/restore when writable, or authoritative display comparison when read-only, with unequal coverage recorded.", ["field writability evidence", "write lifecycle when supported", "read-only value comparison otherwise", "reboot/readback where required", "restoration and coverage delta"], "platform field map, approved values and recovery"),
    ("Functionality|458|Wistron-BIOS-00125-V003", "ED-49", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Retain the source-required PCIe Compliance Mode functional change. A default/read-only observation is partial evidence only and cannot complete the setting-change objective.", ["tested PCIe port", "approved mode change", "expected compliance/link behavior", "safe exit", "restored mode and link health"], "port, mode, expected instrumentation, exit and recovery"),
    ("Functionality|464|Wistron-BIOS-00131-V003", "ED-46", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "This variant covers Firmware Image Selection and its browse/cancel/stage boundary; do not infer or credit an update unless a separately approved commit lifecycle runs.", ["target and image identity", "selection action", "cancel/stage state", "no unintended flash", "UI evidence"], "picker semantics, target and approved image"),
    ("Functionality|465|Wistron-BIOS-00132-V003", "ED-46", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "Update Image is a complete firmware lifecycle with pre-version, approved flash, activation/reset, BIOS target-version confirmation and boot health; extra regions/configuration remain Project SPEC scope.", ["pre-version", "approved image/update path", "activation/reset", "BIOS homepage target version", "boot and scoped preservation evidence"], "component, versions, image/tool, power and rollback"),
    ("Functionality|467|Wistron-BIOS-00134-V003", "ED-47", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "The SMBIOS Event Log viewer is read-only first; verify presentation, fields, records and navigation without changing settings, loading defaults or clearing evidence.", ["page entry", "log visibility", "field correctness", "expected record correlation", "navigation/no clear"], "record expectations and field authority"),
    ("Functionality|470|Wistron-BIOS-00137-V003", "ED-47", "MANUAL ONLY", "IMPROVED", "CHANGED", "BMC self-test log acceptance is read-only page/record/field/navigation evidence. Any actual writable page control is a separate Project SPEC-defined extension.", ["page entry", "displayed self-test records", "field accuracy", "expected record correlation", "navigation"], "self-test baseline and any separate writable contract"),
    ("Functionality|472|Wistron-BIOS-00139-V003", "ED-47", "MANUAL ONLY", "SOURCE_CONFLICT", "CHANGED", "View System Event Log is read-only first; settings changes, Load Default and Clear Log are excluded from viewer acceptance and existing evidence is preserved.", ["page access", "SEL visibility", "field/order correctness", "expected events", "navigation without mutation"], "expected SEL records and schema"),
    ("Functionality|477|Wistron-BIOS-00144-V002", "ED-50", "BLOCKED", "NEED_ENGINEER_DECISION", "IMPROVED", "Define AMD Secure Processor Version through the applicable vendor field/path and expected value source; the review must not invent a utility, offset or value and the TBD source still lacks executable semantics.", ["exact processor component", "authoritative field/path", "applicable versions", "expected value source", "non-empty raw and decoded evidence"], "Vendor SPEC or owner field decision"),
    ("Functionality|557|Wistron-BIOS-00224-V005", "ED-50", "BLOCKED", "SOURCE_CONFLICT", "IMPROVED", "Cache SRAM Type must map to an exact SMBIOS or vendor-defined field rather than being guessed from adjacent Supported/Current SRAM fields; empty grep is not evidence.", ["structure/type", "field offset and encoding", "vendor alias decision", "expected per-cache value", "raw plus decoded non-empty evidence"], "SMBIOS version and Vendor SPEC field mapping"),
    ("Functionality|628|Wistron-BIOS-00295-V005", "ED-50", "BLOCKED", "SOURCE_CONFLICT", "IMPROVED", "The Reserved-field case requires an exact structure/offset/length and applicable SMBIOS version; do not silently move Type 17 scope to Type 32 or accept an empty grep.", ["selected structure", "reserved offset/length", "applicable version", "expected raw reserved value", "non-empty raw/decode evidence"], "owner selection plus SMBIOS/Vendor SPEC mapping"),
    ("Functionality|629|Wistron-BIOS-00296-V005", "ED-50", "BLOCKED", "SOURCE_CONFLICT", "IMPROVED", "Boot Status is a Type 32 concept, not a Type 17 Memory Device field. The Master conflict remains until the owner approves Type 32 correction or names a real Type 17 target; no empty grep PASS.", ["approved Type 32 correction or Type 17 replacement", "field offset/version", "status/additional-data semantics", "expected stimulus/result", "raw and decoded evidence"], "master-owner target decision and applicable standard"),
    ("Functionality|659|Wistron-BIOS-00326-V005", "ED-50", "BLOCKED", "SOURCE_CONFLICT", "IMPROVED", "The Type 38 label BYTE is not a defined acceptance field. Require exact offset/length/semantics and Vendor SPEC; do not substitute a neighboring byte or accept blank grep output.", ["exact Type 38 field", "offset/length", "encoding/semantics", "expected value source", "non-empty raw/decode evidence"], "Vendor SPEC or master-owner field decision"),
    ("Functionality|708|Wistron-BIOS-00376-V002", "ED-51", "BLOCKED", "NEED_ENGINEER_DECISION", "BLOCKED", "ENGINEER DECISION PENDING remains controlling: do not choose TSEG range coverage or SmiHandler4 trace and do not authorize debug BIOS flash or undocumented register operations.", ["owner selects test purpose", "exact range or handler evidence model", "approved debug BIOS if applicable", "read-only register/SOL method", "rollback and OOB recovery"], "explicit engineer decision and approved debug/recovery contract"),
    ("Functionality|713|Wistron-BMC-00003-V008", "ED-52", "REQUIRES PACKAGE / USER CONFIRMATION", "IMPROVED", "CHANGED", "Target remains BMC. Project SPEC binds versions, direction, host state, activation/reset, approved update method, criteria and recovery; these are readiness inputs rather than an irreducible blocker.", ["BMC identity/current-target versions", "signed image and direction", "approved tool/API", "host state and activation/reset", "post-version/health and recovery"], "project update matrix, reset contract and recovery"),
    ("Functionality|714|Wistron-BMC-00004-V007", "ED-52", "REQUIRES PACKAGE / USER CONFIRMATION", "IMPROVED", "CHANGED", "Target remains BMC and the actual Redfish or other update path is Project SPEC-selected. Fixed credentials, untrusted TLS and unadvertised actions are excluded from the formal recommendation.", ["BMC inventory and versions", "approved image/direction", "advertised update action/task", "secure auth/TLS", "activation, health and recovery"], "vendor API contract, images, host/reset plan and OOB recovery"),
    ("Functionality|718|Wistron-BMC-00008-V007", "ED-52", "REQUIRES PACKAGE / USER CONFIRMATION", "IMPROVED", "CHANGED", "Target remains FPGA. Project SPEC binds the update path and host/reset/activation state; a BMC update path or powered-state assumption cannot silently replace FPGA coverage.", ["FPGA identity/current-target versions", "signed FPGA image/direction", "approved tool/API", "host state and activation/reset", "FPGA inventory/health and recovery"], "FPGA vendor contract, power state, images and recovery"),
    ("Functionality|720|Wistron-BMC-00010-V007", "ED-52", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "Target is HIB-CPLD as named by the testcase; the source's FPGA wording remains recorded as a conflict and cannot redirect the image. Project SPEC binds the approved method and lifecycle.", ["HIB-CPLD identity/current-target versions", "signed HIB-CPLD image/direction", "approved tool/API and selector", "host state/activation/reset", "target-specific health and recovery"], "HIB-CPLD vendor contract, images, power state and recovery"),
    ("Functionality|722|Wistron-BMC-00012-V008", "ED-52", "REQUIRES PACKAGE / USER CONFIRMATION", "SOURCE_CONFLICT", "CHANGED", "Target is DCSCM-CPLD as named by the testcase; do not substitute FPGA. Preserve the source conflict while Project SPEC binds device selector, approved update path, activation and independent recovery.", ["DCSCM-CPLD identity/current-target versions", "signed image/direction", "approved selector/tool/API", "host state/activation/reset", "target-specific evidence and independent recovery"], "DCSCM-CPLD contract, images, power state and recovery"),
]


def row_hash(headers: list[object], values: list[object]) -> str:
    row = dict(zip(headers, values, strict=True))
    payload = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def replace_once(text: str, old: str, new: str, path: Path) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path.name}: expected one {old!r}, found {count}")
    return text.replace(old, new, 1)


def replace_json_string(text: str, key: str, old_value: str, new_value: str, path: Path) -> str:
    pattern = rf'("{re.escape(key)}"\s*:\s*)"{re.escape(old_value)}"'
    updated, count = re.subn(pattern, rf'\g<1>"{new_value}"', text, count=1)
    if count != 1:
        raise RuntimeError(f"{path.name}: expected one {key}={old_value!r}, found {count}")
    return updated


def main() -> None:
    progress = json.loads((ROOT / "gpt-review" / "v3-1-full-3112" / "PROGRESS.json").read_text(encoding="utf-8"))
    if progress["completed_count"] != 891:
        raise RuntimeError("decision migration requires completed_count 891")

    workbook = openpyxl.load_workbook(XLSX, read_only=True, data_only=False)
    by_key: dict[str, Path] = {}
    records: dict[str, dict[str, object]] = {}
    for path in RECORDS.glob("*.json"):
        record = json.loads(path.read_text(encoding="utf-8"))
        by_key[str(record["source_key"])] = path
        records[str(record["source_key"])] = record

    changed: list[str] = []
    for source_key, decision_id, new_class, new_outcome, new_second, interpretation, checkpoints, remaining in CASES:
        path = by_key.get(source_key)
        if path is None:
            raise RuntimeError(f"missing active record: {source_key}")
        record = records[source_key]
        sheet_name, row_text, code = source_key.split("|", 2)
        source_row = int(row_text)
        sheet = workbook[sheet_name]
        headers = [cell.value for cell in sheet[1]]
        values = [cell.value for cell in sheet[source_row]]
        if str(values[0] or "").strip() != code:
            raise RuntimeError(f"XLSX code mismatch: {source_key}")
        digest = row_hash(headers, values)
        if digest != record["source_integrity"]["original_row_sha256"]:
            raise RuntimeError(f"XLSX row hash mismatch: {source_key}")

        text = path.read_text(encoding="utf-8")
        old_class = str(record["automation_classification"])
        old_outcome = str(record["review_outcome"])
        old_second = str(record["second_review_outcome"])
        text = replace_json_string(text, "automation_classification", old_class, new_class, path)
        text = replace_json_string(text, "review_outcome", old_outcome, new_outcome, path)
        text = replace_json_string(text, "second_review_outcome", old_second, new_second, path)
        overlay = {
            "decision_version": "2026-10-15",
            "decision_ids": ["ED-33", "ED-34", "ED-35", "ED-36", "ED-37", "ED-38", decision_id],
            "engineering_decision_status": "PENDING" if decision_id == "ED-51" else "APPROVED AND APPLIED",
            "review_count_change": 0,
            "approved_interpretation": interpretation,
            "required_checkpoints": checkpoints,
            "remaining_project_inputs": remaining,
            "active_blocked_analysis": {
                "is_blocked": new_class == "BLOCKED",
                "analysis": "Semantic identity remains unresolved and must not be guessed." if new_class == "BLOCKED" else "The approved ruling resolves the review-level ambiguity; remaining package, SPEC, parameter, environment, approval and recovery facts are execution-readiness inputs."
            },
            "coverage_boundary": "Read-only or alternative-method evidence is credited only to the scope actually executed; unexecuted Master method or functional coverage remains explicit.",
            "verdict_boundary": "Review updated; testcase not executed; engineer retains final PASS/FAIL/BLOCKED ownership.",
            "supersedes": "For current V3.1 use, this additive decision overlay supersedes any earlier classification or blocked rationale that conflicts with the approved ruling while preserving the earlier text as review history."
        }
        serialized = json.dumps(overlay, ensure_ascii=False, separators=(",", ":"))
        marker = '"review_outcome"'
        text = replace_once(text, marker, f'"engineering_decision_update":{serialized},\n  {marker}', path)
        path.write_text(text, encoding="utf-8", newline="\n")
        changed.append(source_key)

    print(json.dumps({"updated_records": len(changed), "completed_count_change": 0, "source_keys": changed}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
