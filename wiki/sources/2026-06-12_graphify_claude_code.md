---
type: source
tags: [ai, claude-code, workflow, knowledge-graph, open-source]
created: 2026-06-12
source_url: https://www.youtube.com/watch?v=ChskqGovoHg
source_date: 2026-06-12
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# This Open Source Repo Just Solved Claude Code's #1 Problem

> 來源：[原始檔](../../raw/transcripts/2026-06-12_graphify_claude_code.md) · [[Claude_Code]]

## 一句話摘要
Graphify 是開源工具，透過三階段（Tree-sitter 解析 → Whisper 轉錄 → LLM 語義）建立知識圖譜，取代 Claude Code 用 grep 盲搜的方式，實測 Token 消耗從 200K 降至 80K（節省 60%）。

## 核心論點
- **地圖 vs. 搜索**：Claude Code 預設用 grep（Ctrl+F）搜尋程式碼，Graphify 提供 nodes/edges/communities 的結構地圖，AI 能理解「為什麼連接」而非只找到「在哪裡」
- **三階段零到有**：Pass 1（Tree-sitter 確定性解析，免費無 API 成本）→ Pass 2（Faster Whisper 影音轉文）→ Pass 3（LLM 語義分析，RAG-lite 但不需 embedding）
- **Token 節省 60%**：Open Design repo（203 檔案）測試：無 Graphify 200K token → 有 Graphify 80K token
- **零成本自動維護**：`graphify hook install` 在每次 git commit 後自動重建圖譜，重建過程主要走 Pass 1（確定性），不產生 API 費用
- **工具定位**：介於 Obsidian（結構筆記）與傳統 Graph RAG（向量搜尋）之間；`--obsidian` 旗標可直接匯出為 Obsidian Vault

## 關鍵 CLI 指令
| 指令 | 說明 |
| :--- | :--- |
| `/graphify .` | 在當前目錄建立初始知識圖譜 |
| `graphify query [question]` | 強制 AI 透過圖譜回答，避免憑直覺回答 |
| `graphify hook install` | 安裝 Git Hook，每次 commit 後自動重建（零 API 成本） |
| `graphify claw install` | 安裝為常駐 hook，AI 回答時預設使用圖譜 |
| `--obsidian` | 匯出為 Obsidian Vault |

## 值得引用的段落
> 「這為 Claude Code 提供了一張地圖，而單純搜尋檔案（grepping）完全無法提供地圖。」

> 「Graphify 介於 Obsidian 和真正的 RAG 系統之間。工具越多，我們就越能根據工作需求選擇合適的工具。」

## 連結到的 wiki
- [[Graphify]]
- [[Claude_Code]]
- [[RAG]]
- [[Agentic_Workflow]]

## 我的問題 / 待追蹤
- Graphify 的 GitHub repo 名稱？（影片未提供連結，需補）
- Pass 3 使用哪個 LLM？是本地模型還是 API？成本估算？
