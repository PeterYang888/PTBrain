---
type: concept
tags: [AI編程, Claude_Code, Karpathy, 氛圍編程]
created: 2026-05-24
updated: 2026-08-22
sources: [2026-05-24_karpathy_how_i_use_llms, 2026-07-18_google_agentic_engineering_day1, 2026-07-18_git_github_vibe_coding基礎, 2026-07-31_ig_設計靈感海莉, 2026-07-13_fb_vibe_coding美感_eason]
---

# Vibe Coding（氛圍編程）

> 由 [[Andrej_Karpathy]] 提出的開發模式：利用 AI Agent 自動處理低階程式碼，人類只需描述目標與驗證結果。

## 詳細說明
傳統編程：人類逐行寫程式碼。Vibe Coding：人類描述目標，AI Agent 生成並執行，人類驗證。

## 關鍵特徵
- 適用場景：快速原型、個人工具、一次性腳本
- 使用工具：[[Claude_Code]]、Cursor
- 人類角色：轉向架構設計與結果驗證
- 限制：複雜系統、安全關鍵代碼仍需人類深度介入

## 應用實例
Karpathy 展示：用 Cursor + Claude 3.7，一分鐘內開發出帶特效的井字遊戲

## 爭議
- 批評：代碼品質不可控，技術債難以管理
- 支持：加速個人開發者生產力
- **[[理解成本]] 風險（2026-06）**：不求甚解的 Vibe Coding 讓系統在架構調整時無法維護；AI 時代的稀缺能力是「判斷力」而非「產出力」
- **決策權外包批判（2026-07-25）**：[[Matt_Pocock]] 陣營定義 Vibe Coding 為「把模糊想法丟給 AI 憑感覺做」＝把幾百個微觀決定外包給黑盒子；`/grill-me` 強制 AI 反向拷問即為反制。見 [[2026-07-25_grill_me_matt_pocock]]

## AI 時代的設計參考素材（2026-07）
兩份獨立來源不約而同觀察到同一個轉變：設計參考素材正從「靜態好看範例」轉向「agent 看得懂、做得出來」的可執行資產。
- 過去參考網站/範例只回答「哪些畫面好看」；現在需要知道 prompt 怎麼寫、動畫怎麼做、CSS 能不能直接用、如何讓 AI 全站維持同一套設計語言（見 [[2026-07-31_ig_設計靈感海莉]]）
- 素材庫/動態庫/元件庫概念興起，重點是能直接複製 Prompt 貼進 [[Claude_Code]]、[[OpenAI_Codex|Codex]] 使用（見 [[2026-07-13_fb_vibe_coding美感_eason]]）

## 演進：從 Vibe Coding 到 Agentic Engineering（2026-07-18）
- Google 官方課程將 Vibe Coding 定位為「直覺式」起點，正式化的下一階段是 [[Agentic_Engineering]]——加上結構、驗證機制與 Harness 設計（「你跟 CTO 說我們在 Vibe Coding 付款系統，他可能臉都綠了」）。見 [[2026-07-18_google_agentic_engineering_day1]]
- **Vibe Coder 的基礎設施**：[[Git_版本控制]] 是 AI 試錯的保險與回溯系統；Vibe Coder 不必手寫指令，但要能對 commit / branch / conflict 下決策。見 [[2026-07-18_git_github_vibe_coding基礎]]

## 來源
- [[2026-05-24_karpathy_how_i_use_llms]]
- [[2026-06-06_anthropic_棄_markdown_改用_html]]
- [[2026-07-18_google_agentic_engineering_day1]]
- [[2026-07-18_git_github_vibe_coding基礎]]
- [[2026-07-31_ig_設計靈感海莉]]
- [[2026-07-13_fb_vibe_coding美感_eason]]
