"""Content inventory of both source sites, with boilerplate removed.
Reads data/crawl/{agi,anglia}/*.html -> data/crawl/inventory.json + docs/content-inventory.csv
Boilerplate = any line that appears on more than 25% of a site's pages (menus, sidebars, footers, cookie text)."""
import os, re, json, html, csv
from collections import Counter, defaultdict
ROOT = r"C:\Users\belko\AGI"; CRAWL = os.path.join(ROOT, "data", "crawl"); V2 = os.path.join(ROOT, "v2")

def strip_chrome(s):
    s = re.sub(r"<(script|style|noscript|svg|iframe|form|template)\b.*?</\1>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    return re.sub(r"<(header|footer|nav|aside)\b.*?</\1>", " ", s, flags=re.S | re.I)
def to_text(s):
    s = re.sub(r"<br\s*/?>|</(p|h[1-6]|li|tr|div|td|th|section|article)>", "\n", s, flags=re.I)
    s = re.sub(r"<h([1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "\n- ", s, flags=re.I)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s)).replace("\u200b", "")
    return [re.sub(r"[ \t\u00a0]+", " ", x).strip() for x in s.split("\n")]
def norm(l): return re.sub(r"[^a-z0-9\u0600-\u06ff]+", " ", l.lower()).strip()

FACT_RX = {
 "money": r"\d[\d,. ]*\s?(?:MAD|DH|DHS|Dhs|dirhams?|€|EUR|euros?|USD)\b|\$\s?\d[\d,.]*",
 "date": r"\b(?:\d{1,2}(?:st|nd|rd|th)?\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:,?\s*\d{4})?",
 "email": r"[\w.+-]+@[\w-]+\.[a-z]{2,}(?:\.[a-z]{2,})?",
 "phone": r"(?:\+?212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}",
 "number": r"\b\d+\s?(?:hours?|weeks?|months?|years?|days?|students?|levels?|regions?|nationalities|credits?|%)",
}
def facts(t):
    f = {}
    for k, rx in FACT_RX.items():
        vals = {re.sub(r"\s+", " ", m.group(0)).strip(" .,") for m in re.finditer(rx, t, re.I)}
        if k == "phone": vals = {re.sub(r"\D", "", v)[-9:] for v in vals}
        if k == "email": vals = {v.lower() for v in vals}
        if vals: f[k] = sorted(vals)
    return f

CATS = [("legal", r"privacy|terms|conditions|cookie"), ("form", r"\bforms?\b|applyform|request|appointment|order-form|book-order"),
 ("calendar", r"calendar|calandar|schedule|exam-dates|last-day"), ("fees", r"fee|pricing|price|tuition"),
 ("policy", r"policy|policies|procedure|handbook|responsibility|attendance|promotion|retention|volunteer|homework|supplies"),
 ("admissions", r"admission|enrol|enroll|placement|inscription"), ("exam", r"exam|test|testing|cite|c-i-t-e|cefr|benchmark|special-arrangements|ucas|mastery"),
 ("teacher", r"teacher|tesol|tefl|sponsorship|internship|training|database|stem"), ("wellbeing", r"adhd|therap|holistic|i-heart|counsel"),
 ("online", r"online|tutoring|zoom|teams|usa"), ("pathways", r"consult|university|agent|college|lane|leverage|chichester|ccg|bridge|network-of-partners"),
 ("partner", r"partner|network|franchise|center|centre|region|headquarters"),
 ("program", r"program|course|class|school|diploma|degree|pods|learning|efl|esl|english|math|special-education|k-12|kindergarten|editing|proctor|medical|corporate|business"),
 ("resource", r"rhymes|mcguffey|self-help|helps|resources|practice|dyslexia|audio|books"), ("about", r"about|vision|mission|team|contact|faq|front-page|^/?$|home|الرئيسية|من-نحن")]
def classify(url, title, kind):
    path = re.sub(r"^https?://[^/]+", "", url).lower()
    if kind == "post": return "news/event"
    if kind == "archive": return "archive"
    for c, rx in CATS:
        if re.search(rx, path + " " + title.lower()): return c
    return "other"

# ---------- pass 1: raw lines per page
pages = []
for site in ("agi", "anglia"):
    d = os.path.join(CRAWL, site)
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        raw = open(os.path.join(d, fn), encoding="utf-8", errors="ignore").read()
        url = re.search(r"<!-- source: (\S+) -->", raw).group(1)
        title = html.unescape(re.sub(r"\s+", " ", (re.search(r"<title>(.*?)</title>", raw, re.S) or [None, ""])[1]))
        title = re.split(r"\s[–|-]\s(?:American Group International|Anglia Morocco)", title)[0].strip()
        body = (re.search(r'<body[^>]*class="([^"]*)"', raw) or [None, ""])[1]
        kind = "post" if re.search(r"\bpostid-\d+", body) else ("archive" if re.search(r"\b(archive|blog|category)\b", body) and not re.search(r"\bpage-id-\d+", body) else "page")
        if re.search(r"elementor_library|floating", url + body): kind = "fragment"
        lang = "ar" if "/ar/" in url or re.search(r'<html[^>]+lang="ar', raw[:800]) else "en"
        date = (re.search(r'article:published_time" content="([^"]+)"', raw) or [None, ""])[1][:10]
        pages.append({"site": site, "url": url, "title": title, "kind": kind, "lang": lang, "date": date, "lines": [l for l in to_text(strip_chrome(raw)) if l]})
# ---------- pass 2: boilerplate per site
for site in ("agi", "anglia"):
    P = [p for p in pages if p["site"] == site]; cnt = Counter()
    for p in P: cnt.update({norm(l) for l in p["lines"] if norm(l)})
    limit = max(3, int(len(P) * 0.25))
    common = {k for k, v in cnt.items() if v > limit}
    for p in P:
        seen, keep = set(), []
        for l in p["lines"]:
            n = norm(l)
            if not n or n in common or n in seen or re.fullmatch(r"[-#\s|]*", l) or n in ("skip to content", "leave a reply cancel reply"): continue
            seen.add(n); keep.append(l)
        p["text"] = "\n".join(keep); del p["lines"]
    print(f"{site}: {len(P)} pages, {len(common)} boilerplate lines removed")

# ---------- coverage against the current site
def site_text():
    buf = []
    for dp, _, fs in os.walk(V2):
        if "_build" in dp or "_legacy" in dp: continue
        for f in fs:
            if f.endswith(".html"):
                s = open(os.path.join(dp, f), encoding="utf-8").read()
                s = re.sub(r"<!--site:(header|footer|seo)-->.*?<!--/site:\1-->", " ", s, flags=re.S)
                buf += to_text(re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S))
    return " " + norm(" ".join(buf)) + " "
SITE = site_text(); DIG = re.sub(r"\D", "", SITE)
def fact_present(k, v): return v in DIG if k == "phone" else (" " + norm(v) + " ") in SITE
def sent_cov(t):
    ss = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", t) if 60 <= len(s.strip()) <= 400]
    if not ss: return None
    hit = 0
    for s in ss:
        ws = [w for w in norm(s).split() if len(w) > 3]
        if ws and sum(1 for w in ws if f" {w} " in SITE) / len(ws) >= 0.8: hit += 1
    return round(hit / len(ss), 2)
for p in pages:
    p["category"] = classify(p["url"], p["title"], p["kind"]); p["words"] = len(p["text"].split()); p["thin"] = p["words"] < 150
    p["facts"] = facts(p["text"]); n = sum(len(v) for v in p["facts"].values())
    p["facts_missing"] = [f"{k}: {v}" for k, vs in p["facts"].items() for v in vs if not fact_present(k, v)]
    p["fact_coverage"] = round(1 - len(p["facts_missing"]) / n, 2) if n else None
    p["text_coverage"] = sent_cov(p["text"])
    sc = [x for x in (p["fact_coverage"], p["text_coverage"]) if x is not None]
    p["status"] = "fragment" if p["kind"] in ("fragment", "archive") else ("covered" if (min(sc) if sc else 1) >= 0.7 else ("partial" if min(sc) >= 0.3 else "missing"))
json.dump(pages, open(os.path.join(CRAWL, "inventory.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
with open(os.path.join(ROOT, "docs", "content-inventory.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["site", "language", "kind", "category", "title", "url", "date", "words", "thin", "text_coverage", "fact_coverage", "status", "missing_facts_examples"])
    for p in sorted(pages, key=lambda x: (x["site"], x["category"], x["title"])):
        w.writerow([p["site"], p["lang"], p["kind"], p["category"], p["title"], p["url"], p["date"], p["words"], "yes" if p["thin"] else "", p["text_coverage"], p["fact_coverage"], p["status"], " | ".join(p["facts_missing"][:8])])
for site in ("agi", "anglia"):
    S = [p for p in pages if p["site"] == site]
    print(f"== {site}: {len(S)} items · {sum(p['words'] for p in S):,} words after cleanup · status {dict(Counter(p['status'] for p in S))} · thin {sum(p['thin'] for p in S)} · categories {dict(Counter(p['category'] for p in S).most_common())}")
