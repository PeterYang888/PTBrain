# wiki/ — 知識層

**由 LLM 擁有並維護。** 你（使用者）主要讀、給回饋；實際的寫入、更新、交叉引用都交給 LLM。

## 子目錄

| 目錄 | 放什麼 | 與 source 的關係 |
|---|---|---|
| `sources/` | 每份 raw 對應一頁摘要 | 1:1 |
| `entities/` | 人、組織、產品、地點、事件 | 1:N（一個 entity 被多個 source 提到） |
| `concepts/` | 抽象概念、理論、方法 | 1:N |
| `topics/` | 頂層主題頁，樞紐用 | 1:N |
| `syntheses/` | 比較、分析、探索問答的歸檔 | 多對多 |

## 頁面模板
請見 [CLAUDE.md §4](../CLAUDE.md)。每種頁面類型都有標準 frontmatter 與結構。

## 原則
- 連結豐富：所有相關實體都用 `[[wiki-link]]`
- 有 frontmatter（type、tags、dates、sources）
- 精簡、高密度：這是查閱用的 wiki，不是文章
- 不杜撰：沒 source 支持就不寫，推測要標註
