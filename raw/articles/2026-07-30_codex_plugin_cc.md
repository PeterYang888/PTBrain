---
type: source
tags: [ai, claude-code, codex, plugin]
created: 2026-07-30
updated: 2026-07-30
source_url: https://github.com/openai/codex-plugin-cc
source_date: 2026-07-30
source_type: article
source_extra:
  platform: github
  processed_by: WebFetch
---

## 核心功能
OpenAI 官方發布的 Claude Code 外掛，讓使用者能在 Claude Code 工作流程中直接呼叫 Codex：
- **程式碼審查**：`/codex:review` 標準審查、`/codex:adversarial-review` 挑戰性設計審查
- **任務委派**：`/codex:rescue` 把除蟲/修復/繼續任務交給 Codex 處理
- **工作管理**：`/codex:status`、`/codex:result`、`/codex:cancel` 追蹤背景工作
- **會話轉移**：`/codex:transfer` 把 Claude Code 對話轉移到 Codex

## 安裝方式
```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```
需求：Node.js 18.18+、ChatGPT 訂閱或 OpenAI API 密鑰

## 指令範例
```
/codex:review --base main
/codex:adversarial-review --background
/codex:rescue investigate why the tests started failing
```

## 配置方式
`.codex/config.toml`：
```
model = "gpt-5.4-mini"
model_reasoning_effort = "high"
```

## 整合特點
外掛使用本機 Codex CLI，共享相同的認證、配置和環境設定。
