---
type: source
tags: [ai, ai-glasses, claude-code, codex, workflow]
created: 2026-06-27
source_url: https://www.youtube.com/watch?v=-FszxC5q400
source_date: 2026-06-27
source_type: transcript
---

# Even G2 智慧眼鏡 × Claude Code 終端模式：隨處工作

> 來源：[原始檔](../../raw/transcripts/2026-06-27_even_g2_claude_code.md) · 主講：トバログ (Tobalog)

## 一句話摘要
用 [[Even_Realities_G2]] 智慧眼鏡的「終端模式」遠端連接電腦端的 [[Claude_Code]] / [[OpenAI_Codex]]，靠語音隨時隨地驅動 AI 自動化工作流——把眼鏡變成桌機 AI Agent 的行動介面，是 [[AI智慧眼鏡]] 的「殺手級應用」實證。

## 核心論點
- **解放地理束縛**：解決 Claude Code 開發時需頻繁按「approve」而被鎖死在電腦前的痛點
- **眼鏡 = 桌機 AI 的行動介面**：比單純翻譯/導航更具實用價值的定位
- **系統級操作**：語音間接操控 Notion、Chrome、Office、DaVinci Resolve
- **[[工具無關性]]遠端連結**：VPN 建立虛擬空間，全球有網路即可喚醒家中電腦執行任務

## 關鍵規格與設定
- **Even Realities G2**：前 Apple Watch 團隊設計，極薄、綠色單色投影，約 **10 萬日圓**；操作環 (Ring) 約 **4–5 萬日圓**（捲動/點擊 + 血氧/睡眠監測）
- **安裝**：電腦端預裝 **Node.js / npm** → 安裝 `claude-code` CLI 與 `even-terminal` 套件 → 終端輸入 `even-terminal` 生成 QR Code 與手機 App 配對
- **遠端**：[[Tailscale]] 建虛擬網域（免費版上限 100 台）；家中電腦開機未睡眠即可行動網路遠端連
- 語音辨識送出前可於眼鏡螢幕確認文字正確性

## 值得引用的段落
> 「這簡直就是智慧眼鏡的殺手級應用（Killer App）。」
> 「即便人在外頭散步或去便利商店買咖啡，家裡的 AI 依然在為你工作。」

## 連結到的 wiki
- [[Even_Realities_G2]] · [[AI智慧眼鏡]] · [[Claude_Code]] · [[OpenAI_Codex]] · [[Vibe_Coding]] · [[Agentic_Workflow]] · [[工具無關性]] · [[Tailscale]]

## 我的問題 / 待追蹤
- 終端模式的延遲與穩定性如何？語音操作長指令的實用門檻
- 與 [[RayNeo_X3_Pro]] 路線（全彩 AR + 本機 Gemini）對比：Even G2 走「極簡單色 + 連桌機算力」的差異化
