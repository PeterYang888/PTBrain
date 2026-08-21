# Log

> 時序記錄。Append-only。每筆以 `## [YYYY-MM-DD] type | title` 開頭，方便 grep。
> 用 `grep "^## \[" log.md | tail -10` 查最近活動。

---

## [2026-04-17] bootstrap | 建立 wiki 架構
- 建立 `CLAUDE.md`（schema）
- 建立 `README.md`、`index.md`、`log.md`
- 建立目錄：`raw/{articles,papers,notes,transcripts,assets}`、`wiki/{sources,entities,concepts,topics,syntheses}`
- 等待第一份 source ingestion

## [2026-04-17] ingest | Claude Code 桌面改版 + routines（數位時代 2026-04-15）
- source 頁：[[2026-04-15_claude_code_desktop_routines改版]]
- 新建 entities：[[Anthropic]], [[Claude_Code]]
- 新建 concepts：[[routines]], [[side_question]]
- 新建 topic：[[Anthropic_Claude_生態]]（作為後續 Claude 相關資料的樞紐）
- 更新：[[index]]

## [2026-04-17] ingest | Claude 模型選擇指南（數位時代 2026-04-16，作者 陳祈安）
- source 頁：[[2026-04-16_claude_模型選擇指南]]
- 新建 entities：[[Claude_Opus_4.6]], [[Claude_Sonnet_4.6]], [[Claude_Haiku_4.5]], [[Claude_Cowork]]
- 新建 concepts：[[延伸思考]], [[自適應思考]], [[合憲_AI]]
- 更新：[[Anthropic]]（補產品線），[[Claude_Code]]（補模型搭配建議），[[Anthropic_Claude_生態]]（補模型與概念），[[index]]
- stub links 留白等待補頁：[[Claude]]（模型家族 umbrella 頁）

## [2026-04-20] ingest | 第一性原理：5 支影片綜合分析（raw/notes）+ 書籍 PDF（raw/papers）
- source 頁：[[2026-04-19_第一性原理_5支影片綜合分析]]（5 支中文影片的綜合筆記）
- source 頁：[[2024_第一性原理_21堂科學通識課]]（Marcus Chown，stub；PDF 因工具限制暫無法讀取）
- 新建 concepts：[[第一性原理]]（主頁）, [[類比思維]], [[語義樹]]
- 新建 entities：[[Elon_Musk]], [[Marcus_Chown]]（stub）, [[Steve_Jobs]]（stub）
- 更新：[[index]]（Topics、People、Concepts、Sources、統計）
- 注意：PDF（199 頁）需要 pdftoppm 才能讀取，待工具齊備後補充章節摘要

## [2026-04-22] ingest | Educational Game Design Fundamentals（NotebookLM GameDesign briefing）
- source 頁：[[2026-04-22_gamedesign_briefing]]
- 新建 concepts：[[教育遊戲設計]], [[內在動機]], [[Flow流暢感]], [[鷹架理論]], [[後向設計]]
- 新建 entities：[[George_Kalmpourtzis]], [[Tynan_Sylvester]]（stub）, [[Jesse_Schell]]（stub）
- 新建 topic：[[遊戲設計]]
- 更新：[[index]]（Topics、People、Concepts、Sources、統計）
- 注意：Tynan Sylvester《Designing Games》尚未 ingest，待補

## [2026-04-22] synthesis | 第一性原理 × AI 工具選擇
- 新建：[[第一性原理_x_AI工具選擇]]
- 橋接兩條主線：[[第一性原理]]四步落地法 × [[Anthropic_Claude_生態]]模型分層
- 核心結論：大多數工具選擇靠類比思維；第一性原理要求先列物理邊界，從最低成本起跑
- 更新：[[index]]（Syntheses、統計）

## [2026-05-16] ingest | 瘦瘦針研究 Podcast（GLP-1 藥物全面解析）
- 前置作業：用 openai-whisper（medium 模型）將 `raw/assets/瘦瘦針研究_podcast.mp3` 轉錄為逐字稿，存至 `raw/transcripts/瘦瘦針研究_podcast_transcript.md`
- source 頁：[[2026-05-16_瘦瘦針研究_podcast]]
- 新建 concepts：[[GLP-1受體激動劑]], [[內臟脂肪作為內分泌器官]]
- 新建 entity：[[Semaglutide]]
- 新建 topic：[[代謝醫學與GLP-1]]
- 更新：[[index]]（Topics、Drugs/Products、Concepts、Sources、統計）
- stub links 留待補頁：[[Tirzepatide]], [[Retatrutide]], [[多巴胺獎勵機制]], [[肥胖的醫學重新定義]]
- 待追蹤：台灣健保給付狀況、Orforglipron 上市時程、肌肉流失 15% 的原始試驗

