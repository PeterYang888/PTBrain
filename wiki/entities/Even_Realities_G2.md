---
type: entity
entity_type: product
tags: [ai-glasses, hardware, wearable, even-realities]
created: 2026-06-27
updated: 2026-08-15
sources: [2026-06-27_even_g2_claude_code, 2026-06-27_even_g2_創辦人訪談, 2026-06-27_even_realities_g2_36g, 2026-08-08_ocuclaw_even_g2_ai_agent, 2026-08-08_even_g2_開放平台評測, 2026-08-08_even_g2_vs_memomind_one, 2026-08-15_even_g2_開箱_joeman]
---

# Even Realities G2

> [[Will_Fan]]（前 [[Apple]] Apple Watch 團隊）2023 年創立的 Even Realities 旗下智慧眼鏡，主打「全天候舒適佩戴 + 寧靜技術」，走與 [[Meta]] 相機/社群路線相反的「無相機生產力工具」路線。

## 背景
創辦人 Will Fan 職涯始於 Apple Watch 團隊，歷經 Anker、Oppo、投影機公司 JimGo，2023 年創立 Even Realities（約 200 人，工程師/設計師/產品專家為主）。產品自比「智慧眼鏡界的 Tesla / OpenAI」，以光學工程專注 + 快速 G 系列迭代挑戰巨頭。

## 關鍵事實
- **減法美學**：刻意不搭相機與喇叭 → 隱私 + 輕量 + 續航；對拍攝隱私文化敏感地區（如日本）更友善（來自 [[2026-06-27_even_realities_g2_36g]]）
- **規格**：重量 **36g**、鏡腳 1.22mm 全鈦、**綠色單色波導 1200 nits**、續航 **48 小時**、4 麥克風（綠色單色基於電力效率最高、對人眼最舒適）
- **算力在手機端**：眼鏡藍牙連手機，主要運算負載交給手機端，維持眼鏡/指環輕量
- **R1 Ring / 操作環**：不鏽鋼 IP68、續航 4 天、觸控滑動/點擊 + PPG（心率/HRV/血氧）+ IMU（計步/卡路里/睡眠）；約 4–5 萬日圓
- **價格**：眼鏡約 **10 萬日圓**
- **AI 功能**：Conversate/Conversation（對話實時摘要 + 術語解釋 + To-do）、Hey Even / Even AI（語音 agent）、Teleprompter（AI 隨語速捲動）、**31 種語言**翻譯字幕、Dashboard（日曆/天氣/股價/新聞）
- **終端模式 (Terminal Mode)**：可遠端連桌機 [[Claude_Code]] / [[OpenAI_Codex]]，語音驅動自動化工作流（搭 [[Tailscale]] 做遠端）（來自 [[2026-06-27_even_g2_claude_code]]）

## 補充：可編程開放平台（2026-08-08）
[[2026-08-08_even_g2_開放平台評測]] 指出，G2 真正的差異化不只是「無相機」，而是**零審查的開放平台**：
- **Evenhub 開發者平台**：用 TypeScript / HTML / CSS / JavaScript 等網頁通用技術開發，模擬器預覽後掃 QR code 直接側載（sideload）上眼鏡，**無審查、無上架門檻**
- **官方 10 個功能 vs 社群 10,000 個**：GitHub 與 Discord 社群已做出 Philips Hue 燈控、電視遙控、Tesla 控制、電子書閱讀器，以及 Tetris、棋類、Flappy Bird 等
- 無相機的硬體決策同時形塑了開發文化——開發者做的是字幕／控制器／閱讀器／儀表板這類面向使用者的工具，而非監視工具
- 評測者對比 [[Meta]] 的一句話：「One path treats you as the content, the other hands you the keyboard」

## 補充：外接自架 Agent（2026-08-08）
除了內建 Terminal 模式直連 [[Claude_Code]]，G2 也可透過 **OcuClaw skill** 接上自架的 [[OpenClaw]]，讓能讀本機檔案／信件的私有 Agent 住進眼鏡（詳見 [[2026-08-08_ocuclaw_even_g2_ai_agent]]）：
- 兩條路線都靠 [[Tailscale]] 打通眼鏡／手機與家用電腦
- 刻意**不做語音喚醒**，改鏡腳觸控或戒指雙擊後單擊才監聽，避免公共場合誤聽
- 缺點是設定極繁瑣（PowerShell ＋ 虛擬區網 ＋ API 串接），且 OpenClaw 端穩定度尚未成熟

