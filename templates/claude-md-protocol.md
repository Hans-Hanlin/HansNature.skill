<!-- self-nurture:start -->

## 🌱 Self-Nurture Protocol

### Session Start Protocol（必讀）

每次新 session 說「報告現況」「繼續」「接手」時，按順序讀：

1. `docs/_dev-log/LATEST.md` — 最新工作摘要
2. `docs/CURRENT_PROJECT_STATUS.md` — 單一現況真相
3. `docs/CONTINUITY.md` — 交班書
4. `docs/project-wiki/00-session-entry.md` — 進場 SOP
5. `docs/DOC_STATUS_LEDGER.md` 的 current 清單
6. 本檔 `## Development Stages`
7. `git log --oneline -10`
8. `git config --get core.hooksPath`（空值 → 跑 `python scripts/install_hooks.py`）
9. 回報：📊 現況 → ⏳ 待辦 → 🎯 建議下一步

### Session End Protocol（必做）

結束 session 前：
1. 更新 `docs/_dev-log/LATEST.md`（≤ 40 行）
2. 更新 `docs/CONTINUITY.md`
3. 更新 `docs/CURRENT_PROJECT_STATUS.md`（如有重大進展）
4. 檢查自養規則 → 新術語/常數/公式/模組？→ 更新索引
5. `git commit -m "session: 更新狀態文件"`

### 自養觸發規則（強制）

| 觸發條件 | 必須更新的檔案 | 等級 |
|---------|--------------|------|
| 寫新 Wiki 頁面 | session-entry + cross-ref + tags | 硬 |
| 完成新模組 | glossary + architecture + tags | 硬 |
| 發現新公式 | formulas.md | 硬 |
| 發現新常數 | constants.md | 軟 |
| 發現新術語 | glossary.md | 軟 |
| 修改架構 | architecture + cross-ref | 硬 |
| 新增 spec/計畫 | LATEST + CONTINUITY | 硬 |
| 新增研究目錄 | LATEST + CONTINUITY | 硬 |
| 重大決策 | CONTINUITY + 新 dev-log | 軟 |
| Session 結束 | 檢查以上所有 | 軟 |

### Canonical 判讀順序

文件衝突時：CURRENT_STATUS > LATEST > CONTINUITY > LEDGER > CLAUDE.md > git log

### 術語避誤表

{INTERVIEWER_Q2_CONTENT}

<!-- self-nurture:end -->
