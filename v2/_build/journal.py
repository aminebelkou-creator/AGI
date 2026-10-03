"""Generates journal/<slug>.html for every news post in the content export, and links journal.html rows to them."""
import os, re, json, html, markdown
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORT = os.path.join(os.path.dirname(V2), "data", "export", "AGI_Website_Content_Export.json")
OUT = os.path.join(V2, "journal"); os.makedirs(OUT, exist_ok=True)
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
DESIGNED = {"chichester": "../journal-ccgi-partnership.html"}   # posts that already have a designed page

def kind_of(t):
    s = t.lower()
    if re.search(r"partner|join forces|forces|member|leverage|bridge|chichester|ccgi|counselor", s): return "Partnership"
    if re.search(r"graduat|congrat|award|spelling bee|celebrat|honor", s): return "Achievement"
    if re.search(r"inscription|admission|back to school|school starts|first day|semester|summer school|calendar", s): return "Admissions"
    if re.search(r"course|program|training|diploma|class|testing|exam|proctor|resource|psychology", s): return "Programs"
    return "News"
def clean_title(t): return re.sub(r'^[“"\s]+|[”"\s]+$', "", t.replace("\u00a0", " ")).strip()
def nice_date(d): y, m, dd = d.split("-"); return f"{MONTHS[int(m)-1]} {int(dd)}, {y}"
def clean_md(md):
    md = md.replace("\u00a0", " ")
    md = re.sub(r"^#+\s*$", "", md, flags=re.M)                          # empty headings
    md = re.sub(r"^\s*(Latest News|Leave a Reply.*|Read more)\s*$", "", md, flags=re.M | re.I)
    return md.strip()

posts = sorted(json.load(open(EXPORT, encoding="utf-8"))["news"], key=lambda p: p["date"], reverse=True)
IMG_MAP = os.path.join(V2, "_build", "journal-images.json")
IMAGES = json.load(open(IMG_MAP, encoding="utf-8")) if os.path.exists(IMG_MAP) else {}
TPL = open(os.path.join(V2, "_build", "article.tpl.html"), encoding="utf-8").read()
links = {}
for i, p in enumerate(posts):
    title = clean_title(p["title"]); slug = p["slug"]
    designed = next((v for k, v in DESIGNED.items() if k in title.lower()), None)
    links[title] = (designed or f"journal/{slug}.html").replace("../", "")
    if designed: continue
    body = markdown.markdown(clean_md(p.get("markdown", "")), extensions=["extra", "sane_lists"])
    body = re.sub(r'href="/(contact|forms|admissions)/?"', lambda m: f'href="../{m.group(1)}.html"', body)  # ROOT_LINKS
    body = re.sub(r'href="/([^"]*)"', r'href="https://www.americangroup-international.com/\1"', body)
    for _u, _local in IMAGES.items(): body = body.replace(_u, "../" + _local)   # local copies of old-site images
    body = re.sub(r"<(/?)h([1-5])\b", lambda m: f"<{m.group(1)}h{int(m.group(2)) + 1}", body)   # page title is the only h1
    body = re.sub(r"<img ", '<img loading="lazy" ', body)
    newer = posts[i - 1] if i > 0 else None; older = posts[i + 1] if i + 1 < len(posts) else None
    def nav(q, label):
        if not q: return "<span></span>"
        t = clean_title(q["title"]); d = next((v for k, v in DESIGNED.items() if k in t.lower()), None)
        return f'<a href="{d or q["slug"] + ".html"}"><small>{label}</small>{html.escape(t)}</a>'
    plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()
    desc = plain[:155].rsplit(" ", 1)[0] + "…" if len(plain) > 155 else plain
    if len(desc) < 70: desc = f"{title} – news from American Group International and Anglia Morocco, Agadir."[:160]
    page_title = title if len(title) > 56 else f"{title} – AGI Journal"
    doc = (TPL.replace("<title>{{TITLE}} – AGI Journal</title>", f"<title>{html.escape(page_title)}</title>").replace("{{TITLE}}", html.escape(title)).replace("{{DESC}}", html.escape(desc))
           .replace("{{DATE}}", nice_date(p["date"])).replace("{{KIND}}", kind_of(title)).replace("{{BODY}}", body)
           .replace("{{NEWER}}", nav(newer, "Newer")).replace("{{OLDER}}", nav(older, "Older")))
    open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8", newline="").write(doc)

