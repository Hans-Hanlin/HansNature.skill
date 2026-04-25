# Document Status Ledger

> 防止新 session 誤讀過時文件。每份文件標記狀態。

## 狀態定義

| 狀態 | 含義 | 新 session 行為 |
|------|------|----------------|
| `current` | 當前有效 | ✅ 優先讀取 |
| `historical` | 舊狀態紀錄 | ⚠️ 只當歷史證據 |
| `superseded` | 已被取代 | ❌ 不讀，讀取代檔 |
| `research` | 研究/考證 | ℹ️ 按需讀取 |
| `spec` | 規格書/計畫書 | 📋 目標，非完成狀態 |
| `report` | 單次工作產出 | 📄 永存但非主線 |

## 文件清單

### current
- `docs/CURRENT_PROJECT_STATUS.md` — 單一現況真相
- `docs/_dev-log/LATEST.md` — 最新日摘要
- `docs/CONTINUITY.md` — 交班書
- `docs/project-wiki/00-session-entry.md` — 進場 SOP
- `docs/project-wiki/01-project-overview.md` — 專案總覽
