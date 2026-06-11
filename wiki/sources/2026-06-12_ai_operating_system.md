---
type: source
tags: [ai, claude-code, workflow, aios, mcp, agent]
created: 2026-06-12
source_url: https://www.youtube.com/watch?v=EyZEJPP2JNQ
source_date: 2026-06-12
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# 什麼是 AI Operating System？一套能讓 AI 替你工作的系統（附免費設定）

> 來源：[原始檔](../../raw/transcripts/2026-06-12_ai_operating_system.md) · [[Claude_Code]] · [[MCP]]

## 一句話摘要
AIOS（AI Operating System）以 4Cs 框架（Context / Connections / Capabilities / Cadence）把 Claude Code 或 Codex 從聊天機器人轉成能在背景自主執行任務的個人 AI 代理，核心是「漸進式加載」和模組化 Skill 設計。

## 核心論點
- **4Cs 框架**：Context（結構化文件系統，漸進式加載）→ Connections（API / MCP / CLI / Playwright）→ Capabilities（模組化 `.md` Skill 文件）→ Cadence（固定流程 or Agentic Routines 自適應排程）
- **Context 防呆機制**：`what-not-to-do.md` 記錄 AI 曾犯的錯誤，每次執行前先複習，系統「越用越聰明」
- **模組化 Skill vs Mega Skill**：拆成單一功能（確認主題 → 生成腳本 → 生成簡報 → 發布）而非一個巨型 Skill；便於偵錯與維護
- **Agentic Routines**（Cadence 層）：具自適應能力，AI 出錯時嘗試自我修正繼續完成，對應 [[routines]] 功能
- **`.claud/` 資料夾**：放 `skills/` 和 `context/`，`/setup-aios` 引導式建立 context 文件

## 關鍵文件清單
| 文件 | 內容 |
| :--- | :--- |
| `me.md` | 個人資訊、喜好、回答偏好 |
| `what-not-to-do.md` | AI 犯過的錯誤記錄（防呆） |
| `working-style.md` | AI 工作方式定義（如開發前先提問確認） |
| `brand.md` / `brandvoice.md` | 個人品牌設定 |

## 值得引用的段落
> 「把這四層疊在一起，你就不再是一個操作者，你是一個系統的擁有者。」

> 「AIOS 有個很大的特點，就是隨著時間它會越用越聰明。」

## 連結到的 wiki
- [[AIOS]]
- [[Claude_Code]]
- [[MCP]]
- [[Agentic_Workflow]]
- [[routines]]

## 我的問題 / 待追蹤
- 「免費設定」指的是什麼具體的免費工具？
- Playwright 連接用在哪些具體工作流場景？
