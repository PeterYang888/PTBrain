---
type: source
tags: [ai, agent, loop-engineering, harness]
created: 2026-06-19
source_url: https://www.youtube.com/watch?v=fS-3o4Tz5cI
source_date: 2026-06-19
source_type: transcript
---

# Loop Engineering 火了：AI Agent 的槓桿，正在從 Prompt 移到 Loop

> 來源：[原始檔](../../raw/transcripts/2026-06-19_loop_engineering.md) · 頻道：靈姐說 AI（靈姐）

## 一句話摘要
AI Agent 的槓桿正從「提示詞工程」轉向 **[[Loop_Engineering|循環工程]]**：設計具自我迭代、觀察反思、工具調用的閉環系統，實現高可靠且有複利效應的自動化工作流。

## 核心論點
- **從 Prompt 轉向 Loop**：核心槓桿是為 Agent 設計循環，讓系統替人去提示、檢查、糾偏
- **工程化四階段**：Prompt Engineering → Workflow/[[Context_工程|Context Engineering]] → [[Harness_Engineering]] → **Loop Engineering**
- **Maker / Tracker 角色分離**：執行者與審核者分離（如 Codex 執行、Claude Code 觀察反思），避免過擬合、提升準確率
- **減少人工介入**：讓 Agent 在特定條件/頻率自動「醒來」執行，從手動提示轉向自動化生產系統
- **企業級考量**：Token 成本、失敗率、權限風險、可審計性，需把 Agent 升級為可控的 Loop

## 關鍵框架：Loop Engineering 5+1 模塊（Addy 定義）
1. **Automation（心跳）** — 誰來啟動；Codex 心跳、Claude Code 定時任務
2. **Worktree（隔離倉）** — 並行不衝突，共享 Git 歷史
3. **Skill（技能插件）** — 沉澱工作流，`/` 斜槓呼叫
4. **Connector（連接器）** — [[MCP]]、API、插件，泛化能力
5. **Sub-agents（子代理）** — 執行/審核分離，各自花 Token
6. **Memory（狀態記憶）** — 經驗寫回 repo，知識複利
- 配套：Dry run / Smoke test 驗證、Acceptance Criteria、最小權限 + **Human Gate**、Observability（記錄任務拆解與動作日誌）

## 值得引用的段落
> Boris Cherny（[[Claude_Code]] 負責人）：「My job is writing loop.」
> Addy：「Sub-agents keep the maker away from the tracker.」

## 連結到的 wiki
- [[Loop_Engineering]] · [[Harness_Engineering]] · [[Agentic_Workflow]] · [[Dynamic_Workflows]] · [[MCP]] · [[Claude_Code]] · [[OpenAI_Codex]] · [[Boris_Cherny]] · [[Peter_Steinberger]]

## 我的問題 / 待追蹤
- Addy 全名與來源（疑為 Addy Osmani）？
- 與 [[Dynamic_Workflows]] 的關係：Loop Engineering 是其上層方法論還是平行概念？
