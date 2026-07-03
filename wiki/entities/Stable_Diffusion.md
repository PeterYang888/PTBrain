---
type: entity
entity_type: product
tags: [ai, image-generation, stable-diffusion, open-source]
created: 2026-06-27
updated: 2026-06-27
sources: [2026-06-27_comfyui_基礎教學ep1, 2026-06-27_comfyui_保姆級安裝]
---

# Stable Diffusion

> 開源文生圖模型家族，是 [[ComfyUI]]、WebUI（Forge/Invoke/Automatic1111）等介面背後的共同底層技術；其原理屬 [[擴散模型]]（逐步去噪）。

## 關鍵事實
- **版本與解析度**：SD 1.5 建議 **512x512**（記憶體友善，如 Realistic Vision）；SDXL 建議 **1024x1024**（畫質佳、需更大記憶體，如 Juggernaut）
- **模型格式**：主流以 **Checkpoint（底模）** + **SafeTensor** 格式分發
- **三件套**：clip（文字編碼）/ 底模 Checkpoint / vae，搭配 [[ComfyUI]] 節點使用
- **生態**：[[CivitAI]] 為最主流的模型/LoRA 下載平台；可疊加 ControlNet、LoRA、Upscale

## 與其他頁的關係
- 底層原理見 [[擴散模型]]（VAE / CLIP / CFG 等組件見 [[VAE]]、[[CLIP]]、[[CFG]]）
- 主要操作介面為 [[ComfyUI]]
- 與新一代開源模型 [[FLUX]] 同屬開源文生圖路線（FLUX 主打低門檻、可編輯）

## 相關來源
- [[2026-06-27_comfyui_基礎教學ep1]]
- [[2026-06-27_comfyui_保姆級安裝]]
