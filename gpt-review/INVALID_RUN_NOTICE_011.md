# INVALID RUN NOTICE 011 — Historical source-row coverage gap

Detected 2026-10-03 after the Stability and `(No Main Function)` sequence reached source exhaustion. The overlay contains no testcase-specific records for these original XLSX rows even though later checkpoints advanced past them:

- `Functionality/row-204/Wistron-HW-00213-V002`
- `Functionality/row-206/Wistron-HW-00215-V002`
- `Functionality/row-208/Wistron-HW-00217-V002`

The current checkpoint remains the last valid sequential exhaustion checkpoint `(No Main Function)/row-13/Wistron---00014-V002`; no completed overlay is rolled back. These three source rows must be independently read from the original XLSX and added one at a time as a historical coverage reconciliation. Existing completed rows will not be redone.