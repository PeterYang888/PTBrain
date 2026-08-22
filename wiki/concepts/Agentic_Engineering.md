---
type: concept
tags: [ai, agent, harness, workflow, engineering]
created: 2026-07-18
updated: 2026-08-22
sources: [2026-07-18_google_agentic_engineering_day1, 2026-08-09_google_ai課程day4_5]
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

## 落地生產環境的三大動作（Day 4+5，2026-08-09）
Day 1 定義了 Agent = Model + Harness 的框架後，Day 4+5 給出讓 Agent 安全上正式環境的具體動作，工程師的角色從「寫程式碼」轉向「藍圖建築師」（見 [[2026-08-09_google_ai課程day4_5]]）：

1. **Spec（規格）**：五大元素——做什麼、為什麼做、用什麼做（寫死工具版本）、什麼不能碰（底線）、什麼叫完成（Given-When-Then 驗收格式）。指令格式未優化，AI 表現最多可相差 40%（SKCC 論文，未查證原文）
2. **Security（零信任防護）**：AI 必然犯錯，重點是「就算犯錯也傷不到系統」的三層防禦——沙盒（用完即丟）、Human-in-the-loop（高風險動作設 Checkpoint，Code 翻譯回白話文供人審核）、套件白名單與固定版本（防 Slop squatting：駭客搶註 AI 幻覺出的虛擬套件名稱植入惡意代碼）
3. **Evaluation（實戰驗收）**：不是二元對錯，而是打分數看「漂移」——初始需求當考題、看成品不看程式碼、看收斂輪數（改 8 次還錯最有分析價值）、收集被糾正的話回頭修 Spec

**可觀測性（Observability）**：完整記錄整趟任務、每步思考過程、工具與參數——用來監控 **Denial of Wallet**（Agent 陷入無限迴圈狂燒付費 API）這類安全威脅

**人類審查瓶頸**：AI 產碼速度提升，但造成 Reviewer「微管理倦怠」（重度使用 AI 者 Burnout 機率高出 45%），解法是 **Conditional LGTM**（人工審完架構給有條件同意，自動化測試通過後系統自動合併）或 CI 掛載 AI Reviewer 代理

## 來源
- [[2026-07-18_google_agentic_engineering_day1]]
- [[2026-08-09_google_ai課程day4_5]]
