# PTBrain Raindrop Ingest Prompt
# 使用方式：複製「=== PROMPT START ===」到「=== PROMPT END ===」之間的全部內容，貼進 Claude Code
# 觸發詞：`ingest raindrop`

=== PROMPT START ===

請處理 Raindrop.io 上標籤為 `ptbrain` 的所有書籤。

---

## 0. 前置準備

**Token**：讀 `C:\Users\user\.raindrop_token`，跳過 `#` 開頭的註解行與空白行，取第一個非空行當 token。**絕對不要**把這個檔案的內容複製進任何 PTBrain repo 內的檔案（含 commit）。

**API 呼叫**：
```
GET https://api.raindrop.io/rest/v1/raindrops/0?search=%23ptbrain&perpage=50&page=N
Authorization: Bearer {token}
```
分頁直到某頁 `items` 為空。收集所有項目的 `_id`, `link`, `title`, `excerpt`, `note`, `type`, `tags`, `created`, `domain`。

---

## 1. 去重檢查（每支都要做，避免跟現有 wiki 重複）

Raindrop 上的書籤可能早就透過別的管道（手動貼、`ingest inbox`）ingest 過。對每一筆：
- 若是 YouTube 連結：從 `link` 中抽取影片 ID（處理 `youtu.be/{id}` 與 `youtube.com/watch?v={id}` 兩種格式，忽略 query string 如 `?si=...`）
- 用這個 ID／或原始網域+路徑，grep `wiki/sources/*.md` 的 frontmatter `source_url:` 欄位是否已有相符項目
- **已存在** → 跳過，不重複建立 source 頁；直接把這筆的 `ptbrain` 標籤移除（視為已處理），在報告中列為「已存在，僅移除標籤」
- **不存在** → 進入下一步分流處理

---

## 2. 依 type + domain 分流

### 2a. YouTube 影片（`type: video`，domain 為 youtube.com / youtu.be）
不重新實作 YouTube 抽取邏輯——**併入現有 `inbox.md` 流程**：
1. 依標題/note 內容判斷最貼近的 notebook 標記（`ai-tooling` / `competitor-intel` / `slot-math` / `team-management` / `thinking`，對應表見 `_meta/inbox_ingest_prompt.md` 的「Notebook 對應規則」）。無法判斷就先標 `ai-tooling`
2. **先把這一批（連同猜測的 notebook 標記）列給使用者看一次，確認或修正後才動手**——這跟 `ingest inbox` 開跑前的確認習慣一致，只在批次開始前問一次，之後不再中途詢問
3. 確認後，把這些項目依格式（`- URL | notebook標記`）加進 `inbox.md` 的「## 待處理」對應分類
4. 呼叫 `ingest inbox` 的完整流程（`_meta/inbox_ingest_prompt.md`）處理這些新加入的項目
5. 全部處理完後，把這些項目在 Raindrop 上的 `ptbrain` 標籤移除

### 2b. 文章／連結（`type: link`，domain 非社群媒體，如 github.com、hackmd.io 等）
不需要 Jina Reader 或額外套件——直接用 **WebFetch** 抓正文：
1. WebFetch `link`，取得正文內容
2. 存成 `raw/articles/YYYY-MM-DD_slug.md`（`YYYY-MM-DD` 用 Raindrop 的 `created` 日期），frontmatter 依 CLAUDE.md 第 4 節格式，`source_type: article`
3. 走 CLAUDE.md §3.1 一般 ingest 流程：回報要點 → 建 `wiki/sources/` 頁 → 盤點更新 entity/concept/topic → 更新 `index.md` → append `log.md`
4. 完成後移除該筆的 `ptbrain` 標籤

### 2c. 社群媒體貼文（domain 為 instagram.com、facebook.com，`type` 通常是 `image`）
**第一版只做 caption-only stub**，不做 Playwright 截圖或 vision 讀圖：
1. 直接用 Raindrop API 已回傳的 `excerpt`（貼文說明文字）、`note`（使用者自己在 Raindrop 上寫的備註，若有）、`link`、`created` 建立一個精簡 source 頁——不另外抓 raw 檔，因為能拿到的內容就只有這些
2. frontmatter `source_type: social`，內容誠實標註「僅有 caption，未讀取圖片/影片內容」
3. 若 `excerpt` 太短或無實質資訊（例如只有讚數留言數），可比照 D 類失敗處理：標成內容過薄的 stub，不強行分析
4. 完成後移除該筆的 `ptbrain` 標籤

---

## 3. 失敗處理

單筆失敗（WebFetch 拿不到內容、API 錯誤等）不中斷整批：在報告中列出失敗原因，該筆的 `ptbrain` 標籤**保留**（下次再試），不要移除。

---

## 4. 移除標籤的做法

```
PUT https://api.raindrop.io/rest/v1/raindrop/{_id}
Authorization: Bearer {token}
Body: {"tags": [<原本的 tags 陣列，去掉 "ptbrain">]}
```
注意：單筆操作的端點是**單數** `raindrop`（不是 `raindrops`），跟第 0 節列表用的複數端點不同，兩者搞混會回 404。

---

## 5. 進度回報格式

```
Raindrop ingest 完成：
- 共 N 筆帶 #ptbrain 標籤
- M 筆已存在於 wiki，僅移除標籤
- K 筆 YouTube → 併入 inbox.md，交給 ingest inbox 處理（見該次報告）
- J 筆文章 → 新建 source：[[...]], [[...]]
- I 筆社群貼文 → 新建 stub source：[[...]]
- F 筆失敗，標籤保留待重試：<原因>
```

=== PROMPT END ===