## [2026-05-16] ingest | 批次處理 10 支 ai-tooling YouTube 影片（NotebookLM 繁中 briefing）
- 工具：notebooklm-py CLI → 繁體中文 briefing-doc → PTBrain raw/transcripts + wiki
- source 頁（10 頁）：
  [[2026-05-16_anthropic_超越_openai]]、[[2026-05-16_ai前沿週報_ep6_claude勒索]]、
  [[2026-05-16_ai泡沫分析]]、[[2026-05-16_claude_code_代理工具]]、
  [[2026-05-16_ai教父_agi內幕]]、[[2026-05-16_stanford_diffusion_lecture4]]、
  [[2026-05-16_stanford_ai系統課程_agentic]]、[[2026-05-16_harness_engineering_ai職涯]]、
  [[2026-05-16_claude_code_obsidian_知識庫]]、[[2026-05-16_claude_code_人物蒸餾]]
- 新建 entities：[[Yann_LeCun]], [[OpenAI]]
- 新建 concepts：[[AGI]], [[JEPA]], [[RAG]], [[AI_Alignment]], [[Harness_Engineering]], [[Agentic_Workflow]], [[人物蒸餾]]
- 更新 entities：[[Anthropic]]（ARR 超越 OpenAI、Claude 勒索事件）、[[Claude_Code]]（Free 代理工具、Obsidian 整合、人物蒸餾）
- 更新：[[index]]（+10 sources, +2 entities, +7 concepts，統計更新）
- 待補（rate limit）：ai-tooling 第 11–13 支（NotebookLM 簡報模板、AI 時代學習法、保時捷 vs Model 3）
- 待補（rate limit）：competitor-intel 4 支（戰神賽特 2 系列），第 5 支影片不可用（fY02Rmzxa7s）

## [2026-05-16] ingest | 7 支影片補充（ai-tooling ×3 + competitor-intel ×4）+ Apple 產品策略 raw 檔
- ai-tooling 用 `notebooklm ask` 取得摘要（briefing-doc rate limited）
- source 頁（7 頁）：
  [[2026-05-16_notebooklm_簡報模板]]、[[2026-05-16_ai時代學習法]]、[[2026-05-16_保時捷_vs_model3]]、
  [[2026-05-16_戰神賽特2_覺醒觸發機制]]、[[2026-05-16_戰神賽特2_五張登頂]]、
  [[2026-05-16_戰神賽特2_5000分加壓]]、[[2026-05-16_戰神賽特2_選房技巧]]（stub，逐字稿提取失敗）
- 額外 ingest：[[2026-05-16_apple_ceo_ternus]]（Apple CEO 換帥，raw/transcripts 中未處理的舊檔）
- inbox.md：所有 18 支影片全部處理完畢（2 支有限制：fY02Rmzxa7s 下架、Lj-wfVnmna8 逐字稿失敗）
- 更新：[[index]]（Sources 16 → 24）

## [2026-05-16] ingest | 5 支影片補充（ai-tooling ×3 + competitor-intel ×2，ask 指令替代 rate-limited briefing）
- 使用 `notebooklm ask` 取得摘要（NotebookLM briefing-doc 每日配額用盡）
- source 頁（5 頁）：
  [[2026-05-16_notebooklm_簡報模板]]（NotebookLM 簡報 Prompt 自動化）、
  [[2026-05-16_ai時代學習法]]（AI Agent 時代個人進化策略）、
  [[2026-05-16_保時捷_vs_model3]]（保時捷 vs 特斯拉開發思維比較）、
  [[2026-05-16_戰神賽特2_覺醒觸發機制]]（competitor-intel）、
  [[2026-05-16_戰神賽特2_五張登頂]]（competitor-intel）
- 尚待處理：competitor-intel 2 支（5000分加壓機制、選房技巧），因 auth 過期待重新登入後補
- 更新：[[index]]（Sources 16 → 21）、[[inbox]]（移 5 項至已處理）

## [2026-04-20] ingest | 補完 PDF 讀取——第一性原理 21 堂科學通識課
- 方法：以 PyMuPDF（fitz）繞過 pdftotext 編碼問題，成功提取全文
- 更新：[[2024_第一性原理_21堂科學通識課]]（stub → 完整，含 21 章目錄與各章命題句）
- 工具備忘：日後 raw/papers/ 放 PDF，用 `C:/Python314/python.exe -c "import fitz..."` 搭配 `sys.stdout.reconfigure(encoding='utf-8')` 即可讀取中文 PDF

## [2026-05-20] ingest | 7 支逐字稿補完（含路徑修正 + hook 修復）
- 背景：上次批次 ingest 用 NotebookLM 摘要建立 source 頁，但 raw ref 指向不存在路徑；hook 也因大小寫不一致而持續誤報
- 修復：`.claude/check_raw.py` 的 `key_segments()` 改為小寫比對 + CJK/ASCII 混排拆分
- source 頁路徑修正（6 個）+ 內容深度擴充（7 個）：
  - [[2026-05-16_ai前沿週報_ep6_claude勒索]]（路徑修正 + Claude 勒索還原 + GPT Real-Time 2 細節）
  - [[2026-05-16_ai教父_agi內幕]]（路徑修正 + AMI Labs 融資/估值 + V-JEPA 2 機器人控制 + Barlow Twins + 歷史脈絡表）
  - [[2026-05-16_ai時代學習法]]（路徑修正 + 三步驟三階段完整細節）
  - [[2026-05-16_anthropic_超越_openai]]（路徑修正 + ARR 時間軸 + 商業模式對比 + 爭議點）
  - [[2026-05-16_stanford_ai系統課程_agentic]]（路徑修正 + BCG 研究 + 4 維度差異 + 三層自主性 + 評估框架 + 客服 case study）
  - [[2026-05-16_stanford_diffusion_lecture4]]（路徑修正 + 像素空間問題 + VAE ELBO 推導 + CLIP + CFG 公式 + 訓練推理流程）
  - [[2026-05-16_apple_ceo_ternus]]（路徑已正確 + Cook 15 年成績 + Ternus 風格 + 人事改組表 + 產品策略）
