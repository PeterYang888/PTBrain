---
type: source
tags: [ai, agent, google, gemini, automation]
created: 2026-06-27
updated: 2026-06-27
source_url: https://www.youtube.com/watch?v=V2gNi-jmjY0
source_date: 2026-06-27
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "Julian Goldie SEO"
  processed_by: notebooklm-py
---

# Gemini Spark: Automate Anything — Google 的 24/7 AI 代理人

## 一句話摘要
Gemini Spark 是 Google 推出的 24/7 自動化 AI 代理人，能在雲端背景持續執行多步驟任務、應用個人化技能並依排程運作，實現從「對話式 AI」到「系統化工作流」的轉型。

## 頻道/主講者背景
主講者為 Julian Goldie（影片中以數位分身呈現），是 Julian Goldie SEO 頻道的創立者，專注分享如何將 AI 工具實際應用於工作流以節省時間，並經營「AI Profit Boardroom」社群提供 AI 自動化的實作教學。

## 核心論點
- **從聊天機器人進化為自主代理人**：傳統 AI 僅在對話時運作，Gemini Spark 是真正的代理人，能在用戶離線（手機關機、電腦蓋上）時持續工作。
- **基於雲端的 24/7 運作**：運行於專用的 Google Cloud 虛擬機，不依賴本地設備，確保任務不中斷。
- **三大核心支柱（任務、技能、排程）**：透過「任務」設定目標、「技能」賦予個人化背景、「排程」實現自動化觸發。
- **原生數據存取與開放標準擴展**：具備 Google Workspace（Gmail、Drive 等）的原生數據權限，並透過 MCP 協議連結第三方工具。
- **零代碼的民主化開發**：無需程式背景或高深 Prompt Engineering，僅需自然語言即可指揮 AI 執行複雜 SOP。

## 關鍵細節與數據
- **開發狀態**：目前 Beta 測試、標記「實驗性（Experimental）」，僅限美國地區的 Google AI Ultra 訂閱者使用。
- **運行容量**：系統最多支援 **15 個任務** 同時在背景運行。
- **核心組件**：
  - **Tasks**：多步驟目標，如「未來兩週追蹤行業職缺」「從 Gmail 提取交付物清單存入 Google Doc」。
  - **Skills**：可重用的風格/邏輯，例如分析 50 封郵件後建立名為 `ghostriter` 的風格指南；支援 `@` 或 `/` 指令呼叫。
  - **Schedules**：時間觸發（每週一早上 9 點總結進度）或事件觸發（航班延誤時自動更新行程）。
- **應用整合**：原生整合 Gmail、日曆、雲端硬碟、文件、試算表、簡報、YouTube、Google Maps；MCP 第三方已支援 Canva、OpenTable、Instacart，預計 **2026 夏季** 加入 Adobe、Spotify、GitHub、Notion、Slack。
- **安全機制**：設有「檢查點（Checkpoints）」，涉及密碼或敏感操作時暫停並請求人工授權，以防禦提示詞注入（Prompt Injection）。

## 值得引用的金句
- 「舊模型是 AI 回答你的問題；新模型是 AI 運行你的工作流。」——總結 AI 從搜尋引擎到生產力系統的思維轉變。
- 「這不是單純的自動化，而是具備上下文背景的自動化（Automation with context）。」——強調「技能」如何讓 AI 模仿用戶的真實聲音與邏輯。
- 「如果你的 AI 在你睡覺時仍持續工作，那會如何？這不再只是假設。」——描述全天候自動化前景。

## 與其他 AI 工具/概念的關聯
- **AI Agent**：Gemini Spark 是 AI 代理人的具體實踐，強調「自主執行」而非「被動問答」。
- **MCP (Model Context Protocol)**：連結 AI 與第三方工具的開放標準，讓 Gemini Spark 跨出 Google 生態系與 Slack、Notion 等協作。
- **Workflow Automation**：將日常手動任務（彙整週報、內容研究）轉化為 Agentic Workflow，把執行瓶頸從人類時間釋放。
- **Agent OS**：主講者提出的實作框架，將 AI 代理人整合進企業底層運作，實現規模化產出。
