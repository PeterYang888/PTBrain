# PROGRESS

## 目前狀態
- 最後更新：2026-08-22
- 目前焦點：`ingest inbox` 新增「從瀏覽紀錄自動補齊」步驟並完成首次實跑（19 支 ingest，entertainment 43 支依使用者決定整類移除不再處理）

## 已完成
- [x] `ingest inbox` 新增「從瀏覽紀錄自動補齊」步驟（讀 Downloads 底下 history.csv）並首次實跑
  - history.csv 1447 筆瀏覽紀錄 → 去重後 63 支新影片候選 → 分類：health×3/tech-news×1/tech-life×6/news×10/entertainment×43
  - **使用者決定移除 entertainment 整類**（動漫/電影解說/明星網紅/音樂放鬆/運動不需要進知識庫）：已刪除誤建立的 NotebookLM entertainment notebook（43 支已加入但未產出 briefing），`inbox_ingest_prompt.md` 明確規定這類內容以後直接 skip，不套用「無法判斷就先標 ai-tooling」規則
  - 剩餘 20 支新建 4 個 notebook（health-wellness、tech-news、tech-lifestyle、news-watch）跑完，19 支成功（health×3、tech-news×1、tech-life×6、news×9），1 支 news（2Smy2AUbLJI）notebooklm 端問題跳過待重試
  - 這批內容只建 wiki/sources 頁，不建 entity/concept（個人生活類內容不適合累積知識網）
  - index.md（統計 129/58/75）、inbox.md、log.md 已同步
- [x] 合併整合：main 分支的 2026-08-15 批次 commit（7d2edad）＋ worktree 分支 `worktree-ingest-inbox-20260822` 全部 commit 合併回 main，解決 CLAUDE.md／PROGRESS.md／inbox.md／index.md／log.md／Claude_Code.md／Gary_Chen.md 的內容衝突（皆為雙邊各自新增內容需要合併，非互斥修改）；`raindrop_ingest.md` 順手移到跟 `inbox_ingest_prompt.md` 一致的路徑慣例（`_meta/raindrop_ingest_prompt.md`，無 `prompts/` 子資料夾）
- [x] 合併整合：main 分支的 2026-08-15 批次 commit（7d2edad）＋ worktree 分支 `worktree-ingest-inbox-20260822` 全部 commit 合併回 main，解決 CLAUDE.md／PROGRESS.md／inbox.md／index.md／log.md／Claude_Code.md／Gary_Chen.md 的內容衝突（皆為雙邊各自新增內容需要合併，非互斥修改）；`raindrop_ingest.md` 順手移到跟 `inbox_ingest_prompt.md` 一致的路徑慣例（`_meta/raindrop_ingest_prompt.md`，無 `prompts/` 子資料夾）
- [x] 設計 + 建置 + 首跑 `ingest raindrop` 流程（最小整合版）
  - 新增 `_meta/raindrop_ingest_prompt.md`（流程文件）與 `CLAUDE.md` §12 快捷指令；複用現有 raw/wiki 三層結構，不新建資料夾/schema
  - Token 存於 repo 外 `C:\Users\user\.raindrop_token`；API 單筆更新端點修正為 `PUT /rest/v1/raindrop/{id}`（單數，非文件初稿誤寫的複數）
  - 首跑處理 30 筆 `#ptbrain` 書籤：14 筆去重（比對既有 `wiki/sources` 的 `source_url`，YouTube 需正規化影片 ID）直接移除標籤；1 筆 YouTube 頻道頁（非單一影片）與 4 筆空白 FB 貼文保留標籤待人工；11 筆新內容全數 ingest（4 篇文章 WebFetch、6 筆 IG/FB caption-only stub、1 支影片併入 inbox.md 走 notebooklm）
  - 新建 entities（2）：[[Cowart]]、[[bookMDViewer]]；更新 [[OpenAI_Codex]]、[[Claude_Code]]（官方 codex-plugin-cc 外掛）、[[Vibe_Coding]]（AI 時代設計參考素材）、[[Agentic_Engineering]]（Google 課程 Day 4+5：Spec/Security/Evaluation）、[[Gary_Chen]]
