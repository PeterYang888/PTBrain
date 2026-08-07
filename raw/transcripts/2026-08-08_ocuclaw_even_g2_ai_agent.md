---
type: source
tags: [ai-glasses, ai-agent, openclaw, setup-guide, even-realities]
created: 2026-08-08
updated: 2026-08-08
source_url: https://www.youtube.com/watch?v=wXT1Ffi9hys
source_date: 2026-08-08
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "Tech with Spencer"
  processed_by: notebooklm-py
---

## 一句話摘要
本影片是一份針對 Even Realities G2 智慧眼鏡的完整實務指南，手把手教學如何透過 Oclaw、Tailscale 與 Sonics 將眼鏡連接至個人私有的 OpenClaw AI 系統，打造出能讀取電腦本地檔案與工具的專屬 AI 助理 [1-3]。

## 主講者背景
*   **主講者/評測者**：Spencer [1]。
*   **頻道名稱**：**Tech with Spencer** [1, 4]。
*   **立場**：影片未提及是否為業配，亦未提及眼鏡是否為自費購買。
*   **使用時長**：已重度測試、使用此套 Even Realities G2 搭配 Oclaw 的系統數天，並已達約一個月的時間 [5]。

## 核心論點
*   **硬體載體與私有 AI 的結合**：將 Even Realities G2 定位為承載個人私有 AI 代理（AI Agent）的硬體終端，透過 Oclaw 橋接，讓能調用本地應用程式、電子郵件與文件的自訂助理隨身運行 [1, 3, 6]。
*   **實際使用體驗（優點）**：
    *   **隱私高度安全**：能建立完全由使用者個人掌控、不對外公開的私有 AI 代理系統 [1]。
    *   **深度本地整合**：AI 代理能直接存取、讀取電腦本機中的檔案、電子郵件、聯絡人並執行長流程自動化任務 [3]。
    *   **極低的語音執行成本**：搭配 Sonics 語音轉文字 API，重度使用一個月也僅需花費幾美分（開發者測試 6 個月僅花費約 \$4.62 美元） [5]。
*   **實際使用體驗（缺點）**： * **設定極其繁瑣**：官方文件說明不夠完善，安裝過程包含眾多移動組件（PowerShell、T ailscale、API 串接），對非技術用戶門檻較高 [1]。
    *   **系統穩定度仍有瑕疵**：OpenClaw 系統並不完美，測試過程中會遇到卡住、報錯或 Session 衝突（如 `reply session initialization conflicted for agent main`）等狀況，需要手動重啟或建立新 Session [7]。
*   **設計取捨**：
    *   **手動觸控監聽優於語音喚醒**：系統放棄了如「Hey Oclaw」的語音自動喚醒，改用鏡腳觸控或戒指雙擊後點擊單擊（single tap）監聽 [8, 9]。雖然操作較多，但在公共場合或嘈雜餐廳中能有效防止 AI 誤判日常對話 [8, 9]。
*   **適合與不適合對象**：
    *   **適合對象**：重視隱私安全、熱愛動手實作（DIY）與客製化，且希望 AI 助理能深度讀取本機電腦資料的科技愛好者 [1, 3]。
    *   **不適合對象**：尋求「開箱即用」、不想花時間研究 PowerShell 程式碼與複雜網路設定（如 Tailscale 虛擬局域網）的普通大眾 [1, 2]。

## 關鍵規格與數據
* **眼鏡硬體規格（重量、續航、亮度、FOV、解析度、價格、充電時間、連線方式、支援語言數）**：**影片未提及**。
*   **軟硬體設定與系統數據**：
    *   **版本限制**：OpenClaw 版本必須為 **`2026.6.9` 或更新版本** [10]。
    *   **語音 API 花費**：開發者 (AU) 重度測試 6 個月共花費 **\$4.62 美元**；講者重度使用數天至一個月僅花費約 **13 至 15 美分** [5]。
    *   **連接規格**：Oclaw app 的 relay 連接格式必須使用 **`WSS`**，且連接埠（Port）為 **`8444`** [6]。
*   **安裝步驟與 CLI 指令原文**：
    1.  **安裝 OpenClaw**：在 Windows 環境下使用 PowerShell 執行 `docs.openclaw.ai/install` 網址中的 PowerShell 安裝指令 [11]。
    2.  **自動依賴檢查**：安裝程式會自動偵測並協助安裝系統缺少的 **Git** 或 **NodeJS** [11]。
    3.  **確認 OpenClaw 版本**：`openclaw - version`（或寫為 `openclaw space- version`） [10]。
    4.  **升級 OpenClaw**：`openclaw space-update` [10]。
    5.  **安裝 Oclaw 技能**：在 OpenClaw 對話框中輸入指令 `install the Oclaw skill` [12]。
    6.  **設定 PowerShell 執行權限**：執行指令 `scope current user`（僅變更當前用戶權限）以允許運行本地腳本 [13]。
    7.  **獲取 Tailscale 主機位址狀態**：`tailscale space serve space status` [6]。
    8.  **本地偵錯（Debug）設定**：在 PowerShell 運行 AU 提供的兩道偵錯命令後，執行 `openclaw gateway restart` 重啟服務 [14, 15]。
    9.  **閘道器狀態與重啟命令**：
        *   確認狀態：`openclaw space gateway space status` [3]。
        *   重啟命令：`openclaw space gateway space restart` [3]。
    10. **語音 API 設定**：至 `sonx.com` 註冊並取得 API Key，在 PowerShell 執行 API 綁定後，重啟 gateway [5]。隨後在手機 Oclaw 軟體中將 `speech to text provider` 設為 `sonics` [8]。

## 重要引言
*   「**...now I have my own private AI agent one that I control living in my glasses...**」—— 談及耗費心力完成設定後，成功在智慧眼鏡中運行完全由個人掌控之私有 AI 代理的喜悅 [1]。
*   「**Oclaw isn't just some third party add-on... I know privacy is a huge concern for people when connecting all these pieces together and I wanted to highlight this.**」—— 強調 Oclaw 是 OpenClaw 官方商城（Clawhub）正式認可的技能，保障用戶串接多方工具時的隱私安全 [6]。
*   「**If everything is working your voice is being captured converted to text sent through Oclaw to your OpenClaw agent processed by your AI model and then the response is landing in your glasses.**」—— 詳細解釋語音互動在眼鏡、手機、網路與電腦本地 AI 之間傳輸的完整運作管線（Pipeline）[9]。
*   「**We're not just asking a basic AI assistant what the weather is. Depending on how you configure OpenClaw your agent can use your tools on your computer go into your email work through longer processes...**」—— 闡述此系統相較於一般只會報天氣的陽春 AI 語音助理，在自動化與本地操作能力上的本質差別 [3]。

## 與其他產品的對比
*   **影片未提及**任何與 Meta Ray-Ban、RayNeo、MemoMind、Xreal 等競品智慧眼鏡的橫向對比、優劣差異或講者的推薦對象（本影片全程聚焦於 Even Realities G2 連接本地 OpenClaw 的技術安裝實測） [1, 3]。
