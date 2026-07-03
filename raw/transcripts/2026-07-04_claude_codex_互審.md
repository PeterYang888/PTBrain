---
type: source
tags: [ai, claude-code, codex, harness-engineering, workflow]
created: 2026-07-04
updated: 2026-07-04
source_url: https://www.youtube.com/watch?v=xzrvAERmvRk
source_date: 2026-07-04
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "Gary Chen"
  processed_by: notebooklm-py
---

# 讓 Claude 跟 Codex 自動互審：個人 Harness 最小實踐

## 一句話摘要
透過在 Claude Code 中建立一套名為「Harness」的自動化系統，利用 stopHook 機制攔截流程，強制讓 Claude 與 Codex 進行跨模型互審，確保程式碼在達成「共識」後才放行，徹底解決 AI 編程的 Bug 與人為紀律問題。

## 頻道/主講者背景
主講者 Gary Chen，AI 工作流專家與 Solo Developer，專注於 Vibe coding（氛圍編程）與 Agentic Workflow。他致力於將「人類 SOP」系統化，讓個人開發者也能擁有如同團隊般的開發把關水準。

## 核心論點
- **打破模型自我檢查的盲點**：AI 模型傾向於認為自己寫的東西是合理的。引入第三方模型（如 Codex）能以不同權重和假設進行審核，發現原模型察覺不到的邊界情況（Corner Cases）。
- **系統勝過人為紀律**：人會因為偷懶或任務簡單而跳過審核，導致後續花費數倍時間除錯。因此必須將審核做成「系統」，在不依賴人類紀律的情況下自動觸發。
- **「天才與門衛」的分工架構**：Claude 細心、具創意且擅長互動，適合擔任「作者」負責實作計畫（PL）；Codex 穩健、無聊但極少出錯，特別擅長處理複雜的後端邏輯，適合作為「審稿人」守最後一道關。
- **追求「共識」而非「輪數」**：傳統設死輪數（如固定三輪）會導致 AI 為結案而敷衍。真正的系統應要求兩邊模型達成共識，若未解決爭議則不准收工。
- **維持對話上下文的收斂性**：在同一個對話 Session 中進行 Review 才能讓 AI「記得」上一輪的討論，從而向共識收斂，避免每一輪都重開新對話導致過度設計。

## 關鍵細節與數據
- **系統組件（The Harness）**：作者（Author）= Claude；守衛（Gatekeeper）= `stopHook`（Claude Code 內部機制，每當 Claude 準備交還控制權給用戶時觸發）；審核標記（Marker）= 一段特定文字暗號（如寫在檔案結尾的 marker），代表審核通過。
- **自動化流程五步驟**：
  1. Claude 寫完實作計畫（PL）並嘗試結束對話
  2. 觸發 `stopHook` 掃描檔案尾端是否有 Marker
  3. 若無 Marker，`stopHook` 攔截對話，並發送預設指令啟動 `codex review skill`
  4. Claude 調用 `codex-cli` 工具請 Codex 審核，雙方進行多輪攻防（修改或反駁）
  5. 達成共識後，Claude 在檔案末尾蓋上 Marker，`stopHook` 識別後正式放行
- **實測經驗**：手動複製貼上的「人肉橋樑」模式會成為多線並行開發（Worktree）時的生產力瓶頸；導入自動化系統後，程式碼架構更乾淨，技術債減少，後續修復 Bug 的頻率大幅降低；系統性攔截可解決約 80% 的重要問題。

## 值得引用的金句
- 「人的紀律是靠不住的，所以與其逼自己每次都記得，不如把這件事直接做成系統。」
- 「審核通過的章……你身為老闆從頭到尾只會看到最後那份定稿，中間那些吵架修改的過程，你完全不用管。」
- 「與其祈禱 AI 不要出錯，不如動手建一個讓他可以出錯，但這個錯誤會被 Harness 攔截的環境。」

## 與其他 AI 工具/概念的關聯
- **Vibe Coding**：在 AI 賦權的開發時代，此互審系統是確保產出品質的核心配套。
- **Harness Engineering**：指包在 AI Agent 外層的完整工作環境（包含限制、流程與工具），是提升 Agent 效能的關鍵，而非僅依賴提示詞。
- **Claude Code 的 Skill 機制**：透過封裝特定的 review skill，讓 Claude 具備調用外部模型（Codex）的能力。
- **Agentic Workflow**：將單次的指令式操作（Prompt）演進為具備自動攔截、審核與反思（Reflect）的閉環循環。
