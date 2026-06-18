---
type: source
tags: [ai, claude-code, codex, tool-agnosticism]
created: 2026-06-19
source_url: https://www.youtube.com/watch?v=DmkKxzdRUAc
source_date: 2026-06-19
source_type: transcript
---

# Claude Code 轉 Codex：五分鐘無痛轉移整個專案

> 來源：[原始檔](../../raw/transcripts/2026-06-19_claude_code轉codex.md) · 頻道：JayLuxAI | AI 自動化（Jay）

## 一句話摘要
把 [[Claude_Code]] 的專案邏輯、Skills 與 Agents 快速同步到 [[OpenAI_Codex|Codex]]，打造不被單一 AI 工具鎖定的「智能開發系統」——即 [[工具無關性]]（Tool Agnosticism）。

## 核心論點
- **工具無關性**：要建的是任何 AI 都能讀的「智能系統」，而非綁定單一工具的專案
- **專案大腦共享**：docs / reference / context 資料夾通用，轉移時不需重建，只補對應工具的介面檔
- **雙引擎策略**：日常任務、風格模仿、快速 Debug 給 Claude Code；複雜 App / 後端邏輯、卡關任務給 Codex
- **推理強度可調**：Codex 提供 Low / Medium / High 三檔，對難題深度思考

## 值得引用的段落
> 「你建的不是一個 Claude 的專案，你建的是一個可以被任何 AI 工具讀取的智能系統。」
> 「最重要的觀念，就是不要鎖死在一個工具裡面。」

## 關鍵技術細節
- 轉移實測約 **2 分 50 秒**；切換後卡關問題可能 **10 分鐘內**解決
- **Skills** 格式兩邊相同可直接複製；**Agents**：Claude Code 用 `.md`、Codex 用 `.toml`，轉移時建 `.agent` 資料夾
- Codex 內輸入 `/` 呼叫所有 Skill；在 `CLAUDE.md` / `agent.md` 設規則讓兩套工具同步
- Codex 可在 **VS Code / Antigravity / Cursor** 透過 Extension 使用

## 連結到的 wiki
- [[Claude_Code]] · [[OpenAI_Codex]] · [[工具無關性]] · [[Agentic_Workflow]]

## 我的問題 / 待追蹤
- `.agent` 資料夾與 Codex `.toml` 的實際 schema 細節？
