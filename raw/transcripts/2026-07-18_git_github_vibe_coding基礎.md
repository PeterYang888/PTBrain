---
type: source
tags: [ai, claude-code, workflow]
created: 2026-07-18
updated: 2026-07-18
source_url: https://www.youtube.com/watch?v=atqcAb7MFAM
source_date: 2026-07-18
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "Gary Chen"
  processed_by: notebooklm-py
---

## 一句話摘要
本教學旨在幫助非技術背景的 AI 開發者（Vibe Coders）掌握 Git 與 GitHub 的核心邏輯，透過版本控制與分支管理，確保 AI Agent 協作過程中的代碼安全與平行開發效率 [1-3]。

## 主講者背景
*   **Gary Chen**：AI 技術觀察家與開發流程專家，專注於降低非工程師進入 AI 開發的門檻，強調「定義問題」與「指揮 Agent」優於手寫指令 [1, 3]。

## 核心論點
*   **Git 是 AI 開發的「保險與回溯系統」**：對於頻繁試錯的 AI Agent，Git 提供的 `commit` 功能是防止代碼被 AI 「發瘋」改壞的最終防線，確保隨時可恢復至安全狀態 [4, 5]。
*   **分支（Branch）實現風險隔離**：強烈建議在開發大功能時開啟獨立 `branch`，避免 AI 在試錯過程中讓主線 `main` 處於不穩定的「半壞掉狀態」 [6, 7]。
*   **Worktree 解決多 Agent 協作瓶頸**：傳統 `branch` 在同一時間只能顯示一個時空，透過 `worktree` 產生的實體資料夾，可讓多個 Agent 同時在不同分支上並行工作而不互相干擾 [7-9]。
*   **從「指令操作」轉向「決策管理」**：Vibe Coder 的核心價值在於對 `conflict`（衝突）下達產出決策，而非親自修改程式碼，將 Git 指令視為指揮 Agent 的語言 [2, 3, 10]。

## 關鍵細節與數據
### 1. 基礎開發指令與行為
*   **`git init`**：告知 Git 開始追蹤此資料夾的所有變動 [4]。
*   **`commit`**：本地端的「手動存檔點」。AI 寫完一段程式碼後，應主動執行 `commit` 並寫下清楚的修改訊息 [5, 11]。
*   **`push`**：將本地存檔推送到遠端雲端倉庫（GitHub） [11]。
*   **`clone`**：正式加入專案並下載完整追蹤紀錄（優於 `download zip`，後者無法同步回傳改動） [12, 13]。
*   **`pull`**：從雲端抓取他人或 AI 產出的最新版本到本地電腦 [13, 14]。

### 2. 安全性與環境隔離
*   **`.gitignore`**：絕對必要的機密保護。必須告知 Claude Code：「確認機密檔、API Key、密碼都已放入 `.gitignore`，絕不要 `commit` 上去」 [11, 12]。
*   **`origin main`**：`origin` 代表遠端 GitHub 地址，`main` 代表專案的正式穩定版 [12]。

### 3. 進階 Agent 工作流
*   **`branch` (分支)**：從 `main` 切出的開發草稿區，目的是讓「開發中功能」與「穩定功能」井水不犯河水 [6, 7]。
*   **`worktree` (工作樹)**：為每個分支創建獨立的實體資料夾。
    *   **應用場景**：Agent A 在資料夾 A 處理資料庫功能，Agent B 在資料夾 B 處理 UI 畫面，平行效率最大化 [8, 9]。
*   **`PR` (Pull Request)**：改動提案，用於讓大家審核 AI 寫好的功能 [9]。
*   **`merge`**：將通過審核的代碼正式合併回 `main` [9]。

### 4. 錯誤復原機制
*   **`restore`**：尚未 `commit` 前，一鍵還原到上個存檔點 [15]。
*   **`revert`**：已 `commit` 後，透過新增一個「反向 commit」來抵消之前的錯誤，適合在協作專案中使用以保留完整修復歷史 [15]。

## 重要引言
*   **關於版本控制**：
    > 「GitHub 是程式碼專用 Google Drive，而 Git 則是幫你在本機端管理程式碼版本的工具。」 [1, 5]
*   **關於開發安全**：
    > 「Commit 最大的價值在於它幫你的程式碼建立了一個絕對安全的檢查點... 就算 AI 發瘋，你都可以瞬間還原。」 [5]
*   **關於 AI 協作概念**：
    > 「Branch 像是同一張桌子上切換不同時空，同一時間你只能看見一個畫面；而 Worktree 則是直接給你第二張實體桌子。」 [8]
*   **關於 Vibe Coding 的本質**：
    > 「你不需要變成長 Git 專家，但你要知道當 AI 問你要不要 commit、開 branch 時，它是問你要不要先存檔或隔絕風險。」 [3]

## 與其他工具的關聯
*   **Claude Code / Cursor**：主要的執行 Agent。當遇到 `conflict` 時，應告知 Agent 決策原則（如：「以朋友的邏輯為主，但保留我的理財分類」），讓 AI 執行 `二選一`、`兩邊保留` 或 `改寫合併` [3, 10, 14]。
*   **GitHub**：作為雲端中心，處理 PR 審核與團隊協作權限（Collaborators）管理 [9, 12]。
*   **API / 金流串接**：開發過程中必須配合 `.gitignore` 防止密鑰外洩至 GitHub 公開環境 [11]。
*   **Patreon 資源**：提供 27 個常見 Git 情境對照表，包含具體的 AI 提示詞範例 [3]。
