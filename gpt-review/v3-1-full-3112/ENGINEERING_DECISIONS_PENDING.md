# Engineering Decisions Pending

No global classification decision is pending. ED-32 resolved Seq 182 without
changing other AC-cycle cases.

## Case-level decision pending

- `Functionality|340|Wistron-BIOS-00007-V003` — The item and project-script
  path name the case `AFULnx: upgrade`, but the preserved Procedure says to
  flash the same version and invokes `afuefix64.efi`. The owner must decide
  whether the intended test is an AFULnx upgrade or an AFUEFI same-version
  reflash, and provide the corresponding approved tool, image, region policy,
  and recovery procedure. This decision is limited to this source variant and
  does not change other BIOS-flash cases.
- `Functionality|341|Wistron-BIOS-00008-V003` — The item and project-script
  path name an `AFULnx: downgrade`, but the preserved Procedure specifies a
  same-version operation and invokes `afuefix64.efi`. The owner must choose the
  intended direction/tool and supply its downgrade/anti-rollback or reflash
  policy. This ruling remains case-specific.
- `Functionality|342|Wistron-BIOS-00009-V003` — The reflash direction is
  consistent, but the item/script say AFULnx while the Procedure invokes
  `afuefix64.efi`. The owner must select the supported execution tool and
  environment for this variant before any firmware write.
- `Functionality|343|Wistron-BIOS-00010-V005` — The title requests upgrade
  and downgrade for 100 times, while Procedure and Criteria define a
  same-version reflash and no iteration sequence. The owner must define the
  operation counted, version/image order, activation method, per-cycle
  acceptance and abort/recovery policy. This case remains `BLOCKED` because
  the destructive operation semantics—not merely project parameters—conflict.
- `Functionality|347|Wistron-BIOS-00014-V002` — The title says the downgrade
  image is corrupt, while Procedure and Criteria only specify a lower version
  that must be rejected. The owner must state whether corruption validation,
  anti-rollback, or a combined stimulus is intended; one combined rejection
  cannot independently prove both mechanisms.
- `Functionality|375|Wistron-BIOS-00042-V002` — The Procedure defines a
  global PCI Hot-Plug Support and resource-padding setting, while Criteria add
  guest OS installation and virtual-function devices without defining their
  causal or per-state relationship. The owner must decide whether physical PCI
  insertion/removal is part of this case or explicitly out of scope, identify
  the hot-plug/SR-IOV device and guest stack, and define the expected host and
  guest/VF result for Enabled and Disabled. This is case-specific and does not
  create a global rule for other PCI hot-plug cases.
- `Functionality|387|Wistron-BIOS-00054-V002` — Items names `User Password`,
  but every role-specific Procedure action sets, authenticates, and clears
  `Administrator Password`. The owner must choose the intended password role
  and provide the corresponding prompt, supported characters/range, lockout
  behavior, secret-handling and recovery method. No password action is safe or
  valid until this case-specific conflict is resolved.
- `Functionality|388|Wistron-BIOS-00055-V002` — The Criteria require an
  unsigned OS to be rejected while Secure Boot is enabled, but step 4 says to
  disable Secure Boot and steps 5–6 perform a MOK state change immediately
  before that boot. The owner must define the exact enabled/disabled, PK and
  MOK state for each signed/unsigned boot attempt and identify the approved
  artifacts. No key, CSM, OS-install or MOK mutation is permitted until this
  case-specific state sequence is corrected.
- `Functionality|391|Wistron-BIOS-00058-V003` — Items and Procedure identify
  `Quiet Boot`, but the Criteria require boot-device enumeration, boot-order
  configuration and following that order. Those are different firmware
  functions with different evidence and risk. The owner must select one scope
  and align the complete Procedure and Criteria before any setting change.
- `Functionality|397|Wistron-BIOS-00064-V002` — Items and Procedure require
  `Discard Changes and Exit` and explicitly say the edit is NOT saved, while
  Criteria 2 says the change should be saved. The owner must correct either
  the operation or the expected persistence result. No BIOS change is valid
  while the two opposite PASS conditions remain.
- `Functionality|399|Wistron-BIOS-00066-V002` — The reset variant independently
  has the same opposite acceptance states: Procedure says the pending edit is
  NOT saved by `Discard Changes and Reset`, while Criteria 2 says it is saved.
  The owner must align the reset-specific operation and expected value before
  any BIOS edit or platform reset.
- `Functionality|401|Wistron-BIOS-00068-V002` — The standalone control is
  `Discard Changes`, which implies removal of the pending edit, while its
  Criteria require that the setting can be saved. The owner must correct the
  operation or the acceptance state before any BIOS edit; this decision is
  separate from the Exit and Reset variants.
- `Functionality|404|Wistron-BIOS-00071-V002` — The item names `Restore User
  Defaults`, but its Criteria only check whether a setting can be saved. The
  owner must accept or correct a recall/application criterion and define the
  approved stored profile; a generic save confirmation cannot prove restore.
  The operation remains `MANUAL ONLY`, with execution not ready until this
  case-specific acceptance gap is resolved.
