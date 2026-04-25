# Verification Rules Reference

## 硬檢查 (H1-H7) — FAIL 阻擋 commit

| # | 規則 | 說明 |
|---|------|------|
| H1 | wiki_referenced | Wiki 頁面必須在 00-session-entry.md 被引用 |
| H2 | cross_ref_synced | 新 Wiki 必須在 cross-reference.md |
| H3 | tags_synced | 新 Wiki 必須在 tags.md 有標籤 |
| H4 | latest_current | LATEST.md 有合法日期 |
| H5 | formulas_synced | § 公式引用必須在 formulas.md 收錄 |
| H6 | spec_synced | 新 spec 必須在 LATEST/CONTINUITY 提及 |
| H7 | dir_synced | 新目錄必須在 LATEST/CONTINUITY 提及 |

## 軟檢查 (S1-S3) — WARN 不阻擋

| # | 規則 | 說明 |
|---|------|------|
| S1 | glossary_hint | CamelCase/UPPER_SNAKE 術語未在 glossary |
| S2 | constants_hint | 裸數字常量未在 constants.md |
| S3 | gaps_hint | 新增 TODO/FIXME/HACK 註解 |

## 觸發路徑（預設）

- `docs/project-wiki/*`
- `docs/superpowers/specs/*`
- `docs/research/*`

專案類型額外路徑見 project-types.md。
