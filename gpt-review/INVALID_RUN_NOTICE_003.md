# Invalid GPT Second-Review Run 003

## Status

Paused pending user direction. The row-20 review is discarded and is not counted as reviewed.

## Integrity failure

After reviewing source row 20 (`Functionality/row-20/Wistron-HW-00020-V002`), the checkpoint advanced `next_key` to `Functionality/row-21/Wistron-HW-00021-V002` without independently verifying the next source row's real code. The source row 21 code is `Wistron-HW-00021-V003`.

This violates the one-row source-key advancement invariant. The review content for row 20 is therefore not presented as valid, and the active overlay was restored to the last valid checkpoint at source row 19.

## Last valid checkpoint

- `reviewed_count`: 19
- `last_valid_checkpoint`: `Functionality/row-19/Wistron-HW-00019-V002`
- `next_key`: `Functionality/row-20/Wistron-HW-00020-V002`

## Resolution

The user authorized automatic re-review after this integrity failure. Source
row 20 was re-reviewed independently, the real next source code
`Wistron-HW-00021-V003` was read from the source before checkpointing, and the
active progress checkpoint now resumes at source row 21.
