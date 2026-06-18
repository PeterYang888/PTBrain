---
type: concept
tags: [ai, claude-code, context, workflow]
created: 2026-06-19
updated: 2026-06-19
sources: [2026-06-19_claude_code_500小時心得, 2026-06-19_loop_engineering, 2026-06-19_notebooklm整座圖書館]
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

## 與其他概念的關係
- 是 [[Agentic_Workflow]] 與 [[Loop_Engineering]] 的基礎工程
- 對比 [[理解成本]]：產出成本趨零後，餵給 AI 的 context 品質與判斷成為瓶頸
- 對比 [[RAG]]：RAG 是動態檢索補 context 的一種手段

## 來源
- [[2026-06-19_claude_code_500小時心得]] · [[2026-06-19_loop_engineering]] · [[2026-06-19_notebooklm整座圖書館]]
