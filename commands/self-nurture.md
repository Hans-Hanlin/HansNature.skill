# /self-nurture Command

> LLM Wiki + 自養閉環 — 為專案建立自養系統

## 行為

### 首次使用（BIRTH）

偵測到專案尚未安裝 self-nurture（無 `docs/project-wiki/` 目錄）時：

1. **偵測專案類型** — 掃描目錄判斷 game/web-api/frontend/data-science/general
2. **檢查既有設施** — 偵測 CLAUDE.md、docs/、.githooks/ 是否存在
3. **訪談用戶** — 使用 `prompts/interviewer.md` 引導 6 問
4. **生成 Wiki 骨架** — 00-session-entry.md + 01-project-overview.md（含真實內容）
5. **生成 7 索引檔** — glossary/formulas/constants/cross-ref/tags/architecture/gaps
6. **生成狀態管理層** — CURRENT_STATUS/LEDGER/CONTINUITY/LATEST
7. **安裝自養規則** — CLAUDE.md 追加（含哨兵標記偵測冪等）
8. **安裝驗證閉環** — verify_wiki_sync.py + pre-commit + install_hooks.py
9. **驗證安裝** — 確認 hooks 就位
10. **寫首個記錄** — dev-log + _usage-log

### 再次使用（已安裝）

偵測到專案已安裝 self-nurture 時：
- 回報當前 Wiki 健康狀態
- 提供選項：跑完整健康檢查 / 進入 GROW 模式

## 安裝規則

- **永不覆蓋使用者內容** — 只 append / merge / 建新檔
- **冪等設計** — 偵測哨兵標記 `<!-- self-nurture:start -->` 判斷已安裝
- **每步顯示結果** — 不沉默執行
- **禁止**：覆蓋 CLAUDE.md（只 append 在頂部）
- **禁止**：直接編輯使用者既有 docs

## 專案類型偵測

```python
indicators = {
    "game": ["Unity", "Godot", "pygame", "game", "assets/sprites", "Assets/"],
    "web-api": ["app.py", "server.js", "main.go", "routes/", "controllers/"],
    "frontend": ["src/components/", "pages/", "next.config", "vite.config"],
    "data-science": ["notebooks/", ".ipynb", "requirements.txt"],
    "general": [],
}
# 掃描根目錄 + 2 層子目錄，計算每類指標命中數，取最高分
```

## rag-builder 遷移

若偵測到 rag-builder 產出（有 `docs/_index/glossary.md` 但無 `docs/project-wiki/`）：
- 保留既有 5 索引
- 補建 architecture.md + gaps.md
- 新增 Wiki 骨架 + 驗證閉環
- 升級 Session Start Protocol（4 步 → 9 步）
