# PA Test Case Library — V3.1 最終交接摘要

## A. Review Logic V3.1

本次在保留 V3 歷史文件的前提下新增 V3.1，並把本次訊息提供的工程裁定正式整理為 ED-01～ED-28。由於 Repository 內沒有完整的原始 01～28 題逐題問句，文件只記錄本次交接可證明的決策內容，未宣稱找到不存在的 GitHub 歷史裁定。

V3.1 的核心新增／修正如下：

- 將 3,112 條定位為全 Server SIT／GPU Server SIT 共用 Master Library，而非單一專案固定 Script。
- 將 Master Default、Approved Project Override、Actual Execution、Coverage Difference、Execution Status 與 Engineering Verdict 分離。
- Machine Time／Attended Time 預設視為工時與排程參考；只有明確同為正式要求時才構成真正 SOURCE_CONFLICT。
- 將 Automation Capability、Execution Readiness、Manual Activity、Required Inputs 與 Safety Approval 分離。
- 一位有權工程師即可核准，不新增雙人簽核；但 Target Identity、Impact Scope、Storage Protection、Safety、Recovery 與明確執行批准不可省略。
- 既有 PA Manager Cycle、Project Script、Vendor Tool、GPU Diagnostic 與 Stress Script 優先；Agent 不重造已有工具。
- 原始方法完整保留，新版方法以可查證、版本／平台限定、可追溯的 Recommendation 另列。
- Storage 寫入、Firmware、Power Cycle、Error Injection 與 Margin 測試維持嚴格安全邊界。
- WebUI／BIOS UI／UID LED 等核心人工觀察不會被 API 或 CLI 取代。
- 普通 Warning 依核准計畫繼續收集；資料、硬體、控制能力或 Safety Stop 風險則停止。
- 不自動 Retry，不覆寫原始失敗；核准計畫內下一個 Loop 不等於 Retry。
- 正式 PASS／FAIL／BLOCKED 由工程師裁定；工具輸出只保留為 Raw Evidence。
- Ethernet、RoCE、InfiniBand 分開選擇，不混成同一種 Network Test。
- WAT、NVDiag、NVQual、MODS 等私有工具不猜測命令語意。

保留的 V3 原則包括來源不可覆寫、四分類、原子化逐案 Review、破壞性操作防護、Evidence First、Vendor/SOP 依賴與真實語意不明時 BLOCKED。個案性決策仍留在各 Review Record；未提供的 Project SPEC、Target、工具版本、參數、Expected 與安全限制維持待確認。

## B. 200 條 Review 統計

### Review outcome

- KEEP：**175**
- IMPROVED：**22**
- RECLASSIFIED：**3**
- NEEDS_ENGINEER_DECISION（readiness）：**6**

### Automation classification

| 分類 | V3 | V3.1 | 差異 |
|---|---:|---:|---:|
| FULLY AUTOMATABLE | 12 | 12 | 0 |
| REQUIRES PACKAGE / USER CONFIRMATION | 133 | 132 | -1 |
| MANUAL ONLY | 33 | 34 | +1 |
| BLOCKED | 22 | 22 | 0 |

三筆分類變更：

- Seq 9：FULLY AUTOMATABLE → REQUIRES PACKAGE / USER CONFIRMATION；安全讀取可執行，但平台 ACPI Table 適用性仍需工程資料。
- Seq 10：REQUIRES PACKAGE / USER CONFIRMATION → MANUAL ONLY；核心是 BIOS 設定、實體目標與高風險注錯，Agent 只能協助蒐證。
- Seq 76：REQUIRES PACKAGE / USER CONFIRMATION → FULLY AUTOMATABLE；CPU Sensor Actual 可完整自動讀取，缺 Expected 只影響正式判定。

SOURCE_CONFLICT 從 **80 降為 58**，移除的 22 筆均有明確來源列與理由，主要是 Machine Time 被錯當正式測試時數；真正的命令、測試目的、QD、I/O Mix、Network Mode、Cycle Count 或 Firmware 語意衝突仍保留。BLOCKED 仍為 22，沒有為了數字好看而放寬安全條件。

## C. 代表性改善案例

