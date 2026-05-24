---
type: concept
tags: [AI架構, Agent, LLM, 多智能體, 系統設計]
created: 2026-05-16
updated: 2026-05-16
sources: [2026-05-16_stanford_ai系統課程_agentic, 2026-05-16_harness_engineering_ai職涯]
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

## 應用 / 實例
- 在 [[Claude_Code]] 中：Claude Code 是 Agentic Workflow 的商業化產品

## 來源
- [[2026-05-16_stanford_ai系統課程_agentic]]
- [[2026-05-16_harness_engineering_ai職涯]]
