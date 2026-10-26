# Invalid Run Notice — Formal Queue 0436–0600

- Detection date: 2026-10-27 (Asia/Taipei).
- Last valid checkpoint: formal queue 0435, review event 0586, commit `fc3bbbcb`.
- Invalid affected range: formal queue 0436–0600, review events 0587–0751, 165 records.
- Reason: the affected overlay files were written through a mechanical generator. This violates the GPU Server SIT review rule that each XLSX row, matching DeepSeek record, command fit, evidence, safety, recovery and disposition must be freshly reasoned and written one testcase at a time without a generator, classifier, range rule, copy-forward template or bulk-writing script.
- Validator limitation: schema, identity, count, protected-source and exact-duplicate checks passed, but those checks do not prove independent reasoning and therefore did not cure the process violation.
- Preservation: the exact affected files are retained under `INVALIDATED_REVIEW_RECORDS/20261027_GENERATOR_0436_0600/`; they are audit history only and are excluded from the active overlay.
- Active state restoration: `PROGRESS.json` and the session handoff are restored to formal queue 0435. Re-review resumes at the directly verified XLSX/manifest identity `Functionality|2273|Wistron-HW-00475-V002` / `0167355737b887af`.
- Protected inputs: `data/REVISED_commands_merged_with_raw.xlsx`, `data/tests.json`, `data/tests_gpt_merged.json`, and `gpt-review/test_gpt_review.json` remain unchanged.
- DUT execution: none. No Flash, FIO write, power cycle or RAS injection was executed.
