# Agent Understanding Final Validation

## Boundary

- 38 cases were selected: every classification correction, every conflict-flag
  correction, all changed high-risk margin/storage/firmware cases, and
  representative BLOCKED, FULLY AUTOMATABLE, MANUAL ONLY and KEEP cases.
- Cards contained only the effective test contract: intent, target, method,
  inputs, override boundary, safety, evidence, stop/retry and verdict owner.
- No DUT or command execution occurred.
- Model status: **SAME_MODEL_FAMILY_CONTEXT_SEPARATED**. The audit environment
  cannot prove a cross-model or human-independent validation, so this is not
  represented as independent external proof.

## Selected cases

`2, 14, 19, 45, 51, 52, 53, 54, 69, 70, 74, 76, 96, 122, 145, 162, 166,
170–181, 183, 186–189, 193, 197, 199, 200`

## Understanding result

All 38 context-separated cards preserved:

- the row-specific function under test and actual target;
- immutable Master requirement versus a separately approved Project Override;
- original method and any conditional recommendation without substitution;
- missing inputs and non-waivable storage, thermal, power, RAS and firmware
  restrictions;
- case-specific raw evidence and safety-stop conditions;
- no automatic retry and immutable first-failure evidence;
- engineer ownership of formal PASS/FAIL/BLOCKED.

Specific challenge results:

- Seq 51/52/53/70/74 did not accept Redfish/IPMI or screenshot analysis as a
  replacement for direct WebUI observation.
- Seq 170–181 separated operator setup from the automated core without giving
  the agent chamber, rail, target-selection or emergency-stop authority.
- Seq 182 was not auto-reclassified because repeated AC removal is the core
  source action until fixture equivalence is approved.
- Seq 19/162/186/199/200 remained semantically blocked while false
  `SOURCE_CONFLICT` labels were removed.
- Seq 14/122/193 retained exact storage target protection.
- Seq 197 retained downgrade/anti-rollback and per-hop recovery.

Result: **38/38 understanding replay PASS; independence level SAME_MODEL_FAMILY,
not cross-model, not hardware validation.** Independent user/ChatGPT review is
still recommended before scaling to 2,912 cases.

