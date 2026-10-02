# Invalid Run Notice 006

- Detected: 2026-10-01 04:23 Asia/Taipei
- Affected range: `Functionality/row-1486/Wistron-BMC-00054-V003` through `Functionality/row-1499/Wistron-BMC-00067-V004`
- Last valid checkpoint: `Functionality/row-1485/Wistron-BIOS-00053-V003`
- Cause: after writing row 1486 and reading its next source row, the runner continued selecting and writing later rows before checkpointing the prior row. This violated the one-row overlay, checkpoint, and next-row ordering rule.
- Correction: the uncheckpointed overlay records were removed; `progress.json` remains at reviewed count 1475 with next key `Functionality/row-1486/Wistron-BMC-00054-V003`.
- Required action: re-review rows 1486 onward directly from the XLSX and matching DeepSeek records, writing and checkpointing exactly one row before selecting the next.
- Original XLSX and `data/tests.json` remain immutable.
