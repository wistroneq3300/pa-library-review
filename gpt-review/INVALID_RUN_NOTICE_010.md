# Invalid Run Notice 010

- Detected: 2026-10-02
- Affected testcase: `Compatibility/row-235/Wistron-AMD GPU-00228-V002`
- Failure: the overlay record was appended, but the checkpoint `reviewed_count`
  remained at 2776 instead of advancing to 2777.
- Impact: the record is not counted as reviewed and cannot be retained as a
  valid checkpoint.
- Repair: remove the uncheckpointed row-235 overlay, restore the checkpoint to
  row 234, and independently re-review row 235 before continuing.
- Original XLSX and `data/tests.json` remain unchanged.
