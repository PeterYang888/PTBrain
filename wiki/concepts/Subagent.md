---
type: concept
tags: [ai, agent, multi-agent, workflow, claude-code]
created: 2026-07-10
updated: 2026-07-10
sources: [2026-07-10_agent_teams_協作模式]
---

# Subagent

> 多 Agent 協作的**執行層**：各 subagent 獨立執行任務、獨立回報結果，彼此之間不互相溝通。適合定義明確且可並行的任務。

## 詳細說明
Subagent 是最單純的多 Agent 形態——主 agent 派工，subagent 各自完成後回報。因為沒有橫向溝通，它避免了訊息往返的成本，但也無法處理「子任務彼此需要對齊」的情境。

在 [[Dynamic_Workflows]] 頁的 4 層功能階梯中，Subagent 屬「執行層」，控制權歸模型（模型自行決定何時派工），其代價是**主 context window 可能被 subagent 的回傳內容塞滿**。

## 適用與不適用
- ✅ 定義明確、彼此獨立、可完全並行的任務（例如：分頭讀 10 個檔案各自摘要）
- ❌ 子任務需要互相對齊 → 改用 [[Agent_Teams]]
- ❌ 需要確定性流水線與極低 context 佔用 → 改用 [[Dynamic_Workflows]]
- ❌ 任務前置依賴強（一步接一步）→ 單一 agent 即可

## 與其他概念的差別
| | Subagent | [[Agent_Teams]] | [[Dynamic_Workflows]] |
|---|---|---|---|
| 橫向溝通 | 無 | 有（群組訊息） | 由腳本協調 |
| 控制權 | 模型 | 模型間互動 | 腳本／程式碼 |
| Context 影響 | 可能塞滿 | 較多 | 極低 |

## 來源
- [[2026-07-10_agent_teams_協作模式]]
