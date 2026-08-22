# PTBrain Inbox Ingest Prompt
# 使用方式：複製「=== PROMPT START ===」到「=== PROMPT END ===」之間的全部內容，貼進 Claude Code

=== PROMPT START ===

請處理 `inbox.md` 裡「## 待處理」區塊的所有 YouTube 連結。

---

## 執行規則

**順序**：從上到下逐一處理，一次處理一支，完成後才處理下一支。

**每支影片的完整流程**：

1. 讀取該筆的 URL 和 notebook 標記（`| ai-tooling` 之類）
2. 用 notebooklm skill 把影片加進對應的 notebook
3. 等來源處理完成後，產出繁體中文 briefing doc
   - 聚焦提示依 notebook 類型決定（見下方）
4. 將 briefing 下載後存到 `raw/transcripts/`
   - 檔名格式：`YYYY-MM-DD_影片標題slug.md`（底線，小寫）
5. 在檔案開頭加上 PTBrain frontmatter（見下方格式）
6. 執行標準 ingest 流程（CLAUDE.md 第 3.1 節）：
   a. 向我回報 2-4 個關鍵要點，確認方向
   b. 建立 `wiki/sources/` 對應頁（1:1）
   c. 盤點並更新相關 `wiki/entities/` 和 `wiki/concepts/`
   d. 更新 `index.md`
   e. 附加一筆到 `log.md`
7. 將 `inbox.md` 中該筆從「待處理」移到「已處理」，加上完成時間
8. 回報完成，等我確認後繼續下一支

**失敗處理**：若某支影片 notebooklm 失敗（逾時、來源無法處理等），
在 `inbox.md` 該筆後面標註 `❌ 失敗原因`，跳過繼續下一支，不要中斷整批。

---

## Frontmatter 格式（存進 raw/transcripts/ 時加在檔頭）

```yaml
---
type: source
tags: [依 notebook 對應填入，見下方]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_url: https://www.youtube.com/watch?v=xxx
source_date: YYYY-MM-DD
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: notebook名稱
  channel: "頻道名稱"
  processed_by: notebooklm-py
---
```

---

## Notebook 對應規則

| inbox 標記 | NotebookLM notebook | tags | briefing 聚焦提示 |
|---|---|---|---|
| ai-tooling | ai-tooling | [ai, claude-code, workflow] | 聚焦 Claude Code、MCP、agent、workflow automation。保留 CLI 指令、程式碼片段、設定範例。 |
| thinking | thinking-methods | [thinking, mental-model, reasoning] | 聚焦思維框架本身——如何拆解、如何應用、實際案例。保留具體提問模板與操作步驟。 |

---

## 進度回報格式

每支完成後回報：

```
✓ [序號/總數] 標題（前40字）
   notebook: ai-tooling
   raw 檔案: raw/transcripts/YYYY-MM-DD_slug.md
   wiki 新建: [[頁面1]], [[頁面2]]
   wiki 更新: [[頁面3]]
   → 繼續下一支？
```

---

## 開始前先做

0. **從瀏覽紀錄自動補齊 inbox.md**：
   a. 找 `C:\Users\user\Desktop\Downloads\` 底下**最新**的 `history.csv`（若有多個依檔案修改時間取最新一份）
   b. 讀取 CSV，找出網址欄位（實際欄名以檔案第一行 header 為準——目前版本欄名是「網址 (URL)」，標題欄是「標題」；瀏覽器版本或語言變了就依實際 header 調整，不要硬套死欄名）
   c. 篩選：只留 `https://www.youtube.com/watch?v=...` 或 `https://youtu.be/...` 這種**單一影片頁面**，排除搜尋結果頁（`youtube.com/results?...`）、頻道頁等非單一影片內容
   d. 依影片 ID 去重（同一支影片常有多筆瀏覽紀錄；ID 需處理 `watch?v=` 與 `youtu.be/` 兩種格式，忽略 query string）
   e. 二次去重：跟現有 `wiki/sources/*.md` 的 frontmatter `source_url` 比對（YouTube ID 正規化後比對），已存在的直接跳過；也跳過 `inbox.md`「已處理」區塊已經列過的連結
   f. 依標題內容判斷最貼近的 notebook 標記（對照下方「Notebook 對應規則」表），無法判斷就先標 `ai-tooling`
   g. 依 `inbox.md` 現有格式（`- URL | notebook標記` 換行加一句標題），把這些新項目加進「## 待處理」對應分類區塊——不要覆蓋或刪除既有的待處理項目，用附加的方式加進去
   h. 這一步不用另外跟我確認，直接做；補齊後的完整清單會在下面第 3 步一起列出來讓我確認
1. 讀 `inbox.md`，列出「待處理」的所有連結與數量
2. 確認 notebooklm skill 可用（`notebooklm status`）
3. 回報清單給我確認，我說「開始」後才執行

=== PROMPT END ===
