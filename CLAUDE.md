# PTBrain — LLM Wiki Schema

> 這份檔案是整個知識庫的「作業系統」。每次進入這個 vault 時，先讀完這份文件再做任何事。
> 使用者負責：提供資料、探索方向、提出問題。你（LLM）負責：讀、寫、整理、交叉引用、維護一致性。

---

## 1. 架構總覽（三層）

```
PTBrain/
├── CLAUDE.md          ← 你現在讀的這份。schema，不要自行修改，除非使用者同意
├── README.md          ← 給使用者看的入口說明
├── index.md           ← 內容導引（所有 wiki 頁面的目錄）
├── log.md             ← 時序記錄（ingest / query / lint）
│
├── raw/               ← ❶ 原始資料層（不可變 — 你只讀不寫）
│   ├── articles/      ← 網頁文章（Obsidian Web Clipper 或手動貼上）
│   ├── papers/        ← 論文、PDF 摘要
│   ├── notes/         ← 使用者手寫筆記、日誌
│   ├── transcripts/   ← Podcast、影片、會議逐字稿
│   └── assets/        ← 圖片、附件（Obsidian 下載的圖片會放這）
│
└── wiki/              ← ❷ Wiki 層（由你建立與維護）
    ├── sources/       ← 每份 raw 來源對應一頁摘要（1:1）
    ├── entities/      ← 具體的人、組織、產品、地點、事件
    ├── concepts/      ← 抽象概念、理論、方法、術語
    ├── topics/        ← 廣義主題頁（統合多個 entities + concepts）
    └── syntheses/     ← 綜合分析、比較、你被問到而值得保存的答案
```

**三層的角色（核心原則，不可違反）**

| 層                            | 誰寫？         | 修改規則                        |
| ---------------------------- | ----------- | --------------------------- |
| raw/                         | 使用者         | **不可變**。你只讀，絕不改動任何 raw 檔案內容 |
| wiki/                        | 你           | 你擁有這層。建立、更新、合併、重構都由你主動執行    |
| schema（CLAUDE.md / index.md） | 使用者 + 你（協作） | 需徵得使用者同意後才能修改 schema 約定     |

---

## 2. 檔案命名與連結規範

### 命名

- **用底線 `_` 而非空白**：`Vannevar_Bush.md`，不要 `Vannevar Bush.md`
- **中英混雜允許**：`大型語言模型.md`、`RAG_系統.md` 都可以
- **小寫英文、首字大寫中文**：`rag_systems.md`、`知識管理.md`（看哪個讀起來自然）
- **entities 用專有名詞本身**：`OpenAI.md`、`Tolkien.md`
- **concepts 用完整術語**：`retrieval_augmented_generation.md`、`向量資料庫.md`
- **sources 用「日期_簡短標題」**：`2026-04-02_memex_as_you_may_think.md`
- **syntheses 用「主題_分析類型」**：`rag_vs_wiki_比較.md`

### 連結

- 一律使用 Obsidian wiki-link 語法 `[[檔名]]` 或 `[[檔名|顯示文字]]`
- **盡量豐富地連結**。每個實體、概念第一次出現時務必加連結
- 反向連結會自動形成，不必手動維護
- 如果連結到的頁面還不存在，**也要加上連結**（stub link），之後再補頁面

### Frontmatter（YAML）

每個 wiki 頁面開頭加上 frontmatter，以便 Obsidian Dataview 查詢：

```yaml
---
type: entity | concept | topic | source | synthesis
tags: [標籤1, 標籤2]
created: 2026-04-17
updated: 2026-04-17
sources: [2026-04-02_memex, 2026-04-10_rag_paper]   # 僅 non-source 頁面
source_url: https://...                              # 僅 source 頁面
source_date: 2026-04-02                              # 僅 source 頁面
---
```

---

## 3. 工作流程（三種操作）

### 3.1 Ingest — 吸收新資料

當使用者說「請處理 raw/articles/xxx.md」或「幫我看這篇」：

