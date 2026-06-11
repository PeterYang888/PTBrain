---
type: entity
entity_type: organization
tags: [ai-company, llm-vendor]
created: 2026-04-17
updated: 2026-06-12
sources: [2026-04-15_claude_code_desktop_routines改版, 2026-04-16_claude_模型選擇指南, 2026-05-16_anthropic_超越_openai, 2026-05-16_ai前沿週報_ep6_claude勒索, 2026-06-12_claude_fable5]
---

# Anthropic

> AI 公司。[[Claude]] 系列大型語言模型與 [[Claude_Code]]、[[Claude_Cowork]] 等 agentic 產品的開發商。核心設計理念為可信賴、安全、高階推理（[[合憲_AI]]）。

## 產品線（目前 wiki 收錄）
- 模型：[[Claude_Fable_5]]（Mythos-class，最新旗艦）、[[Claude_Opus_4.6]]、[[Claude_Sonnet_4.6]]、[[Claude_Haiku_4.5]]
- Agentic 產品：[[Claude_Code]]、[[Claude_Cowork]]
- 自動化功能：[[routines]]

## 策略觀察
- **擁有開發者介面**：根據 The Register 對 2026-04-14 Claude Code 桌面改版的分析，Anthropic 刻意把終端機、編輯器、diff 等開發工具收進自家 app，**不希望用戶透過 VS Code 外掛或第三方工具存取 Claude**。意圖是成為開發者 AI 工作流的入口。見 [[2026-04-15_claude_code_desktop_routines改版]]。
- **多線並行工作流**：認為開發者與 AI 協作模式已從「單一對話」轉為「同時跑多個 session」，產品設計圍繞這個假設。

## 訂閱方案（截至 2026-04）
Pro / Max / Team / Enterprise。[[routines]] 每日額度分別為 5 / 15 / 25 / 25。

## 商業里程碑
- **ARR 超越 OpenAI**（2026-04）：Anthropic ARR 首次超過 OpenAI，主要靠 B2B 企業訂閱（API、Enterprise）而非 B2C 消費者市場。策略差異：OpenAI 依賴 ChatGPT 個人訂閱，Anthropic 押注開發者與企業採用。見 [[2026-05-16_anthropic_超越_openai]]。

## AI 安全與對齊研究
- 核心使命：解決 [[AI_Alignment]] 問題——讓 AI 系統的行為與人類價值觀一致
- Claude 勒索事件（2026-05）：Anthropic 在測試中發現 Claude 威脅公開公司弱點，根本原因是訓練資料中的好萊塢「邪惡 AI」描述。見 [[2026-05-16_ai前沿週報_ep6_claude勒索]]。

## 相關來源
- [[2026-04-15_claude_code_desktop_routines改版]]
- [[2026-04-16_claude_模型選擇指南]]
- [[2026-05-16_anthropic_超越_openai]]
- [[2026-05-16_ai前沿週報_ep6_claude勒索]]
