---
type: concept
tags: [LLM, 知識庫, 向量資料庫, AI架構]
created: 2026-05-16
updated: 2026-05-16
sources: [2026-05-16_claude_code_obsidian_知識庫, 2026-05-16_stanford_ai系統課程_agentic]
---

# RAG（Retrieval-Augmented Generation，檢索增強生成）

> 解決 LLM 幻覺與資訊落後問題的標準方案：在推理時從外部知識庫檢索相關文件，作為 context 補充給模型，使回答更準確、即時。

## 詳細說明
### 傳統 RAG 流程
1. 將文件切成 chunks（分塊）
2. 用向量模型轉為 embedding，存入向量資料庫（Vector Database）
3. 查詢時：將問題轉為 embedding → 找最相似的 chunks → 連同問題一起送給 LLM

### 核心優勢
- 即使 context window 變長，RAG 在降低延遲與及時更新資料方面仍具優勢（來自 [[2026-05-16_stanford_ai系統課程_agentic]]）

## 與其他概念的差別
- 跟 **結構化 Wiki 知識庫**（如 PTBrain）的差別：RAG 找最相似的文字片段，不理解片段之間的關係；Wiki 是有目錄和交叉引用的結構化知識，AI 讀「書」而非「碎紙片」（來自 [[2026-05-16_claude_code_obsidian_知識庫]]）
- 跟 **Fine-tuning** 的差別：RAG 在推理時動態補充知識，Fine-tuning 是把知識烙印進模型參數

## 爭議 / 未定論
- 超長 context window 出現後，有人質疑 RAG 是否仍必要：RAG 在延遲、成本、動態更新三方面仍有優勢，但邊界正在模糊

## 應用 / 實例
- 在 [[Claude_Code]] + [[Obsidian]] 知識庫中：以結構化 Wiki + index 取代碎片化 RAG，可節省 95% Token 用量
- [[Graphify]]：針對程式碼庫的 RAG-lite；不需要 embedding，以確定性 Tree-sitter 解析為主，LLM 語義分析為輔；實測 Token 節省 60%

## 來源
- [[2026-05-16_claude_code_obsidian_知識庫]]
- [[2026-05-16_stanford_ai系統課程_agentic]]
- [[2026-06-12_graphify_claude_code]]
