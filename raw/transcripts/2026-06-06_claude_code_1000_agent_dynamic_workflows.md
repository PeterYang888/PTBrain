---
type: source
tags: [ai, claude-code, workflow, dynamic-workflows, javascript]
created: 2026-06-06
updated: 2026-06-06
source_url: https://www.youtube.com/watch?v=GHWckrzW-jc
source_date: 2026-06-06
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# Claude Code Dynamic Workflows 深度技術簡報：Agent 編排的範式轉移

本簡報旨在深入分析 Anthropic 最近發佈的 Claude Code 更新功能——**Dynamic Workflows（動態工作流）**。此項技術被視為「Agent Scaling（Agent 規模化）」的新里程碑，解決了過去 AI Agent 在處理大型工程任務時的效能瓶頸，並首度實現了成百上千個 Agent 同時協作的可能性。

---

## 1. 執行摘要 (Executive Summary)

Anthropic 在發佈 Claude Opus 4.8 的同時，推出了處於 Research Preview 階段的 **Dynamic Workflows**。這項技術的核心突破在於將 Agent 的「編排與計劃」從大型語言模型（LLM）的有限上下文視窗（Context Window）中抽離，轉而由真實的 JavaScript 腳本進行驅動。

**關鍵成果指標：**
*   **工程壯舉：** Bun Runtime 作者 Jarred Sumner 利用此功能，在 **11 天內** 將 75 萬行代碼從 Zig 語言遷移至 Rust，且測試套件通過率高達 99.8%。
*   **規模突破：** 突破了過去單一 Session 只能維持 3-5 個 Sub-agent 的限制，現在支援單次任務動員高達 1,000 個 Agent。
*   **品質保證：** 引入「對抗式驗證」機制，透過不同群組的 Agent 互相質疑與修正，確保輸出品質。

---

## 2. 核心技術分析：從「腦內記憶」到「程式執行」

### 2.1 傳統架構的瓶頸
在 Dynamic Workflows 出現之前，Claude Code 的 Sub-agent 運作高度依賴上下文視窗。
*   **Context 擁擠：** 每個 Agent 的讀取、寫入、摘要都會在對話紀錄中留下軌跡。
*   **效能衰退：** 當並行 Agent 超過 10 個時，Context 會迅速飽和，導致模型進入「愚蠢區（Dumb Zone）」，開始做出錯誤決策。

### 2.2 Dynamic Workflows 的解決方案
Dynamic Workflows 將編排邏輯從「LLM 的記憶」搬移到「真實的 JavaScript 執行環境」。

| 特性 | 傳統 Sub-agent | Dynamic Workflows |
| :--- | :--- | :--- |
| **編排位置** | 模型上下文 (Context Window) | 外部 JavaScript 腳本 |
| **並行能力** | 極低 (通常 < 10 個) | 高 (單次累計可達 1,000 個) |
| **狀態管理** | 依賴對話紀錄回溯 | 存儲於 JavaScript 變數中 |
| **可靠性** | 易受 Context 雜訊干擾 | 可重跑、可偵錯 (Debuggable) |

**比喻：** 傳統方式像是導師在腦袋裡死記硬背解題步驟；Dynamic Workflows 則是導師先寫好一份複雜的 Excel 公式（JS 腳本），讓系統自動執行，模型只需負責高層次的決策。

---

## 3. 運作流程與對抗式驗證

### 3.1 四大運作步驟
1.  **任務定義：** 用戶給予高難度指令（例如：跨語言重構整個模組）。
2.  **腳本生成：** Claude 即時編寫一份專屬的 **JavaScript Orchestration Script**，計畫如何拆解任務、需要多少 Agent。
3.  **環境執行：** Runtime 在背景執行該腳本。腳本啟動多個 Agent，Agent 之間透過腳本變數傳遞資料。
4.  **結果彙整：** 跑完所有步驟後，彙整結果進入最終驗證。

