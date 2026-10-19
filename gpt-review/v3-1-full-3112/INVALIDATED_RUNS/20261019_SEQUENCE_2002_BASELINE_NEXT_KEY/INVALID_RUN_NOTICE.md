# Invalid Run Notice: Review Sequence 2002 Baseline Next-Key Selection

- Detected: 2026-10-19
- Affected committed draft: `2002_012a3064811f8fb2.json` in commit `6b1cd85`
- Source identity: `Functionality|1870|Wistron-BMC-00959-V002`
- Last valid checkpoint: review sequence 2001
- Last valid next key: `Functionality|1870|Wistron-BMC-00959-V002` / `012a3064811f8fb2`
- Incorrect proposed next key: `Functionality|1871|Wistron-BMC-00960-V002` / `071022e68e1b6067`
- Correct next pending key after sequence 2002: `Functionality|1872|Wistron-BMC-00961-V002` / `86353647f9520c5e`

## Reason

The selected row 1870 and its matching DeepSeek/GPT references were read correctly, but the committed draft treated the immediately adjacent XLSX row 1871 as the next unreviewed testcase. Row 1871 is already covered by the completed Final Audit baseline and must not re-enter the active Full Review sequence. The per-case Validator rejected the checkpoint immediately after the commit and before any push.

## Corrective action

The committed draft is isolated under this invalid-run directory and contributes zero to the active record count and classification statistics. The active overlay is restored to checkpoint 2001 without Reset. Sequence 2002 will be re-reviewed from row 1870; row 1871 is explicitly treated as baseline-covered, and row 1872 must be directly reopened and verified as the next pending Source Identity before the corrected record is written. Original XLSX and protected JSON sources remain unchanged.
