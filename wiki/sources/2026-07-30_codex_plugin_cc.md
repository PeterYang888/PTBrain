---
type: source
tags: [ai, claude-code, codex, plugin]
created: 2026-08-22
source_url: https://github.com/openai/codex-plugin-cc
source_date: 2026-07-30
source_type: article
---

# openai/codex-plugin-cc：官方 Claude Code ↔ Codex 外掛

> 來源：[原始檔](../../raw/articles/2026-07-30_codex_plugin_cc.md)

## 一句話摘要
OpenAI 官方發布的 [[Claude_Code]] 外掛，讓使用者在 Claude Code 裡直接用斜線指令呼叫 [[OpenAI_Codex]] 做程式碼審查、任務委派與會話轉移。

## 核心論點
- 提供 `/codex:review`（標準審查）、`/codex:adversarial-review`（挑戰性設計審查）、`/codex:rescue`（除蟲/修復委派）、`/codex:transfer`（會話轉移到 Codex）等斜線指令
- 外掛使用本機 Codex CLI，共享同一份認證/配置/環境設定，不是獨立的整合層
- 這是**官方提供**的 Claude↔Codex 互審方案，跟 [[Gary_Chen]] 自己用 `stopHook` 手刻的互審 Harness（見 [[2026-07-04_claude_codex_互審]]）是同一個問題的兩種解法——一個是官方外掛，一個是個人 DIY

## 關鍵細節與數據
- 安裝：`/plugin marketplace add openai/codex-plugin-cc` → `/plugin install codex@openai-codex` → `/reload-plugins` → `/codex:setup`
- 需求：Node.js 18.18+、ChatGPT 訂閱或 OpenAI API 金鑰
- 設定檔 `.codex/config.toml` 可指定 `model` 與 `model_reasoning_effort`

## 連結到的 wiki
- [[Claude_Code]]、[[OpenAI_Codex]] — 已更新此工具
- [[Gary_Chen]]、[[2026-07-04_claude_codex_互審]] — 對照的 DIY 互審方案
