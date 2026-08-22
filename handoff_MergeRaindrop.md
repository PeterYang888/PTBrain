# Handoff: Raindrop → PTBrain 知識管線（Karpathy Compile Loop）

> 目標：把 Raindrop 儲存的知識（Instagram 貼文、網路文章、YouTube）蒸餾進 PTBrain Obsidian vault，
> 之後任何問題先問 vault，回答附知識點 + 原始連結。
> 設計哲學（Karpathy）：不用向量資料庫、不用 fancy RAG——全部蒸餾成 Markdown，agent 用全文搜尋（grep）檢索。

---

## 1. 整體架構：兩條 Loop

### Compile Loop（定期 ingest）
```
Raindrop API → 依 type 分流抽取 → raw 存檔 → LLM 蒸餾 → compiled 知識筆記進 vault
```

### Query Loop（隨問隨答）
```
使用者提問
  → grep compiled 層（知識點、標題、tags）
    → 命中：回答知識點 + 原始連結
    → 未命中：grep _raw/ 層（蒸餾可能漏了細節）
      → 仍未命中：打 Raindrop API search 找還沒 ingest 的書籤
        → 有：詢問是否現場 ingest，ingest 完再回答
        → 無：明說知識庫裡沒有
```

---

## 2. Vault 目錄結構（兩層設計）

```
PTBrain/
├── Raindrop/                    # compiled 層：查詢對象，出現在 Obsidian graph
│   ├── slot-cascade-mechanics.md
│   └── ...
└── _raw/
    └── raindrop/                # raw 層：編譯原料，搜尋預設排除
        ├── {raindrop_id}-transcript.md
        ├── {raindrop_id}-article.md
        └── {raindrop_id}-ig/    # IG caption + 圖片
```

**分層理由（實作時不要合併）：**
1. Grep 命中品質——raw 逐字稿會產生大量雜訊命中，淹掉知識點。`_raw/` 底線前綴讓搜尋 script 預設排除。
2. 可重新編譯——蒸餾 prompt 迭代後，重跑 compile 即可，不用重抓來源。IG 來源隨時消失，raw 就是永久副本。
3. Vault 乾淨度——Obsidian 設定排除 `_raw/`，graph view 只留知識筆記。

`_raw/` 放在 vault 內部（一個 working directory 全包），用 Obsidian 的 Excluded files 設定排除索引。

---

## 3. 資料源與抽取策略

### Raindrop API
- Token：app.raindrop.io/settings/integrations → 建 app → test token（個人用免 OAuth）
- 主要 endpoints：
  - `GET /rest/v1/raindrops/0` — 全部書籤（0 = all collections），分頁 `perpage=50&page=N`
  - `GET /rest/v1/raindrops/0?search={query}` — Query loop 的 fallback 搜尋
- 每筆取：`_id`, `link`, `title`, `excerpt`, `tags`, `collection`, `created`, `type`
- 增量同步：本地存 `last_sync` timestamp（如 `.raindrop-sync.json`），只拉 `created > last_sync` 的項目

### 依 type 分流

| 來源 | 抽取方式 | 備援 |
|------|---------|------|
| 網路文章 | fetch + readability 抽正文；或 Jina Reader `https://r.jina.ai/{url}` | Raindrop Pro permanent copy |
| YouTube | `yt-dlp --write-auto-sub` 或 `youtube-transcript-api` 抓字幕逐字稿 | 無字幕 → 存 metadata + 描述，標記 `needs_manual` |
| Instagram | `gallery-dl` 抓 caption + 圖片 | 抓不到 → Playwright 截圖 + Claude vision 讀圖（複用 RiskScreen_Auto 的 Playwright 基礎）。第一版先降級：只存 caption + 連結 |

---

## 4. 蒸餾格式（Compile 步驟核心）

每個書籤 → 一張 compiled 筆記：

```markdown
---
source: https://原始連結
type: youtube | article | instagram
raindrop_id: 12345
raw: _raw/raindrop/12345-transcript.md
tags: [slot-math, cascade]
ingested: 2026-08-22
---
# 標題

## 知識點
- 一句話一個 point
- 用「未來的你會怎麼問」的語言寫，中英術語都埋進去（grep 是字面比對，同義詞要寫出來）

## 摘要
（3-5 句）
```

**蒸餾 prompt 要求：**
- 知識點必須可獨立被搜到（self-contained，不依賴上下文）
- 中英混寫關鍵術語（例：「級聯消除 cascade / tumble 機制」）
- 檔名用語意化 slug，不用 raindrop_id
- 保留 frontmatter `raw:` 指回原料，方便重編譯與溯源

---

## 5. 要建的兩個 Skills

### Skill A: `raindrop-ingest`
觸發詞：「ingest raindrop」「同步 raindrop」「跑 raindrop 匯入」

流程：
1. 讀 `.raindrop-sync.json` 的 `last_sync`
2. 拉新書籤（分頁處理）
3. 依 type 分流抽取 → 寫入 `_raw/raindrop/`
4. 逐篇蒸餾 → 寫入 `PTBrain/Raindrop/`
5. 更新 `last_sync`；輸出本次 ingest 報告（成功/失敗/needs_manual 清單）

錯誤處理：
- 單篇抽取失敗不中斷整批，記入報告
- IG 抓取失敗 → 降級存 caption/excerpt + 連結，標記 `partial: true`

排程：可掛 Windows 登入自動執行（與 performance-review 同機制），或每週手動跑。

### Skill B: `ptbrain-ask`
觸發詞：「問 ptbrain」「知識庫裡有沒有…」或任何知識查詢

流程（三層 fallback，見第 1 節 Query Loop）：
1. grep `PTBrain/Raindrop/`（排除 `_raw/`）：搜標題、知識點、tags
2. 未中 → grep `_raw/raindrop/`
3. 仍未中 → `GET /rest/v1/raindrops/0?search={keywords}` → 有結果詢問是否現場 ingest

回答格式：知識點條列 + 每點附 `[原文連結](source)`；來自 raw 層的命中要註明「來自逐字稿，尚未蒸餾成知識點」。

---

## 6. 實作順序

1. **Raindrop API 連通**：拿 token，寫 `fetch_raindrops.py`（或 ts），確認能分頁拉全量 + 增量
2. **文章管線**（最簡單，先打通端到端）：抽取 → raw → 蒸餾 → compiled，跑 10 篇驗證格式
3. **YouTube 管線**：yt-dlp 字幕，整併現有 YouTube → NotebookLM 流程（不要維護兩套）
4. **批次清存量**：全量跑一次（幾百篇約一個晚上），檢查 needs_manual 清單
5. **`ptbrain-ask` skill**：三層 fallback 檢索
6. **IG 管線**：先 caption-only 降級版，穩定後再上 Playwright + vision
7. **排程化**：Windows 登入 hook 或 weekly

## 7. 待確認（實作前補齊）

- [ ] Raindrop 書籤總量（影響批次策略）
- [ ] 是否有 Raindrop Pro（決定文章抽取走 permanent copy 或 Jina Reader）
- [ ] Vault 絕對路徑 & `Raindrop/` 資料夾命名是否沿用
- [ ] 蒸餾用的 model / API（Claude Code 內建 or 另掛 API key）
