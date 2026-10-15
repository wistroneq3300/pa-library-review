# Invalid Run Notice — Remote Checkpoint 1,000

Date: 2026-10-15 (Asia/Taipei)

## Last valid checkpoint

- Commit: `b8da580a50d36ed1538d1c5262c3c95bb5bbcab2`
- Effective completed count: 891 / 3,112
- Next source key: `Functionality|724|Wistron-BMC-00014-V004`

## Invalidated range

- Remote commit audited: `582332ec066b7612ca51208aff23c9dc87d98323`
- Claimed effective sequences: 892–1,000
- New review records: 109
- Source rows: `Functionality|724|Wistron-BMC-00014-V004` through
  `Functionality|838|Wistron-BMC-00128-V005`

## Integrity failure

The remote checkpoint added 109 previously unreviewed testcase records in one
commit. Repository policy requires each unreviewed testcase to be read,
persisted, checkpointed, and committed independently before selecting the next
row; a normal commit changing multiple unreviewed cases is explicitly invalid.
The structural validator passed source identity, hashes, schema, count, and
exact-duplicate checks, but those checks cannot prove the mandatory sequential
review and commit boundary.

## Preservation and recovery

The 109 JSON records and their batch/checkpoint documents are preserved
verbatim under this directory as non-counting historical evidence. They are
not deleted, overwritten, or presented as completed review. Active progress is
restored by a forward commit to the last valid 891 checkpoint. Re-review starts
from the first affected row, directly from the XLSX, one testcase at a time.

No Master Source, `data/tests.json`, GPT V2 history, or V3/V3.1 historical
record is modified by this invalidation.
