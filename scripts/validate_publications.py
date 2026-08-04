#!/usr/bin/env python3
"""Validate the public publication catalog against the human-readable archive."""

from __future__ import annotations

import csv
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "publications" / "catalog.csv"
ARCHIVE = ROOT / "publications" / "2026.md"
REQUIRED = {
    "published_date",
    "platform",
    "format",
    "title_or_opening",
    "url",
    "topic",
    "status",
}
EXPECTED_COUNTS = {"Insight Extractor": 12, "LinkedIn": 22}


def main() -> int:
    errors: list[str] = []
    with CATALOG.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            errors.append(f"catalog missing columns: {sorted(missing)}")
        rows = list(reader)

    archive_text = ARCHIVE.read_text(encoding="utf-8")
    urls: list[str] = []
    counts: Counter[str] = Counter()

    for line_number, row in enumerate(rows, start=2):
        empty = sorted(field for field in REQUIRED if not row.get(field, "").strip())
        if empty:
            errors.append(f"line {line_number}: empty fields {empty}")
            continue

        try:
            published = date.fromisoformat(row["published_date"])
            if published.year != 2026:
                errors.append(f"line {line_number}: date is outside 2026")
        except ValueError:
            errors.append(f"line {line_number}: invalid date {row['published_date']!r}")

        parsed = urlparse(row["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"line {line_number}: URL is not public HTTPS")
        if row["status"] != "verified_public":
            errors.append(f"line {line_number}: unsupported status {row['status']!r}")
        if row["url"] not in archive_text:
            errors.append(f"line {line_number}: URL missing from 2026.md")

        urls.append(row["url"])
        counts[row["platform"]] += 1

    duplicates = sorted(url for url, count in Counter(urls).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate URLs: {duplicates}")
    if dict(counts) != EXPECTED_COUNTS:
        errors.append(f"platform counts {dict(counts)} != {EXPECTED_COUNTS}")
    if len(rows) != sum(EXPECTED_COUNTS.values()):
        errors.append(f"catalog has {len(rows)} rows, expected {sum(EXPECTED_COUNTS.values())}")

    if errors:
        print("Publication catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Publication catalog OK: {len(rows)} verified records; {dict(counts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
