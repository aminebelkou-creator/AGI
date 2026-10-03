import os, re, json, collections
C = r"C:\Users\belko\AGI\data\crawl\anglia"
home = open(os.path.join(C, "_home.html"), encoding="utf-8", errors="ignore").read()
print("LOGO candidates:")
for m in re.findall(r'<img[^>]+src="([^"]+)"[^>]*>', home)[:40]:
    if re.search(r"logo|anglia|brand", m, re.I): print("  ", m)
print("\nCUSTOM LOGO / site icon:", re.findall(r'(?:custom-logo[^>]+src|rel="icon"[^>]+href)="([^"]+)"', home)[:4])
cols = collections.Counter(re.findall(r"--e-global-color-(\w+):\s*(#[0-9A-Fa-f]{3,8})", home))
print("\nELEMENTOR GLOBAL COLORS:", dict(cols))
allhex = collections.Counter(c.upper() for f in os.listdir(C) for c in re.findall(r"#[0-9A-Fa-f]{6}\b", open(os.path.join(C, f), encoding="utf-8", errors="ignore").read()))
print("MOST USED COLORS:", allhex.most_common(12))
inv = json.load(open(r"C:\Users\belko\AGI\data\crawl\inventory.json", encoding="utf-8"))
for part, n in [("angliamorocco.org/step-to-books/", 1600), ("step-to-books-2", 700), ("angliamorocco.org/exams/", 4200)]:
    p = next((x for x in inv if part in x["url"]), None)
    if p: print(f"\n######## {p['title']} ({p['words']}w)\n{p['text'][:n]}")
raw = open(os.path.join(C, "practice-resources.html"), encoding="utf-8", errors="ignore").read()
heads = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", raw, re.S)
print("\nPRACTICE headings:", [re.sub(r"<[^>]+>", "", h).strip() for h in heads][:20])
links = re.findall(r'<a[^>]+href="(https?://[^"]+\.(?:zip|pdf|mp3))"[^>]*>(.*?)</a>', raw, re.S)
print("PRACTICE links:", len(links), "e.g.", [(u.split("/")[-1], re.sub(r"<[^>]+>|\s+", " ", t).strip()) for u, t in links[-12:]])
