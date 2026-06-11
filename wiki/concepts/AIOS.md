---
type: concept
tags: [ai, claude-code, workflow, agent, context-management, automation]
created: 2026-06-12
updated: 2026-06-12
sources: [2026-06-12_ai_operating_system]
---

# AIOS（AI Operating System，AI 作業系統）

> 以 LLM 框架（如 Claude Code 或 Codex）為核心引擎，透過 4Cs 架構（Context / Connections / Capabilities / Cadence）把 AI 從聊天機器人升級成能在背景自主執行任務的個人代理系統。

## 詳細說明
AIOS 的核心理念：在最適當的時機給 AI 最正確的資訊。使用者從「指令操作者」轉為「系統擁有者」，AI 在背景自動處理任務（發文、腳本、數據分析等）。

## 4Cs 框架

### C1 — Context（上下文，系統的大腦）
結構化文件系統，採「漸進式加載（Progressive Loading）」——AI 只在需要時讀取相關文件，避免資訊過載。

**核心文件：**
| 文件 | 內容 |
| :--- | :--- |
| `me.md` | 個人資訊、喜好、回答偏好 |
| `what-not-to-do.md` | AI 曾犯的錯誤記錄（防呆機制，系統「越用越聰明」） |
| `working-style.md` | AI 工作方式（如開發前先提問確認） |
| `brand.md` | 品牌聲音 / 視覺規範 |

### C2 — Connections（工具連接，系統的手腳）
讓 AI 觸達真實世界：
- **API**：標準應用程式介面
- **[[MCP]]（Model Context Protocol）**：AI 連結外部數據的專用協議
- **CLI**：命令行直接操控
- **Playwright**：無 API 時讓 AI 模擬真人操作網頁

### C3 — Capabilities（技能，系統的 SOP）
將 SOP 轉為 AI 可讀的 `.md` 技能文件，置於 `.claud/skills/` 資料夾。

**模組化原則（優於 Mega Skill）：**
- 拆成單一功能（確認主題 → 生成腳本 → 生成簡報 → 發布）
- 每個 Skill 可獨立偵錯與修改，不影響整體流程

### C4 — Cadence（排程與自動化，系統的節奏）
背景自動運行的兩種模式：

| 模式 | 特性 | 適用 |
| :--- | :--- | :--- |
| Fixed Models | 固定流程 Step 1 → 2 → 3，中途出錯即停 | 確定性任務 |
| Agentic Routines（[[routines]]） | 具自適應能力，出錯自我修正繼續完成 | 複雜自動化任務 |

## 資料夾結構
```text
Project_Folder/
├── .claud/
│   ├── skills/
│   │   └── setup-aios.md
│   └── context/
│       ├── me.md
│       ├── what-not-to-do.md
│       └── working-style.md
```

## 快速啟動
```bash
/setup-aios   # 引導式設定，自動生成 .claud/context/ 文件
```

## 與其他概念的差別
- 跟 [[Agentic_Workflow]]：AIOS 是一套具體的個人化實作模式，Agentic Workflow 是更廣泛的系統架構概念
- 跟 [[Harness_Engineering]]：Harness Engineering 是組織/企業層面的 AI 架構，AIOS 是個人/小團隊層面
- 跟 [[Dynamic_Workflows]]：AIOS 是靜態配置框架，Dynamic Workflows 是單次大規模任務的動態執行引擎

## 應用場景
- 個人品牌：自動排程發文、腳本生成、分析
- 職場：自動處理重複性報告、溝通摘要
- 小團隊：將 SOP 轉為可執行的 Skill，交由 AI 持續執行

## 來源
- [[2026-06-12_ai_operating_system]]
