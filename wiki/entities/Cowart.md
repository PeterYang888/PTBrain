---
type: entity
entity_type: product
tags: [ai, codex, image-editing, plugin]
created: 2026-08-22
updated: 2026-08-22
sources: [2026-07-10_codex_cowart_修圖, 2026-07-10_ig_cowart_ai郵報]
---

# Cowart

> 2026-06 開源的 [[OpenAI_Codex]] 插件，開發者 zhongerxin。把 tldraw 畫布標註（箭頭/圈選/手寫指令）跟 gpt-image-1.5 生圖串成完整工作流，解決純文字修圖指令的位置/對象歧義問題。

## 關鍵事實
- 核心痛點：純文字描述修圖位置（如「左上標題改紅色」）常因「位置歧義」「對象歧義」而失敗，模型抓不準要改哪裡
- 操作流程：安裝插件到 Codex → 在原圖上用箭頭指位置、寫簡短動作指令 → 告訴 Codex 生成修訂版本 → 模型在畫布內直接生成乾淨版圖片
- 定位：中等修圖需求（改 3-5 個地方），效率介於 Midjourney（零創作）與 Photoshop（像素級精修）之間
- 適用場景：電商去背、換產品、改標題

## 與其他頁的關係
- 是 [[OpenAI_Codex]] 的插件生態一員，跟 [[2026-07-30_codex_plugin_cc]]（Claude Code 官方外掛）是不同性質的擴充——一個做圖片編輯，一個做程式碼審查/委派

## 相關來源
- [[2026-07-10_codex_cowart_修圖]] — AI郵報部落格文章，操作步驟與引言
- [[2026-07-10_ig_cowart_ai郵報]] — 同帳號 IG reel，caption 版本
