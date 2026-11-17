#!/usr/bin/env python3
"""Validate AGI's CMS-neutral content export using only the Python standard library."""
import json, pathlib, sys
p = pathlib.Path(__file__).resolve().parents[1] / "content" / "entries.json"
data = json.loads(p.read_text(encoding="utf-8"))
assert data["format"] == "agi-content-bundle-v1"
entries = data["entries"]
assert len(entries) == 36 == data["record_count"]
assert len({(e["id"], e["locale"]) for e in entries}) == 36
assert {e["locale"] for e in entries} == {"en-US", "fr-MA", "ar-MA"}
assert all(e["direction"] == ("rtl" if e["locale"] == "ar-MA" else "ltr") for e in entries)
assert all(e["status"] in {"editorial-review", "translation-review"} for e in entries)
assert all(e["body"].strip() and e["title"].strip() for e in entries)
print("PASS: 36 structured entries; 12 pages × 3 locales; locale direction and review states valid.")