- 新建 entities：[[Apple]], [[AMI_Labs]], [[John_Ternus]], [[Tim_Cook]]
- 新建 concepts：[[世界模型]], [[VAE]], [[CLIP]], [[CFG]], [[擴散模型]], [[MCP]]
- 更新：[[Yann_LeCun]]（修正 Meta 現職描述 → 已離職，AMI Labs 創辦人）、[[index]]（+4 entities, +6 concepts, 統計更新）

## [2026-05-30] ingest | 7 支影片（ai-tooling ×7）+ 1 支失敗（competitor-intel Pinata）
- 工具：notebooklm generate report --format briefing-doc -s <source_id>，逐源生成繁體中文 briefing
- 處理來源：inbox.md 2026-05-30 批次（ai-tooling 7 支 + competitor-intel 1 支）
- **失敗**：競爭情報 Pinata Wins by PG Soft（https://www.youtube.com/watch?v=ecyfJTM2LmI），API 返回無資料（可能影片有地區限制或私人設定）
- source 頁（7 頁）：
  [[2026-05-30_ai_agent_goal功能]]（/goal 功能與 Rubric 評審架構）、
  [[2026-05-30_股癌_ep659_生理科技心智]]（AI 硬體輪動 + AI Slop + 生理優化）、
  [[2026-05-30_karpathy_ai編程陷阱]]（claud.md 四條規則，返工率 41%→11%）、
  [[2026-05-30_codex_零基礎入門]]（Codex 入門、Plugins/Skills/NCP）、
  [[2026-05-30_codex_office全包辦]]（AGENTS.md + Computer Use + 校慶案例）、
  [[2026-05-30_ai_ppt_codex]]（邏輯分離法則，8分鐘/10頁 PPT）、
  [[2026-05-30_ai眼鏡時代]]（AI 智慧眼鏡市場，CAGR 58%，三強鼎立）
- 新建 entities：[[OpenAI_Codex]]、[[Meta]]
- 新建 concepts：[[AI智慧眼鏡]]
- 更新：[[Andrej_Karpathy]]（+claud.md 四條規則）、[[OpenAI]]（+Codex 產品說明）、
  [[Google]]（+EssilorLuxottica+Magic Leap 合作）、[[Agentic_Workflow]]（+/goal+Context Anxiety+Rubric）
- 更新：[[index]]（+7 sources, +2 entities, +1 concept）
- inbox.md：7 支移至已處理，competitor-intel Pinata 記錄失敗原因後保留

## [2026-05-24] ingest | 7 支 ai-tooling 影片（Karpathy 三部曲 + Karpathy 筆記術 + PrintingPress + Google I/O 2026 + AI裁員）
- 工具：notebooklm ask --json（PowerShell UTF-8 模式解決 Windows 編碼問題）
- source 頁（7 頁）：
  [[2026-05-24_karpathy_how_i_use_llms]]、[[2026-05-24_karpathy_deep_dive_llms]]、
  [[2026-05-24_karpathy_intro_llms_1hr]]、[[2026-05-24_karpathy_筆記術_claude_code]]、
  [[2026-05-24_printingpress_cli]]、[[2026-05-24_google_io_2026]]、
  [[2026-05-24_ai_裁員_經理vs個人貢獻者]]
- 新建 entities：[[Andrej_Karpathy]]、[[Google]]
- 新建 concepts：[[推理模型]]、[[Vibe_Coding]]、[[RLHF]]、[[MTS]]
- 更新：[[index]]（+7 sources, +2 entities, +4 concepts，統計更新）
- inbox.md：7 支全部處理完畢，移至已處理區
- stub links 留待補頁：[[Gemini]]、[[Few-shot_Prompting]]、[[PrintingPress]]（工具頁）、[[Token效率]]、[[DeepSeek]]、[[知識管理]]

## [2026-06-06] ingest | 11 天寫 75 萬行程式碼！Claude Code Dynamic Workflows（YouTube）
- source 頁：[[2026-06-06_11天_claude_code_dynamic_workflows]]
- 新建 concepts：[[Dynamic_Workflows]]
- 更新：[[Claude_Code]]（新增 Dynamic Workflows 段落），[[Agentic_Workflow]]（補充多智能體協作模式）
- 更新：[[index]]

