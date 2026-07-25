---
type: concept
tags: [automation, rpa, agent, enterprise]
created: 2026-06-27
updated: 2026-07-25
sources: [2026-06-27_rpa_要沒了, 2026-07-10_六月_ai_更新彙整, 2026-07-25_claude_record_a_skill]
---

# RPA（機器人流程自動化）

> Robotic Process Automation：透過錄製滑鼠座標與鍵盤動作來自動化重複性作業的傳統技術。其「**指令式**」本質正被 AI agent 的「**目標式**」自動化取代。

## 指令式 vs 目標式（核心對比）
| | 傳統 RPA（指令式） | AI Agent（目標式，如 [[OpenAI_Codex]]） |
|---|---|---|
| 記錄什麼 | 座標、鍵盤動作 | 操作意圖（做什麼 / 為什麼） |
| 抗變化 | 介面改版即崩潰 | 理解語意，較能適應 |
| 非結構化內容 | 無法處理 | 可理解處理 |
| 異常處理 | 停擺報錯 | 含結果驗證與異常處理閉環 |

## RPA 的三大致命缺陷
1. 介面稍微改版，腳本即崩潰
2. 無法處理非結構化內容
3. 遇到預設路徑外的異常只能停擺報錯

## 為何被取代
- [[OpenAI_Codex]] 的 `record and replay`：示範一遍即學成可編輯 **Skill**，把 IT 維護的腳本變成普通員工可建的流程（自動化民主化）
- **Figma 效應**：可共享 Skill 形成網路效應，一人錄製帶動全團隊 SOP
- 整合 Goal / Automations / Heartbeat / Skills，朝 [[AIOS]] 企業作業系統演進

## 補充：Record and Reply 的抗變化原理（[[2026-07-10_六月_ai_更新彙整]]）
Codex 在 **Mac** 上觀測使用者的實際工作流程（如上傳 YouTube、整理資料），並自動轉為可編輯、可共享的 Skill。關鍵差異在於它記錄的是**意圖**而非座標：

> 「Record and Reply 記住的是你為什麼要這麼做，因此即使介面有些微的變動，它仍然有能力執行流程，而不是直接失效。」

**數位資產化**：員工錄製的 Skill 成為公司共同資產，降低新人學習成本，也避免流程隨員工離職而流失。

## 同代競品
- **Microsoft Scout**：連接 Outlook / OneDrive / SharePoint 管理行程
- **Microsoft Copilot Coworker**：自主串接工具完成資料分析與報告產出
- **Claude Tech**（推測指 [[Claude_Cowork]]）：整合 Slack，具 Ambience 環境感知模式
- **[[Claude_Cowork]] record a skill**（2026-07-25 確認）：co-work 模式錄螢幕 + 語音示範即成 Skill，與 Codex Record & Replay 同屬 [[示範式自動化]]

## 來源
- [[2026-06-27_rpa_要沒了]] · [[2026-07-10_六月_ai_更新彙整]]