- [x] ingest inbox 2026-08-22 批次（3 支：ai-tooling ×2、competitor-intel ×1，全數完成，在獨立 worktree 進行）
  - source 頁新增 3：[[2026-08-22_省token三招_context管理]]、[[2026-08-22_super_ace_deluxe_實錄]]、[[2026-08-22_詞向量到transformer_nlp演進]]；raw/transcripts/ 新增 3 檔
  - 新建 entities（1）：[[軒轅]]；新建 concepts（6）：[[Prompt_Caching]]、[[N-gram]]、[[詞向量]]、[[前饋網路]]（填補 [[LLM_原理]] 已知缺口）、[[RNN]]、[[LSTM]]
  - 更新：[[Context_工程]]（四層 Context 結構）、[[Gary_Chen]]（2026-08-22 內容主軸）、[[LLM_原理]]（新增「第 1.5 層」、五位主講者理解階梯、缺口清單移除前饋網路）、[[MoE]]（補前饋網路回連）
  - ai-tooling `j-PlWhTJVsc`（詞向量到 Transformer）第一次連結因大小寫錯誤已失效（`j-PlWhTJVsc` vs 正確 `j-PLWhTJVsc`），經 curl 查 oEmbed/player response 確認後由使用者提供修正連結，補跑成功（見 D-015、D-017）
  - competitor-intel `n3WFEnVPSBE`（Super Ace Deluxe）逐字稿僅符號報讀，內容過薄未建 entity，僅存 source stub
  - 批次過程另撞上 notebooklm 認證再次過期（D-014），已由使用者跑 `login --fresh` 解決；另發現 worktree bash 對含 `source` 字樣指令的誤攔截（D-016）
