---
type: concept
tags: [automation, rpa, agent, enterprise]
created: 2026-06-27
updated: 2026-06-27
sources: [2026-06-27_rpa_要沒了]
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

## 來源
- [[2026-06-27_rpa_要沒了]]