## 補充：Joeman 開箱實測（2026-08-15）
來自 [[2026-08-15_even_g2_開箱_joeman]]，第三位評測者視角，補充前兩批未提到的細節：
- **設計協作**：邀請德國高階眼鏡品牌 MYKITA 共同創辦人 Filip Hoffman 操刀外觀；2 種框型（復古圓形／俐落方形）× 3 色（綠/棕/灰）
- **Claude Code Terminal 連線門檻**：電腦端需裝 Claude Code CLI＋Node 環境，經官方 Even Terminal 連線；**免費版 Claude 帳號無法使用，必須 Pro 以上訂閱或 API 計量付費的 Console 帳號**
- **對話轉寫實測準確度**：約 90%
- **導航限制**：僅走路／腳踏車兩種慢速模式（不適合開車/騎摩托車，GPS 有延遲），且僅支援 App 內建地圖，不支援第三方地圖
- **EvenHub 生態實例**：電子書閱讀器（可調自動翻頁速度）、貪食蛇等小遊戲

## 補充：美元價格階梯與規格（2026-08-08）
來自 [[2026-08-08_even_g2_vs_memomind_one]]（主講者自費購買、數月實測）：
- **基本款 $599** ｜ 配鏡版 $758–$948（依度數）｜ Ring controller $249（未稅）｜ 太陽鏡片 $99 ｜ 最高配總價可達 **$1,296**
- 解析度 **640×350**、**FOV 27.5°**（既有來源未提供的兩項）
- **完全沒有喇叭**：不能通話、不能放音樂——這是它與 [[MemoMind_One]] 最大的功能差距
- 2025 年 11 月上市；製造商剛達 10 億美元估值（[來源口述，未查證]）

## ⚠️ 待裁決的規格衝突
| 項目 | 說法 A | 說法 B |
|---|---|---|
| 續航 | **48 小時 / 2 天**（[[2026-06-27_even_realities_g2_36g]]、[[2026-08-08_even_g2_開放平台評測]]） | **12 小時**（[[2026-08-08_even_g2_vs_memomind_one]]） |
| 翻譯語言數 | **31 種**（2026-06-27 批次） | **29 種**（2026-08-08 Ken） | **支援 35 種，其中 29 種可雙向翻中文**（2026-08-15 Joeman） |

推測續航差異來自測試條件（混合／待機 vs 重度使用），但三方來源皆未說明測法。語言數：Joeman 的「29」與 Ken 的「29」數字相同但計量基準不同（前者明確是「雙向翻中文」子集，後者未說明是否為同一基準），31 種說法仍未解釋差異來源。本頁並列不裁決。

## 與其他頁的關係
- 是 [[AI智慧眼鏡]] 的「無相機生產力工具」路線代表，對比 [[RayNeo_X3_Pro]]（全彩 AR + 本機 Gemini，76g/約 1hr）、[[Ray-Ban_Meta]]（相機/社群、299 美元起）
- 同路線的價格帶競爭者：[[MemoMind_One]]（$399 早鳥、46.6g、有喇叭、16 小時、2000 nits）
- 終端模式把眼鏡變成 [[Claude_Code]] 的行動介面，實踐 [[Vibe_Coding]] / [[Agentic_Workflow]]
- 體現 [[寧靜技術]] 設計哲學，並把它延伸成「不奪取控制權」的平台開放性

## 相關來源
- [[2026-06-27_even_g2_claude_code]] — 終端模式連 Claude Code
- [[2026-06-27_even_g2_創辦人訪談]] — Will Fan 設計哲學
- [[2026-06-27_even_realities_g2_36g]] — 36g 評測與寧靜技術
- [[2026-08-08_even_g2_開放平台評測]] — Evenhub 與社群生態
- [[2026-08-08_ocuclaw_even_g2_ai_agent]] — 外接 OpenClaw 完整設定
- [[2026-08-08_even_g2_vs_memomind_one]] — 對 MemoMind One 的規格與價格對照
- [[2026-08-15_even_g2_開箱_joeman]] — Joeman 開箱：設計協作、Claude Code 連線門檻、導航限制
