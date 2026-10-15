# Engineering Decisions Pending

The 2026-10-15 rulings ED-33 through ED-52 resolve the earlier review-level
questions for their named variants except BIOS 00376. Project images, versions,
SPEC values, parameters, tool packages, environments, safety approval and
recovery remain per-case execution-readiness inputs; they are not global
engineering-decision blockers.

## Case-level decision pending

- `Functionality|708|Wistron-BIOS-00376-V002` — **ENGINEER DECISION PENDING**.
  Decide whether the testcase validates whole SMM TSEG range coverage or the
  absence of `SmiHandler4` in a debug SOL trace. Align the title, procedure and
  criteria; define the exact range/register model or handler stimulus/evidence;
  and approve any debug BIOS, read-only register/SOL method, rollback and OOB
  recovery. No debug BIOS flash or unapproved register operation is authorized.

See `ENGINEERING_DECISIONS_APPROVED_20261015.md` and
`RETROSPECTIVE_IMPACT_20261015.md` for applied decisions and affected records.