## [2026-06-06] ingest | Claude Code 同時跑 1000 個 agent：Dynamic Workflows（YouTube）
- source 頁：[[2026-06-06_claude_code_1000_agent_dynamic_workflows]]
- 更新 concepts：[[Dynamic_Workflows]]（補充對抗式驗證機制、Zig→Rust 案例、版本規格）
- 更新：[[index]]

## [2026-06-06] ingest | Anthropic 工程師為什麼拋棄 Markdown 改用 HTML 跟 AI 工作？（YouTube）
- source 頁：[[2026-06-06_anthropic_棄_markdown_改用_html]]
- 新建 concepts：[[理解成本]]
- 更新 concepts：[[Vibe_Coding]]（補充理解成本風險段落）
- 更新：[[index]]

## [2026-06-06] ingest | AI 時代非技術人最該學的設計能力：把 Human SOP 變成 Agentic Workflow（YouTube）
- source 頁：[[2026-06-06_human_sop_agentic_workflow]]
- 更新 concepts：[[Agentic_Workflow]]（補充 SOP 四部曲）、[[MCP]]（USB-C 比喻 + Agentic AI Foundation 治理）
- 更新：[[index]]

## [2026-06-06] ingest | AI 正在掏空中型公司（YouTube）
- source 頁：[[2026-06-06_ai_掏空中型公司]]
- 新建 concepts：[[AI組織變革]]
- 更新：[[index]]

## [2026-06-12] ingest | Graphify：解決 Claude Code 記憶與成本問題的開源知識圖譜工具（YouTube）
- source 頁：[[2026-06-12_graphify_claude_code]]
- 新建：[[Graphify]]（concepts）
- 更新：[[Claude_Code]]（新增 Graphify 段落）、[[RAG]]（新增 Graphify 作為 RAG-lite 應用）、[[index]]

## [2026-06-12] ingest | Claude Dynamic Workflow 解析，什麼時候該用、什麼時候別碰？（YouTube）
- source 頁：[[2026-06-12_dynamic_workflow_解析]]
- 更新：[[Dynamic_Workflows]]（新增 4 層階梯表、成本三招、更新時間戳）
- 更新：[[Agentic_Workflow]]（新增 AI 原生組織角色）
- 更新：[[index]]

## [2026-06-12] ingest | 什麼是 AI Operating System？一套能讓 AI 替你工作的系統（YouTube）
- source 頁：[[2026-06-12_ai_operating_system]]
- 新建：[[AIOS]]（concepts）
- 更新：[[Agentic_Workflow]]（新增 AIOS 實作模式）
- 更新：[[index]]

## [2026-06-12] ingest | Introducing Claude Fable 5（YouTube）
- source 頁：[[2026-06-12_claude_fable5]]
- 新建：[[Claude_Fable_5]]（entities）
- 更新：[[Anthropic]]（產品線新增 Fable 5、更新 sources）
- 更新：[[index]]

## [2026-06-12] ingest | AI 原生組織的底層邏輯（YouTube）
- source 頁：[[2026-06-12_ai_原生組織底層邏輯]]
- 更新：[[AI組織變革]]（新增串行瓶頸/並行網路框架、三代演進、5 大人類能力）
- 更新：[[index]]

## [2026-06-19] lint | 清理 raw/transcripts 殘留 tmp_ 暫存檔
- 起因：hook 提示 `tmp_ai_native_org.md` 未 ingest；驗證後確認內容早已 ingest（屬 2026-06-12 批）
- 刪除 5 個未追蹤殘留重複檔（2026-06-12 批，已有正式 `2026-06-12_*.md` + source 頁）：
  tmp_ai_native_org / tmp_ai_operating_system / tmp_claude_fable5 / tmp_dynamic_workflow_解析 / tmp_graphify_claude_code
- 正名 7 組已 commit 的 raw 逐字稿（.md + .json，2026-05-24 批；原 tmp_ 命名是該批 source 頁唯一原始檔）：
  `tmp_<slug>` → `2026-05-24_<slug>`（google_io_2026 / printingpress_cli / ai_裁員_經理vs個人貢獻者 / karpathy_intro_llms_1hr / karpathy_deep_dive_llms / karpathy_how_i_use_llms / karpathy_筆記術_claude_code）
- 未碰：`tmp_briefings/` 10 個 NotebookLM 中間檔（另一種結構）
- 無 wiki 頁面內容變動

