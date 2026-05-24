---
title: "Claude Code官方App大改版！內建終端機、側邊欄，專為「一心多用」開發而生"
source: "https://www.bnext.com.tw/article/90646/claude-code-routines-update?openExternalBrowser=1&utm_source=line&utm_medium=message"
author:
published:
created: 2026-04-17
description: "Anthropic 大幅改造 Claude Code 桌面版並推出 routines 雲端自動化，搶佔開發者 AI 工作流入口。"
tags:
  - "clippings"
---
[![年度必聽 AI 趨勢指標論壇，免費報名！](https://bnextmedia.s3.hicloud.net.tw/pumpkin/image/photo/2026-03/img-1774796235-64801.gif)](https://edm.bnext.com.tw/AIA_AI2026/?utm_campaign=26ALLinAI&utm_source=web_bn&utm_medium=logo_banner&utm_content=164523&utm_term=channel_all)

![Claude Code官方App大改版！內建終端機、側邊欄，專為「一心多用」開發而生](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/eg1s-1776224187.jpg?w=900&output=webp)

2026.04.15 | [AI與大數據](https://www.bnext.com.tw/categories/ai)

Anthropic 大幅改造 Claude Code 桌面版並推出 routines 雲端自動化，搶佔開發者 AI 工作流入口。

[＃Anthropic](https://www.bnext.com.tw/tags/Anthropic) [＃Claude](https://www.bnext.com.tw/tags/Claude)

---

> **重點一** ：Claude Code 桌面版大改版，一次開多個 AI 任務同時跑，還內建終端機和程式碼編輯器。  
>   
> **重點二** ：新功能 routines 讓 AI 自動排程工作，關掉電腦也能跑。  
>   
> **重點三** ：routines 每天有次數限制，Pro 方案 5 次、Max 15 次、企業版 25 次，超過要加錢。

Anthropic 於 4 月 14 日同步發布 Claude Code 桌面應用程式重大改版與全新 routines 雲端自動化功能，這是該公司針對 AI 輔助開發工具一次涵蓋範圍最廣的更新。

Anthropic 在官方部落格指出，開發者與 AI 協作的模式已經改變： **同時在多個程式庫中啟動重構、修 bug、寫測試，在結果回傳時逐一檢視並即時調整方向。**

新版桌面 app 正是為上述這種「多線並行」的工作流而設計。

掌握最新AI、半導體、數位趨勢！訂閱《數位時代》日報及社群活動訊息

重構後的桌面版新增側邊欄（sidebar），所有進行中與近期的 session 集中呈現，可依狀態、專案或環境篩選，也能依專案分組。而當 session 對應的 PR 被合併或關閉，會自動歸檔。

開發者也可透過 /btw 指令開啟側邊提問（side question），在不中斷主任務的情況下快速查詢問題。側邊提問能讀取當前對話的完整上下文，但不會呼叫工具或影響主執行緒的進度，即使 Claude 正在處理任務時也能使用。

### 內建開發工具，降低切換成本

本次改版的另一個重點是將常用開發工具直接內建於 app 中。新版加入了整合終端機，可在 session 旁同步執行測試或建置指令。

內建檔案編輯器則可直接開啟、編輯並儲存檔案；diff 檢視器針對大型變更集重新優化效能；預覽面板除了既有的本地伺服器預覽外，也支援 HTML 檔案與 PDF 的即時預覽。所有面板支援拖放排列。

The Register報導分析指出，Anthropic 刻意將開發工具收進自家介面，核心意圖是「擁有開發者與 Claude 互動的介面」， **不希望用戶透過 VS Code 外掛或第三方工具存取 AI 服務。**

新版桌面 app 也達成與 CLI 外掛的完整對等，組織集中管理或開發者自行安裝的外掛，在桌面版與終端機中行為完全一致。

SSH 遠端連線支援已從 Linux 擴展至 Mac。顯示模式分為 Verbose、Normal、Summary 三種，開發者可自行調整 AI 工具呼叫的透明度。

### routines：關筆電也能跑的雲端自動化

Anthropic 同日以研究預覽（research preview）形式推出 routines 功能。

routine 是一組預設好的 Claude Code 自動化配置，包含提示詞、程式庫與連接器（connectors），設定完成後可依三種方式觸發：

> - 排程：每天晚上、每週一次，時間到了自動執行（像鬧鐘）
> - API 呼叫：接到其他系統的訊號就動（像部署完自動跑測試）
> - GitHub 事件：有人發 PR 或合併程式碼時自動觸發（像自動 code review）

在實際應用上，官方舉例如下：

> **排程型**  
> \- 每天晚上自動掃新 issue，分好類，發摘要到 Slack → 隔天上班直接看重點。  
> \- 每週掃一次已合併的 PR，找出哪些文件該更新，自動開 PR 提醒。  
>   
> **部署觸發型**  
> \- 每次程式碼部署上線後，Claude 自動跑煙霧測試、掃錯誤日誌，判斷這次上線有沒有問題。  
>   
> **GitHub 觸發型**  
> \- 有人開 PR → 自動跑團隊的安全與效能檢查清單。  
> \- Python SDK 合併了一個改動 → 自動把同樣的改動搬到 Go SDK。

routines 開放給 Pro、Max、Team 與 Enterprise 方案用戶，每日執行次數設有上限：Pro 用戶 5 次、Max 用戶 15 次、Team 與 Enterprise 用戶 25 次，超額部分需啟用額外用量計費。

> 延伸閱讀： [Claude Code只發揮1成實力？7個設定目錄完整教學，讓AI每次都按你的規則工作](https://www.bnext.com.tw/article/90642/claude-code-folder-config-guide)

資料來源： [Anthropic 官方部落格](https://claude.com/blog/claude-code-desktop-redesign) 、 [Anthropic 官方部落格](https://claude.com/blog/introducing-routines-in-claude-code) 、 [The Register](https://www.theregister.com/2026/04/14/claude_code_routines/)

本文初稿為AI編撰，整理．編輯/ 李先泰

[![](https://cdn.bnextmedia.com.tw/img/16x9.png "【年度唯一】4/23 超級店長學－台中場")](https://edm.managertoday.com.tw/super/?utm_source=web_bn&utm_medium=aa_event_er&utm_campaign=stage_1&utm_term=model_5 "【年度唯一】4/23 超級店長學－台中場")

[【年度唯一】4/23 超級店長學－台中場](https://edm.managertoday.com.tw/super/?utm_source=web_bn&utm_medium=aa_event_er&utm_campaign=stage_1&utm_term=model_5 "【年度唯一】4/23 超級店長學－台中場")

[

活動詳情

](https://edm.managertoday.com.tw/super/?utm_source=web_bn&utm_medium=aa_event_er&utm_campaign=stage_1&utm_term=model_5 "【年度唯一】4/23 超級店長學－台中場")

關鍵字： [＃Anthropic](https://www.bnext.com.tw/tags/Anthropic) [＃Claude](https://www.bnext.com.tw/tags/Claude)

往下滑看下一篇文章

<video controls=""></video><video title="Advertisement" src="https://gcdn.2mdn.net/videoplayback/id/dd140c52904a002e/itag/59/source/web_video_ads/xpc/EgVovf3BOg%3D%3D/ctier/L/acao/yes/ip/0.0.0.0/ipbits/0/expire/1807914377/sparams/ip,ipbits,expire,id,itag,source,xpc,ctier,acao/signature/8365EBB3D02B2676F7F594042D174798C4C5B145.970F41D9DBC6D00843DA2FA5D80E8FFF71B2CEF7/key/ck2/file/file.mp4" controls=""></video><iframe src="https://imasdk.googleapis.com/js/core/bridge3.757.0_en.html#deid=%22%22&amp;eventfe_experiment_ids=%5B%5D&amp;fid=%22goog_1616544415%22&amp;genotype_experiment_data=%7B%22experimentStateProto%22%3A%22%5B%5B%5B45713128%2Cnull%2Cnull%2C%5B%5D%5D%2C%5Bnull%2C745150931%2Cnull%2C%5Bnull%2C1%5D%5D%2C%5Bnull%2C749060184%2Cnull%2C%5Bnull%2C128%5D%5D%2C%5B841585769%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B45761044%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45722344%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45706017%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B45774999%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45776042%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45668885%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45685340%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45765927%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45734716%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45735891%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45663239%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45715032%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B45661356%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B839547366%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B45676441%2Cnull%2Cnull%2C%5B%5D%5D%2C%5Bnull%2C45645574%2Cnull%2C%5B%5D%5D%2C%5B45688859%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45656766%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45710689%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45710688%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B45685601%2Cnull%2Cnull%2C%5B%5D%5D%2C%5Bnull%2C45685602%2Cnull%2C%5Bnull%2C500%5D%5D%2C%5Bnull%2C45767902%2Cnull%2C%5Bnull%2C500%5D%5D%2C%5B45756824%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45747172%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B775241416%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B781107959%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B781107958%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B792614055%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B781107957%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45729602%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45753603%2Cnull%2Cnull%2C%5B%5D%5D%2C%5B45753604%2Cnull%2Cnull%2C%5B%5D%5D%5D%2C%5B%5B16%2C%5B%5B1%2C%5B%5B31089630%5D%2C%5B31089631%2C%5B%5B45668885%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B10%2C%5B%5B31097690%5D%2C%5B31097691%2C%5B%5B846355750%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B1000%2C%5B%5B95332046%5D%5D%5D%2C%5Bnull%2C%5B%5B95332047%5D%5D%5D%2C%5B10%2C%5B%5B95338769%2C%5B%5Bnull%2C45645574%2Cnull%2C%5Bnull%2C1%5D%5D%5D%5D%2C%5B95338770%2C%5B%5Bnull%2C45645574%2Cnull%2C%5Bnull%2C2%5D%5D%5D%5D%5D%5D%2C%5B50%2C%5B%5B95345206%5D%2C%5B95345207%2C%5B%5B45661356%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B1%2C%5B%5B95351425%5D%2C%5B95351426%2C%5B%5B45676441%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B20%2C%5B%5B95356068%5D%2C%5B95356069%2C%5B%5B45685601%2Cnull%2Cnull%2C%5B%5D%5D%2C%5Bnull%2C45685602%2Cnull%2C%5B%5D%5D%5D%5D%2C%5B95356070%2C%5B%5B45685601%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C45685602%2Cnull%2C%5B%5D%5D%5D%5D%2C%5B95356071%2C%5B%5B45685601%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5Bnull%2C45685602%2Cnull%2C%5Bnull%2C100%5D%5D%5D%5D%5D%5D%2C%5B1%2C%5B%5B95373378%2C%5B%5B792614055%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%2C%5B95373379%2C%5B%5B45747172%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B781107959%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B792614055%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B781107957%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B10%2C%5B%5B95378629%5D%2C%5B95378630%2C%5B%5B45729602%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%2C%5B95381582%2C%5B%5B45729602%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B45753603%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%2C%5B95381583%2C%5B%5B45729602%2Cnull%2Cnull%2C%5B1%5D%5D%2C%5B45753604%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B10%2C%5B%5B95382403%5D%2C%5B95386528%2C%5B%5Bnull%2C45767902%2Cnull%2C%5B%5D%5D%2C%5B45756824%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%2C%5B95386532%2C%5B%5Bnull%2C45767902%2Cnull%2C%5Bnull%2C100%5D%5D%2C%5B45756824%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%2C%5B95386533%2C%5B%5Bnull%2C45767902%2Cnull%2C%5Bnull%2C300%5D%5D%2C%5B45756824%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%2C%5B95386534%2C%5B%5Bnull%2C45767902%2Cnull%2C%5Bnull%2C500%5D%5D%2C%5B45756824%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5Bnull%2C%5B%5B95385117%5D%2C%5B95385118%2C%5B%5B45761044%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5Bnull%2C%5B%5B95385193%5D%2C%5B95385194%2C%5B%5B45765927%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B10%2C%5B%5B95387816%5D%2C%5B95387817%2C%5B%5B45774999%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%2C%5B10%2C%5B%5B95388078%5D%2C%5B95388079%2C%5B%5B45776042%2Cnull%2Cnull%2C%5B1%5D%5D%5D%5D%5D%5D%5D%5D%5D%2Cnull%2Cnull%2C%5Bnull%2C1000%2C1%2C1000%5D%5D%22%7D&amp;imalib_experiments=%5B95322027%2C95331589%2C95332046%5D&amp;is_eap_loader=false&amp;managed_js_experiment_id=0&amp;page_correlator=3954740641215140&amp;pvsid=6503606090517723&amp;top_accessible_page_url=%22https%3A%2F%2Fwww.bnext.com.tw%2Farticle%2F90646%2Fclaude-code-routines-update%3FopenExternalBrowser%3D1%26utm_source%3Dline%26utm_medium%3Dmessage%22" allowfullscreen="" allow="autoplay" title="Advertisement" width="640" height="360"></iframe>

即時熱門文章

[1 Claude Code只發揮1成實力？7個設定目錄完整教學，讓AI每次都按你的規則工作](https://www.bnext.com.tw/article/90642/claude-code-folder-config-guide) [2 不用Obsidian也能建AI知識庫！Karpathy同款「說明書」設定，4.1萬人超人氣方法完整拆解](https://www.bnext.com.tw/article/90650/andrej-karpathy-ai-how) [3 Chrome內建Gemini Skills！輸入「/」叫出提示詞，跨分頁比價、掃文件一鍵搞定](https://www.bnext.com.tw/article/90647/google-chrome-gemini-skills-save-ai-prompts) [4 不只是共享辦公室，更是企業孵化器！韻驊如何運用空間與資源，加速企業成長？](https://www.bnext.com.tw/article/90413/vqznxduk) [5 AI 改寫外貿規則！Alibaba.com 用 AI 助台灣中小企業提升跨境獲客力](https://www.bnext.com.tw/article/90494/alibaba.com115129) [6 AI做95%、你做5%！Anthropic執行長：槓桿效應讓人類貢獻放大20倍，比較優勢反而更關鍵](https://www.bnext.com.tw/article/90636/anthropic-dario-amodei-ai-task)

![AI 改寫外貿規則！Alibaba.com 用 AI 助台灣中小企業提升跨境獲客力](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/hexf-1775014530.jpg?w=900&output=webp)

2026.04.02 | [AI與大數據](https://www.bnext.com.tw/categories/ai)

AI 改寫外貿規則！Alibaba.com 用 AI 助台灣中小企業提升跨境獲客力

---

分享

過去談外貿競爭力，企業多半聚焦在產品品質、價格優勢與業務能力，但在 AI 新世代，外貿經營模式開始改變，從搜尋供應商、產品比價，到詢價與下單，越來越多流程倚靠 AI 優化與處理，企業若無法善用 AI 工具，接單效率跟市場競爭力都將逐漸落後。

在這樣的趨勢下，全球 B2B 跨境電商平台 Alibaba.com 持續以 AI 強化平台能力，並透過在地團隊與服務體系，協助台灣中小企業提升跨境營運效率與訂單轉換率，同時，每年皆舉辦「跨境電商達人賽」，今年遴選出 10 家台灣代表企業，展示 AI 如何協助企業提升外貿接單能力並拓展海外市場。

例如，深耕五金泵浦領域 40 餘年、積極將產品服務延伸至消防系統與節能設備的偉盛豐貿易，便透過 Alibaba.com 與 AI 生意助手自動回覆海外買家的 RFQ 詢盤，突破時差限制，讓接單流程更加即時，成功將市場拓展至美國、義大利與新加坡等地。

## 解決客戶痛點，Alibaba.com 以 AI 外貿金三角助台灣企業提升跨境接單力

受到貿易戰與地緣政治影響，全球貿易環境的不確定性大幅提升，過度依賴單一市場已成為潛在風險，越來越多企業透過提供多元產品與布局多元市場確保營運韌性、台灣中小企業也不例外。只不過，受到開發新市場成本高昂、優秀外貿人才逐漸流向半導體與科技產業等因素影響，中小企業面臨諸多挑戰。

為協助企業解決這些痛點，Alibaba.com 台灣總經理廖羿琦表示：「Alibaba.com 不只提供『一站通全球』平台，也透過一系列 AI 與數據工具，幫助台灣賣家更有效率地將產品銷往歐美與東南亞市場，讓 MIT 產品被更多全球買家看見。」

廖羿琦進一步指出，跨境電商從店鋪開設、商品上架、產品描述、回覆買家需求，到成交後的金流與物流，每個環節都影響接單效率，因此，Alibaba.com 提出 AI 外貿金三角策略，協助台灣中小企業系統化提升跨境接單能力：

首先，是透過 Alibaba.com 的一站式外貿平台，連結全球超過 190多個國家和地區、超過5000 萬活躍買家，並提供 AI 工具協助商家提升營運效率。例如，AI 生意助手可協助分析不同市場熱銷商品，提供商品標題與關鍵字建議，甚至生成產品場景圖與影片，提高商品在全球市場的曝光度。

其次，透過 OKKI CRM 協助台灣商家深入理解與客戶的互動關係與需求變化，進而精準地預測客戶需求，挖掘潛在商機。

最後，透過 OKKI AiReach 協助企業從被動接單轉為主動開發客戶。廖羿琦指出：「企業可以透過 AiReach 盤點產業上下游的關聯圖譜與企業關係，讓商家透過更精準的 eDM 與客戶接觸，進一步提升陌生開發的轉換率與成交率。」

值得特別一提的是，除了平台工具，Alibaba.com 也持續強化與企業社群的連結。例如在台灣北、中、南設立六個商圈，透過交流活動讓商家分享跨境經驗與市場洞察，同時也有專職團隊協助企業導入平台與 AI 工具，加速跨境電商的營運成長。

![#0 AI 改寫外貿規則！Alibaba.com 用 AI 助台灣中小企業提升跨境獲客力](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/7nr6-1775011351.jpg?w=1200&output=webp)

Alibaba.com 台灣總經理 廖羿琦

圖／ 數位時代

## 高效佈局，偉盛豐貿易以 Alibaba.com 成功擴展外貿市場

偉盛豐貿易長期深耕泵用閥件與 DC 循環扇市場，隨著第二代接班，公司也開始面臨新的經營課題：疫情衝擊全球供應鏈、台灣內銷市場逐漸飽和，加上通膨、貿易戰與地緣政治等因素，使企業必須重新思考成長動能。

為尋找新的營收來源，偉盛豐貿易王珮馨決定積極布局外貿市場，目標是直接與海外企業客戶建立合作關係，進一步掌握市場需求與訂單結構。

偉盛豐貿易一開始是透過參加國際展會拓展海外市場，但成本高、效益有限。「直到加入 Alibaba.com 後，才真正打開跨境市場。」王珮馨表示，短短一年的時間，偉盛豐貿易與來自美國、義大利與新加坡等六個國家的客戶建立合作關係，甚至在產品單價高於同業約七倍的情況下，仍成功拿下義大利與美國的貨櫃訂單。

背後的關鍵之一，是 Alibaba.com 提供的 AI 生意助手。她表示：「將產品知識庫與技術資料導入 AI 生意助手後，系統便能依照產品規格與應用場景，自動回覆海外買家的 RFQ 詢盤，就算我在休息的時候，AI 仍在替公司接單，而且是用客戶熟悉的語言回覆，等到我隔天上班後再接手處理客戶的進階問題，整體接單效率大幅提升。」

例如，面對美國芝加哥並重視ESG議題的客戶詢問：為何偉盛豐提供的 2.9W DC 循環扇售價高達 156 美元、幾乎是市售產品的七倍，王珮馨的做法是先查詢芝加哥的電價資料，再透過 AI 生意助手生成產品應用場景圖與競品耗電分析表，從「整體持有成本（TCO）」角度說明產品節能優勢，成功說服客戶，取得40呎貨櫃訂單。

王珮馨說：「至於來自義大利的食品加工廠客戶，也是因為 AI 生意助手即時回覆產品規格，了解我們提供的泵浦閥門可在不更動既有設備管線的情況下直接替換使用，因此決定採用該產品並建立長期合作。」對偉盛豐而言，AI 生意助手不只是平台工具，更像是全天候運作的「跨境電商店長」，不僅降低外貿經營門檻，也有益於偉盛豐貿易將隱形冠軍產品推向全球市場。

偉盛豐貿易 王珮馨

圖／ 數位時代

## 善用 AI 工具，加樂實業以 Alibaba.com 維運 70% 外貿營收

深耕建築五金市場的加樂實業，也高度肯定 Alibaba.com 在其拓展全球市場過程中的重要角色。加樂實業總經理王拓白表示，公司早在 19 年前便開始使用 Alibaba.com，隨著 Alibaba.com 台灣在地團隊成立，不僅協助加樂實業更有效掌握平台功能，也透過多元課程與培訓活動協助提升跨境電商經營能力，讓公司能以更有效率的方式推動外貿業務，同時將管理工作負擔降低約 50%，員工流動率也減少約 20%。

王拓白指出，加樂實業長期以外貿市場為主要營收來源。過去公司主要透過參加國際展會拓展客戶，一場展覽平均可取得近 70-100 個潛在客戶名單；但在加入 Alibaba.com 後，每月至少能收到超過 350 筆客戶詢問，不僅大幅提升商機來源，也成功培養出年貢獻「億元級」營收的客戶，並將業務版圖拓展至《財富》500 大企業與全球安防領先品牌。

舉例來說，2016 年，加樂實業透過 Alibaba.com 接觸到一名來自澳洲的客戶，最初訂單僅 50 件產品，但在長期合作與信任累積下，訂單量逐年增加，如今已成為公司最大客戶之一，單一客戶一年貢獻營收突破億元。

隨著跨境電商經營的逐漸成熟，加樂實業的外貿結構也出現顯著轉變：過去外貿營收幾乎 100% 來自展會客戶，如今已有高達 70% 的外貿營收來自 Alibaba.com，顯示平台已成為加樂實業拓展全球市場的重要管道。

雙方長期建立的合作默契與信任，也讓加樂實業得以率先導入 Alibaba.com 的 AI 工具並取得實際成效。王拓白以 OKKI CRM 為例說明：「曾有一位合作長達 15 年的客戶訂單突然下滑，我們透過客戶數據分析發現對方開始向其他供應商採購，進一步拜訪後才了解，客戶因為更換經營團隊，產品策略從高階市場轉向平價市場，我們隨即調整產品規格與報價策略，逐步把訂單爭取回來。」

![#2 AI 改寫外貿規則！Alibaba.com 用 AI 助台灣中小企業提升跨境獲客力](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/7jaa-1775011352.jpg?w=1200&output=webp)

加樂實業總經理 王拓白

圖／ 數位時代

此外，加樂實業也透過 OKKI AiReach 進行自動化商機開發：只需輸入相關條件，系統便能自動搜尋並篩選潛在客戶名單，在一個月內，挖掘出 748 名潛在客戶並自動發送產品資訊，成功與俄羅斯、美國、杜拜與澳洲等市場的 5 家企業展開合作洽談。

「AiReach 挖掘出的客戶輪廓相當精準，是我們鎖定的進口商與品牌商，因此能大幅提升陌生開發的效率與成交率。」王拓白表示，Alibaba.com 與 AI 工具不僅讓團隊成員可以高效完成跨境電商營運、深入了解市場與客戶動態，更重要的是，可以化被動為主動的布局全球市場，未來將持續深化應用雙方合作與平台工具應用。

偉盛豐貿易跟加樂實業不是特殊案例，Alibaba.com 除持續優化產品服務，更積極協助台灣中小企業跨越全球外貿市場布局門檻，讓其可以更便利且精準的方式提升外貿接單力，創造生態夥伴的共贏。

#### Alibaba.com

Website: [https://seller.alibaba.com/tw](https://seller.alibaba.com/tw)

Facebook: [https://www.facebook.com/AlibabaTW](https://www.facebook.com/AlibabaTW)

Spotify: [https://open.spotify.com/show/7IJmBg9V8hjsjxyFPRxmDI?si=66gqnCx2TqiQ91fSWoUqyQ](https://open.spotify.com/show/7IJmBg9V8hjsjxyFPRxmDI?si=66gqnCx2TqiQ91fSWoUqyQ)

即時熱門文章

[1 Claude Code只發揮1成實力？7個設定目錄完整教學，讓AI每次都按你的規則工作](https://www.bnext.com.tw/article/90642/claude-code-folder-config-guide) [2 不用Obsidian也能建AI知識庫！Karpathy同款「說明書」設定，4.1萬人超人氣方法完整拆解](https://www.bnext.com.tw/article/90650/andrej-karpathy-ai-how) [3 Chrome內建Gemini Skills！輸入「/」叫出提示詞，跨分頁比價、掃文件一鍵搞定](https://www.bnext.com.tw/article/90647/google-chrome-gemini-skills-save-ai-prompts) [4 不只是共享辦公室，更是企業孵化器！韻驊如何運用空間與資源，加速企業成長？](https://www.bnext.com.tw/article/90413/vqznxduk) [5 AI 改寫外貿規則！Alibaba.com 用 AI 助台灣中小企業提升跨境獲客力](https://www.bnext.com.tw/article/90494/alibaba.com115129) [6 AI做95%、你做5%！Anthropic執行長：槓桿效應讓人類貢獻放大20倍，比較優勢反而更關鍵](https://www.bnext.com.tw/article/90636/anthropic-dario-amodei-ai-task)

[![AI全球100+台灣20](https://image-cdn.learnin.tw/bnextmedia/image/album/2026-04/47ru-1775031962.jpg?w=600&output=webp)](https://www.bnext.com.tw/magazine/view/130126)