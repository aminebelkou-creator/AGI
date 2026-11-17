#!/usr/bin/env python3
"""Audit legacy AGI route/news indexes against their referenced JSON files.

Run from any directory: python scripts/audit_legacy_content.py
Uses only the Python standard library and never changes source files.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "app" / "public" / "content"
PAGES = CONTENT / "pages"
ROUTE_INDEX = CONTENT / "index.json"
NEWS_INDEX = CONTENT / "news.json"
DATE_RE = re.compile(r"^\\d{4}-\\d{2}-\\d{2}$")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # report malformed source files as audit failures
        raise ValueError(f"Cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    routes = load_json(ROUTE_INDEX)
    news = load_json(NEWS_INDEX)

    if not isinstance(routes, dict):
        raise ValueError("content/index.json must contain a route-keyed JSON object")
    if not isinstance(news, list):
        raise ValueError("content/news.json must contain a JSON array")

    route_keys = list(routes)
    route_files: list[str] = []
    section_counts: Counter[str] = Counter()
    for route, record in routes.items():
        if not isinstance(route, str) or not route.startswith("/"):
            errors.append(f"Invalid route key: {route!r}")
        if not isinstance(record, dict):
            errors.append(f"{route}: route record is not an object")
            continue
        for field in ("title", "fullTitle", "section", "file"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                errors.append(f"{route}: missing/empty {field}")
        filename = record.get("file")
        if isinstance(filename, str):
            route_files.append(filename)
        if isinstance(record.get("section"), str):
            section_counts[record["section"]] += 1

    news_files: list[str] = []
    news_slugs: list[str] = []
    news_dates: list[str] = []
    for i, record in enumerate(news):
        if not isinstance(record, dict):
            errors.append(f"news[{i}]: record is not an object")
            continue
        for field in ("title", "slug", "date", "file"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                errors.append(f"news[{i}]: missing/empty {field}")
        if isinstance(record.get("file"), str):
            news_files.append(record["file"])
        if isinstance(record.get("slug"), str):
            news_slugs.append(record["slug"])
        raw_date = record.get("date")
        if isinstance(raw_date, str):
            if not DATE_RE.fullmatch(raw_date):
                errors.append(f"news[{i}] {record.get('slug')}: date is not YYYY-MM-DD")
            else:
                try:
                    date.fromisoformat(raw_date)
                    news_dates.append(raw_date)
                except ValueError:
                    errors.append(f"news[{i}] {record.get('slug')}: invalid calendar date {raw_date}")

    def duplicates(values: list[str]) -> list[str]:
        counts = Counter(values)
        return sorted(value for value, count in counts.items() if count > 1)

    for route in duplicates(route_keys):
        errors.append(f"Duplicate route: {route}")
    for filename in duplicates(route_files + news_files):
        errors.append(f"File referenced more than once: {filename}")
    for slug in duplicates(news_slugs):
        errors.append(f"Duplicate news slug: {slug}")

    referenced = set(route_files + news_files)
    for filename in sorted(referenced):
        if Path(filename).name != filename or filename in {".", ".."}:
            errors.append(f"Unsafe/non-local content filename: {filename}")
            continue
        path = PAGES / filename
        if not path.is_file():
            errors.append(f"Missing referenced file: {path.relative_to(ROOT)}")
            continue
        try:
            payload = load_json(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if not isinstance(payload, dict):
            errors.append(f"{path.relative_to(ROOT)}: expected JSON object")
            continue
        for field in ("title", "markdown"):
            if not isinstance(payload.get(field), str) or not payload[field].strip():
                errors.append(f"{path.relative_to(ROOT)}: missing/empty {field}")
        if filename.startswith("news__") and not isinstance(payload.get("date"), str):
            warnings.append(f"{path.relative_to(ROOT)}: article body has no date field")

    actual_files = {
        path.name for path in PAGES.glob("*.json") if path.is_file()
    }
    orphaned = sorted(actual_files - referenced)
    for filename in orphaned:
        warnings.append(f"Unreferenced JSON file (review; do not auto-delete): {filename}")

    print("AGI legacy content audit")
    print(f"Routes: {len(routes)}")
    print(f"News records: {len(news)}")
    print(f"Referenced JSON files: {len(referenced)}")
    print(f"JSON files present: {len(actual_files)}")
    print("Routes by section: " + ", ".join(f"{k}={v}" for k, v in sorted(section_counts.items())))
    if news_dates:
        print(f"News date range: {min(news_dates)} to {max(news_dates)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")

    if errors:
        print("FAIL: legacy content integrity checks need attention.")
        return 1
    print("PASS: every indexed route/news record resolves to a valid JSON content file.")
    if orphaned:
        print("REVIEW: unreferenced files exist; preserve until manually classified.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        raise SystemExit(2)