## [2026-06-19] ingest | 批次處理 7 支 ai-tooling YouTube 影片（NotebookLM 繁中 briefing）
- 來源：inbox.md「待處理」7 支；用 notebooklm `ask` 產 6 段式繁中 briefing，存 `raw/transcripts/2026-06-19_*.md`（含 frontmatter）
- source 頁（7）：[[2026-06-19_claude_code_500小時心得]], [[2026-06-19_claude_code轉codex]], [[2026-06-19_loop_engineering]], [[2026-06-19_prompt定義任務]], [[2026-06-19_notebooklm整座圖書館]], [[2026-06-19_ai復活老遊戲]], [[2026-06-19_rayneo_x3_pro_ar眼鏡]]
- 新建 concepts（4）：[[Loop_Engineering]], [[Context_工程]], [[工具無關性]], [[定義任務]]
- 新建 entities（4）：[[NotebookLM]], [[RayNeo_X3_Pro]], [[Boris_Cherny]], [[Peter_Steinberger]]
- 更新 entities/concepts：[[Claude_Code]]（心法+工具分工+Loop+逆向工程）, [[OpenAI_Codex]]（互轉+推理強度+Maker/Tracker）, [[MCP]]（Token 成本+Connector）, [[AIOS]]（AI as OS+Context_工程）, [[Harness_Engineering]]（Harness→Loop 階梯）, [[AI智慧眼鏡]]（RayNeo 實機）, [[Claude_Opus_4.6]]（架構師）, [[Claude_Sonnet_4.6]]（執行者+Artifacts）, [[遊戲設計]]（AI 復活老遊戲）
- 更新 [[index]]（People/Tools/Concepts/Sources/統計）
- inbox.md：7 筆從「待處理」移到「已處理」
- 待追蹤：Addy 全名、OpenClaw、Grok 2000萬 token/Apple AFM3 規格查證、復刻遊戲版權
- 注意：source_date 暫用 ingest 日（2026-06-19），非影片實際發布日（沿用 2026-06-12 批慣例）

## [2026-06-27] ingest | 批次處理 12 支 ai-tooling YouTube 影片（NotebookLM 繁中 briefing）
- 來源：inbox.md「待處理」12 支；用 notebooklm `ask -s` 產 6 段式繁中 briefing，存 `raw/transcripts/2026-06-27_*.md`（含 frontmatter）
- 三個子主題群：AI 眼鏡（Even G2，3 支）、ComfyUI 教學（4 支）、其餘各 1（FLUX.2 / Codex PPT / Google Omni / RPA / Gemini Spark）
- source 頁（12）：[[2026-06-27_even_g2_claude_code]], [[2026-06-27_even_g2_創辦人訪談]], [[2026-06-27_even_realities_g2_36g]], [[2026-06-27_comfyui_保姆級安裝]], [[2026-06-27_comfyui_v8整合包]], [[2026-06-27_comfyui_系統教程前言]], [[2026-06-27_comfyui_基礎教學ep1]], [[2026-06-27_flux2_klein]], [[2026-06-27_image2_codex_可編輯ppt]], [[2026-06-27_google_omni_影片模型]], [[2026-06-27_rpa_要沒了]], [[2026-06-27_gemini_spark]]
- 新建 entities（6）：[[Even_Realities_G2]], [[ComfyUI]], [[Stable_Diffusion]], [[FLUX]], [[Gemini_Spark]], [[Gemini_Omni]]（+ [[Will_Fan]] stub）
- 新建 concepts（2）：[[寧靜技術]], [[RPA]]
- 更新 entities/concepts：[[AI智慧眼鏡]]（Even G2 無相機路線 + 三產品光譜表）, [[OpenAI_Codex]]（record-and-replay 取代 RPA + Image2 PPT Master）, [[Google]]（Gemini Omni 影片模型 + Gemini Spark 代理人）
- 更新 [[index]]（Tools/People/Concepts/Sources/統計：Sources 56→68）
- notebooklm 註記：加來源時 S4uYjG_AzXU（Image2+Codex PPT）首次「API returned no data」，重試成功；其餘 11 支一次成功
- 待追蹤：三家「個人/企業 AI 自動化 OS」（Codex record-and-replay / [[Gemini_Spark]] / Claude [[routines]]）可做 synthesis；FLUX.2 vs SDXL 編輯場景比較
- 注意：source_date 沿用 ingest 日（2026-06-27），非影片實際發布日

## [2026-06-27] query | 三家 AI 自動化 OS 是否同構？
- 問題：Codex record-and-replay / [[Gemini_Spark]] / Claude [[routines]]+`/goal` 三家自動化框架的異同
- 參考頁面：[[2026-06-27_rpa_要沒了]], [[2026-06-27_gemini_spark]], [[2026-05-30_ai_agent_goal功能]], [[routines]], [[AIOS]]
- 產出：[[ai自動化os_三家比較]]（synthesis）——歸納「目標 + 觸發 + 技能 + 監控驗證」四要素同構骨架；指出 Claude 的 Rubric 驗證最深、Spark 結果驗證最弱、MCP 成跨生態連接標準
- 更新 [[index]]（Syntheses 1→2 + 統計）

