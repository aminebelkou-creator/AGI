import json, sys
inv = json.load(open(r"C:\Users\belko\AGI\data\crawl\inventory.json", encoding="utf-8"))
for part, n in [("school-calandar", 3000), ("admission-fee", 2600), ("/enrollment", 1800), ("admissions-procedure", 2600), ("handbook", 2500), ("supplies-list", 1600)]:
    p = next(x for x in inv if part in x["url"])
    print(f"\n######## {p['title']} ({p['words']}w)\n{p['text'][:n]}")
