import json
items = json.load(open(r"C:\Users\belko\AGI\data\crawl\inventory.json", encoding="utf-8"))
want = [("anglia", "FAQ", 3500), ("anglia", "Exams", 2600), ("anglia", "Special Arrangements", 1600), ("anglia", "AngliaMorocco Networks", 3000),
        ("anglia", "ANGLIA EXAM DATES", 1200), ("anglia", "Practice Resources", 1000), ("agi", "Online Tutoring Session Prices", 1500), ("agi", "Holistic Play Therapy", 1400),
        ("agi", "Anglia Morocco Learning Pods", 1600), ("agi", "Policies & Procedures", 2200)]
for site, t, n in want:
    it = next((i for i in items if i["site"] == site and i["lang"] == "en" and i["title"].strip().lower().startswith(t.lower())), None)
    if it: print(f"\n######## {site}: {it['title']} ({it['url']})\n{it['text'][:n]}")
