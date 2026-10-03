"""Coverage audit: which facts from the old WordPress site are missing from v2."""
import os, re, json, html, csv
ROOT = r"C:\Users\belko\AGI"; V2 = os.path.join(ROOT, "v2")
d = json.load(open(os.path.join(ROOT, "data", "export", "AGI_Website_Content_Export.json"), encoding="utf-8"))
def strip(s):
    s = re.sub(r"<!--site:(header|footer|seo)-->.*?<!--/site:\1-->", " ", s, flags=re.S)
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s)))
site = " ".join(strip(open(os.path.join(dp, f), encoding="utf-8").read()) for dp, _, fs in os.walk(V2)
                if "_build" not in dp and "_legacy" not in dp for f in fs if f.endswith(".html")).lower()
site_n = re.sub(r"[^a-z0-9]+", " ", site)
redir = {r["old_address"].rstrip("/"): r["new_page"] for r in csv.DictReader(open(os.path.join(V2, "_build", "redirects.csv"), encoding="utf-8"))}
STOP = set("the and for with from that this your you our are was were will have has not but all can any its into more than then them they their there these those when what which who how also about other some such only very most many much each per may must should would could been being over under after before between during within without upon".split())
def facts(md):
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", md); md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    out = set()
    for m in re.finditer(r"\b\d[\d,.]*\s?(?:MAD|DH|Dhs?|dirhams?|euros?|EUR|€|\$|USD|hours?|weeks?|days?|months?|years?|%|credits?|students?)\b|\$\s?\d[\d,.]*", md, re.I): out.add(("num", m.group(0).strip()))
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.]+", md): out.add(("email", m.group(0)))
    for m in re.finditer(r"(?:\+?212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}", md): out.add(("phone", re.sub(r"\D", "", m.group(0))[-9:]))
    for m in re.finditer(r"\b(?:[A-Z][a-zA-Z&'.-]+(?:\s+(?:of|and|&|de|for|the)\s+|\s+)){1,4}[A-Z][a-zA-Z&'.-]+\b", md):
        t = m.group(0).strip()
        if len(t) > 6 and not t.split()[0].lower() in STOP: out.add(("name", t))
    return out
def present(kind, val):
    if kind == "phone": return val in re.sub(r"\D", "", site)
    if kind == "num":
        n = re.sub(r"[^0-9]", "", val)
        return bool(n) and re.search(r"(?<!\d)" + re.escape(re.sub(r"\B(?=(\d{3})+(?!\d))", ",", n) if len(n) > 3 else n) + r"(?!\d)", site) is not None or (n in re.sub(r"[^0-9 ]", " ", site).split())
    v = re.sub(r"[^a-z0-9]+", " ", val.lower()).strip()
    return v in site_n
rows = []
for p in d["pages"]:
    F = facts(p.get("markdown", ""))
    if not F: rows.append((p["title"].strip(), p.get("route", ""), 1.0, 0, [])); continue
    miss = sorted(v for k, v in F if not present(k, v))
    rows.append((p["title"].strip(), p.get("route", ""), 1 - len(miss) / len(F), len(F), miss))
rows.sort(key=lambda r: r[2])
print(f"old pages: {len(rows)}   site text words: {len(site.split())}")
print("\n=== coverage by old page (lowest first) ===")
for t, route, cov, n, miss in rows:
    flag = "MISSING " if cov < 0.35 else ("PARTIAL " if cov < 0.7 else "ok      ")
    print(f"{flag}{cov:4.0%} ({n:3} facts) {t[:58]:58} -> {redir.get(route.rstrip('/'), '?')}")
    if cov < 0.7 and miss: print("          missing e.g.: " + " | ".join(miss[:9]))
