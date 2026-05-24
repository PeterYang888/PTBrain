---
type: topic
tags: [anthropic, claude, ecosystem]
created: 2026-04-17
updated: 2026-04-17
sources: [2026-04-15_claude_code_desktop_routines改版, 2026-04-16_claude_模型選擇指南]
---

# Anthropic / Claude 生態

> 關於 [[Anthropic]] 公司、[[Claude]] 模型家族、周邊 agentic 產品（[[Claude_Code]]、[[Claude_Cowork]]）的樞紐頁。

## 公司
- [[Anthropic]]

## 模型
按成本由高到低：
- [[Claude_Opus_4.6]] — 旗艦、最強推理
- [[Claude_Sonnet_4.6]] — 日常主力
- [[Claude_Haiku_4.5]] — 最快最便宜

## Agentic 產品
- [[Claude_Code]] — 程式開發 agent（CLI + 桌面 app）
- [[Claude_Cowork]] — 另一款付費 agentic 功能（資訊仍少）

## 自動化 / 功能
- [[routines]] — Claude Code 的雲端自動化（2026-04-14 研究預覽）
- [[side_question]] — 桌面 app 的 `/btw` 側邊提問

## 核心概念
- [[合憲_AI]] — Anthropic 的訓練理念
- [[延伸思考]] — 三款模型皆支援
- [[自適應思考]] — 僅 Opus / Sonnet 支援

## 時間軸
- **2026-04-14**：Claude Code 桌面 app 重大改版 + [[routines]] 研究預覽發布（見 [[2026-04-15_claude_code_desktop_routines改版]]）

## 觀察與論點
- **擁有開發者介面**：Anthropic 把開發工具收進自家 app，目標是成為開發者 AI 工作流入口，而非靠 VS Code 等第三方載體觸及用戶
- **多線並行工作流**：產品設計假設開發者會同時跑多個 AI session
- **模型分層的成本槓桿**：Opus/Sonnet/Haiku 在相同 API 下錯配可造成 5 倍成本落差；官方明確推薦「從 Haiku 起跑，不夠用再升」

## 所有相關來源
- [[2026-04-15_claude_code_desktop_routines改版]]
- [[2026-04-16_claude_模型選擇指南]]
