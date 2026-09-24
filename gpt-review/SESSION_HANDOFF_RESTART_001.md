# GPT Second Review Handoff — Restart 001

- Active review method: exactly one testcase row at a time.
- Active overlay records: 16.
- Completed through `Functionality/row-1816/Wistron-HW-00015-V002` (I3C CPU1; duplicate code is distinguished by source row 1816).
- Next testcase: `Functionality/Wistron-HW-00017-V002`.
- A 99-case run was discarded because its generation method did not meet the
  independent-reasoning requirement.
- A review run may accumulate up to approximately 200 completed individual
  testcases, stopping immediately on a question or hard safety blocker.
- No batch, category, keyword, regex, or copy-forward template review is allowed.
- Original XLSX and `data/tests.json` remain source-of-truth and must remain unchanged.
- Records from source row 17 through source row 47 were discarded as an invalid run because their wording reused an analysis scaffold instead of demonstrating independent testcase reasoning.
- Review is paused; do not select the next testcase or restart until the user explicitly directs how to proceed.
