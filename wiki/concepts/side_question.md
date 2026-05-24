---
type: concept
tags: [claude-code, ui-feature]
created: 2026-04-17
updated: 2026-04-17
sources: [2026-04-15_claude_code_desktop_routines改版]
---

# 側邊提問 / side question（`/btw`）

> [[Claude_Code]] 桌面 app 2026-04-14 改版引入的功能。透過 `/btw` 指令在不中斷主任務的情況下快速查詢問題。

## 運作方式
- 讀取**當前對話的完整上下文**
- **不呼叫工具**、**不影響主執行緒進度**
- 即使 Claude 正在處理主任務也能使用

## 為什麼重要
對應「多線並行」的工作流想像：開發者在等主任務跑的空檔，還想隨手問 Claude 小問題（例：這段程式碼做什麼？某個 API 怎麼用？）。以往要開新 session 或打斷當前，`/btw` 消除這個摩擦。

## 待追蹤
- 支援跨 session 嗎？（目前描述只提到「當前對話」）
- Token 計入主 session 還是獨立計？
- CLI 是否也支援？

## 相關來源
- [[2026-04-15_claude_code_desktop_routines改版]]
