---
type: source
tags: [Stanford, Agentic_Workflow, RAG, Prompt_Engineering, LLM, 多智能體, ai-tooling]
created: 2026-05-16
source_url: https://www.youtube.com/watch?v=eKW9ITaltWw
source_date: 2026-05-16
source_type: transcript
---

# 史丹佛 AI 系統課程深度解析：從大型語言模型到 Agentic Workflow

這份簡報文件旨在深入探討史丹佛大學「BLLM」課程的核心內容，解析 AI 工程師如何透過「重軸（Augmenting LLM）」技術，將基礎語言模型轉化為具備商業價值的實戰系統。

---

## 執行摘要

目前的 AI 發展可分為橫軸（提升基礎模型能力）與重軸（工程技術疊加）。對大多數開發者與企業而言，真正的價值在於**重軸（Augmenting LLM）**的應用。透過提示詞工程（Prompt Engineering）、檢索增強生成（RAG）以及 Agentic Workflow，開發者能克服基礎模型缺乏專業知識、資訊落後、難以控制以及長文本理解力退步等四大限制。

---

## 關鍵主題詳細分析

### 1. 強化單一模型的技術路徑

*   **提示詞工程 (Prompt Engineering)：** 最重要的技術是**提示詞鏈（Prompt Chaining）**，將複雜任務拆解為多個獨立 Prompt，前一個的輸出作為後一個的輸入，以提升可觀察性與測試效率。
*   **微調 (Fine-tuning)：** 史丹佛教授建議「能不做就不做」。僅在法律、科學等需要極高重複精度，或基礎模型表現極其吃力的特定領域才建議使用。
*   **檢索增強生成 (RAG)：** 解決模型幻覺與資訊落後的標準方案。透過向量資料庫（Vector Database）儲存語義向量，並利用**分塊（Chunking）**與多層次存儲技術，在模型推理時提供精確的外部參考文件。

### 2. 從單一模型到系統設計 (Agentic Workflow)

#### 傳統軟體與 Agentic AI 軟體的對比
| 維度 | 傳統軟體 | Agentic AI 軟體 |
| :--- | :--- | :--- |
| **資料類型** | 結構化資料 (JSON, DB) | 自由文本、圖片、音訊 |
| **邏輯特性** | 確定性 (Deterministic) | 模糊性 (Fuzzy) |
| **架構思維** | 精確控制執行路徑 (Microservices) | 目標管理 (Manager Mindset) |
| **測試方式** | 可重複、確定性測試 | 迭代、探索式測試 |

#### 智能體 (Agent) 的三核心要素
1.  **提示詞 (Prompt)：** 定義角色與權限範圍。
2.  **上下文管理 (Context Management)：** 區分短期記憶（Working Memory）與長期記憶（Archival Memory），在有限窗口內保留關鍵資訊。
3.  **工具 (Tools)：** 賦予 Agent 執行能力（如搜尋、預訂、支付）與查詢能力（如訪問 CRM 或資料庫）。

### 3. 評估體系 (Evaluation/Evals)
評估是 AI 系統能否進入生產環境（Production）的命脈。三個維度的評估框架：

*   **整體 vs 組件：** 看最終回覆的滿意度，也看每一步拆解動作的精準度。
*   **客觀 vs 主觀：** 客觀指標可由腳本驗證；主觀指標需人工評分或使用 **LLM-as-judge**。
*   **定量 vs 定性：** 統計成功率與延遲，並深入分析幻覺發生的原因。

### 4. 多智能體協作 (Multi-agent Systems)
多智能體系統適用於需要「平行處理」或「跨團隊復用」的複雜場景。溝通模式分為：
*   **科層制 (Hierarchical)：** 由一個統籌者（Orchestrator）派工，結構清晰。
*   **扁平制 (Flat)：** 智能體之間直接互通。
*   **MCP (Model Context Protocol)：** 作為通用協議層，讓 Agent 不需認識每個 API，簡化智能體間的通信。

---

## 重要語錄與背景解析

> **「Prompt Engineering 不會是一個職業，因為它是每個工程師都該會的基本技能，就像九九乘法表一樣。」**

> **「Agentic 系統的思維是 Think like a manager：你給 AI 一個目標和限制，讓它自己決定怎麼完成。」**

> **「Fuzzy 的問題一定要加上 Human-in-the-loop。」**

---

## 具體實踐指引

1.  **任務拆解 (Task Decomposition) 第一優先：** 先觀察真人如何處理該任務，將大任務拆解成細碎的小步驟，決定哪些步驟使用確定性代碼，哪些使用 LLM。

2.  **採用「硬編碼工具 (Hardcoded Tools)」起步：** 給予一組固定的工具，讓 Agent 自行決定執行的步驟與順序。這在可控性與靈活性之間達到最佳平衡。

3.  **建立自動化評估流程：** 人工標註少量負面案例 → 設計 Rubric → 進行 AB 測試。

4.  **避免過度工程 (Over-engineering)：** 在引入 Multi-agent 或 Fine-tuning 之前，先問自己：單一 Agent 或簡單的 Prompt Chaining 是否已經能解決問題？
