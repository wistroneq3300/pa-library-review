# Invalid Run Notice: Review Sequence 1873 Baseline Next-Key Selection

- Detected: 2026-10-19
- Affected uncommitted draft: `1873_b50c6884b0ef34a5.json`
- Source identity: `Functionality|1737|Wistron-HW-00366-V002`
- Last valid checkpoint: review sequence 1872
- Last valid next key: `Functionality|1737|Wistron-HW-00366-V002` / `b50c6884b0ef34a5`
- Incorrect proposed next key: `Functionality|1738|Wistron-HW-00367-V002` / `4fcfa8e44c66b208`
- Correct next pending key after sequence 1873: `Functionality|1739|Wistron-HW-00368-V003` / `17ad400172e741db`

## Reason

The selected source row and its DeepSeek/GPT references were read correctly, but the draft treated the immediately adjacent XLSX row 1738 as the next unreviewed testcase. Row 1738 is already covered by the completed Final Audit baseline and must not re-enter the active Full Review sequence. The per-case Validator rejected the checkpoint before commit because the manifest-derived next pending Source Identity is row 1739.

## Corrective action

The uncommitted draft and its progress increment were removed, restoring the active overlay to checkpoint 1872. The original XLSX and protected JSON sources were not modified. Sequence 1873 will be re-reviewed from row 1737, with row 1738 explicitly recognized as baseline-covered and row 1739 directly reopened and verified as the next pending Source Identity before the corrected record is written.
