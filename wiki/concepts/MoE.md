---
type: concept
tags: [ai, llm, transformer, efficiency]
created: 2026-08-01
updated: 2026-08-01
sources: [2026-08-01_llm如何工作_transformer架構]
---

# MoE（Mixture of Experts，混合專家模型）

> 把 [[Transformer]] 的前饋網路（FFN）拆成多個「專家」子網路，每個 Token 只路由到其中少數幾個。總參數量很大，但單次運算量小。

## 核心取捨
**稀疏激活**：用「總參數量」買知識容量，用「激活參數量」付運算成本。

以 **Mixtral 8x7B** 為例：
| 指標 | 數值 |
|---|---|
| 每層專家數 | 8 |
| 每個 Token 激活 | 2 個 |
| 總參數 | 約 **467 億** |
| 實際運算參數 | 約 **129 億** |

即：記憶體要裝得下 467 億，但每個 Token 的計算只花 129 億的代價。

## 為什麼作用在 FFN 層
因為 FFN 是 [[Transformer]] 裡負責「事實記憶」與非線性深加工的部分，參數量佔比最大，也最適合切分成專精不同領域的專家。[[注意力機制]] 層則通常不做 MoE。

## 與其他概念的關係
- 是 [[Transformer]] 的效率演進路線之一，與 GQA（壓 KV cache）、FlashAttention（壓注意力計算）互補而非互斥
- 影響模型部署的實務判斷：MoE 模型的「參數量」不能直接拿來跟稠密模型比推論成本

## 來源
- [[2026-08-01_llm如何工作_transformer架構]]
