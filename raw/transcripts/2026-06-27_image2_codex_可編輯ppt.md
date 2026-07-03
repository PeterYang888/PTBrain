---
type: source
tags: [ai, codex, ppt, workflow]
created: 2026-06-27
updated: 2026-06-27
source_url: https://www.youtube.com/watch?v=S4uYjG_AzXU
source_date: 2026-06-27
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "阿達的AI思辨"
  processed_by: notebooklm-py
---

# Image2 + Codex：真能做可編輯 PPT 的終極形態

## 一句話摘要
透過 Codex 結合開源的 PPT Master 技能，將 GPT Image 2 生成的高美感靜態圖片轉化為具備元素級、可編輯內容的 PPT 檔案。

## 頻道/主講者背景
主講者來自 YouTube 頻道「阿達的AI思辨」。

## 核心論點
- **終結「圖片型 PPT」的局限**：傳統 AI 工具生成的 PPT 往往只是不可編輯的圖片，本方法讓 AI 產出的美感設計能被二次編輯。
- **高美感的精準復刻**：利用 Pinterest 的風格模板配合 GPT Image 2，產出美觀度與還原度極高的版面。
- **結構化設計思維**：不應直接讓 AI 籠統產出，而是先用思考模型設計 PPT 骨架大綱，再進行視覺化生成。
- **技能化（Skill-based）工作流**：將 GitHub 開源項目封裝為 Codex 的 Skill，把複雜的圖像拆解與轉化簡化為單一指令。

## 關鍵細節與數據
- **核心工具組**：
  - **Codex**：主要執行環境。
  - **PPT Master**：GitHub 上的開源項目，作為 Codex 的 Skill 調用。
  - **GPT Image 2**：負責將文案與風格模板結合，生成高質量靜態 PPT 圖片。
  - **Pinterest**：尋找風格化 PPT 模板的參考網站。
- **操作步驟**：
  1. 將 PPT Master 的倉庫地址複製丟給 Codex 安裝。
  2. 用 AI 思考模型生成內容大綱（範例為 6 頁 PPT 大綱）。
  3. 將參考圖與文案交給 Image 2 產出靜態圖並批量下載。
  4. 在 Codex 呼叫 `/PPT Master`，要求「把這份文檔做成可編輯的 PPT」。
- **效能與消耗**：製作 6 頁可編輯 PPT 耗時約 **6 分 17 秒**；5 小時配額中花費 **13**；推理強度設定為 **5.5 高**。

## 值得引用的金句
- 「AI 做 PPT，終於不是圖片了，這才是 AI 做 PPT 的終極形態。」——形容解決不可編輯痛點後的突破。
- 「關於 PPT 的骨架內容，我也建議大家用 AI 去寫，不要去籠統的讓它給一份。」——強調內容結構化設計的重要性。

## 與其他 AI 工具/概念的關聯
- **Codex Skill 擴展**：展示 Codex 能透過引入 GitHub 開源倉庫（如 PPT Master）獲取原本不具備的特定處理能力。
- **Workflow Automation**：一套「參考取樣 → AI 繪圖 → 技能轉化」的自動化流程，把設計師手動排版轉為 AI 邏輯處理。
- **多模型協作**：結合 GPT 思考模型（內容規劃）、Image 2（視覺生成）與 Codex（格式轉化），體現 Agent 協作模式。