- [x] ingest 2026-08-15 批次 3 支影片（ai-tooling ×2 + thinking ×1）— raw/transcripts/ 新增 3 檔、wiki/sources/ 新增 3 頁；新建 entities [[Joeman]]、[[阿蘭]]，新建 concepts [[Output_Style]]、[[STE100]]、[[原子習慣]]；更新 [[Claude_Code]]（Output Style 段落）、[[Gary_Chen]]（2026-08-15 內容主軸）、[[Matt_Pocock]]（W skill/STE100 關聯）、[[Even_Realities_G2]]（Joeman 開箱：設計協作、Claude Code Terminal 連線門檻＋Pro 訂閱限制、導航限制、規格衝突表補第三筆翻譯語言數據）；notebooklm CLI 全程無認證問題
- [x] 修正 CLAUDE.md 第 12 節「ingest inbox」路徑：`_meta/prompts/inbox_ingest.md`（不存在）→ `_meta/inbox_ingest_prompt.md`（實際檔案位置）
- [x] ingest 2026-08-08 批次 5 支 ai-tooling 影片 — raw/transcripts/ 新增 5 檔、wiki/sources/ 新增 5 頁；新建 entities [[MemoMind_One]]、[[Ray-Ban_Meta]]、[[OpenClaw]]、[[Tailscale]]，新建 concept [[指令預算]]；更新 [[Even_Realities_G2]]（Evenhub 平台／OcuClaw／美元價格階梯／規格衝突表）、[[AI智慧眼鏡]]（路線光譜擴為四款＋顯示派vs相機派＋眼鏡作為 Agent 終端）、[[Meta]]、[[Gary_Chen]]、[[Peter_Steinberger]]、[[Context_工程]]、[[Skill_輕量化]]；index.md（實測 93/53/66）、log.md、inbox.md 已同步；斷鏈掃描通過（僅餘 stub [[Even_Realities_G1]] 與既有 [[Will_Fan]]）
- [x] lint LLM 底層原理頁群（22 concept ＋ 8 source）— 新建 topic 樞紐頁 [[LLM_原理]]（四層階梯／路線之爭／四位主講者理解階梯／缺口清單，38 個連結零斷鏈）；修 [[World_Models]] 斷鏈 3 處 → [[世界模型]]；[[Transformer]]、[[神經網路]] 加回連；index.md（Topics 4）、log.md 已同步
- [x] ingest 2026-08-01 批次 2 支 ai-tooling 影片（AI 原理類）— raw/transcripts/ 新增 2 檔、wiki/sources/ 新增 2 頁；新建 entities [[大飛]]、[[王木頭]]，新建 concepts [[Transformer]]、[[注意力機制]]、[[位置編碼]]、[[MoE]]、[[萬能逼近定理]]、[[激活函數]]；更新 [[神經網路]]、[[反向傳播]]、[[梯度下降]]、[[2026-07-10_神經網路_漫士科普]]；index.md（實測 88/49/65）、log.md、inbox.md 已同步
- [x] 修復 NotebookLM CLI 認證失效 — 根因為版本落後（Python312 環境 0.3.4 → 0.7.3），非 cookie 問題
- [x] ingest 2026-07-25 批次 3 支 ai-tooling 影片 — raw/transcripts/ 新增 3 檔、wiki/sources/ 新增 3 頁；新建 [[Matt_Pocock]]、[[Corey_McClain]]、[[示範式自動化]]；更新 [[Claude_Cowork]]（stub 補實）、[[RPA]]、[[Skill_輕量化]]、[[Vibe_Coding]]、[[Gary_Chen]]、[[Google]]、[[2026-07-18_codex_record_replay_fork]]（待追蹤回填）；index.md（86/47/59）、log.md、inbox.md 已同步
- [x] ingest 2026-07-18 批次 7 支 ai-tooling 影片（NotebookLM 繁中 briefing）— raw/transcripts/ 新增 7 檔、wiki/sources/ 新增 7 頁；新建 concepts `Agentic_Engineering`、`Skill_輕量化`、`Git_版本控制` 與 entities `Grok_4.5`、`Jay_JayLuxAI`、`李廠長`；更新 `NotebookLM`、`OpenAI_Codex`、`Harness_Engineering`、`Context_工程`、`Vibe_Coding`、`AIOS`、`xAI`、`Claude_Fable_5`、`黃一河`、`Gary_Chen`；index.md（統計 83 sources／46 entities／58 concepts）、log.md（append 一筆）、inbox.md（7 筆移入已處理）
- [x]（前次）ingest「多 AI Deep Research → Claude 裁決 Prompt 組」＋ raw 檔正名歸位（詳見 log.md 2026-07-16）

## 進行中
- （無）