1. **讀**：完整讀完 raw 檔案
2. **對話**：向使用者簡述 2–4 個關鍵要點，確認我抓到的重點對不對
3. **建立 source 頁**：在 `wiki/sources/` 建立對應摘要頁（見下方模板）
4. **盤點要更新的頁面**：這份來源涉及哪些 entity / concept / topic？
   - 已存在的頁面 → 更新（新增事實、補充引用、修正舊說法）
   - 不存在但重要 → 新建
   - 不存在但只是順帶提及 → 加 stub link，但不急著建頁
5. **更新 index.md**：新建的頁面加到目錄
6. **附加 log.md**：寫一條 ingest 記錄
7. **回報**：告訴使用者你碰了哪些頁面（條列 10–15 條都很正常）

### 3.2 Query — 回答問題

當使用者提問：

1. **先讀 index.md**：這是最便宜的路由方式
2. **鎖定相關頁面**：entity / concept / topic / synthesis
3. **需要時再下探 sources**：當需要原始引用或具體數據時
4. **綜合回答**：要有引用（用 `[[頁面名]]` 指向 wiki，而非 raw）
5. **提議歸檔**：若這個答案有價值（比較、分析、新發現的連結），**主動問使用者：「要不要把這個答案存成 wiki/syntheses/xxx.md？」** 這是讓探索累積的關鍵。
6. **附加 log.md**：記錄查詢與（若歸檔的話）產出的頁面

### 3.3 Lint — 健康檢查

當使用者說「lint」或「健檢」：

檢查項目：

- [ ] **矛盾**：不同頁面對同一事實說法不同？列出並建議修正
- [ ] **過時聲明**：較新的 source 已經蓋過舊結論？
- [ ] **孤立頁面**：沒有任何 inbound link 的頁面（graph view 裡會浮出來）
- [ ] **缺頁概念**：多處被提及但沒有自己的頁面
- [ ] **漏連結**：頁面中出現的重要名詞沒有 wiki-link
- [ ] **缺 frontmatter**：type / tags / dates 缺失
- [ ] **資料缺口**：可以透過網路搜尋補上的空白
- [ ] **建議新問題**：根據目前積累，有哪些值得探索的新方向

輸出一份報告（Markdown 清單），讓使用者勾選要採取的行動。

---

## 4. 頁面模板

### 4.1 Source 頁（wiki/sources/）

```markdown
---
type: source
tags: [...]
created: YYYY-MM-DD
source_url: https://...
source_date: YYYY-MM-DD
source_type: article | paper | transcript | note
---

# {{標題}}

> 來源：[原始檔]({{相對路徑到 raw/}}) · [[原作者 entity 頁]]

## 一句話摘要
（一句話講完）

## 核心論點
- 論點 1
- 論點 2
- 論點 3

## 值得引用的段落
> 「…」— 位置 / 頁碼

## 連結到的 wiki
- [[相關 entity]]
- [[相關 concept]]
- [[相關 topic]]

## 我的問題 / 待追蹤
- ?
```

### 4.2 Entity 頁（wiki/entities/）

```markdown
---
type: entity
entity_type: person | organization | product | place | event
tags: [...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [...]
---

# {{名稱}}

> 一行定位：是誰 / 是什麼 / 做過什麼

## 背景
...

## 關鍵事實
- 事實 1（來自 [[source 頁]]）
- 事實 2

## 與其他頁的關係
- 關聯 [[另一個 entity]]：...
- 屬於 [[topic]]

## 相關來源
- [[source 1]]
- [[source 2]]
```

### 4.3 Concept 頁（wiki/concepts/）

```markdown
---
type: concept
tags: [...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [...]
---

# {{概念名}}

> 精簡定義（1–2 句）

## 詳細說明
...

## 關鍵特徵 / 組成
- ...

## 與其他概念的差別
- 跟 [[concept X]] 的差別：...
- 跟 [[concept Y]] 的關係：...

## 應用 / 實例
- 在 [[entity A]] 中：...

## 爭議 / 未定論
- 有兩派觀點：... vs ...

## 來源
- [[source 1]]
```

### 4.4 Topic 頁（wiki/topics/）

頂層主題，像 wiki 的導航樞紐。列出屬於這個主題的所有 entities / concepts / syntheses。

### 4.5 Synthesis 頁（wiki/syntheses/）

使用者提問後值得保留的分析。比較表、時間軸、立場盤點、新發現的連結都適合放這。

