---
type: source
source_type: article
tags: [anthropic, claude-code, ai-dev-tools, agent]
created: 2026-04-17
source_url: https://www.bnext.com.tw/article/90646/claude-code-routines-update
source_date: 2026-04-15
publisher: 數位時代 / Business Next
---

# Claude Code 官方 App 大改版：內建終端機、側邊欄 + routines 雲端自動化

> 來源：[原始檔](../../raw/Claude%20Code官方App大改版！內建終端機、側邊欄，專為「一心多用」開發而生.md) · 《數位時代》編輯：李先泰（初稿 AI 編撰）
> 原始公告來自 [[Anthropic]] 官方部落格（2026-04-14）與 The Register 報導。

## 一句話摘要
[[Anthropic]] 於 2026-04-14 同步發布 [[Claude_Code]] 桌面 app 重大改版與全新 [[routines]] 雲端自動化，目標是擁有開發者介面、支援「多線並行」AI 工作流。

## 核心論點
- 桌面 app 為**多線並行**工作流重構：側邊欄集中管理 session（依狀態 / 專案 / 環境篩選，PR 合併自動歸檔），支援 `/btw` [[side_question]] 在不中斷主任務下快速查詢。
- 開發工具內建化：整合終端機、檔案編輯器、diff 檢視器、預覽面板（含 HTML / PDF），所有面板可拖放排列。SSH 遠端從 Linux 擴展至 Mac。
- **[[routines]]**（研究預覽）：將提示詞 + 程式庫 + connectors 包成自動化配置；三種觸發—**排程** / **API 呼叫** / **GitHub 事件**。
- 戰略意圖（據 The Register 分析）：Anthropic 刻意把開發工具收進自家介面，**不希望用戶透過 VS Code 外掛或第三方工具存取 Claude**。
- 桌面版與 CLI 外掛行為完全對等；顯示模式分 Verbose / Normal / Summary，透明度可調。

## routines 每日額度
| 方案 | 每日執行上限 |
|---|---|
| Pro | 5 |
| Max | 15 |
| Team / Enterprise | 25 |

超額部分需啟用額外用量計費。

## 官方範例用途
- **排程**：每晚掃新 issue 發 Slack 摘要；每週盤點 PR 找出該更新的文件自動開 PR
- **部署觸發**：上線後自動跑煙霧測試 + 掃錯誤日誌
- **GitHub 事件**：PR 開啟自動跑安全/效能檢查；SDK A 合併的改動自動搬到 SDK B

## 值得引用的段落
> 「開發者與 AI 協作的模式已經改變：同時在多個程式庫中啟動重構、修 bug、寫測試，在結果回傳時逐一檢視並即時調整方向。」— Anthropic 官方部落格

## 連結到的 wiki
- 公司：[[Anthropic]]
- 產品：[[Claude_Code]]
- 概念：[[routines]]、[[side_question]]
- 主題：[[Anthropic_Claude_生態]]

## 我的問題 / 待追蹤
- routines 的 connectors 實際支援哪些外部系統？
- 桌面 app 與 CLI 「完全對等」是否包含自訂 skills / hooks？
- `/btw` 是否支援跨 session？
