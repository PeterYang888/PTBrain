---
type: concept
tags: [ai, agent, loop-engineering, harness, workflow]
created: 2026-06-19
updated: 2026-06-19
sources: [2026-06-19_loop_engineering, 2026-06-19_ai復活老遊戲]
---

# Loop Engineering（循環工程）

> 為 AI Agent 設計具自我迭代、觀察反思、工具調用的「閉環系統」，讓系統替人去提示、檢查、糾偏；AI 工程化階梯的最新一層。

## 詳細說明
槓桿正從「寫好一次性 Prompt」轉向「設計 Loop」。閉環邏輯：目標設定 → 規劃任務 → 執行 → **觀察與反思（Observe/Reflect）** → 改進 → 進入下一輪。目標是讓 Agent 在特定條件/頻率自動「醒來」執行，從手動提示轉為自動化生產系統。

## 工程化四階段
1. Prompt Engineering（單次理解）
2. Workflow / [[Context_工程|Context Engineering]]（任務串聯）
3. [[Harness_Engineering]]（執行環境與權限）
4. **Loop Engineering（自我演進的閉環）**

## 5+1 模塊框架（Addy 定義）
1. **Automation（心跳）** — 誰來啟動（Codex 心跳 / Claude Code 定時任務）
2. **Worktree（隔離倉）** — 並行不衝突，共享 Git 歷史
3. **Skill（技能插件）** — 沉澱工作流，`/` 斜槓呼叫
4. **Connector（連接器）** — [[MCP]]、API、插件帶來泛化能力
5. **Sub-agents（子代理）** — 執行/審核分離，各自花 Token
6. **Memory（狀態記憶）** — 經驗寫回 repo，知識複利
- 配套機制：Dry run / Smoke test、Acceptance Criteria、最小權限 + **Human Gate**、Observability

## 關鍵特徵：Maker / Tracker 角色分離
讓「制圖者/執行者」與「檢查者/審核者」分離（如 Codex 執行、Claude Code 觀察反思），避免過擬合、提升準確率。[[2026-06-19_ai復活老遊戲]] 的「Opus 規劃、Sonnet 執行」即此模式的雙模型版。

## 與其他概念的關係
- 上承 [[Harness_Engineering]]，是其之上的方法論層
- 與 [[Dynamic_Workflows]]：Dynamic Workflows 是 Claude Code 的 JS 腳本實作；Loop Engineering 是更廣的閉環設計哲學
- 實踐者：[[Claude_Code]]、[[OpenAI_Codex]]

## 來源
- [[2026-06-19_loop_engineering]]（[[Boris_Cherny]]「My job is writing loop」、[[Peter_Steinberger]]、Addy）
- [[2026-06-19_ai復活老遊戲]]（Opus/Sonnet 雙模型實踐）
