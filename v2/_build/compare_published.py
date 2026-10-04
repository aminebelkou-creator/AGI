"""Compare pages published by a CMS (e.g. Sitewright) with our original pages – nothing may be lost.
python _build/compare_published.py <published-folder> [page.html ...]
Checks per page: visible text kept (sentence coverage), facts (MAD/DH amounts, dates, phones, emails), links & buttons,
placeholders (data-placeholder / data-verify), language + direction (lang/dir), headings. Writes docs/poc-fidelity.csv."""
import os, re, sys, html, csv
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
if len(sys.argv) < 2: sys.exit(__doc__)
PUB = sys.argv[1]; PAGES = sys.argv[2:] or ["index.html", "fees.html", "ar/index.html"]
def main(s):
    m = re.search(r"<main\b.*?</main>", s, re.S) or re.search(r"<body\b.*?</body>", s, re.S)
    return m.group(0) if m else s
def text(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style|svg)\b.*?</\1>", " ", s, flags=re.S)))).strip()
def sents(t): return {re.sub(r"\W+", " ", x.lower()).strip() for x in re.split(r"(?<=[.!?؟])\s+", t) if len(x) > 30}
FACT = r"\d[\d,. ]{1,8}\s?(?:MAD|DH|درهم|US\$)|(?:\+212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}|[\w.+-]+@[\w-]+\.[a-z]{2,}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}"
def facts(t): return {re.sub(r"\s+", " ", f.strip()) for f in re.findall(FACT, t)}
def links(s): return {re.sub(r"^(\.\./|\./|/)", "", h).split("?")[0] for h in re.findall(r'href="([^"#][^"]*)"', s) if not h.startswith(("http", "mailto:", "tel:", "javascript"))}
def find_pub(p):
    for c in (os.path.join(PUB, p), os.path.join(PUB, p.replace(".html", ""), "index.html"), os.path.join(PUB, p.replace("index.html", "").rstrip("/"), "index.html")):
        if os.path.isfile(c): return c
rows, ok_all = [], True
print(f"{'page':24} {'text':>6} {'facts':>9} {'links':>9} {'markers':>9} {'lang/dir':>12} {'h1':>4}  verdict")
for p in PAGES:
    o = open(os.path.join(V2, p), encoding="utf-8").read(); fp = find_pub(p)
    if not fp: print(f"{p:24} not found in the published folder"); ok_all = False; rows.append((p, "missing", "", "", "", "", "")); continue
    n = open(fp, encoding="utf-8").read(); om, nm = main(o), main(n); ot, nt = text(om), text(nm)
    S, Sn = sents(ot), sents(nt); cov = len(S & Sn) / len(S) if S else 1
    F, Fn = facts(ot), facts(nt); fmiss = F - Fn
    L, Ln = links(om), links(nm); lmiss = {x for x in L - Ln if not x.startswith("assets/")}
    M = set(re.findall(r'data-(?:placeholder|verify)="([^"]+)"', om)); Mn = set(re.findall(r'data-(?:placeholder|verify)="([^"]+)"', nm)); mmiss = M - Mn
    olang = re.search(r'<html[^>]*lang="([^"]+)"', o); odir = re.search(r'<html[^>]*dir="([^"]+)"', o)
    nlang = re.search(r'lang="([^"]+)"', n); ndir = "rtl" if re.search(r'dir="rtl"', n) else "ltr"
    want_dir = odir.group(1) if odir else "ltr"
    langdir_ok = (nlang and olang and nlang.group(1).startswith(olang.group(1)[:2])) and ndir == want_dir
    h1 = len(re.findall(r"<h1\b", nm))
    good = cov >= 0.95 and not fmiss and not mmiss and len(lmiss) <= 2 and langdir_ok and h1 == 1
    ok_all &= good
    print(f"{p:24} {cov:6.0%} {len(F) - len(fmiss):>4}/{len(F):<4} {len(L) - len(lmiss):>4}/{len(L):<4} {len(M) - len(mmiss):>4}/{len(M):<4} {('ok ' if langdir_ok else 'NO ') + ndir:>12} {h1:>4}  {'PASS' if good else 'FAIL'}")
    for kind, miss in (("missing fact", fmiss), ("missing link", lmiss), ("missing marker", mmiss)):
        for x in sorted(miss)[:8]: print(f"      {kind}: {x}")
    rows.append((p, f"{cov:.0%}", ";".join(sorted(fmiss)), ";".join(sorted(lmiss)), ";".join(sorted(mmiss)), ndir, "PASS" if good else "FAIL"))
with open(os.path.join(ROOT, "docs", "poc-fidelity.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["page", "text_coverage", "missing_facts", "missing_links", "missing_markers", "direction", "verdict"]); w.writerows(rows)
print("\n" + ("ALL PAGES FAITHFUL" if ok_all else "DIFFERENCES FOUND – see above and docs/poc-fidelity.csv"))
sys.exit(0 if ok_all else 1)
