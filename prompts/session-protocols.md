# Session Protocols — Start & End

## Session Start Protocol（9 步）

每次新 session 開始時，**必須**按順序執行：

| Step | 動作 | 機制 | 說明 |
|------|------|------|------|
| 1 | 讀 `docs/_dev-log/LATEST.md` | Hook 自動注入 | 前 40 行由 hook 注入 |
| 2 | 讀 `docs/CURRENT_PROJECT_STATUS.md` | Hook 自動注入 | 前 20 行由 hook 注入 |
| 3 | 讀 `docs/CONTINUITY.md` | AI 執行 | CLAUDE.md 指示讀取 |
| 4 | 讀 `docs/project-wiki/00-session-entry.md` | AI 執行 | 進場 SOP 導航 |
| 5 | 讀 `docs/DOC_STATUS_LEDGER.md` 的 current 清單 | AI 執行 | 確認最新文件 |
| 6 | 讀 CLAUDE.md 的 `## Development Stages` | AI 執行 | 發展階段概覽 |
| 7 | `git log --oneline -10` | Hook 注入 5 筆 | AI 可跑完整 10 筆 |
| 8 | `git config --get core.hooksPath` | Hook 自動注入 | 空值 → 跑 install_hooks.py |
| 9 | 回報現況 | AI 執行 | 📊→⏳→🎯 |

**禁止**：跳過此流程直接回答問題。
**禁止**：自己重新掃描整個專案。

## Session End Protocol（5 步）

結束 session 前，**必須**執行：

1. 更新 `docs/_dev-log/LATEST.md`（今天做了什麼，≤ 40 行）
2. 更新 `docs/CONTINUITY.md`（下個 session 需要知道什麼）
3. 更新 `docs/CURRENT_PROJECT_STATUS.md`（如有重大進展）
4. 檢查自養觸發規則 → 新術語/常數/公式/模組？→ 更新索引
5. `git commit -m "session: 更新狀態文件"`

**禁止**：不執行此流程就結束 session。

## Canonical 判讀順序

多份文件衝突時的優先級（1 最高）：

1. `CURRENT_PROJECT_STATUS.md` — 單一現況真相
2. `docs/_dev-log/LATEST.md` — 最新日摘要
3. `docs/CONTINUITY.md` — 交班書
4. `docs/DOC_STATUS_LEDGER.md` — 文件狀態台帳
5. `CLAUDE.md` — 專案指令
6. `git log` — 不可篡改歷史

DOC_STATUS_LEDGER 標記為 `historical`/`superseded` 的文件只當歷史證據，不可當現況。
