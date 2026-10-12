# V3 Pilot Checkpoint — 100 Cases

- 已完成 100 筆唯一來源測項的逐條 Review，序號 1–100；下一筆為
  `Reliability|77|Wistron-System RAS-00797-V002`。
- 六個 Sheet 均已覆蓋：Functionality 80、Reliability 10、Performance 3、
  Compatibility 3、Stability 2、No Main Function 2。
- 校準 20 條已完成並通過 Gate；目前為正式 Pilot Review 階段。
- Workbook、`tests.json` 與 GPT V2 的 SHA-256 均與 `BASELINE.md` 一致；
  正式來源檔沒有修改。
- 100 筆 schema、唯一來源鍵、`case_variant_id`、合法 V3 分類與來源 hash
  檢查通過；`reason_for_change` 沒有完全相同的重複群組。
- 71 份 Agent Contract 已在隔離、同模型家族上下文驗收，其中 66 份清楚、
  5 份正確保留歧義；序號 90、93、95 的文件缺陷修正後已重新驗收通過。
  其餘 29 筆不是宣稱驗收通過，而是尚未被選為 material/high-risk validation
  或仍待後續批次驗收。
- 本階段沒有 DUT 連線、實機執行或 Hardware Validation；所有 PASS 僅指
  靜態稽核或 Agent Understanding Validation。
- 此 next-case 值曾在 checkpoint 初版誤抄為 row 88 / RAS-00808-V003；開始
  第 101 條前由固定 Selection Manifest 的 sequence 101 檢查攔截並更正，沒有
  建立錯誤 Review Record，也沒有以相似 code 代替來源。

V2 的 21 條 BLOCKED 中，13 條改為 `REQUIRES PACKAGE / USER CONFIRMATION`、
4 條改為 `MANUAL ONLY`、4 條維持 `BLOCKED`。同時，V3 將 6 條原非 BLOCKED
測項因真正的語意或來源衝突改為 BLOCKED。這表示分類調整不是以降低
BLOCKED 數量為 KPI，而是同時解除可由工程師提供條件的假阻擋，並新增必要
的真阻擋。
