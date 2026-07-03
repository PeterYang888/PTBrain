---
type: entity
entity_type: product
tags: [ai, agent, google, gemini, automation]
created: 2026-06-27
updated: 2026-06-27
sources: [2026-06-27_gemini_spark]
---

# Gemini Spark

> [[Google]] 推出的 24/7 自動化 AI 代理人，跑在雲端 VM、用戶離線時仍持續工作；以 Tasks / Skills / Schedules 三支柱 + [[MCP]] 擴展，把「對話式 AI」變成「系統化工作流」。

## 關鍵事實
- **自主代理人**：用戶離線（關機/蓋電腦）時仍持續工作，運行於專用 Google Cloud VM
- **三大支柱**：
  - **Tasks**：多步驟目標（如兩週追蹤職缺、Gmail 提取交付清單存 Google Doc）
  - **Skills**：可重用風格/邏輯（分析 50 封郵件建風格指南 `ghostriter`），`@`/`/` 呼叫
  - **Schedules**：時間觸發（週一 9 點總結）或事件觸發（航班延誤更新行程）
- **狀態**：Beta「實驗性」，限美國 [[Google]] AI Ultra 訂閱者；最多 **15 個任務** 並行
- **整合**：原生 Google Workspace（Gmail/日曆/Drive/Docs/Sheets/Slides/YouTube/Maps）；[[MCP]] 已支援 Canva/OpenTable/Instacart，2026 夏加 Adobe/Spotify/GitHub/Notion/Slack
- **安全**：Checkpoints 在敏感操作（密碼）時暫停請求人工授權，防 Prompt Injection

## 與其他頁的關係
- 與 [[OpenAI_Codex]] record-and-replay（[[2026-06-27_rpa_要沒了]]）、Claude Code [[routines]] 同屬「個人/企業 AI 自動化 OS」競爭，體現 [[AIOS]] 願景
- 透過 [[MCP]] 跨出 Google 生態系與第三方工具協作；實踐 [[Agentic_Workflow]]

## 相關來源
- [[2026-06-27_gemini_spark]]
