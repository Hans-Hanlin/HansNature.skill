# Self-Nurture Lifecycle Reference

## BIRTH → GROW → GUARD → EVOLVE

### BIRTH（誕生期）
- 觸發：使用者首次說「開始自養」
- 時長：10-15 分鐘
- 產出：Wiki 骨架 + 7 索引 + 狀態管理層 + 驗證閉環 + CLAUDE.md 追加
- 冪等：哨兵標記 `<!-- self-nurture:start/end -->` 偵測

### GROW（成長期）
- 觸發：AI 日常工作中背景觀察
- 行為：Discoverer 累積 3+ 觀察後批次提議
- 規則：用戶確認才寫入，不中斷 debug

### GUARD（守護期）
- 觸發：每次 git commit（pre-commit hook）
- 行為：verify_wiki_sync.py 跑 7 硬 + 3 軟檢查
- 失敗：硬檢查 FAIL → 阻擋 commit + 修復指引

### EVOLVE（進化期，v1.0 scope）
- 觸發：每次 BIRTH 完成
- 行為：寫 _usage-log，累積 3 次後萃取 _patterns
- v1.1 scope：auto-adjust 預設值、版本升級
