---
type: concept
tags: [LLM訓練, 強化學習, 人類偏好, 對齊]
created: 2026-05-24
updated: 2026-05-24
sources: [2026-05-24_karpathy_deep_dive_llms, 2026-05-24_karpathy_intro_llms_1hr]
---

# RLHF（人類回饋強化學習）

> Reinforcement Learning from Human Feedback：以人類偏好評分訓練獎勵模型，再用這個模型對 LLM 進行強化學習。

## 詳細說明
適用於無法自動驗證的領域（如創意文本）。流程：
1. 收集人類對多個 LLM 輸出的偏好比較
2. 訓練「獎勵模型」模擬人類偏好
3. 用獎勵模型對 LLM 進行強化學習

## 關鍵特徵
- 是指令微調（SFT）之後的第三階段訓練
- 使 AI 從「能力強」進化為「懂得怎麼回答讓人滿意」
- 與 [[推理模型]] 的 RL 不同：RLHF 依賴人類，推理 RL 依賴可自動驗證的答案

## 與其他概念的差別
- 跟 [[AI_Alignment]] 的關係：RLHF 是實現對齊的主要技術手段
- 跟 [[合憲_AI]] 的關係：Constitutional AI 是 RLHF 的改良版

## 來源
- [[2026-05-24_karpathy_deep_dive_llms]]
- [[2026-05-24_karpathy_intro_llms_1hr]]