- `Functionality|429|Wistron-BIOS-00096-V003` — The item names firmware-update
  image selection, but the generic Procedure treats it as a stored value that
  persists through save/reboot and returns through Load Default. The owner and
  vendor must decide whether the case covers non-destructive selection/cancel,
  staging, or an actual firmware write, then define the target component,
  commit trigger, image provenance, acceptance lifecycle and independent
  recovery. No image may be selected while those semantics remain unresolved.
- `Functionality|430|Wistron-BIOS-00097-V003` — The item explicitly names
  `Update Image`, while the Procedure and Criteria only exercise generic BIOS
  setting persistence and Load Default. The owner/vendor must supply an actual
  update lifecycle: target component, source/target version, signed compatible
  image, supported update and activation path, configuration-preservation
  expectation, stable-power controls and independent rollback/recovery. No
  firmware write is authorized by the existing generic steps.
- `Functionality|432|Wistron-BIOS-00099-V003` — Items names a read-only
  `View Smbios Event Log` function, but Procedure and Criteria demand an
  unspecified setting change, persistence check and Load Default. The owner
  must choose either viewer behavior with expected event records/UI evidence,
  or a separately defined settings lifecycle, and align the complete source.
  No log change, erase or default operation is authorized while this
  View-versus-configuration conflict remains.
- `Functionality|435|Wistron-BIOS-00102-V003` — `BMC self test log` does not
  establish whether the page is a read-only diagnostic view, exposes
  persistent policy fields, or mixes policy with clear/reset actions. The
  owner/vendor must confirm page type and log ownership, then provide either
  expected self-test records and viewer acceptance or a bounded field/default
  lifecycle. No generic mutation or log clear is safe before that decision.
- `Functionality|437|Wistron-BIOS-00104-V003` — Items explicitly says
  `View System Event Log`, while Procedure and Criteria require random setting
  changes, persistence and Load Default. The owner must retain a read-only
  viewer scope with expected record fields/navigation, or define a separate
  event-log settings case. No log clear or settings/default action is valid
  evidence for the current View objective.
- `Functionality|453|Wistron-BIOS-00120-V003` — Items names
  `ADVANCE AMD Mem Configuration Status`, but Procedure and Criteria require
  all/random non-default changes and saved persistence. The owner must confirm
  whether this is read-only memory topology/training/status validation, a
  writable memory-configuration lifecycle, or two separate cases, then align
  the fields, expected evidence and recovery. No memory-setting change is
  authorized while the scope remains contradictory.
- `Functionality|458|Wistron-BIOS-00125-V003` — The primary Procedure requires
  non-default PCIe Compliance Mode changes and persistence, while the same-row
  DeepSeek command narrows the test to a default-only inspection and reboot.
  The owner must choose one scope and define affected ports/endpoints, expected
  link or instrumented compliance behavior, reset and restoration. No active
  compliance/test mode is authorized while the operation remains unresolved.
- `Functionality|464|Wistron-BIOS-00131-V003` — `Select Image file` names a
  firmware picker, but the generic Procedure describes an unnamed persistent
  setting and Load Default. The owner/vendor must define whether the case is
  browse/cancel, transient selection, persistent staging, or an actual update,
  including target, image provenance, commit boundary, pending state and
  recovery. No image selection or firmware write is authorized meanwhile.
- `Functionality|465|Wistron-BIOS-00132-V003` — `Update Image` names a
  destructive firmware lifecycle, but Procedure and Criteria only exercise an
  unspecified BIOS setting and Load Default. The owner/vendor must provide the
  target, source/target versions, signed image, supported update and activation
  path, region/configuration preservation, stable power and rollback/recovery.
  No firmware write is authorized by the current generic steps.
- `Functionality|467|Wistron-BIOS-00134-V003` — Items explicitly names
  `View Smbios Event Log`, but Procedure and Criteria demand an unspecified
  setting change, persistence and Load Default. The owner must choose a
  read-only viewer lifecycle with expected record/navigation evidence or a
  separately defined settings case. No log clear or mutation is authorized
  while the view-versus-settings conflict remains.
- `Functionality|470|Wistron-BIOS-00137-V003` — `BMC self test log` does not
  establish whether the page is a read-only diagnostic viewer, a status page,
  exposes persistent policy fields, or combines scopes. The owner/vendor must
  define the page type, record/store ownership and scope-specific acceptance.
  No generic setting change, clear or diagnostic reset is authorized meanwhile.
- `Functionality|472|Wistron-BIOS-00139-V003` — Items explicitly names
  `View System Event Log`, while Procedure and Criteria require random setting
  changes, persistence and Load Default. The owner must retain a read-only SEL
  viewer scope with expected record/navigation evidence or define a separate
  settings case. No SEL clear or mutation is authorized while unresolved.
- `Functionality|477|Wistron-BIOS-00144-V002` — define the exact AMD Secure
  Processor component/version field, authoritative read-only BIOS/BMC/OS path,
  expected value source and acceptance criteria. Procedure and Criteria are both
  `TBD`; no guessed PSP utility, image, update or flash action is authorized.
