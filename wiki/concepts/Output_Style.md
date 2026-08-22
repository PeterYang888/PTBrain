---
type: concept
tags: [claude-code, prompt-engineering, workflow]
created: 2026-08-15
updated: 2026-08-15
sources: [2026-08-15_claude_output_style_不降智]
---

# Output Style

> [[Claude_Code]] 的專案層級設定，用來規範 AI 輸出的技術密度與語氣，不影響其程式碼編寫能力。

## 詳細說明
把「跟我說話的方式」寫成規則檔存進 output style 資料夾，之後在設定裡隨時切換。核心價值：把「AI 太囉唆／看不懂」從模糊抱怨轉成可執行的溝通規則，且對程式碼實作能力完全無副作用——只改報告格式，不改思考與執行。

## 關鍵特徵 / 組成
- **內建 4 套**：`default`（簡潔有效率）、`proactive`（行動派、少討論）、`learning`（故意留白讓使用者練習）、`explanatory`（每個改動解釋架構與 pattern，適合不熟的專案）
- **儲存於專案層級**（settings local），不同專案可掛不同風格，互不影響
- **設定方式**：把風格文字貼給 Claude 說「加進 output style」→ `/config` → 選 `output style` → 選定套用
- **自建流程**：用 `/branch` 從當前對話分支，要求 AI 用多種風格重寫回覆，挑選後固化成自訂 style
- **依對象分流**：技術小白（術語必解釋＋高風險動作先警告）、Vibe Coder/PM（[[STE100]] 簡報版＋tradeoff 對比）、工程師（先講結論與風險，細節按需追問）

## 與其他概念的差別
- 跟 [[STE100]] 的關係：STE100 是句構層級的寫作標準，可作為 output style 的其中一條規則來源，而非等同概念
- 跟 Matt Pocock 的「W」skill 的差別：output style 是長駐設定，W skill 是按需召喚的一次性翻譯

## 應用 / 實例
- [[Gary_Chen]] 團隊依技術背景設計三套自訂 style（技術翻譯機／STE100 簡報版／工程師直球版）

## 爭議 / 未定論
- 風格偏好高度個人化，沒有絕對最佳解；需自行用 `/branch` 測試找出最省力版本

## 來源
- [[2026-08-15_claude_output_style_不降智]]
