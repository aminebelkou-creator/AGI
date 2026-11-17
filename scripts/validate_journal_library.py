#!/usr/bin/env python3
"""Validate AGI's source-preserved journal content library."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "content" / "library" / "journal-records.json"
SCHEMA = ROOT / "content" / "schemas" / "journal-content-library.schema.json"

data = json.loads(PATH.read_text(encoding="utf-8"))
json.loads(SCHEMA.read_text(encoding="utf-8"))
assert data["format"] == "agi-journal-content-library-v1"
records = data["records"]
ids = [record["id"] for record in records]
assert len(ids) == len(set(ids)), "Duplicate journal record IDs"
assert len(records) == data["counts"]["total"]
assert sum(record["source_type"] == "wordpress-export" for record in records) == data["counts"]["wordpress_export"]
assert sum(record["source_type"] == "crawl-inventory" for record in records) == data["counts"]["crawl_inventory"]
assert data["counts"]["total"] == data["counts"]["wordpress_export"] + data["counts"]["crawl_inventory"]

allowed_locales = {"en-US", "fr-MA", "ar-MA", "und"}
allowed_status = {"source-captured", "editorial-review", "rights-review", "partner-approval", "legal-review", "archived-candidate", "approved", "published"}
for record in records:
    assert re.fullmatch(r"agi\\.journal\\.[a-z0-9-]+", record["id"]), record["id"]
    assert record["source_type"] in {"wordpress-export", "crawl-inventory"}
    assert record["source_locale"] in allowed_locales, (record["id"], record["source_locale"])
    assert record["title"].strip() and record["slug"].strip() and record["canonical_route"].strip()
    assert record["editorial_status"] in allowed_status
    assert record["image_rights_status"] in {"review-required", "approved", "no-image"}
    assert (record.get("body_markdown") or record.get("body_text") or "").strip(), (record["id"], "empty source body")
    assert isinstance(record["review_notes"], list) and isinstance(record["evidence_gates"], list)
    assert record["editorial_status"] != "published", "Source capture must not auto-publish"

print(f"PASS: {len(records)} historical journal records; {data['counts']['wordpress_export']} WordPress exports + {data['counts']['crawl_inventory']} crawl-only sources; source text and review gates present.")
