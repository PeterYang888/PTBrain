---
type: source
tags: [ai, git, vibe-coding, workflow]
created: 2026-07-18
source_url: https://www.youtube.com/watch?v=atqcAb7MFAM
source_date: 2026-07-18
source_type: transcript
---

# 給非技術人員的 GitHub 教學：Vibe Coding 必學的基礎技能

> 來源：[原始檔](../../raw/transcripts/2026-07-18_git_github_vibe_coding基礎.md) · [[Gary_Chen]]

## 一句話摘要
面向 Vibe Coder 的 [[Git_版本控制]] 教學：Git 是 AI 開發的「保險與回溯系統」，核心價值在於讓非工程師能對 AI Agent 的試錯下決策，而非親手寫指令。

## 核心論點
- **Git 是 AI 開發的最終防線**：`commit` = 絕對安全的檢查點，AI「發瘋」改壞也能瞬間還原
- **Branch 實現風險隔離**：大功能開獨立 branch，避免 main 處於「半壞掉狀態」
- **Worktree 解決多 Agent 協作瓶頸**：branch 同時只能看一個時空；worktree 給每個分支實體資料夾，多 Agent 並行不互相干擾
- **從指令操作轉向決策管理**：Vibe Coder 的價值是對 conflict 下產出決策（二選一/兩邊保留/改寫合併），Git 指令是指揮 Agent 的語言

## 關鍵指令對照（AI 協作視角）
- `git init` 開始追蹤；`commit` 本地存檔點；`push` 推上 GitHub；`clone` 正式加入專案（優於 download zip）；`pull` 抓最新版
- `.gitignore`：必須告知 Claude Code「確認機密檔、API Key、密碼都已放入 .gitignore，絕不要 commit 上去」
- `restore`：未 commit 前一鍵還原；`revert`：已 commit 後用反向 commit 抵消（保留修復歷史）
- `branch` → `PR` → `merge`：開發草稿 → 改動提案審核 → 正式合併

## 值得引用的段落
> 「GitHub 是程式碼專用 Google Drive，而 Git 則是幫你在本機端管理程式碼版本的工具。」

> 「Branch 像是同一張桌子上切換不同時空……Worktree 則是直接給你第二張實體桌子。」

> 「你不需要變成 Git 專家，但你要知道當 AI 問你要不要 commit、開 branch 時，它是問你要不要先存檔或隔絕風險。」

## 連結到的 wiki
- [[Git_版本控制]]（新建 concept）
- [[Vibe_Coding]] · [[Claude_Code]] · [[Gary_Chen]]
- [[Agent_Teams]]（worktree 多 agent 並行是其基礎設施）

## 我的問題 / 待追蹤
- 與 raw/notes/2026-07-16_GitEasyLearning.md（使用者手寫筆記，尚未 ingest）主題重疊，之後 ingest 該筆記時合併觀點
