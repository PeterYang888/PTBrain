---
type: source
tags: [ai, claude-code, workflow, dynamic-workflows, agent]
created: 2026-06-12
updated: 2026-06-12
source_url: https://www.youtube.com/watch?v=4fpZhuJuIls
source_date: 2026-06-12
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: ""
  processed_by: notebooklm-py
---

# Claude Dynamic Workflow 深度解析與實踐指南

這份簡報文件旨在深入探討 Anthropic 為 Claude Code 推出的新功能：**Dynamic Workflow（動態工作流）**。透過分析其運作機制、與其他功能（如 Skill、Subagent、Agent Team）的差異，以及實際應用場景，協助開發者與決策者判斷何時該採用此技術以優化自動化流程。

## 執行摘要 (Executive Summary)

Dynamic Workflow 是 Claude 的一項進階功能，它允許 Claude 不再僅僅以單一模型身分作業，而是化身為「指揮官」。透過自動生成的 JavaScript 腳本，Claude 可以在背景環境中調動數十甚至上百個 Subagent 同時並行工作（Parallel Processing），並進行多層次的驗證與收斂。

該功能的中心價值在於**「廣度」與「可驗證性」**，它有效解決了單次對話 Context Window（上下文視窗）容易過載的問題，並透過「互相挑錯」的機制提升產出品質。儘管成本較高，但在處理大規模代碼審查、深度研究與複雜遷移任務時，展現了傳統單一 AI 難以企及的效率。

---

## 技術原理解析

### 1. 運作流程
Dynamic Workflow 的本質是 **「AI 幫你寫一段自動化程式碼」**。其運作分為以下階段：
1.  **腳本生成**：用戶下達複雜指令後，Claude 不直接執行，而是先撰寫一段 JavaScript 腳本。
2.  **獨立環境執行**：腳本運行於背景獨立環境，不佔用或阻塞主對話 session。用戶可繼續與 Claude 進行其他交談。
3.  **大規模並行**：腳本會根據任務需求，調動大量 Subagent。例如，第一階段派 5 個 agent 蒐集資料，第二階段派 30 個 agent 深讀，第三階段再派一批 agent 互相驗證。
4.  **結果收斂**：中間產生的海量數據保留在腳本變數中，僅將最後整理好的精簡結論回傳至主對話。

### 2. 核心架構特徵
根據來源文件，一個典型的 Workflow 腳本包含：
*   **元數據 (Metadata)**：定義名稱與用途。
*   **階段化設計 (Stages)**：如搜尋、驗證、報告撰寫。
*   **Agent 關係模型**：
    *   **排隊接力 (Sequential)**：前一階段產出作為後一階段輸入。
    *   **撒網收斂 (Parallel & Aggregate)**：橫向展開多個任務後一次性彙整。

---

## 功能差異化分析

在 Claude 的生態系中，Dynamic Workflow 常與其他專有名詞混淆。區分的關鍵在於：**「下一步是由誰決定的？」**

| 功能名稱 | 核心定義 | 控制權歸屬 | 對 Context 的影響 |
| :--- | :--- | :--- | :--- |
| **Skill** | 食譜/說明書，定義工具使用步驟。 | 寫死在指令中 | 佔據主 Context |
| **Subagent** | 臨時派出的助手，處理單一任務。 | 模型隨機決定 | 過程數據可能塞滿主 Context |
| **Agent Team** | 一個工作群組（PM、工程師、QA），彼此對話辯論。 | 模型間互動 | 動態討論，消耗較多 Context |
| **Dynamic Workflow** | 指揮數百個 Agent 的 **JavaScript 腳本**。 | **程式碼/腳本決定** | **極低**（過程不進入主 Context） |
| **Deep Research** | 內建的特定 Workflow，用於多角度搜尋與交叉驗證。 | 預設腳本 | 極低 |

### 動態層級階梯
1.  **基礎層**：與 Claude 直接對話。
2.  **執行層**：利用 Subagent 平行處理零星雜事。
3.  **溝通層**：利用 Agent Team 讓不同角色互相補位與防禦。
4.  **指揮層**：利用 Workflow 透過腳本指揮大規模軍團，達成複雜且具備可驗證性的目標。

---

## 優勢與劣勢分析

### 優勢 (Strengths)
*   **節省主 Session 負擔**：中間過程不污染 Context Window，避免對話變得「臃腫」或反應遲鈍。
*   **可觀測與重跑**：因為是程式碼，可以儲存、重複調用，並能精確觀察每個階段的 token 消耗與進度。
*   **極高的可靠性**：內建「多角驗證」與「互相反駁」機制，產出品質優於單次推理。
*   **規模化處理**：具備同時處理上百個檔案或多個資料來源的能力。

### 劣勢 (Weaknesses)
*   **高成本**：每個 Subagent 都是一次完整的 API 調用，大量並行會迅速消耗 Token。
*   **開發階段限制**：目前仍處於 Research Preview 階段。
*   **不適合日常瑣事**：對於修改數行程式碼或簡單查詢，使用 Workflow 屬於「殺雞用牛刀」。

---

## 操作指南與指令範例

### 觸發方式
1.  **關鍵字觸發**：在 Prompt 中直接加入 `workflow`。
2.  **調整推理模式**：使用 `effort` 指令。
    *   `effort: ultra`：Claude 會進入高推理模式，自動判斷是否開啟 Workflow 並進行複雜編排（注意：此模式較貴）。
3.  **內建深度研究**：使用斜線指令。
    *   `/deep-research`：自動啟動多角度搜尋與表決過濾機制。

### 進度管理
*   **查詢進度**：輸入 `/workflows` 即可看到當前各階段運作狀況、Agent 數量、消耗 Token 與執行時間。
*   **預算控制**：在下達指令時，可直接限制預算上限。

---

## 成本優化策略

1.  **模型分級制度**：撒網階段用 Haiku，收斂推理階段用 Opus。
2.  **預算硬上限**：下指令時明確規定 Token 燒毀限制，觸及臨界點自動停止。
3.  **小範圍測試**：先針對單一資料夾或特定問題運行，確認腳本邏輯與成本後再放大規模。

---

## 推薦應用場景

*   **全代碼庫 Bug 掃描**：多 agent 找 bug，再派另一批 agent 驗證與反駁
*   **多維度 Code Review**：從效能、資安、可讀性等多個角度同時審查大型 PR
*   **跨來源深度研究**：同時翻閱官方文件、論文、社群討論，交叉核實後產出附有出處的報告
*   **大規模代碼遷移**：一次性處理數百個檔案的架構更動
