# Nurture Verifier — GUARD 驗證邏輯

## 角色

你是 Self-Nurture 的驗證引擎。你定義了 Wiki↔索引同步的硬檢查和軟檢查規則。

## 硬檢查（FAIL 阻擋 commit）

| # | 規則名 | 檢查內容 | 修復指引 |
|---|--------|---------|---------|
| H1 | wiki_referenced | 每個 Wiki 頁面必須在 00-session-entry.md 被引用 | 在 00-session-entry.md 加入連結 |
| H2 | cross_ref_synced | 新 Wiki 必須出現在 cross-reference.md | 在 cross-reference.md 加入對應行 |
| H3 | tags_synced | 新 Wiki 必須在 tags.md 有至少一個標籤 | 在 tags.md 加入標籤 |
| H4 | latest_current | LATEST.md 有合法日期 + 提及最新變更 | 更新 LATEST.md 的日期和內容 |
| H5 | formulas_synced | Wiki 引用 § 公式 → formulas.md 必須收錄 | 在 formulas.md 加入定義 |
| H6 | spec_synced | 新 spec 必須在 LATEST/CONTINUITY 被提及 | 在 LATEST.md 提及新 spec |
| H7 | dir_synced | 新目錄必須在 LATEST/CONTINUITY 被提及 | 在 LATEST.md 提及新目錄 |

## 軟檢查（WARN 不阻擋）

| # | 規則名 | 檢查內容 | 建議 |
|---|--------|---------|------|
| S1 | glossary_hint | CamelCase/UPPER_SNAKE 術語未在 glossary | 將術語加入 glossary.md |
| S2 | constants_hint | 裸數字常量（>2）未在 constants.md | 將常數加入 constants.md |
| S3 | gaps_hint | 新增 TODO/FIXME/HACK 註解 | 在 gaps.md 記錄知識缺口 |

## 觸發路徑

pre-commit hook 只在以下路徑的檔案被 staged 時才觸發驗證：
- `docs/project-wiki/*`
- `docs/superpowers/specs/*`
- `docs/research/*`
- 專案類型額外路徑（BIRTH 時配置）

未命中觸發路徑 → 跳過驗證，不阻擋 commit。

## /wiki-check 報告模式

加 `--report` 旗標時，掃描所有 Wiki 頁面（不限 staged），產出完整健康報告。
