# V3 to V3.1 Changelog

Date: 2026-10-13

## Added

- Shared Master Library versus Project Test Plan separation.
- Explicit Master Default, Project Inputs, Approved Override, Actual Execution,
  Coverage Difference, and Engineer Verdict fields.
- Project-run completion semantics: approved reduced scope may complete the
  project run without completing the original master default.
- Attended/Machine Time treatment as planning reference unless both fields are
  explicitly normative requirements.
- Separate automation capability, readiness, manual activity, user input, and
  safety-approval dimensions.
- Single-authorized-engineer approval without an invented dual-signoff policy.
- Existing project validation tool/PA Manager Cycle preference with mandatory
  coverage mapping.
- Original Method plus separately versioned Modernized Recommendation.
- Official tool-default disclosure and confirmation requirement.
- Platform-specific Expected and historical-PASS equivalence controls.
- Run-level approval, continue-on-error, immutable failure evidence, and no
  automatic retry.
- Package-installation impact/rollback disclosure.
- Engineer-owned formal PASS/FAIL/BLOCKED verdict.
- Explicit InfiniBand/RoCE/Ethernet mode selection.

## Corrected from V3

- A Procedure-versus-Machine-Time mismatch is no longer automatically a
  blocking `SOURCE_CONFLICT`; both values are retained and the project plan
  resolves execution unless both are normative.
- Missing project Expected, firmware version, device count, package, path, or
  runtime no longer implies permanent BLOCKED when intent and safe execution
  boundary are identifiable.
- Human parameter/specification supply is not itself partial automation.
- Manual setup plus automated execution is explicitly hybrid; core visual
  acceptance remains manual.
- A tool's successful exit is not testcase completion without coverage proof.
- V3 recovery language is constrained: recovery and retry require approval,
  and failed evidence is immutable.

## Preserved

- Exact-XLSX-row reread and one-case atomic review.
- Four formal automation classifications.
- Source/history immutability and case-variant identity.
- Intent, duration, iteration, target, evidence, safety, and recovery
  preservation.
- Storage, firmware, GPU/BDF, network-management, I2C/I3C, power, and
  environmental safety invariants.
- `SOURCE_CONFLICT` for genuine contradictory normative intents.
- No DUT execution and no agent-owned formal testcase verdict.

## Migration boundary

V3 records remain historical. V3.1 records are new overlays under
`gpt-review/v3-1/`; no V3 record is edited or silently backfilled.
