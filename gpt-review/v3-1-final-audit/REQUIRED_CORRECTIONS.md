# Required Corrections Applied

## Applied

1. Added ED-30 and ED-31 while preserving ED-01–ED-28 and the absent ED-29 gap.
2. Added additive overlay retention and precise `SOURCE_CONFLICT` semantics to
   the V3.1 logic.
3. Corrected 17 automation classifications: five core WebUI cases to
   `MANUAL ONLY`, twelve manual-setup/automated-core cases to
   `REQUIRES PACKAGE / USER CONFIRMATION`.
4. Removed ten false `SOURCE_CONFLICT` flags without deblocking any unsafe or
   semantically undefined case.
5. Restored Seq 51's two required WebUI views.
6. Corrected the Seq 19 blocked-summary domain error in the audit overlay.
7. Refreshed modernization evidence against current official public sources
   while retaining installed-version and project applicability gates.

## Resolved after the Final Audit

- Seq 182 is now formally `MANUAL ONLY` under ED-32. Its ten source-defined
  physical AC cable removals may not be replaced by PDU control, BMC power off,
  software reboot, or another remote action. The agent may assist with approved
  stress preparation, evidence collection, and reporting without claiming the
  physical action.

## Pending, not hidden

- Private-tool cases still need applicable manuals/SOPs and installed versions.
- Project SPEC, target, limits, Expected, overrides and recovery remain per-case
  execution inputs.
- Cross-model/human-independent Agent Understanding validation is not available
  in this audit environment; same-model-family status is explicitly labeled.

## Historical preservation

The original V3.1 records and reports were not overwritten. Final Audit records
carry Before/After/Reason and act as the release-candidate correction overlay.
