---
type: source
tags: [ai, agent, google, gemini, automation]
created: 2026-06-27
source_url: https://www.youtube.com/watch?v=V2gNi-jmjY0
source_date: 2026-06-27
source_type: transcript
---

# Gemini Spark: Automate Anything — Google 的 24/7 AI 代理人

> 來源：[原始檔](../../raw/transcripts/2026-06-27_gemini_spark.md) · 主講：Julian Goldie SEO

## 一句話摘要
[[Gemini_Spark]] 是 [[Google]] 的 24/7 自動化 AI 代理人，跑在雲端 VM，用戶離線時仍持續工作；以 Tasks / Skills / Schedules 三支柱 + [[MCP]] 擴展，把「對話式 AI」變成「系統化工作流」。

## 核心論點
- **聊天機器人 → 自主代理人**：用戶離線（關機/蓋電腦）仍持續工作
- **雲端 24/7**：跑在專用 Google Cloud VM，不依賴本地設備
- **三支柱**：Tasks（目標）、Skills（個人化背景）、Schedules（自動觸發）
- **原生數據 + 開放擴展**：Google Workspace 原生權限 + [[MCP]] 連第三方
- **零代碼民主化**：自然語言即可指揮複雜 SOP

## 關鍵細節與數據
- 狀態：Beta「實驗性」，限美國 **Google AI Ultra** 訂閱者；最多 **15 個任務** 並行
- **Tasks**：如「兩週追蹤職缺」「Gmail 提取交付清單存 Google Doc」
- **Skills**：分析 50 封郵件建風格指南 `ghostriter`；`@` / `/` 呼叫
- **Schedules**：時間觸發（週一 9 點總結）或事件觸發（航班延誤更新行程）
- 整合：原生 Gmail/日曆/Drive/Docs/Sheets/Slides/YouTube/Maps；MCP 已支援 Canva/OpenTable/Instacart，**2026 夏** 加 Adobe/Spotify/GitHub/Notion/Slack
- 安全：**Checkpoints** 敏感操作暫停請求人工授權，防 Prompt Injection

## 值得引用的段落
> 「舊模型是 AI 回答你的問題；新模型是 AI 運行你的工作流。」
> 「這不是單純的自動化，而是具備上下文背景的自動化（Automation with context）。」

## 連結到的 wiki
- [[Gemini_Spark]] · [[Google]] · [[MCP]] · [[Agentic_Workflow]] · [[AIOS]]

## 我的問題 / 待追蹤
- 與 Claude Code [[routines]]、[[OpenAI_Codex]] record-and-replay（[[2026-06-27_rpa_要沒了]]）三家「個人 AI 自動化 OS」正面對打，是高價值 synthesis 題材
