# PA Manager Compatibility Report

## Read-only baseline

- Repository: `https://github.com/wistroneq3300/pa-cycle-lab`
- Branch: `codex/platform-premium-ui-v1`
- Inspected commit: `3ce4b9c6e5467abe9d27050e5af0240b07fff3dc`
- Inspection mode: separate temporary read-only clone; working tree remained clean.
- Modification performed: **none**.

Relevant inspected files include `app/test_library_contract.py`, `integration/agent_runs.py`, `integration/agent_gateway.py`, `app/static/js/engineering-ux.js`, `app/static/js/app.js`, `HANDOFF.md` and the existing cycle validation implementation.

## Compatibility conclusions

| Requirement | Current behavior | V3.1 finding |
|---|---|---|
| Preserve Original Procedure | `procedure` and `criteria` remain source fields; UI shows the original work order separately. | Compatible. V3.1 recommendation must remain an additive display section and must never write `procedure`. |
| Preserve `ai_review` | Full nested `ai_review` is carried into immutable `AgentRunContext`. | Compatible as a legacy review, but V3.1 should be a versioned additive overlay rather than destructive replacement. |
| Preserve `case_variant_id` | `prepare_library()` calculates it from the row payload; merged-review derived UI fields are excluded, but review payload changes still affect the hash. | **Platform change required before importing V3.1.** Adding/changing review data in the hashed row can churn identity. Join V3.1 after identity calculation or exclude the versioned overlay from the identity payload and regression-test all 3,112 IDs. |
| Agent assignment | Assignment uses `case_variant_id`; duplicate `code` values require explicit variant identity. | Compatible. Never join V3.1 by `code` alone; use variant plus `source_ref` integrity. |
| Immutable run snapshot | `AgentRunContext` stores testcase and `ai_review` once, with a context hash. | Good foundation; context schema must be versioned to include V3.1 plan/approval/evidence fields. |
| Engineer-owned verdict | Runtime status uses DONE/ERROR/WAITING rather than equating gateway completion with PASS/FAIL. | Compatible and aligned with V3.1. Tool output status must remain raw evidence. |
| Existing cycle control | PA Manager already implements cycle validation, pre/post checks and immutable attempt evidence. | Compatible. V3.1 should reference the existing engine rather than add another loop controller. |

## Required additive data contract

Recommended versioned object, stored outside the identity hash or joined after `case_variant_id` is frozen:

```json
{
  "review_schema_version": "v3.1",
  "review_provenance": {
    "source_key": "sheet|row|code",
    "source_xlsx_sha256": "...",
    "logic_version": "V3.1",
    "record_sha256": "..."
  },
  "automation_capability": "FULLY AUTOMATABLE | REQUIRES PACKAGE / USER CONFIRMATION | MANUAL ONLY | BLOCKED",
  "execution_readiness": [],
  "manual_test_activity": "...",
  "required_user_inputs": [],
  "safety_approval": {
    "required": true,
    "target_identity": [],
    "impact_scope": "...",
    "storage_protection": [],
    "safety_checks": [],
    "recovery_requirements": []
  },
  "master_defaults": {},
  "project_plan": {},
  "approved_override": {},
  "actual_execution": {},
  "coverage_difference": "...",
  "original_method_ref": "procedure",
  "modernized_recommendation": {
    "method": "...",
    "applicable_platform": "...",
    "supported_version": "...",
    "official_references": [],
    "difference_from_original": "...",
    "coverage_difference": "...",
    "required_inputs": [],
    "risks_limitations": []
  },
  "evidence_contract": [],
  "retry_policy": "NO_AUTOMATIC_RETRY",
  "engineer_verdict": null
}
```

### Field mapping

