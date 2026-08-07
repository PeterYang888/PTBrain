---
type: entity
entity_type: product
tags: [ai, agent, open-source, self-hosted]
created: 2026-08-08
updated: 2026-08-08
sources: [2026-08-08_ocuclaw_even_g2_ai_agent, 2026-06-19_loop_engineering]
---

# OpenClaw

> [[Peter_Steinberger]] 創立的自架 AI Agent 系統：跑在自己電腦上、能操作本機檔案／信件／工具的個人 Agent，以 skill 擴充、以 gateway 對外服務。

## 背景
在 [[2026-06-19_loop_engineering]] 中，Peter Steinberger 被列為 OpenClaw 創始人，與 [[Boris_Cherny]]、Addy 並列討論 [[Loop_Engineering]]，但當時未展開專案細節。[[2026-08-08_ocuclaw_even_g2_ai_agent]] 是本 vault 第一份具體描述其安裝與運作的來源。

## 關鍵事實
- **自架 + 本機操作**：Agent 跑在使用者自己的電腦上，可讀取本機檔案、電子郵件、聯絡人，並執行長流程自動化——與「只會報天氣」的雲端語音助理有本質差別
- **安裝**：Windows 走 PowerShell（`docs.openclaw.ai/install`），安裝程式會自動偵測並補裝 **Git** 與 **NodeJS**
- **skill 機制**：在對話框直接下 `install the <name> skill` 安裝；官方商城稱 **Clawhub**，收錄經認可的 skill
- **gateway**：對外服務的常駐元件，用 `openclaw gateway status` / `openclaw gateway restart` 管理
- **版本編號用日期制**：如 `2026.6.9`（OcuClaw skill 要求的最低版本）
- **已知穩定度問題**：會出現 Session 衝突（`reply session initialization conflicted for agent main`），需手動重啟或開新 Session
- 語音管線可外掛第三方 speech-to-text provider，成本極低（重度使用月付約 13–15 美分）

## 與其他頁的關係
- **OcuClaw skill** 把 OpenClaw 接上 [[Even_Realities_G2]]，讓 Agent 住進眼鏡（詳見 [[2026-08-08_ocuclaw_even_g2_ai_agent]]）；遠端連線靠 [[Tailscale]]
- 與 [[Claude_Code]] 的 G2 Terminal 模式是**同一需求的兩條路線**：前者是通用自架 Agent，後者是直連編碼工具（見 [[2026-06-27_even_g2_claude_code]]）
- 屬於 [[Agentic_Workflow]] / [[Loop_Engineering]] 的自架實作路線
- skill 擴充模型與 [[Skill_輕量化]] 討論的 Claude Skill 機制同構

## 相關來源
- [[2026-08-08_ocuclaw_even_g2_ai_agent]] — 完整安裝流程與實測
- [[2026-06-19_loop_engineering]] — 創始人脈絡

## 待追蹤
- 授權方式、repo 位置、是否真為開源（名稱含 "Open" 但來源未證實）— TODO
- 支援哪些模型後端？影片只說「your AI model」，未指名
- macOS / Linux 安裝路徑（來源只示範 Windows）
