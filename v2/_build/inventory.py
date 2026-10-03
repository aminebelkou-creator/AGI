"""Content inventory of both source sites (americangroup-international.com + angliamorocco.org).
Reads data/crawl/{agi,anglia}/*.html, writes data/crawl/inventory.json and docs/content-inventory.csv."""
import os, re, json, html, csv
from collections import Counter, defaultdict
ROOT = r"C:\Users\belko\AGI"; CRAWL = os.path.join(ROOT, "data", "crawl"); V2 = os.path.join(ROOT, "v2")

def clean_html(s):
    s = re.sub(r"<(script|style|noscript|svg|iframe|form)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    # drop site chrome: header/footer/nav and Elementor header/footer templates, cookie banners, sidebars
    s = re.sub(r"<(header|footer|nav|aside)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r'<div[^>]+(elementor-location-(header|footer)|cookie|cmplz|sidebar|widget-area)[^>]*>.*?(?=<div[^>]+elementor-location-|$)', " ", s, flags=re.S | re.I)
    return s
def to_text(s):
    s = re.sub(r"<br\s*/?>|</(p|h[1-6]|li|tr|div|td|th|section)>", "\n", s, flags=re.I)
    s = re.sub(r"<h([1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "\n- ", s, flags=re.I)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    lines, seen = [], set()
    for l in (re.sub(r"[ \t\u00a0]+", " ", x).strip() for x in s.split("\n")):
        if l and l not in seen and not re.fullmatch(r"[-#\s|]*", l): seen.add(l); lines.append(l)
    return "\n".join(lines)

CATS = [  # (category, regex on url+title+first text)
 ("legal", r"privacy|terms|conditions|cookie"),
 ("form", r"form\b|forms|apply|applyform|request|book-an-appointment|appointment|register|inscription-form|order"),
 ("calendar", r"calendar|schedule|dates|last-day|holiday"),
 ("fees", r"fee|pricing|price|tuition|cost"),
 ("policy", r"policy|policies|procedure|handbook|responsibility|attendance|promotion|retention|media|volunteer|homework|supplies"),
 ("admissions", r"admission|enrol|enroll|placement"),
 ("exam", r"exam|test|testing|cite|c-i-t-e|level|cefr|benchmark|results|certificate"),
 ("teacher", r"teacher|tesol|tefl|educator|sponsorship|internship|training"),
 ("program", r"program|course|class|school|diploma|degree|pods|learning|efl|esl|english|math|special-education|k-12|kindergarten"),
 ("service", r"service|consult|proctor|coaching|therapy|editing|tutor|agent|attestation"),
 ("partner", r"partner|network|franchise|center|centre|region|college|university|chichester|ccg|leverage|bridge"),
 ("resource", r"rhymes|mcguffey|self-help|helps|grammar|resources|practice|tips|how-long|instructions|zoom|teams|sight"),
 ("about", r"about|vision|mission|team|who-we|history|director|ceo|contact|faq"),
]
def classify(url, title, kind):
    if kind == "post": return "news/event"
    hay = (url + " " + title).lower()
    for c, rx in CATS:
        if re.search(rx, hay): return c
    return "other"

def facts(t):
    f = defaultdict(set)
    for m in re.finditer(r"\d[\d,. ]*\s?(?:MAD|DH|DHS|Dhs|dirhams?|€|EUR|euros?|USD|\$)|\$\s?\d[\d,.]*", t): f["money"].add(m.group(0).strip())
    for m in re.finditer(r"\b(?:\d{1,2}(?:st|nd|rd|th)?\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:,?\s*\d{4})?|\b\d{1,2}/\d{1,2}/\d{2,4}\b", t): f["date"].add(m.group(0).strip())
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.]+", t): f["email"].add(m.group(0).lower())
    for m in re.finditer(r"(?:\+?212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}", t): f["phone"].add(re.sub(r"\D", "", m.group(0))[-9:])
    for m in re.finditer(r"\b\d+\s?(?:hours?|weeks?|months?|years?|days?|students?|levels?|regions?|nationalities|%)", t, re.I): f["number"].add(m.group(0))
    return {k: sorted(v) for k, v in f.items()}

def site_text():
    out = []
    for dp, _, fs in os.walk(V2):
        if "_build" in dp or "_legacy" in dp: continue
        for f in fs:
            if f.endswith(".html"):
                s = open(os.path.join(dp, f), encoding="utf-8").read()
                s = re.sub(r"<!--site:(header|footer|seo)-->.*?<!--/site:\1-->", " ", s, flags=re.S)
                out.append(to_text(re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S)))
    return re.sub(r"[^a-z0-9]+", " ", " ".join(out).lower())
SITE = site_text(); SITE_DIGITS = re.sub(r"\D", "", SITE)
def covered(kind, v):
    if kind == "phone": return v in SITE_DIGITS
    n = re.sub(r"[^a-z0-9]+", " ", v.lower()).strip()
    return n in SITE
def sentences(t):  # distinctive sentences for coverage
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", t) if 60 <= len(s.strip()) <= 400]
def sent_cov(t):
    ss = sentences(t)
    if not ss: return None
    hit = 0
    for s in ss:
        words = [w for w in re.sub(r"[^a-z0-9 ]+", " ", s.lower()).split() if len(w) > 3]
        key = [w for w in words if w not in ("with", "that", "this", "from", "have", "your", "their", "will", "which", "also", "they", "were", "been", "more")]
        if key and sum(1 for w in key if f" {w} " in f" {SITE} ") / len(key) >= 0.75: hit += 1
    return hit / len(ss)

items = []
for site in ("agi", "anglia"):
    d = os.path.join(CRAWL, site)
    if not os.path.isdir(d): continue
    for fn in sorted(os.listdir(d)):
        raw = open(os.path.join(d, fn), encoding="utf-8", errors="ignore").read()
        url = re.search(r"<!-- source: (\S+) -->", raw).group(1)
        title = html.unescape(re.sub(r"\s+", " ", (re.search(r"<title>(.*?)</title>", raw, re.S) or [None, ""])[1])).split(" - ")[0].split(" – ")[0].strip()
        body_cls = (re.search(r'<body[^>]*class="([^"]*)"', raw) or [None, ""])[1]
        kind = "post" if re.search(r"\bpostid-\d+", body_cls) else ("page" if re.search(r"\bpage-id-\d+|\bhome\b", body_cls) else ("archive" if re.search(r"archive|blog|category", body_cls) else "page"))
        lang = "ar" if re.search(r"/ar/|lang=\"ar", url + raw[:600]) else ("fr" if "/fr/" in url else "en")
        date = (re.search(r'article:published_time" content="([^"]+)"', raw) or [None, ""])[1][:10]
        text = to_text(clean_html(raw))
        words = len(text.split())
        fx = facts(text)
        nfx = sum(len(v) for v in fx.values()); miss = [f"{k}: {v}" for k, vs in fx.items() for v in vs if not covered(k, v)]
        sc = sent_cov(text)
        items.append({"site": site, "url": url, "title": title, "kind": kind, "lang": lang, "date": date, "category": classify(url, title, kind),
                      "words": words, "thin": words < 150, "facts": fx, "facts_missing": miss,
                      "fact_coverage": None if not nfx else round(1 - len(miss) / nfx, 2), "text_coverage": None if sc is None else round(sc, 2), "text": text})
json.dump(items, open(os.path.join(CRAWL, "inventory.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def status(it):
    tc = it["text_coverage"]; fc = it["fact_coverage"]
    score = min(x for x in (tc, fc) if x is not None) if (tc is not None or fc is not None) else 1
    return "covered" if score >= 0.7 else ("partial" if score >= 0.3 else "missing")
with open(os.path.join(ROOT, "docs", "content-inventory.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["site", "language", "kind", "category", "title", "url", "date", "words", "thin", "text_coverage", "fact_coverage", "status", "missing_facts_examples"])
    for it in sorted(items, key=lambda x: (x["site"], x["category"], x["title"])):
        w.writerow([it["site"], it["lang"], it["kind"], it["category"], it["title"], it["url"], it["date"], it["words"], "yes" if it["thin"] else "",
                    it["text_coverage"], it["fact_coverage"], status(it), " | ".join(it["facts_missing"][:8])])
# ---- summary
for site in ("agi", "anglia"):
    S = [i for i in items if i["site"] == site]
    if not S: continue
    print(f"\n===== {site}: {len(S)} pages · {sum(i['words'] for i in S):,} words · languages {dict(Counter(i['lang'] for i in S))} · kinds {dict(Counter(i['kind'] for i in S))}")
    print("  by category:", dict(Counter(i["category"] for i in S).most_common()))
    print("  status:", dict(Counter(status(i) for i in S)))
    print("  thin pages (<150 words):", sum(1 for i in S if i["thin"]))
    for st in ("missing", "partial"):
        L = sorted([i for i in S if status(i) == st and i["kind"] != "archive"], key=lambda i: (i["category"], -i["words"]))
        print(f"  --- {st.upper()} ({len(L)}):")
        for i in L[:70]: print(f"     [{i['category']:10}] {i['words']:5}w  {i['title'][:62]}")
