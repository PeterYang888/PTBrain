---
type: source
tags: [tool, markdown, local-first]
created: 2026-06-04
updated: 2026-06-04
source_url: https://github.com/craig7351/bookMDViewer
source_date: 2026-06-04
source_type: article
source_extra:
  platform: github
  processed_by: WebFetch
---

## 核心用途
輕量級 Markdown 檢視器與編輯器（Windows／macOS／Linux），雙擊 `.md` 檔案直接開啟渲染。

## 主要功能
- 即時編輯與預覽：分割編輯器、左右同步捲動
- 自動大綱生成：依標題建立可導覽的 TOC 側欄
- 程式碼語法高亮、Mermaid 圖表支援
- HTML 匯出：產生自包含的單一檔案
- 檔案監看：存檔後自動重新渲染
- 搜尋功能與鍵盤快捷鍵

## 技術棧
- Tauri v2 框架（系統內建 WebView，非 Chromium）
- markdown-it（GFM 渲染）、highlight.js（語法高亮）、DOMPurify（安全性）

## 與其他工具的差異
不同於 Obsidian 等雲端筆記應用，強調「完全本機、無遙測、離線運作」，執行檔僅約 4 MB，記憶體耗用約 30-60 MB。適合單純檢視與編輯本地 Markdown 檔，不做知識管理/連結圖譜。
