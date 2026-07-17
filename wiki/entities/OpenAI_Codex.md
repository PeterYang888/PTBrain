---
type: entity
entity_type: product
tags: [openai, ai-tool, automation, agentic]
created: 2026-05-30
updated: 2026-07-18
sources: [2026-05-30_codex_零基礎入門, 2026-05-30_codex_office全包辦, 2026-05-30_ai_ppt_codex, 2026-06-19_claude_code轉codex, 2026-06-19_loop_engineering, 2026-06-27_image2_codex_可編輯ppt, 2026-06-27_rpa_要沒了, 2026-07-04_claude_codex_互審, 2026-07-04_codex_geo, 2026-07-10_六月_ai_更新彙整, 2026-07-18_codex_record_replay_fork]
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
- **record and replay（2026-06-27）**：在 AI 面前操作一遍即學成可編輯 Skill，把自動化從「指令式」轉為「目標式」，被視為傳統 [[RPA]] 的替代品；整合 Goal / Automations / Heartbeat / Skills 朝 [[AIOS]] 企業作業系統演進（見 [[2026-06-27_rpa_要沒了]]）
  - **抗變化原理（2026-07-10）**：在 **Mac** 上觀測工作流程，記錄的是「**你為什麼要這麼做**」而非座標，因此介面微幅變動時流程仍可執行而不失效。錄下的 Skill 可共享，成為公司數位資產（見 [[2026-07-10_六月_ai_更新彙整]]）

## Session 管理與遠端操控（2026-07-18）
持續性 Agent Workspace 的四組新能力（見 [[2026-07-18_codex_record_replay_fork]]）：
- **懸浮導覽 + Fork**：長對話左側橫線滑動預覽跳轉；每則回覆可分叉出帶完整上下文的平行對話線，從任何歷史節點重試而不污染主線
- **Side Chat（`/side` 或 `/by`）+ Steering**：理解性問題走側邊對話、修正性指令用 `comment + enter` 即時介入——任務分流防上下文污染（對應 [[Claude_Code]] 的 [[side_question|/btw]]）
- **Record & Replay 細節**：外掛安裝；最長錄 30 分鐘；基於 Computer Use（每步思考 10 幾秒），適合固定重複流程、不適合搶票類即時任務
- **手機遠端操控**：QR code 連線；支援進度查看、File Previews、inline review comments；開發者角色從編碼者轉向「移動中的決策者」
- **跨 AI 代理鏈範例**：`Gemini（分析影像）→ Claude（改寫創意）→ Codex（自動化上傳與表格化）`

## 關鍵事實
- PPT 生成：約 8 分鐘生成 10 頁可編輯 PPT，含自我截圖視覺檢查（來自 [[2026-05-30_ai_ppt_codex]]）
- Gmail 整合：自動分類、摘要、批次回覆郵件
- 被定位為 2026 年「AI 做 PPT 最優選」（來自 [[2026-05-30_ai_ppt_codex]]）
- PPT 進階：調用開源 Skill「PPT Master」+ GPT Image 2，把高美感靜態圖轉成元素級可編輯 PPT（6 頁約 6 分 17 秒）（來自 [[2026-06-27_image2_codex_可編輯ppt]]）

## 跨模型互審角色（2026-07-04）
- **Codex 當審稿人**：在 [[Gary_Chen]] 的個人 [[Harness_Engineering|Harness]] 實踐中，Codex 被賦予「守最後一道關」的角色——特點是穩健、無聊但極少出錯，擅長處理複雜後端邏輯；與 Claude（細心、創意、擅互動的「作者」角色）形成分工。見 [[2026-07-04_claude_codex_互審]]

## [[GEO]] 執行引擎（2026-07-04）
- [[黃一河]] 用 Codex 執行「盤點內容 → 結構化 → 建 Wiki → 機器入口 → 追數據 → 強化贏家頁」六步驟 SOP，把內容資產轉成 AI 友善知識庫，實測單頁 30 天被 AI 引用 700+ 次。見 [[2026-07-04_codex_geo]]

## 與 Claude Code 的互補與互轉（2026-06-19）
- **雙引擎策略**：Codex 強在複雜 App / 後端邏輯與深度推理（提供 Low / Medium / High 三檔推理強度）；[[Claude_Code]] 強在開發/風格/快速 Debug
- **無痛互轉（[[工具無關性]]）**：Skills 格式兩邊相同可直接複製；Agents 在 Claude Code 用 `.md`、Codex 用 `.toml`（轉移建 `.agent` 資料夾）；Codex 內輸入 `/` 呼叫 Skill。可在 VS Code / Antigravity / Cursor 用 Extension。見 [[2026-06-19_claude_code轉codex]]
- **[[Loop_Engineering]] 角色**：常擔任 Maker（執行者），由 Claude Code/GPT 當 Tracker（審核者）做觀察反思，避免過擬合

## 與其他頁的關係
- 屬於 [[OpenAI]] 的產品
- 與 [[Claude_Code]] 競爭：都是 agentic AI 開發/生產力工具，AGENTS.md vs CLAUDE.md 機制類似
- 與 [[MCP]] 相關：NCP 協議類似 MCP，都是 AI 工具的標準化協議層
- 屬於 [[Agentic_Workflow]] 的落地工具

## 相關來源
- [[2026-05-30_codex_零基礎入門]] — 基礎入門、Plugins/Skills 系統
- [[2026-05-30_codex_office全包辦]] — AGENTS.md + Computer Use 進階案例
- [[2026-05-30_ai_ppt_codex]] — PPT 生成最佳實踐與邏輯分離法則
- [[2026-06-27_image2_codex_可編輯ppt]] — Image2 + PPT Master Skill 做可編輯 PPT
- [[2026-06-27_rpa_要沒了]] — record and replay 目標式自動化取代 RPA
- [[2026-07-04_claude_codex_互審]] — 跨模型互審：Codex 當審稿人守最後一關
- [[2026-07-04_codex_geo]] — GEO 六步驟 SOP：內容資產轉 AI 友善 Wiki
- [[2026-07-10_六月_ai_更新彙整]] — Record and Reply 的抗變化原理與 Skill 數位資產化
- [[2026-07-18_codex_record_replay_fork]] — Fork / Side Chat / Steering / 手機遠端操控
