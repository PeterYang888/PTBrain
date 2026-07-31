# PROGRESS

## 目前狀態
- 最後更新：2026-08-01
- 目前焦點：LLM 原理頁群 lint 完成並建立 [[LLM_原理]] 樞紐頁，尚未 commit（ingest 批次已於 af4a03a commit）

## 已完成
- [x] lint LLM 底層原理頁群（22 concept ＋ 8 source）— 新建 topic 樞紐頁 [[LLM_原理]]（四層階梯／路線之爭／四位主講者理解階梯／缺口清單，38 個連結零斷鏈）；修 [[World_Models]] 斷鏈 3 處 → [[世界模型]]；[[Transformer]]、[[神經網路]] 加回連；index.md（Topics 4）、log.md 已同步
- [x] ingest 2026-08-01 批次 2 支 ai-tooling 影片（AI 原理類）— raw/transcripts/ 新增 2 檔、wiki/sources/ 新增 2 頁；新建 entities [[大飛]]、[[王木頭]]，新建 concepts [[Transformer]]、[[注意力機制]]、[[位置編碼]]、[[MoE]]、[[萬能逼近定理]]、[[激活函數]]；更新 [[神經網路]]、[[反向傳播]]、[[梯度下降]]、[[2026-07-10_神經網路_漫士科普]]；index.md（實測 88/49/65）、log.md、inbox.md 已同步
- [x] 修復 NotebookLM CLI 認證失效 — 根因為版本落後（Python312 環境 0.3.4 → 0.7.3），非 cookie 問題
- [x] ingest 2026-07-25 批次 3 支 ai-tooling 影片 — raw/transcripts/ 新增 3 檔、wiki/sources/ 新增 3 頁；新建 [[Matt_Pocock]]、[[Corey_McClain]]、[[示範式自動化]]；更新 [[Claude_Cowork]]（stub 補實）、[[RPA]]、[[Skill_輕量化]]、[[Vibe_Coding]]、[[Gary_Chen]]、[[Google]]、[[2026-07-18_codex_record_replay_fork]]（待追蹤回填）；index.md（86/47/59）、log.md、inbox.md 已同步
- [x] ingest 2026-07-18 批次 7 支 ai-tooling 影片（NotebookLM 繁中 briefing）— raw/transcripts/ 新增 7 檔、wiki/sources/ 新增 7 頁；新建 concepts `Agentic_Engineering`、`Skill_輕量化`、`Git_版本控制` 與 entities `Grok_4.5`、`Jay_JayLuxAI`、`李廠長`；更新 `NotebookLM`、`OpenAI_Codex`、`Harness_Engineering`、`Context_工程`、`Vibe_Coding`、`AIOS`、`xAI`、`Claude_Fable_5`、`黃一河`、`Gary_Chen`；index.md（統計 83 sources／46 entities／58 concepts）、log.md（append 一筆）、inbox.md（7 筆移入已處理）
- [x]（前次）ingest「多 AI Deep Research → Claude 裁決 Prompt 組」＋ raw 檔正名歸位（詳見 log.md 2026-07-16）

## 進行中
- （無）

## 待辦（依優先序）
1. commit 本輪 lint 產出（[[LLM_原理]] 樞紐頁 ＋ 斷鏈修復 ＋ index/log）
2. 兩處敘述小修（使用者本輪未選，隨時可做）：[[Transformer]] 頁「靠後續 RLHF 等對齊階段」把三階段壓成兩階段，應改為明確的預訓練→SFT→RL；[[2026-05-16_stanford_diffusion_lecture4]] 的 [[潛在空間]] stub 可指向 [[VAE]]
3. 補 [[LLM_原理]] 標記的六個缺口頁（依重要性）：Tokenization、預訓練、前饋網路 FFN、SFT、Scaling_Laws、Context_Window
4. competitor-intel「Treasures of Aztec — PG Soft 大獎實錄」（W-5vaMiUlKQ）ingest 失敗待重試（見 D-004）
5. ingest `raw/notes/2026-07-16_GitEasyLearning.md`（使用者手寫筆記，與 `Git_版本控制` concept 主題重疊，屆時合併觀點）

