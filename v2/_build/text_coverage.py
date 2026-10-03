import csv, json
m = {r["url"]: r for r in csv.DictReader(open(r"C:\Users\belko\AGI\docs\content-map.csv", encoding="utf-8-sig"))}
inv = json.load(open(r"C:\Users\belko\AGI\data\crawl\inventory.json", encoding="utf-8"))
ph = __import__("sys").argv[1] if len(__import__("sys").argv) > 1 else "2"
for p in sorted(inv, key=lambda x: (x.get("text_coverage") or 0)):
    r = m.get(p["url"])
    if r and r["phase"] == ph and r["action"] != "drop":
        print(f"{str(p['text_coverage']):5} {p['status']:8} {r['destination']:34} {p['title'][:52]}")
