# Project Type Detection & Defaults

## 偵測指標

| 類型 | 指標（命中越多分越高） |
|------|---------------------|
| game | Unity/, Godot/, pygame, game, assets/sprites, Assets/ |
| web-api | app.py, server.js, main.go, routes/, controllers/ |
| frontend | src/components/, pages/, next.config, vite.config |
| data-science | notebooks/, .ipynb, requirements.txt + pandas/sklearn |
| general | fallback（無明顯指標） |

掃描根目錄 + 2 層子目錄。計算每類指標命中數，取最高分。

## 各類型預設配置

| 設定 | game | web-api | frontend | data-science | general |
|------|------|---------|----------|-------------|---------|
| Wiki 初始焦點 | 機制/數值 | API/資料流 | 頁面/元件 | 實驗/模型 | 模組 |
| 額外觸發路徑 | assets/ | routes/ | src/components/ | notebooks/ | （無） |
| 訪談重點 | 術語避誤 | API 規格 | 設計規範 | 特徵欄位 | 通用 |
| 預設索引數 | 7 | 7 | 6（-formulas） | 7 | 5 基本 |
