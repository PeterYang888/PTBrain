---
type: source
tags: [ai, claude-code, workflow, dynamic-workflows, javascript]
created: 2026-06-06
source_url: https://www.youtube.com/watch?v=pI-AX98dlvY
source_date: 2026-06-06
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# 11 天寫 75 萬行程式碼！Claude Code Dynamic Workflows 動態工作流完整實測

> 來源：[原始檔](../../raw/transcripts/2026-06-06_11天_claude_code_dynamic_workflows.md) · [[Claude_Code]]

## 一句話摘要
Dynamic Workflows 用 JavaScript 腳本取代 Prompt 驅動 agent 協作，讓主 context window 只存最終結果，實現 16 個 agent 並行、11 天完成 75 萬行 C++ → Rust 遷移。

## 核心論點
- **JS 取代 MD**：傳統 Agent Team 用自然語言協調；Dynamic Workflows 把中間步驟封裝進 JS 變數，主上下文只收濃縮結果，大幅節省 Token
- **三種觸發方式**：`deep-search`（內建腳本）、`workflow` 關鍵字（生成可重用 JS 檔）、Ultra Code 模式（自動撰寫並執行）
- **/workflows 監控**：`wf` 或 `/workflows` 查看進度；按 `s` 存成 JS 檔可跨 session 重用
- **成本警告**：極端情況下一次 session 可能耗盡 $200 額度，建議先用 Medium / Low 模型測試

## 值得引用的段落
> 「它把 Prompt 從 Context 搬進了程式碼裡面……你的上下文視窗自然就可以變得很大，所以可以調用非常多個 Sub-agent 下去工作。」

## 連結到的 wiki
- [[Claude_Code]]
- [[Dynamic_Workflows]]
- [[Agentic_Workflow]]
- [[Vibe_Coding]]

## 我的問題 / 待追蹤
- 目前最多 16 個並行 agent，限制因素是什麼？
- JS 腳本可手動撰寫到什麼複雜度？
