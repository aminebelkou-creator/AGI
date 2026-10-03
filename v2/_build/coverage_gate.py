"""Coverage gate: every fact from every mapped source page must appear on its destination page,
or be listed in docs/content-exclusions.csv with a reason.
  python _build/coverage_gate.py            -> report all phases
  python _build/coverage_gate.py --phase 1  -> exit 1 unless phase 1 passes (use before calling a phase done)"""
import os, re, json, csv, sys, html
from collections import defaultdict
ROOT = r"C:\Users\belko\AGI"; V2 = os.path.join(ROOT, "v2")
inv = {p["url"]: p for p in json.load(open(os.path.join(ROOT, "data", "crawl", "inventory.json"), encoding="utf-8"))}
rows = list(csv.DictReader(open(os.path.join(ROOT, "docs", "content-map.csv"), encoding="utf-8-sig")))
exc_path = os.path.join(ROOT, "docs", "content-exclusions.csv")
if not os.path.exists(exc_path):
    with open(exc_path, "w", encoding="utf-8-sig", newline="") as fh: csv.writer(fh).writerow(["source_url", "fact", "reason"])
EXC = {(r["source_url"], r["fact"]) for r in csv.DictReader(open(exc_path, encoding="utf-8-sig"))}
def norm(s): return " " + re.sub(r"[^a-z0-9\u0600-\u06ff]+", " ", s.lower()).strip() + " "
_cache = {}
def site_all():
    if "__all__" in _cache: return _cache["__all__"]
    ws, ds = [], []
    for dp, _, fs in os.walk(V2):
        if "_build" in dp or "_legacy" in dp: continue
        for f in fs:
            if f.endswith(".html"):
                t = page_text(os.path.relpath(os.path.join(dp, f), V2).replace(os.sep, "/"))
                if t: ws.append(t[0]); ds.append(t[1])
    _cache["__all__"] = (" ".join(ws), "".join(ds)); return _cache["__all__"]
def page_text(dest):
    if dest in _cache: return _cache[dest]
    p = os.path.join(V2, dest.replace("/", os.sep))
    if dest.endswith("/"): p = os.path.join(p, "index.html")
    if not os.path.exists(p): _cache[dest] = None; return None
    s = open(p, encoding="utf-8").read()
    s = re.sub(r"<!--site:(header|footer|seo)-->.*?<!--/site:\1-->", " ", s, flags=re.S)
    s = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S)))
    _cache[dest] = (norm(s), re.sub(r"\D", "", s)); return _cache[dest]
def present(kind, val, t):
    words, digits = t
    if kind == "phone": return val in digits
    if kind == "money":   # compare the number; accept MAD/DH/dirhams as the same currency
        n = re.sub(r"[^\d]", "", val)
        return bool(n) and (norm(val) in words or norm(re.sub(r"[^\d.,]", "", val)) in words or f" {n} " in words or f" {int(n):,} ".replace(",", " ") in words)
    return norm(val) in words
want = int(sys.argv[sys.argv.index("--phase") + 1]) if "--phase" in sys.argv else None
by_phase = defaultdict(lambda: {"sources": 0, "facts": 0, "ok": 0, "excluded": 0, "unbuilt": set(), "missing": []})
for r in rows:
    if r["action"] in ("drop",): continue
    ph = int(r["phase"]); s = by_phase[ph]; s["sources"] += 1
    src = inv.get(r["url"]); dest = r["destination"]
    if not src: continue
    facts = [(k, v) for k, vs in src["facts"].items() for v in vs]
    t = page_text(dest) if r["action"] != "translate" else None
    for k, v in facts:
        s["facts"] += 1
        if (r["url"], v) in EXC: s["excluded"] += 1; continue
        if t is None: s["unbuilt"].add(dest); continue
        if present(k, v, t): s["ok"] += 1
        elif present(k, v, site_all()): s["ok"] += 1; s.setdefault("elsewhere", []).append((dest, k, v))
        else: s["missing"].append((dest, k, v, r["url"]))
fail = False
print(f"{'phase':5} {'sources':>7} {'facts':>6} {'present':>8} {'excluded':>8} {'missing':>8} {'pages not built':>16}  result")
for ph in sorted(by_phase):
    s = by_phase[ph]; done = s["ok"] + s["excluded"]
    ok = not s["unbuilt"] and not s["missing"]
    print(f"{ph:5} {s['sources']:7} {s['facts']:6} {s['ok']:8} {s['excluded']:8} {len(s['missing']):8} {len(s['unbuilt']):16}  {'PASS' if ok else 'FAIL'}")
    if want is not None and ph == want: fail = not ok
if want is not None:
    s = by_phase[want]
    print(f"\nPhase {want}: pages not built: {sorted(s['unbuilt'])}")
    print(f"Facts found on another page than their destination: {len(s.get('elsewhere', []))}")
    by_dest = defaultdict(list)
    for d, k, v, u in s["missing"]: by_dest[d].append(f"{k}: {v}")
    for d, L in sorted(by_dest.items()): print(f"  {d}: {len(L)} missing – " + " | ".join(L[:10]))
    sys.exit(1 if fail else 0)
