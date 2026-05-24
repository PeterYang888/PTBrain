---
type: concept
tags: [AI架構, Agent, 協議, Agentic_Workflow]
created: 2026-05-20
updated: 2026-05-20
sources: [2026-05-16_stanford_ai系統課程_agentic]
---

# MCP（模型上下文協議）

> Model Context Protocol；Anthropic 提出的開放協議，在 LLM 和外部服務之間提供標準化的通信層，讓 Agent 不需為每個 API 單獨撰寫串接邏輯，也是 Multi-Agent 系統中 Agent 互相調用的基礎。

## 核心問題
傳統 AI Agent 整合外部工具的方式：
- 為每個 API 單獨撰寫串接代碼
- 教 LLM 每個 API 的輸入/輸出格式
- 維護成本高，缺乏標準化

## MCP 的解法
```
Agent → MCP Server → 後端服務 API
```
- Agent 只需與 MCP Server 溝通（統一接口）
- MCP Server 負責與各後端服務打交道
- 比喻：通用插頭 — 以前每個國家插座規格不同需帶轉接頭，MCP 讓一個插頭全通

## Agent-to-Agent 通信
MCP 更大的想像：
- 把別人做好的 Agent 當作一種「工具」
- 讓自己的 Agent 像調用 API 一樣調用其他 Agent
- 這是 Multi-Agent 系統的基礎架構

## 在 Agentic Workflow 中的位置
```
User → Orchestrator Agent
         ↓
    [Tool calls via MCP]
    ├── Search Agent
    ├── Database Agent
    ├── Email Agent
    └── 其他 Specialized Agent
```

## 與 LangChain 的定位差異
- LangChain：Python 框架，提供各種 Agent/Chain 的抽象
- MCP：協議層（Protocol），與語言和框架無關，更底層、更通用

## 相關資源
- Anthropic 開源 MCP 規範

## 來源
- [[2026-05-16_stanford_ai系統課程_agentic]]

## 相關概念
- [[Agentic_Workflow]]（使用 MCP 的系統）
- [[RAG]]（可透過 MCP 整合的工具之一）
- [[Claude_Code]]（Anthropic 的 Agentic 產品，整合 MCP）
