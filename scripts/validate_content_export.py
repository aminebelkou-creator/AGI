#!/usr/bin/env python3
"""Validate AGI's CMS-neutral content export using only the Python standard library."""
import csv, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXPORT = ROOT / "content" / "entries.json"
CLAIMS = ROOT / "content" / "governance" / "claims-register.csv"

data = json.loads(EXPORT.read_text(encoding="utf-8"))
assert data["format"] == "agi-content-bundle-v1"
entries = data["entries"]
assert len(entries) == data["record_count"], f"Unexpected record count: {len(entries)}"
locales = {"en-US", "fr-MA", "ar-MA"}
assert {e["locale"] for e in entries} == locales
page_groups = {e["slug"] for e in entries}
assert len(entries) == len(page_groups) * len(locales), "Each page group must have one entry per locale"
assert len({(e["id"], e["locale"]) for e in entries}) == len(entries), "Duplicate id/locale pair"
assert all(e["direction"] == ("rtl" if e["locale"] == "ar-MA" else "ltr") for e in entries)
assert all(e["status"] in {"editorial-review", "translation-review"} for e in entries)
assert all(e["body"].strip() and e["title"].strip() for e in entries)

with CLAIMS.open(encoding="utf-8", newline="") as f:
    known_claims = {row["Claim ID"] for row in csv.DictReader(f)}
unknown = sorted({claim for entry in entries for claim in entry["claims"]} - known_claims)
assert not unknown, f"Unknown claim references: {unknown}"
assert all(isinstance(e["claims"], list) and isinstance(e["sources"], list) for e in entries)

print(f"PASS: {len(entries)} structured entries; {len(page_groups)} pages × {len(locales)} locales; RTL/LTR and review states valid; claim references resolve.")
