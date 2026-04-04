#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!\!)\[[^\]]+\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:")


def tracked_markdown_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "*.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [ROOT / line for line in result.stdout.splitlines() if line.strip()]


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip().strip("<>").split()[0]
    return unquote(target)


def should_skip(target: str) -> bool:
    if not target or target.startswith("#"):
        return True
    return target.startswith(SKIP_PREFIXES)


def resolve_target(source: Path, target: str) -> Path:
    path_only = target.split("#", 1)[0]
    return (source.parent / path_only).resolve()


def collect_targets(markdown: str) -> list[str]:
    return [*LINK_RE.findall(markdown), *IMAGE_RE.findall(markdown)]


def main() -> int:
    failures: list[str] = []

    for markdown_file in tracked_markdown_files():
        content = markdown_file.read_text(encoding="utf-8")
        for raw_target in collect_targets(content):
            target = normalize_target(raw_target)
            if should_skip(target):
                continue

            resolved = resolve_target(markdown_file, target)
            if not resolved.exists():
                failures.append(
                    f"{markdown_file.relative_to(ROOT)} -> {target} (missing: {resolved.relative_to(ROOT) if resolved.is_relative_to(ROOT) else resolved})"
                )

    if failures:
        print("Markdown link checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Markdown link checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
