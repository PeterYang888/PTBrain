---
type: entity
entity_type: product
tags: [anthropic, claude, llm-model, workhorse]
created: 2026-04-17
updated: 2026-04-17
sources: [2026-04-16_claude_模型選擇指南]
---

# Claude Sonnet 4.6

> [[Anthropic]] 的主力日常模型。在智慧與速度間取得平衡—能應付大多數進階任務，不像 [[Claude_Opus_4.6]] 那麼費工，卻比 [[Claude_Haiku_4.5]] 有更強推理。

## 規格
| 項目 | 值 |
|---|---|
| 上下文窗口 | 1M tokens（beta） |
| 最大輸出 | 64K tokens |
| 輸入定價 | US$3 / MTok |
| 輸出定價 | US$15 / MTok |
| [[延伸思考]] | ✅ |
| [[自適應思考]] | ✅ |

## 定位
日常生產力主力。支援延伸思考與多輪 agent 工具使用。適合內容創作者、分析師、需要頻繁與 AI 來回互動的工作者。

## 適用情境
- 程式碼生成與程式開發輔助
- 資料整理與分析報告
- 內容寫作與多版本草稿生成
- 圖像理解與說明
- 搭配外部工具的 agent 工作流程

## 與其他模型的差別
- 比 [[Claude_Opus_4.6]]：輸出 64K（Opus 128K）、單位輸出成本為 Opus 的 60%；[[自適應思考]] 同樣支援
- 比 [[Claude_Haiku_4.5]]：多了 [[自適應思考]]、context 5 倍、輸出成本 3 倍

## 實戰角色與 Artifacts（2026-06-19）
- **雙模型「執行者」**：在逆向工程復刻案例中，Sonnet 擔任執行者，依 [[Claude_Opus_4.6|Opus]] 架構師的文檔高速生成代碼（見 [[2026-06-19_ai復活老遊戲]]）
- **Artifacts 介面**：[[2026-06-19_notebooklm整座圖書館]] 將 Sonnet 4.6 + Artifacts（約 20 萬字上下文）列為當前寫作與編程的首選工具

## 相關來源
- [[2026-04-16_claude_模型選擇指南]]
- [[2026-06-19_ai復活老遊戲]]（執行者角色）
- [[2026-06-19_notebooklm整座圖書館]]（Artifacts）
