#!/usr/bin/env python3
"""
Self-Nurture Stop Hook — Milestone Safety Net (v1.0.1)

Runs after each Claude turn. Detects large uncommitted changes
or stale LATEST.md and injects a reminder. Quiet mode: no warning
= no output. Never blocks. Always exits 0. Pure read-only.

Origin: reverse-engineered from a production project where AI completed
81 files / 6156 lines without committing — a real-world self-nurturing failure.
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

MAX_FILES = 10
MAX_LINES = 300
STALE_HOURS = 4


def main():
    # Only run if self-nurture is installed
    if not Path("docs/project-wiki").exists():
        return 0

    warnings = []

    # Check 1: Uncommitted changes scale
    try:
        r = subprocess.run(
            ["git", "diff", "--shortstat", "HEAD"],
            capture_output=True, text=True, timeout=5
        )
        stat = r.stdout.strip()
        if stat:
            fm = re.search(r"(\d+) files? changed", stat)
            im = re.search(r"(\d+) insertions?", stat)
            dm = re.search(r"(\d+) deletions?", stat)
            files = int(fm.group(1)) if fm else 0
            lines = (int(im.group(1)) if im else 0) + (int(dm.group(1)) if dm else 0)

            # Count untracked
            r2 = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True, text=True, timeout=5
            )
            untracked = len([l for l in r2.stdout.splitlines() if l.startswith("??")])
            files += untracked

            if files >= MAX_FILES:
                warnings.append(f"🔴 {files} 個檔案未 commit（閾值 {MAX_FILES}）")
            if lines >= MAX_LINES:
                warnings.append(f"🔴 {lines} 行 diff 未 commit（閾值 {MAX_LINES}）")
    except Exception:
        pass

    # Check 2: LATEST.md freshness
    latest = Path("docs/_dev-log/LATEST.md")
    if latest.exists():
        try:
            content = latest.read_text(encoding="utf-8", errors="replace")
            match = re.search(r"最後更新[：:]\s*(\d{4}-\d{2}-\d{2})", content)
            if match:
                last = datetime.strptime(match.group(1), "%Y-%m-%d")
                age = datetime.now() - last
            else:
                age = datetime.now() - datetime.fromtimestamp(latest.stat().st_mtime)

            if age > timedelta(hours=STALE_HOURS):
                h = int(age.total_seconds() / 3600)
                warnings.append(f"🟡 LATEST.md 已 {h} 小時未更新（閾值 {STALE_HOURS}h）")
        except Exception:
            pass

    # Quiet mode
    if not warnings:
        return 0

    msg = "\n".join([
        "⚠️ Self-Nurture 自養提醒：",
        "",
        *warnings,
        "",
        "建議：分批 commit → 更新 LATEST.md → 檢查自養觸發規則",
    ])

    print(json.dumps({"decision": "approve", "systemMessage": msg}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
