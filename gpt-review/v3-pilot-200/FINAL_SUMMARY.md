# PA Test Case Library — Review Logic V3 / 200-Case Pilot Final Summary

## 結論

本 Pilot 已完成 200 條唯一來源測項的逐條 V3 Review、靜態稽核與適用的隔離 Agent Understanding Validation。結果只代表文件與執行契約審查；本次沒有操作 DUT，因此不得解讀為 Hardware Validation PASS。

狀態區分：

- Review completed: 200/200。
- Semantically reviewed: 200/200，每條均讀取原始 XLSX row、DeepSeek、GPT V2 與適用歷史。
- Agent understanding validated: calibration 20 條及後續高風險/實質修訂子集；使用隔離但同模型家族的 reviewer，並非獨立模型驗證。
- Hardware tested: 0/200。

## 1. V3 新增與修改的規則

- 建立 Test Intent Accuracy、Automation Capability、Execution Readiness、Agent Execution Contract 四層模型。
- 將能力分類與當前缺項/批准狀態分離；缺 SPEC、package、參數或一次性 approval 不再自動等於 BLOCKED。
- 增加 `SOURCE_CONFLICT`，禁止從標題自行補造與 Procedure/Criteria 不一致的測試。
- 強制保留測試對象、完整範圍、時間、循環、條件、操作與證據；禁止以 inventory 代替 stress/update/function test。
- 增加 Actual-versus-Acceptance 分離：缺 Expected Value 不阻止安全 Actual collection，但沒有 reference 不得 PASS。
- 對 storage、fault injection、firmware、power cycle、environmental margin 建立穩定身分、批准、停止、復原與不可自動 retry 邊界。
- Skill 入口已優先導向 V3，同時保留 V2 歷史用途。

## 2. V2 容易造成過度 BLOCKED 的邏輯

- 將「尚未提供 SPEC/threshold」等同「技術上不能自動化」。
- 將「需要 package/image/vendor command」等同永久 BLOCKED。
- 將「包含人工 fixture/physical step」與「整條無法規劃」混為一談。
- 未充分區分可立即收集的 read-only Actual 與需要 reference 才能作出的 PASS。
- 部分案例把高風險當成不可自動化，而不是 `NEEDS_APPROVAL` 加嚴格安全契約。

## 3. 六個 Sheet 分布

| Sheet | Cases |
|---|---:|
| Functionality | 80 |
| Reliability | 30 |
| Performance | 25 |
| Compatibility | 30 |
| Stability | 25 |
| (No Main Function) | 10 |

## 4. V2 原始分類分布（正規化為正式四類）

| Classification | Cases |
|---|---:|
| FULLY AUTOMATABLE | 18 |
| REQUIRES PACKAGE / USER CONFIRMATION | 102 |
| MANUAL ONLY | 39 |
| BLOCKED | 41 |

歷史單獨的 `REQUIRES PACKAGE` 1 條與 `USER CONFIRMATION` 1 條已在統計中映射至正式 combined class，原始值仍保留在 record。

## 5. V3 提議分類分布

| Classification | Cases |
|---|---:|
| FULLY AUTOMATABLE | 12 |
| REQUIRES PACKAGE / USER CONFIRMATION | 133 |
| MANUAL ONLY | 33 |
| BLOCKED | 22 |

## 6. 合理解除 BLOCKED

共 25 條歷史 V2 BLOCKED 被提議改為非 BLOCKED。主要依據是：操作目的已可理解、缺項可由工程師提供、存在人工 setup 加自動化 evidence 的混合流程，或安全 read-only Actual 可以先收集。所有案例仍保留具體 readiness/approval gate，沒有因 reclassification 立即取得執行權限。

## 7. 必須維持 BLOCKED

V3 共 22 條 BLOCKED。主要原因是核心 procedure/criteria 完全缺失、標題與命令的 target/operation 無法調和、fault injection 的事件/預期反應不可歸因，或 AC/DC/WAT 私有 scenario 無法確定真正執行內容。詳細序號與理由見 `BLOCKED_RECLASSIFICATION.md`。

## 8. V3 Review Outcome

| Outcome | Cases |
|---|---:|
| KEEP | 16 |
| IMPROVED | 74 |
| RECLASSIFIED | 43 |
| REWRITE_REQUIRED | 12 |
| SOURCE_CONFLICT | 49 |
| NEED_ENGINEER_DECISION | 6 |

KEEP 不代表未審查；它表示 V2 的實質結論已正確，沒有為了增加修改率而改寫。

## 9. 十個重要技術改善案例

