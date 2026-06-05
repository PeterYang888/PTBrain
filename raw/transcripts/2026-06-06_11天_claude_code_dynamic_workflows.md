---
type: source
tags: [ai, claude-code, workflow]
created: 2026-06-06
updated: 2026-06-06
source_url: https://www.youtube.com/watch?v=pI-AX98dlvY
source_date: 2026-06-06
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: ""
  processed_by: notebooklm-py
---

# Claude Code Dynamic Workflows (動態工作流) 技術深度簡報

本文件旨在深入分析 Claude Code 的「Dynamic Workflows」（動態工作流）功能。這項技術透過 JavaScript (JS) 腳本驅動，顯著提升了 Agent 的並行處理能力與上下文（Context）管理效率，使其能應對大規模的程式碼遷移與複雜搜尋任務。

## 執行摘要 (Executive Summary)

Claude Code 推出的 Dynamic Workflows 是一項具備顛覆性的功能，其核心在於將 Agent 的協作邏輯從傳統的提示詞（Prompt）轉向程式化的 JavaScript 腳本。這項變革解決了傳統 Agent 在多工處理時上下文視窗（Context Window）容易「爆炸」的問題。

**核心數據與成就：**
*   **大規模生產力：** 官方案例顯示，在 11 天內完成了從 C++ 到 Rust 的 75 萬行程式碼遷移。
*   **並行處理：** 支援多達 16 個 Agent 單位同時運行。
*   **上下文優化：** 透過將中間過程存於 JS 變數，僅將最終結果傳回主上下文，大幅節省 Token 消耗。

---

## 技術核心分析：Dynamic Workflows 的機制

### 1. 從 MD 到 JavaScript 的演進
傳統的 Agent 協作（如 Agent Team）主要依賴 Markdown (MD) 或自然語言指令。而 Dynamic Workflows 將邏輯隱藏在 JavaScript 腳本中：
*   **變數管理：** 中間步驟的詳細數據被封裝在 JS 腳本中，主上下文僅接收濃縮後的結果（如 Excel 匯總表概念）。
*   **流程控制：** 支援順序執行與平行處理（Parallel Processing），Agent 之間雖然不直接溝通，但可透過腳本的輸入輸出進行數據傳遞。

### 2. 上下文壓力緩解
傳統方法中，多個 Sub-agent 的對話會迅速填滿上下文視窗。Dynamic Workflows 透過腳本化，讓主程式只需關注結果，從而容納更多 Sub-agent 的並行工作，這也是實現「一天產出 7 萬行程式碼」的關鍵。

---

## 操作指南：CLI 指令與設定

### 環境檢查與配置
在開始使用前，需確保功能已啟用：

| 指令/動作 | 描述 |
| :--- | :--- |
| `config` | 檢查 `dynamicWorkflows` 與 `workflowKeywordTrigger` 是否開啟（預設通常為開啟）。 |
| `alt + p` | 快速切換模型強度（Low / Medium / High / Ultra / Ultra Code）。 |

### 三種觸發方式
根據需求複雜度，可透過以下三種方式啟用工作流：

1.  **Deep Search (內建腳本)：**
    *   指令：`deep-search [查詢內容]`
    *   特性：會自動執行多個 Agent 進行資料對抗、評分與運算，適合深入的資訊檢索。
2.  **Workflow 關鍵字觸發：**
    *   操作：在終端機輸入 `workflow`（字體變色即代表觸發），隨後輸入需求。
    *   特性：可自定義需求，並能將產生的流程存為 JS 檔案。
3.  **Ultra Code 模式：**
    *   操作：切換模型至 `Ultra Code`。
    *   特性：預設使用最高推理強度，並自動編寫與執行工作流。

### 監控與重用 (Workflow Management)
*   **檢視進度：** 輸入 `/workflows` 或縮寫 `wf` 可查看當前運行的 Agent 狀態。
*   **存檔重用：** 在監控介面按 `s` 鍵，可將工作流存成 JS 檔，便於在未來的 Session 中直接重用該流程。
*   **導覽快捷鍵：**
    *   `Enter`：查看 Agent 下達的 Prompt。
    *   `J` / `K`：滾動查看輸出結果。

---

## 程式碼片段與腳本結構範例

Dynamic Workflows 的背後是一套 JS 規則。雖然使用者可以讓 AI 自動生成腳本，但其基本邏輯結構如下：

```javascript
// 簡化的工作流邏輯概念範例
{
  "tasks": [
    {
      "id": "search_phase",
      "type": "parallel", // 平行處理
      "action": "search",
      "queries": ["query1", "query2"]
    },
    {
      "id": "validation_phase",
      "type": "sequential", // 順序執行
      "action": "verify",
      "input": "search_phase.output"
    }
  ],
  "summary": "final_result"
}
```
*註：實際腳本會根據 AI 規劃的需求動態生成，包含驗證觀點與資料查證。*

---

## 關鍵評論與引用

> 「它把 Prompt 從 Context 搬進了程式碼裡面……你的上下文視窗自然就可以變得很大，所以可以調用非常多個 Sub-agent 下去工作。」

**上下文理解：** 這是對 Dynamic Workflows 能處理大規模工程的核心解釋。傳統方法像是在一張小桌子（Context Window）上塞滿人，人越多桌子越快崩潰；Dynamic Workflows 則是每個人領取任務後將結果整理成一份精簡報告（JS Variable），老本只需看報告。

> 「11 天產生 75 萬行程式碼……這個真的很猛。」

**背景：** 引用自官方將大型專案從 Legacy C++ 移植到 Rust 的案例，強調了 Workflow Automation 在大規模移植上的潛力。

---

## 比較分析：Workflow vs. Agent Team

| 特性 | Dynamic Workflows | Agent Team |
| :--- | :--- | :--- |
| **通訊方式** | 透過 JS 腳本進行數據傳遞（流水線模式） | Agent 之間可直接相互溝通、分派 |
| **適用場景** | 確定性強的流水線、大規模移植、全站 Bug 掃描 | 需動態決策、互相討論的複雜分派任務 |
| **擴展性** | 高（16+ 並行 Agent），較不佔上下文 | 中等，受限於上下文視窗長度 |

---

## 行動建議與注意事項

1.  **成本監控：** Dynamic Workflows 會消耗大量 Token。在 200 美元的 Session 額度下，極端情況下可能一次任務就會耗盡額度。建議初次嘗試時使用較弱的模型（如 Medium 或 Low）進行測試。
2.  **適用場景優先：** 優先將此功能應用於「大規模移植」、「全代碼庫安全掃描」或「跨多維度的深度資料搜尋」。
3.  **腳本優化：** 若不知如何撰寫 JS 腳本，可先透過 `workflow` 指令讓 AI 跑一遍，再要求 AI 根據該過程寫出可重用的 JS 檔案。
4.  **限制因素：** 目前工作流執行中途不支援使用者手動輸入干預，屬於全自動執行的流程。