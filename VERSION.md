# Self-Nurture Version History

## v1.0.1 (2026-04-26)

- 新增 Stop hook 里程碑安全網（從遊戲專案 v3 自養失敗事件反向萃取）
- 偵測：≥10 檔未 commit / ≥300 行 diff / LATEST.md 過期 >4h → 自動提醒
- 安靜模式：無警報時完全不輸出，不打擾工作流
- 純讀取：不寫檔、不改 git 狀態、永遠 exit 0
- 新增 templates/check-milestone.py.template（專案安裝用模板）

## v1.0.0 (2026-04-25)

- 初版：從天道降臨·文字三國 v3 自養系統反向萃取
- BIRTH：偵測 + 訪談 + 安裝（10 步）
- GROW：Discoverer 主動發現 + 批次提議
- GUARD：verify_wiki_sync.py（7 硬 + 3 軟）+ pre-commit hook
- EVOLVE：_usage-log 記錄（auto-adjust 延至 v1.1）
- 全 Python 跨平台 hook
- 支援 5 種專案類型（game/web-api/frontend/data-science/general）
- rag-builder 遷移支援
