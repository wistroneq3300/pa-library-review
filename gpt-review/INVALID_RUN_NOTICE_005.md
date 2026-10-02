# Invalid Run Notice 005

- Detected: 2026-10-01 02:30 Asia/Taipei
- Affected range: `Functionality/row-1416/Wistron-BMC-00708-V004` through `Functionality/row-1418/Wistron-BMC-00710-V002`
- Last valid checkpoint: `Functionality/row-1415/Wistron-BMC-00707-V004`
- Cause: after completing row 1416 and reading its next source row, the runner selected rows 1417 and 1418 before writing the row 1416 checkpoint. This violated the one-row overlay, checkpoint, and next-row ordering rule.
- Correction: the three uncheckpointed overlay records were removed; `progress.json` remains at reviewed count 1405 with next key `Functionality/row-1416/Wistron-BMC-00708-V004`.
- Required action: re-review rows 1416, 1417, and 1418 directly from the XLSX and matching DeepSeek records, writing and checkpointing exactly one row before selecting the next.
- Original XLSX and `data/tests.json` remain immutable.
