---
type: source
tags: [ai, claude-code, skill, tdd, software-design]
created: 2026-07-25
source_url: https://www.youtube.com/watch?v=aR97E7aKEgg
source_date: 2026-07-25
source_type: transcript
---

# 700 萬人下載的 /grill-me：Matt Pocock 的極簡 Skill 工作流拆解

> 來源：[原始檔](../../raw/transcripts/2026-07-25_grill_me_matt_pocock.md) · [[Gary_Chen]]

## 一句話摘要
[[Matt_Pocock]] 把深厚軟體工程底蘊（TDD、深模組架構）轉化為極簡模組化 Skill（GitHub 16 萬星、700 萬次下載），示範如何把隨機的 AI 黑盒子馴化為有大局觀的工程師。

## 核心論點
- **控制 AI 的隨機性**：開發的核心挑戰是穩定控制 AI，不是產碼速度
- **極簡模組化優於重型框架**：對比 Superpowers「保姆級」寫死九步驟，MPO 的 Skill 是隨插即用的樂高積木，適合理解力強的現代模型——佐證 [[Skill_輕量化]]
- **奪回決策主權**：`/grill-me` 強制 AI 反向拷問人類，防止把幾百個微觀決定外包給黑盒子（反制 [[Vibe_Coding]]）
- **TDD 防 AI 作弊**：先寫測試再寫功能；順序顛倒時 AI 會生成「保證通過的假測試」交差
- **深模組對抗邏輯碎片化**：AI 缺大局觀易寫「淺模組」；要重構出簡單門戶、隱藏細節的 [[深模組|Deep Modules]]（briefing 中「生模組」為語音誤植，推測）

## Skill 清單（開發管線順序）
`/grill-me`（拷問需求）→ `/spec`（規格書，嚴禁寫入程式碼）→ `/2-tickets`（按使用者功能拆票，非技術架構）→ `/implement`（TDD 實作）→ `/code-review`（乾淨 session 審查）→ `/improve-case-architecture`（架構大掃除、殘酷刪除測試）；另有進化版 `/grill-with-docs`（自動記錄專有名詞與決策）

## /grill-me 五行 Prompt 要義
1. 未達共識前把我往死裡問
2. 像畫心智圖般追每個決定的連鎖反應
3. 每次只問一個問題
4. 必須附建議答案
5. 共識前絕不准偷跑寫程式

## 其他細節
- Code review 用《重構》12 種壞味道診斷：Shotgun Surgery、Feature Envy、Data Clumps
- Prompt 壓縮三原則：修剪（Pruning）、指引詞（Indexing，用術語如 `data clumps` 壓縮資訊）、完成標準（Completion）

## 值得引用的段落
> 「寫程式的本質是連續做出幾百個微觀的決定……把模糊的想法直接丟給 AI 憑感覺做，你其實是把這幾百個決定的決策權外包給 AI 這個黑盒子。」

> 「只有成為專業領域的專家，你才能真正控制好 AI。」

## 連結到的 wiki
- [[Matt_Pocock]] · [[Gary_Chen]]
- [[Skill_輕量化]]（樂高式 vs 重型框架，同一結論的第二來源）
- [[Vibe_Coding]] · [[理解成本]]
- [[Claude_Code]] · [[深模組]]（stub）

## 我的問題 / 待追蹤
- MPO 專案的實際 GitHub repo 名稱？（影片僅稱 /grill-me 系列，待查證）
- `/grill-me` 五行 prompt 可否直接移植到本專案的 plan 流程？
