import os, re, json, csv, urllib.request, ssl
V2 = r"C:\Users\belko\AGI\v2"; ROOT = os.path.dirname(V2)
OUT = os.path.join(V2, "assets", "journal", "files"); os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130.0 Safari/537.36"}
rows = list(csv.DictReader(open(os.path.join(ROOT, "docs", "external-links.csv"), encoding="utf-8-sig")))
mapping = {}
for r in rows:
    u = r["url"]
    if r["status"].startswith("OLD SITE") and "/wp-content/uploads/" in u:
        name = u.split("/")[-1].split("?")[0]
        dst = os.path.join(OUT, name)
        try:
            if not os.path.exists(dst):
                with urllib.request.urlopen(urllib.request.Request(u.replace("http://", "https://"), headers=UA), timeout=120, context=ssl.create_default_context()) as resp:
                    open(dst, "wb").write(resp.read())
            mapping[u] = "assets/journal/files/" + name
            print(f"saved {name}: {os.path.getsize(dst) // 1024} KB")
        except Exception as e: print("FAILED", u, e)
json.dump(mapping, open(os.path.join(V2, "_build", "old-site-files.json"), "w"), indent=1)
print("mapped:", len(mapping))
