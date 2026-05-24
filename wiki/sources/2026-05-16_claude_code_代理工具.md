---
type: source
tags: [Claude_Code, 開源, 代理工具, NVIDIA, GitHub]
created: 2026-05-16
source_url: https://www.youtube.com/watch?v=TlLx4Iy6n2Q
source_date: 2026-05-16
source_type: transcript
---

# Free Claude Code：GitHub 萬星開源 Claude Code 代理工具

> 來源：[原始檔](../../raw/transcripts/2026-05-16_claude_code_代理工具.md)

## 一句話摘要
Free Claude Code 是 GitHub 萬星開源工具，用本地 HTTP 代理「偷梁換柱」，讓 Claude Code 前端接 NVIDIA NIM 等免費模型後端，API 費用降至零。

## 核心論點
- 架構：本地代理服務器攔截 Claude Code 的 Anthropic API 請求，轉譯成 OpenAI 兼容格式轉發至免費模型
- 支援 NVIDIA NIM（推薦，完全免費，每分鐘 4 次請求）、OpenRouter、本地 Ollama 等
- 智能優化：過濾簡單請求（目錄查詢等）在本地直接返回，保留 quota 給複雜編程任務
- 支援 Discord/Telegram 機器人遠程控制 Claude Code

## 值得引用的段落
> 「這套精妙的代理機制，把世界上最貴的模型客戶端和最便宜的免費模型後端接在了一起。」

## 連結到的 wiki
- [[Claude_Code]]
- [[Anthropic]]
- [[Anthropic_Claude_生態]]

## 我的問題 / 待追蹤
- 使用 NVIDIA NIM 免費模型，在複雜編程任務上品質與 Claude Sonnet 差距多大？
- 這類工具是否違反 Anthropic ToS？
