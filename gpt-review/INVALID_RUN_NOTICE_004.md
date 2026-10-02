# Invalid Run Notice 004

## Detected

During the manual 100-case run, the record for `Wistron-HW-00272-V002` was
inserted before the previous last record instead of being appended after
`Wistron-HW-00271-V003`. The record was not counted as valid.

## Recovery

- Rolled the active overlay back to the last valid checkpoint:
  `Functionality/row-252/Wistron-HW-00271-V003`.
- Restored `reviewed_count` to `252` and restored `next_key` to
  `Functionality/row-253/Wistron-HW-00272-V002`.
- The testcase must be independently reread and written again at the correct
  append position before the run continues.

The original XLSX and `data/tests.json` remain read-only.
