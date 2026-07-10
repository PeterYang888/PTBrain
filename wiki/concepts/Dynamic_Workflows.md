---
type: concept
tags: [claude-code, workflow, javascript, agent, parallel]
created: 2026-06-06
updated: 2026-07-10
sources: [2026-06-06_11天_claude_code_dynamic_workflows, 2026-06-12_dynamic_workflow_解析, 2026-07-10_agent_teams_協作模式]
---

# Dynamic Workflows

> [[Claude_Code]] 的 JavaScript 腳本驅動 agent 協作模式；以程式碼取代 Prompt 協調多個 Sub-agent，讓主 context window 只存最終結果。

## 詳細說明
傳統 [[Agentic_Workflow]] 讓多個 Agent 互相傳遞對話，很快就會讓 context window 爆炸。Dynamic Workflows 的解法：

- **JS 腳本作為骨架**：中間步驟的數據封裝進 JS 變數，主上下文只接收濃縮後的結果
- **平行 + 順序彈性**：腳本可定義哪些步驟並行、哪些順序執行
- **可重用性**：每次工作流可存成 JS 檔，跨 session 重用

核心數據（Bun Runtime 案例）：75 萬行 Zig → Rust 遷移，11 天完成，測試通過率 99.8%。規格：16 並行 / 累計最多 1000 個 Agent；適合耗時 >30 分鐘任務；需 CLI V2.1.154+。

## 三種觸發方式

| 模式 | 指令 | 適用場景 |
|---|---|---|
| Deep Search | `deep-search [查詢]` | 深度資訊檢索，多 Agent 對抗評分 |
| Workflow 關鍵字 | 輸入 `workflow`，字體變色後描述需求 | 生成可自訂的 JS 腳本 |
| Ultra Code | 切換模型至 Ultra Code | 自動撰寫並執行，最高推理強度 |

## 監控與管理
- `/workflows` 或 `wf`：查看當前運行 Agent 狀態
- 監控介面按 `s`：存成 JS 檔供未來重用
- `Enter`：查看 Agent 的 Prompt；`J/K`：滾動查看輸出

## 4 層功能階梯（何時該用？）
| 層級 | 工具 | 控制權歸屬 | Context 影響 |
| :--- | :--- | :--- | :--- |
| 基礎 | 直接對話 | 使用者 | 正常 |
| 執行層 | [[Subagent]] | 模型隨機 | 可能塞滿 |
| 溝通層 | [[Agent_Teams|Agent Team]] | 模型間互動 | 較多 |
| 指揮層 | **Dynamic Workflow** | **腳本/程式碼** | **極低** |

**何時別用**：任務前置依賴強（一步接一步）、修改數行程式碼、日常查詢——殺雞用牛刀。

## 多 Agent 的效能與成本陷阱（[[2026-07-10_agent_teams_協作模式]]）
更多 Agent 不等於更強。[[Kelly_Tsai]] 提出的風險指標：
- 結構不良的系統會把錯誤**放大 17 倍**
- 循序漸進式（逐步推理）任務中，多 Agent 效能可能**退步至 70%**
- 生產環境的多 Agent 系統**失敗率常過半**
- 因工具重算與訊息往返，成本可達單一 Agent 的**三倍以上**

> 「問題出在系統設計，不在模型本身。」

**設計原則**：以 Context 分工（誰需要看到哪些資料），而非以角色頭銜分工——後者會造成「傳話遊戲」式的資訊丟失。見 [[Context_工程]]。

## 成本控制三招
1. **模型分級**：撒網/蒐集階段用 Haiku，收斂推理階段用 Opus
2. **預算硬上限**：下指令時明定 Token 上限，觸及即停
3. **小範圍先測試**：先對單一資料夾跑，確認腳本邏輯與成本再放大規模

## 與其他模式的差別
- 跟 **[[Agent_Teams|Agent Team]]** 的差別：Agent Team 讓 agent 直接互通（動態決策）；Dynamic Workflows 是腳本定義的流水線（確定性強），適合大規模移植與掃描
- 跟 [[Vibe_Coding]] 的關係：都是「人類定義目標，AI 自主執行」，但 Dynamic Workflows 在執行層更結構化
- 跟 **N8N** 的差別：N8N 是固定式（Fixed）自動化流程；Dynamic Workflows 的路徑可隨任務進展動態調整
- 跟 [[Replit]] 的差別：Replit 以 Git 分支/合併語意組織多 agent（Pro 並行 10 個），並行度遠低於 Dynamic Workflows 的 16 並行 / 上限 1000

## 對抗式驗證機制（Adversarial Verification）
設計靈感源自 GAN（生成對抗網絡）：
- **生成組**：第一批 Agent 給出初步解答
- **反駁組**：第二批獨立 Agent 專門找漏洞與錯誤
- **迭代**：兩組反覆交鋒直到無可挑剔才輸出
- 這是 Bun 案例能達成 99.8% 測試通過率的關鍵

## 注意事項
- 成本高：極端情況一次 session 可耗盡 $200 額度
- 執行中不支援手動干預（全自動）
- 建議先用 Medium / Low 模型測試再升級

## 來源
- [[2026-06-06_11天_claude_code_dynamic_workflows]]
- [[2026-06-06_claude_code_1000_agent_dynamic_workflows]]
- [[2026-07-10_agent_teams_協作模式]]
