---
type: source
tags: [ai, claude-code, workflow]
created: 2026-08-15
updated: 2026-08-15
source_url: https://www.youtube.com/watch?v=E8Bx9OlpmdM
source_date: 2026-08-15
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "Gary Chen"
  processed_by: notebooklm-py
---

# 你以為 Claude 降智，其實是你少設了這個

## 一句話摘要
這支影片介紹了如何透過 Claude Code 內建與自定義的 `output style`（輸出風格）功能，控制 AI 輸出的「技術密度」與「溝通語氣」，藉此消除高難度模型（如 Opus 5）所帶來的「囉唆與天書感」認知負荷。

## 主講者背景
- 主講者：Gary Chen，頻道名稱同為 Gary Chen。
- 影片中未提及是否為業配、自費或使用時長。立場偏向「實戰乾貨派」，主張用工程思維（如航太業 STE100 標準）有系統地管理 AI 的溝通方式。

## 核心論點
- **AI 降智實為溝通語境失配**：模型（如 Opus 5）在 Benchmark 分數變高，但實際用起來卻更累。這並非模型變笨，而是表達方式變得冗長、術語密集、充滿黑話，造成認知負荷。
- **Output Style 能規範表達格式**：調整「說話的說明書」（output style），可以在完全不影響 AI 程式碼編寫與推導能力的前提下，強制規範其簡報與報告格式。
- **依專案熟悉度與疲憊感動態切換**：output style 屬於專案層級設定，存在每個專案的 settings local 中。應依專案熟悉度、任務緊急度或當下疲憊程度靈活切換。
- **針對不同背景量身定制規則**：控制 AI 囉唆不能只用「講簡單點」這種模糊指令；影片將人群劃分為「純技術小白」「Vibe Coder / PM」「專業工程師」，分別套用結構化規則。
- **技術溝通管理由來已久**：可引入歐洲航太工業數十年前制定的 STE100（Simplify Technical English）標準，透過短句、單一動詞與固定詞義來馴服 AI。

## 關鍵細節與數據
**內建 4 套 output style**：
- `default`：簡潔有效率（預設）。
- `proactive`：行動派，能動手就直接動手，極少廢話與討論。
- `learning`：故意留白一小段程式碼供使用者親手編寫，適合練習。
- `explanatory`：每個改動都詳細解釋架構設計與 pattern，適合不熟的專案、repo 或新框架。

**設定自定義 style（以 Lia Hy 的「I5／Explain like I'm five」為例）**：
1. 複製 output style 文字。
2. 貼給 Claude，說「幫我把這個加進 output style」。
3. 輸入 `/config`。
4. 輸入 `output`，在清單找到 `output style`，選 `I5` 並 Enter。

**建立專屬風格**：收到看不懂的輸出時，輸入 `/branch` 從當前對話分支出新對話，要求 AI 用 5 種不同風格重寫該回覆，選定後做成自定義 output style。

**檔案存儲位置**：output style 存在每個專案的 `settings local`（專案本地設定）中，A 專案掛 A 風格、B 專案掛 B 風格互不影響。

**自定義 3 套 output style 的設計規則**：
1. 純技術小白（「技術翻譯機」）：術語每次出現都用白話＋生活比喻解釋（如 API 像餐廳服務生）；遇到刪除、花錢、動到正式環境的動作，必須先白話警告，確認後才動手。
2. Vibe Coder / PM（「STE100 簡報版」）：句子短、主動語態、一詞一意；API/前後端/資料庫等基礎詞不解釋，微觀細節（migration、condition）第一次出現給一行解釋；每個改動講清動到哪個功能，決策時排成 tradeoff 對比並給建議。
3. 專業工程師：像桌邊同事說話，先講改了什麼、能不能動，細節除非主動追問才給；未經詢問的高風險判斷必須放在第一句，不准藏在報告最後。

**其他術語**：
- STE100：簡化技術英文標準，句子短、一動作一句、一詞一意。
- `I5`（Explain like I'm five）：Lia Hy（Claude Code 團隊工程師）分享的風格，用於腦力疲憊時要求極簡總結。

## 重要引言
> 「Opus 5 可能只是講話的方式跟你對不上了，並不是他變笨。」

> 「output style 改變了之後，他跟你說話的方式，他寫程式碼的能力完全不受影響。」

> 「技術文件寫到沒人看得懂，並不是 AI 時代才出現的問題，而是工程界幾十年前就付出過代價，並且已經解決過的老問題。」

> 「要治 AI 的囉唆，光跟他說講簡單一點是沒有用的，他只會把長廢話換成短廢話，真正有效的方法是你要把你喜歡的溝通方式精煉成原則。」

## 與其他 AI 工具/概念的關聯
- **Claude Code**：output style 是其內建功能，用於在與模型（如 Opus 5）頻繁多工協作時降低認知負擔。
- **Matt Pocock（MPO）的「W」Skill**：與長駐的 output style 不同，MPO 寫了一個叫「W」的 skill，AI 開始講天書時才臨時召喚，用 STE100 標準＋專案詞彙重講一次，屬於「按需採用」的翻譯功能，與 output style 互補。

## 連結到的 wiki
- [[Claude_Code]]
- [[Gary_Chen]]
- [[Output_Style]]
- [[STE100]]
- [[Matt_Pocock]]

## 我的問題 / 待追蹤
- ?
