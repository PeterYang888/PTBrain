# PROGRESS

## 目前狀態
- 最後更新：2026-07-25 08:38
- 目前焦點：ingest inbox 2026-07-25 批次（3 支 ai-tooling）已全數完成並同步 index/log/inbox，待 commit

## 已完成
- [x] ingest 2026-07-25 批次 3 支 ai-tooling 影片 — raw/transcripts/ 新增 3 檔、wiki/sources/ 新增 3 頁；新建 [[Matt_Pocock]]、[[Corey_McClain]]、[[示範式自動化]]；更新 [[Claude_Cowork]]（stub 補實）、[[RPA]]、[[Skill_輕量化]]、[[Vibe_Coding]]、[[Gary_Chen]]、[[Google]]、[[2026-07-18_codex_record_replay_fork]]（待追蹤回填）；index.md（86/47/59）、log.md、inbox.md 已同步
- [x] ingest 2026-07-18 批次 7 支 ai-tooling 影片（NotebookLM 繁中 briefing）— raw/transcripts/ 新增 7 檔、wiki/sources/ 新增 7 頁；新建 concepts `Agentic_Engineering`、`Skill_輕量化`、`Git_版本控制` 與 entities `Grok_4.5`、`Jay_JayLuxAI`、`李廠長`；更新 `NotebookLM`、`OpenAI_Codex`、`Harness_Engineering`、`Context_工程`、`Vibe_Coding`、`AIOS`、`xAI`、`Claude_Fable_5`、`黃一河`、`Gary_Chen`；index.md（統計 83 sources／46 entities／58 concepts）、log.md（append 一筆）、inbox.md（7 筆移入已處理）
- [x]（前次）ingest「多 AI Deep Research → Claude 裁決 Prompt 組」＋ raw 檔正名歸位（詳見 log.md 2026-07-16）

## 進行中
- （無）

## 待辦（依優先序）
1. competitor-intel「Treasures of Aztec — PG Soft 大獎實錄」（W-5vaMiUlKQ）ingest 失敗待重試（見 D-004）
2. ingest `raw/notes/2026-07-16_GitEasyLearning.md`（使用者手寫筆記，與 `Git_版本控制` concept 主題重疊，屆時合併觀點）

## 重要決策與假設（D-001 起編號，永不刪除）
- D-001：inbox「待處理」為空時，`ingest` 指令的對象是 raw/ 中未 ingest 的新檔案（本次即 `00_brief_多AI研究裁決.md`；另兩篇 raw 根目錄文章已有對應 source 頁）
- D-002：三家 AI 的 deep research 定位（Gemini 廣度／ChatGPT 深挖／Grok 社群）寫入 entity 頁時標註「使用者定位」，因其出處是使用者自寫筆記而非外部驗證事實
- D-003：stub link 保留未建頁：[[Pragmatic_Play]]、[[Gates_of_Olympus]]（僅範例提及，依 CLAUDE.md 3.1 不急著建頁）
- D-004：W-5vaMiUlKQ 加入 NotebookLM 兩次皆回報「API returned no data」，判定為來源端問題（可能無字幕或影片受限），依 inbox prompt 失敗規則標註 ❌ 並保留在待處理區，不中斷整批
- D-005：Grok 4.5 影片口述的 benchmark 名稱與數字（SWE Bench Pro 60.7 等）語意混亂，僅寫入 source 頁並標「依來源說法、待查證」，不寫入 entity 頁當事實
- D-006：Jay（JayLuxAI）與 2026-06-12 AIOS 4Cs 影片主講者可能同一人（框架同構），entity 頁標「待確認」，未合併來源

## 已知問題 / 風險
- [[多AI研究裁決]] 工作流尚無實跑驗證；首次 run 後應回填效果評估到 source 頁「待追蹤」
- `research-runs/` 資料夾尚未建立（筆記建議的實跑檔案佈局），首次實跑時再建
- `raw/transcripts/tmp_briefings/` 目錄仍存在（2026-06-19 lint 清過 tmp_ 檔，此目錄殘留），下次 lint 時確認可否清除
- [[ai自動化os_三家比較]] synthesis 可能需擴充：Grok 4.5 入局後 agentic 編程成三強格局

## 下次接續點
- 本批已完成，建議 commit（訊息慣例：`ingest: 2026-07-25 批次 3 支影片（ai-tooling）`）
- 注意：inbox.md 待處理區已不見 W-5vaMiUlKQ 失敗件（與待辦 1 的描述不一致，重試時以 notebook 直加路徑為準）
- 待使用者裁決的建議：是否做「AI 簡報生成工具比較」synthesis（Codex／NotebookLM／Gemini in Slides 三路線 source 已齊，見 [[2026-07-25_gemini_slides_簡報]] 待追蹤）
- 若有新 ingest：先查 `inbox.md` 待處理區，再查 `raw/` untracked 檔案（`git status --short raw/`）
- 失敗件重試路徑：`notebooklm source add "https://www.youtube.com/watch?v=W-5vaMiUlKQ" -n c8bcfd26`（competitor-intel notebook）；若仍失敗，改走手動逐字稿或跳過
- 若實跑多 AI 研究：從 `raw/notes/2026-07-16_多ai研究裁決_prompt組.md` 取 prompt，產出存 `research-runs/<日期_主題>/`，裁決結果可考慮歸檔為 synthesis
