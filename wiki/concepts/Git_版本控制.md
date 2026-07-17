---
type: concept
tags: [git, github, vibe-coding, ai, workflow]
created: 2026-07-18
updated: 2026-07-18
sources: [2026-07-18_git_github_vibe_coding基礎]
---

# Git 版本控制（AI 協作視角）

> 對 Vibe Coder 而言，Git 不是工程師的指令集，而是 AI 開發的「保險與回溯系統」＋指揮 Agent 的語言：commit 是存檔點、branch 是風險隔離、worktree 是多 Agent 並行的基礎設施。

## 核心心智模型
- **GitHub = 程式碼專用 Google Drive；Git = 本機版本管理**
- **commit = 絕對安全的檢查點**：AI「發瘋」改壞也能瞬間還原——頻繁試錯的 AI Agent 開發最終防線
- **branch = 風險隔離**：大功能開獨立分支，避免 main 處於「半壞掉狀態」
- **worktree = 第二張實體桌子**：branch 同時只能看一個時空；worktree 給每個分支實體資料夾，讓 Agent A（資料庫）與 Agent B（UI）並行不互相干擾——[[Agent_Teams]] / [[Subagent]] 並行的基礎設施
- **conflict = 決策點**：Vibe Coder 不親手改 code，而是告知 Agent 決策原則（二選一/兩邊保留/改寫合併）

## 關鍵指令對照
| 指令 | AI 協作意義 |
|------|------------|
| `git init` | 開始追蹤資料夾變動 |
| `commit` | 手動存檔點；AI 寫完一段就該存 |
| `push` / `pull` | 推上雲端 / 抓最新版 |
| `clone` | 正式加入專案（優於 download zip，可同步回傳） |
| `branch` → PR → `merge` | 草稿區 → 改動提案審核 → 正式合併 |
| `restore` | 未 commit 前一鍵還原 |
| `revert` | 已 commit 後用反向 commit 抵消（保留修復歷史） |

## 安全紅線
`.gitignore` 是機密保護的絕對必要：必須告知 [[Claude_Code]]「確認機密檔、API Key、密碼都已放入 .gitignore，絕不要 commit 上去」。

## 與其他概念的關係
- [[Vibe_Coding]] 的必學基礎設施：不必成為 Git 專家，但要聽懂 AI 問「要不要 commit / 開 branch」= 問「要不要存檔 / 隔絕風險」
- [[Agent_Teams]]：worktree 是多 agent 並行協作的實體隔離層

## 來源
- [[2026-07-18_git_github_vibe_coding基礎]]
- 另見使用者手寫筆記 raw/notes/2026-07-16_GitEasyLearning.md（尚未 ingest，主題重疊）
