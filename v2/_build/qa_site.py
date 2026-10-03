"""Site QA: facts, structure, organization, buttons/links, design drift.  python _build/qa_site.py -> docs/qa-site.csv + summary"""
import os, re, json, html, csv
from collections import defaultdict, Counter
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
files = [f for f in sorted(os.listdir(V2)) if f.endswith(".html")] + [f"{d}/{f}" for d in ("fr", "ar", "journal") if os.path.isdir(os.path.join(V2, d)) for f in sorted(os.listdir(os.path.join(V2, d))) if f.endswith(".html")]
SRC = {f: open(os.path.join(V2, f), encoding="utf-8").read() for f in files}
rows = []
def flag(page, area, issue, detail=""): rows.append((page, area, issue, detail[:180]))
def main_of(s):
    m = re.search(r"<main\b.*?</main>", s, re.S); return m.group(0) if m else ""
# ---------- 1. facts: contacts & key dates
PHONES = {"528843349": "+212 528 843 349", "618639911": "+212 618 639 911 (Arabic)", "688739393": "WhatsApp +212 688 739 393"}
for f, s in SRC.items():
    if f.startswith("journal/"): continue
    t = html.unescape(re.sub(r"<[^>]+>", " ", main_of(s)))
    for raw in re.findall(r"(?:\+?212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}", t):
        d = re.sub(r"\D", "", raw)[-9:]
        if d not in PHONES and d != "612345678": flag(f, "facts", "Unknown phone number", raw)
    for e in set(re.findall(r"[\w.+-]+@[\w-]+\.[a-z]{2,}", t.lower())):
        if e not in {"americanecoleagadir@gmail.com", "j.wilburn@angliamorocco.org", "a.lam@angliamorocco.org", "name@example.com"}: flag(f, "facts", "Email outside the official list", e)
    for m in re.finditer(r"(?i)registration days?[^.]{0,40}?(August|Aug\.?)\s*(\d{1,2})(?:\s*(?:&|and)\s*(\d{1,2}))?", t):
        if (m.group(2), m.group(3)) not in (("28", "31"), ("28", None)): flag(f, "facts", "Registration days differ from Aug 28 & 31", m.group(0))
    for m in re.finditer(r"(?i)first day[^.]{0,30}?(September|Sept\.?)\s*(\d{1,2})", t):
        if m.group(2) not in ("7",) and "2025" not in t[max(0, m.start() - 80):m.end() + 20] and "2027" not in t[m.start():m.end() + 40]: flag(f, "facts", "First day differs from Sept 7", m.group(0))
    for m in re.finditer(r"(?i)(?:tuition|monthly)[^.]{0,40}?(\d[\d,. ]{2,6})\s?(?:MAD|DH|dirhams|درهم)", t):
        if re.sub(r"\D", "", m.group(1)) not in ("2600",): flag(f, "facts", "Tuition amount differs from 2,600 MAD", m.group(0))
# ---------- 2. structure signature
sig = {}
for f, s in SRC.items():
    m = main_of(s)
    sig[f] = {"hero": "home-hero" if "home-hero" in m else ("story-hero" if "story-hero" in m else ("page-hero" if "page-hero" in m else "none")),
              "crumb": bool(re.search(r'class="crumb"', m)), "h1": len(re.findall(r"<h1\b", m)), "cta": "cta-band" in m, "aside": "<aside" in m,
              "sections": len(re.findall(r"<section\b", m)), "inline_styles": len(re.findall(r'style="', m))}
    if f.startswith(("journal/",)): continue
    if f != "index.html" and sig[f]["hero"] == "none": flag(f, "structure", "No page hero", "")
    if f not in ("index.html",) and not f.endswith("/index.html") and not sig[f]["crumb"]: flag(f, "structure", "No breadcrumb", "")
    if sig[f]["h1"] != 1: flag(f, "structure", f"{sig[f]['h1']} h1 headings", "")
    if not sig[f]["cta"] and not f.startswith(("fr/", "ar/")) and f not in ("forms.html", "privacy.html", "terms.html", "cookies.html", "connect.html", "journal.html"): flag(f, "structure", "No closing call to action", "")
    if sig[f]["sections"] <= 1 and f not in ("connect.html",): flag(f, "structure", "Thin layout (one section)", "")
    if sig[f]["inline_styles"] > 25: flag(f, "design", "Many inline styles (design drift)", f"{sig[f]['inline_styles']} style attributes")
