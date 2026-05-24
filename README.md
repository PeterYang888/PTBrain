# PTBrain

個人知識庫，由 LLM 協同維護。基於 [LLM Wiki 模式](./CLAUDE.md) 建置。

## 這是什麼

不是 RAG。不是聊天記錄。是一個**持續累積、交叉連結的 markdown wiki**，由你提供資料與方向，由 LLM 負責讀、寫、整理、交叉引用與維護一致性。

## 如何使用

### 1. 準備 Obsidian 環境
- 這個資料夾本身就是一個 Obsidian vault，直接用 Obsidian 開啟即可
- 建議裝的 plugin：
  - **Obsidian Web Clipper**（瀏覽器擴充）— 把網頁一鍵存成 markdown 到 `raw/articles/`
  - **Dataview** — 根據 frontmatter 生成動態清單
  - **Marp**（選配）— 從 wiki 頁面直接產簡報

### 2. 加資料到 `raw/`
- 網頁文章 → `raw/articles/`
- 論文 / PDF 摘要 → `raw/papers/`
- 手寫筆記 / 日誌 → `raw/notes/`
- 逐字稿 → `raw/transcripts/`
- 圖片 → `raw/assets/`（Obsidian 會自動處理）

**`raw/` 是不可變的原始資料。** LLM 只讀不改。

### 3. 叫 LLM 處理
三種操作：

- **Ingest**：「請處理 `raw/articles/xxx.md`」 → LLM 讀完、討論要點、寫 source 頁、更新相關 entity / concept 頁、更新 index 與 log
- **Query**：「RAG 跟 wiki-based 記憶的差別？」 → LLM 查詢 wiki，給有引用的答案；若值得保留，會問你要不要存成 synthesis
- **Lint**：「健檢一下」 → LLM 找矛盾、孤立頁、缺頁概念，給你一份可勾選的修補清單

### 4. 讀 wiki
`index.md` 是入口。Obsidian graph view 是最好的總覽工具。

## 目錄結構

```
PTBrain/
├── CLAUDE.md       ← LLM 的操作手冊（最重要的一份）
├── README.md       ← 你現在讀的
├── index.md        ← wiki 目錄（按分類）
├── log.md          ← 時序記錄（append-only）
├── raw/            ← 原始資料（不可變）
└── wiki/           ← LLM 維護的知識庫
    ├── sources/    ← 每份 raw 對應一頁
    ├── entities/   ← 人、組織、產品、地點、事件
    ├── concepts/   ← 概念、理論、方法
    ├── topics/     ← 廣義主題（樞紐頁）
    └── syntheses/  ← 分析、比較、探索的歸檔
```

## 核心原則

- **raw/ 不可變** — LLM 絕不修改原始資料
- **wiki/ 由 LLM 擁有** — 你不用自己寫，提 feedback 就好
- **連結豐富** — 所有相關實體一律 `[[wiki-link]]`
- **累積而非重算** — 每次 ingest 讓 wiki 變得更密、更準

## 下一步

1. 打開 Obsidian，開啟這個 vault
2. 丟一兩篇文章到 `raw/articles/`
3. 跟你的 LLM 說：「請處理 `raw/articles/xxx.md`」
4. 看 wiki/ 開始長出來
