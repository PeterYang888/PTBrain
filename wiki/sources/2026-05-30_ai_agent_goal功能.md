---
type: source
tags: [ai-tooling, agentic, goal, automation, rubric]
created: 2026-05-30
source_url: https://www.youtube.com/watch?v=PpeCur6fEXc
source_date: 2026-05-30
source_type: transcript
---

# 我的 AI agent 連續跑了 27 個小時，/goal 功能怎麼用？

> 來源：[briefing](../../raw/transcripts/2026-05-30_ai_agent_goal功能.md)

## 一句話摘要
`/goal` 功能透過「實作者 + 評審」雙角色讓 AI 持續自主工作，而成功關鍵不是 prompt 技巧，是建立具體的 Rubric（評審準則）。

## 核心論點
- **真正自動化 = 把任務從心上移走**：不只移出手，還要移出腦；只要心裡掛念未完成任務，認知資源就持續消耗。
- **Context Anxiety（上下文焦慮）**：AI 感覺 context window 快滿時，會產生「下班心態」——假裝完成、詢問不必要的確認、偷懶交差。
- **/goal 雙角色架構**：Executor 執行任務，Reviewer 持續審查「目標是否達成」，未達成就要求繼續；AI 沒有「完成幻象」的退路。
- **Rubric 五大元素**：預期結果 / 驗證方式 / 限制條件 / 迭代策略 / 錯誤處理——缺一不可。
- **品位拆解四維度**（Anthropic 框架）：設計品質、原創性、技術執行、可用性；針對模型弱項加重評分權重。

## 值得引用的段落
> 「把任務從你手上移到 AI 手上，只走完了自動化的前半段；後半段是把那件事從你的心上徹底移開。」

> 「寫 Rubric 表面上是給 AI 用的，但實際上它是在逼你把那些一直以來只存在你腦袋裡的模糊品位，具體寫成文字。」

## 連結到的 wiki
- [[Agentic_Workflow]] — /goal 是 agentic 工作流的具體實現
- [[Claude_Code]] — 採用 /goal 功能的工具之一
- [[Vibe_Coding]] — 人類定義目標，AI 自主執行的模式
- [[Anthropic]] — Context Anxiety 為 Anthropic 2025 末研究發現

## 我的問題 / 待追蹤
- Rubric SOP 六步驟值得整合進個人 workflow 實驗
- Context Anxiety 的研究論文在哪？
