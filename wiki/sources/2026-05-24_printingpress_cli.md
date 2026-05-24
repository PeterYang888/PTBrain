---
type: source
tags: [Claude_Code, CLI, Token節省, Agentic, PrintingPress]
created: 2026-05-24
source_url: https://www.youtube.com/watch?v=48yu2garzl0
source_date: 2026-05-01
source_type: transcript
---

# PrintingPress：把任何網站變成 Claude Code 能用的 CLI

> 來源：YouTube（JayLuxAI | AI 自動化頻道）

## 一句話摘要
介紹如何使用 **PrintingPress** 工具將任何網站轉換為高效、省 Token 且適合 AI Agent 閱讀的 CLI，解決官方 API 笨重及 MCP 耗能的問題。

## 核心論點
- **CLI 是 Agent 時代的最佳溝通媒介**：命令列輸出純文字無雜質，是目前最適合 AI Agent 操作的方式
- **解決 Token 焦慮**：Token 成本決定 Agent 能走多遠；CLI 在本地過濾資訊，避免垃圾數據傳給雲端模型
- **API 與 MCP 的侷限性**：官方 API 回傳冗長 JSON；MCP 即使不使用也載入所有工具描述，兩者皆造成 Token 浪費
- **賦予無 API 網站操作能力**：沒有官方 API 或 MCP 的網站，10 分鐘內建置出可用 CLI
- **追求極致的「乾淨」輸出**：CLI 過濾掉不需要的欄位，只回傳 AI 執行任務真正需要的關鍵數據
- **Skill 的多層嵌套**：CLI 封裝成 Claude Code 的「Skill」，組合成複雜自動化 Pipeline
- **讀取優先於寫入**：CLI 大量用於資料讀取；複雜寫入/發布動作先衡量 Token 代價

## 關鍵細節與數據
- **Token 節省效率**：同樣任務，**MCP 消耗 Token 量是 CLI 的 35 倍**
- **數據過濾對比**：132,000 個 Token 的原始網頁在本地處理，最終只回傳 **2,000 個 Token** 給 Claude
- **官方 Library**：PrintingPress 已提供超過 **82 個**現成 CLI（Amazon、Slack、Figma、TikTok、Notion 等）
- **底層技術**：以 **Go 語言**撰寫
- **建置時間**：自定義網站 CLI 約 **10 分鐘**

## 值得引用的段落
> 「Token 成本決定你的 Agent 能走多遠。」

> 實測：132,000 個 Token 的原始網頁資料，本地過濾後只回傳 2,000 個 Token 給 Claude。

> Library 中甚至有可以讓 Agent 直接幫你**訂披薩**（Domino's）的 CLI 工具。

## 連結到的 wiki
- [[Claude_Code]]
- [[MCP]]
- [[Agentic_Workflow]]
- [[PrintingPress]]
- [[Token效率]]
- [[Anthropic_Claude_生態]]

## 我的問題 / 待追蹤
- PrintingPress 的 GitHub 在哪裡？是否開源？
- 和 MCP 的共存策略：何時用 MCP，何時用 PrintingPress CLI？
