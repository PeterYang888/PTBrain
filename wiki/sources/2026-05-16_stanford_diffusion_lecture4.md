---
type: source
tags: [Stanford, 擴散模型, VAE, CLIP, CFG, 潛在空間]
created: 2026-05-16
source_url: https://www.youtube.com/watch?v=WUUq6TVAu8U
source_date: 2026-05-16
source_type: transcript
---

# Stanford CME296 Lecture 4：潛在空間與引導式生成

> 來源：[原始檔](../../raw/transcripts/Stanford_Diffusion_Lecture4_transcript.md)

## 一句話摘要
CME296 第 4 講從無條件生成轉向引導式生成：VAE 建立潛在空間、CLIP 實現跨模態對齊、CFG（無分類器引導）成為工業標準，三者構成現代文生圖系統的技術核心。

## 核心論點
- 為何需要潛在空間：像素空間維度過高（1024×1024 超過百萬維），VAE 壓縮成高效緊湊空間
- VAE 損失函數：重建損失（L2）+ 正則化損失（KL 散度），但需結合感知損失（LPIPS）和 GAN 對抗損失解決模糊問題
- CLIP 透過對比學習實現圖文對齊，是多模態條件表示的基礎組件
- CFG（Classifier-Free Guidance）：訓練時隨機丟棄條件，推理時引導係數 w>1 強化條件特徵；代價是兩次前向傳播

## 值得引用的段落
> 「如果你不使用這個超參數（引導係數 w），你得到的圖像可能不會緊密遵循你的提示。」

## 連結到的 wiki
- [[擴散模型]]
- [[VAE]]
- [[CLIP]]
- [[CFG]]
- [[潛在空間]]

## 擴充細節

### 為何不用像素空間
- 1024×1024 圖片 = 約 **300 萬維度**（H × W × 3 channels）
- 像素空間問題：高維、冗餘（鄰近像素高度相似）、不連續（稍加噪音得到無意義圖像）

### Autoencoder vs VAE
| | Autoencoder | VAE |
|---|---|---|
| 潛在空間 | 點映射，任意分布 | 映射到分布（預測 μ, σ²），強制近似標準正態 |
| 重建質量 | 較清晰但潛在空間無結構 | 結構化但有模糊問題 |
| 生成能力 | 差（空間不連續） | 好（可從 N(0,I) 採樣） |

### VAE 損失函數（ELBO 推導）
- **重建損失**：像素 L2（鼓勵精確重建）
- **正則化損失**：KL 散度 D_KL(q_φ(z|x) || p(z))（強制潛在分布貼近標準正態）
- **模糊問題根因**：像素 L2 在不確定性下取平均 → 輸出模糊

### 解決模糊的兩個策略
1. **感知損失（LPIPS）**：比較特徵圖（feature maps）而非原始像素，容忍小幅空間偏移
2. **對抗損失（GAN）**：訓練判別器區分真假圖像，驅使解碼器生成更真實的輸出

### CLIP 架構
- 圖像編碼器（ViT）和文字編碼器（Transformer）各自輸出嵌入向量，投影到同一共享空間
- 訓練：對比損失（同批次中正樣本對相似度最大化，負樣本對最小化）
- 數據：網路爬取 4 億圖文對（圖片 alt tag + 圖片）
- 後續改進：SigLIP（Sigmoid Loss，逐對判斷而非批次 softmax，效率更高）

### ViT（Vision Transformer）
- 圖像切成 patches → 每個 patch 線性投影為 embedding（類比文字 token）
- 加入位置編碼後，過 Transformer encoder
- CLS token 的輸出 = 圖像的全局語義表示

### Classifier Guidance vs CFG

| | Classifier Guidance | Classifier-Free Guidance (CFG) |
|---|---|---|
| 需要額外分類器 | 是（需在噪聲圖訓練） | 否 |
| 推理成本 | 高（需反向傳播計算梯度） | 中（兩次前向傳播） |
| 工業採用 | 少 | 主流 |
| 引導公式 | 移動 μ 加上分類器梯度 | ε_guided = ε_uncond + w · (ε_cond − ε_uncond) |

### 訓練與推理流程
- **訓練**：先訓練 VAE（固定），再在潛在空間訓練流匹配/擴散模型
- **推理**：從潛在空間 Gaussian 採樣 → 流匹配 ODE 求解 → VAE 解碼器解碼到像素空間

### 編碼器 vs 解碼器的角色分工
- **編碼器**：捕捉語義相似性（讓擴散模型好學）
- **解碼器**：還原感知細節（實際用的 VAE 中解碼器比編碼器大）

## 我的問題 / 待追蹤
- 第 5 講是否進入 DiT（Diffusion Transformer）架構？
- FLUX、SD3 等最新模型是否仍使用 CFG 還是已有替代（如 Flow Matching + CFG free）？
