---
type: source
tags: [ai, codex, workflow, automation]
created: 2026-07-18
source_url: https://www.youtube.com/watch?v=pJR6I9_06e4
source_date: 2026-07-18
source_type: transcript
---

# Codex 新功能教學：Record & Replay、對話快搜、Fork、手機遠端操控

> 來源：[原始檔](../../raw/transcripts/2026-07-18_codex_record_replay_fork.md) · [[Gary_Chen]]

## 一句話摘要
[[OpenAI_Codex]] 透過 Record & Replay、Fork 與手機遠端操控，從代碼助手轉型為具備「觀察學習」與「跨時空調度」能力的持續性 Agent Workspace。

## 核心論點
- **從提示工程轉向「示範工程」**：Record & Replay 讓非技術人員用「手把手示範」取代寫 prompt/skill，把操作固化為穩定工作流
- **平行時空式專案管理（Fork）**：從任何歷史節點分叉出帶完整上下文的平行對話線，避免單一 session 被錯誤引導帶偏
- **任務分流防上下文污染**：「理解性需求」走 Side Chat、「修正性指令」走 Steering，保護主線心流
- **碎片化管理轉型**：遠端操控讓開發者從「編碼者」變「決策者」，在移動中審核與批准

## 關鍵操作細節
- **懸浮導覽**：長對話左側空白橫線滑動預覽、點擊跳轉
- **Fork**：每則回覆下方分叉按鈕，複製完整上下文的平行線
- **Side Chat**：CLI 指令 `/side` 或 `/by`；問背景知識不佔主線運算
- **Steering**：`Enter` 排隊；`comment + enter` 即時「敲門介入」
- **Record & Replay**：外掛程式搜尋 `record and replay` 安裝；觸發用 `/`、`@` 或「錄製我的操作並學習記錄」；最長 30 分鐘；基於 Computer Use（每步思考 10 幾秒），適合固定重複流程、不適合搶票類即時任務
- **手機遠端**：設定 → 連線 → 開啟「可控制此電腦的裝置」→ QR code；支援進度查看、File Previews、Side Chat、inline review comments；無法直開 `localhost:3000`，需指揮 Codex 用 in-app browser 截圖回傳

## 跨 AI 代理鏈範例
`Gemini（分析影像）→ Claude（改寫創意）→ Codex（自動化上傳與表格化）`——各取所長的 multi-agent chain。

## 值得引用的段落
> 「這功能你可以把它理解成在手把手教一個實習生……以前最痛苦的是那些你早就習慣到不用動腦的細節要想辦法講得清楚，現在你可以先示範。」

> 「手機已經慢慢變成我在外面拿來做決策的遠端指揮台。」

## 連結到的 wiki
- [[OpenAI_Codex]] · [[RPA]]（Record & Replay 是目標式自動化取代 RPA 的延伸）
- [[Gary_Chen]] · [[side_question]]（Claude Code `/btw` 的 Codex 對應物）
- [[Agentic_Workflow]]

## 我的問題 / 待追蹤
- Claude Code 是否會跟進 Record & Replay 式的示範學習？
