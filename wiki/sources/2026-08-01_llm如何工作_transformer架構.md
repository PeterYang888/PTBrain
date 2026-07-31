---
type: source
tags: [ai, llm, transformer, attention, 科普]
created: 2026-08-01
updated: 2026-08-01
source_url: https://www.youtube.com/watch?v=jFuft0mKj7E
source_date: 2026-08-01
source_type: transcript
---

# 大語言模型是如何工作的：從分詞到生成的完整拆解

> 來源：[原始檔](../../raw/transcripts/2026-08-01_llm如何工作_transformer架構.md) · 主講：[[大飛]]（頻道「最佳拍檔」）

## 一句話摘要
把 LLM 的一次前向運算完整拆開——[[Tokenization]] → Embedding → [[位置編碼]] → [[注意力機制]] → [[前饋網路]] → 殘差流 → 下一個 Token，並補上 [[MoE]]、[[GQA]] 等現代效率架構的演進脈絡。

## 核心論點
- **模型不讀文字，只讀向量**：Tokenization 把文本轉成整數 ID，Embedding 矩陣再查出帶語義特徵的高維向量
- **位置感必須額外注入**：[[注意力機制]] 本身不具順序感，現代模型多用 **RoPE**（旋轉位置編碼）以旋轉向量角度來編碼相對位置
- **注意力＝Token 之間交談**：Q（我在找什麼）／K（我能提供什麼）／V（匹配後的實際資訊）三者匹配後分配權重，跨距離捕捉關聯（如動詞找主語）
- **FFN＝Token 自己關門深加工**：研究顯示模型的「事實記憶」（如巴黎是法國首都）主要存在 FFN 的參數與激活模式中
- **殘差連接與 Layer Norm 是機械穩定件**：確保數十層深的網路訓練時不數值爆炸或塌縮
- **生成只是把預測結果接回輸入**：Base LLM 本質只做「預測下一個 Token」，反覆追加即產生連貫文本

## 關鍵數據
- **7B 模型**：常見隱藏維度（Hidden Dimension）**4096**
- **LLaMA-2 70B**：採 **GQA（分組查詢注意力）**，64 個 Query Head 但僅 **8 個 KV Head**
- **Mixtral 8x7B**：[[MoE]]，每層 8 專家、每 Token 僅激活 2 個；總參數 **467 億**，實際運算約 **129 億**
- **2015** 何愷明等提出 ResNet（殘差網路）｜**2017** Google《Attention Is All You Need》｜**2021** 蘇劍林等提出 RoPE｜**2022** [[Anthropic]] 發現 **Induction Heads**，解釋 in-context learning
- 分詞演算法：GPT 系列 **BPE**，LLaMA 系列常用 **SentencePiece**
- [[激活函數]]演進：ReLU → GELU → **SwiGLU**；歸一化由 Post-norm 轉 **Pre-norm**，並常用更簡單的 **RMSNorm**

## 關鍵比喻
- **殘差流＝高速公路**：各組件從流中讀取資訊、把結果寫回，而不覆蓋原始資訊
- **Embedding 算術**：`King - Man + Woman ≈ Queen`，展示語義空間的幾何結構
- **QKV**：Query＝我在找什麼、Key＝我能提供什麼、Value＝匹配成功後交出的實際資訊

## 值得引用的段落
> 「嵌入只編碼了這個 Token 是什麼，完全不知道這個 Token 在序列裡的位置。」— 解釋為何需要[[位置編碼]]

> 「注意力是 Token 之間互相交談、交換信息，那前饋網絡（FFN）就是每個 Token 關起門來獨自做深加工。」— 對比 Transformer 兩大組件

> 「預測下一個 Token 這個單一目標，就是基礎大語言模型全部的訓練信號。」— LLM 訓練的底層驅動力

## 與其他概念的關聯
- **長上下文瓶頸**：即便有 RoPE，仍有 **Lost in the Middle**（中間迷失）——模型對提示詞中段的處理不如開頭結尾可靠
- **效率優化**：為降低注意力 $O(n^2)$ 代價，衍生 FlashAttention、稀疏注意力、投機解碼（Speculative Decoding）
- **架構替代**：Mamba 等狀態空間模型（SSM）被視為超長序列的 Transformer 潛在替代
- **可解釋性**：ROME（Rank-One Model Editing）可對特定 FFN 權重做「手術式」修改，例如把「巴黎」改成「羅馬」
- 補上 [[2026-07-10_神經網路_漫士科普]] 未展開的 Transformer 環節：該頁只把 Transformer 列為進階架構，本頁展開其內部

## 連結到的 wiki
- [[Transformer]] · [[注意力機制]] · [[位置編碼]] · [[MoE]] · [[激活函數]] · [[神經網路]] · [[大飛]] · [[Anthropic]]

## 我的問題 / 待追蹤
- 影片為簡體中文來源，本頁術語已轉台灣慣用譯名（如「歸一化」保留原文語感，PTBrain 內文用「正規化／歸一化」皆可）
- briefing 把 Induction Heads 譯為「歸一頭」，應為「歸納頭」之誤；本頁保留英文原名
- 影片提到的 FlashAttention、Mamba、ROME 皆僅點到，PTBrain 尚無專頁 TODO
