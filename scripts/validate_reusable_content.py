#!/usr/bin/env python3
"""Validate AGI's reusable multilingual content library (Python standard library only)."""
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "content" / "library" / "reusable-content-library.json"
SCHEMA = ROOT / "content" / "schemas" / "reusable-content-library.schema.json"
COMPOSITIONS = ROOT / "content" / "library" / "page-compositions.json"
PAGE_EXPORT = ROOT / "content" / "entries.json"
FACTS = ROOT / "content" / "facts" / "fact-register.csv"

data = json.loads(LIBRARY.read_text(encoding="utf-8"))
json.loads(SCHEMA.read_text(encoding="utf-8"))
assert data["format"] == "agi-reusable-content-library-v1"
assert data["editorial_master_locale"] == "en-US"
locales = {"en-US", "fr-MA", "ar-MA"}
assert set(data["supported_locales"]) == locales
items = data["content_items"]
ids = [item["id"] for item in items]
assert len(ids) == len(set(ids)), "Duplicate content item ID"
assert len(items) >= 10, f"Expected a useful initial library, got {len(items)} items"

allowed_status = {"draft", "editorial-review", "translation-review", "legal-review", "partner-approval", "approved", "published", "archived"}
allowed_types = {"brand-message", "brand-pillar", "programme-description", "service-description", "resource-description", "call-to-action", "faq-answer", "policy-summary", "proof-point", "story"}
for item in items:
    assert re.fullmatch(r"agi(?:\.[a-z0-9-]+)+", item["id"]), item["id"]
    assert item["type"] in allowed_types, (item["id"], item["type"])
    assert item["status"] in allowed_status, (item["id"], item["status"])
    assert set(item["locales"]) == locales, f"Missing locale for {item['id']}"
    assert isinstance(item["evidence_gates"], list)
    for locale, copy in item["locales"].items():
        assert copy["status"] in allowed_status, (item["id"], locale, copy["status"])
        assert copy["title"].strip() and copy["body"].strip(), (item["id"], locale)
        assert copy["summary"].strip(), (item["id"], locale, "empty summary")
    assert item["locales"]["en-US"]["status"] != "published", "This first batch must not be auto-published"

composition_data = json.loads(COMPOSITIONS.read_text(encoding="utf-8"))
page_export = json.loads(PAGE_EXPORT.read_text(encoding="utf-8"))
with FACTS.open(encoding="utf-8", newline="") as handle:
    known_fact_ids = {row["fact_id"] for row in csv.DictReader(handle)}
for item in items:
    for fact_id in item.get("fact_refs", []):
        assert fact_id in known_fact_ids, (item["id"], "unknown fact reference", fact_id)
module_ids = set(ids)
page_entry_ids = {entry["id"] for entry in page_export["entries"]}
page_ids = [page["page_id"] for page in composition_data["pages"]]
assert len(page_ids) == len(set(page_ids)), "Duplicate page composition ID"
for page in composition_data["pages"]:
    assert page["existing_page_entry"] in page_entry_ids, (page["page_id"], "unknown page entry")
    assert page["modules"], (page["page_id"], "no modules")
    for block in page["modules"]:
        assert block["module_id"] in module_ids, (page["page_id"], "unknown module", block["module_id"])
    assert isinstance(page["missing_content"], list)
print(f"PASS: {len(items)} reusable content modules; {len(items) * len(locales)} locale variants; {len(composition_data['pages'])} page compositions; all module references resolve.")