---

## 5. index.md 的維護

`index.md` 是「按分類」的目錄（不是時序的，log.md 才是）。

結構如下：

```markdown
# Index

## Topics
- [[topic_a]] — 一行說明
- [[topic_b]] — 一行說明

## Entities
### People
- [[Vannevar_Bush]] — Memex 的提出者
### Organizations
- [[OpenAI]] — ...

## Concepts
- [[memex]] — ...
- [[rag]] — ...

## Syntheses
- [[rag_vs_wiki_比較]] — YYYY-MM-DD

## Sources
按時間倒序列最近 N 筆即可，完整列表交給 Obsidian 的檔案瀏覽器。
```

**每次 ingest 新增頁面，都要更新 index.md。** 這是便宜但高價值的工作。

---

## 6. log.md 的維護

**Append-only**。每筆以一致的 heading 開頭，方便 grep：

```markdown
## [YYYY-MM-DD] ingest | {{來源標題}}
- source 頁：[[2026-04-02_memex_as_you_may_think]]
- 新建：[[Vannevar_Bush]], [[memex]]
- 更新：[[知識管理]], [[index]]

## [YYYY-MM-DD] query | {{問題摘要}}
- 參考頁面：[[...]], [[...]]
- 產出：[[synthesis_xxx]]（若有歸檔）

## [YYYY-MM-DD] lint
- 發現 3 個矛盾 / 2 個孤立頁 / ...
- 已修：...
```

用 `grep "^## \[" log.md | tail -10` 可以快速看近期活動。

---

## 7. 圖片與附件

- Obsidian 設定把圖片存到 `raw/assets/`（附件資料夾路徑）
- Markdown 裡嵌入圖片用 `![[image_name.png]]` 即可
- 你（LLM）**一次只能讀文字或圖片之一**。處理有圖片的 source 時：先讀文字，必要時再單獨 view 圖片補上下文
- 圖片不要複製到 wiki/，wiki 只放 markdown 和 wiki-link。要引用圖片時用 `![[raw/assets/xxx.png]]`

---

## 8. 規模與工具升級路徑

- **< 50 sources**：index.md 就夠了，不需任何搜尋工具
- **50–200 sources**：開始用 Obsidian 內建搜尋 + graph view；可以考慮 Dataview plugin 做動態查詢
- **> 200 sources**：考慮裝 [qmd](https://github.com/tobi/qmd) 做 BM25 + 向量搜尋；或寫個小 script。**到那一步再講**，不要現在就過度工程

---

## 9. 風格守則

- **寫作簡潔、資訊密度高**。Wiki 是查閱用，不是閱讀用
- **不杜撰**。沒有 source 支持的主張一律不寫；若是你的推測，明確標註「（推測）」
- **引用要具體**。不要只寫「根據某文章」，要 `[[2026-04-02_memex]]`
- **承認不知道**。用 `TODO:` 或 `?` 標註待補的空白
- **中英夾雜可以**。看哪個詞最精準就用哪個，不要為了「全中」而翻得很拗口

---

## 10. 跟使用者協作的節奏

- 使用者偏好：**一次處理一份 source，過程中保持互動**（非批次靜默處理）
- ingest 過程主動回報：「我打算碰 A / B / C 頁，對嗎？」
- query 後主動問：「這個答案要不要存成 synthesis？」
- 不確定時**問**，不要猜
- 使用者用中文，你也用中文回；但 wiki 內容語言以 source 原文為主（中文 source → 中文頁，英文 source → 英文頁，兩者混合時以中文為主）

---

## 11. 啟動檢查

每次 session 開始，先看：

1. `index.md` — 目前有什麼
2. `log.md` 最後 5 筆 — 最近做了什麼
3. `raw/` 有沒有新檔案還沒 ingest

然後等使用者指示。





## 12. 快捷指令

- **`ingest inbox`**：讀 `_meta/prompts/inbox_ingest.md`，執行其中的完整流程
- **`ingest raindrop`**：讀 `_meta/prompts/raindrop_ingest.md`，執行其中的完整流程（從 Raindrop.io 的 `#ptbrain` 標籤拉書籤 ingest）
