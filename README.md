# HansNature.skill

> **LLM Wiki + Self-Nurturing Closed-Loop Framework for Claude Code**

讓任何專案說「開始自養」，自動建立 Wiki + 閉環自養系統。AI 和用戶在每次 session 中共同成長。

## What is this?

一個 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skill，為你的專案建立：

- **Project Wiki** — 結構化的知識頁面，有標準格式和閱讀順序
- **7 索引檔** — glossary / formulas / constants / cross-reference / tags / architecture / gaps
- **驗證閉環** — pre-commit hook 自動檢查 Wiki ↔ 索引同步（7 硬檢查 + 3 軟檢查）
- **AI 主動發現** — 工作中自動偵測新術語、常數、公式，批次提議加入 Wiki
- **Session Protocol** — 9 步 Start + 5 步 End，確保跨 session 不失憶

## Core Concept

```
Wiki = 身體（知識本體，持續生長）
自養 = 代謝（維持知識健康）
驗證 = 免疫系統（偵測脫節）

三者缺一不可。
```

### Three-Layer Self-Nurturing

```
AI 自養：每次 session 比上次更了解專案
   ↕
用戶自養：Wiki 寫作迫使隱性知識顯性化
   ↕
專案自養：文件和知識體系越來越完整
```

## Installation

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- Python 3.x (for hooks and verification scripts)

### Install

Clone this repo into your Claude Code skills directory:

```bash
# Linux / macOS
git clone https://github.com/langlive04-crypto/HansNature.skill.git ~/.claude/skills/self-nurture

# Windows
git clone https://github.com/langlive04-crypto/HansNature.skill.git %USERPROFILE%\.claude\skills\self-nurture
```

Or copy the files manually to `~/.claude/skills/self-nurture/`.

## Usage

In any project, say:

```
開始自養
```

or use the slash command:

```
/self-nurture
```

The skill will:

1. **Detect** your project type (game / web-api / frontend / data-science / general)
2. **Interview** you (6 questions about terminology, constants, formulas, modules)
3. **Generate** Wiki skeleton + 7 index files + state management layer
4. **Install** verification closed-loop (pre-commit hook + verify script)
5. **Start** self-nurturing — every session builds on the last

### Health Check

```
/wiki-check
```

Runs a full verification and produces a health report.

## Lifecycle

```
BIRTH → GROW → GUARD → EVOLVE
```

| Stage | Trigger | What happens |
|-------|---------|-------------|
| **BIRTH** | `/self-nurture` (first time) | Detect → Interview → Install (10-15 min) |
| **GROW** | During daily work | AI discovers new terms/constants/formulas, proposes additions |
| **GUARD** | Every `git commit` | pre-commit hook runs 7 hard + 3 soft checks |
| **EVOLVE** | After 3 uses | Extract patterns from usage logs, improve defaults |

## Verification Rules

### Hard Checks (block commit)

| # | Rule | What it checks |
|---|------|---------------|
| H1 | wiki_referenced | Every Wiki page must be referenced in session-entry |
| H2 | cross_ref_synced | New Wiki must appear in cross-reference.md |
| H3 | tags_synced | New Wiki must have at least one tag |
| H4 | latest_current | LATEST.md must have a valid date |
| H5 | formulas_synced | § formula references must be in formulas.md |
| H6 | spec_synced | New specs must be mentioned in LATEST/CONTINUITY |
| H7 | dir_synced | New directories must be mentioned in LATEST/CONTINUITY |

### Soft Checks (warn only)

| # | Rule | What it checks |
|---|------|---------------|
| S1 | glossary_hint | CamelCase/UPPER_SNAKE terms not in glossary |
| S2 | constants_hint | Magic numbers not in constants.md |
| S3 | gaps_hint | New TODO/FIXME/HACK comments |

## Project Structure

```
self-nurture/
├── SKILL.md                    # Skill entry point
├── VERSION.md                  # Version history
├── plugin.json                 # Plugin registration
├── commands/                   # /self-nurture, /wiki-check
├── hooks/                      # SessionStart hook (Python)
├── prompts/                    # Interviewer, Discoverer, Verifier, Protocols
├── templates/                  # All file templates (Wiki, indexes, scripts)
├── references/                 # Lifecycle, rules, priority, project types
├── _usage-log/                 # Skill self-growth records
└── _patterns/                  # Extracted patterns (after 3 uses)
```

## What Gets Installed in Your Project

After running `/self-nurture`, your project will have:

```
your-project/
├── CLAUDE.md                          # Session protocols appended
├── docs/
│   ├── CURRENT_PROJECT_STATUS.md      # Single source of truth
│   ├── DOC_STATUS_LEDGER.md           # Document status tracking
│   ├── CONTINUITY.md                  # Handoff document
│   ├── _dev-log/LATEST.md             # Daily summary (≤40 lines)
│   ├── _index/                        # 7 index files
│   └── project-wiki/                  # Wiki pages
├── .githooks/pre-commit               # Verification hook
└── scripts/
    ├── verify_wiki_sync.py            # 7H + 3S verification
    └── install_hooks.py               # One-click hook setup
```

## Origin

This skill was reverse-engineered from a production self-nurturing system built for the「天道降臨 — 文字三國」game development project, which achieved a v3 maturity rating with:

- 7 hard checks + 3 soft checks
- 25 research Wiki pages + 12 engineering Wiki pages
- Fully automated pre-commit verification
- Cross-session context continuity

## Compatibility

- **Claude Code** — Native skill
- **Codex** — See [Codex migration spec](docs/superpowers/specs/2026-04-22-codex-self-nurturing-harness-spec.md) for adaptation guide
- **Windows / Linux / macOS** — All hooks use Python (cross-platform)

## License

MIT

## Author

**漢霖** (HansLin) — Built with Claude Code
