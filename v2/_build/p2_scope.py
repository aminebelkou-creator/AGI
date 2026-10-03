import csv, json, re, os
from collections import defaultdict
ROOT = r"C:\Users\belko\AGI"
rows = [r for r in csv.DictReader(open(os.path.join(ROOT, "docs", "content-map.csv"), encoding="utf-8-sig")) if r["phase"] == "2"]
inv = {p["url"]: p for p in json.load(open(os.path.join(ROOT, "data", "crawl", "inventory.json"), encoding="utf-8"))}
by = defaultdict(list)
for r in rows: by[r["destination"]].append(r)
for d, rs in sorted(by.items()):
    print(f"\n== {d}")
    for r in rs: print(f"   [{r['site']}/{r['action']}] {r['words']:>5}w facts:{r['facts']:>3}  {r['title'][:55]:55} {r['url'][-55:]}")
# download links on the practice / audio / books pages (from the raw HTML)
for fn in os.listdir(os.path.join(ROOT, "data", "crawl", "anglia")):
    if re.search(r"practice|audio|book|step", fn):
        raw = open(os.path.join(ROOT, "data", "crawl", "anglia", fn), encoding="utf-8", errors="ignore").read()
        links = re.findall(r'href="(https?://[^"]+\.(?:pdf|mp3|zip|docx?))"', raw, re.I)
        print(f"\n{fn}: {len(links)} file links, e.g. {links[:3]}")
print("\nall anglia urls:", sorted(u for u in inv if "angliamorocco" in u))
