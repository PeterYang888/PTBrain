---
type: entity
entity_type: product
tags: [ai, notebooklm, knowledge-management, google]
created: 2026-06-19
updated: 2026-07-18
sources: [2026-06-19_notebooklm整座圖書館, 2026-07-18_notebooklm_2_0_更新]
---

# NotebookLM

> Google 推出的 AI 研究/筆記工具，以使用者上傳的來源為依據生成摘要、音訊、心智圖、簡報等；由 Gemini 驅動。

## 關鍵事實
- 一次可丟入多達 **50 個**來源（PDF、YouTube、雲端文件），由 [[Google|Gemini]] 模型分析（見 [[2026-06-19_notebooklm整座圖書館]]）
- 音訊摘要（Audio Overview）支援 **80+ 語言**
- 升級內建「雲端電腦」模組：自動分析數據、寫程式、產出 Excel 試算表或簡報
- 互動式問答「像打電話進 Podcast 節目讓主持人解答」
- 研究工作流閉環：雜亂來源 → 自動生成心智圖 / 音訊 / 數據圖表 / 簡報，是典型 [[Agentic_Workflow]]

## NotebookLM 2.0（2026-07-18）
從問答工具轉型為 agentic 成品生產平台（見 [[2026-07-18_notebooklm_2_0_更新]]）：
- **Studio（工作室）九大工具**：音頻概覽（5–10 分鐘，可選深入分析/摘要/評論/辯論）、演示文稿（可修改風格）、視頻概覽（10–15 分鐘生成）、思維導圖、報告、閃卡、測驗、信息圖、數據表格
- **整合進 Gemini 任務欄**：兼得 NotebookLM 的源頭可靠性與 Gemini 的創造力/寫碼能力
- **Agentic 資訊缺口偵測**：主動分析已上傳來源、指出知識遺漏、建議發起搜索補全
- **搜索三模式**：網絡搜索+快速調研 / 網絡搜索+深度研究（自動生成整合報告）/ Google Drive+快速搜索
- **Configure Notebook**：自定義指令（類 ChatGPT Project）；Google Drive 即時同步；「閱讀模式」抓取受限網頁

## 與其他頁的關係
- 屬 [[Google]] 產品線，與 [[AIOS]]「AI as OS」趨勢一致
- 本 vault（PTBrain）的 ingest 流程即用 NotebookLM 產生繁中 briefing（透過 notebooklm-py CLI）
- 相關工具對比：[[Claude_Sonnet_4.6]] 的 Artifacts、[[Claude_Code]]

## 相關來源
- [[2026-06-19_notebooklm整座圖書館]]
- [[2026-07-18_notebooklm_2_0_更新]] — 2.0 Studio 九大工具與 agentic 缺口偵測
- 多次出現於 ai-tooling 批次的 NotebookLM 教學影片
