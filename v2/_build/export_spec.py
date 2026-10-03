"""Exports a design-neutral content specification of the website (pages, sections, copy, data, forms).
Output: docs/website-content-spec.md (front matter from docs/_spec-intro.md + generated page content)."""
import os, re, json, html
from html.parser import HTMLParser
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
INLINE = {"a", "span", "b", "strong", "em", "i", "small", "br", "sup", "sub", "img", "abbr", "code", "label", "time", "u", "mark", "s"}
SKIP = {"script", "style", "noscript", "header", "footer", "svg", "template", "iframe", "dialog"}

class Node:
    def __init__(s, tag, attrs, parent): s.tag, s.attrs, s.parent, s.kids = tag, dict(attrs), parent, []
class Tree(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.root = Node("root", [], None); s.cur = s.root
    def handle_starttag(s, t, a):
        n = Node(t, a, s.cur); s.cur.kids.append(n)
        if t not in VOID: s.cur = n
    def handle_endtag(s, t):
        n = s.cur
        while n is not None and n.tag != t: n = n.parent
        if n is not None and n.parent is not None: s.cur = n.parent
    def handle_data(s, d): s.cur.kids.append(d)
def parse(p):
    t = Tree(); t.feed(open(p, encoding="utf-8").read()); return t.root
def find(n, pred):
    if isinstance(n, str): return None
    if pred(n): return n
    for k in n.kids:
        r = find(k, pred)
        if r is not None: return r
def cls(n): return n.attrs.get("class") or ""
def text(n):
    if isinstance(n, str): return n
    if n.tag in SKIP: return ""
    if n.tag == "br": return " "
    if n.tag == "img": return ""
    t = "".join((" " + text(k) + " ") if not isinstance(k, str) else text(k) for k in n.kids)
    if n.tag in ("a", "span", "b", "strong", "small"): t = t
    ph = n.attrs.get("data-placeholder", "")
    if ph.startswith("fact:") or "ph-text" in cls(n): t = f"[TO CONFIRM: {re.sub(r'\s+', ' ', t).strip()}]"
    return t
def clean(t): return re.sub(r"\s+([.,;:!?)])", r"\1", re.sub(r"\s+", " ", t)).strip().replace("Sample testimonial", "").strip()
def is_block(n):
    if isinstance(n, str): return False
    if n.tag == "a" and any(x in (n.attrs.get("class") or "") for x in ("btn", "card", "link", "more")): return True
    if n.tag == "span" and any(x in (n.attrs.get("class") or "") for x in ("tag", "num", "more")): return True
    return n.tag not in INLINE
def link_of(n):
    return n.attrs.get("href", "") if not isinstance(n, str) and n.tag == "a" else ""

out = []
def emit(line):
    if line and (not out or out[-1] != line): out.append(line)

def walk(n, depth=0):
    if isinstance(n, str):
        t = clean(n)
        if t: emit(t)
        return
    if n.tag in SKIP: return
    c = cls(n); ph = n.attrs.get("data-placeholder", "")
    if ph.startswith("photo:"):
        emit(f"[PHOTO NEEDED – {clean(text(n)).replace('Photo', '', 1).strip()}]"); return
    if n.tag == "figure" and "testimonial" in c:
        q = find(n, lambda x: x.tag == "blockquote"); cap = find(n, lambda x: x.tag == "figcaption")
        tag = " [SAMPLE – replace with a real testimonial]" if ph.startswith("testimonial") else ""
        emit(f"> “{clean(text(q))}” — {clean(text(cap))}{tag}"); return
    if n.tag == "img":
        alt = n.attrs.get("alt", ""); src = n.attrs.get("src", "")
        emit(f"[IMAGE: {alt or os.path.basename(src)}]"); return
    if n.tag in ("h1", "h2", "h3", "h4"):
        lvl = {"h1": "Page title (H1)", "h2": None, "h3": None, "h4": None}[n.tag]
        t = clean(text(n))
        if n.tag == "h2": emit(f"\n#### Section: {t}")
        elif n.tag == "h1": emit(f"**{lvl}:** {t}")
        else: emit(f"**{t}**")
        return
    if n.tag == "table":
        rows = []
        for tr in iter_tag(n, "tr"):
            rows.append([clean(text(c2)) for c2 in tr.kids if not isinstance(c2, str) and c2.tag in ("td", "th")])
        if rows:
            emit(""); emit("| " + " | ".join(rows[0]) + " |"); emit("|" + "---|" * len(rows[0]))
            for r in rows[1:]: emit("| " + " | ".join(r) + " |")
            emit("")
        return
    if n.tag == "dl" or (n.tag == "div" and "rows" in c):
        for item in [k for k in n.kids if not isinstance(k, str)]:
            dt = find(item, lambda x: x.tag == "dt"); dd = find(item, lambda x: x.tag == "dd")
            if dt and dd: emit(f"- **{clean(text(dt))}** — {clean(text(dd))}{links_in(dd)}")
            else: walk(item, depth + 1)
        return
    if n.tag == "details":
        s = find(n, lambda x: x.tag == "summary"); body = "".join(clean(text(k)) + " " for k in n.kids if k is not s)
        emit(f"- **Q: {clean(text(s))}** — A: {clean(body)}"); return
    if n.tag == "a" and ("btn" in c or "card" in c or "link" in c or "more" in c):
        t = clean(text(n)); href = n.attrs.get("href", "")
        if "card" in c and is_compound(n):
            parts = [clean(text(k)) for k in n.kids if not isinstance(k, str) and clean(text(k)) and "more" not in cls(k)]
            emit(f"- Link card → `{href}`: " + " · ".join(parts)); return
        emit(f"→ **{t}** (`{href}`)"); return
    if n.tag == "span" and "tag" in c: emit(f"_{clean(text(n))}_"); return
    if n.tag == "span" and "num" in c: emit(f"Step {clean(text(n))}"); return
    if n.tag == "span" and "more" in c: return
    if n.tag == "li":
        emit(f"- {clean(text(n))}{links_in(n)}"); return
    kids = [k for k in n.kids if not (isinstance(k, str) and not k.strip())]
    if kids and all(not is_block(k) for k in kids):          # leaf block: emit its text once
        t = clean(text(n))
        if t: emit(t + links_in(n))
        return
    for k in n.kids: walk(k, depth + 1)

def iter_tag(n, tag):
    for k in n.kids:
        if isinstance(k, str): continue
        if k.tag == tag: yield k
        else: yield from iter_tag(k, tag)
def iter_all(n, tag):
    for k in n.kids:
        if isinstance(k, str): continue
        if k.tag == tag: yield k
        yield from iter_all(k, tag)
def iter_every(n):
    for k in n.kids:
        if isinstance(k, str): continue
        yield k
        yield from iter_every(k)
def is_compound(n): return any(not isinstance(k, str) and k.tag in ("h3", "p", "span") for k in n.kids)
def links_in(n):
    ls = [(clean(text(a)), a.attrs.get("href", "")) for a in iter_tag(n, "a") if a.attrs.get("href") and not a.attrs.get("href").startswith(("tel:", "mailto:"))]
    return "".join(f" [link: “{t}” → `{h}`]" for t, h in ls if t) if ls else ""

ORDER = ["index.html", "our-story.html", "parents.html", "founder-letter.html", "about.html", "programs.html", "k12.html", "special-education.html",
         "adult-diploma.html", "english-anglia.html", "teachers.html", "professional.html", "pathways.html", "admissions.html", "policies.html",
         "student-life.html", "journal.html", "journal-ccgi-partnership.html", "partnerships.html", "investors.html", "contact.html", "connect.html", "privacy.html", "terms.html"]
ORDER += sorted(f for f in os.listdir(V2) if f.endswith(".html") and f not in ORDER and not f.startswith("_"))
pages_md = []
for i, f in enumerate(ORDER, 1):
    root = parse(os.path.join(V2, f))
    title = clean(text(find(root, lambda x: x.tag == "title")))
    desc = find(root, lambda x: x.tag == "meta" and x.attrs.get("name") == "description")
    main = find(root, lambda x: x.tag == "main")
    out.clear()
    if f == "journal.html":   # the archive list is data: summarize
        walk(find(main, lambda x: x.tag == "section"))
        emit("\n#### Section: Archive"); emit("All 60 posts, grouped by year (newest first). Each row: date, category (Partnership, Achievement, Admissions, Programs, News), title, link to the article page. Full list in Appendix B.")
    else:
        walk(main)
    body = "\n".join(out).strip()
    pages_md.append(f"### 4.{i} `{f}`\n\n- **Browser title:** {title}\n- **Meta description:** {desc.attrs.get('content', '') if desc else ''}\n\n{body}\n")

# ---------------- forms (from the rendered page) ----------------
froot = parse(os.path.join(os.environ["TEMP"], "forms_rendered.html"))
fmain = find(froot, lambda x: x.tag == "main")
forms_md = []
for sheet in iter_tag(fmain, "section"):
    if "sheet" not in cls(sheet) or sheet.attrs.get("id") == "start": continue
    sid = sheet.attrs.get("id"); h2 = find(sheet, lambda x: x.tag == "h2")
    meta = find(sheet, lambda x: x.tag == "p" and "meta" in cls(x)); intro = find(sheet, lambda x: x.tag == "p" and "intro" in cls(x))
    brief = find(sheet, lambda x: "brief" in cls(x)); notice = find(sheet, lambda x: x.tag == "p" and "notice" in cls(x))
    have = [clean(text(li)) for li in iter_tag(brief, "li")] if brief else []
    nxt = [clean(text(p)) for p in iter_tag(brief, "p")] if brief else []
    btn = find(sheet, lambda x: x.tag == "button" and x.attrs.get("type") == "submit")
    lines = [f"#### Form: {clean(text(h2))} (`forms.html#{sid}`)", f"- **Duration shown:** {clean(text(meta))}", f"- **Introduction:** {clean(text(intro))}",
             "- **Have ready:** " + "; ".join(have), "- **What happens next:** " + " ".join(nxt)]
    if notice: lines.append(f"- **Notice:** {clean(text(notice))}")
    lines.append("")
    form = find(sheet, lambda x: x.tag == "form")
    for fs in iter_tag(form, "fieldset"):
        if "group" not in cls(fs): continue
        lg = find(fs, lambda x: x.tag == "legend"); lines.append(f"**{clean(text(lg))}**"); lines.append("")
        lines.append("| Field | Type | Required | Hint / options |"); lines.append("|---|---|---|---|")
        for fld in [k for k in iter_every(fs) if (k.tag == "div" and "field" in cls(k).split()) or (k.tag == "fieldset" and "choice" in cls(k))]:
            lab = find(fld, lambda x: x.tag in ("label", "legend")); hint = find(fld, lambda x: "hint" in cls(x))
            ctl = find(fld, lambda x: x.tag in ("input", "select", "textarea"))
            if ctl is None: continue
            typ = ctl.tag if ctl.tag != "input" else ctl.attrs.get("type", "text")
            if "choice" in cls(fld): typ = "single choice" if typ == "radio" else "multiple choice"
            req = "yes" if ("required" in ctl.attrs or any("required" in o.attrs for o in iter_tag(fld, "input"))) else ("conditional" if ctl.attrs.get("data-req-if") else "no")
            if "data-min-one" in fld.attrs: req = "at least one"
            if ctl.attrs.get("data-req-if"): req = "if " + ctl.attrs["data-req-if"].replace("|", " = ")
            opts = [clean(text(o)) for o in iter_tag(fld, "option") if o.attrs.get("value", "x") != ""] or [o.attrs.get("value") for o in iter_tag(fld, "input") if o.attrs.get("type") in ("radio", "checkbox") and "choice" in cls(fld)]
            label = re.sub(r"\s*optional$", "", clean(text(lab))) if lab else ""
            extra = "; ".join(x for x in [clean(text(hint)) if hint else "", ("Options: " + ", ".join(opts)) if opts else ""] if x)
            lines.append(f"| {label} | {typ} | {req} | {extra} |")
        lines.append("")
    lines.append(f"- **Submit button:** {clean(text(btn))}"); lines.append("")
    forms_md.append("\n".join(lines))

# ---------------- journal appendix ----------------
news = json.load(open(os.path.join(ROOT, "data", "export", "AGI_Website_Content_Export.json"), encoding="utf-8"))["news"]
journal_md = "| Date | Title | Article page |\n|---|---|---|\n" + "\n".join(
    f"| {n['date']} | {clean(n['title']).replace('|', '/')} | `{'journal-ccgi-partnership.html' if 'chichester' in n['title'].lower() else 'journal/' + n['slug'] + '.html'}` |"
    for n in sorted(news, key=lambda n: n["date"], reverse=True))

intro = open(os.path.join(ROOT, "docs", "_spec-intro.md"), encoding="utf-8").read()
doc = (intro.rstrip() + "\n\n---\n\n## 4. Pages – sections and content\n\nContent is listed in reading order. Notation: **Section:** = a main section heading · **bold line** = a sub-heading · `→ Label (target)` = a button or link · `[PHOTO NEEDED – …]` = photo to supply · `[TO CONFIRM: …]` = fact awaiting confirmation · `[SAMPLE …]` = placeholder testimonial.\n\n"
       + "\n---\n\n".join(pages_md) + "\n---\n\n## 5. Forms – fields and behavior\n\nAll forms live on one page (`forms.html`) with a list of forms and one form shown at a time; each can be opened directly by its address. An overview panel (\"How it works\") is shown when no form is selected: 1) Choose a form, 2) Fill it in – every field is required unless marked optional, 3) The office replies within one working day, Monday to Friday. Most-used shortcuts: Report an absence, Apply for a place, Payment notice, Request a transcript. Side panel: \"Prefer to talk?\" with phone numbers, WhatsApp, and \"The office is closed on Sundays.\" Every form ends with: *Your details go only to the AGI office in Agadir and are used to handle this request.*\n\n"
       + "\n".join(forms_md) + "\n\n---\n\n## Appendix B. Journal posts (60)\n\nFull text of each post: `data/export/AGI_Website_Content_Export.json` → `news[]` (title, slug, date, markdown).\n\n" + journal_md + "\n")
open(os.path.join(ROOT, "docs", "website-content-spec.md"), "w", encoding="utf-8").write(doc)
print("written docs/website-content-spec.md:", len(doc.split()), "words,", doc.count("\n"), "lines,", len(pages_md), "pages,", len(forms_md), "forms")
