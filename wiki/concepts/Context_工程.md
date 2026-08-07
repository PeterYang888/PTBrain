---
type: concept
tags: [ai, claude-code, context, workflow]
created: 2026-06-19
updated: 2026-07-18
sources: [2026-06-19_claude_code_500小時心得, 2026-06-19_loop_engineering, 2026-06-19_notebooklm整座圖書館, 2026-07-10_agent_teams_協作模式, 2026-07-18_google_agentic_engineering_day1]
---

# Context 工程（Context Engineering）

> 刻意管理 LLM 的上下文（context window）內容與載入時機，以最少 Token 換取最準輸出。Agentic 工作流的核心工程能力。

## 詳細說明
LLM 的輸出品質幾乎完全取決於 context 的質量；但 context window 有限且每個 token 都有成本。Context 工程就是「在對的時機，只給 AI 當下需要的資訊」。它是 [[Harness_Engineering]] → [[Loop_Engineering]] 工程化階梯中，介於 Prompt 與 Harness 之間的一層。

## 關鍵手法
- **漸進式載入（Progressive Loading）**：只載入任務當下所需資料，不一次塞滿（見 [[2026-06-19_claude_code_500小時心得]]）
- **CLI 優先**：CLI 輸出最乾淨、無冗餘 metadata；API 回傳大量 JSON / status codes 都算 Token；[[MCP]] 光載入背景就可能耗 ~4,300 tokens —— Token 效率 CLI > API > MCP
- **設定檔承接背景**：用 `CLAUDE.md` 等專案設定檔固化偏好與限制，讓每次 session 不從零開始
- **記憶寫回**：把歷史判斷、行業框架系統化（呼應 [[AI組織變革]] 的「管理上下文能力」）

## Google 課程版分類：Static vs Dynamic（2026-07-18）
Google Agentic Engineering 課程把 context 分成兩類並給出取捨框架（見 [[2026-07-18_google_agentic_engineering_day1]]）：
- **Static Context**：每次必載（系統指令、agent.md）——可靠但 Token 成本高
- **Dynamic Context**：按需載入（RAG 撈取、工具結果）——省錢但有抓取失敗風險
- **Progressive Disclosure**：Agent 啟動只讀 Skill metadata 一行，任務匹配才載入完整指令——與上方「漸進式載入」同一原則的官方版本
- **Token 經濟學（Capex/Opex）**：前期整理 Context 是資本支出，靠提高一次成功率降低長期 Token 燃燒率；Context Engineering 被明示為取代 Prompt Engineering 的核心技能

## 延伸：以 Context 分工，不以角色分工
在多 Agent 系統中，Context 工程直接決定任務切分方式。[[Kelly_Tsai]] 的判準是問「**誰需要看到哪些資料**」，而非指派角色頭銜（Role）：

- 按**角色**分工 → 資訊需在 agent 間交接，產生「傳話遊戲」式的丟失，錯誤被逐層放大（結構不良可放大 **17 倍**）
- 按 **context** 分工 → 每個 agent 拿到的就是它該看的，交接面最小

這是 [[Subagent]] / [[Agent_Teams]] / [[Dynamic_Workflows]] 三種模式共通的設計原則。詳見 [[2026-07-10_agent_teams_協作模式]]。

## 與其他概念的關係
- **注意力面向的姊妹概念 [[指令預算]]**：Context 工程管的是 Token 稀缺，指令預算管的是同一份 context 裡「模型能真正顧到幾條規則」的注意力稀缺——規則就算 Token 便宜，存在本身就有成本（見 [[2026-08-08_claude_md_15分鐘精通]]）
- 是 [[Agentic_Workflow]] 與 [[Loop_Engineering]] 的基礎工程
- 對比 [[理解成本]]：產出成本趨零後，餵給 AI 的 context 品質與判斷成為瓶頸
- 對比 [[RAG]]：RAG 是動態檢索補 context 的一種手段

## 來源
- [[2026-06-19_claude_code_500小時心得]] · [[2026-06-19_loop_engineering]] · [[2026-06-19_notebooklm整座圖書館]] · [[2026-07-10_agent_teams_協作模式]] · [[2026-07-18_google_agentic_engineering_day1]]
