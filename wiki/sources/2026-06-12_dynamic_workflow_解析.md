---
type: source
tags: [ai, claude-code, workflow, dynamic-workflows, agent]
created: 2026-06-12
source_url: https://www.youtube.com/watch?v=4fpZhuJuIls
source_date: 2026-06-12
source_type: transcript
source_extra:
  platform: youtube
  notebooklm_notebook: ai-tooling
  processed_by: notebooklm-py
---

# Claude Dynamic Workflow 解析，什麼時候該用、什麼時候別碰？

> 來源：[原始檔](../../raw/transcripts/2026-06-12_dynamic_workflow_解析.md) · [[Claude_Code]]

## 一句話摘要
Dynamic Workflow 的「什麼時候用/不用」決策指南：4 層功能階梯（對話→Subagent→Agent Team→Dynamic Workflow），適合並行可驗證的大任務；成本控制三招：模型分級（Haiku 撒網/Opus 收斂）、預算硬上限、小範圍先測試。

## 核心論點
- **4 層功能階梯**：基礎對話 → Subagent（平行雜事）→ Agent Team（角色辯論）→ Dynamic Workflow（腳本指揮軍團）；前進每層的關鍵是「任務是否可並行且需要可驗證性」
- **Skill vs Subagent vs Agent Team vs Dynamic Workflow**：區別在「下一步由誰決定」——Dynamic Workflow 由程式碼/腳本決定，Context 影響極低
- **何時別用**：任務必須一步接一步（前置依賴強）、修改數行程式碼、日常查詢——用 Workflow 是殺雞用牛刀
- **成本三招**：撒網階段用 Haiku、收斂推理用 Opus；設預算硬上限觸及即停；先單資料夾測試再放大
- **`effort: ultra`**：高推理模式，Claude 自動判斷是否開啟 Workflow；較貴，適合需要 Workflow 的任務才開

## 觸發指令
| 方式 | 指令 | 說明 |
| :--- | :--- | :--- |
| 關鍵字 | Prompt 中加入 `workflow` | Claude 自動撰寫 JS 腳本 |
| 推理模式 | `effort: ultra` | 自動判斷是否需 Workflow |
| 內建深度研究 | `/deep-research` | 多角度搜尋 + 表決過濾 |
| 進度查詢 | `/workflows` | 查看 Agent 狀態/Token 消耗 |

## 推薦應用場景
- 全代碼庫 Bug 掃描（找 + 驗證/反駁）
- 多維度 Code Review（效能/資安/可讀性）
- 跨來源深度研究（官方文件/論文/社群，附出處）
- 大規模代碼遷移（數百個檔案架構更動）

## 值得引用的段落
> 「Subagent 像你叫一個實習生去查資料，他查完把整疊資料堆在你桌上... Workflow 就是那個先在外面把 100 份資料整理好，只把結論端上桌的人。」

> 「如果任務是那種一定要一步接一步、前面沒做完後面就動不了的... 那就別用，殺雞用牛刀而已。」

## 連結到的 wiki
- [[Dynamic_Workflows]]
- [[Claude_Code]]
- [[Agentic_Workflow]]

## 我的問題 / 待追蹤
- `effort: ultra` 跟 Ultra Code 模式是同一個東西嗎？
- Agent Team 模式有獨立的觸發指令嗎？
