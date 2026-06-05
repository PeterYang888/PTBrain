---
type: entity
entity_type: product
tags: [anthropic, ai-dev-tool, agent]
created: 2026-04-17
updated: 2026-06-06
sources: [2026-04-15_claude_code_desktop_routines改版, 2026-04-16_claude_模型選擇指南, 2026-05-16_claude_code_代理工具, 2026-05-16_claude_code_obsidian_知識庫, 2026-05-16_claude_code_人物蒸餾, 2026-06-06_11天_claude_code_dynamic_workflows]
---

# Claude Code

> [[Anthropic]] 推出的 agentic 程式開發工具。付費方案進階功能之一，支援跨檔案任務、自主調用工具、執行複雜程式碼。提供 CLI 與桌面 app 兩種形態，行為對等。

## 桌面 app（2026-04-14 改版後）
為**多線並行**工作流設計。核心組件：

- **側邊欄**：集中管理所有進行中與近期 session；可依狀態 / 專案 / 環境篩選；PR 合併或關閉時 session 自動歸檔
- **[[side_question]]**：透過 `/btw` 啟動側邊提問，讀取當前上下文但不呼叫工具、不影響主執行緒
- **整合終端機**：session 旁邊同步跑測試或 build
- **檔案編輯器**：直接開啟、編輯、儲存
- **diff 檢視器**：針對大型變更集重新優化
- **預覽面板**：本地伺服器 / HTML / PDF 即時預覽
- **SSH 遠端**：已從 Linux 擴展至 Mac
- **顯示模式**：Verbose / Normal / Summary，可調工具呼叫透明度
- 所有面板支援拖放排列

## CLI
與桌面版行為完全對等。組織集中管理或個人安裝的外掛，兩邊通用。

## 雲端自動化：[[routines]]
2026-04-14 同步推出的研究預覽功能。把 Claude Code 配置（提示詞 + 程式庫 + connectors）封裝成可排程、可由 API 或 GitHub 事件觸發的自動化 job，關電腦也能跑。

## 模型搭配建議
- 複雜除錯、長任務：[[Claude_Opus_4.6]]
- 日常程式生成、refactor、測試：[[Claude_Sonnet_4.6]]
- 大量批次、原型快速迭代：[[Claude_Haiku_4.5]]

## 代理工具 / 開源生態
- **Free Claude Code**（2026-05）：開源代理工具（GitHub 萬星），讓不同 IDE 和 Claude Code 互通，解決官方版本鎖定問題。見 [[2026-05-16_claude_code_代理工具]]。

## 知識庫整合
- **Claude Code + [[Obsidian]]**：以結構化 Wiki + index 取代傳統 [[RAG]] 碎片化檢索，Token 用量減少 95%。AI 讀「書」而非「碎紙片」，能理解頁面間的交叉引用關係。見 [[2026-05-16_claude_code_obsidian_知識庫]]。

## Dynamic Workflows（JS 驅動工作流）
- **核心機制**：以 JavaScript 腳本取代 Prompt 協調多個 Sub-agent；中間數據封裝於 JS 變數，主 context 只存最終結果，大幅節省 Token
- **規模**：最多 16 個 Agent 並行；官方案例：11 天 75 萬行 C++ → Rust 遷移
- **觸發方式**：`deep-search`（內建）、`workflow` 關鍵字（可存 JS 檔）、Ultra Code 模式（自動撰寫）
- **監控**：`/workflows` 或 `wf` 查看進度，按 `s` 儲存腳本供重用
- 詳見 [[Dynamic_Workflows]]、[[2026-06-06_11天_claude_code_dynamic_workflows]]

## 進階應用
- **[[人物蒸餾]]**：用 Claude Code + GitHub Skill（Queen Skill）提取名人（Naval Ravikant、Elon Musk 等）的公開資料，建構具有其三層思維結構的 AI 顧問。見 [[2026-05-16_claude_code_人物蒸餾]]。

## 相關來源
- [[2026-04-15_claude_code_desktop_routines改版]]
- [[2026-04-16_claude_模型選擇指南]]
- [[2026-05-16_claude_code_代理工具]]
- [[2026-05-16_claude_code_obsidian_知識庫]]
- [[2026-05-16_claude_code_人物蒸餾]]
