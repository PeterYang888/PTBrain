---
type: source
tags: [Stanford, Agentic_Workflow, RAG, Prompt_Engineering, LLM, 多智能體]
created: 2026-05-16
source_url: https://www.youtube.com/watch?v=eKW9ITaltWw
source_date: 2026-05-16
source_type: transcript
---

# Stanford BLLM：從 LLM 到 Agentic Workflow 完整系統課程

> 來源：[原始檔](../../raw/transcripts/Stanford_AI系統課程_Agentic_transcript.md)

## 一句話摘要
Stanford BLLM 課程教 AI 工程師用「重軸」技術（Prompt Chaining、RAG、Agentic Workflow）克服 LLM 四大限制，並強調 Evaluation 體系是 AI 系統上線的命脈。

## 核心論點
- 強化單一模型三工具：Prompt Chaining（可觀察、可測試）、Fine-tuning（能不做就不做）、RAG（解決幻覺與資訊落後）
- Agentic AI 思維轉變：從「精確控制每行代碼」到「給目標和限制讓 AI 決定怎麼完成」（Think like a manager）
- Agent 三要素：提示詞（角色/權限）、上下文管理（短期/長期記憶）、工具（執行+查詢能力）
- 評估三維度：整體 vs 組件、客觀 vs 主觀（LLM-as-judge）、定量 vs 定性
- MCP（Model Context Protocol）作為通用協議層，簡化多智能體間通信

## 值得引用的段落
> 「Prompt Engineering 不會是一個職業，因為它是每個工程師都該會的基本技能，就像九九乘法表一樣。」

> 「Fuzzy 的問題一定要加上 Human-in-the-loop。」

## 連結到的 wiki
- [[Agentic_Workflow]]
- [[RAG]]
- [[Claude_Code]]
- [[Harness_Engineering]]

## 擴充細節

### BCG 研究：AI 使用模式
- 三組對照：無 AI、有 ChatGPT、有 ChatGPT + 提示詞訓練
- 三個發現：
  1. **Jagged Frontier（鋸齒邊界）**：AI 並非全面優越，有些任務加分、有些反而扯後腿
  2. **Falling Asleep at the Wheel**：在 AI 不擅長的任務上過度信任 → 結果比不用 AI 還差
  3. **Centaur vs Cyborg**：
     - Centaur（半人馬）：分工委派型，丟長 prompt 讓 AI 完成整件事
     - Cyborg（生化人）：高頻來回型，與 AI 逐句協作

### LLM 四大限制
1. 缺乏 domain knowledge（公司內部文件、特定產業數據）
2. 資訊落後（無法頻繁重訓）
3. 控制難（機率性輸出，同 prompt 不同結果）
4. Long context 下 lost in the middle 現象

### 為何少做 Fine-Tuning
- 需大量高質量標注數據
- 易 overfit，失去 base model 廣度
- 時效性差：fine-tune 完上線，新 base model 就出來了
- Prompt engineering 通常能達到同樣效果，成本更低

### Agent 三要素 × 三層自主性
**三要素**：提示詞（角色/權限）、Context Management（短期記憶 + 長期記憶 + RAG）、Tools（執行 API + 查詢 API）

**三層自主性**：
1. Hardcoded steps（全步驟固定）— 安全、可預測、但僵硬
2. Hardcoded tools + AI 決定步驟（推薦的 production 起點）
3. Fully autonomous（自決步驟甚至創工具）— 風險最高

### 傳統 vs Agentic 系統思維差異
| 維度 | 傳統軟體 | Agentic AI |
|---|---|---|
| 資料 | 結構化（JSON/DB） | 自由文本/圖片/音訊 |
| 邏輯 | Deterministic（相同 input → 相同 output） | Fuzzy（機率輸出） |
| 架構心態 | 精確控制每行程式碼 | Think like a manager：給目標和邊界 |
| 測試 | 確定性，窮舉 | 迭代探索式，用 LLM-as-Judge |

### Evaluation 三維度
- **整體 vs 組件**：End-to-end（使用者滿意度）+ Component-based（每個工具的指標）
- **客觀 vs 主觀**：Objective（可自動驗證的邏輯正確性）+ Subjective（語氣、同理心，用 LLM-as-Judge）
- **定量 vs 定性**：Quantitative（成功率、延遲）+ Qualitative（人工審查幻覺、邏輯缺失）

### LLM-as-Judge 四種玩法
1. Pair-wise comparison（哪個答案比較好）
2. Single-answer grading（打 1-5 分）
3. Reference-guided pair-wise（有標準答案對比）
4. Rubric-based（自訂評分標準）

### 客服 Agent Case Study（改地址任務拆解）
1. 抽出關鍵資訊（intent / order ID / 新地址）— LLM one-shot
2. 查資料庫客戶紀錄 — custom tool / MCP
3. 查退費/改地址政策 — RAG
4. 根據收集資訊起草回信 — LLM
5. 送出 email — email 發送工具

### MCP（Model Context Protocol）
- 傳統方式：每個 API 單獨撰寫串接邏輯
- MCP：通用協議層，agent 只需與 MCP server 溝通，由 MCP 與後端服務打交道
- 更大想像：agent-to-agent communication（把別人的 agent 當工具呼叫）= Multi-Agent 基礎

## 我的問題 / 待追蹤
- Stanford BLLM 課程完整版在哪裡？是否有 Coursera 版本？
- MCP 與 LangChain 的定位差異？
- LLM-as-Judge 的可靠性研究（多大程度上能取代人工評分）？
