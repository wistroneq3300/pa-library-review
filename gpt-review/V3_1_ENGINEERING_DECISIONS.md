# V3.1 Engineering Decisions 01–28

Authority: the user's 2026-10-13 V3.1 task handoff. The repository does not
contain the original text of questions 01–28. The IDs below preserve the
confirmed decisions conveyed by this handoff; the unavailable original
question wording is explicitly unresolved and is not claimed as GitHub
history.

## Decision register

### ED-01 — Shared Master Library

- Scope: all 3,112 Server SIT/GPU Server SIT rows.
- Decision: the library is shared master content, not one project's fixed run.
- Rationale: project applicability and values vary by platform.
- Rule type: general.
- Impact: all 200 cases and future reviews.
- Unresolved: original Question 01 wording is not available.

### ED-02 — Preserve master provenance

- Decision: preserve original intent, procedure, command, tool, parameters,
  criteria, timing, and source provenance.
- Rationale: project execution must remain auditable against the source.
- Rule type: general; impacts all cases.
- Unresolved: none beyond unavailable original question wording.

### ED-03 — Project Test Plan ownership

- Decision: engineers bind applicable platform/devices, method, tool, runtime,
  loop count, expected values, coverage, and approved overrides.
- Rationale: these are project facts, not global constants.
- Rule type: general; impacts all cases with platform/run inputs.
- Unresolved: project values remain pending per testcase.

### ED-04 — Missing project values are not permanent blockers

- Decision: absent project Expected, firmware version, device count, path, or
  runtime does not alone cause permanent BLOCKED.
- Rationale: readiness and capability are separate.
- Rule type: general; impacts V3 BLOCKED/NEEDS_SPEC cases.
- Unresolved: irreducible intent/target/safety ambiguity remains BLOCKED.

### ED-05 — Approved override and coverage

- Decision: record master default, approved override, Actual, coverage delta,
  execution status, and engineer verdict separately.
- Rationale: a 100-loop approved run can complete without satisfying a 500-loop
  master default.
- Rule type: general; impacts cycle/stress/duration cases.
- Unresolved: each project supplies its approved override.

### ED-06 — Never overwrite master with override

- Decision: project override is an overlay, not a source edit.
- Rationale: preserve cross-project reuse and provenance.
- Rule type: general; impacts all overridden cases.
- Unresolved: none.

### ED-07 — Machine/attended time interpretation

- Decision: treat timing fields primarily as planning/work estimates.
- Rationale: project duration/iteration is engineer-selected.
- Rule type: general; impacts V3 timing-conflict cases.
- Unresolved: identify rows where both fields are explicitly normative.

### ED-08 — Genuine timing conflicts only

- Decision: do not auto-block because Machine Time differs from Procedure;
  preserve both. Use conflict only when both are formal requirements.
- Rationale: avoid false SOURCE_CONFLICT.
- Rule type: general.
- Unresolved: project selection where source does not establish precedence.

### ED-09 — Five automation dimensions

- Decision: separate capability, readiness, manual activity, required inputs,
  and safety approval while retaining the four formal classes.
- Rationale: one label cannot represent all execution state.
- Rule type: general; impacts all cases.
- Unresolved: future PA Manager field mapping.

### ED-10 — Input supply is not partial activity

- Decision: an engineer supplying a SPEC/parameter or pressing OK does not make
  the underlying test partially automated.
- Rationale: input ownership differs from execution activity.
- Rule type: general; impacts SPEC/parameter/approval-gated cases.
- Unresolved: none.

### ED-11 — Hybrid physical setup

- Decision: cabling, environment, or fixture setup followed by automated tool
  execution is hybrid/partial.
- Rationale: manual setup and automated core execution must both be visible.
- Rule type: general; impacts network, fixture, hot-plug and environment cases.
- Unresolved: per-case setup/evidence boundary.

### ED-12 — Core visual acceptance

- Decision: UID/LED/WebUI visual acceptance remains MANUAL ONLY when human
  observation is the core criterion; agent commands/logs are assistance.
- Rationale: telemetry cannot prove the observed interface state.
- Rule type: general; impacts LED/WebUI cases.
- Unresolved: project may later provide qualified machine-vision/UI automation.

### ED-13 — Single authorized operator approval

- Decision: one authorized engineer may approve a complete defined run; do not
  invent dual review/signoff.
- Rationale: avoid unsupported company process.
- Rule type: general.
- Unresolved: external project mandates override when documented.

### ED-14 — Approval does not waive safety

- Decision: retain target identity, impact scope, storage protection, safety,
  recovery, and explicit execution approval.
- Rationale: authorization cannot make an unidentified target safe.
- Rule type: general; impacts destructive/disruptive cases.
- Unresolved: per-project recovery owners.

### ED-15 — Existing validation tool first

- Decision: prefer PA Manager Cycle, project scripts, approved GPU diagnostics,
  vendor tools, and existing stress scripts when applicable.
- Rationale: avoid duplicate or conflicting control logic.
- Rule type: general; impacts cycle/diagnostic/stress cases.
- Unresolved: tool inventory/version per project.

