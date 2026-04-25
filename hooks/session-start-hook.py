#!/usr/bin/env python3
"""
Self-Nurture Session Start Hook (Skill-level)

Detects whether the current project has self-nurture installed
(by checking for docs/project-wiki/ directory). If installed,
injects LATEST.md + CURRENT_PROJECT_STATUS.md + git log into
the session context via systemMessage.
"""
import json
import subprocess
import sys
from pathlib import Path


def main():
    wiki_dir = Path("docs/project-wiki")
    if not wiki_dir.exists():
        # Not a self-nurture project — skip silently
        sys.exit(0)

    parts = []

    # Step 1: Read LATEST.md (first 40 lines)
    latest = Path("docs/_dev-log/LATEST.md")
    if latest.exists():
        try:
            lines = latest.read_text(encoding="utf-8", errors="replace").splitlines()
            content = "\n".join(lines[:40])
            parts.append(f"--- LATEST.md (前 40 行) ---\n{content}")
        except Exception:
            parts.append("--- LATEST.md ---\n（讀取失敗）")

    # Step 2: Read CURRENT_PROJECT_STATUS.md (first 20 lines)
    status = Path("docs/CURRENT_PROJECT_STATUS.md")
    if status.exists():
        try:
            lines = status.read_text(encoding="utf-8", errors="replace").splitlines()
            content = "\n".join(lines[:20])
            parts.append(f"--- CURRENT_PROJECT_STATUS.md (前 20 行) ---\n{content}")
        except Exception:
            pass

    # Step 7: git log --oneline -5
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "-5"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            parts.append(f"--- git log ---\n{result.stdout.strip()}")
    except Exception:
        pass

    # Step 8: Verify hooks path
    hooks_status = "未設定"
    try:
        result = subprocess.run(
            ["git", "config", "--get", "core.hooksPath"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            hooks_status = result.stdout.strip()
    except Exception:
        pass
    parts.append(f"--- hooks ---\nhooksPath: {hooks_status}")

    # Build system message
    body = "\n\n".join(parts)
    output = {
        "systemMessage": (
            "🌱 Self-Nurture Active | 請按 CLAUDE.md 的 Session Start Protocol 回報現況\n\n"
            + body
        )
    }
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