## [2026-07-04] ingest | 批次處理 5 支影片（ai-tooling ×4、thinking ×1，NotebookLM 繁中 briefing）
- 來源：inbox.md「待處理」5 支；用 notebooklm `ask -s` 產結構化繁中 briefing，存 `raw/transcripts/2026-07-04_*.md`（含 frontmatter）；thinking 主題首次使用，新建 notebook「thinking-methods」
- source 頁（5）：[[2026-07-04_claude_codex_互審]], [[2026-07-04_codex_geo]], [[2026-07-04_comfyui_零基礎ep01]], [[2026-07-04_running_train_擬真遊戲]], [[2026-07-04_馬斯克_清醒演講]]
- 新建 entities（2）：[[Gary_Chen]]（Claude/Codex stopHook 互審 Harness 實踐者）, [[黃一河]]（Netpe 創辦人，GEO 實踐者）
- 新建 concepts（1）：[[GEO]]（Generative Engine Optimization，與 [[理解成本]] 方向相反但呼應）
- 更新 entities/concepts：[[Harness_Engineering]]（新增個人開發者 stopHook 互審實例）, [[OpenAI_Codex]]（新增審稿人角色 + GEO 執行引擎兩節）, [[Claude_Code]]（新增 stopHook 跨模型互審機制）, [[ComfyUI]]（新增命令列手動安裝路線）, [[Elon_Musk]]（新增 2008 生死抉擇、理性接納失敗機率）, [[第一性原理]]（新增馬斯克案例）, [[理解成本]]（新增 GEO 反向視角交叉連結）
- 更新 [[遊戲設計]]（topic，新增「極致寫實案例（非 AI）」一節：《Running Train》對照 AI 生成內容的以假亂真路徑）
- 更新 [[index]]（Entities/Concepts/Sources/統計：Sources 68→73，Entities 34→36，Concepts 47→48）
- inbox.md：5 筆從「待處理」移到「已處理」
- 注意：`raw/transcripts/2026-06-27_*` 批次（12 支）與對應 wiki 頁面在 ingest 前已存在（上次 session 完成但未 commit），本次未重複處理，僅確認無 URL 重複
- 待追蹤：codex review skill 是否可公開取用；Netpe/TypeOS 商業模式；「AI 比核武危險」論述細節；ComfyUI 命令列版與既有保姆級安裝教學的路線比較

## [2026-07-10] ingest | 批次處理 3 支影片（ai-tooling，NotebookLM 繁中 briefing）

**來源**：inbox.md 待處理 3 支 YouTube → NotebookLM notebook `ai-tooling`（40e24946）

- source 頁（新建 3）：
  - [[2026-07-10_agent_teams_協作模式]] — Kelly Tsai / CKY channel
  - [[2026-07-10_六月_ai_更新彙整]] — Ava - 凜
  - [[2026-07-10_神經網路_漫士科普]] — 漫士
- raw 檔（新建 3）：`raw/transcripts/2026-07-10_*.md`
- 新建 entities（6）：[[Kelly_Tsai]], [[Replit]], [[Ava_凜]], [[漫士]], [[Geoffrey_Hinton]], [[xAI]]
- 新建 concepts（9）：[[Agent_Teams]], [[Subagent]], [[神經網路]], [[感知機]], [[梯度下降]], [[反向傳播]], [[泛化]], [[聯結主義]], [[對抗樣本]]
- 更新（9）：[[Dynamic_Workflows]]（補多 agent 效能陷阱、Replit/N8N 對照、Subagent/Agent_Teams 連結）、[[Context_工程]]（補「以 Context 分工不以角色分工」）、[[AI智慧眼鏡]]（補 Ray-Ban Meta 規格）、[[RPA]]（補 Record and Reply 抗變化原理、同代競品）、[[OpenAI_Codex]]、[[Claude_Cowork]]（補「Claude Tech」推測）、[[Meta]]、[[Yann_LeCun]]（Hinton 補連結）、[[index]]

**待核實（標為推測，未當事實寫入）**：
- 第 2 支影片的「Cedce 2.5」「Claude Tech」「Gemini 3.5」「Diffusion Spec」疑為語音辨識誤植或非官方名稱
- 第 1 支影片的「錯誤放大 17 倍」「退步至 70%」「失敗率過半」未點名原始研究出處

**lint 發現（本次未修）**：
- [[Yann_LeCun]] 頁連向 `[[World_Models]]`，但實際頁名為 `世界模型` → 斷鏈
- index.md 統計數字先前與實際檔案數有偏差（73/36/48 vs 實際 72/36/45），本次已校正為實際值

## [2026-07-16] ingest | 多 AI Deep Research → Claude 裁決 Prompt 組（使用者筆記）
- source 頁：[[2026-07-16_多ai研究裁決_prompt組]]
- 新建：[[多AI研究裁決]]（concept）
- 更新：[[Google]], [[OpenAI]], [[xAI]]（三家 deep research 分工定位）, [[定義任務]]（五欄位同構交叉連結）, [[index]]
- 備註：raw 檔已正名移至 `raw/notes/2026-07-16_多ai研究裁決_prompt組.md`；stub link：[[Pragmatic_Play]], [[Gates_of_Olympus]]

