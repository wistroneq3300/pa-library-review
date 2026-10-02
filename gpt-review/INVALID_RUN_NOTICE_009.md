# Invalid run notice 009

The run was invalidated from `Functionality/row-1517/Wistron-BMC-00085-V002` through `Functionality/row-1518/Wistron-BMC-00086-V003`.

Row 1517 was written and row 1518 was read, but row 1517 was not checkpointed before row 1518 was written. The two uncheckpointed overlay records were removed. Progress remains at the last valid checkpoint, row 1516, and both affected testcases must be independently re-reviewed one at a time before they are counted again.

This notice is an audit record, not a review result. The source XLSX, `data/tests.json`, and DeepSeek records were not modified.
