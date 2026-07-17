---
type: concept
tags: [ai, agent, harness, workflow, engineering]
created: 2026-07-18
updated: 2026-07-18
sources: [2026-07-18_google_agentic_engineering_day1]
---

# Agentic Engineering

> [[Vibe_Coding]] 的正式化下一階段：以嚴格結構、驗證機制與 Harness 設計來開發 AI 系統的工程範式；Google 官方五天開發課將其定名並給出正式框架。

## 核心公式與主張
- **Agent = Model + Harness**：模型本身不是 Agent；Harness 提供狀態、工具執行、反饋迴圈與行為約束（六大組件見 [[Harness_Engineering]]）
- **[[Context_工程|Context Engineering]] 優於 Prompt Engineering**：核心技能是把任務背景、領域知識、範例、工具定義編成 AI 能高效利用的動態形式
- **工廠模型（Factory Model）**：開發者的產出不再是程式碼，而是「產出程式碼的系統」——規格定義、實作 agents、自動化測試（Evals）、失敗回傳機制
- **Token 經濟學（Capex/Opex）**：前期投入系統設計與 Context 整理（Capex），靠提高一次成功率（First Pass Success Rate）降低長期 Token 燃燒率（Opex）

## 與其他概念的差別
- 跟 [[Vibe_Coding]]：Vibe Coding 是直覺式起點（快速原型 OK）；Agentic Engineering 加上驗證與約束，才能碰生產系統（「跟 CTO 說在 Vibe Coding 付款系統，他臉都綠了」）
- 跟 [[Harness_Engineering]]：Harness 是 Agentic Engineering 的系統實現層；本概念是整體工程範式（含流程、Evals、經濟學）
- 跟 [[Agentic_Workflow]]：Agentic Workflow 描述「AI 如何工作」；Agentic Engineering 描述「人如何工程化地建造與驗證它」

## 關鍵引言
> 「Generation is solved. Verification, judgment and direction are the new craft.」

呼應 [[理解成本]]：產出成本趨零後，驗證與判斷成為新瓶頸；SDLC 的實作階段被壓縮，「驗證」成為新的流程瓶頸。

## 關鍵數據（依 Google 課程說法）
- 85% 專業開發者使用 AI agent；41% 新程式碼由 AI 生成
- 反例：資深工程師缺驗證機制用 AI，特定任務效率反降 19%

## 來源
- [[2026-07-18_google_agentic_engineering_day1]]
