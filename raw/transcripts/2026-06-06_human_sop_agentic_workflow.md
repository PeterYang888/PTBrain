---
type: source
tags: [ai, claude-code, workflow, agentic-workflow, mcp, sop]
created: 2026-06-06
updated: 2026-06-06
source_url: https://www.youtube.com/watch?v=Yzpx4Xaigms
source_date: 2026-06-06
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# 從人類 SOP 到 AI 代理工作流：企業自動化轉型指南

本報告深入分析如何將傳統供人類閱讀的標準作業程序（Human SOP）轉化為可由 AI 代理（Agent）穩定執行的代理工作流（Agentic Workflow）。透過任務拆解（Task Decomposition）與標準化協議，企業能從依賴黑盒子的單體模型（Mega Agent）轉向具備穩定性、可觀測性與可修復性的生產線架構。

---

## 執行摘要

當前大型語言模型的能力已足以勝任多數任務，但許多使用者仍面臨產出不穩定或不符合預期的問題。核心原因在於未能將複雜任務有效拆解為 AI 可處理的微型單元。本文件詳述了從 Human SOP 轉向 Agentic Workflow 的四部曲方法論，並強調 **模型上下文協議（Model Context Protocol, MCP）** 在整合外部工具中的關鍵角色。未來 AI 的競爭力將不再僅限於模型使用，而是在於設計能與 AI 協同工作的流程架構。

---

## 核心概念定義

在構建自動化系統前，必須區分以下三種不同層級的執行單位：

| 概念 | 定義 | 核心功能 | 適用對象 |
| :--- | :--- | :--- | :--- |
| **Human SOP** | 寫給人看的傳統流程文件（如 Word 或 PPT）。 | 依賴人類背景知識自動補足細節與判斷例外。 | 人類員工 |
| **Skill** | 將方法論、判斷標準與工具打包的執行單元。 | 包含 Markdown 說明、參考資料與自動化腳本。 | AI 代理 |
| **Agentic Workflow** | 由多個代理、工具、技能與資料源組成的生產線。 | 模擬工廠運作，透過多個節點串聯完成複雜大任務。 | 自動化系統 |

---

## 任務拆解（Task Decomposition）的重要性

直接將大任務丟給最強模型（Mega Agent）會導致以下風險：
*   **不可觀測性**：中間推理過程不透明，無法 review。
*   **穩定性低**：任務邊界模糊，模型容易產生幻覺或執行非預期動作。
*   **難以修復**：一旦出錯必須整段重來，無法精確定位問題點點。

相較之下，**分而治之（Divide and Conquer）** 的策略是設計一條可預測、有邊界且出錯可修復的生產線。

---

## 轉型四部曲：構建 Agentic Workflow

### 第一步：格式標準化
將 Human SOP 改造成 Agent 能讀懂的結構化版本，重點在於：

1.  **參數化 (Parameterization)**：避免寫死數值。
    *   *範例*：將「使用一般模式」改為變數 `mode: [normal, delicate]` 或 `temperature: [cold, warm, hot]`。
2.  **採用 RFC2119 規範**：強制定義規則強度：
    *   **MUST**：硬性規定，絕對不可跳過。
    *   **SHOULD**：建議做法，若不執行須說明原因。
    *   **MAY**：選配項目。
3.  **結構化佈局**：使用 Markdown 將 `parameters`、`steps`、`error handling` 區塊切分清楚。

### 第二步：任務拆解與連接
將任務拆解為獨立的管道節點（Pipeline Steps），每個節點具備明確的 Input 與 Output。

*   **獨立性**：若節點 A 出錯（如分類錯誤），僅需修正該節點的 SOP，不影響後續節點的邏輯。
*   **工件串接 (Artifacts)**：節點間不靠「感應」，而是靠標準格式（如 **JSON**）傳遞資訊。例如，分類節點輸出的 JSON 直接成為設定機器節點的輸入。

### 第三步：雙向開發 (Two-way Development)
由於「默會知識」（Tacit Knowledge）的存在，第一版 SOP 必定會出錯。
*   **迭代流程**：先寫粗糙版 SOP -> 實際運行 -> 發現 AI 踩坑（如衣服縮水）-> 回頭補強 SOP 規則 -> 再次運行。
*   **關鍵精神**：不追求在房間內想出完美 SOP，而是透過快速迭代（Iteration）讓 SOP 趨於穩定。

### 第四步：整合與執行環境 (MCP)
AI 必須連接真實世界的工具（API、資料庫、檔案系統）才能產生價值。

*   **MCP (Model Context Protocol)**：被譽為 AI 世界的 「USB-C」。它是一個開放標準，讓不同的 AI 主機（如 Claude, ChatGPT, Cursor）能以統一的方式調用外部工具。
*   **Human-in-the-Loop**：在涉及高風險決策（如財務核銷、權限變更）時，設計 Checkpoint 讓 Agent 暫停並等待人類確認。

---

## 實作案例：公司內部請求分類系統

以下演示如何將「處理公司雜事請求」轉化為代理工作流：

### 1. 標準化 SOP (Internal Request)
*   **Parameters**: `ticket_source`, `raw_text`, `employee_id`.
*   **MUST**: 根據 `employee_id` 驗證身份。
*   **SHOULD**: 根據關鍵字判斷 `priority`。
*   **Output**: 結構化 JSON。

### 2. 技能拆解 (Skills)
*   **Skill A (Triage)**：負責分類、判斷優先級、推薦負責人。
*   **Skill B (Drafting)**：接收 Skill A 的 JSON 輸出，自動生成回覆同事的草稿。

### 3. 雙向開發與整合
*   **迭代**：修正「離職員工仍被推薦為負責人」或「誤判優先級」的邏輯坑。
*   **執行**：透過小腳本將結果寫回 Google Sheet 或 Notion，並在超過 5000 元的財務請求設定人類確認點。

---

## 重要語錄與背景分析

> **「問題從來不是幫手夠不夠聰明，或者模型表現好不好...只要沒有讀心術，他就永遠滿足不了你的需求。」**
*   **背景分析**：強調了溝通意圖與明確定義邊界的重要性。即使 AGI 時代來臨，人類仍需具備定義偏好與流程的能力。

> **「MCP 就像 AI 世界的 USB-C。」**
*   **背景分析**：隱喻 MCP 協議將解決 AI 工具整合碎片化的問題。目前 Anthropic 已將此協議移交至 Linux Foundation 旗下的 Agentic AI Foundation，確保其作為開放標準的長期維護。

> **「你不是在學怎麼用 AI，而是在學怎麼設計給 AI 用的工作流。」**
*   **背景分析**：指出未來人才的核心競爭力在於「設計能力」而非單純的「操作能力」。工具的操作半年就會過時，但流程設計的價值會隨時間增長。

---

## 行動指南與建議

1.  **從小處著手**：挑選一個最無聊、重複性最高且最不想做的 Human SOP（如週報、上線清單、新人引導）。
2.  **不追求完美**：先開發一個能節省 30% 時間的粗糙版本，再透過實戰疊代。
3.  **關注開放協議**：優先考慮支援 MCP 的工具與平台，以確保工作流的可移植性與長久性。
4.  **擁抱 Agentic AI Foundation**：關注 IBM、AWS、ServiceNow 等大廠已將此工作流導入生產環境的趨勢，這已非工程師的小眾興趣，而是企業自動化的主流趨勢。