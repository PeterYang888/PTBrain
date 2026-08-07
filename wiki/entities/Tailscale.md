---
type: entity
entity_type: product
tags: [networking, vpn, remote-access, tooling]
created: 2026-08-08
updated: 2026-08-08
sources: [2026-08-08_ocuclaw_even_g2_ai_agent, 2026-06-27_even_g2_claude_code]
---

# Tailscale

> 建立私有虛擬區域網（mesh VPN）的工具；在本 vault 中反覆出現的角色是「**讓穿戴裝置從外面連回家用電腦**」的那條隧道。

## 關鍵事實
- 在 [[Even_Realities_G2]] 的兩條 Agent 路線中都是必要元件：
  - [[2026-06-27_even_g2_claude_code]]：G2 Terminal 模式遠端連桌機 [[Claude_Code]] / [[OpenAI_Codex]]
  - [[2026-08-08_ocuclaw_even_g2_ai_agent]]：手機 OcuClaw app 連回本機 [[OpenClaw]] gateway
- 相關指令：`tailscale serve status`（查主機服務位址）
- OcuClaw 的 relay 連線規格：**`WSS`** 協定、連接埠 **`8444`**
- 被評測者列為「設定繁瑣」的主因之一——虛擬區網概念對非技術用戶門檻高

## 與其他頁的關係
- 是「算力留在自己機器、裝置只做 I/O」這種架構的關鍵拼圖（見 [[AI智慧眼鏡]] 的技術架構段）
- 與 [[OpenClaw]]、[[Claude_Code]] 的遠端使用情境緊密相關

## 相關來源
- [[2026-08-08_ocuclaw_even_g2_ai_agent]] · [[2026-06-27_even_g2_claude_code]]

## 待追蹤
- 本 vault 目前只從「被使用」的角度記錄，未涵蓋 Tailscale 本身的技術原理（WireGuard 基礎、ACL、Funnel 等）— stub 待補
