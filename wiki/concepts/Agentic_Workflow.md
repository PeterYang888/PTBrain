---
type: concept
tags: [AI架構, Agent, LLM, 多智能體, 系統設計]
created: 2026-05-16
updated: 2026-05-16
sources: [2026-05-16_stanford_ai系統課程_agentic, 2026-05-16_harness_engineering_ai職涯, 2026-05-30_ai_agent_goal功能, 2026-05-30_codex_office全包辦]
---

# Agentic Workflow

> 將 LLM 與外部工具、記憶、規劃機制組合成具有自主決策能力的系統架構；對比傳統軟體的確定性控制流，Agentic Workflow 是模糊性、目標導向的。

## 詳細說明
Agentic Workflow 的核心思維轉變：從「精確控制每一行代碼（Microservices）」到「給 AI 目標和限制，讓它自己決定怎麼完成（Manager Mindset）」。

### Agent 三核心要素
1. **提示詞（Prompt）**：定義角色與權限範圍
2. **上下文管理（Context Management）**：區分短期記憶（Working Memory）與長期記憶（Archival Memory）
3. **工具（Tools）**：賦予執行能力（如搜尋、預訂、支付）與查詢能力（如訪問 CRM）

## 與其他概念的差別
- 跟 [[Harness_Engineering]] 的關係：Agentic Workflow 是概念框架，Harness Engineering 是系統實現層
- 跟傳統軟體的差別：確定性（Deterministic）vs 模糊性（Fuzzy），精確控制 vs 目標管理

## 多智能體協作模式
- **科層制（Hierarchical）**：統籌者（Orchestrator）派工，結構清晰
- **扁平制（Flat）**：智能體之間直接互通
- **MCP（Model Context Protocol）**：通用協議層，讓 Agent 不需認識每個 API

## 評估體系
Agentic Workflow 上線的命脈是**評估（Evaluation）**：整體 vs 組件、客觀 vs 主觀（LLM-as-judge）、定量 vs 定性

## /goal 功能與 Context Anxiety（2026-05-30 新增）
主流 agentic 工具（Claude Code、OpenAI Codex）推出 `/goal` 模式，解決 LLM 的「下班心態」問題：
- **Context Anxiety（上下文焦慮）**：LLM 在 context window 接近滿載時，會本能地假裝完成任務或過早交差
- **/goal 雙角色架構**：Executor（執行者）+ Reviewer（評審者）——評審者持續判斷「目標是否達成」，未達成就要求繼續
- **Rubric = 評審準則**：定義何謂「完成」的具體標準，是 /goal 成功的關鍵，比 prompt 技巧更重要
- 對應 [[Vibe_Coding]] 的「人類定義目標，AI 自主執行到完成」理念
→ 詳見 [[2026-05-30_ai_agent_goal功能]]

## 應用 / 實例
- 在 [[Claude_Code]] 中：Claude Code 是 Agentic Workflow 的商業化產品
- 在 [[OpenAI_Codex]] 中：AGENTS.md + Skills/Plugins + Computer Use 的 Office 自動化
- /goal 功能：AI agent 連續自主執行 27 小時的案例

## 來源
- [[2026-05-16_stanford_ai系統課程_agentic]]
- [[2026-05-16_harness_engineering_ai職涯]]
- [[2026-05-30_ai_agent_goal功能]]
- [[2026-05-30_codex_office全包辦]]
