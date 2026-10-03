"""Fact-conflict check: prices on pages that are not in the fact register (possible outdated or wrong fees).
python _build/fact_conflicts.py -> docs/fact-conflicts.csv"""
import os, re, json, html, csv
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
facts = json.dumps(json.load(open(os.path.join(V2, "_build", "facts.json"), encoding="utf-8")), ensure_ascii=False)
KNOWN = {int(re.sub(r"\D", "", x)) for x in re.findall(r"\d[\d,]*(?=\s?(?:MAD|DH|dirhams|EUR|€))", facts)} | {26000, 1200, 100, 150, 200, 500, 3000, 15}
rows = []
files = [f for f in sorted(os.listdir(V2)) if f.endswith(".html")] + [f"{d}/{f}" for d in ("journal", "fr", "ar") if os.path.isdir(os.path.join(V2, d)) for f in sorted(os.listdir(os.path.join(V2, d))) if f.endswith(".html")]
for f in files:
    s = open(os.path.join(V2, f), encoding="utf-8").read(); m = re.search(r"<main\b.*?</main>", s, re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(0) if m else "")))
    archived = "Archived post" in t or "Archive:" in t
    for mm in re.finditer(r"(\d{1,3}(?:[ ,.]\d{3})+|\d+)\s?(MAD|DH|Dhs|dirhams?|Dirhams|درهم)", t):
        v = int(re.sub(r"\D", "", mm.group(1)))
        if v not in KNOWN:
            rows.append((f, mm.group(0), "archived post (banner shown)" if archived else "CHECK – not in the fact register", t[max(0, mm.start() - 70):mm.end() + 50]))
with open(os.path.join(ROOT, "docs", "fact-conflicts.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["page", "amount", "status", "context"]); w.writerows(rows)
live = [r for r in rows if r[2].startswith("CHECK")]
print(f"amounts not in the fact register: {len(rows)} ({len(live)} on current pages, {len(rows) - len(live)} in archived posts)")
for r in live[:15]: print(f"   {r[0]:40} {r[1]:14} …{r[3][:100]}…")