## [2026-07-18] ingest | 批次處理 7 支影片（ai-tooling，NotebookLM 繁中 briefing）
- source 頁：[[2026-07-18_notebooklm_2_0_更新]], [[2026-07-18_大模型吃掉skills]], [[2026-07-18_google_agentic_engineering_day1]], [[2026-07-18_codex_record_replay_fork]], [[2026-07-18_git_github_vibe_coding基礎]], [[2026-07-18_aios_儀表板]], [[2026-07-18_grok_4_5_發布]]
- 新建：[[Agentic_Engineering]], [[Skill_輕量化]], [[Git_版本控制]], [[Grok_4.5]], [[Jay_JayLuxAI]], [[李廠長]]
- 更新：[[NotebookLM]], [[黃一河]], [[Gary_Chen]], [[OpenAI_Codex]], [[Harness_Engineering]], [[Context_工程]], [[Vibe_Coding]], [[AIOS]], [[xAI]], [[Claude_Fable_5]], [[index]]
- 失敗：competitor-intel「Treasures of Aztec — PG Soft 大獎實錄」（W-5vaMiUlKQ）NotebookLM 兩次回報 API returned no data，已在 inbox.md 標註

## [2026-07-25] ingest | 批次處理 3 支影片（ai-tooling，NotebookLM 繁中 briefing）
- source 頁：[[2026-07-25_claude_record_a_skill]], [[2026-07-25_grill_me_matt_pocock]], [[2026-07-25_gemini_slides_簡報]]
- raw 檔（新建 3）：`raw/transcripts/2026-07-25_*.md`
- 新建 entities（2）：[[Matt_Pocock]], [[Corey_McClain]]
- 新建 concepts（1）：[[示範式自動化]]（Codex Record & Replay × Claude record a skill 對照表）
- 更新（7）：[[Claude_Cowork]]（stub 補實：co-work/chat 模式、record a skill）、[[RPA]]（同代競品補 Claude）、[[Skill_輕量化]]（MPO 樂高式 Skill 第二來源佐證）、[[Vibe_Coding]]（決策權外包批判）、[[Gary_Chen]]、[[Google]]（Gemini in Slides）、[[2026-07-18_codex_record_replay_fork]]（待追蹤回填：Claude 已跟進示範學習）、[[index]]
- 待核實（標為推測，未當事實寫入）：grill-me 影片中「生模組」疑為「深模組（Deep Modules）」語音誤植；MPO 專案 GitHub repo 名稱未在影片中出現；「GPT-5.6」為影片口述名稱
- stub link 保留未建頁：[[深模組]]
- 備註：本批開工時 NotebookLM 認證過期，使用者重新 login 後續跑；index 統計 entities 前值 46 與實測 47 有 1 筆偏差，已按實測校正

## [2026-08-01] ingest | 批次處理 2 支影片（ai-tooling，NotebookLM 繁中 briefing）
- source 頁：[[2026-08-01_llm如何工作_transformer架構]], [[2026-08-01_神經網路40分鐘_王木頭]]
- raw 檔（新建 2）：`raw/transcripts/2026-08-01_*.md`
- 新建 entities（2）：[[大飛]]（最佳拍檔）, [[王木頭]]（王木頭學科學）
- 新建 concepts（6）：[[Transformer]], [[注意力機制]], [[位置編碼]], [[MoE]], [[萬能逼近定理]], [[激活函數]]
- 更新（4）：[[神經網路]]（回填 Transformer 專頁 TODO、補萬能逼近／隱藏層抽象／策略假設／量綱）、[[反向傳播]]（補梯度消失）、[[梯度下降]]（回填學習率 TODO、補優化器問題）、[[2026-07-10_神經網路_漫士科普]]（待追蹤回填）、[[index]]
- 已更正的來源錯誤：briefing 的「Induction Heads＝歸一頭」應為歸納頭（本批保留英文原名）；「Google LLaMDA 事件」正確為 **LaMDA**
- stub link 保留未建頁：[[Tokenization]], [[前饋網路]], [[GQA]]
- 備註：本批開工時 NotebookLM 認證失效，根因是 CLI 版本落後（0.3.4 → 0.7.3），非 cookie 問題；升級後即通。tags 未套用 inbox 表格的 ai-tooling 預設值（見 PROGRESS D-007）

## [2026-08-01] lint | LLM 底層原理頁群整合檢查
- 範圍：22 個原理層 concept 頁 ＋ 8 份原理來源頁（Karpathy ×3、漫士、王木頭、大飛、AGI 內幕、Stanford diffusion）
- 新建：[[LLM_原理]]（topic 樞紐頁，四層階梯 ＋ 路線之爭 ＋ 四位主講者理解階梯 ＋ 缺口清單）
- 已修矛盾：[[World_Models]] 斷鏈 3 處（[[JEPA]]、[[Yann_LeCun]]、[[2026-05-16_ai教父_agi內幕]]）→ 改指實際頁名 [[世界模型]]
- 更新：[[Transformer]]、[[神經網路]]（加樞紐頁回連）、[[index]]（Topics 4）
- 未修（使用者本輪未選）：[[Transformer]] 對齊敘述把三階段壓成兩階段（與 [[RLHF]] 頁的 SFT 說法不完全一致）；[[潛在空間]] stub 可指向 [[VAE]]
- 已知缺口（記錄於 [[LLM_原理]]，本輪未建頁）：Tokenization、預訓練、SFT、Scaling Laws、Context Window、前饋網路 FFN

