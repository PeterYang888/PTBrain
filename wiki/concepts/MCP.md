---
type: concept
tags: [AI架構, Agent, 協議, Agentic_Workflow]
created: 2026-05-20
updated: 2026-05-20
sources: [2026-05-16_stanford_ai系統課程_agentic, 2026-06-06_human_sop_agentic_workflow]
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
- 比喻：**AI 世界的 USB-C**——讓不同 AI 主機（Claude / ChatGPT / Cursor）以統一方式調用外部工具
- 治理：Anthropic 已將 MCP 協議移交 Linux Foundation 旗下的 **Agentic AI Foundation**，確保長期開放維護

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

## Token 成本考量與在 Loop 中的角色（2026-06-19）
- **Token 效率最低的選項**：實務上 Token 效率 CLI > API > MCP。MCP 光是載入背景（未開始任務）就可能消耗約 **4,300 tokens**（`/context` 可觀察）；CLI 輸出最乾淨、無冗餘 metadata（見 [[2026-06-19_claude_code_500小時心得]]、[[Context_工程]]）
- **Loop 的 Connector 模塊**：在 [[Loop_Engineering]] 的 5+1 框架中，MCP 是「Connector（連接器）」核心，讓 Agent 取得收發郵件、剪輯、生成等泛化能力（見 [[2026-06-19_loop_engineering]]）
- **多模態調度精神**：AR 眼鏡（[[RayNeo_X3_Pro]]）整合視覺+語義、Apple 跨模型呼叫 Gemini，皆呼應 MCP 的跨能力調度理念

## 相關資源
- Anthropic 開源 MCP 規範

## 來源
- [[2026-05-16_stanford_ai系統課程_agentic]]
- [[2026-06-19_claude_code_500小時心得]]（MCP Token 成本）
- [[2026-06-19_loop_engineering]]（Connector 模塊）

## 相關概念
- [[Agentic_Workflow]]（使用 MCP 的系統）
- [[RAG]]（可透過 MCP 整合的工具之一）
- [[Claude_Code]]（Anthropic 的 Agentic 產品，整合 MCP）
