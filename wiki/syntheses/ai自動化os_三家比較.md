---
type: synthesis
tags: [ai, agent, automation, aios, comparison]
created: 2026-06-27
updated: 2026-06-27
sources: [2026-06-27_rpa_要沒了, 2026-06-27_gemini_spark, 2026-05-30_ai_agent_goal功能, 2026-04-15_claude_code_desktop_routines改版, 2026-06-12_ai_operating_system]
---

# AI 自動化 OS 三家比較：Codex vs Gemini Spark vs Claude Code

> 2026 年三大廠不約而同把 AI 從「對話時才運作的問答機」推向「用戶離線也持續工作的 24/7 後台 worker」。本頁盤點 [[OpenAI_Codex]]、[[Gemini_Spark]]、[[Claude_Code]] 三條路線，並指出它們**幾乎同構的底層框架**。

## 核心命題
「舊模型是 AI 回答你的問題；新模型是 AI 運行你的工作流。」（[[2026-06-27_gemini_spark]]）

真正的自動化分兩段：把任務從**手上**移走（執行），再把它從**心上**移走（不必盯著它做完）。後半段需要 AI 能自主判斷「目標達成了沒」——這正是三家設計的交集。（[[2026-05-30_ai_agent_goal功能]]）

## 三家對照表

| 維度 | [[OpenAI_Codex]] | [[Gemini_Spark]] | [[Claude_Code]] |
|------|------------------|------------------|-----------------|
| 代表機制 | `record and replay`（目標式，取代 [[RPA]]） | Tasks / Skills / Schedules | [[routines]] + `/goal` + [[AIOS]] 4Cs |
| **目標** | Goal | Tasks | `/goal`（Executor + Reviewer） |
| **觸發/排程** | Automations（定時觸發） | Schedules（時間 + 事件觸發） | routines（排程 / API / GitHub 事件） |
| **技能** | Skills（含數據位置+驗證邏輯，可共享） | Skills（`@`/`/` 呼叫，可重用風格） | Capabilities（`.md` Skill，模組化） |
| **監控/驗證** | Heartbeat（心跳監控流程） | Checkpoints（敏感操作暫停） | Reviewer + Rubric 五元素 |
| **外部連接** | NCP（類 MCP）+ Plugins | 原生 Workspace + [[MCP]] | connectors + [[MCP]] + CLI/Playwright |
| **運行位置** | 本地端為主 | 雲端專用 Google Cloud VM | 雲端（routines，關筆電也跑） |
| **安全** | 三級權限模式 | Checkpoints 防 Prompt Injection | 權限確認 + Reviewer 把關 |
| **狀態（2026-06）** | 已上市 | Beta，限美國 AI Ultra | routines 研究預覽（2026-04） |

## 關鍵洞察

### 1. 四要素框架幾乎同構
三家拆解自動化的方式高度一致，可歸納為一個共通骨架：
```
目標(Goal) + 觸發(Trigger/Schedule) + 技能(Skill) + 監控驗證(Monitor/Review)
```
- Codex：Goal / Automations / Skills / **Heartbeat**
- Spark：Tasks / Schedules / Skills /（Checkpoints 偏安全而非結果驗證）
- Claude：`/goal` / routines / Capabilities / **Reviewer + Rubric**

### 2. 「Skill」成為三家共通的可共享工作單元
三家都用「Skill」當作可重用、可共享的最小自動化單位——呼應 [[工具無關性]]：Skill 格式在 Claude Code 與 Codex 間幾乎可直接互通。RPA 的「Figma 效應」（一人錄製 → 全團隊 SOP）在三家身上都成立。（[[2026-06-27_rpa_要沒了]]）

### 3. 監控/驗證才是「移出心上」的關鍵差異點
- **Codex Heartbeat**：持續確認流程是否正常運行
- **Claude Reviewer + Rubric**：用「實作者 + 評審」雙角色破除 AI 的「完成幻象」與 Context Anxiety；成敗取決於 Rubric（預期結果/驗證方式/限制/迭代/錯誤處理）寫得夠不夠具體
- **Spark Checkpoints**：偏「安全暫停」而非「結果驗證」——這是 Spark 目前相對較弱的一環

> Claude 路線把「驗證」這件事做得最深：Rubric 表面是給 AI 用，實際是逼人把腦中模糊品位寫成文字。

### 4. [[MCP]] 正在成為跨生態連接標準
Spark 明確以 MCP 連 Canva/Notion/Slack 等第三方；AIOS 的 C2（Connections）也把 MCP 列為核心；Codex 的 NCP 是同類協議。連接層的標準化讓「哪家引擎」變得可替換。

## 路線差異（各自的賭注）
- **Codex**：主打 `record and replay` 正面取代傳統 [[RPA]]，切入**企業既有自動化市場**
- **Gemini Spark**：押注**雲端 VM + Workspace 原生數據權限**，靠 Google 生態系黏著度
- **Claude Code**：押注**開發者工作流入口** + Rubric 式深度驗證（routines + AIOS 4Cs），偏個人/小團隊「系統擁有者」

## 延伸閱讀
- 概念框架：[[AIOS]]（4Cs）、[[Agentic_Workflow]]、[[Loop_Engineering]]
- 來源頁：[[2026-06-27_rpa_要沒了]]、[[2026-06-27_gemini_spark]]、[[2026-05-30_ai_agent_goal功能]]

## 待追蹤
- Spark 是否會補上「結果驗證」層（目前只有 Checkpoints 安全暫停）？
- 三家 Skill 格式能否真正互通（Claude↔Codex 已驗證，Google 是否加入）？
- routines 正式上市後的額度與 connectors 生態範圍
