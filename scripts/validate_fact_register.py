#!/usr/bin/env python3
"""Validate the public, non-sensitive AGI website fact register."""
import csv
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "content" / "facts" / "fact-register.csv"
REQUIRED = {
    "fact_id", "subject", "claim_or_value", "locale_format", "source_reference",
    "current_status", "owner", "verification_required", "last_verified_utc",
    "review_due_utc", "publication_rule"
}
ALLOWED = {
    "unverified", "owner-confirmation-required", "partner-approval-required",
    "legal-review-required", "specialist-review-required", "verified"
}
with PATH.open(encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    assert reader.fieldnames and REQUIRED.issubset(reader.fieldnames), "Missing fact-register columns"
    rows = list(reader)
ids = [row["fact_id"] for row in rows]
assert len(rows) >= 10, f"Fact register unexpectedly small: {len(rows)}"
assert len(ids) == len(set(ids)), "Duplicate fact IDs"
for row in rows:
    assert re.fullmatch(r"F-AGI-[0-9]{3}", row["fact_id"]), row["fact_id"]
    assert row["current_status"] in ALLOWED, (row["fact_id"], row["current_status"])
    for key in REQUIRED - {"last_verified_utc", "review_due_utc"}:
        assert row[key].strip(), (row["fact_id"], "empty", key)
    if row["current_status"] == "verified":
        assert row["last_verified_utc"] and row["review_due_utc"], (
            row["fact_id"], "verified facts require verification and review dates"
        )
print(f"PASS: {len(rows)} governed facts; unique IDs, owners, evidence requirements and publication rules present.")
