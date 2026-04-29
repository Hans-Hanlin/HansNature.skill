---
name: self-nurture
description: "LLM Wiki + 自養閉環一站式框架。當用戶說「開始自養」、「啟動自養」、「自養模式」、「建立 Wiki」、「專案 Wiki」、「自我成長」、「開始成長」、「self-nurture」時觸發。為任何專案建立 Wiki 骨架 + 7 索引 + 驗證閉環 + AI 主動發現機制。"
user-invocable: true
argument-hint: "[--type game|web-api|frontend|data-science|general]"
effort: high
---

# Self-Nurture — LLM Wiki + 自養閉環

為任何專案建立 Wiki + 自養閉環系統，讓 AI 和用戶在每次 session 中共同成長。

**核心理念：Wiki 是身體（知識本體），自養是代謝（維持健康），驗證是免疫系統（偵測脫節）。**

## 觸發與參數

觸發：`/self-nurture`、`開始自養`、`建立 Wiki`、`自我成長`

| 用戶說法 | 動作 |
|---------|------|
| 「開始自養」「建立 Wiki」 | 進入 BIRTH 階段（偵測→訪談→安裝） |
| 「/wiki-check」 | 跑健康檢查（GUARD 階段） |

## 四階段生命週期

BIRTH（誕生）→ GROW（成長）→ GUARD（守護）→ EVOLVE（進化）

- BIRTH：一次性，10-15 分鐘。偵測專案類型→訪談用戶→安裝 Wiki 骨架+索引+驗證閉環
- GROW：持續，每次工作中。AI 背景觀察，發現新術語/常數/公式時批次提議
- GUARD：自動，每次 commit。pre-commit hook 觸發 verify_wiki_sync.py
- EVOLVE：自我成長，累積 3 次使用後萃取通用模式

## 執行流程

### BIRTH（首次使用）

1. 偵測專案類型（掃描目錄結構）
2. 檢查既有設施（CLAUDE.md? docs/? .githooks/?）— 冪等，只補缺
3. 訪談用戶（6 問：目標、術語、常數、公式、痛點、模組）— 使用 prompts/interviewer.md
4. 生成 Wiki 骨架 + 種子內容（00-session-entry + 01-project-overview）
5. 生成 7 索引檔（glossary/formulas/constants/cross-ref/tags/architecture/gaps）
6. 生成狀態管理層（CURRENT_STATUS/LEDGER/CONTINUITY/LATEST）
7. 安裝自養規則到 CLAUDE.md（含哨兵標記 `<!-- self-nurture:start/end -->`）— 使用 templates/claude-md-protocol.md
8. 安裝驗證閉環（verify_wiki_sync.py + pre-commit hook + install_hooks.py）
9. 驗證安裝完整性
10. 寫首個 dev-log + Skill 自我記錄到 _usage-log/

### GROW（日常使用）

AI 工作中使用 prompts/discoverer.md 背景觀察。累積 3+ 觀察後批次提議。
用戶確認後才寫入。絕不自動寫入，絕不中斷 debug。

### GUARD（自動守護）

- **pre-commit hook**：觸發 verify_wiki_sync.py（7 硬檢查 + 3 軟檢查）
  - 硬檢查失敗 → 阻擋 commit + 修復指引
- **Stop hook 安全網（v1.0.1）**：每次 Claude turn 結束時偵測
  - ≥10 檔未 commit → 🔴 提醒分批 commit
  - ≥300 行 diff → 🔴 提醒分批 commit
  - LATEST.md 過期 >4h → 🟡 提醒更新
  - 安靜模式：無警報 = 無輸出，不打擾工作流
  - 來源：生產專案實戰踩坑（81 檔 6156 行未 commit 事件）
- `/wiki-check` 手動觸發完整健康報告

### EVOLVE（自我成長）

每次使用寫 `_usage-log/YYYY-MM-DD_{project}.md`。累積 3 次後萃取 `_patterns/`。

## 關鍵原則

- **永不覆蓋** — 只 append / merge / 建新檔
- **冪等設計** — 可重複執行，只補缺不重建
- **用戶決定** — AI 提議，人類確認
- **全 Python** — 跨平台（Windows/Linux/macOS）

## 與其他 Skill 的關係

- 與 **evo** 互補（evo 管代碼品質進化，self-nurture 管知識系統成長）
- 與 **graphify** 互補（graphify 管 Layer 4 知識圖譜）
- 取代 **rag-builder** 的安裝功能（更完整的 Wiki + 驗證閉環版本）

## Prompts

- `prompts/interviewer.md` — BIRTH 訪談引導
- `prompts/discoverer.md` — GROW 主動發現
- `prompts/nurture-verifier.md` — GUARD 驗證邏輯
- `prompts/session-protocols.md` — Session Start/End Protocol
