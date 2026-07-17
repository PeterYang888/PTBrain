---
type: source
tags: [ai, claude-code, workflow, harness]
created: 2026-07-18
source_url: https://www.youtube.com/watch?v=GzHfE50N8x4
source_date: 2026-07-18
source_type: transcript
---

# 15 分鐘看完 Google Vibe Coding / Agentic Engineering 開發課 Day 1

> 來源：[原始檔](../../raw/transcripts/2026-07-18_google_agentic_engineering_day1.md) · [[Gary_Chen]]

## 一句話摘要
Google 官方五天 AI 開發課 Day 1：AI 開發正從直覺式 [[Vibe_Coding]] 演進為具備嚴格結構、驗證機制與 Harness 設計的 [[Agentic_Engineering]]，核心技能是 [[Context_工程]]。

## 核心論點
- **Agent = Model + Harness**：模型本身不是 Agent；真正的 Agent 需要 Harness 提供狀態、工具執行、反饋迴圈與行為約束
- **Context Engineering 優於 Prompt Engineering**：核心技能是把任務背景、領域知識、範例與工具定義編成 AI 能高效利用的動態形式
- **工廠模型（Factory Model）**：開發者的產出不再是程式碼，而是「產出程式碼的系統」（規格、實作 agents、Evals、失敗回傳）
- **Token 經濟學 Capex/Opex**：前期投入系統設計與 Context 整理（Capex），靠提高一次成功率降低長期 Token 燃燒（Opex）

## Harness 六大組件
1. `rules files`：agent.md / claude.md，定義身分、價值觀、禁忌
2. `tools`：可呼叫功能與 [[MCP]] servers，含工具選擇說明
3. `sandbox`：限制讀寫權限的運行環境
4. `orchestration`：[[Subagent]] 調度、模型路由、專家交接
5. `hooks`：生命週期固定點的確定性程式碼（如 commit 前擋硬編碼密碼）
6. `observability`：logs / traces / evals / 成本監控

## 關鍵數據（依來源說法）
- 85% 專業開發者使用 AI agent；41% 新程式碼由 AI 生成
- 某團隊只優化 Harness（不換模型），bench 2.0 排名從 30 名外進前 5
- LangChain 實驗：同一模型加 Middleware + 優化 System Prompt，評分 +13.7
- 反例：資深工程師缺驗證機制用 AI，特定任務效率反降 19%

## Context 管理策略
- **Static Context**：每次必載（系統指令、agent.md）——可靠但貴
- **Dynamic Context**：按需載入（RAG、工具結果）——省錢但有抓取失敗風險
- **Progressive Disclosure**：啟動只讀 Skill metadata 一行，任務匹配才載入完整指令

## 值得引用的段落
> 「Generation is solved. Verification, judgment and direction are the new craft.」

> 「當 agent 出包時，真正的原因通常是缺一個工具、一條規則寫得太模糊、少一個 guardrail 或 context 塞滿了雜訊。」

## 連結到的 wiki
- [[Agentic_Engineering]]（本片核心，新建）
- [[Harness_Engineering]] · [[Context_工程]] · [[Vibe_Coding]]
- [[Google]] · [[Gary_Chen]] · [[MCP]] · [[Subagent]]

## 我的問題 / 待追蹤
- Google 課程 Day 2–5 的內容（Evals、Multi-agent？）值得追
