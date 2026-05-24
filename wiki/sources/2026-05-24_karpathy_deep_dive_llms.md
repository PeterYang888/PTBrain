---
type: source
tags: [LLM, AI技術原理, Karpathy, 預訓練, 強化學習]
created: 2026-05-24
source_url: https://www.youtube.com/watch?v=7xTGNNLPyMI
source_date: 2025-01-01
source_type: transcript
---

# Deep Dive into LLMs like ChatGPT — Andrej Karpathy

> 來源：YouTube · [[Andrej_Karpathy]]

## 一句話摘要
全面探討 LLM 從預訓練、指令微調到強化學習（RL）的技術指南，解釋 AI 如何從「統計 Token 模擬器」演變為具備「思考能力」的數位助理，並揭示認知能力的邊界。

## 核心論點
- **LLM 是網路數據的「有損壓縮」**：數十 TB 文本壓縮進神經網路，形成機率性模糊記憶
- **Token 是 AI 的基本原子**：處理 Token 區塊而非字元，導致拼寫/計數任務可能出錯
- **訓練的三大支柱**：
  1. **預訓練（Pre-training）**：獲取知識，產出「基礎模型」
  2. **指令微調（SFT）**：模仿人類對話行為，產出「助理模型」
  3. **強化學習（RL）**：透過實踐與獎勵發現最優推理路徑，產出「推理模型」
- **「Token 運算」決定思考深度**：每個 Token 的運算量固定，複雜推理需更多 Token（即「思考時間」）
- **Context Window 是「工作記憶」**：相對於參數中的長期模糊記憶，上下文是精確的工作記憶
- **思考能力的湧現**：RL 下 AI 自發學會「自我檢查」、「回溯」、「嘗試不同路徑」
- **瑞士起司能力模型**：AI 可解決博士級科學問題，卻可能答錯 9.11 與 9.9 誰大

## 關鍵細節與數據
- Fine-web 數據集約 **44TB**，包含約 **15 兆 Token**
- GPT-4 Token 字典：約 **10 萬（100,277）**個符號
- GPT-2 級模型訓練成本：從 2019 年 **4 萬美元** → 現在約 **100 美元**
- 訓練最尖端模型需 **10 萬顆 H100 GPU**
- 推理模型（o1、DeepSeek R1）vs 一般模型（GPT-4o）的核心差異：大規模 RL

## 值得引用的段落
> 「嗨，我是 ChatGPT。我是個 1TB 的壓縮檔。我的知識來自網路，但我只記得大概，且個性是由人類設定的。」

> AlphaGo 的 Move 37：RL 讓 AI 在推理領域發現人類未曾想過的絕妙「走法」。

> 草莓（Strawberry）計數：AI 因 Token 化機制而數不清單字中「R」的數量。

## 連結到的 wiki
- [[Andrej_Karpathy]]
- [[推理模型]]
- [[RLHF]]
- [[Agentic_Workflow]]
- [[AGI]]
- [[DeepSeek]]
- [[延伸思考]]

## 我的問題 / 待追蹤
- RL 訓練的「自動獎勵函數」在哪些領域目前無法自動化？
- Token 化機制改進方向？
