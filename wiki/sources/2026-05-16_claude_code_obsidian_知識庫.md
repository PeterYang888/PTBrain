---
type: source
tags: [Claude_Code, Obsidian, 知識庫, Token節省, RAG, 個人知識管理]
created: 2026-05-16
source_url: https://www.youtube.com/watch?v=dlnqJIgsiAg
source_date: 2026-05-16
source_type: transcript
---

# Claude Code + Obsidian 個人知識庫：Token 節省 95%

> 來源：[原始檔](../../raw/transcripts/2026-05-16_claude_code_obsidian_知識庫.md)

## 一句話摘要
用 Claude Code + Obsidian 構建結構化個人知識庫（raw/wiki/index/log 四層），透過「消化（Ingest）」機制取代碎片化 RAG，達到 AI 知識累積和 Token 節省 95% 的效果。

## 核心論點
- 四層架構：raw（原始資料，唯讀）/ wiki（知識實體，AI 維護）/ index.md（導航）/ log.md（時序記錄）
- Ingest 機制：與 RAG 根本不同 — RAG 找相似片段，Ingest 建立結構化連結網路，AI 讀「有目錄的書」而非「碎紙片」
- Token 節省：AI 先讀 index.md 直接定位相關頁面，比掃描整個資料夾省去大量推理
- 重要建議：一個知識庫對應一個主題，混合主題會降低精準度

## 值得引用的段落
> 「這本質上的概念其實跟傳統的 RAG 不一樣。RAG 是找最相似的文字片段，但它不理解片段之間的關係。Wiki 有點像讀書，AI 讀的是一本整理好、有目錄、有交叉引用的書。」

## 連結到的 wiki
- [[Claude_Code]]
- [[RAG]]
- [[Anthropic_Claude_生態]]

## 我的問題 / 待追蹤
- PTBrain 本身就是這個架構的實踐，應記錄差異與改進
- 95% Token 節省是否有可驗證的基準測試？
