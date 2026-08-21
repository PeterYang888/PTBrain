---
type: source
tags: [ai, claude-code, context-engineering, workflow]
created: 2026-08-22
source_url: https://www.youtube.com/watch?v=d4329xvSDK4
source_date: 2026-08-22
source_type: transcript
---

# AI 額度老是不夠用？三招省 Token 的實戰方法

> 來源：[原始逐字稿](../../raw/transcripts/2026-08-22_省token三招_context管理.md) · [[Gary_Chen]]

## 一句話摘要
分享「丟掉用不到的」、「縮減留下來的」、「善用 Prompt Caching 折扣」三招，節省 Token 的同時清除 AI 的雜訊 context，提升產出品質。

## 核心論點
- LLM 底層 API 無記憶，每次送出都要重新注入系統規則／工具說明／對話歷史／外部檔案四層 context，這是 token 越滾越大的主因
- 縮短 prompt 或換小模型效果有限：歷史 context 已佔大宗，縮短當前輸入省不了多少；小模型出錯反而多花更多來回
- 三招心法：換任務開新對話＋編輯回溯＋精簡工具（丟）／先搜尋再餵＋給結論清過程＋縮小輸入輸出（縮）／善用 Prompt Caching（折扣）
- Prompt Caching：命中快取價格打一折（省 10 倍），但壽命約 1 小時，且中途換模型／調思考強度／開加速模式會整包失效

## 連結到的 wiki
- [[Gary_Chen]] — 主講者
- [[Context_工程]] — 四層 context 結構、漸進式載入原則的具體實戰版
- [[Prompt_Caching]] — 本集新建的快取折扣機制專頁
- [[指令預算]] — 姊妹概念（token 稀缺 vs 注意力稀缺）

## 我的問題 / 待追蹤
- 影片提到的「交接 Prompt」（Patreon 資源）與既有的 Markdown 交接法是否可以整理成可重用範本？
