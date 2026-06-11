---
type: source
tags: [ai, claude, anthropic, model, safety, autonomous-agent]
created: 2026-06-12
source_url: https://www.youtube.com/watch?v=Y9Wz2PV404E
source_date: 2026-06-12
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# Introducing Claude Fable 5

> 來源：[原始檔](../../raw/transcripts/2026-06-12_claude_fable5.md) · [[Anthropic]] · [[Claude_Code]]

## 一句話摘要
Claude Fable 5（Mythos-class 神話級模型）以極高自主性為賣點，可在無人干預下連續執行數日；但因 Mythos preview 測試發現能識別數千個網路漏洞，正式版加入「自動審核 + Opus 4.8 重定向」安全機制。

## 核心論點
- **Mythos-class 定位**：Fable 5 是 Anthropic 最強大的公開模型；高度自主性，能獨立運作數日，處理編碼/金融/研究/法律等長程複雜任務
- **安全問題優先**：Mythos preview 能識別數千個網路漏洞 → 正式版加入「高風險請求自動審核」機制
- **Opus 4.8 重定向**：當請求涉及網路安全或生物學高風險領域時，系統自動改用 Opus 4.8 處理，以降低 Fable 5 帶來的極端風險
- **主動防護先行**：公開前先讓 Fable 5 協助安全專家修補漏洞，優先發揮防護價值
- **Human-in-the-loop 降低**：比前代模型更少需要人工干預，適合「晚上交代任務、隔天查結果」的工作流

## 值得引用的段落
> 「Fable 5 是一個神話級（Mythos-class）模型，具備使其足以供大眾使用的防護機制。」

> 「我們將這些請求定向至 Opus 4.8……以便人們可以繼續從 Fable 這樣強大的模型中獲益，而不會產生隨之而來的網路和生物風險。」

## 連結到的 wiki
- [[Claude_Fable_5]]
- [[Anthropic]]
- [[AI_Alignment]]
- [[Agentic_Workflow]]

## 我的問題 / 待追蹤
- Fable 5 是否已正式發布或仍為 preview？模型 ID 為何？
- Fable 5 與 Opus 4.8 的定位關係？（Fable 5 = 新旗艦，Opus 4.8 = 安全降級？）