| Existing PA Manager field | V3.1 treatment |
|---|---|
| `procedure` / `criteria` | Retain verbatim as Master source. Never populate from a recommendation. |
| `ai_review.automation_classification` | May continue as the capability class for legacy UI; add separate readiness/manual/input/safety fields. |
| `ai_review.test_command` | Treat as reviewed prose, not a pasteable command. V3.1 execution plan must be approved per run. |
| `ai_review.pre_check_commands` / `post_check_commands` | Reuse as legacy guidance; V3.1 adds target-specific safety and evidence contracts. |
| `ai_review.openhands_instruction` | Keep for compatibility; gateway should assemble V3.1 fields explicitly instead of compressing them into one prose string. |
| `ai_review.end_user_decides` | Map to unresolved project decisions; do not treat as approval. |
| `case_variant_id` | Immutable identity. V3.1 join must not recompute or replace it. |
| AgentRun `approvals_json` | Extend to a signed run-level plan snapshot: target, method, parameters, destructive scope, stops, recovery and retry authorization. |
| AgentRun `commands_json` / `evidence_json` | Keep append-only; add attempt/loop identity so failed attempts cannot be overwritten. |
| `final_result` | Store agent completion/raw result separately from engineer verdict. |

## Agent Gateway changes required

1. Pass the versioned V3.1 object and approved project plan into the immutable AgentRunContext.
2. Gate execution on both capability and readiness; classification alone is insufficient.
3. Preserve Master defaults, approved override and Actual as different objects.
4. Enforce one approval for a fully specified run, then re-prompt only on target/command/important parameter/destructive scope/recovery/retry/installation changes.
5. Represent planned loops separately from retries; do not auto-add attempts.
6. Keep tool PASS/FAIL as evidence and reserve formal testcase verdict for the engineer.
7. Select existing PA Manager Cycle/project scripts before asking an agent to generate a new controller.
8. For packages, surface source/version/dependencies/install command/system impact/rollback and wait for confirmation.
9. Preserve original failures and append later authorized attempts.

### Current MANUAL ONLY policy mismatch

The current gateway instructs MANUAL ONLY cases to avoid all DUT commands. V3.1 needs a finer distinction:

- `manual_test_activity`: the core acceptance that remains human (for example UID LED visual confirmation or WebUI observation).
- `agent_assistance_allowed`: bounded supporting commands, log collection or evidence analysis.

Without this split, a case whose formal result is MANUAL ONLY cannot use safe agent assistance even when engineering explicitly approves it. The platform should not reclassify the case as partial merely to permit assistance.

## Test Case UI changes required

- Keep the current Original Procedure/Criteria section unchanged.
- Add separate sections for V3.1 capability, execution readiness, manual activity, missing inputs and safety approval.
- Display Master Defaults, Project Plan/Override, Actual Execution and Coverage Difference as four visually distinct blocks.
- Display Original Method and Modernized Recommendation side by side; show official references, applicability and version.
- Add a run-level approval summary and change-detection banner.
- Show “Agent result” separately from “Engineer verdict.”
- For WebUI/manual cases, provide evidence upload and screenshot/log analysis without implying the agent performed the observation.

## Execution-flow changes required

1. Resolve `case_variant_id` and source provenance.
2. Load legacy `ai_review` plus V3.1 overlay without changing identity.
3. Resolve project documents and expected/platform inputs.
4. Build a versioned run plan with target, method, parameters, duration/loops, safety stops, evidence and recovery.
5. Obtain one explicit run-level approval.
6. Dispatch only the approved scope through the existing execution/cycle path.
7. Continue on ordinary warnings according to plan; stop on safety/data/control triggers.
8. Never add a retry automatically.
9. Append raw evidence and Actual; calculate coverage difference.
10. Finish AgentRun without assigning the engineer's PASS/FAIL/BLOCKED.

## Compatibility gate

- Original Procedure overwrite: PASS — current design can keep it separate.
- `case_variant_id` stability without platform work: **FAIL / modification required** before V3.1 ingestion.
- Existing `ai_review` survival: PASS with additive overlay.
- PA Agent assignment flow: PASS if variant identity remains frozen.
- V3.1 field delivery to Agent: **PARTIAL / schema and gateway changes required**.
- PA Manager repository modified by this task: PASS — no.
