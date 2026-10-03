"""External link check: every outside link on the site, tested.  python _build/ext_linkcheck.py -> docs/external-links.csv"""
import os, re, csv, html, json, urllib.request, urllib.error, ssl, concurrent.futures as cf
from collections import defaultdict
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
SKIP = ("fonts.googleapis.com", "fonts.gstatic.com", "schema.org", "openapi.vercel.sh", "www.w3.org", "agi-preview.vercel.app", "wa.me", "maps.google", "google.com/maps", "www.google.com/maps")
files = [f for f in sorted(os.listdir(V2)) if f.endswith(".html")] + [f"{d}/{f}" for d in ("fr", "ar", "journal") if os.path.isdir(os.path.join(V2, d)) for f in sorted(os.listdir(os.path.join(V2, d))) if f.endswith(".html")]
where = defaultdict(set)
for f in files:
    s = open(os.path.join(V2, f), encoding="utf-8").read()
    s = re.sub(r"<!--site:seo-->.*?<!--/site:seo-->", " ", s, flags=re.S)
    for u in re.findall(r'(?:href|src)="(https?://[^"#]+)', s):
        u = html.unescape(u)
        if not any(k in u for k in SKIP): where[u].add(f)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36", "Accept": "*/*"}
CTX = ssl.create_default_context()
def check(u):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(u, headers=UA, method=method)
            with urllib.request.urlopen(req, timeout=20, context=CTX) as r: return (r.status, r.geturl())
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 400, 501): continue
            return (e.code, "")
        except Exception as e:
            if method == "HEAD": continue
            return ("error", type(e).__name__ + ": " + str(e)[:80])
    return ("error", "no response")
res = {}
with cf.ThreadPoolExecutor(12) as ex:
    for u, r in zip(where, ex.map(check, list(where))): res[u] = r
rows = []
for u, (st, final) in sorted(res.items(), key=lambda x: str(x[1][0])):
    old = "americangroup-international.com" in u
    ok = isinstance(st, int) and st < 400
    status = ("OLD SITE – will break after migration" if old and ok else ("OK" if ok else "BROKEN"))
    rows.append((status, st, u, final if final and final != u else "", len(where[u]), " ".join(sorted(where[u])[:6])))
with open(os.path.join(ROOT, "docs", "external-links.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["status", "http", "url", "redirects_to", "pages", "used_on"]); w.writerows(rows)
from collections import Counter
c = Counter(r[0] for r in rows)
print(f"external links: {len(rows)} unique · " + " · ".join(f"{k}: {n}" for k, n in c.items()))
for r in rows:
    if r[0] != "OK": print(f"  [{r[0][:12]}] {r[1]}  {r[2][:95]}  ({r[4]} page(s): {r[5][:60]})")

# remember dead links permanently (pages exclude them even after they disappear from this report)
_dj = os.path.join(V2, '_build', 'dead-links.json')
_known = set(json.load(open(_dj, encoding='utf-8-sig'))) if os.path.exists(_dj) else set()
json.dump(sorted(_known | {r[2] for r in rows if r[0] == 'BROKEN'}), open(_dj, 'w', encoding='utf-8'), indent=1)
