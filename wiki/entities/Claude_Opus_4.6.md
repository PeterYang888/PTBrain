---
type: entity
entity_type: product
tags: [anthropic, claude, llm-model, flagship]
created: 2026-04-17
updated: 2026-04-17
sources: [2026-04-16_claude_模型選擇指南]
---

# Claude Opus 4.6

> [[Anthropic]] 智慧層級最高的旗艦模型。主打複雜推理、多步驟問題拆解、精密程式設計。Anthropic 在程式開發、企業自動化代理與專業工作流程上的主推款。

## 規格
| 項目 | 值 |
|---|---|
| 上下文窗口 | 1M tokens |
| 最大輸出 | 128K tokens |
| 輸入定價 | US$5 / MTok |
| 輸出定價 | US$25 / MTok |
| [[延伸思考]] | ✅ |
| [[自適應思考]] | ✅ |

## 定位
三軸中「能力」最強，但成本最高。輸出成本是 [[Claude_Haiku_4.5]] 的 5 倍。

## 適用情境
- 複雜的軟體工程開發與除錯
- 長達數小時的研究分析任務
- 高度推理要求的科學或數學問題
- 企業級 agent 部署
- **準確性比成本更重要**的場景

## 與其他模型的差別
- 比 [[Claude_Sonnet_4.6]]：同支援 [[自適應思考]]、同為 1M context，但輸出 128K（Sonnet 64K）、單位成本約為其 1.67 倍
- 比 [[Claude_Haiku_4.5]]：多了 [[自適應思考]]，context 5 倍、輸出 2 倍、單位輸出成本 5 倍

## 實戰角色：雙模型「架構師」（2026-06-19）
在 [[Claude_Code]] 逆向工程復刻老遊戲的案例中，Opus 擔任 **架構師（Architect）**——負責深層思考、拆解模組、撰寫技術文檔，再交 [[Claude_Sonnet_4.6|Sonnet]]（執行者）高速生成代碼。此「Opus 規劃、Sonnet 執行」即 [[Loop_Engineering]] 的雙模型實踐（見 [[2026-06-19_ai復活老遊戲]]）。

## 相關來源
- [[2026-04-16_claude_模型選擇指南]]
- [[2026-06-19_ai復活老遊戲]]（架構師角色）