# point the journal list rows at the real articles
jp = os.path.join(V2, "journal.html"); s = open(jp, encoding="utf-8", newline="").read()
def row(m):
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(3))).strip()
    href = links.get(t) or next((v for k, v in links.items() if k.lower() == t.lower()), None)
    if not href: print("  no article for:", t); return m.group(0)
    return m.group(1) + href + m.group(2) + m.group(3)
s2, n = re.subn(r'(<a class="[^"]*agi-jrow" href=")[^"]*(".*?<span style="font-family:\'Newsreader\'[^>]*>)(.*?</span>)', row, s, flags=re.S)
open(jp, "w", encoding="utf-8", newline="").write(s2)
print(f"articles generated: {len([f for f in os.listdir(OUT) if f.endswith('.html')])}; journal rows relinked: {n}")

# ---------------- CRAWL-ONLY POSTS: posts found on the live sites but not in the export ----------------
import csv as _csv
INV = {x["url"]: x for x in json.load(open(os.path.join(os.path.dirname(V2), "data", "crawl", "inventory.json"), encoding="utf-8"))}
MAPROWS = list(_csv.DictReader(open(os.path.join(os.path.dirname(V2), "docs", "content-map.csv"), encoding="utf-8-sig")))
def text_to_html(t):
    out, ul = [], False
    for l in t.split("\n")[1:]:
        l = l.strip()
        if not l: continue
        if l.startswith("#"):
            if ul: out.append("</ul>"); ul = False
            out.append(f"<h2>{html.escape(l.lstrip('# '))}</h2>"); continue
        if re.match(r"^[-•*]\s+", l):
            if not ul: out.append("<ul>"); ul = True
            out.append(f"<li>{html.escape(re.sub(r'^[-•*]\s+', '', l))}</li>"); continue
        if ul: out.append("</ul>"); ul = False
        out.append(f"<p>{html.escape(l)}</p>")
    if ul: out.append("</ul>")
    return "\n".join(out)
extra = 0
for r in MAPROWS:
    d = r["destination"]
    if not d.startswith("journal/") or os.path.exists(os.path.join(V2, d)): continue
    src = INV.get(r["url"])
    if not src: continue
    title = re.sub(r'^[“"\s]+|[”"\s]+$', "", src["title"]); body = text_to_html(src["text"])
    date = src.get("date") or ""
    nice = nice_date(date) if re.match(r"\d{4}-\d{2}-\d{2}", date) else ""
    plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body)).strip()
    doc = (TPL.replace("<title>{{TITLE}} – AGI Journal</title>", f"<title>{html.escape(title if len(title) > 56 else title + ' – AGI Journal')}</title>")
           .replace("{{TITLE}}", html.escape(title)).replace("{{DESC}}", html.escape((plain[:150] + "…") if len(plain) > 150 else plain or title))
           .replace("{{DATE}}", nice).replace("{{KIND}}", kind_of(title)).replace("{{BODY}}", body + f'<p class="muted" style="font-size:13px">Originally published on {html.escape(src["url"].split("/")[2])}.</p>')
           .replace("{{NEWER}}", "<span></span>").replace("{{OLDER}}", "<span></span>"))
    open(os.path.join(V2, d), "w", encoding="utf-8", newline="").write(doc); extra += 1
print(f"crawl-only posts generated: {extra}")

# ---------------- LANGUAGE MARKUP: bilingual posts keep their French/Arabic paragraphs, marked with lang ----------------
_FRW = set("le la les des est et pour avec une un du dans sur que qui vous nous sont aux au ce cette ces leur leurs pas plus être été par".split())
_ENW = set("the and for with is are to of in on that this you we our your be was were by not from".split())
def _lang_of(t):
    if len(re.findall(r"[\u0600-\u06ff]", t)) >= 8: return "ar"
    w = re.findall(r"[a-zà-ÿ']+", t.lower()); fr = sum(x in _FRW for x in w); en = sum(x in _ENW for x in w)
    return "fr" if len(w) >= 6 and fr >= 4 and fr > en * 1.5 else None
