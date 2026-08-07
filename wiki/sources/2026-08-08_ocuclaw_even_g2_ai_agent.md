---
type: source
tags: [ai-glasses, ai-agent, openclaw, setup-guide, even-realities]
created: 2026-08-08
updated: 2026-08-08
source_url: https://www.youtube.com/watch?v=wXT1Ffi9hys
source_date: 2026-08-08
source_type: transcript
---

# Run Your Own AI Agent on Even Realities G2（OcuClaw 完整設定教學）

> 來源：[原始檔](../../raw/transcripts/2026-08-08_ocuclaw_even_g2_ai_agent.md) · 主講：Spencer（頻道 Tech with Spencer）

## 一句話摘要
手把手把 [[Even_Realities_G2]] 接上自架的 [[OpenClaw]]：透過 OcuClaw skill ＋ [[Tailscale]] 打通眼鏡與家用電腦，讓能讀本機檔案／信件、跑長流程的私有 AI Agent 住進眼鏡裡。

## 核心論點
- **眼鏡＝私有 Agent 的隨身終端**：不是接雲端助理，而是把 OpenClaw 這個能操作「你自己電腦」的 Agent 接到眼前
- **隱私是主要動機**：整條管線（語音 → 文字 → OcuClaw → 你的 OpenClaw agent → 你的模型 → 回到眼鏡）都在自己掌控的機器上
- **成本低到可忽略**：語音轉文字 API 重度使用數天至一個月僅花約 **13–15 美分**；開發者測試 6 個月共 **$4.62 美元**
- **設定極繁瑣是最大缺點**：官方文件不完善，牽涉 PowerShell、Tailscale 虛擬區網、API 串接，非技術用戶門檻高
- **穩定度尚未成熟**：測試中會遇到卡住、報錯、Session 衝突（`reply session initialization conflicted for agent main`），需手動重啟或開新 Session
- **刻意放棄語音喚醒**：不做「Hey OcuClaw」，改成鏡腳觸控或戒指雙擊後單擊才開始監聽——操作變多，但在餐廳等吵雜公共場合能避免 AI 誤聽日常對話
- **官方認證的 skill**：OcuClaw 不是第三方外掛，是 OpenClaw 官方商城（Clawhub）認可的 skill，串接時的隱私有保障

## 關鍵細節（設定流程）
- **版本門檻**：OpenClaw 需 **`2026.6.9`** 或更新版
- **連線規格**：OcuClaw app 的 relay 必須用 **`WSS`**、連接埠 **`8444`**
- 安裝步驟（依影片順序）：
  1. Windows 用 PowerShell 跑 `docs.openclaw.ai/install` 的安裝指令（會自動偵測並補裝 **Git** / **NodeJS**）
  2. 在 OpenClaw 對話框輸入 `install the OcuClaw skill`
  3. 設定 PowerShell 執行權限（`-Scope CurrentUser`，只改當前使用者）
  4. 取得 Tailscale 主機位址：`tailscale serve status`
  5. 重啟閘道器：`openclaw gateway restart`；查狀態：`openclaw gateway status`
  6. 到語音 API 網站註冊取 API Key，綁定後重啟 gateway，再於手機 OcuClaw 把 `speech to text provider` 設為該服務

## 值得引用的段落
> 「...now I have my own private AI agent one that I control living in my glasses...」— 設定完成後的核心價值主張

> 「If everything is working your voice is being captured converted to text sent through OcuClaw to your OpenClaw agent processed by your AI model and then the response is landing in your glasses.」— 完整管線說明

> 「We're not just asking a basic AI assistant what the weather is. Depending on how you configure OpenClaw your agent can use your tools on your computer go into your email work through longer processes...」— 與陽春語音助理的本質差別

## 與其他頁的關聯
- 補完 [[2026-06-27_even_g2_claude_code]] 的另一條路線：該支用 G2 內建 **Terminal 模式**直連 [[Claude_Code]]，本支則走 [[OpenClaw]] ＋ OcuClaw skill 的通用 Agent 路線，兩者都靠 [[Tailscale]] 做遠端
- 回填 [[Peter_Steinberger]] 頁的待追蹤：OpenClaw 是什麼，本頁首次有具體描述
- 是 [[Agentic_Workflow]] 的穿戴式介面實例；也印證 [[AI智慧眼鏡]]「算力在手機/PC 端、眼鏡只做 I/O」的架構

## 連結到的 wiki
- [[Even_Realities_G2]] · [[OpenClaw]] · [[Tailscale]] · [[AI智慧眼鏡]] · [[Agentic_Workflow]] · [[Peter_Steinberger]] · [[Claude_Code]]

## 我的問題 / 待追蹤
- **語音誤植已校正**：briefing 中的 `openclaw space- version`、`openclaw space gateway space restart`、`scope current user` 等，「space」明顯是逐字稿把空格／連字號念出來所致，本頁已還原為 `openclaw --version`、`openclaw gateway restart`、`-Scope CurrentUser`（[推導]，未經實機驗證）
- **未核實的名詞**：語音轉文字服務被念成 "Sonics"、網址 "sonx.com"，實際服務名與網址待查；產品名 "Oclaw" 與 "OcuClaw" 在逐字稿中混用，本頁統一用影片標題的 **OcuClaw**
- 影片全程未提 G2 硬體規格（重量／續航／亮度），規格請看 [[2026-08-08_even_g2_vs_memomind_one]]
- 未提及 macOS / Linux 的安裝路徑，只示範 Windows PowerShell