## [2026-08-08] ingest | 批次處理 5 支影片（ai-tooling，NotebookLM 繁中 briefing）
- source 頁（新建 5）：[[2026-08-08_claude_md_15分鐘精通]], [[2026-08-08_ocuclaw_even_g2_ai_agent]], [[2026-08-08_even_g2_開放平台評測]], [[2026-08-08_even_g2_vs_memomind_one]], [[2026-08-08_meta三款新眼鏡]]
- raw 檔（新建 5）：`raw/transcripts/2026-08-08_*.md`
- 新建 entities（4）：[[MemoMind_One]], [[Ray-Ban_Meta]], [[OpenClaw]], [[Tailscale]]
- 新建 concepts（1）：[[指令預算]]（Instruction Budget，Gary Chen）
- 更新（8）：[[Even_Realities_G2]]（Evenhub 開放平台、OcuClaw 外接、美元價格階梯、FOV 27.5°、規格衝突表）、[[AI智慧眼鏡]]（路線光譜表擴為四款、新增「顯示派 vs 相機派」與「眼鏡作為 Agent 終端」兩節）、[[Meta]]（去 Ray-Ban 化三款、Meta AI 弱項）、[[Gary_Chen]]、[[Peter_Steinberger]]（回填 OpenClaw 待追蹤）、[[Context_工程]]（連指令預算）、[[Skill_輕量化]]（Gary 的三分流表佐證）、[[index]]
- 本批主題分佈：1 支 Claude Code 工作流 ＋ 4 支 AI 眼鏡（同一位評測者 Steven Sullivan 同時測了兩派產品，形成難得的橫向對照）
- **已記錄但未裁決的矛盾**：Even G2 續航 48 小時（2026-06-27 批次、Ken）vs 12 小時（Steven Sullivan）；翻譯語言數 31 種 vs 29 種。兩者皆並列於 [[Even_Realities_G2]] 的「待裁決的規格衝突」表
- 已更正的來源誤植：`openclaw space gateway space restart` 等「space」為逐字稿把空格/連字號念出，已還原為 `openclaw gateway restart`、`-Scope CurrentUser`（標為 [推導]）；"Meta Gen 2 WFares" → Wayfarer
- 未核實的名詞（已在 source 頁標註）：語音轉文字服務 "Sonics"/`sonx.com`、"Harmon audio"（疑為 Harman）、Meta 三款型號名、CLAUDE.md 影片的 `.code` 資料夾（實際應為 `~/.claude/`）與 `/insights` 指令拼法
- stub link 保留未建頁：[[Even_Realities_G1]]
- 既有斷鏈（非本批造成，待 lint 處理）：[[Will_Fan]] 被 [[Even_Realities_G2]] 與 [[AI智慧眼鏡]] 引用但無頁面
- 工具狀況：開工時 NotebookLM 認證過期，升級 CLI 0.7.3→0.8.0 無效（與 D-008 不同），headless reauth 與 browser-cookies 皆失敗，最後由使用者跑 `login --fresh` 解決（見 PROGRESS D-012）

## [2026-08-22] ingest | 省 token 三招（ai-tooling，1/3）
- source 頁：[[2026-08-22_省token三招_context管理]]
- raw 檔：`raw/transcripts/2026-08-22_省token三招_context管理.md`
- 新建 concepts（1）：[[Prompt_Caching]]（快取折扣機制：省 10 倍、壽命 1hr、換模型/調思考強度會失效）
- 更新（2）：[[Context_工程]]（新增「四層 Context 結構」實戰拆解節）、[[Gary_Chen]]（2026-08-22 內容主軸）
- 工具狀況：開工前 notebooklm 認證再次過期（token_fetch 失敗），比對 PyPI 排除版本落後，確認為真過期，使用者跑 `login --fresh` 解決（PROGRESS D-014）

## [2026-08-22] ingest | 批次 3/3（j-PlWhTJVsc 失敗，Super Ace Deluxe 實錄）
- ❌ ai-tooling `j-PlWhTJVsc`（詞向量到 Transformer）：notebooklm source add 連續 2 次失敗（RPC rpc_code=9），疑來源端問題，已在 inbox.md 標註跳過，未中斷整批
- source 頁：[[2026-08-22_super_ace_deluxe_實錄]]（competitor-intel）
- raw 檔：`raw/transcripts/2026-08-22_super_ace_deluxe_實錄.md`
- 未新建 entity/concept：逐字稿僅為遊戲符號/音效報讀，無下注額、RTP、選房邏輯等機制資訊，資訊量不足以建立《Super Ace Deluxe》entity 頁（與既有 [[2026-05-16_戰神賽特2_選房技巧]] 同類型限制）
- 更新：[[index]]（統計待補）
- 本輪 3 支批次結果：1 支完整 ingest（省 token 三招）、1 支失敗跳過（詞向量到 Transformer）、1 支內容過薄僅存 source stub（Super Ace Deluxe）
