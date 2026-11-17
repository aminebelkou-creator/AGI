#!/usr/bin/env python3
"""Validate the proposed AGI legacy-route disposition matrix against the live-in-repo index."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "app/public/content/index.json"
MATRIX = ROOT / "content/migration/route-content-review.csv"
IA = ROOT / "content/strategy/proposed-information-architecture-v2.md"

def main() -> int:
    routes = json.loads(INDEX.read_text(encoding="utf-8"))
    with MATRIX.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {
        "legacy_route", "legacy_title", "proposed_route", "target_section",
        "content_type", "proposed_action", "priority",
        "observed_content_finding", "owner_or_evidence_gate", "legacy_url_handling",
    }
    if not rows:
        raise ValueError("Route review matrix is empty")
    missing_columns = sorted(required - set(rows[0]))
    if missing_columns:
        raise ValueError(f"Missing matrix columns: {missing_columns}")
    matrix_routes = [row["legacy_route"] for row in rows]
    duplicates = sorted({route for route in matrix_routes if matrix_routes.count(route) > 1})
    if duplicates:
        raise ValueError(f"Duplicate routes in matrix: {duplicates}")
    if set(matrix_routes) != set(routes):
        missing = sorted(set(routes) - set(matrix_routes))
        extra = sorted(set(matrix_routes) - set(routes))
        raise ValueError(f"Route coverage mismatch; missing={missing}, extra={extra}")
    for row in rows:
        for field in required:
            if field != "proposed_route" and not row[field].strip():
                raise ValueError(f"{row['legacy_route']}: empty required field {field}")
        if row["priority"] not in {"high", "medium", "low"}:
            raise ValueError(f"{row['legacy_route']}: invalid priority {row['priority']}")
    if not IA.is_file() or IA.stat().st_size < 5000:
        raise ValueError("Proposed information architecture document is missing or unexpectedly short")
    print(f"PASS: route disposition matrix covers all {len(routes)} indexed legacy routes.")
    print(f"PASS: {len(rows)} unique route decisions; priorities and evidence gates are populated.")
    print("PASS: proposed information architecture document exists.")
    print("NOTE: this validates completeness and consistency, not human approval of recommendations.")
    return 0

if __name__ == "__main__":
    main()
