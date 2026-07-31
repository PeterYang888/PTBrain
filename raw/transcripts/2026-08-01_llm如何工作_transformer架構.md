---
type: source
tags: [ai, llm, transformer, attention, 科普]
created: 2026-08-01
updated: 2026-08-01
source_url: https://www.youtube.com/watch?v=jFuft0mKj7E
source_date: 2026-08-01
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  channel: "最佳拍檔"
  processed_by: notebooklm-py
---

這是一份針對影片《大語言模型是如何工作的》所整理的技術原理簡報：

## 一句話摘要

本影片深入淺出地拆解了現代大語言模型（LLM）從輸入文字、分詞、嵌入、位置編碼，到 Transformer 架構核心（注意力機制與前饋網路）及殘差流的完整運算流程與技術演進。

## 主講者背景

主講者為**大飛**，來自 YouTube 頻道「**最佳拍檔**」。他的講述風格偏向科普教學，擅長將艱澀的技術論文轉化為直覺的比喻，幫助非技術背景的觀眾理解模型內部的運算邏輯。

## 核心論點

*   **分詞與嵌入（Tokenization & Embedding）**：模型不直接讀取文字，而是透過 Tokenization 將文本轉為整數 ID，再經由 Embedding 矩陣查找出具備語義特徵的高維向量 [1-3]。
*   **位置資訊的賦予**：由於注意力機制本身不具備順序感，現代模型多採用 **RoPE（旋轉位置編碼）**，透過旋轉向量角度來編碼 Token 之間的相對位置關係 [4, 5]。
*   **注意力機制（Attention）**：透過 Q（Query）、K（Key）、V（Value）的匹配與權重分配，讓模型在預測下一個詞時，能跨越距離捕捉上下文的關聯性（如動詞找主語） [6, 7]。
*   **前饋網路（FFN）與知識存儲**：每一層中除了交換資訊，更透過 FFN 進行深加工；研究顯示模型的「事實記憶」（如巴黎是法國首都）主要存儲於 FFN 的參數與激活模式中 [8-10]。
*   **穩定訓練的機械部件**：**殘差連接（Residual Connections）**與**層歸一化（Layer Norm）**確保了數十層深的模型在訓練時不會出現數值爆炸或塌縮，維持信號傳遞 [11, 12]。
*   **生成循環（Generation Loop）**：基礎模型（Base LLM）本質上只做「預測下一個 Token」這件事，透過不斷將預測結果追加回輸入端，實現連貫的文本輸出 [13, 14]。

## 關鍵細節與數據

*   **模型架構與參數**：
    *   **7B 參數模型**：常見隱藏維度（Hidden Dimension）長度為 **4096** [3]。
    *   **LLaMA-2 70B**：採用 **GQA（分組查詢注意力）**，擁有 64 個查詢頭（Query Heads）但僅 8 個 KV 頭（KV Heads） [8]。
    *   **Mixtral 8x7B**：**MoE（混合專家模型）**，每層 8 個專家，每個 Token 僅激活 2 個，總參數 467 億，但實際運算僅約 129 億 [10]。
*   **關鍵年份與技術名稱**：
    *   **2015 年**：何愷明等人提出 **ResNet**（殘差網絡） [11]。
    *   **2017 年**：Google 發表經典論文《**Attention Is All You Need**》，提出原始 Transformer [4]。
    *   **2021 年**：蘇劍林等人提出 **RoPE（旋轉位置編碼）** [4]。
    *   **2022 年**：Anthropic 發現 **Induction Heads（歸一頭）** 解釋了上下文學習機制 [7]。
*   **數學公式與演算法**：
    *   **分詞演算法**：GPT 系列用 **BPE（位元組對編碼）**，LLaMA 系列常用 **SentencePiece** [2]。
    *   **激活函數（Non-linearity）**：演進過程為 ReLU → GELU → **SwiGLU** [9]。
    *   **注意力機制**：Q、K 做「縮放點積」（Scaled Dot-product），再透過 **Softmax** 函數轉化為權重 [6]。
    *   **歸一化函數**：現代模型從 Post-norm 轉向 **Pre-norm**，並常使用更簡單的 **RMSNorm** [12]。
*   **重要比喻**：
    *   **Embedding 算術**：`King - Man + Woman ≈ Queen` 展示了語義空間的幾何結構 [3]。
    *   **殘差流（Residual Stream）**：比喻為一條「高速公路」，各組件從中讀取資訊並將結果寫回，而不覆蓋原始資訊 [11]。
    *   **QKV 機制**：Query（我在找什麼）、Key（我能提供什麼）、Value（匹配成功後的實際資訊） [6]。

## 重要引言

*   「**嵌入只編碼了這個 Token 是什麼，完全不知道這個 Token 在序列裡的位置。**」—— 解釋為什麼需要位置編碼（Positional Encoding）來填補語義資訊的缺口 [3, 4]。
*   「**注意力是 Token 之間互相交談、交換信息，那前饋網絡（FFN）就是每個 Token 關起門來獨自做深加工。**」—— 對比 Transformer 兩大核心組件的不同功能 [8, 9]。
* 「**基礎模型沒有被直接針對事實準確性、對話能力或寫程式來訓練，它只是在預測下一個最可能的 Token。**」—— 強調對齊（Alignment）與微調在開發過程中的重要性 [14]。
*   「**預測下一個 Token 這個單一目標，就是基礎大語言模型全部的訓練信號。**」—— 揭示 LLM 訓練的底層驅動力 [14]。

## 與其他 AI 主題的關聯

*   **長上下文瓶頸（Long Context Problems）**：影片提到 **Lost in the Middle** 現象（中間迷失），即便有 RoPE，模型對提示詞中間部分的處理仍不如開頭與結尾可靠 [5]。
*   **效率優化技術**：為了降低注意力機制的 $O(n^2)$ 計算代價，衍生出 **FlashAttention**、**稀疏注意力**與**投機解碼（Speculative Decoding）**等研究方向 [14, 15]。
*   **架構替代方案**：提到 **Mamba** 等**狀態空間模型（SSM）**，被視為處理超長序列時具備天然優勢的 Transformer 潛在替代方案 [16]。
*   **可解釋性研究（Interpretability）**：透過 **ROME（Rank-One Model Editing）** 等方法，研究者已能對模型內的特定 FFN 權重進行「手術式」修改，例如將「巴黎」改為「羅馬」 [10]。