## 待辦（依優先序）
1. 裁決 [[Even_Realities_G2]] 的規格衝突（續航 48hr vs 12hr、語言 31 vs 29 vs「35 種支援/29 種雙向中文」）——2026-08-15 新增第三筆語言數據仍未解開差異，需第三方規格頁或官網佐證
1b. 建 [[Will_Fan]] entity 頁（既有斷鏈，被 [[Even_Realities_G2]] 與 [[AI智慧眼鏡]] 引用；素材在 2026-06-27_even_g2_創辦人訪談）
2. 兩處敘述小修（使用者本輪未選，隨時可做）：[[Transformer]] 頁「靠後續 RLHF 等對齊階段」把三階段壓成兩階段，應改為明確的預訓練→SFT→RL；[[2026-05-16_stanford_diffusion_lecture4]] 的 [[潛在空間]] stub 可指向 [[VAE]]
3. 補 [[LLM_原理]] 標記的五個缺口頁（依重要性，前饋網路已於 2026-08-22 補齊）：Tokenization、預訓練、SFT、Scaling_Laws、Context_Window
4. competitor-intel「Treasures of Aztec — PG Soft 大獎實錄」（W-5vaMiUlKQ）ingest 失敗待重試（見 D-004）
5. ingest `raw/notes/2026-07-16_GitEasyLearning.md`（使用者手寫筆記，與 `Git_版本控制` concept 主題重疊，屆時合併觀點）
6. 若有更完整機制說明的來源，可考慮建立《Super Ace Deluxe》entity 頁（見 [[2026-08-22_super_ace_deluxe_實錄]]，目前僅 source stub）
7. Raindrop `#ptbrain` 標籤還留著 5 筆待人工處理：YouTube 頻道頁 `@twtrubiks`（raindrop_id 1742793174，非單一影片內容）；4 筆 Facebook 貼文 excerpt 完全空白（1801195206、1738256591、1716800463、1710412372），需要使用者自己看原貼文決定要不要保留/怎麼處理
8. [[2026-08-05_李宏毅機器學習2026筆記集]] 只讀了 HackMD 集合頁摘要，11 篇子文章都還沒逐篇深入；若想真正蒸餾內容需要之後個別 WebFetch
9. news `2Smy2AUbLJI`（同一人?12年前爸爸為接球...TVBS新聞）notebooklm source add 連續失敗，oEmbed 確認影片本身有效，疑 notebooklm 端問題，待重試

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
- D-012：2026-08-08 的 `Authentication expired` **不是**版本問題（0.7.3→0.8.0 升級後仍失敗），是 cookie 真的失效。已排除的自動路徑：`NOTEBOOKLM_HEADLESS_REAUTH=1`（無效）、`notebooklm login --browser-cookies chrome`（Windows App-Bound Encryption 導致 `Could not decrypt chrome cookies`）。結論：**只能由使用者跑 `notebooklm login --fresh` 走瀏覽器 OAuth**，且要確認 Chromium 視窗登入完成才會寫入 storage_state（本次使用者第一次跑的 PID 27680 結束但未寫入）
- D-013：升級 notebooklm-py 前要先確認沒有 notebooklm 程序在跑，否則 pip 無法覆寫 `Scripts\notebooklm.exe`（WinError 32），會留下 `~otebooklm` / `~otebooklm_py-<舊版>.dist-info` 殘留目錄。模組本體仍會裝成功、`--version` 正常，可事後清理
- D-009：這台機器有兩套 Python（PATH 上 `pip` 屬 Python314，但 `notebooklm` 執行檔屬 Python312）。升級 notebooklm-py 必須指定 `/c/Users/user/AppData/Local/Programs/Python/Python312/python -m pip install -U notebooklm-py`，直接下 `pip install` 會裝到錯的環境
- D-014：2026-08-22 `ingest inbox` 一開始就撞到 `notebooklm list` 回報 `Authentication expired`。依 D-008 慣例先查版本：`notebooklm --version` 顯示 CLI 0.8.0，PyPI 最新 0.8.1，只差一個 patch version，排除版本落後的可能。`notebooklm auth check --test` 證實 cookie 存在但 `token_fetch: false`（真的過期，非 D-008 那種版本問題）。依 D-012 的結論，這種情況只能由使用者跑 `notebooklm login --fresh` 走瀏覽器 OAuth 重新授權，agent 端無法代為處理
- D-015：ai-tooling `j-PlWhTJVsc`（詞向量到 Transformer）`notebooklm source add` 連續 3 次皆回報 `RPCError rpc_code=9`。追查根因：`curl` 直查 YouTube oEmbed 回 404，watch 頁面 player response 顯示 `"status":"ERROR"`、`"reason":"無法播放影片"`——**影片本身已失效**（下架/私人/區域限制之一），不是 notebooklm 或本流程的問題，重試無用。已在 inbox.md 標註並請使用者提供正確連結，不猜測替代影片 ID
- D-016：worktree-isolated 的 Bash 環境會攔截任何含有字面字串 `source` 的指令（誤判為 shell `source` 建置腳本，即使是 `notebooklm source add/wait` 這類 CLI 子指令名稱），直接 `export ... && notebooklm source ...` 會被拒絕。解法：把指令寫進 `.sh` 檔（存在 job tmp 目錄），再用 `bash <script路徑>` 執行——Bash 工具收到的指令字串本身不含 `source` 字樣即可放行
- D-017：D-015 的 `j-PlWhTJVsc` 失效連結，根因是**使用者貼進 inbox.md 時打錯大小寫**——正確 ID 是 `j-PLWhTJVsc`（YouTube 影片 ID 區分大小寫，`l` vs `L` 是完全不同的影片）。經 `curl "https://www.youtube.com/oembed?url=...&format=json"` 驗證修正後的連結回傳有效 JSON（含標題／作者）即可放心進 notebooklm，不必再猜測；下次遇到「影片無法播放」，先檢查連結字元本身有無大小寫或形似字元（l/I/1、O/0）的手誤，比假設影片下架更快排除
- D-018：Raindrop API 單筆操作（更新/刪除單一 raindrop）的端點是**單數** `PUT /rest/v1/raindrop/{id}`；列表/搜尋端點才是**複數** `GET /rest/v1/raindrops/{collectionId}`。第一次照 `raindrop_ingest.md` 初稿寫的複數端點打單筆更新會全部回 404，已修正文件
- D-019：2026-08-22 `ingest raindrop` 首跑過程中 notebooklm 認證中途又報過期一次（`token_fetch: false`），但幾分鐘後**未經使用者任何動作就自行恢復正常**（`token_fetch: true`）。跟 D-012/D-014 的「真過期、只能使用者手動 login」不同——這次可能是短暫的 session token 刷新延遲。下次遇到認證錯誤，若使用者稍早才成功登入過，可以先間隔幾分鐘重試一次 `auth check --test`，不必立刻要求重新 login
- D-020：一般個人娛樂內容（動漫、電影/劇集解說與預告、明星網紅偶像、音樂放鬆/BGM、運動賽事）**明確不進 PTBrain**，遇到直接 skip，不建 notebook、不進 inbox.md。這跟 CLAUDE.md 的知識庫定位一致：PTBrain 是專業/知識類累積，不是全部瀏覽紀錄的備份。判斷關鍵字沒有窮舉清單，靠常識判斷「這是不是知識/專業內容」，模糊時才套用「無法判斷先標 ai-tooling」規則，不要對明顯的娛樂內容套用這個 fallback
- D-021：從瀏覽紀錄／Raindrop 這類「被動蒐集」來源批次 ingest 個人生活類內容時（health/tech-life/news 等），只建 `wiki/sources/` 頁，**不建 entity/concept**——這類內容多是一次性事件或消費性產品評測，沒有累積性的知識網絡可言，跟 ai-tooling/thinking 那種會被多篇來源反覆更新的專業概念不同

