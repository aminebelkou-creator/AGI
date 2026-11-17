#!/usr/bin/env python3
"""Validate AGI's reusable multilingual content library (Python standard library only)."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "content" / "library" / "reusable-content-library.json"
SCHEMA = ROOT / "content" / "schemas" / "reusable-content-library.schema.json"

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

print(f"PASS: {len(items)} reusable content modules; {len(items) * len(locales)} locale variants; unique IDs and complete editorial states.")
