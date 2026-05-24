---
type: concept
tags: [深度學習, 擴散模型, 條件生成, 文生圖]
created: 2026-05-20
updated: 2026-05-20
sources: [2026-05-16_stanford_diffusion_lecture4]
---

# CFG（無分類器引導）

> Classifier-Free Guidance；現代文生圖系統的標準引導機制，在不依賴外部分類器的情況下，透過混合有條件和無條件的噪聲預測來強化生成結果與 prompt 的對齊程度。

## 背景：為何需要「引導」
擴散模型在訓練和推理時，若只用條件噪聲預測 ε_cond，生成的圖像往往不夠緊密遵循 prompt。CFG 透過「放大條件信號」來解決這個問題。

## 核心公式
```
ε_guided = ε_uncond + w × (ε_cond − ε_uncond)
```
- `ε_uncond`：無條件預測（不看 prompt）
- `ε_cond`：有條件預測（看 prompt）
- `w`：引導強度（通常設 3–7）；w=1 等同無引導，w 越大越緊貼 prompt 但多樣性越低

## 對比：Classifier Guidance vs CFG
| | Classifier Guidance | Classifier-Free Guidance |
|---|---|---|
| 額外模型 | 需要在噪聲圖上訓練的分類器 | 不需要 |
| 推理成本 | 高（需反向傳播計算梯度） | 中（兩次前向傳播） |
| 工業採用 | 少見 | **主流** |
| 靈活性 | 受限於分類器能力 | 只需要訓練一個模型 |

## 訓練方式
- 以 10–20% 的機率丟棄條件（unconditional probability），模型學會同時處理有條件和無條件生成
- 推理時：分別跑一次有條件 + 一次無條件，兩次前向傳播的成本

## 與 w 值的關係
- `w` 太小：圖像不緊貼 prompt
- `w` 太大：圖像失去多樣性，過度飽和
- 實務上 3–7 是常見範圍

## 在文生圖系統中的地位
FLUX、Stable Diffusion、DALL-E 3 等主流模型均使用 CFG 或其變體作為引導機制。

## 來源
- [[2026-05-16_stanford_diffusion_lecture4]]

## 相關概念
- [[擴散模型]]（使用 CFG 的系統）
- [[VAE]]（潛在空間）
- [[CLIP]]（提供條件向量）
