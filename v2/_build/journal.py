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
