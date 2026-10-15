# Invalid Run Notice — Sequence 1027 next-variant verification failure

Detected: 2026-10-16T01:07:36+08:00 (Asia/Taipei)

## Last valid checkpoint

- Commit: `0e6dcefca9cdef47efd79b407af37ce7f0432871`
- Effective completed count: 1,026 / 3,112
- Next source key: `Functionality|865|Wistron-BMC-00155-V002`
- Next case variant: `58071ca34b60e364`

## Invalidated draft

- Proposed review sequence: 1,027
- Source row: `Functionality|865|Wistron-BMC-00155-V002`
- Draft file preserved as `REVIEW_RECORDS/1027_58071ca34b60e364.invalid-draft.json`
- The draft is historical audit evidence only and does not count as completed review.

## Integrity failure

The current source row and immediate next XLSX row were directly read, and the
next source key was correct. However, the proposed checkpoint assigned an
unverified and incorrect `case_variant_id` to the next row before the next
manifest identity had been read. The draft used `6ea13788d9573ce5`; the exact
manifest identity for `Functionality|866|Wistron-BMC-00156-V003` is
`1d4a2f496ac4172b`.

Repository policy requires the next source key and variant identity to be read
and verified before writing the checkpoint. Therefore sequence 1,027 is
invalid even though its testcase reasoning was otherwise source-backed.

## Recovery

Active progress is restored to the last valid sequence 1,026 checkpoint. The
invalid draft is removed from the active `REVIEW_RECORDS` set and preserved in
this directory. Re-review restarts from Functionality row 865, directly from
the XLSX and all required reference/history sources, with the next row's exact
manifest identity verified before the replacement record is written.

No Master source, DeepSeek source, GPT V2 history, completed Review Record or
valid progress checkpoint was deleted or overwritten.