1. Case 167 GDS：以官方 gdsio 語意確認 `-x 0` 是 Storage-to-GPU，禁止 source 的 CPU-crossing 誤述，並要求 matched CPU control、mounted disposable file 與 UUID/BDF mapping。
2. Case 168 AMD UMC RAS：將 Replay AC Parity、ODECC CE、0x800 與 opaque flags 的矛盾提升為 SOURCE_CONFLICT，要求 CE/UE delta 與事件相關 kernel evidence。
3. Case 194 SMBIOS Type 46：由 BLOCKED 改為 FULLY AUTOMATABLE + NEEDS_SPEC；可先安全收 Actual，無 reference 時只是不准 PASS。
4. Case 185 CX-7/BF3 network stress：分離 Ethernet/RoCE/IB、host/DPU execution location、雙端角色及每 port 一小時與 numeric SPEC。
5. Case 175 BMC upload/delete：加入 canonical sandbox containment、每輪 end-to-end integrity、容量 floor、單一 finite bound 及具體 rail controls。
6. Case 180 cold storage margin：加入每個 physical bay disposition、即時 persistent identity/protected-device interlock、12 小時完整覆蓋及 humidity/dew-point safeguards。
7. Case 183 reboot campaign：暴露 500 cycles 與 12 hours 的 completion conflict，禁止 agent 自行選擇。
8. Case 195 BMC firmware：禁止假設通用 Redfish action URI，要求 advertised/vendor path、完整 preserve-all matrix、task terminal/timeout/stall 與所有 management services recovery。
9. Case 197 BIOS downgrade：加入 ordered intermediate-image manifest、每 hop signature/activation/POST/boot/security/device gate，禁止把 downgrade 當普通 upgrade。
10. Case 164 BF3 FRU：修正 `ipmitool fru list` portability assumption；命令未被 target tool 文件支持時必須停止而非靜默換命令。

## 10. Agent 誤解與修訂結果

隔離 validator 曾發現 cases 51、56、57、60、61、63、68、70、72、84、164、165、175、180、187、189、195、197 等契約存在可導致錯誤規劃的文件缺陷。每個缺陷均保留首次結果、修訂內容及 revalidation；最終均為 CLEAR_AFTER_REVISION 或等價的修訂後通過狀態。具體問題包括 I2C physical address 與 command byte 混用、sensor capability/routing 不完整、SEL sentinel 誤用、Redfish pagination 遺漏、GPU Power 缺少 identity/sampling/skew 定義、SMBIOS 缺 raw-table correlation、普通資料差異誤觸發整體停止，以及 final batch 的 metadata/dwell、failed-cycle retry、preserve-all、BIOS intermediate image 與 cold-storage dew-point/protected-device interlock。Pilot 最終 160 條有隔離同模型家族理解驗收，40 條依既定風險樣式明確記為 not selected/not required；沒有待處理、未驗證或仍需修訂的 validation status。

## 11. 尚需 Server SIT 工程師提供的事項

包括 vendor/private tool semantics、platform-specific SPEC/golden values、完整拓撲與 stable identity、performance tolerance、destructive I/O ownership、fault-injection mapping、power-cycle waveform、environmental rail/dew-point limits、firmware compatibility/rollback/security policy。完整清單見 `ENGINEERING_DECISIONS_REQUIRED.md`。

## 12. Regression 結果

- 未發現已知 Test Intent、scope、duration、iteration、安全或分類回歸。
- Static validator 對 200 條為 PASS，沒有非法類別、重複來源鍵、重複 variant、exact duplicate reason 或高相似度 warning。
- 原始 XLSX、tests.json、GPT V2 overlay hash 不變。
- 所有 record 的 `pass_claimed=false`、`hardware_tested=false`。

## 13. 未通過或未執行的驗收

- Calibration gate 已完成並通過。
- 多個初次 Agent Understanding validation 未通過，但已修訂並 revalidate CLEAR；首次失敗沒有被刪除或偽裝。
- 200 條 record 中 160 條完成隔離同模型家族理解驗收，另外 40 條明確標示為依風險樣式不選取／不需要；沒有 `PENDING*`、`REVISION_REQUIRED`、`NOT_VALIDATED` 或缺失狀態。
- 未做獨立模型驗證，只做隔離同模型家族驗證。
- 未做 DUT/hardware validation。

## 14. 是否適合套用至剩餘 2,912 條

V3 適合進入受控、分批的剩餘案例 Review，不適合無人監督的一次性 bulk rewrite 或自動 merge。建議維持每條 source-row 閱讀、每 20 條 checkpoint、每 50 條品質摘要、BLOCKED 加權抽查、material-change 隔離理解驗收及 immutable-source gate。私有工具與平台 SPEC 未提供時仍必須保留待決狀態。

## 15. Git 與報告位置

- Branch: `codex/testcase-review-v3-pilot-200`
- Baseline: `770c2bd81d329414f308999faa55d20212210fab`
- Reviewed-artifact commit (200 records, V3 outputs and validations): `9c9388978fcc38b6e97333bfa19792b53ccf11fb`.
- The metadata-only commit that records this SHA is the branch HEAD reported in the final handoff; Git commits cannot contain their own hash.
- Reports: `gpt-review/v3-pilot-200/`

## Release Gate

`PILOT COMPLETE — DOCUMENT REVIEW`; `INDEPENDENT MODEL VALIDATION NOT PERFORMED`; `HARDWARE VALIDATION NOT PERFORMED`.
