# /wiki-check Command

> Wiki 健康檢查 — 跑完整自養驗證並產出報告

## 行為

執行 `scripts/verify_wiki_sync.py --report`（使用專案安裝的版本），產出健康報告：

```
📊 Wiki 健康度報告
━━━━━━━━━━━━━━━━━━━━━
Wiki 頁面：{N} 頁
索引覆蓋率：
  - glossary：{Y} 術語
  - formulas：{Z} 公式（§ 編號）
  - constants：{W} 常數
  - tags：{V} 標籤
  - architecture：{A} 模組
  - gaps：{G} 缺口
硬檢查：{通過/失敗} ({P}/{T})
軟檢查：{M} 項建議
LATEST.md 最後更新：{日期}
Hooks 狀態：{已安裝 / 未安裝}
━━━━━━━━━━━━━━━━━━━━━
```

## 前置條件

專案必須已安裝 self-nurture（有 `docs/project-wiki/` 目錄）。
若未安裝，提示使用者先執行 `/self-nurture`。

## 執行方式

```bash
python scripts/verify_wiki_sync.py --report
```

加 `--report` 旗標時，輸出健康報告而非 pre-commit 驗證模式。
不加旗標時，使用 pre-commit 模式（讀 staged files，硬檢查失敗 exit 1）。
