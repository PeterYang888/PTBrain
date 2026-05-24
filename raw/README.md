# raw/ — 原始資料層

**不可變。** LLM 只讀，不改寫任何檔案內容。

## 子目錄

| 目錄 | 放什麼 |
|---|---|
| `articles/` | 網頁文章（Obsidian Web Clipper 匯出的 markdown） |
| `papers/` | 論文全文 / 摘要 / PDF 轉 markdown |
| `notes/` | 你自己手寫的筆記、日記、心得 |
| `transcripts/` | Podcast、影片、會議逐字稿 |
| `assets/` | 圖片、附件（Obsidian 會自動下載到這裡） |

## 命名建議
- 日期開頭方便排序：`2026-04-17_標題.md`
- 來源網址可以放在 frontmatter 的 `source_url`
- 不需要太工整，LLM 進 wiki/ 時會重新命名與摘要
