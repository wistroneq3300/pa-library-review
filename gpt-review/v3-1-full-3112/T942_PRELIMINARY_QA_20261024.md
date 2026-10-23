# T942 Preliminary Source Audit / Impact (2026-10-24)

**NOT INDEPENDENT QA ACCEPTANCE. NOT A 942-CASE RE-REVIEW.**

## Verified snapshot

Repository `wistroneq3300/pa-library-review`, baseline branch `codex/testcase-review-v3-1-full-3112`, completion commit `411e3381f961bce52bf7db0e2b9d1a9306dfab6f`, report commit `3062b95be2486f46f1745ec994235750a7149d2e`.

The repository's existing `FINAL_SUMMARY.md` and `PROGRESS.json` report 3112/3112 REVIEW COMPLETE, 942 case-level pending engineering questions, 927 SOURCE_CONFLICT and 214 BLOCKED. Prior Validator PASS is a reported baseline, not a Validator run performed for this triage.

## Direct original XLSX audit

`data/REVISED_commands_merged_with_raw.xlsx` was decoded as an XLSX workbook and the exact **physical sheet row** was reopened for every T942-01..10. Each row's A (Code), D (Items), E (Procedure) and F (Criteria) was checked against the question context. **10/10 matching Source Key + physical row + code**. This supports the decision-register source claims, but is not a comparison against all 942 case overlays.

Key findings:
- Compatibility row130 RAID0 explicitly conflicts with embedded RAID1/5 rebuild steps and Criteria; retain coverage delta.
- Stability row71 has a normative Reboot 500 times title and a 12h Procedure but no warm/cold operation; project selection still required.
- Functionality row1436's Procedure contains a BIOS WebUI version read, not a flash action, although Criteria references before/after flash. User-chosen full flash is explicitly expanded scope, not source-equivalent evidence.
- Functionality row2237's literal Procedure and Criteria test WebUI login after Refresh/F5; KVM persistence is an Items-driven extra checkpoint that requires different visual evidence.
- Compatibility row100's Present LED insertion does not prove the stated Rebuild LED.
- Functionality row2273 has RetinaNet Offline command but stray Training/BERT text.

## Read-only candidate scan, not disposition

The 942-item `ENGINEERING_DECISIONS_PENDING.md` list was checked with descriptive theme words for only T942-01..10. **115 unique entries** are potential follow-up review candidates (some match multiple themes). This is intentionally a **candidate count only**: it does not validate relevance, resolve decisions, reclassify tests, or justify a batch template edit. A separate direct-XLSX per-case review is mandatory.

## Next QA gate

1. Collect pending T942-11..30 user selections; add their justified rules to the supplement and their case-specific decisions to a separate register.
2. Read each of the 942 unique Source Keys in the real workbook and inspect current/historical review records, including full intent, command semantics, safety, Expected, and coverage.
3. Record original→proposed outcome independently per case, keep conflicts distinct from execution readiness, and do not auto-clear an undecided item.
4. Validate any proposed effective changes with existing case-level and full-review validators and protected-source hashes.
5. Apply ED-QA-01 312-case 10% blind independent QA sample plus risk-expansion ED-QA-10 before claiming QA ACCEPTED.
6. Retain legacy duplicate-key and anti-template candidates for specific QA. No Merge or Force Push.

## Operations performed in this triage

Only additive text documents on `codex/ed-triage-policy-20261024`. No Master XLSX/JSON, original V3.1 logic, original protected records, PROGRESS, classification, conflict count or pending queue has been changed. No hardware tests.
