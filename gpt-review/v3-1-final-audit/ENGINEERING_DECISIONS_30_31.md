# Engineering Decisions 30 and 31

Authority: the user's 2026-10-13 Final Audit handoff. Decision 29 was not
provided and is not invented.

## ED-30 — Manual setup plus automated execution

- Formal capability: hybrid/partial automation.
- Canonical JSON: `REQUIRES PACKAGE / USER CONFIRMATION`.
- Manual setup includes chamber, voltage/rail, fixture, cabling, population and
  other physical preconditions. The setup, calibration, safety interlocks and
  emergency stop remain operator-owned.
- The classification changes only when the subsequent core workload,
  monitoring and evidence collection are machine-executable. A repeated
  physical operation that is itself the test is not automatically hybrid.
- Individually applied to sequences 170–181. Sequence 182 is not batch-changed:
  the source calls for ten AC removals and requires an engineer to approve an
  automated fixture as equivalent coverage before hybrid classification.

## ED-31 — WebUI sensor/manual observation

- Formal capability: `MANUAL ONLY` when the core acceptance is the rendered
  BMC WebUI page, displayed sensor value, label, link, navigation or visible
  state.
- The agent may explain, analyze supplied screenshots/logs, correlate IPMI or
  Redfish and organize evidence. Backend data cannot substitute for the WebUI
  function under test, and AI screenshot analysis does not transfer formal
  observation ownership.
- Individually applied to sequences 51, 52, 53, 70 and 74.
- Sequences 8, 81, 84, 90 and 153 remain hybrid because substantive,
  independent cross-interface collection is part of their original scope;
  their WebUI phase remains human-owned.

The full register was updated in
`gpt-review/V3_1_ENGINEERING_DECISIONS.md` without changing ED-01–ED-28.

