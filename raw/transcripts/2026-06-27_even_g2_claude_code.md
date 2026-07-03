---
type: source
tags: [ai, ai-glasses, claude-code, codex, workflow]
created: 2026-06-27
updated: 2026-06-27
source_url: https://www.youtube.com/watch?v=-FszxC5q400
source_date: 2026-06-27
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "トバログ (Tobalog)"
  processed_by: notebooklm-py
---

# 【Tobalog】Even G2 智慧眼鏡 × Claude Code 終端模式：隨處工作活用法

## 一句話摘要
透過 Even G2 智慧眼鏡的「終端模式（Terminal Mode）」遠端連接電腦端的 Claude Code 或 Codex，實現隨時隨地透過語音操作 AI 進行自動化工作流與程式開發，解放了必須守在電腦前的地理限制。

## 頻道/主講者背景
主講者為 YouTube 頻道「トバログ (Tobalog)」的主理人，是一位科技產品愛好者與創作者，擅長分享各類 Gadget 的深度評測與生活應用，並出版過エッセイ（隨筆）集《Tobalog_Paper》探討對物品的喜愛。

## 核心論點
- **解放地理束縛的 AI 協作**：解決了使用 Claude Code 進行開發時，因需要頻繁按下「授權/確認（approve）」按鈕而導致使用者被「鎖死」在電腦前的痛點。
- **智慧眼鏡的「殺手級應用」**：將眼鏡定位為電腦端強大 AI 模型（Claude Code / Codex）的行動介面，這比單純的翻譯或導航更具實用價值。
- **系統級的操作能力**：透過眼鏡端輸入語音，可間接操控電腦內的 Notion、Chrome、Office、以及專業剪輯軟體 DaVinci Resolve。
- **工具無關性的遠端連結**：利用 VPN 技術建立虛擬空間，讓使用者在全球任何地方只要有網路，就能喚醒家中的電腦進行任務。

## 關鍵細節與數據
- **硬體設備與價格**：
  - **Even Realities G2 (Even G2)**：由前 Apple Watch 開發成員設計，外觀極薄，搭載綠色單色投影顯示器，價格約 **10 萬日圓**。
  - **操作環 (Ring)**：專屬觸控配件，價格約 **4 萬至 5 萬日圓**，支援捲動、タップ（點擊）操作，並內建血氧與睡眠監測。
- **軟體安裝與設定**：
  - 電腦端需預裝 **Node.js** 與 **npm**。
  - 需安裝 `claude-code` CLI 工具以及 `even-terminal` 套件。
  - **CLI 指令**：在終端機輸入 `even-terminal` 會生成一個 **QR Code**，用於與手機 App 掃描配對。
- **遠端連接技術**：
  - **Tailscale**：用於建立虛擬網域，免費版最多支援 **100 台**設備連接。
  - 只要家中電腦電源開啟且未進入「睡眠模式」，即可透過行動網路實現遠端連接。
- **模型與功能**：
  - 對接 Claude 的最頂級模型及 Codex。
  - 語音辨識具備驗證機制，可在發送給 AI 之前，於眼鏡螢幕上確認文字是否正確。

## 值得引用的金句
- 「這簡直就是智慧眼鏡的殺手級應用（Killer App）。」——主講者形容將 Even G2 與 Claude Code 結合後的實用性。
- 「這讓我覺得像 iPhone 第一次連接到網路、或是 App Store 剛展開時那樣震撼。」——主講者形容透過眼鏡終端操作家中的 AI 系統。
- 「即便人在外頭散步或去便利商店買咖啡，家裡的 AI 依然在為你工作。」——主講者描述行動化 AI agent 對生產力的改變。

## 與其他 AI 工具/概念的關聯
- **Claude Code & Codex**：作為核心的 AI Agent，負責處理本地文件、讀取數據並執行實際的自動化操作。
- **Agentic Workflow & Vibe Coding**：本系統實踐了即使人不在電腦前，也能透過語音維持「氛圍編程（Vibe Coding）」的開發流，將人類角色轉向高層級的「決策者」而非「操作者」。
- **Notion 整合**：透過 AI 代理人讀取 Notion 的影片構成案，並將眼鏡端的對話摘要自動寫回 Notion 頁面。
- **專業軟體自動化**：展示了 AI 如何透過眼鏡指令，自動調用 DaVinci Resolve 的原生文字轉字幕功能，並由 AI 進行後續的內容微調。
- **VPN 與遠端存取**：結合 Tailscale，將傳統的「本地開發環境」轉化為「全球可訪問的 AI 核心」，打破了物理空間對自動化流程的限制。
