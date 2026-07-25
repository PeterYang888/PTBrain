---
type: entity
entity_type: product
tags: [anthropic, claude, agent]
created: 2026-04-17
updated: 2026-07-25
sources: [2026-04-16_claude_模型選擇指南, 2026-07-10_六月_ai_更新彙整, 2026-07-25_claude_record_a_skill]
---

# Claude Cowork

> [[Anthropic]] 付費方案的進階 agentic 功能之一，與 [[Claude_Code]] 並列。授權 AI 自主調用工具、執行複雜程式碼、跨文件執行任務。

## 目前已知
- 屬於 Anthropic 的 agentic AI 產品線
- 與 [[Claude_Code]] 同樣開放給付費用戶
- 對話框可切換 `chat` / `co-work` 兩種模式；agentic 能力（如下方錄製功能）僅在 `co-work` 模式可用（[[2026-07-25_claude_record_a_skill]]）

## Record a Skill（2026-07-25 確認）
co-work 模式內建「示範即自動化」功能（見 [[示範式自動化]]）：
- 路徑：對話框 `+` → `record a skill` → 選麥克風開錄；可 `discard` 重錄
- Claude 同時捕捉**螢幕截圖**與**語音敘述**，學習操作意圖後存為可重複調用的 Skill
- 實測：57 秒錄完「YouTube Studio 下載數據」流程
- 對標 [[OpenAI_Codex]] 的 Record & Replay（[[2026-07-18_codex_record_replay_fork]]）

## 可能的新進展（2026-07-10，**推測**）
[[2026-07-10_六月_ai_更新彙整]] 提到 [[Anthropic]] 的「**Claude Tech**」（疑為語音辨識誤植，推測即本產品）：
- 整合至 **Slack**；管理員可授權其存取工具、資料與程式碼庫
- 具備 **Ambience（環境感知）** 模式，可自動整理未解決的討論、提醒任務
- 定位同 Microsoft Copilot Coworker / [[OpenAI_Codex]] Record and Reply 一線——「AI 同事」而非「AI 工具」（見 [[RPA]]）

## 待追蹤 / 缺口
- 具體用途 vs. [[Claude_Code]] 的差別？
- 「Claude Tech」是否即 Claude Cowork，**待官方來源核實**
- 錄出的 Skill 能否編輯／匯出？與 Claude Code skill 格式是否互通？

## 相關來源
- [[2026-04-16_claude_模型選擇指南]]（僅提及一次）
- [[2026-07-10_六月_ai_更新彙整]]（「Claude Tech」Slack 整合，推測為本產品）
- [[2026-07-25_claude_record_a_skill]]（record a skill 實操示範）
