---
type: source
tags: [ai, claude, skill, workflow, automation]
created: 2026-07-25
source_url: https://www.youtube.com/watch?v=YjXxQ85_PUg
source_date: 2026-07-25
source_type: transcript
---

# Claude「Record a Skill」：2 分鐘錄一個 Skill

> 來源：[原始檔](../../raw/transcripts/2026-07-25_claude_record_a_skill.md) · [[Corey_McClain]]

## 一句話摘要
[[Anthropic]] 在 [[Claude_Cowork|co-work]] 模式推出「record a skill」：錄下螢幕操作與語音說明，Claude 觀察學習後把整段工作流固化為可重複執行的 Skill。

## 核心論點
- **示範即自動化**：Claude 直接觀察使用者操作行為（螢幕截圖 + 語音敘述），之後可精確重複該任務——見 [[示範式自動化]]
- **降低自動化門檻**：不用寫程式碼或 prompt，像平常一樣操作一遍即可
- **Skill 化保存**：錄完存為 Skill，成為 Agent 能力庫的一部分，後續可自動調用

## 關鍵操作細節
- **模式要求**：對話框需為 `co-work` 模式；`chat` 模式看不到錄製選項
- **路徑**：`+`（plus button）→ `record a skill` → 選麥克風 → 開始錄；出錯可 `discard` 重錄
- **實測範例**：「前往 YouTube Studio 下載最新數據」全程錄製僅 57 秒
- **最佳實踐**：錄前關閉無關分頁、先預演一兩次、在安靜環境錄（語音說明要清晰）

## 值得引用的段落
> 「Claude watches and learns how to do the work exactly like you and then it can repeat that task for you whenever you wanted to.」

## 連結到的 wiki
- [[Claude_Cowork]]（co-work 模式的首個深入 source）
- [[示範式自動化]] · [[RPA]]
- [[Skill_輕量化]]（錄製是 Skill 產生方式的新入口）
- [[2026-07-18_codex_record_replay_fork]]（[[OpenAI_Codex]] 的對應功能 Record & Replay）

## 我的問題 / 待追蹤
- 錄出來的 Skill 是否可編輯 / 匯出？與 Claude Code 的 skill 檔案格式是否互通？
- co-work 模式的完整能力邊界（桌面 app 限定？）
