---
type: source
tags: [ai, agent, multi-agent, workflow, claude-code]
created: 2026-07-10
updated: 2026-07-10
source_url: https://www.youtube.com/watch?v=4dom8ne0hg0
source_date: 2026-07-10
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "CKY channel（Kelly Tsai）"
  processed_by: notebooklm-py
---

# Agent Teams 怎麼運作？Subagent、Agent Teams 與 Dynamic Workflows

## 一句話摘要
這部影片深入剖析了 AI Agent 團隊（從 Subagent 到 Dynamic Workflows）的協作模式與效能瓶頸，強調未來工程師的核心價值將轉向系統設計、任務判斷與結果審核。

## 頻道/主講者背景
主講者為 **Kelly Tsai**，其 YouTube 頻道為 **CKY channel**。她擁有超過一年使用 AI 協助編寫程式的實務經驗，擅長觀察矽谷科技圈趨勢並解構複雜的 AI 技術術語。

## 核心論點
* **AI 協作的三種分級模式**：分為彼此獨立回報的 **Subagent**（適合定義明確且可並行的任務）、具備群組溝通機制的 **Agent Teams**（適合需要互相對齊的任務），以及由 AI 自主規劃、執行與驗收的 **Dynamic Workflows**。
* **以 Context（上下文）而非角色分工**：最穩定的系統設計應根據「誰需要看到哪些資料」來分配任務，若單純按角色頭銜（Role）分工，容易在資訊交接中產生「傳話遊戲」般的丟失，導致錯誤放大。
* **多代理系統的效能與成本陷阱**：更多 Agent 不代表更強。在需要逐步推理的任務中，多 Agent 效能可能退步至原本的 70%；且因工具重算與訊息往返，成本可能是單一 Agent 的三倍以上。
* **工程師價值的典範轉移**：2026 年後，工程師真正的競爭力不在於會開多少 Agent，而在於具備判斷「何時該開團隊」的決策力，以及作為一名合格「Reviewer」的審核力。

## 關鍵細節與數據
* **極端案例數據**：一名工程師利用 AI 團隊在 **11 天**內翻寫了 **75 萬行**的程式碼專案。
* **Claude Dynamic Workflows 效能規格**：Anthropic 提及該功能支援同時（parallel）開啟 **16 個**分身，一輪任務上限可達 **1000 個**。
* **性能風險指標**：
    * 結構不良的系統會將錯誤放大 **17 倍**。
    * 循序漸進式任務中，多 Agent 表現可能退步至原本的 **70%**。
    * 實際生產環境中，多 Agent 系統失敗率常 **過半**。
* **Replit 工具設定與方案**：
    * **Replit Pro**：支援同時（parallel）運行最多 **10 個 agents**。
    * **一般 Replit 方案**：同時運行 **2 個 agents**。
    * **Credits 售價範例**：購買 **$500** 的 credits 優惠價為 **$440**。

## 值得引用的金句
* 「是不是一個工程師帶著一隻 AI 團隊就可以抵過一整個團隊的時代真的來了？」
* 「結構設計得好的可以幫你加速，結構亂搞的卻會把錯誤放大 17 倍以上。」
* 「問題出在系統設計，不在模型本身。」
* 「2026 年工程師真正值錢的不是會不會開一堆 agent，而是判斷出來什麼時候應該要開團隊，什麼時候用一個就夠了。」
* 「一兩年後會帶一個 AI 團隊，會變成跟今天會用 Google 一樣基本的能力。」

## 與其他 AI 工具/概念的關聯
* **AutoGPT / AutoGen / CrewAI**：影片指出 AI Agent 團隊概念並非全新，這些工具已在業界摸索數年。
* **GitHub Branches**：將 Replit 的多 Agent 協作模式類比為 Git 的分支（branches）與合併（try to merge back to main）機制。
* **N8N**：將 Dynamic Workflows 與 N8N 的固定自動化流程（Fixed Workflows）做對比，前者適合路徑需隨任務進展動態調整的情境。
* **Reviewer 角色**：強調在 AI 快速產出的時代，人類角色轉向軟體開發中的代碼審查者（Reviewer），負責最終的拍板與品質控管。

註：來源影片主要討論 **Claude Dynamic Workflows** 及其協作架構，並未提及「Claude Code」CLI 指令或「MCP」具體設定範例。
