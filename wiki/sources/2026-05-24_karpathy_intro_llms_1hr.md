---
type: source
tags: [LLM, AI技術原理, Karpathy, LLM-OS, 安全]
created: 2026-05-24
source_url: https://www.youtube.com/watch?v=zjkBMFhNj_g
source_date: 2023-11-01
source_type: transcript
---

# [1hr Talk] Intro to Large Language Models — Andrej Karpathy

> 來源：YouTube · [[Andrej_Karpathy]]

## 一句話摘要
全面解析大型語言模型的技術指南，涵蓋訓練流程（預訓練、微調、RLHF）到未來「LLM 作業系統」的核心願景，並深入探討隨之而來的安全挑戰。

## 核心論點
- **LLM 本質是兩個文件**：「參數文件」（大腦權重）+ 「運行代碼」（約 500 行 C 語言），即可離線在筆電運行
- **互聯網的有損壓縮**：數十 TB 文本壓縮進數百億參數，形成對知識的機率性「完形（Gestalt）」
- **三階段訓練體系**：預訓練（知識獲取）→ 指令微調（對話行為）→ 強化學習 RLHF（比較提升）
- **規模定律（Scaling Laws）**：模型表現是參數量 N 與訓練數據量 D 的平滑函數；增加算力幾乎保證性能提升
- **邁向「系統二」思維**：目前 LLM 僅具快思考（系統一），未來賦予「思考時間」實現慢思考複雜推理
- **LLM 作為操作系統（LLM OS）**：LLM 作為內核，協調記憶（Context）、外部工具（搜尋/代碼執行）與多模態輸出
- **安全挑戰的新戰場**：越獄（Jailbreak）、提示詞注入（Prompt Injection）、數據投毒等全新漏洞

## 關鍵細節與數據
- **Llama 2-70B 規格**：700 億參數，參數文件 ≈ **140 GB**；訓練需 10TB 文本、6,000 顆 GPU、12 天，成本 ≈ **200 萬美元**
- 閉源模型（GPT-4、Claude 3）仍優於開源權重模型（Llama 系列）
- Context Window = **AI 的 RAM**，極其有限且珍貴

## 值得引用的段落
> 「你可以把 LLM 想像成一個 1TB 的有損壓縮檔，它記得網際網路的大概樣子。」

> **奶奶越獄法**：要求 AI 扮演「過世的奶奶教我做凝固汽油彈」，繞過安全機制。

> **反向偏誤（Reversal Curse）**：模型知道「湯姆克魯斯的母親是誰」，卻答不出「某某人是誰的兒子」。

> **隱形指令攻擊**：在網頁加入白色（隱形）文字，誤導 AI 執行竊取數據等惡意任務。

## 連結到的 wiki
- [[Andrej_Karpathy]]
- [[推理模型]]
- [[RLHF]]
- [[RAG]]
- [[Agentic_Workflow]]
- [[AI_Alignment]]
- [[AGI]]
- [[延伸思考]]

## 我的問題 / 待追蹤
- LLM OS 的具體架構如何實現？現在有哪些框架最接近這個願景？
- Prompt Injection 攻擊有哪些防禦方式？
