# ED-REVIEW-001 Reconciliation — 2026-10-17

Published basis: `9f1e4492afd9917ff0c4020a8f39feb8b280cbd5`  
Historical checkpoint retained: `b8da580a50d36ed1538d1c5262c3c95bb5bbcab2` (891 completed)

## Classification discrepancy

The published 1,097-record state contained 1,097 effective classifications but its four stored counters summed to 1,094. The three missing increments were traced to valid, independently committed `REQUIRES PACKAGE / USER CONFIRMATION` records; no number was filled without a source record:

| Review sequence | Source key | Commit | Classification |
|---:|---|---|---|
| 1078 | `Functionality|917|Wistron-BMC-00207-V004` | `3a13e313` | `REQUIRES PACKAGE / USER CONFIRMATION` |
| 1081 | `Functionality|920|Wistron-BMC-00210-V003` | `c105b620` | `REQUIRES PACKAGE / USER CONFIRMATION` |
| 1083 | `Functionality|922|Wistron-BMC-00212-V002` | `21e1b526` | `REQUIRES PACKAGE / USER CONFIRMATION` |

At the preserved local valid checkpoint of 1,106 records, the record-derived statistics are:

- `MANUAL ONLY`: 349
- `REQUIRES PACKAGE / USER CONFIRMATION`: 351
- `FULLY AUTOMATABLE`: 317
- `BLOCKED`: 89
- Total: 1,106

## Invalid sequence 1107 draft

The unpublished sequence-1107 draft selected `Functionality|946|Wistron-BMC-00236-V002`, which is already one of the 200 Final Audit baseline records. It was moved intact to `INVALIDATED_RUNS/20261017_SEQUENCE_1107_BASELINE_OVERLAP/` and contributes zero to all effective counts. The correct next pending case is `Functionality|947|Wistron-BMC-00237-V002` / `c04e36eb37762c08`.

## Quality gates added

The validator now checks protected source hashes; direct XLSX-to-manifest order; all 200 Final Audit records plus every active Full Review record; unique Source Key and Variant ID; contiguous review sequence; exact pending-manifest order; all four classification counters and their total; blocked and source-conflict totals; next pending identity; ED-33 through ED-52 report/overlay/register consistency; the preserved 891 checkpoint; and strict duplicate JSON-key handling.

Sixteen historical files contain a byte-equivalent duplicate top-level `engineering_decision_update` key. They are explicitly allowlisted as legacy warnings because both values are identical. Any additional duplicate key or any non-identical duplicate fails validation.

No Master XLSX, formal test JSON, original Source, historical review or approved engineering decision was modified by this reconciliation.
