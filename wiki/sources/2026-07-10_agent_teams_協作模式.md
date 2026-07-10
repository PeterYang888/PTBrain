---
type: source
tags: [ai, agent, multi-agent, workflow, claude-code]
created: 2026-07-10
source_url: https://www.youtube.com/watch?v=4dom8ne0hg0
source_date: 2026-07-10
source_type: transcript
---

# Agent Teams 怎麼運作？Subagent、Agent Teams 與 Dynamic Workflows

> 來源：[原始檔](../../raw/transcripts/2026-07-10_agent_teams_協作模式.md) · 主講：[[Kelly_Tsai]]（CKY channel）

## 一句話摘要
多 Agent 協作分三級（[[Subagent]] → [[Agent_Teams]] → [[Dynamic_Workflows]]）；更多 Agent 不等於更強，**問題出在系統設計而非模型**，2026 年工程師的價值在於「判斷何時該開團隊」與擔任 Reviewer。

## 核心論點
- **三種分級模式**：[[Subagent]]（各自獨立回報，適合定義明確可並行的任務）、[[Agent_Teams]]（有群組溝通機制，適合需互相對齊）、[[Dynamic_Workflows]]（AI 自主規劃、執行與驗收）
- **以 Context 而非角色分工**：依「誰需要看到哪些資料」分配任務最穩定；按角色頭銜（Role）分工容易產生「傳話遊戲」式資訊丟失，導致錯誤放大（見 [[Context_工程]]）
- **效能與成本陷阱**：多 Agent 在需要逐步推理的任務中反而退步；工具重算與訊息往返讓成本可達單一 Agent 的三倍以上
- **工程師價值的典範轉移**：競爭力不在會開多少 Agent，而在決策力（何時開團隊）與審核力（Reviewer）

## 關鍵數據
- 結構不良的系統會把錯誤**放大 17 倍**；循序漸進式任務中多 Agent 效能可能**退步至 70%**；生產環境多 Agent 系統**失敗率常過半**
- [[Dynamic_Workflows]] 規格：同時 **16 個**分身，一輪任務上限 **1000 個**（與 [[Dynamic_Workflows]] 頁既有記載一致）
- 極端案例：一名工程師用 AI 團隊在 **11 天**內翻寫 **75 萬行**程式碼（即 [[Dynamic_Workflows]] 頁記載的 Bun Runtime Zig → Rust 遷移案例）
- [[Replit]] 方案：Pro 支援並行 **10 個** agents，一般方案 **2 個**；$500 credits 優惠價 $440

## 值得引用的段落
> 「結構設計得好的可以幫你加速，結構亂搞的卻會把錯誤放大 17 倍以上。」
> 「問題出在系統設計，不在模型本身。」
> 「2026 年工程師真正值錢的不是會不會開一堆 agent，而是判斷出來什麼時候應該要開團隊，什麼時候用一個就夠了。」
> 「一兩年後會帶一個 AI 團隊，會變成跟今天會用 Google 一樣基本的能力。」

## 與其他工具的關聯
- **AutoGPT / AutoGen / CrewAI**：Agent 團隊概念並非全新，業界已摸索數年
- **Git branches**：[[Replit]] 的多 Agent 協作類比為分支與合併回 main
- **N8N**：固定式（Fixed）自動化流程 vs [[Dynamic_Workflows]] 的路徑動態調整

## 連結到的 wiki
- [[Agent_Teams]] · [[Subagent]] · [[Dynamic_Workflows]] · [[Context_工程]] · [[Agentic_Workflow]] · [[Kelly_Tsai]] · [[Replit]] · [[Anthropic]] · [[Claude_Code]]

## 我的問題 / 待追蹤
- 「錯誤放大 17 倍」「退步至 70%」「失敗率過半」的原始研究出處未在影片中點名，待查
- 影片未提及 [[Claude_Code]] CLI 指令或 [[MCP]] 設定範例（NotebookLM 已註明）
