---
type: concept
tags: [深度學習, 多模態, 對比學習, 文生圖]
created: 2026-05-20
updated: 2026-05-20
sources: [2026-05-16_stanford_diffusion_lecture4]
---

# CLIP（對比語言-圖像預訓練）

> Contrastive Language-Image Pre-training；OpenAI 提出的多模態模型，透過對比學習將圖像和文字投影到同一共享嵌入空間，實現圖文語義對齊；是現代文生圖系統（如 Stable Diffusion、DALL-E）提供文字條件的核心組件。

## 架構
- **圖像編碼器**（ViT 或 CNN）：將圖像轉為嵌入向量
- **文字編碼器**（Transformer）：將文字轉為嵌入向量
- **投影層**：將兩種嵌入投影到同一共享空間，使其可直接計算相似度

## 訓練方式（對比學習）
- 數據：從網路爬取 **4 億對**圖文（圖片 + alt tag）
- 損失：批次內對比學習（In-batch negatives）
  - 同批次中：真正配對的圖文 → 高相似度
  - 同批次中：不配對的圖文 → 低相似度
- 不需人工標注，自監督

## 改進版：SigLIP
- 以 Sigmoid Loss 替代 Softmax
- 逐對判斷（圖文是否匹配）而非批次 Softmax
- 優點：不需建立相似度矩陣，效率更高，語義更精準

## ViT（Vision Transformer）
- 將圖像切成 patches → 線性投影為 embedding（類比文字 token）
- 加位置編碼 → 過 Transformer encoder
- CLS token 輸出 = 圖像全局語義表示

## 語義相似 vs 感知相似
- **語義相似**（CLIP 捕捉）：整體代表相同的事物（兩張不同角度的泰迪熊）
- **感知相似**：細節紋理對人眼相似（同一場景的不同渲染）

## 在文生圖系統中的角色
- 將用戶文字 prompt 編碼為條件向量，透過 Cross-Attention 注入擴散模型
- 搭配 [[CFG]] 引導生成方向

## 來源
- [[2026-05-16_stanford_diffusion_lecture4]]

## 相關概念
- [[VAE]]（提供潛在空間）
- [[CFG]]（引導機制）
- [[擴散模型]]（整合系統）