_n = 0
for _f in os.listdir(os.path.join(V2, "journal")):
    _p = os.path.join(V2, "journal", _f); _t = open(_p, encoding="utf-8").read()
    def _mark(m):
        global _n
        lang = _lang_of(re.sub(r"<[^>]+>", " ", m.group(2)))
        if not lang: return m.group(0)
        _n += 1; return f'<{m.group(1)} lang="{lang}"' + (' dir="rtl"' if lang == "ar" else "") + f'>{m.group(2)}</{m.group(1)}>'
    _new = re.sub(r"<(p|li|h2|h3)>(.*?)</\1>", _mark, _t, flags=re.S)
    if _new != _t: open(_p, "w", encoding="utf-8", newline="").write(_new)
print(f"journal: {_n} French/Arabic paragraphs marked with lang")

# ---------------- JOURNAL CLEANUP: video codes, shortcodes, hashtag lines, raw links, duplicates ----------------
def _clean_article(t):
    head, sep, body = t.partition("<main")
    if not sep: return t
    body = re.sub(r'\[video[^\]]*?(?:mp4|src)="([^"]+)"[^\]]*\](?:\s*\[/video\])?', lambda m: f'<a class="link" href="{m.group(1).replace("http://", "https://")}" target="_blank" rel="noopener">Watch the video</a>', body)
    body = re.sub(r"\[/?(?:caption|gallery|embed|contact-form-7|video)[^\]]*\]", "", body)
    body = re.sub(r"<p>(?:\s*#\w+[\s,.]*){2,}</p>", "", body)
    body = re.sub(r"<p>\s*_{4,}\s*</p>", "", body)
    body = re.sub(r"<p>\s*[a-z]+(?: [a-z]+){0,2}\s*</p>", "", body)                         # lowercase gallery captions ("christmas party")                                     # separator lines of underscores
    _fn = re.compile(r"\d{6,}_|_\d{4,}|^[a-z]{3,}\d+$")
    def _gallery(m):                                                                    # lists of photo file names / gallery captions
        items = re.findall(r"<li>(.*?)</li>", m.group(0), re.S)
        return "" if sum(1 for x in items if _fn.search(x.strip())) >= 2 else m.group(0)
    body = re.sub(r"<ul>.*?</ul>", _gallery, body, flags=re.S)
    body = re.sub(r"<p>\s*(?:[^<\s]*\d{6,}_[^<\s]*|[a-z]{3,}\d+)\s*</p>", "", body)                              # paragraphs of hashtags only
    body = re.sub(r"(<p>[^<]*?)((?:\s*#\w+){3,}\s*)(</p>)", r"\1\3", body)                  # trailing hashtag runs
    body = re.sub(r'(?<![="\'>])(https?://[^\s<"]+)', lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{re.sub(r"^https?://(www\.)?", "", m.group(1)).split("/")[0]}</a>', body)
    seen = set()
    def _dedupe(m):
        k = re.sub(r"\W+", " ", re.sub(r"<[^>]+>", " ", m.group(0)).lower()).strip()
        if len(k) > 40 and k in seen: return ""
        seen.add(k); return m.group(0)
    body = re.sub(r"<p\b[^>]*>.*?</p>", _dedupe, body, flags=re.S)
    return head + sep + body
_c = 0
for _f in os.listdir(os.path.join(V2, "journal")):
    _p = os.path.join(V2, "journal", _f); _t = open(_p, encoding="utf-8").read(); _n2 = _clean_article(_t)
    if _n2 != _t: open(_p, "w", encoding="utf-8", newline="").write(_n2); _c += 1
print(f"journal cleanup: {_c} articles cleaned")

# ---------------- PRIVACY + ARCHIVE: hidden photos until consent, banner on posts older than 12 months ----------------
import datetime as _dt
_PJ = os.path.join(V2, "_build", "privacy.json")
_PRIV = json.load(open(_PJ, encoding="utf-8")) if os.path.exists(_PJ) else {"hide_photos": [], "approved": []}
_HIDE = set(_PRIV.get("hide_photos", [])) - set(_PRIV.get("approved", []))
_MON = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"], 1)}
_CUT = _dt.date.today() - _dt.timedelta(days=365)
_h = _a = 0
for _f in os.listdir(os.path.join(V2, "journal")):
    _p = os.path.join(V2, "journal", _f); _t = open(_p, encoding="utf-8").read(); _o = _t
    if f"journal/{_f}" in _HIDE:
        _t = re.sub(r"<figure\b[^>]*>\s*<img\b[^>]*>.*?</figure>|<img\b[^>]*>", '<span class="photo-hidden">Photo hidden until parental consent is confirmed.</span>', _t, flags=re.S)
        _t = _t.replace('<main id="main" class="article np">', '<main id="main" class="article np" data-verify="privacy-review">', 1); _h += 1
    _m = re.search(r'<p class="article-meta"><b>[^<]*</b>([^<]*)</p>', _t)
    if _m and "archived-note" not in _t:
        _d = _m.group(1); _y = re.search(r"(19|20)\d{2}", _d); _mo = next((v for k, v in _MON.items() if k in _d.lower()), 1)
        if _y and _dt.date(int(_y.group(0)), _mo, 1) < _CUT:
            _t = _t.replace('<div class="prose">', f'<div class="prose"><p class="archived-note">Archived post{(" from " + _d.strip()) if _d.strip() else ""}. Fees, dates and programs may have changed – see the current <a href="../fees.html">tuition &amp; fees</a> and <a href="../calendar.html">calendar</a>.</p>', 1); _a += 1
    if _t != _o: open(_p, "w", encoding="utf-8", newline="").write(_t)
print(f"privacy: photos hidden in {_h} posts · archive banner on {_a} posts")

import csv
# ---------------- OLD-SITE LINKS: files moved here, home links, dead images, Facebook hashtag links ----------------
_OLDMAP = json.load(open(os.path.join(V2, "_build", "old-site-files.json"), encoding="utf-8")) if os.path.exists(os.path.join(V2, "_build", "old-site-files.json")) else {}
_XP = os.path.join(os.path.dirname(V2), "docs", "external-links.csv")
_DEAD = {r["url"] for r in csv.DictReader(open(_XP, encoding="utf-8-sig")) if r["status"] == "BROKEN"} if os.path.exists(_XP) else set()
_fx = 0
for _f in [x for x in os.listdir(os.path.join(V2, "journal")) if x.endswith(".html") and not x.startswith("_")]:
    _p = os.path.join(V2, "journal", _f); _t = open(_p, encoding="utf-8").read(); _o = _t
    for _u, _loc in _OLDMAP.items(): _t = _t.replace(_u, "../" + _loc).replace(_u.replace("http://", "https://"), "../" + _loc)
    _t = re.sub(r'href="https?://www\.americangroup-international\.com/?"', 'href="../index.html"', _t)
    _t = re.sub(r'<a[^>]+href="https://www\.facebook\.com/hashtag/[^"]*"[^>]*>.*?</a>', "", _t, flags=re.S)
    _t = re.sub(r'<img\b[^>]*src="([^"]+)"[^>]*>', lambda m: "" if m.group(1).replace("&amp;", "&") in _DEAD else m.group(0), _t)
    if _t != _o: open(_p, "w", encoding="utf-8", newline="").write(_t); _fx += 1
print(f"old-site links fixed in {_fx} posts ({len(_OLDMAP)} files now hosted here)")

# ---------------- JOURNAL LIST + CCGI ARTICLE (shared design, generated from the articles themselves) ----------------
def _root_page(main_html, title, desc):
    doc = TPL.replace("<title>{{TITLE}} – AGI Journal</title>", f"<title>{html.escape(title)}</title>").replace("{{DESC}}", html.escape(desc))
    doc = re.sub(r"<main\b.*?</main>", lambda m: main_html, doc, flags=re.S)
    return re.sub(r'(href|src)="\.\./', r'\1="', doc)
# CCGi partnership article from the original post text
_cc = next((r for r in MAPROWS if "join-forces-with-chichester" in r["url"]), None)
if _cc and _cc["url"] in INV:
    _src = INV[_cc["url"]]; _title = re.sub(r'^[“"\s]+|[”"\s]+$', "", _src["title"])
    _main = (f'<main id="main" class="article np"><section class="page-hero wrap"><p class="crumb"><a href="index.html">Home</a> / <a href="journal.html">Journal</a> / <span>Partnership</span></p>'
             f'<h1 style="max-width:22ch;font-size:clamp(36px,4.4vw,64px)">{html.escape(_title)}</h1><p class="article-meta"><b>Partnership</b>{nice_date(_src["date"]) if re.match(r"\d{4}-\d{2}-\d{2}", _src.get("date") or "") else ""}</p></section>'
             f'<section class="section bg-white"><div class="wrap"><div class="prose">{text_to_html(_src["text"])}</div><p style="margin-top:28px"><a class="link" href="partnerships.html">Partnerships &amp; franchise</a> · <a class="link" href="journal.html">All journal entries</a></p></div></section>'
             + '<section class="section tight bg-navy"><div class="wrap cta-band"><div><h2>Partner with AGI.</h2><p>Franchise and partnership enquiries are handled from the Agadir headquarters.</p></div><div class="btn-row"><a class="btn btn-gold" href="forms.html#enquiry/partnership">Partnership enquiry</a></div></div></section></main>')
    open(os.path.join(V2, "journal-ccgi-partnership.html"), "w", encoding="utf-8", newline="").write(_root_page(_main, f"{_title[:60]} – AGI Journal", "AGI and Anglia Morocco join Chichester College Group International to empower global learners."))
# journal list: every article, newest first, grouped by year
_items = []
for _f in [x for x in os.listdir(os.path.join(V2, "journal")) if x.endswith(".html") and not x.startswith("_")]:
    _t = open(os.path.join(V2, "journal", _f), encoding="utf-8").read()
    _ti = html.unescape(re.sub(r"<[^>]+>", "", (re.search(r"<h1[^>]*>(.*?)</h1>", _t, re.S) or [None, _f])[1])).strip()
    _mm = re.search(r'<p class="article-meta"><b>([^<]*)</b>([^<]*)</p>', _t); _kind = _mm.group(1) if _mm else "News"; _d = (_mm.group(2) if _mm else "").strip()
    _y = re.search(r"(19|20)\d{2}", _d); _mo = next((v for k, v in _MON.items() if k in _d.lower()), 0)
    _ex = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", (re.search(r'<div class="prose">(.*?)</div>', _t, re.S) or [None, ""])[1]))).replace("Archived post", "").strip()
    _ex = re.sub(r"^from [^.]*\.\s*Fees, dates and programs may have changed – see the current tuition & fees and calendar\.\s*", "", _ex)
    _items.append((int(_y.group(0)) if _y else 0, _mo, _ti, _kind, _d, _f, (_ex[:150] + "…") if len(_ex) > 150 else _ex, "angliamorocco" in _t))
_items.sort(key=lambda x: (x[0], x[1]), reverse=True)
_groups = {}
for it in _items: _groups.setdefault(it[0] or "Undated", []).append(it)
_nav = " · ".join(f'<a href="#y{y}">{y}</a>' for y in _groups)
_body = "".join(f'<h2 id="y{y}" style="margin-top:48px">{y}</h2><div class="cards">' + "".join(
    f'<a class="card" href="journal/{f}"><span class="tag">{html.escape(k)}{" · Anglia Morocco" if a else ""}</span><h3>{html.escape(ti)}</h3><p class="muted" style="font-size:13px;margin:0 0 8px">{html.escape(d)}</p><p>{html.escape(ex)}</p><span class="more">Read</span></a>'
    for _y2, _m2, ti, k, d, f, ex, a in L) + "</div>" for y, L in _groups.items())
_main = (f'<main id="main" class="np"><section class="page-hero wrap"><p class="crumb"><a href="index.html">Home</a> / <span>Journal</span></p><h1>Journal.</h1>'
         f'<p class="lede">News from AGI and Anglia Morocco since 2017: graduations, partnerships, exams, events and school life. Posts older than a year are archived – fees and dates in them may have changed.</p></section>'
         f'<section class="section bg-white"><div class="wrap"><p><b>{len(_items)} posts</b> · {_nav}</p>{_body}</div></section>'
         '<section class="section tight bg-navy"><div class="wrap cta-band"><div><h2>Come and see the school.</h2><p>Tours are arranged individually, Monday to Friday.</p></div><div class="btn-row"><a class="btn btn-gold" href="forms.html#visit">Book a visit</a><a class="btn btn-light" href="parents.html">For parents</a></div></div></section></main>')
open(os.path.join(V2, "journal.html"), "w", encoding="utf-8", newline="").write(_root_page(_main, "Journal – American Group International, Agadir", f"News from American Group International and Anglia Morocco: {len(_items)} posts on graduations, partnerships, Anglia exams, events and school life."))
print(f"journal list: {len(_items)} posts in {len(_groups)} years · CCGi article rebuilt")
