import os, re, html
from urllib.parse import unquote
V2 = r"C:\Users\belko\AGI\v2"
files = [os.path.join(dp, f) for dp, _, fs in os.walk(V2) if "_legacy" not in dp and "_build" not in dp for f in fs if f.endswith(".html")]
ids = {}
for f in files:
    ids[os.path.normpath(f)] = set(re.findall(r'\sid="([^"]+)"', open(f, encoding="utf-8").read()))
import re as _re
FORM_IDS = {"start", "transcript"} | set(_re.findall(r'id:\s*"([a-z-]+)"', open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "forms.html"), encoding="utf-8").read()))   # read from forms.html
broken, checked = [], 0
for f in files:
    s = open(f, encoding="utf-8").read()
    for attr, url in re.findall(r'\s(href|src)="([^"]+)"', s):
        url = html.unescape(url)
        if re.match(r"(https?:|mailto:|tel:|data:|javascript:)", url): continue
        checked += 1
        path, _, frag = url.partition("#")
        target = os.path.normpath(os.path.join(os.path.dirname(f), unquote(path))) if path else os.path.normpath(f)
        if not os.path.exists(target):
            broken.append((os.path.relpath(f, V2), url, "missing file")); continue
        if frag and target.endswith(".html"):
            anchor = frag.split("/")[0]
            if target.endswith("forms.html"):
                if anchor not in FORM_IDS: broken.append((os.path.relpath(f, V2), url, "unknown form"))
            elif anchor and anchor not in ids.get(target, set()):
                broken.append((os.path.relpath(f, V2), url, "missing anchor"))
print(f"pages: {len(files)}  internal links/images checked: {checked}  broken: {len(broken)}")
seen = set()
for b in broken:
    if (b[1], b[2]) in seen: continue
    seen.add((b[1], b[2])); print("  ", b)
