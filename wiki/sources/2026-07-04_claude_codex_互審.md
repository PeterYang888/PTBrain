---
type: source
tags: [ai, claude-code, codex, harness-engineering, workflow]
created: 2026-07-04
source_url: https://www.youtube.com/watch?v=xzrvAERmvRk
source_date: 2026-07-04
source_type: transcript
---

# 讓 Claude 跟 Codex 自動互審：個人 Harness 最小實踐

> 來源：[原始檔](../../raw/transcripts/2026-07-04_claude_codex_互審.md) · 主講：Gary Chen

## 一句話摘要
在 [[Claude_Code]] 中用 `stopHook` 攔截結束流程，強制 Claude 與 [[OpenAI_Codex|Codex]] 互審直到達成共識才放行，用系統取代人為紀律解決 AI 編程 Bug。

## 核心論點
- **打破自我檢查盲點**：引入第三方模型（Codex）用不同權重審核，抓原模型看不到的邊界情況
- **系統勝過人為紀律**：把審核做成系統，不依賴人記得要做
- **天才與門衛分工**：Claude = 作者（實作計畫 PL），Codex = 審稿人（把最後一關）
- **追求共識而非輪數**：不設死輪數，未解決爭議不准收工
- **同一 Session 收斂**：在同一對話中 review 才能讓 AI「記得」上一輪討論

## 自動化流程（Harness 五步驟）
1. Claude 寫完實作計畫（PL）並嘗試結束對話
2. `stopHook` 掃描檔案尾端是否有 Marker（審核通過暗號）
3. 無 Marker → `stopHook` 攔截，發送指令啟動 `codex review skill`
4. Claude 調用 `codex-cli` 請 Codex 審核，雙方多輪攻防
5. 達成共識 → Claude 蓋上 Marker，`stopHook` 放行

## 值得引用的段落
> 「人的紀律是靠不住的，所以與其逼自己每次都記得，不如把這件事直接做成系統。」
> 「與其祈禱 AI 不要出錯，不如動手建一個讓他可以出錯，但這個錯誤會被 Harness 攔截的環境。」

## 連結到的 wiki
- [[Harness_Engineering]] · [[Claude_Code]] · [[OpenAI_Codex]] · [[Agentic_Workflow]] · [[Gary_Chen]]

## 我的問題 / 待追蹤
- `codex review skill` 是否為 Gary Chen 自製、可公開取用的 skill？
