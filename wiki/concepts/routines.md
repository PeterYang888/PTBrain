---
type: concept
tags: [anthropic, claude-code, automation, agent]
created: 2026-04-17
updated: 2026-04-17
sources: [2026-04-15_claude_code_desktop_routines改版]
---

# routines

> [[Claude_Code]] 的雲端自動化功能，2026-04-14 以研究預覽（research preview）形式推出。將提示詞、程式庫、connectors 打包成一組可重複觸發的自動化配置，關筆電也能跑。

## 組成
一個 routine 包含：
- **提示詞**：告訴 Claude 要做什麼
- **程式庫**：要操作的 repo
- **connectors**：連接外部系統（具體支援對象待查）

## 三種觸發方式
| 觸發 | 例子 |
|---|---|
| **排程** | 每天晚上、每週一次，時間到了自動跑（像鬧鐘） |
| **API 呼叫** | 接到其他系統訊號就動（像部署完自動跑測試） |
| **GitHub 事件** | 有人發 PR 或合併程式碼就觸發（像自動 code review） |

## 官方範例用途
- **排程型**：每晚掃新 issue 發 Slack 摘要；每週盤點 PR 找該更新的文件並自動開 PR
- **部署觸發型**：上線後跑煙霧測試 + 掃錯誤日誌，判斷本次上線是否有問題
- **GitHub 觸發型**：PR 開啟自動跑團隊安全/效能檢查清單；Python SDK 合併的改動自動搬到 Go SDK

## 每日額度
| 方案 | 每日上限 |
|---|---|
| Pro | 5 |
| Max | 15 |
| Team / Enterprise | 25 |

超額需啟用額外用量計費。

## 為什麼重要
把 [[Claude_Code]] 從「開發者手上的即時 agent」擴展為「後台 24 小時跑的自動化 worker」。方向與 [[Anthropic]] 想擁有開發者 AI 工作流入口的策略一致。

## 爭議 / 未定論
- 額度設計：5–25 次/日 對複雜團隊流程夠嗎？超額計費細節待進一步揭露。
- connectors 生態系範圍：目前只看到 Slack、GitHub 的例子。

## 相關來源
- [[2026-04-15_claude_code_desktop_routines改版]]
