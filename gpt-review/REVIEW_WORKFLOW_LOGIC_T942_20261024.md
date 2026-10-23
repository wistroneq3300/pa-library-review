# T942 Engineering Triage Review Logic Supplement (2026-10-24)

Status: APPROVED FOR REVIEW GUIDANCE ONLY, T942-01 through T942-10. T942-11 through T942-30 remain unapproved questions.

## Authority, provenance and numbering

This is an additive V3.1 review-logic supplement, not a rewrite of the protected V3.1 baseline. It records the user's decisions provided on 2026-10-24 for the pending 942 engineering-decision cases. To avoid collision with previously approved ED-01 through ED-52 and ED-QA-01 through ED-QA-10, the user's first round ED-01 through ED-10 is indexed here as T942-01 through T942-10.

Read the exact source XLSX row (sheet, physical row and code), DeepSeek/GPT historical evidence and current V3.1 review record independently for every affected testcase. Precedence: immutable original source and provenance; explicit source-specific user decision as an approved **review-layer/project overlay**; existing V3.1/ED safety and lifecycle constraints; documented platform/tool facts. New guidance may resolve a project interpretation but never silently change the master source or erase the contradiction. Keep Source Key and Case Variant ID stable.

This supplement applies only to review planning. It does not approve execution or establish DUT PASS/FAIL, QA ACCEPTED, a firmware image, an arbitrary expected threshold, destructive target, host password, management session, or permission to mutate hardware. Review complete, engineering decision, execution readiness, actual execution, raw tool results and engineer verdict remain separate.

## Generalizable rules newly affirmed

1. **Purpose vs conflicting procedure** (T942-01, T942-04, T942-10): where user approves a clearly stated test purpose, produce a separate corrected review-layer proposal anchored to that purpose. Preserve original Procedure/Criteria verbatim and a full coverage-delta/source-conflict note. Do not fabricate an expected value or claim the original contradictory requirement was fulfilled.
2. **Source identity collision** (T942-02): a duplicate human-readable Test Code is never grounds to merge materially different physical XLSX rows. Preserve each Source Key and Variant ID independently. Changing the master code requires independent library-owner authority.
3. **Standards-based draft, not unauthorized execution** (T942-03): a public, exact-version technical standard may support a labeled test-command draft when the source lacks request bytes. Validate platform/firmware scope, request/response schema, semantic side effects, pre-state, restore and acceptance. If core operation semantics remain unknowable, retain BLOCKED. Missing project parameters alone remain execution-readiness inputs. A draft is NOT a runnable command authorization.
4. **Destructive I/O remains non-waivable** (T942-01, T942-04, T942-09): review-layer FIO/RAID proposals may be written without a target. Execution requires independently verified disposable identity/serial/path, no OS/boot/mounted/RAID/user-data/unknown target, bounded profile, approved data-loss scope, backed-up evidence and recovery. Never copy a source placeholder `/dev/nvme*` into an executable target.
5. **Transport and reset are not interchangeable** (T942-05, T942-06): separate Ethernet, InfiniBand and RoCE by path/port/threshold/evidence, and warm OS reboot, DC/host power cycle, AC power removal by exact reset class. A chosen project subset may be executed only with scope/coverage delta; no substitute is silently marked complete.
6. **Distinct acceptance checkpoints** (T942-05, T942-08, T942-09): one preserved source row may have separately tracked child checkpoints for mutually different test functions (e.g. Ethernet vs IB; WebUI login vs KVM session; Present LED vs Rebuild LED). Child checkpoints are not new master rows or duplicate keys. Track each phase's observable acceptance and whether a human must observe it.
7. **Explicit flash ownership** (T942-07): the user approves this exact source case's review-layer plan covering a full BIOS flash transaction plus WebUI before/after BIOS version checks. Source Procedure itself only specifies WebUI version check; keep this expansion conspicuous as an approved case-specific overlay, not a generic requirement for all version-view cases. Keep the separate same-code upgrade variant distinct, detect overlapping flash ownership, and require approved image/device compatibility, version/direction/active-staged readback, activation/reboot, power safety, rollback/OOB recovery and fresh explicit run authorization. No automatic flash.
8. **UI/visual evidence ownership** (T942-08, T942-09): human-visible WebUI/KVM session, rendered status and physical LEDs require qualified direct observation/evidence. Backend API, IPMI and logs may corroborate but never substitute unless separately documented equivalent coverage is formally approved. In this no-DUT review, nothing was operated or observed.
9. **Benchmark identity and reference** (T942-10): distinguish MLPerf Inference RetinaNet Offline from BERT, MLPerf Training, alternative scenarios and other versions. A benchmark command alone does not validate dataset, harness, compliance, latency/throughput reference or engineer verdict.
10. **No keyword-based disposition**: first perform a read-only impact candidate scan if useful, then reopen and review each testcase individually. Never auto-clear the 942-item queue by regex, group label or A/B/C similarity. Keep 927 source conflicts and 214 blocked cases until independently resolved by recorded evidence and validated transition.

## Re-review/QA gates

- Read actual source workbook row and all available legacy review evidence for each case.
- Log source facts, the exact T942 policy applied, old/new recommended plan, original coverage, residual blocker/readiness issue, retained conflict and the engineer-specific question if still needed.
- If approved guidance does not settle an ambiguous primary purpose or operation, keep ENGINEERING DECISION PENDING.
- Never mutate protected XLSX/JSON/master/test manifest/locked Final Audit; put new recommendations and correction records in an additive overlay.
- A change to an effective review record requires isolated provenance, case-level validator, whole-review integrity validation and affected-scope independent QA as defined by ED-QA-01 through ED-QA-10.
- Do not mark QA ACCEPTED without the separate approved 312-case 10% blind sample and risk-driven expanded sampling. Preserve 16 known duplicate-key warnings and 2 anti-template candidate groups in QA scope.
- No Merge, Reset or Force Push. Stop with an explicit handoff when required project or safety authority is missing.

Case-bound decisions and unresolved inputs: `gpt-review/v3-1-full-3112/T942_DECISIONS_APPROVED_20261024.md`.
Preliminary source audit: `gpt-review/v3-1-full-3112/T942_PRELIMINARY_QA_20261024.md`.