### 3.2 對抗式驗證機制 (Adversarial Verification)
其設計靈感來自於生成對抗網絡（GAN）。
*   **生成組：** 第一組 Agent 針對任務給出初步解答。
*   **反駁組：** 第二組獨立 Agent 專門尋找生成組答案中的漏洞與錯誤。
*   **疊代：** 兩組反覆交鋒，直到反駁組找不出問題，結果趨於收斂。
*   **效益：** 這是 Bun 案例能達成 99.8% 測試通過率的關鍵，遠超單一 Agent 的準確率。

---

## 4. 軟體工程規格與系統要求

### 4.1 核心規格限制
為了平衡品質與成本，Anthropic 設定了以下參數：
*   **單次最高並行量 (Concurrent)：** 16 個 Agent（這是目前公認的品質/成本平衡點）。
*   **單次任務總量上限 (Total Cap)：** 1,000 個 Agent。
*   **適用任務時長：** 建議處理預計耗時 **超過 30 分鐘** 的複雜任務。

### 4.2 環境需求與設定
*   **版本要求：** Claude Code CLI 版本需在 **V2.1.154** 以上。
*   **支援介面：** 終端機 (CLI)、Desktop App、VS Code 插件。
*   **啟用方式：**
    *   **Max/Team 方案：** 預設開啟，直接可用。
    *   **Enterprise 方案：** 需管理員於後台手動啟用。
    *   **Pro 方案：** 需進入 `config` 檔案中，將 `dynamic workflows` 區塊設為開啟。

---

## 5. 實務操作：Ultra Code 模式

`Ultra Code` 是 Dynamic Workflows 的全自動化形態，屬於 Session 級別的設定。

*   **功能：** 自動結合模型推理（Reasoning Effort）與 Dynamic Workflows。它會自行判斷當前的 Request 是否需要動用大規模編排。
*   **典型場景：** 
    1. 第一階段：進行全域架構分析。
    2. 第二階段：動員多個 Agent 同時修改代碼。
    3. 第三階段：執行自動化測試與驗證。
*   **建議操作：** 適合在下班前啟動，讓系統在背景長時間運行，隔日查看結果。

---

## 6. 成本與限制分析

雖然技術強大，但 **成本** 是 Dynamic Workflows 的隱性負擔。

*   **費用放大：** 由於每個 Agent 都有獨立的 Token 計費，一個包含 500 個 Agent 的任務，其帳單可能比一般的 Claude Code Session 高出 **10 倍以上**。
*   **風險管理：** Anthropic 建議企業需設計用量配額與審批流程，避免員工誤用導致「天文數字」帳單。
*   **安全設計：** 編排腳本（Script）本身無法直接讀取檔案或呼叫 Shell，所有敏感操作必須透過受控的 Agent 進行。

---

## 7. 重要語錄與洞察

> 「Dynamic Workflows 讓 Claude Code 第一次能同時跑成千上百個 Agent……這不是隨便的升級，是把 Agent 編排這件事從根本翻轉。」

> 「Bun 的案例證明，這套機制能把三個月的工作變三天，三年的工作變三週。它改變的是軟體工程的時間尺度。」

> 「它（Dynamic Workflows）把 LLM 當成工程師，而不是工具。工程師會自己寫工程系統，這就是 AI 編排概念的根本進化。」

---

## 8. 行動指南與建議 (Actionable Insights)

1.  **任務篩選：** 
    *   **適用：** 大型重構 (Refactor)、跨語言翻譯 (如 Python 轉 TS)、Monolith 拆分為 Microservices、長時研擬任務。
    *   **不適用：** 寫簡單 Function、修改單一 Bug、查詢 API 文件（使用一般模式即可，省下 10 倍成本）。
2.  **版本檢查：** 執行 `claude --version` 確保在 V2.1.154 以上，否則請立即執行 `upgrade`。
3.  **循序漸進：** 建議 Pro 用戶先以一個月的試用期觀察成本曲線，從 4-8 個 Agent 的並行規模開始測試，熟悉後再處理如 500+ Agent 等級的大型專案。
4.  **善用 Ultra 模式：** 針對非緊急但極其複雜的問題，善用 `Ultra Code` 進行離線（背景）運算。