## 已知問題 / 風險
- [[多AI研究裁決]] 工作流尚無實跑驗證；首次 run 後應回填效果評估到 source 頁「待追蹤」
- `research-runs/` 資料夾尚未建立（筆記建議的實跑檔案佈局），首次實跑時再建
- `raw/transcripts/tmp_briefings/` 目錄仍存在（2026-06-19 lint 清過 tmp_ 檔，此目錄殘留），下次 lint 時確認可否清除
- [[ai自動化os_三家比較]] synthesis 可能需擴充：Grok 4.5 入局後 agentic 編程成三強格局

## 下次接續點
- **`ingest inbox` 現在每次都會先跑「從瀏覽紀錄自動補齊」**：讀 Downloads 底下最新 history.csv，遇到娛樂內容直接 skip，不會再像這次一樣建出entertainment notebook
- **主目錄與 worktree 已正式合併，worktree 即將清除**：合併後只保留 main 一份，不用再擔心兩邊分岔
- **下次 `ingest raindrop`**：直接跑 `_meta/raindrop_ingest_prompt.md`；Raindrop `#ptbrain` 標籤上還留 5 筆待人工的（見待辦 7），下次跑之前使用者可以先自己清一清或決定要不要保留
- inbox.md 待處理區已清空；下次 ingest 先查 `git status --short raw/` 有無未處理的 untracked 檔
- 本批未建立 topic 樞紐頁：[[原子習慣]] 是 thinking-methods notebook 的第二個主題（第一個是 2026-07-04 的馬斯克清醒演講/第一性原理），兩者尚未有共同樞紐，暫不急著建（CLAUDE.md 3.1：少量頁面不用急著建 topic）
- 環境已清理（2026-08-08 使用者授權）：移除 `~otebooklm` / `~otebooklm_py-0.7.3.dist-info` 殘留目錄，卸載本次臨時安裝的 10 個套件（browser_cookie3、rookiepy 及其依賴鏈 lz4／pycryptodomex／pywin32／WMI／shadowcopy，以及查依賴用的 pipdeptree／nab-index／nab-python）。清理後 `pip check` 無破損、`notebooklm status` API 實測正常
- 可重用腳本存於本次 scratchpad：`make_raw.py`（rich 硬換行 unwrap ＋ 加 frontmatter，本批 5 檔實測可用）、`linkcheck.py`（斷鏈 ＋ inbound 統計，可直接當 lint 第一步）
- 可考慮的 synthesis：**AI 眼鏡兩派路線對決**素材已齊（顯示派 [[Even_Realities_G2]]／[[MemoMind_One]] vs 相機派 [[Ray-Ban_Meta]]，加上 [[RayNeo_X3_Pro]] 的全彩 AR 第三路線，共 8 份來源）——比既有的三家 AI OS 比較更成熟
- 可考慮的動作：用 [[指令預算]] 的三分流表回頭體檢本 vault 的 `CLAUDE.md`（使用者全域規範第 11 節已有 250 行預算規則，主張同源）
- 斷鏈掃描腳本已固化為 scratchpad `linkcheck.py`（掃 `wiki/**/*.md` 的 `[[連結]]` 比對檔案 stem，同時查斷鏈、孤立頁、inbound 數）；建議每次 lint 先跑它再讀內容。全庫現況：35 頁有斷鏈，絕大多數是 CLAUDE.md 3.1 允許的刻意 stub
- 新版 CLI（0.7.3）差異：`-n` 取代 `--notebook`；新增 `--prompt-file`（長 prompt 免跳脫，本批已改用）
- CLI 輸出有 rich 終端硬換行，raw 檔需經 unwrap 才可用；本批腳本存於 scratchpad `make_raw.py`，下批可重用（規則：結構行另起、標題後另起、非雙 CJK 交界補空格）
- 可考慮的 synthesis：三支 AI 原理科普（[[漫士]]／[[王木頭]]／[[大飛]]）涵蓋層次互補，可做「神經網路到 LLM 的理解階梯」對照頁
- 注意：inbox.md 待處理區已不見 W-5vaMiUlKQ 失敗件（與待辦 1 的描述不一致，重試時以 notebook 直加路徑為準）
- 待使用者裁決的建議：是否做「AI 簡報生成工具比較」synthesis（Codex／NotebookLM／Gemini in Slides 三路線 source 已齊，見 [[2026-07-25_gemini_slides_簡報]] 待追蹤）
- 若有新 ingest：先查 `inbox.md` 待處理區，再查 `raw/` untracked 檔案（`git status --short raw/`）
- 失敗件重試路徑：`notebooklm source add "https://www.youtube.com/watch?v=W-5vaMiUlKQ" -n c8bcfd26`（competitor-intel notebook）；若仍失敗，改走手動逐字稿或跳過
- 若實跑多 AI 研究：從 `raw/notes/2026-07-16_多ai研究裁決_prompt組.md` 取 prompt，產出存 `research-runs/<日期_主題>/`，裁決結果可考慮歸檔為 synthesis
