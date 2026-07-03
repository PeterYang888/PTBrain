---
type: entity
entity_type: product
tags: [ai, image-generation, flux, open-source]
created: 2026-06-27
updated: 2026-06-27
sources: [2026-06-27_flux2_klein, 2026-06-27_comfyui_v8整合包]
---

# FLUX

> 黑森林實驗室 (Black Forest Labs) 的開源文生圖/圖像編輯模型家族；FLUX.2 Klein (CL) 是 2026 年 1 月的輕量「統一性」版本，主打低門檻、快速、可編輯，被稱為「性價比小鋼砲」。

## 關鍵事實（FLUX.2 Klein）
- **統一性模型**：單一文件同時做文生圖、單圖編輯（換裝/視角/修復老照片）、多圖組合
- **編輯為舒適區**：提示詞核心是「描述變化而非內容」，顯存佔用低於千問等重型模型
- **版本**：9B / 4B，各有基礎版與蒸餾版；推薦 **9B 蒸餾版**（效果遠優於 4B）
- **格式/顯存**：BF16 18.2G（12G 顯存）/ FP8 9.43G（6G 顯存）/ NVFP4 5.76G（限 NVIDIA Blackwell 50 系）
- **速度**：蒸餾模型僅 **4–6 步**，4080 出 720x1280 約 5 秒；最佳約 100 萬像素
- **推薦參數**：6 步、**[[CFG]]=1**、Euler + Simple；多圖參考 ≤ 4 張
- **文本編碼器**：採用千問（Qwen）系列（9B 搭 38B、4B 搭 34B）
- **局限**：複雜長提示英文更穩；複雜空間關係與手指仍會出錯

## 與其他頁的關係
- 與 [[Stable_Diffusion]] 同屬開源文生圖路線，原理見 [[擴散模型]]
- 主要在 [[ComfyUI]] 中運作（需內核 V0.9.2↑）；[[2026-06-27_comfyui_v8整合包|ComfyUI V8 包]] 已預裝 Flux 2

## 相關來源
- [[2026-06-27_flux2_klein]] — FLUX.2 Klein 深度評測
- [[2026-06-27_comfyui_v8整合包]] — 整合包預裝 Flux 2
