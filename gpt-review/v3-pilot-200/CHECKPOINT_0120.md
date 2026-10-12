# V3 Pilot Checkpoint — 120 Cases

- 已完成 120 筆唯一來源測項逐條 Review；下一筆固定為
  `Performance|2|Wistron-Performance CPU-00001-V003`。
- 六個 Sheet 均已覆蓋：Functionality 80、Reliability 30、Performance 3、
  Compatibility 3、Stability 2、No Main Function 2。
- Workbook、`tests.json` 與 GPT V2 SHA-256 均與 `BASELINE.md` 一致；正式
  原始資料未修改。
- 120 筆 schema、唯一來源鍵、`case_variant_id`、合法分類與來源 hash 驗證
  通過；`reason_for_change` 沒有完全相同的重複群組。
- 目前 V3 outcome：KEEP 11、IMPROVED 37、RECLASSIFIED 35、
  REWRITE_REQUIRED 7、SOURCE_CONFLICT 27、NEED_ENGINEER_DECISION 3。
- 93 份執行合約完成隔離、同模型家族理解驗收：85 份直接清楚，8 份在
  歧義修正或明確保留後通過；其餘 27 筆未宣稱 Agent Understanding PASS。
- 第 118–120 條均為 AMD GPU RAS，但各自發現不同問題：SDMA 使用 UMC
  基線與隱含 Device 0、UMC replay 的三種地址/計數域衝突、以及 GFX poison
  producer/consumer 次序被 V2 改寫成獨立 variants。三條均各自完成合約驗收。
- 本階段沒有 DUT 連線、注錯或 Hardware Validation；所有 PASS 僅表示靜態
  完整性或 Agent Understanding Validation。

V2 的 27 條 BLOCKED 中，14 條改為 `REQUIRES PACKAGE / USER CONFIRMATION`、
4 條改為 `MANUAL ONLY`、9 條維持 `BLOCKED`。同時 V3 將 6 條原非 BLOCKED
測項改為 BLOCKED，證明本 Pilot 並未以降低 BLOCKED 數量作為品質目標。
