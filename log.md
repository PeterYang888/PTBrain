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
