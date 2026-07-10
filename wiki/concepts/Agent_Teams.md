---
type: concept
tags: [ai, agent, multi-agent, workflow, claude-code]
created: 2026-07-10
updated: 2026-07-10
sources: [2026-07-10_agent_teams_協作模式]
---

# Agent Teams

> 具備**群組溝通機制**的多 Agent 協作模式：agent 之間能互相看到彼此的訊息與進度，適合需要互相對齊的任務。位於 [[Subagent]] 與 [[Dynamic_Workflows]] 之間的中間層。

## 詳細說明
在 [[Kelly_Tsai]] 提出的三級分類中，Agent Teams 是「溝通層」：
- **[[Subagent]]（執行層）**：各自獨立執行、獨立回報，彼此不對話
- **Agent Teams（溝通層）**：agent 之間可互通訊息，能在過程中對齊認知
- **[[Dynamic_Workflows]]（指揮層）**：由腳本/程式碼定義流水線，AI 自主規劃、執行與驗收

溝通能力是雙面刃：它讓需要協調的任務得以完成，但也帶來訊息往返的 token 成本與錯誤傳播風險。

## 何時該用
| 情境 | 建議模式 |
|---|---|
| 任務定義明確、可完全並行 | [[Subagent]] |
| 子任務需互相對齊、有相依認知 | **Agent Teams** |
| 大規模移植/掃描、需確定性流水線 | [[Dynamic_Workflows]] |
| 任務前置依賴強（一步接一步）、只改數行程式碼 | 單一 agent 即可 |

## 設計原則：以 Context 分工，不以角色分工
最穩定的切分方式是問「**誰需要看到哪些資料**」，而非指派角色頭銜（Role）。按角色分工時，資訊要在 agent 間交接，容易產生「傳話遊戲」式的丟失，讓錯誤被逐層放大。見 [[Context_工程]]。

## 效能與成本陷阱（來自 [[2026-07-10_agent_teams_協作模式]]）
- 結構不良的系統會把錯誤**放大 17 倍**
- 循序漸進式（逐步推理）任務中，多 Agent 效能可能**退步至單一 agent 的 70%**
- 生產環境的多 Agent 系統**失敗率常過半**
- 因工具重算與訊息往返，成本可達單一 Agent 的**三倍以上**

> 「問題出在系統設計，不在模型本身。」— [[Kelly_Tsai]]

## 實作對照
- [[Replit]]：Pro 方案並行 10 個 agent，協作類比 Git 分支與合併回 main
- **AutoGPT / AutoGen / CrewAI**：業界已摸索數年的早期多 agent 框架
- [[Claude_Code]] 的 [[Dynamic_Workflows]]：16 並行 / 上限 1000 個 agent

## 與其他概念的差別
- 跟 [[Dynamic_Workflows]] 的差別：Agent Team 讓 agent 直接互通（動態決策）；Dynamic Workflows 是腳本定義的流水線（確定性強）
- 跟 [[Agentic_Workflow]] 的關係：Agentic Workflow 是上位概念，Agent Teams 是其中一種組織形態

## 來源
- [[2026-07-10_agent_teams_協作模式]]
