import json, csv
inv = {p["url"]: p for p in json.load(open(r"C:\Users\belko\AGI\data\crawl\inventory.json", encoding="utf-8"))}
rows = [r for r in csv.DictReader(open(r"C:\Users\belko\AGI\docs\content-map.csv", encoding="utf-8-sig")) if r["phase"] == "5" and r["action"] != "drop"]
for r in rows:
    p = inv[r["url"]]; t = p["text"]
    n = 1200 if r["destination"] in ("index.html", "about.html", "forms.html", "contact.html") else 500
    heads = [l for l in t.split("\n") if l.startswith("#")][:25]
    print(f"\n######## [{r['destination']}] {p['title']} ({p['words']}w) facts={p['facts']}\nHEADINGS: {' | '.join(h.lstrip('# ')[:50] for h in heads)}\n{t[:n]}")
