---
type: source
tags: [ai, agentic-engineering, security, evaluation]
created: 2026-08-22
source_url: https://www.youtube.com/watch?v=h7abDtqN9gs
source_date: 2026-08-09
source_type: transcript
---

# Google AI 課程 Day 4+5 解析，怎麼放心讓 AI 上正式環境？

> 來源：[原始檔](../../raw/transcripts/2026-08-09_google_ai課程day4_5.md) · [[Gary_Chen]]（頻道「Gary Chen」）

## 一句話摘要
Google 五天 AI 課程系列最後一集：用「寫清規格（Spec）」「設好邊界（Security）」「做好驗收（Evaluation）」三大動作，讓 AI Agent 能安全落地正式環境。

## 核心論點
- 工程師轉型為「藍圖建築師」：程式碼可拋棄、低成本生成，真正有價值的資產是 Spec、Rules、Evals
- 「零信任」安全防護：AI 必然會犯錯，重點是打造「就算犯錯也傷不到系統」的防護網
- 評估非二元對錯：要用打分數與容忍範圍監控 AI 行為的「漂移」
- 人類審查瓶頸：AI 產碼速度提升造成 Reviewer「微管理倦怠」，需自動化審查機制

## 值得引用的段落
> 「AI 能幫你自動化的範圍，取決於你能驗證的範圍。換句話說，你的驗證能力就是你自動化能力的上限。」

> 「Generation is solved; verification, judgment, and direction are the new craft.」

## 連結到的 wiki
- [[Gary_Chen]] — 主講者
- [[Agentic_Engineering]] — 已更新，補上 Day 4+5 的 Spec/Security/Evaluation 三大動作
- [[Harness_Engineering]] — 三層安全防禦（沙盒/human-in-the-loop/套件白名單）呼應 Harness 的約束機制

## 我的問題 / 待追蹤
- 「SKCC」論文名稱疑為口誤/縮寫，未查證原始論文
- 本集是系列最後一集，Day 2/3 內容目前 PTBrain 尚無對應來源
