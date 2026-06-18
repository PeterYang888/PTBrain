---
type: concept
tags: [AI架構, Agent, 系統設計, AI職涯]
created: 2026-05-16
updated: 2026-05-16
sources: [2026-05-16_harness_engineering_ai職涯, 2026-05-16_stanford_ai系統課程_agentic]
---

# Harness Engineering

> 為 LLM「裝上身體」的系統架構工程；解決 LLM 的記憶、工具使用、規劃執行、自動評估四大限制，被視為 2026 年 AI 競爭的核心能力。

## 詳細說明
LLM 本身像「超級聰明但失憶且沒有手腳的大腦」，Harness Engineering 就是替這個大腦設計以下四個模組：

| 模組 | 功能 |
|------|------|
| **記憶（Memory）** | 儲存歷史對話、代碼規範、用戶偏好，解決 LLM 缺乏長期記憶的問題 |
| **工具（Tools）** | 讓 AI 能讀取檔案、操作終端機、呼叫 API，即「手腳」 |
| **規劃與執行（Planning & Execution）** | 拆解任務、錯誤重試邏輯 |
| **評估（Evaluation）** | 自動測試結果是否正確，決定是否重新運行 |

## 與其他概念的差別
- 跟 [[Prompt_Engineering]] 的差別：Prompt Engineering 是「怎麼問醫生」，Harness Engineering 是「建一整間醫院」
- 跟 [[Agentic_Workflow]] 的關係：Harness 是 Agentic Workflow 的系統實現層；Agentic Workflow 是概念，Harness 是工程架構
- 跟 [[Loop_Engineering]] 的關係：在工程化階梯中為 **Prompt → [[Context_工程|Context]] → Harness → Loop**。Harness 提供執行環境、工具反饋與權限框架；Loop Engineering 在其上設計自我迭代的閉環，是進入 Loop 前的必要基礎（見 [[2026-06-19_loop_engineering]]）

## 兩大流派（2026 年）
- **OpenCloud（Gateway First）**：連接廣度，擁有約 4.4 萬個 Skills 市集
- **Harness Agent（Agent First）**：記憶與學習的深度，執行-評估-萃取-改進-檢索的學習閉環

## 應用 / 實例
- 在 [[Claude_Code]] 中：Claude Code 本身就是 Harness 的典型實現（記憶、工具、規劃、評估）

## 職涯資訊
矽谷 Harness Engineer 底薪 22-38 萬美元，含股票總報酬超過 50 萬美元（需同時具備系統設計、LLM 特性、分散式系統、評估方法論四維能力）

## 來源
- [[2026-05-16_harness_engineering_ai職涯]]
- [[2026-05-16_stanford_ai系統課程_agentic]]
- [[2026-06-19_loop_engineering]]（Harness → Loop 的工程化階梯）
