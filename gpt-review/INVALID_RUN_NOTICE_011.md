# INVALID RUN NOTICE 011 — Historical source-row coverage gap

Detected 2026-10-03 after the Stability and `(No Main Function)` sequence reached source exhaustion. The overlay contains no testcase-specific records for these original XLSX rows even though later checkpoints advanced past them:

- `Functionality/row-204/Wistron-HW-00213-V002`
- `Functionality/row-206/Wistron-HW-00215-V002`
- `Functionality/row-208/Wistron-HW-00217-V002`

The current checkpoint remains the last valid sequential exhaustion checkpoint `(No Main Function)/row-13/Wistron---00014-V002`; no completed overlay is rolled back. These three source rows must be independently read from the original XLSX and added one at a time as a historical coverage reconciliation. Existing completed rows will not be redone.

## Resolution — 2026-10-03

The three historical omissions were independently read from the original XLSX and reconciled one at a time: row 204 BLOCKED / CHANGED, row 206 MANUAL ONLY / IMPROVED, and row 208 BLOCKED / CHANGED. Existing row 205 and row 207 overlays were verified as already present and were not redone; progress-only checkpoint corrections advanced to the repaired rows. The source audit now maps all 3,112 original XLSX rows to 3,112 unique testcase source references with no missing or duplicate source mappings. A historical duplicate copy of the row 2208 overlay was also removed to restore the one-record/one-key invariant; the valid row 2208 review remains.
