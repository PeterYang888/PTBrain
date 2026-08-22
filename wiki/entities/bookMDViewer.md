---
type: entity
entity_type: product
tags: [tool, markdown, local-first]
created: 2026-08-22
updated: 2026-08-22
sources: [2026-06-04_bookmdviewer]
---

# bookMDViewer

> 輕量本機 Markdown 檢視/編輯工具（Windows／macOS／Linux），雙擊 `.md` 檔案直接開啟渲染。開發者 craig7351，開源。

## 關鍵事實
- 功能：即時編輯與預覽（左右同步捲動）、自動大綱 TOC、Mermaid 圖表支援、HTML 匯出、檔案監看自動重渲染
- 技術棧：Tauri v2（系統內建 WebView，非 Chromium）+ markdown-it + highlight.js + DOMPurify
- 體積：執行檔約 4 MB，記憶體耗用約 30-60 MB
- 定位：完全本機、無遙測、離線運作——單純檢視/編輯，不做知識管理或連結圖譜

## 與其他頁的關係
- 跟 PTBrain 用的 Obsidian 走不同路線：Obsidian 提供 wiki-link 圖譜與雙向連結，bookMDViewer 純粹是輕量檢視器，兩者是互補而非競爭關係（前者做知識庫，後者做單檔快速檢視）

## 相關來源
- [[2026-06-04_bookmdviewer]]
