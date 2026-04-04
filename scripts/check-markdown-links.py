#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:")
TITLE_SUFFIX_RE = re.compile(
    r"""^(?P<target>.*?)(?:\s+(?:"[^"]*"|'[^']*'|\([^()]*\)))?\s*$"""
)


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
    target = raw_target.strip()
    if not target:
        return ""

    if target.startswith("<"):
        closing = target.find(">")
        target = target[1:closing] if closing != -1 else target[1:]
    else:
        title_match = TITLE_SUFFIX_RE.match(target)
        if title_match:
            target = title_match.group("target").strip()

    return unquote(target)


def should_skip(target: str) -> bool:
    if not target or target.startswith("#"):
        return True
    return target.startswith(SKIP_PREFIXES)


def resolve_target(source: Path, target: str) -> Path:
    path_only = target.split("#", 1)[0]
    return (source.parent / path_only).resolve()


def find_closing_bracket(markdown: str, start: int) -> int:
    depth = 1
    index = start + 1

    while index < len(markdown):
        char = markdown[index]
        if char == "\\":
            index += 2
            continue
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return index
        index += 1

    return -1


def extract_parenthesized(markdown: str, start: int) -> tuple[str, int] | None:
    depth = 0
    in_angle = False
    chars: list[str] = []
    index = start + 1

    while index < len(markdown):
        char = markdown[index]
        if char == "\\" and index + 1 < len(markdown):
            chars.append(char)
            chars.append(markdown[index + 1])
            index += 2
            continue

        if char == "<" and not in_angle:
            in_angle = True
        elif char == ">" and in_angle:
            in_angle = False
        elif not in_angle and char == "(":
            depth += 1
        elif not in_angle and char == ")":
            if depth == 0:
                return ("".join(chars), index)
            depth -= 1

        chars.append(char)
        index += 1

    return None


def collect_targets(markdown: str) -> list[str]:
    targets: list[str] = []
    index = 0

    while index < len(markdown):
        char = markdown[index]
        if char == "!" and index + 1 < len(markdown) and markdown[index + 1] == "[":
            label_start = index + 1
        elif char == "[":
            label_start = index
        else:
            index += 1
            continue

        label_end = find_closing_bracket(markdown, label_start)
        if label_end == -1 or label_end + 1 >= len(markdown) or markdown[label_end + 1] != "(":
            index = label_start + 1
            continue

        extracted = extract_parenthesized(markdown, label_end + 1)
        if extracted is None:
            index = label_end + 1
            continue

        target, target_end = extracted
        targets.append(target)
        index = target_end + 1

    return targets


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
