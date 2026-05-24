---
type: source
tags: [Stanford, 擴散模型, VAE, CLIP, CFG, 潛在空間, ai-tooling]
created: 2026-05-16
source_url: https://www.youtube.com/watch?v=WUUq6TVAu8U
source_date: 2026-05-16
source_type: transcript
---

# CME296 講義 4 簡報：潛在空間與引導式生成

本簡報針對 Stanford CME296 課程「擴散與大型視覺模型」第四講進行深度分析。本課重點在於從前三講討論的「無條件生成」（Unconditional Generation）轉向「多模態引導生成」（Multimodal Guided Generation），探討如何利用用戶提示（如文本或圖像）來引導圖像生成過程。

---

## 執行摘要

本課程探討了將擴散模型應用於圖像生成時的三大核心挑戰：
1.  **表示空間（Representation Space）：** 為什麼在像素空間（Pixel Space）直接操作效率低下，以及如何透過變分自動編碼器（VAE）構建更高效的「潛在空間」（Latent Space）。
2.  **條件表示（Conditioning Representation）：** 如何使用 Transformer 和視覺 Transformer（ViT）將文本和圖像轉化為機器可理解的嵌入（Embeddings），以及如何透過 CLIP 模型實現跨模態對齊。
3.  **引導機制（Guidance Mechanisms）：** 比較「分類器引導」（Classifier Guidance）與「無分類器引導」（Classifier-Free Guidance, CFG）的優劣，並說明後者為何成為目前工業界的標準。

---

## 核心主題深度分析

### 1. 潛在空間的必要性與變分自動編碼器 (VAE)

在像素空間中進行計算存在維度過高（例如 $1024 \times 1024$ 圖像具有超過 $10^6$ 個維度）、資訊冗餘且空間分佈不均勻（Spiky）等問題。

#### 潛在空間的理想特性：
*   **可處理的維度（Tractable dimension）：** 降低計算負荷。
*   **緊湊的表示（Compact representation）：** 減少冗餘。
*   **有意義的空間（Meaningful space）：** 相似語義的圖像在空間中應鄰近分佈。

#### 變分自動編碼器 (VAE) 的機制：
VAE 不僅是將圖像壓縮為單點，而是預測一個分佈的參數：**平均值 ($\mu$)** 和 **標準差 ($\sigma$)**。
*   **重建損失（Reconstruction Loss）：** 確保輸出圖像與輸入一致（像素級 L2 距離）。
*   **正則化損失（Regularization Loss）：** 使用 KL 散度（KL Divergence）迫使潛在空間符合標準正態分佈。

#### 解決模糊問題：
*   **感知損失（Perceptual Loss, LPIPS）：** 比較圖像在預訓練模型中的特徵圖而非原始像素。
*   **對抗損失（Adversarial Loss）：** 引入判別器（Discriminator）區分真假圖像，迫使解碼器生成更具細節的結果。

---

### 2. 多模態條件表示：CLIP 與跨模態對齊

| 技術組件 | 說明 |
| :--- | :--- |
| **Tokenization** | 將文本分解為原子組件（子詞級別 Subword level）。 |
| **Transformer** | 基於注意力機制（Attention）的架構。透過 Self-Attention 和 Cross-Attention 提取語義。 |
| **ViT (Vision Transformer)** | 將圖像分割成塊（Patches）並視為 Token，使圖像處理能套用 Transformer 架構。 |
| **CLIP 模型** | 透過「對比學習」（Contrastive Learning）訓練，最大化圖像及其對應標題的相似度。 |

---

### 3. 引導式生成機制：從分類器到 CFG

#### 分類器引導 (Classifier Guidance)
*   **原理：** 使用一個額外的分類器對雜訊圖像進行評估，利用分類器的梯度（Gradient）來修正擴散模型的預測路徑。
*   **缺點：** 需要額外訓練一個能處理雜訊圖像的分類器，且反向傳播計算量大。

#### 無分類器引導 (Classifier-Free Guidance, CFG)
*   **原理：** 目前最流行的技術。在訓練時，以一定比例（如 10-20%）隨機丟棄條件，使模型同時學習「有條件生成」和「無條件生成」。
*   **引導係數 ($w$)：** 當 $w > 1$ 時，模型會強化條件特徵。每次推理需要兩次前向傳播（一次有條件，一次無條件）。

---

## 重要語錄與語境

1.  > 「語義相似性指的是全球幾何結構……兩張圖像如果語義相似，意味著它們大致代表相同的東西。而感知相似性指的是局部細節……對人眼來說看起來是一樣的。」

2.  > 「在與擴散模型結合使用的 VAE 中，解碼器實際上比編碼器更大。」

3.  > 「如果你不使用這個超參數（引導係數 $w$），你得到的圖像可能不會緊密遵循你的提示。這就是為什麼我們需要這種引導。」

---

## 行動見解與結論

*   **訓練策略：** 應優先採用潛在擴散模型（LDM）框架。先訓練高品質 VAE 建立壓縮空間，再於該空間內訓練擴散模型。
*   **損失函數優化：** 訓練 VAE 時，單純的 L2 損失不夠，必須結合感知損失和 GAN 對抗損失。
*   **推理優化：** CFG 雖增加兩倍計算開銷（兩次前向傳播），但這是換取圖像與文本高度一致性的必要代價。引導係數 $w$ 是調整「多樣性」與「保真度」之間平衡的關鍵槓桿。
*   **編碼器選擇：** 對於多模態任務，使用 CLIP 等對齊模型提供的嵌入，比單獨訓練文本或圖像編碼器更能有效捕捉跨模態關聯。
