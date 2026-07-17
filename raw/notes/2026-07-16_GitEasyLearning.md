這是一份為你整理的 [給非技術人員的 Github 教學，Vibe Coding 必學的基礎技能](https://www.youtube.com/watch?v=atqcAb7MFAM) 影片摘要與學習筆記：

### **影片摘要**

這支影片專為沒有程式背景、但正嘗試使用 AI（如 Claude 或 Cursor）進行 Vibe Coding 的使用者設計。影片透過開發「記帳軟體」的生活化比喻，白話解釋了 AI 常常詢問的 Git 和 GitHub 專有名詞，幫助觀看者釐清版本控制的核心邏輯，並將其無縫融入日常的 AI 開發與多代理 (Agent) 協作流程中。

### **作者簡介**

Gary Chen 是一位專注於將複雜程式開發觀念與 AI 協作工具轉化為直白、易懂教學的內容創作者。

### ---

**知識重點與可執行的 Takeaway**

* [**01:02在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=62) **Git vs. GitHub 的本質差異**  
  * GitHub 是存放程式碼的雲端空間（類似 Google Drive）；而 Git 則是安裝在電腦本機端，負責紀錄程式碼版本歷史的工具。  
  * **Takeaway:** 開始寫程式前，先確保資料夾已經讓 Git 開始追蹤，這是一切版本控制的基礎。  
* [**02:56在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=176) **Commit 與 Push**  
  * commit 是在本機端的「存檔點」，就算 AI 把程式改壞也能隨時還原；push 則是把存檔正式推送到雲端的 origin 備份。  
  * **Takeaway:** 只要 AI 完成一個你滿意的階段性功能，就請它先 commit 一次。  
* [**04:40在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=280) **致命危機與 .gitignore**  
  * 絕對不能把機密（如 API 鑰匙、資料庫密碼）push 上網，一旦外洩只能整把作廢。  
  * **Takeaway:** 直接指令 AI：「確保所有金鑰與機密都在 .gitignore 中，絕對不要 commit 上去」。  
* [**06:07在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=367) **Clone 與 Pull**  
  * clone 是第一次加入專案時，將完整記錄下載到電腦；pull 則是平時用來同步雲端上最新的進度到本機端。  
* [**07:35在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=455) **Branch (分支) 的保護機制**  
  * main 是一直穩定運行的主線。開發新功能時必須開新的 branch，像是在平行的時空中試錯，不會搞壞主線。  
* [**09:59在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=599) **Worktree 的多重 Agent 協作**  
  * 當你需要同時開啟多個 AI agent（例如一個處理資料庫邏輯，一個切換 UI 介面）時，在同一個資料夾切換 branch 會互相干擾。worktree 相當於買了第二張實體辦公桌。  
  * **Takeaway:** 要求 AI 開新的 worktree，讓不同的 Agent 在各自獨立的實體資料夾中平行開發，效率極佳且互不衝突。  
* [**12:02在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=722) **PR (Pull Request) 與 Merge**  
  * 寫完功能要合併回 main 之前，先開 PR 提出改動提案讓團隊審核；確認無誤後再執行 merge 合併。  
* [**13:36在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=816) **處理 Conflict (衝突)**  
  * 當兩人或兩個 AI 改到同一段核心邏輯時會發生衝突。  
  * **Takeaway:** 遇到衝突時，不需要自己下去改程式碼。直接給出明確的「產品決策」（例如：「資料庫寫法以 A 為主，但保留 B 的前端選單介面」），讓 AI 幫你處理合併。  
* [**15:48在新視窗中開啟**](http://www.youtube.com/watch?v=atqcAb7MFAM&t=948) **改壞了怎麼救 (Restore vs Revert)**  
  * 若還沒 commit，用 restore 直接抹除退回；若已經 commit，用 revert 發布一個「反向操作」來安全抵銷錯誤，且會留下完整紀錄。

### ---

**留言分析與觀看者看法**

交叉比對熱門的前 10 則留言，觀看者的核心看法可以歸納為以下三點：

1. **精準痛擊新手痛點：** 許多嘗試 Vibe Coding 幾個月的玩家，經常被 AI 突然詢問的 commit 或 PR 搞得一頭霧水。觀眾盛讚影片完美解答了「為什麼 AI 總是問我要不要 commit」的背後邏輯。  
2. **化繁為簡的教學能力：** 觀眾一致認為這部影片比傳統的工程師教學好懂非常多，特別是「把 Git 當成防範神經病 AI 的保險機制」以及「Git 嚇死以為是衝突」等生動比喻，讓人一聽就懂。  
3. **進階實務經驗共鳴：** 有些進階使用者在留言區交流踩雷經驗，例如為了避免浪費 API token 與程式碼衝突，會利用 Handoff 紀錄並要求 Claude 在動到 Core function 時提出警戒，呼應了影片中對於並行開發與管控 AI 協作的重視。

### ---

**Vibe Coding 快速複習筆記**

在日常指揮 Claude 或 Cursor 開發與管理專案時，可以直接套用以下概念對應情境：

**🔹 1\. 隔離風險與平行開發**

* **Branch (分支)：** 「接下來要大改老虎機的數學模型，幫我從 main 開一個新的 branch，免得把主線搞砸。」  
* **Worktree (工作樹)：** 「我要同時開兩個 Cursor Agent，一個處理後端邏輯，一個優化前端介面。幫我建兩個 worktree，讓他們在實體資料夾平行作業。」

**🔹 2\. 存檔與備份循環**

* **Commit：** 「這版測試沒問題，幫我 commit 存檔留底。」（發生在本地）  
* **Push：** 「進度不錯，幫我 push 推送到雲端備份。」（發布到雲端）  
* **.gitignore：** 「千萬別把任何開發金鑰傳出去，先確認都加進 .gitignore 了。」

**🔹 3\. 發布與版本管控**

* **PR (Pull Request)：** 「幫我整理這次改了什麼，發個 PR 準備合併，我要檢閱一下。」  
* **Merge：** 審查無誤，正式將新功能合併回 main 主線。  
* **Conflict (衝突)：** 出現衝突時，直接以主管視角下達規則：「登入邏輯以最新分支為主，但保留我原本改好的 UI，幫我解衝突。」

**🔹 4\. 搶救 AI 失控的代碼**

* **Restore：** （尚未 commit 時發現 AI 寫爛）「這版完全不行，用 restore 直接退回上次正常狀態。」  
* **Revert：** （已經 commit 後發現會導致系統崩潰）「幫我用 revert 發一個反向 commit 安全抵銷上次的錯誤，保留完整紀錄。」