# ---------- 3. organization: inbound links, breadcrumb vs menu
inbound = Counter()
for f, s in SRC.items():
    base = os.path.dirname(f)
    for h in set(re.findall(r'href="([^"#?]+\.html)', s)):
        if h.startswith("http"): continue
        tgt = os.path.normpath(os.path.join(base, h)).replace(os.sep, "/")
        if tgt != f: inbound[tgt] += 1
nav_links = set(re.findall(r'href="([^"#]+\.html)', SRC["index.html"].split("<!--site:header-->")[1].split("<!--/site:header-->")[0])) | set(re.findall(r'href="([^"#]+\.html)', SRC["index.html"].split("<!--site:footer-->")[1].split("<!--/site:footer-->")[0]))
for f in files:
    if f.startswith("journal/") or f in ("index.html",): continue
    body_links = sum(1 for g, s in SRC.items() if g != f and re.search(rf'href="(?:\.\./|\./)?{re.escape(os.path.basename(f))}[#"]', main_of(s)) and (os.path.dirname(g) == os.path.dirname(f) or "../" in s))
    if inbound[f] == 0: flag(f, "organization", "Orphan page (no link to it)", "")
    elif f not in nav_links and not f.startswith(("fr/", "ar/")) and body_links < 2: flag(f, "organization", "Hard to find (not in menu/footer, linked from < 2 pages)", f"{inbound[f]} inbound links")
# ---------- 4. buttons & links
forms_js = SRC.get("forms.html", "")
form_ids = set(re.findall(r'id:\s*"([a-z-]+)"', forms_js))
topics = set(re.findall(r'"(programs|anglia|partnership|careers|press|other|admissions|fees)"', forms_js))
for f, s in SRC.items():
    m = main_of(s)
    for a, href, label in re.findall(r'(<a\b[^>]*href="([^"]*)"[^>]*>)(.*?)</a>', m, re.S):
        lab = re.sub(r"<[^>]+>", "", label).strip()
        if "btn" in a and not lab: flag(f, "links", "Button without text", href)
        mm = re.match(r"(?:\.\./)?forms\.html#([a-z-]+)(?:/([a-z-]+))?", href)
        if mm and form_ids and mm.group(1) not in form_ids and mm.group(1) != "start": flag(f, "links", "Button opens an unknown form", href)
        if href.startswith("tel:") and not re.fullmatch(r"tel:\+212\d{9}", href): flag(f, "links", "Phone link not in +212 format", href)
        if "wa.me/" in href and not re.search(r"wa\.me/212688739393", href): flag(f, "links", "WhatsApp link to another number", href)
        if re.fullmatch(r"(?i)(click here|here|read more|more|link)", lab): flag(f, "links", "Vague link text", f"{lab} -> {href}")
        if href.startswith("http") and "target=\"_blank\"" in a and "noopener" not in a: flag(f, "links", "External link without rel=noopener", href)
# ---------- 6. design drift: colors and fonts hard-coded in pages
for f, s in SRC.items():
    m = main_of(s)
    cols = set(c.lower() for c in re.findall(r"#[0-9a-fA-F]{6}\b", m)) - {"#ffffff", "#000000", "#0a3161", "#b22234", "#c9a227", "#061529", "#f6f5f1", "#fff8e1"}
    if cols and not f.startswith("journal/"): flag(f, "design", "Hard-coded colors outside the palette", ", ".join(sorted(cols))[:80])
with open(os.path.join(ROOT, "docs", "qa-site.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["page", "area", "issue", "detail"]); w.writerows(rows)
json.dump(sig, open(os.path.join(ROOT, "data", "qa-structure.json"), "w"), indent=1)
by = Counter((r[1], r[2]) for r in rows)
print(f"pages: {len(files)} · findings: {len(rows)} · pages flagged: {len({r[0] for r in rows})}")
for (a, i), n in sorted(by.items()): print(f"  {a:12} {n:4}  {i}")
print("\nexamples:")
seen = Counter()
for r in rows:
    if seen[r[2]] < 3: seen[r[2]] += 1; print(f"  [{r[1]}] {r[0]}: {r[2]} {('– ' + r[3]) if r[3] else ''}")
