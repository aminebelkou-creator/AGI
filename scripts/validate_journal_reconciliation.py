#!/usr/bin/env python3
"""Reconcile the AGI journal index, article files, crawl map and WordPress export."""
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
V2 = ROOT / "v2"
EXPORT = ROOT / "data" / "export" / "AGI_Website_Content_Export.json"
CONTENT_MAP = ROOT / "docs" / "content-map.csv"
JOURNAL_INDEX = V2 / "journal.html"
JOURNAL_DIR = V2 / "journal"
DESIGNED_CCGI = V2 / "journal-ccgi-partnership.html"

export = json.loads(EXPORT.read_text(encoding="utf-8"))
news = export["news"]
news_by_slug = {item["slug"]: item for item in news}
assert len(news_by_slug) == len(news), "Duplicate WordPress news slugs"

journal_html = JOURNAL_INDEX.read_text(encoding="utf-8")
card_hrefs = re.findall(r'<a class="card" href="(journal/[^"]+)"', journal_html)
card_slugs = [pathlib.PurePosixPath(href).stem for href in card_hrefs]
assert len(card_hrefs) == len(set(card_hrefs)), "Duplicate journal card links"

article_files = {p.name for p in JOURNAL_DIR.glob("*.html")}
missing_files = sorted({pathlib.PurePosixPath(href).name for href in card_hrefs} - article_files)
assert not missing_files, f"Journal cards without article files: {missing_files}"

with CONTENT_MAP.open(encoding="utf-8-sig", newline="") as handle:
    mapped = [row for row in csv.DictReader(handle) if row.get("destination", "").startswith("journal/")]
map_destinations = {row["destination"] for row in mapped}
card_destinations = set(card_hrefs)
assert map_destinations == card_destinations, (
    f"Content-map/index mismatch: map-only={sorted(map_destinations-card_destinations)}, "
    f"index-only={sorted(card_destinations-map_destinations)}"
)

matched = {slug for slug in card_slugs if slug in news_by_slug}
crawl_only = set(card_slugs) - set(news_by_slug)
unindexed_export = [item for item in news if item["slug"] not in set(card_slugs)]
assert len(news) == 60, f"Expected 60 source export posts, found {len(news)}"
assert len(card_hrefs) == 66, f"Expected 66 journal cards, found {len(card_hrefs)}"
assert len(article_files) == 66, f"Expected 66 article files, found {len(article_files)}"
assert len(matched) == 59, f"Expected 59 export posts represented in journal cards, found {len(matched)}"
assert len(crawl_only) == 7, f"Expected 7 crawl-only journal cards, found {len(crawl_only)}"
assert len(unindexed_export) == 1, f"Expected one designed export post outside the journal cards, found {len(unindexed_export)}"
assert "chichester" in unindexed_export[0]["slug"].lower(), "The unindexed export post is not the expected CCGi announcement"
assert DESIGNED_CCGI.is_file(), "The standalone designed CCGi article is missing"

print(
    f"PASS: {len(news)} WordPress news records; {len(card_hrefs)} journal cards and article files; "
    f"{len(matched)} export posts indexed; {len(crawl_only)} crawl-only entries; "
    "one CCGi export post mapped to a standalone designed page."
)