- `Functionality|557|Wistron-BIOS-00224-V005` — identify the authoritative
  SMBIOS or vendor field and offset intended by `Cache SRAM Type`. Adjacent
  cases independently cover Supported SRAM Type and Current SRAM Type, while
  this row supplies no third-field definition or alias rule. Decide whether it
  is a duplicate/alias or a distinct vendor field and provide its encoding and
  expected per-cache baseline. The literal grep and any silent substitution are
  not authorized meanwhile.
- `Functionality|628|Wistron-BIOS-00295-V005` — decide whether the item targets
  a specific Type 17 enum/bit region or the six Reserved bytes of SMBIOS Type
  32 suggested by the immediately adjacent `Boot Status` row. Supply the exact
  structure, offset/length, applicable version and expected raw value, and
  correct or split the testcase/script. The current Type 17 `grep Reserved`
  cannot distinguish these scopes and must not be used for acceptance.
- `Functionality|629|Wistron-BIOS-00296-V005` — correct the structure identity:
  `Boot Status` is defined by SMBIOS Type 32 System Boot Information, not Type
  17 Memory Device. Decide whether to convert this case to Type 32 or replace
  the target with a real Type 17 field, then specify exact offsets/version,
  expected status and additional-data semantics, any boot stimulus and recovery.
  An empty Type 17 grep is not PASS evidence and no silent substitution is
  authorized.
- `Functionality|659|Wistron-BIOS-00326-V005` — identify the exact SMBIOS
  Type 38 field intended by the bare label `BYTE`, including offset/length,
  applicable version, semantics and expected value. Decide whether it is a
  distinct field, an alias/duplicate of an adjacent row, or a source artifact.
  The literal grep is not field evidence, and silently substituting Interrupt
  Number or another neighboring byte is not authorized.
- `Functionality|708|Wistron-BIOS-00376-V002` — decide whether the case
  validates whole SMM TSEG range coverage, as the title states, or absence of
  `SmiHandler4` in a debug SOL trace, as the procedure and criteria state.
  Align the source fields; define either the exact TSEG base/limit/range
  calculation or the handler stimulus/evidence contract; and supply a
  compatible debug BIOS plus rollback, read-only AMI RU/IO `0xB2`, SOL and OOB
  recovery procedure. No debug flash or undocumented register operation is
  authorized until this semantic and safety decision is resolved.
- `Functionality|713|Wistron-BMC-00003-V008` — define the exact BMC firmware
  upgrade/downgrade version pair and order, and clarify the criterion `after
  BMC reset only one time`: identify the reset initiator, whether an automatic
  WebUI activation reset counts, the allowed count/timing per transition, and
  the expected result plus rollback/recovery for both directions. No image
  upload, firmware write, retry or extra reset is authorized until this
  destructive-operation contract is deterministic.
- `Functionality|714|Wistron-BMC-00004-V007` — define the exact Redfish BMC
  upgrade/downgrade version matrix and order, resolve the required host power
  state and `only one` reset/apply semantics, and provide the target's
  advertised/vendor-approved UpdateService action URI, payload/content type and
  task/failure contract. Replace the embedded root credential and `curl -k`
  pattern with approved secret and trusted-CA handling, and supply tested
  rollback/OOB recovery. The source PATCH/POST/GET are not authorized meanwhile.
- `Functionality|718|Wistron-BMC-00008-V007` — resolve the source's booted-host
  requirement against the same-row DeepSeek risk instruction to power the host
  off. Define the exact FPGA upgrade/downgrade matrix and order, the initiator,
  timing and allowed count behind `BMC reset only one time` for each transition,
  and the target-advertised/vendor-approved FPGA update action, payload, task and
  activation contract. Replace embedded credentials and `curl -k`, and supply a
  tested FPGA/BMC/host recovery path. No write or reset is authorized meanwhile.
- `Functionality|720|Wistron-BMC-00010-V007` — correct the destructive target:
  Items and Script identify HIB-CPLD, while Procedure explicitly says FPGA.
  Then define the component image/version/order, reconcile booted versus powered-
  off host state, define the sole BMC reset, and provide the advertised Redfish
  action/task/activation, secure authentication and tested recovery contract.
  No firmware write or reset is authorized while these conflicts remain.
- `Functionality|722|Wistron-BMC-00012-V008` — correct the destructive target:
  Items and Script identify DCSCM-CPLD, while Procedure explicitly says FPGA.
  Define a component selector and signed image/version order, reconcile booted
  versus powered-off host state, define the sole BMC reset, and provide the
  vendor Redfish action/task/activation, secure authentication and a recovery
  route that does not depend only on the updated DCSCM. No write is authorized.

Per-case project inputs, private specifications, tool manuals, target maps,
expected values, parameters, overrides, safety limits, and recovery owners are
tracked in the applicable independent review record. They are execution
readiness inputs and do not become new Master Library policy.

If a later row exposes a genuine rule contradiction that affects multiple
cases, record its exact source facts, affected source keys, safety impact, and
the decision needed here. Do not infer or apply a new global rule.
