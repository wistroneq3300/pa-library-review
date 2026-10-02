# Invalid run notice 008

The run was invalidated from `Functionality/row-1517/Wistron-BMC-00085-V002` through `Functionality/row-1556/Wistron-BIOS-00401-V004`.

Rows 1517-1556 were appended to the GPT overlay after row 1516, but the required one-record overlay append, actual-next-row read, and progress checkpoint cycle was not completed for each row. Those 40 overlay records were removed. Progress remains at the last valid checkpoint, row 1516, and every affected testcase must be independently re-reviewed one at a time before it is counted again.

This notice is an audit record, not a review result. The source XLSX, `data/tests.json`, and DeepSeek records were not modified.
