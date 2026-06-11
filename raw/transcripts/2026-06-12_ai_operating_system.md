---
type: source
tags: [ai, claude-code, workflow, aios, mcp, agent]
created: 2026-06-12
updated: 2026-06-12
source_url: https://www.youtube.com/watch?v=EyZEJPP2JNQ
source_date: 2026-06-12
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: ""
  processed_by: notebooklm-py
---

# AI Operating System (AIOS) 構建全指南：邁向自動化 AI 代理時代

這份簡報文件詳細分析了「AI 作業系統」（AI Operating System，簡稱 AIOS）的架構與實作方法。AIOS 的核心理念在於如何有效管理資訊，並在最適當的時機提供 AI 最正確的數據，從而將 AI 從單純的聊天機器人（Chatbot）轉化為能主動執行任務的個人助理（AI Agent）。

## 執行摘要

在 AI 技術高度發展的今日，建立一套「懂你」並能「替你執行」的系統是提升生產力的關鍵。AIOS 透過大型語言模型驅動框架（LLM Harness），如 **Claude Code** 或 **Codex**，作為本地端運行的入口。其架構由四大核心支柱（4Cs）構成：**Context（上下文）**、**Connections（工具連接）**、**Capabilities（技能）**以及 **Cadence（排程與自動化）**。透過這套系統，使用者不再僅是指令的操作者，而是系統的擁有者，能讓 AI 在背景自動處理發文、腳本撰寫、數據分析及個人健康管理等任務。

---

## AIOS 四大核心支柱分析

AIOS 的運作依賴於四個維度的整合，確保 AI 具備足夠的知識、工具存取權限、標準作業程序及自動化執行能力。

### 1. Context (上下文)：系統的大腦
Context 是讓 AI 理解使用者身份、目標與偏好的關鍵。它並非單一的大型檔案，而是一套結構化的文件系統。

*   **管理原則：** 採用「漸進式加載」（Progressive Loading），確保 AI 只在需要時讀取相關資訊，避免資訊過載導致理解錯誤。
*   **關鍵文件類型：**
    *   `me.md`: 存放個人資訊、喜好、回答偏好。
    *   `what-not-to-do.md`: 記錄 AI 曾犯過的錯誤，防止重複出錯。
    *   `working-style.md`: 定義 AI 的工作方式。
*   **場景化配置：**
    *   **個人品牌：** `brand.md`、`brandvoice.md`、`brand-assets.md`
    *   **商業經營：** `business.md`、`team.md`、`goals-milestones.md`
    *   **職場工作：** `my-roles-kpi.md`、`communication-guidelines.md`

#### 漸進式加載範例表 (Progressive Loading)
| 觸發時機 (Load When) | 對應檔案 (File) | 目的 |
| :--- | :--- | :--- |
| 需要生成 PDF 或 HTML 時 | `reference/documentation.md` | 查閱格式規範 |
| 需要處理生活開銷時 | `finance-admin.md` | 獲取財務管理準則 |
| 處理個人品牌網站任務時 | `context/rules/website-id.md` | 確保品牌視覺一致性 |

### 2. Connections (工具連接)：系統的手腳
讓 AI 觸達真實世界的數據並執行實際任務。

*   **主流連接方式：**
    1.  **API:** 標準化的應用程式介面連接。
    2.  **MCP (Model Context Protocol):** 專為 AI 連結外部數據設計的協議。
    3.  **CLI (Command Line Interface):** 透過命令行介面直接操控系統工具。
    4.  **Playwright:** 當工具缺乏 API 時，讓 AI Agent 直接模擬真人操作網頁頁面。

### 3. Capabilities (技能)：系統的 SOP
將大腦中的 SOP 轉換為 AI 可閱讀的 `.md` 技能文件，確保輸出結果的一致性。

*   **技能系統 (Skill System)：** 建議將複雜任務拆解為多個單一功能的 Skill（如：確認主題 -> 生成腳本 -> 生成簡報 -> 發布網站），而非建立一個巨大的 Mega Skill。
*   **優點：** 易於管理與偵錯。若其中一個步驟出錯，僅需修改該 Skill 的邏輯。

### 4. Cadence (排程與自動化)：系統的運作節奏
讓系統在無人值守的情況下，於背景自動運行。

*   **兩大運作模式：**
    1.  **Fixed Models:** 跑固定流程（Step 1 -> Step 2），若中途出錯則停止。
    2.  **Agentic Routines (如 Claude Routines):** 具備自適應能力。AI 會先讀取背景資訊並執行，若執行中出錯，AI 會嘗試自我修正以確保任務完成。

---

## 技術實作與指令參考

### 資料夾結構規範
建議在專案根目錄下建立 `.claud` 資料夾來存放所有系統指令與上下文。

```text
Project_Folder/
├── .claud/
│   ├── skills/
│   │   ├── setup-aios.md    <-- 系統初始化技能
│   │   └── daily-meal-plan.md
│   └── context/
│       ├── me.md
│       ├── what-not-to-do.md
│       └── working-style.md
```

### CLI 操作流程
```bash
/setup-aios   # 引導式設定，自動生成 context 文件
```

---

## 重要語錄

> 「AI Operating System 的核心，其實就是如何有效管理並在最適當的時機給 AI 最正確的資訊。」

> 「把這四層疊在一起，你就不再是一個操作者，你是一個系統的擁有者。」

> 「AIOS 有個很大的特點，就是隨著時間它會越用越聰明。」

---

## 具體執行建議

1.  **建立防呆機制：** 立即建立 `what-not-to-do.md`，每當 AI 產生不符預期的結果時將案例存入。
2.  **模組化 Skill 撰寫：** 針對重複性高的工作，將 SOP 寫成獨立 Skill 文件放入 `skills/` 資料夾。
3.  **隱私安全考量：** 將所有 Context 資料儲存在本地端電腦，不上傳敏感資料至雲端。
4.  **逐步自動化：** 先從「個人資訊 (Me)」與「工作風格 (Working Style)」開始設定，待 Context 穩定後再擴展。
