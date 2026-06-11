---
type: concept
tags: [ai, claude-code, knowledge-graph, open-source, workflow]
created: 2026-06-12
updated: 2026-06-12
sources: [2026-06-12_graphify_claude_code]
---

# Graphify

> 開源工具，透過三階段分析將程式碼庫轉為知識圖譜，解決 Claude Code 在大型 repo 中「只能 grep 不能導航」的問題，實測 Token 節省 60%。

## 詳細說明
傳統 AI 編碼助手用 `grep`（全文搜尋）找檔案，Graphify 改為建立由節點（Nodes）、邊（Edges）、社群（Communities）組成的知識圖譜，讓 AI 理解代碼間的邏輯關係（"why" behind connections），而非只找到位置。

## 三階段建圖流程
| 階段 | 技術 | 內容 | 成本 |
| :--- | :--- | :--- | :--- |
| Pass 1（確定性） | Tree-sitter | 類別/函式/import/call graph/行內註釋 | 零（本地，無 LLM） |
| Pass 2（影音） | Faster Whisper | 影片/音檔轉錄為可索引文字 | 本地運算 |
| Pass 3（語義） | LLM | PDF/文件/論文/圖像的語義分析 | LLM API 費用 |

## 核心概念
- **節點 (Nodes)**：程式碼單元（函式、檔案）
- **上帝節點 (God Nodes)**：連接數最多的核心節點；快速理解新 repo 的入口
- **邊 (Edges)**：節點間的引用/呼叫/邏輯關聯
- **社群 (Communities)**：性質相似的節點聚類，幫助 AI 理解模組邊界

## 關鍵 CLI
```bash
/graphify .           # 在當前目錄建立初始圖譜
graphify query "..."  # 強制 AI 透過圖譜回答
graphify hook install # Git Hook：每次 commit 後自動重建（Pass 1，零 API 成本）
graphify claw install # 常駐 hook，AI 回答時預設使用圖譜
graphify --obsidian   # 匯出為 Obsidian Vault
```

## 與其他概念的差別
- 跟 [[RAG]]：Graphify 針對程式碼庫，不需要向量 embedding；RAG 針對非結構化文件，依賴向量相似度
- 跟 [[Dynamic_Workflows]]：Graphify 提供靜態知識地圖，Dynamic Workflows 是動態 agent 編排；兩者互補
- 跟 Obsidian：都是結構化知識管理，Graphify 的輸入是程式碼庫，可 `--obsidian` 匯出橋接

## 實測數據
- Open Design repo：203 檔案 → 197 nodes、3,447 edges、109 communities
- Token：200K（無 Graphify）→ 80K（有 Graphify），節省 60%

## 應用場景
- 接手大型陌生 repo 前：先 `/graphify .` 建地圖
- 長期專案：`graphify hook install` 維持圖譜與程式碼同步
- 團隊協作：圖譜可共享，保持所有 AI 助手的一致理解

## 來源
- [[2026-06-12_graphify_claude_code]]
