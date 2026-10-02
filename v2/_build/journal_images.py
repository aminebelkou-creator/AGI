"""Download the journal's images from the old WordPress site into assets/journal/ and record the mapping."""
import os, re, json, hashlib, urllib.request, concurrent.futures as cf
from urllib.parse import urlparse, unquote
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT = json.load(open(os.path.join(os.path.dirname(V2), "data", "export", "AGI_Website_Content_Export.json"), encoding="utf-8"))
OUT = os.path.join(V2, "assets", "journal"); os.makedirs(OUT, exist_ok=True)
MAP_FILE = os.path.join(V2, "_build", "journal-images.json")
mapping = json.load(open(MAP_FILE, encoding="utf-8")) if os.path.exists(MAP_FILE) else {}
urls = set()
for n in EXPORT["news"]:
    urls.update(re.findall(r"!\[[^\]]*\]\((https?://[^)\s]+)", n.get("markdown", "")))
    if n.get("image"): urls.add(n["image"])
urls = {u for u in urls if "americangroup-international.com" in u}
def name_for(u):
    base = os.path.basename(unquote(urlparse(u).path)) or "image"
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", base)[-80:]
    return hashlib.md5(u.encode()).hexdigest()[:6] + "-" + base
def fetch(u):
    if u in mapping and os.path.exists(os.path.join(V2, mapping[u])): return u, mapping[u], "cached"
    fn = name_for(u); dest = os.path.join(OUT, fn)
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (AGI site migration)"})
        with urllib.request.urlopen(req, timeout=30) as r: data = r.read()
        open(dest, "wb").write(data); return u, "assets/journal/" + fn, f"{len(data)//1024} KB"
    except Exception as e:
        return u, None, f"FAILED {e}"
ok = fail = 0; total = 0
with cf.ThreadPoolExecutor(8) as ex:
    for u, local, info in ex.map(fetch, sorted(urls)):
        if local: mapping[u] = local; ok += 1
        else: fail += 1; print("  ", info, u)
json.dump(mapping, open(MAP_FILE, "w", encoding="utf-8"), indent=1)
size = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
print(f"journal images: {len(urls)} found, {ok} saved, {fail} failed; folder size {size//1024//1024} MB")