### ED-16 — Tool coverage must be proven

- Decision: successful tool execution is not testcase completion; map tool
  coverage to approved Test Plan requirements.
- Rationale: prevent false completion.
- Rule type: general.
- Unresolved: per-tool coverage matrices.

### ED-17 — Preserve original; separate modernization

- Decision: retain original method and provide a verified modern method only
  as a separate recommendation.
- Rationale: modernization must not erase provenance or redefine the test.
- Rule type: general; impacts cases with legacy commands/tools.
- Unresolved: some original methods need platform-specific support checks.

### ED-18 — Modern recommendation evidence

- Decision: record tool/method, platform, supported version, official source,
  difference, coverage delta, inputs, risks, and limitations; do not invent.
- Rationale: recommendations must be reproducible and scoped.
- Rule type: general.
- Unresolved: private tool documentation may remain unavailable.

### ED-19 — Do not replace the function under test

- Decision: Redfish cannot alone complete a WebUI-display test; alternative
  telemetry is supporting evidence unless the project changes scope.
- Rationale: observation path may itself be the tested feature.
- Rule type: general; impacts WebUI/serial/LED/interface cases.
- Unresolved: explicit project-scope changes remain engineer decisions.

### ED-20 — Official tool defaults need confirmation

- Decision: a documented default is only a candidate after tool-version,
  applicability, functional-impact, and safety review and user confirmation.
- Rationale: defaults can change coverage or risk.
- Rule type: general; impacts benchmark/stress/vendor-tool cases.
- Unresolved: installed tool versions and selected defaults.

### ED-21 — Storage safety is non-waivable

- Decision: identify exact write target and exclude OS, active, data, evidence,
  recovery, and unknown devices; do not unmount/format/reconfigure to bypass.
- Rationale: an OK cannot cure target ambiguity.
- Rule type: general; impacts fio/dd/storage/GDS.
- Unresolved: project allowlists and data ownership.

### ED-22 — Platform-specific Expected

- Decision: GPU/PCIe/NVLink/sensor/FW/device-count Expected values are bound to
  approved platform/configuration specs; Actual never becomes Expected.
- Rationale: master rows span platforms.
- Rule type: general; impacts topology/inventory/performance cases.
- Unresolved: applicable specifications per project.

### ED-23 — Historical PASS as controlled reference

- Decision: a historical PASS report may be a reference only after
  platform/version/configuration equivalence and engineer approval.
- Rationale: prevent circular or cross-platform acceptance.
- Rule type: general.
- Unresolved: equivalence criteria and report provenance.

### ED-24 — Source conflict and project resolution

- Decision: preserve original contradictions; a project decision controls only
  the current run and does not merge/delete/fix the master permanently.
- Rationale: project resolution is not source correction.
- Rule type: general; impacts SOURCE_CONFLICT cases.
- Unresolved: master-library owner may later issue formal source revisions.

### ED-25 — WebUI/manual operating boundary

- Decision: engineers operate WebUI; agent explains, analyzes screenshots/logs,
  organizes evidence, and identifies omissions without claiming observation.
- Rationale: preserve truthful evidence ownership.
- Rule type: general; impacts WebUI and visual cases.
- Unresolved: none for this no-DUT review.

### ED-26 — Continue on ordinary error; no automatic retry

- Decision: record ordinary warnings and continue approved collection; stop for
  safety/data/control conditions; never add retry or overwrite first failure.
  A scheduled next loop is not a retry.
- Rationale: preserve failure evidence and avoid masking defects.
- Rule type: general; impacts stress/cycle/fault cases.
- Unresolved: project-specific safety-stop thresholds.

### ED-27 — Run-level approval, recovery, installation

- Decision: one approval covers the unchanged run; reapprove changes, extra
  recovery/retry, installs, or system mutation. Installation proposals must
  disclose source/version/dependencies/command/impact/rollback; no independent
  driver/kernel/FW changes.
- Rationale: bounded authorization and reversible dependency handling.
- Rule type: general.
- Unresolved: project package repository and rollback capability.

### ED-28 — Engineer verdict, network modes, and private tools

- Decision: the agent preserves raw tool PASS/FAIL but the engineer owns the
  formal verdict; IB, RoCE, and Ethernet are distinct project-selected modes;
  WAT/NVDiag/NVQual and vendor tools use applicable manuals/SOPs and ambiguous
  semantics are never guessed.
- Rationale: preserve decision authority, transport scope, and vendor safety.
- Rule type: general with case-specific network/tool bindings.
- Impact: all execution reports; network and vendor-tool cases.
- Unresolved: the original Question 28 wording, selected network mode, and
  private-tool documentation/version per project.

## Explicit carry-forward decisions

- PA Manager Cycle and existing project scripts take precedence over new cycle
  control logic when coverage is adequate.
- Original commands remain recorded even when a modern method is recommended.
- No automatic retry, no agent-owned formal verdict, no dual-signoff invention,
  and no DUT execution are authorized by this review.