1. **Seq 14 — Storage target safety**：V3 含不必要的雙人目標核對；V3.1 依單一有權工程師裁定移除雙人制度，但保留 persistent identity、OS/mount/RAID/data/evidence-disk 排除與復原。
2. **Seq 18 — 40C Margin**：V3 把 12 小時 Procedure 與 240 分鐘 Machine Time 判為衝突；V3.1 保留 12 小時 Master，只把 240 分鐘視為排程資料。
3. **Seq 54 — BMC capping**：V3.1 只移除 Machine Time 假衝突；Get/write、CPU/chassis 與 enforcement 語意仍互斥，因此保持 BLOCKED。
4. **Seq 76 — CPU Temperature**：缺少平台 Expected 不再降低自動化能力；Actual 收集為 FULLY AUTOMATABLE，正式正確性仍由工程師判斷。
5. **Seq 122 — Storage performance**：移除 Machine Time 假衝突，但保留真正的 QD1／QD64 衝突及寫入目標安全。
6. **Seq 143 — Storage 70/30 vs randwrite**：沒有把所有 SOURCE_CONFLICT 一律解除；I/O Mix 衝突維持待工程師決定。
7. **Seq 170 — All PCIe slot margin**：保留 12 小時、全槽位、>80% bandwidth 與實體 Margin 控制；不接受 240 分鐘替代。
8. **Seq 176 — Idle 24 hrs**：允許工程師核准 12 小時 Project Run，但明確記錄與 24 小時 Master 的 12 小時 Coverage Gap。
9. **Seq 185 — CX-7/BF3 network stress**：要求專案明確選 Ethernet、RoCE 或 InfiniBand，對應端點、工具與 SPEC；不把三種模式混為一個結果。
10. **Seq 193 — GDS**：完整保留 gdsio 原始參數；修正不安全／錯誤路徑，要求安全 mounted file、GPU UUID/BDF 對應及官方定義的 GDS/CPU paired mode。
11. **Seq 195 — BMC firmware**：保留 WebUI Preserve-all 流程；只有目標實際 advertise 且 vendor 支援時才用 UpdateService，不虛構通用 POST URI。
12. **Seq 197 — BIOS downgrade**：將一般 upgrade 文字與 downgrade 目的分開保留，新增 anti-rollback、ordered version path 與每 hop 啟動／安全／設定檢查。

## D. Agent Readiness

較適合交給 Agent 的測項包括唯讀 Inventory/Sensor/SMBIOS 收集、已定義的 Pre/Post check、具有核准 Project Plan 的 stress/cycle script，以及可由現成工具完整執行且 Evidence Contract 明確的案例。Seq 76、194 是「缺 Expected 但 Actual 可安全自動蒐集」的代表。

仍需工程師核心人工操作／觀察的包括 WebUI、BIOS Setup、UID LED、接線／治具、Chamber／Rail Margin、實體 Hot-plug 與需人工確認的 Firmware/OEM 操作。Agent 可解釋步驟、送出核准輔助命令、分析截圖／Log 與整理證據，但不能宣稱自己完成目視驗證。

已有 PA Manager Cycle、Project Cycle Script、WAT、SST、DCGM、Vendor Tool 或 OEM Update Flow 的案例，應先核對 Coverage 後使用現成工具，不另造 Cycle/Diagnostic 控制器。缺少 Project SPEC、工具套件、Target Map、參數或 Expected 的案例大多是 readiness 問題；只有測試意圖、操作對象或危險命令語意不明的 22 筆保持 BLOCKED。

所有實質修改的高風險案例及代表性其他修改共 25 筆完成 context-isolated same-model-family Understanding Validation，25/25 通過。本結果不是跨模型獨立驗證，也不是實機測試。

## E. PA Manager 相容性

本次唯讀檢查 `pa-cycle-lab` 的 `codex/platform-premium-ui-v1`，基準 commit 為 `3ce4b9c6e5467abe9d27050e5af0240b07fff3dc`，沒有修改該 Repository。

可直接沿用：

- 原始 `procedure`／`criteria` 顯示與保留方式。
- nested `ai_review` 與 immutable AgentRunContext。
- `case_variant_id` 指派、重複 code 的 variant 選擇。
- Pre-check／Post-check、Evidence、Agent Chat Drawer 與 Cycle Validation。
- DONE 與工程正式 PASS/FAIL 分離的現行方向。

需要未來平台修改：

- V3.1 必須以 versioned overlay 在 identity 計算後合併，或從 hash 排除，否則修改 review payload 可能改變 `case_variant_id`。
- UI 新增 Master／Project／Actual／Coverage、Original Method／Modernized Recommendation、Readiness、Manual Activity、Required Inputs、Safety Approval 與 Engineer Verdict 分區。
- Agent Gateway 不能只讀一個 Automation Classification；需傳遞 Project Plan、批准範圍、Safety Stop、Evidence、Retry Policy 與 Coverage Difference。
- 現行 MANUAL ONLY Gateway 全面禁止 DUT 指令，與「核心人工、Agent 可做核准輔助命令」的 V3.1 模型不完全相容；需新增 `agent_assistance_allowed` 或等價欄位。
- 原始人工作業單不可被新版建議覆蓋，Firmware/WebUI/API 等方法必須分開呈現。

完整資料契約與流程差異見 `PA_MANAGER_COMPATIBILITY_REPORT.md`。

## Release Gate 結論

- 200/200 唯一來源鍵與 variant；Manifest 對應零錯誤。
- 200/200 直接 XLSX code/hash 對應成功。
- Source XLSX、V2、V3 Pilot、`tests.json` 與 `tests_gpt_merged.json` 均未修改。
- 200/200 未宣稱實機測試、未宣稱正式 PASS、未自動 Retry、未放寬安全邊界。
- 反套版完全重複檢查：Test Intent 0、Review Improvement 0、Safety Boundaries 0、Expected Evidence 0。
- V3.1 Review Branch Release Gate：**PASS**。

建議在使用者與 ChatGPT 完成獨立 Review、且 PA Manager 的 identity／V3.1 overlay 契約確認後，再用相同逐條流程審查剩餘 2,912 條；本次不自動展開。
