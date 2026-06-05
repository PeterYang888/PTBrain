---
type: source
tags: [ai, claude-code, workflow, dynamic-workflows, javascript]
created: 2026-06-06
source_url: https://www.youtube.com/watch?v=GHWckrzW-jc
source_date: 2026-06-06
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# Claude Code 同時跑 1000 個 agent：Dynamic Workflows

> 來源：[原始檔](../../raw/transcripts/2026-06-06_claude_code_1000_agent_dynamic_workflows.md) · [[Claude_Code]]

## 一句話摘要
Dynamic Workflows Research Preview：JS 腳本把 agent 編排從 context window 搬到外部執行環境，支援最高 16 並行 / 1000 總量，Bun Runtime 案例 11 天完成 75 萬行 Zig → Rust 遷移、測試通過率 99.8%。

## 核心論點
- **架構轉移**：傳統方式超過 10 個 agent 就進入「愚蠢區（Dumb Zone）」；Dynamic Workflows 把狀態存到 JS 變數，agent 數再多也不污染主 context
- **對抗式驗證**：生成組 Agent + 反駁組 Agent 反覆交鋒（類似 GAN），直到無漏洞才輸出——這是 99.8% 測試通過率的關鍵
- **規格**：16 並行 / 1000 總量；適合耗時 >30 分鐘的任務；CLI 需 V2.1.154+
- **Ultra Code 模式**：自動判斷是否需動員大規模編排，適合下班前啟動、隔日查看結果
- **成本**：500 agent 任務可能是一般 session 的 10 倍費用；Enterprise 需管理員啟用

## 值得引用的段落
> 「Dynamic Workflows 讓 Claude Code 第一次能同時跑成千上百個 Agent……這不是隨便的升級，是把 Agent 編排這件事從根本翻轉。」

> 「Bun 的案例證明，這套機制能把三個月的工作變三天，三年的工作變三週。它改變的是軟體工程的時間尺度。」

## 連結到的 wiki
- [[Claude_Code]]
- [[Dynamic_Workflows]]
- [[Agentic_Workflow]]

## 我的問題 / 待追蹤
- 第一支影片說「C++ → Rust」，這支說「Zig → Rust」——Bun 主要用 Zig，這支更準確
- Enterprise 手動啟用的入口在哪？
