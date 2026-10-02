# Invalid Run Notice 007

- Detected: 2026-10-01 04:31 Asia/Taipei
- Affected range: `Functionality/row-1502/Wistron-BMC-00070-V003` through `Functionality/row-1504/Wistron-BMC-00072-V003`
- Last valid checkpoint: `Functionality/row-1501/Wistron-BMC-00069-V003`
- Cause: after writing row 1502 and reading its next source row, the runner continued selecting and writing rows 1503-1504 before checkpointing each prior row. This violated the one-row overlay, checkpoint, and next-row ordering rule.
- Correction: the uncheckpointed overlay records were removed; `progress.json` remains at reviewed count 1491 with next key `Functionality/row-1502/Wistron-BMC-00070-V003`.
- Required action: re-review rows 1502 onward directly from the XLSX and matching DeepSeek records, writing and checkpointing exactly one row before selecting the next.
- Original XLSX and `data/tests.json` remain immutable.