## 重要決策與假設（D-001 起編號，永不刪除）
- D-001：inbox「待處理」為空時，`ingest` 指令的對象是 raw/ 中未 ingest 的新檔案（本次即 `00_brief_多AI研究裁決.md`；另兩篇 raw 根目錄文章已有對應 source 頁）
- D-002：三家 AI 的 deep research 定位（Gemini 廣度／ChatGPT 深挖／Grok 社群）寫入 entity 頁時標註「使用者定位」，因其出處是使用者自寫筆記而非外部驗證事實
- D-003：stub link 保留未建頁：[[Pragmatic_Play]]、[[Gates_of_Olympus]]（僅範例提及，依 CLAUDE.md 3.1 不急著建頁）
- D-004：W-5vaMiUlKQ 加入 NotebookLM 兩次皆回報「API returned no data」，判定為來源端問題（可能無字幕或影片受限），依 inbox prompt 失敗規則標註 ❌ 並保留在待處理區，不中斷整批
- D-005：Grok 4.5 影片口述的 benchmark 名稱與數字（SWE Bench Pro 60.7 等）語意混亂，僅寫入 source 頁並標「依來源說法、待查證」，不寫入 entity 頁當事實
- D-006：Jay（JayLuxAI）與 2026-06-12 AIOS 4Cs 影片主講者可能同一人（框架同構），entity 頁標「待確認」，未合併來源
- D-007：inbox 的 notebook 標記只決定「進哪個 NotebookLM notebook」，不硬套 `_meta/inbox_ingest_prompt.md` 表格的預設 tags。2026-08-01 兩支標記為 ai-tooling 但內容是 AI 原理，tags 依實際內容填（`[ai, llm, transformer, attention, 科普]` / `[ai, neural-network, deep-learning, 科普]`），與既有 [[2026-07-10_神經網路_漫士科普]] 對齊
- D-008：notebooklm CLI 報 `Authentication expired` 時，先查 `notebooklm --version` 與 PyPI 最新版，再懷疑 cookie。2026-08-01 該錯誤的真因是版本落後（0.3.4 vs 0.7.3）＋Google 網域改為 `notebook.google.com`；重跑 login 無效，升級後即通
- D-010：topic 頁的定位＝**導航樞紐＋缺口台帳**，不重複 concept 頁內容。[[LLM_原理]] 只放層次關係、跨頁交叉驗證（如王木頭／漫士獨立提出同一梯度下降比喻）與「已知缺口」清單；細節一律留在各 concept 頁
- D-011：wiki-link 一律使用**頁面實際檔名**，不用同義英文別名。[[World_Models]] 斷鏈即因概念頁名為中文 `世界模型` 但 3 處連英文名；lint 時應掃描斷鏈而非只看內容矛盾
- D-009：這台機器有兩套 Python（PATH 上 `pip` 屬 Python314，但 `notebooklm` 執行檔屬 Python312）。升級 notebooklm-py 必須指定 `/c/Users/user/AppData/Local/Programs/Python/Python312/python -m pip install -U notebooklm-py`，直接下 `pip install` 會裝到錯的環境

## 已知問題 / 風險
- [[多AI研究裁決]] 工作流尚無實跑驗證；首次 run 後應回填效果評估到 source 頁「待追蹤」
- `research-runs/` 資料夾尚未建立（筆記建議的實跑檔案佈局），首次實跑時再建
- `raw/transcripts/tmp_briefings/` 目錄仍存在（2026-06-19 lint 清過 tmp_ 檔，此目錄殘留），下次 lint 時確認可否清除
- [[ai自動化os_三家比較]] synthesis 可能需擴充：Grok 4.5 入局後 agentic 編程成三強格局

## 下次接續點
- 工作區有未提交的 lint 產出：`wiki/topics/LLM_原理.md`（新）、[[JEPA]]／[[Yann_LeCun]]／[[2026-05-16_ai教父_agi內幕]]（斷鏈修復）、[[Transformer]]／[[神經網路]]（回連）、index.md、log.md、PROGRESS.md
- 斷鏈掃描腳本可重用（本輪 inline 執行）：掃 `wiki/**/*.md` 的 `[[連結]]` 比對檔案 stem，能同時查斷鏈、孤立頁、inbound 數；建議每次 lint 先跑它再讀內容
- ingest 批次已 commit 於 af4a03a
- 新版 CLI（0.7.3）差異：`-n` 取代 `--notebook`；新增 `--prompt-file`（長 prompt 免跳脫，本批已改用）
- CLI 輸出有 rich 終端硬換行，raw 檔需經 unwrap 才可用；本批腳本存於 scratchpad `make_raw.py`，下批可重用（規則：結構行另起、標題後另起、非雙 CJK 交界補空格）
- 可考慮的 synthesis：三支 AI 原理科普（[[漫士]]／[[王木頭]]／[[大飛]]）涵蓋層次互補，可做「神經網路到 LLM 的理解階梯」對照頁
- 注意：inbox.md 待處理區已不見 W-5vaMiUlKQ 失敗件（與待辦 1 的描述不一致，重試時以 notebook 直加路徑為準）
- 待使用者裁決的建議：是否做「AI 簡報生成工具比較」synthesis（Codex／NotebookLM／Gemini in Slides 三路線 source 已齊，見 [[2026-07-25_gemini_slides_簡報]] 待追蹤）
- 若有新 ingest：先查 `inbox.md` 待處理區，再查 `raw/` untracked 檔案（`git status --short raw/`）
- 失敗件重試路徑：`notebooklm source add "https://www.youtube.com/watch?v=W-5vaMiUlKQ" -n c8bcfd26`（competitor-intel notebook）；若仍失敗，改走手動逐字稿或跳過
- 若實跑多 AI 研究：從 `raw/notes/2026-07-16_多ai研究裁決_prompt組.md` 取 prompt，產出存 `research-runs/<日期_主題>/`，裁決結果可考慮歸檔為 synthesis
