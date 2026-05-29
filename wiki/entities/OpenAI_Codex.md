---
type: entity
entity_type: product
tags: [openai, ai-tool, automation, agentic]
created: 2026-05-30
updated: 2026-05-30
sources: [2026-05-30_codex_零基礎入門, 2026-05-30_codex_office全包辦, 2026-05-30_ai_ppt_codex]
---

# OpenAI Codex

> OpenAI 推出的本地端 AI 工作助理，能「直接動手執行任務」，而非僅回答問題；定位為通用辦公自動化平台。

## 背景
- 原為 OpenAI 的程式碼生成 API，2025-2026 年演進為桌面端全功能 AI 助理
- 對話界面類似 ChatGPT，但能操控本地檔案、連接外部服務、執行排程任務

## 關鍵功能
- **Plugins（外掛程式）**：遵循 NCP 協議，可接 Gmail、Presentations（PPT）、Netlify、Canva 等；類比「Type-C 統一接頭」
- **Skills（技能）**：把 SOP 外置為結構化文件，分專案層級（一次性）與全域層級（跨專案），節省 Token 並穩定行為
- **AGENTS.md**：專案守則文件，Codex 每次執行前主動讀取，確保 AI 在正確脈絡下運作
- **Computer Use**：模仿真人操作瀏覽器，執行填表測試等跨軟體任務
- **三種權限模式**：預設安全（橘色）→ 自動審核 → 完全存取
- **自動化排程**：可設定定時任務（如每日 8 點摘要 AI 新聞）

## 關鍵事實
- PPT 生成：約 8 分鐘生成 10 頁可編輯 PPT，含自我截圖視覺檢查（來自 [[2026-05-30_ai_ppt_codex]]）
- Gmail 整合：自動分類、摘要、批次回覆郵件
- 被定位為 2026 年「AI 做 PPT 最優選」（來自 [[2026-05-30_ai_ppt_codex]]）

## 與其他頁的關係
- 屬於 [[OpenAI]] 的產品
- 與 [[Claude_Code]] 競爭：都是 agentic AI 開發/生產力工具，AGENTS.md vs CLAUDE.md 機制類似
- 與 [[MCP]] 相關：NCP 協議類似 MCP，都是 AI 工具的標準化協議層
- 屬於 [[Agentic_Workflow]] 的落地工具

## 相關來源
- [[2026-05-30_codex_零基礎入門]] — 基礎入門、Plugins/Skills 系統
- [[2026-05-30_codex_office全包辦]] — AGENTS.md + Computer Use 進階案例
- [[2026-05-30_ai_ppt_codex]] — PPT 生成最佳實踐與邏輯分離法則
