---
type: entity
entity_type: product
tags: [ai, image-generation, comfyui, workflow, open-source]
created: 2026-06-27
updated: 2026-07-04
sources: [2026-06-27_comfyui_保姆級安裝, 2026-06-27_comfyui_v8整合包, 2026-06-27_comfyui_系統教程前言, 2026-06-27_comfyui_基礎教學ep1, 2026-07-04_comfyui_零基礎ep01]
---

# ComfyUI

> 開源、節點式（node-based）的 AIGC 工作流工具，是 [[Stable_Diffusion]] 等文生圖/多模態模型的「進階操作介面」；以可視化節點搭建複雜工作流，能做 WebUI 做不到的事。

## 定位
- ComfyUI、Forge、Invoke、Automatic1111（WebUI）本質都是 [[Stable_Diffusion]] 技術的不同操作介面，差異在速度/靈活性/易用性
- ComfyUI 的核心競爭力是**節點式工作流**：可視化節點（Nodes）+ 連接線（Noodles），如樂高積木，無需寫程式即可建複雜任務
- 與 [[擴散模型]] 是「工具 ↔ 底層原理」的關係

## 關鍵事實
- **節點/工作流**：產出圖片內嵌全部設定，拖回介面即復原工作流；可 Export 分享、拖入下載的工作文件自動載入（來自 [[2026-06-27_comfyui_基礎教學ep1]]）
- **Manager**：右上角「Install Missing Custom Nodes」自動修復缺失節點，降低環境維護難度
- **硬體門檻**：VRAM 生圖 8G↑ / 編輯 12G↑ / 影片 16G↑；建議 NVIDIA + 裝 PyTorch（CUDA/DirectML）+ SSD（來自 [[2026-06-27_comfyui_保姆級安裝]]）
- **Desktop 版**：0.4.7 Beta 取代命令列，全自動安裝，支援 Win/Mac
- **整合包路線**：如 V8 包（Python 3.13 / PyTorch 2.10 + CUDA 13）「解壓即用」，預裝多模態模型（視訊 LTX-Video、口型 Infini-Talk、語音 千問TTS、圖編 [[FLUX|Flux 2]]）；啟動器 UI 由 GLM-5 以 [[Vibe_Coding]] 重寫（來自 [[2026-06-27_comfyui_v8整合包]]）
- **模型生態**：自 [[CivitAI]] 下載 Checkpoint（SafeTensor）；核心技術 ControlNet / LoRA / Upscale
- **命令列手動安裝路線**：另有教學走 Python 3.10.9 + Git + venv 虛擬環境的手動配置路線（區別於 Desktop 一鍵版），強調環境隔離避免套件版本衝突；裝完主程式後首要任務是裝 Manager 做視覺化插件管理（來自 [[2026-07-04_comfyui_零基礎ep01]]）

## 與其他頁的關係
- 操作介面之於 [[Stable_Diffusion]] / [[擴散模型]]；多模態整合納入 [[FLUX]] 等模型
- V8 整合包啟動器以 [[Vibe_Coding]] 開發，呼應 [[Andrej_Karpathy]] 的氛圍編程
- 節點式「資料流動 + 處理」概念與 Agent 作業模式相似（每節點 = 具輸入/輸出的任務）

## 相關來源
- [[2026-06-27_comfyui_保姆級安裝]] — 硬體門檻與安裝
- [[2026-06-27_comfyui_v8整合包]] — V8 多模態整合包
- [[2026-06-27_comfyui_系統教程前言]] — 系統教學規劃
- [[2026-06-27_comfyui_基礎教學ep1]] — Desktop 版上手
- [[2026-07-04_comfyui_零基礎ep01]] — 命令列手動安裝路線（Python/Git/venv）
