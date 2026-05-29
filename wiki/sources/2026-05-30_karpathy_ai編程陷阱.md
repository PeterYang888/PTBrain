---
type: source
tags: [ai-tooling, karpathy, claud-md, vibe-coding, code-quality]
created: 2026-05-30
source_url: https://www.youtube.com/watch?v=-H1n7teqW7A
source_date: 2026-05-30
source_type: transcript
---

# Karpathy 發現的 AI 編程三大陷阱｜14萬Star的秘密：一個文件如何降低 AI 返工率

> 來源：[briefing](../../raw/transcripts/2026-05-30_karpathy_ai編程陷阱.md) · [[Andrej_Karpathy]]

## 一句話摘要
Karpathy 指出 AI 編程的三大致命缺陷（錯誤假設、過度複雜化、無關編輯），而 `claud.md` 四條規則將返工率從 41% 降至 11%。

## 核心論點
- **三大陷阱**：
  1. 錯誤假設——AI 憑空假設需求並執行，不主動澄清
  2. 過度複雜化——用 1000 行解決 100 行能完成的問題
  3. 無關編輯——改動與當前任務無關的既有代碼或注釋
- **`claud.md` 四條核心規則**：
  1. 編碼前思考（Think Before Coding）— 消除錯誤假設
  2. 簡潔優先（Simplicity First）— 對抗過度複雜化
  3. 精準修改（Precise Modifications）— 只碰必須碰的部分
  4. 目標驅動執行（Goal-Driven Execution）— 聲明式目標 + 循環驗證
- **實測數據**：30 個代碼庫、6 週實測，返工率 41% → 11%
- **2026 年是「高能量年份」**（Karpathy 語）：有工程憲法的團隊 vs 被劣質 AI 代碼淹沒的團隊，將出現分水嶺。

## 值得引用的段落
> 「AI 已經足夠聰明了，問題是指導問題。大多數人用 AI 編程的方式就像在和一個極其聰明、但完全沒有常識的外星人溝通。」

> 「代碼質量的決定因素已從『模型能力』轉向『約束的清晰度』。」

## 連結到的 wiki
- [[Andrej_Karpathy]] — 影片主角，主要觀點來源
- [[Vibe_Coding]] — claud.md 是 Vibe Coding 的重要配套工具
- [[Claude_Code]] — claud.md 即 CLAUDE.md，直接影響 Claude Code 工作方式
- [[Agentic_Workflow]] — 目標驅動執行（Goal-Driven）是 agentic workflow 的核心

## 我的問題 / 待追蹤
- claud.md GitHub 連結：作者 @freschange（張家園）
- 完整四條規則值得直接整合進本 vault 的 CLAUDE.md 參考
