# Phase 1 content pages – generated from the crawled source texts (data/crawl/inventory.json) + the fact register (facts.json).
# Loaded by pages.py (exec), so page(), hero(), cta(), PH_TXT, APPLY, VISIT, GOLD_APPLY, LIGHT_VISIT are available.
import json as _json, re as _re, html as _html
import re
_INV = {p["url"]: p for p in _json.load(open(os.path.join(os.path.dirname(V2), "data", "crawl", "inventory.json"), encoding="utf-8"))}
FACTS = _json.load(open(os.path.join(V2, "_build", "facts.json"), encoding="utf-8"))
def SRC(part):
    hit = next((p for u, p in _INV.items() if part in u), None)
    if hit is None: print(f'WARNING: source not found in inventory: {part}'); return {'text': '', 'url': '', 'title': part}
    return hit

# ---------------- language detection + text cleanup (content quality) ----------------
_FRW = set("le la les des est et pour avec une un du dans sur que qui vous nous sont aux au ce cette ces leur leurs pas plus être été par".split())
_ENW = set("the and for with is are to of in on that this you we our your be was were by not from".split())
def is_ar(t):
    letters = len(_re.sub(r"\s", "", t)); ar = len(_re.findall(r"[\u0600-\u06ff]", t))
    return ar >= 8 and ar >= 0.3 * max(letters, 1)
def is_fr(t):
    w = _re.findall(r"[a-zà-ÿ']+", t.lower())
    if len(w) < 6: return False
    fr = sum(x in _FRW for x in w); en = sum(x in _ENW for x in w)
    return (fr >= 4 and fr > en * 1.5) or (len(_re.findall(r"[éèêàçù]", t)) >= 3 and fr >= 3 and fr > en)
AGI_EMAIL = '<a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a>'
def clean_line(l):
    """Returns (kind, value): ('skip',None) | ('html', ready html) | ('text', cleaned text)."""
    t = l.replace("u003cbru003e", " ").replace("u003cbr", " ").replace("u003e", "").replace("u003c", "")
    t = _re.sub(r"\s+", " ", t).strip()
    if not t: return ("skip", None)
    if t.count("#") >= 2 and _re.fullmatch(r"[\w\s#.,!&-]*#\w+[\w\s#.,!&-]*", t) and len(_re.sub(r"#\w+", "", t).split()) <= 3: return ("skip", None)   # hashtag lines
    v = _re.search(r'\[video[^\]]*?(?:mp4|src)="([^"]+)"[^\]]*\]', t)
    if v: return ("html", f'<p><a class="link" href="{v.group(1).replace("http://", "https://")}" target="_blank" rel="noopener">Watch the video</a></p>')
    t = t.replace("[email/contact info]", "\x00EMAIL\x00")
    t = _re.sub(r"\[(?:contact-form-7|caption|/caption|gallery|embed|/embed)[^\]]*\]", "", t).strip()
    if not t or _re.fullmatch(r"(?i)(?:[-•*·]\s*)?(click here|show the way|find your way by cli[c]?king here ?:?|read more|contact us|download|apply now!?|enroll now|learn more|register now|book now|submit|share)", t): return ("skip", None)
    if _re.search(r"\s&$", t) and len(t.split()) <= 6: return ("skip", None)                     # old form field labels ("Drivers License Number &")
    return ("text", t)
TITLE_FIX = [(r"groupinternationala@gmail\.com", "americanecoleagadir@gmail.com"),
             (r"Julie\s+(?:A\.\s+)?WILBURN\s+Director of Operations of Anglia Morocco", "Julie Wilburn, CEO &amp; Educational Director, Anglia Examinations Morocco"),
             (r"Julie\s+Wilburn\s*[-–]\s*Director of Operations", "Julie Wilburn – CEO &amp; Educational Director"),
             (r"Anglia Morocco Country Manager", "CEO &amp; Educational Director, Anglia Examinations Morocco"),
             (r"Director of Operations of Anglia Morocco", "CEO &amp; Educational Director, Anglia Examinations Morocco")]
CLAIM_MARK = [(r"\b(International\s+)?Correspondence(\s+School)?\b", "claim-correspondence"), (r"\b45\+?\s+(?:different\s+)?nationalities\b", "claim-nationalities")]
def fix_claims(esc):
    for rx, rp in TITLE_FIX: esc = _re.sub(rx, rp, esc, flags=_re.I)
    for rx, key in CLAIM_MARK:
        esc = _re.sub(rx, lambda m: f'<span class="ph-text" data-placeholder="fact:{key}">{m.group(0)}</span>', esc)
    return esc
def linkify(esc):
    esc = _re.sub(r"\[\s*([^\]]+?)\s*\]\((https?://[^)\s]+)\)", lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', esc)
    esc = _re.sub(r'(?<!href=")(?<!">)(https?://[^\s<)]+)', lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{_re.sub(r"^https?://(www\.)?", "", m.group(1)).split("/")[0]}</a>', esc)
    return fix_claims(esc.replace("\x00EMAIL\x00", AGI_EMAIL))
def _is_filename(t):
    """Image file names and gallery captions left by WordPress: '30174036_1021…_o', 'ahmedpic', 'adamjulie18', 'IMG_2034'."""
    return bool(_re.search(r"\d{6,}_|_\d{4,}|^(?:img|dsc|image|photo|whatsapp)[_ -]?\d", t, _re.I) or _re.fullmatch(r"[a-z]{3,}\d+", t))
def _runs_to_lists(lines):
    """5+ consecutive one-to-three-word lines (a list that lost its bullets) become a bulleted list."""
    out, run = [], []
    def flush():
        junk = sum(1 for x in run if _is_filename(x.strip()))
        if sum(1 for x in run if x.strip().endswith((":", "&"))) >= 3: run.clear(); return      # old paper-form labels
        if len(run) >= 5 and junk >= 2: pass                                   # photo-gallery captions / file names: drop the whole run
        elif len(run) >= 5: out.extend("- " + x.strip() for x in run)
        else: out.extend(x for x in run if not _is_filename(x.strip()))
        run.clear()
    for l in lines:
        t = l.strip()
        if t and not t.startswith(("#", "-", "<")) and len(t.split()) <= 3 and not t.endswith((".", ":", "?")) and not _re.match(r"^\d{1,2}[.)]\s", t): run.append(l)
        else: flush(); out.append(l)
    flush(); return out
FOREIGN = {"ar": {}, "fr": {}}
def split_languages(page_html, name):
    """Move Arabic/French blocks out of an English page (kept for ar/ and fr/), and drop repeated paragraphs."""
    seen = set()
    def repl(m):
        txt = _re.sub(r"\s+", " ", _html.unescape(_re.sub(r"<[^>]+>", " ", m.group(0)))).strip()
        lang = "ar" if is_ar(txt) else ("fr" if is_fr(txt) else None)
        if lang: FOREIGN[lang].setdefault(name, []).append(m.group(0)); return ""
        key = _re.sub(r"\W+", " ", txt.lower()).strip()
        if len(key) > 40 and m.group(1) in ("p", "li"):
            if key in seen: return ""
            seen.add(key)
        return m.group(0)
    head, sep, rest = page_html.partition("<main")
    if not sep: return page_html
    return head + sep + _re.sub(r"<(p|li|h2|h3|dd|blockquote)\b(?![^>]*\blang=)[^>]*>.*?</\1>", repl, rest, flags=_re.S)

_BUL = _re.compile(r"^\s*(?:[-•*·]|ÔÇó|\u2022)\s+")
_NUM = _re.compile(r"^\s*(\d{1,2})[.)]\s+")
def _is_heading(l):
    if l.startswith("#"): return True
    t = l.strip(); letters = _re.sub(r"[^A-Za-z]", "", t)
    return 3 < len(t) < 70 and len(letters) > 3 and t.upper() == t and not _re.search(r"\d{3,}", t)
_SMALL = {"a", "an", "and", "the", "of", "to", "in", "for", "on", "at", "by", "or", "vs", "with", "is", "it", "your", "our", "a"}
def _is_subhead(l, lines, i):
    t = l.strip()
    if not (3 <= len(t) <= 70) or t[0].islower() or _BUL.match(t) or _NUM.match(t) or t.startswith("#"): return False
    if t[-1] in ".,;:!" or _re.search(r"\d{2,}|@|http|MAD|\$", t): return False
    words = [w for w in _re.findall(r"[A-Za-z'’]+", t)]
    if len(words) < 2: return False
    caps = sum(1 for w in words if w[0].isupper() or w.lower() in _SMALL)
    nxt = next((x.strip() for x in lines[i + 1:] if x.strip()), "")
    return caps / len(words) >= 0.8 and len(nxt) > 80
TABLES = [["Grade Level", "Session Length", "Sessions Per Week"]]   # known tables flattened in the old pages
def _tableize(lines):
    L = [x.strip() for x in lines]; out = []; i = 0
    while i < len(L):
        hit = next((h for h in TABLES if L[i:i + len(h)] == h), None)
        if not hit: out.append(lines[i]); i += 1; continue
        n = len(hit); j = i + n; rows = []
        while j + n <= len(L) and all(len(c) < 40 and not _is_heading(c) for c in L[j:j + n]) and not any(c in ("Traditional Schooling vs Homeschooling",) for c in L[j:j + n]):
            rows.append(L[j:j + n]); j += n
            if len(rows) >= 12: break
        part = []
        while j < len(L) and len(part) < n - 1 and L[j] and len(L[j]) < 40 and not _is_heading(L[j]) and not _is_subhead(L[j], L, j): part.append(L[j]); j += 1
        if len(part) >= 2: rows.append(part + ["—"] * (n - len(part)))
        elif part: j -= len(part)
        out.append("<table><thead><tr>" + "".join(f"<th>{_html.escape(h)}</th>" for h in hit) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{_html.escape(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")
        i = j
    return out
def render(text, skip=(), privacy=False, start=None, stop=None, toc=False):
    """Turn crawled text into clean HTML: headings, lists, paragraphs. Keeps every line (except skip/privacy)."""
    lines = text.split("\n")
    if lines and _re.search(r"[–-] American Group International|W25317017|[–-] Anglia Morocco\s*$", lines[0]): lines = lines[1:]
    if start: lines = lines[next((i for i, l in enumerate(lines) if start in l), 0):]
    if stop: lines = lines[:next((i for i, l in enumerate(lines) if stop in l), len(lines))]
    out, lst, heads = [], None, []
    seen_h2 = [False]
    paper_form = [False]
    def close():
        nonlocal lst
        if lst: out.append(f"</{lst}>"); lst = None
    lines = _runs_to_lists(_tableize(lines))
    for l_i, l in enumerate(lines):
        if l.startswith("<table"): close(); out.append('<div class="table-wrap">' + l + "</div>"); continue
        kind_, val_ = clean_line(l)
        if kind_ == "skip" or any(s in l for s in skip): continue
        if kind_ == "text" and (_re.search(r"_{3,}", val_) or _re.match(r"(?i)please (list|return)\b", val_)):
            if not paper_form[0]: close(); out.append('<p class="note">The application form is now online: <a href="forms.html#enrollment">apply on the forms page</a>.</p>'); paper_form[0] = True
            continue
        if kind_ == "html": close(); out.append(val_); continue
        l = val_
        if privacy and (_re.search(r"[\w.+-]+@[\w-]+\.\w+", l) and "americanecoleagadir" not in l or _re.search(r"(?:\+?212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}", l)): continue
        if _is_heading(l):
            close(); t = l.lstrip("#").strip(); lvl = 2 if (l.startswith("#") and len(l) - len(l.lstrip("#")) <= 2) or not l.startswith("#") else 3
            if len(t) > 90: out.append(f"<p><strong>{_html.escape(t)}</strong></p>"); continue
            hid = _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:50]
            if lvl == 3 and not seen_h2[0]: lvl = 2
            if lvl == 2: seen_h2[0] = True; heads.append((hid, t.title() if t.isupper() else t))
            out.append(f'<h{lvl} id="{hid}">{_html.escape(t.title() if t.isupper() else t)}</h{lvl}>'); continue
        if _is_subhead(l, lines, l_i):
            close(); tg = "h3" if seen_h2[0] else "h2"; seen_h2[0] = True; out.append(f"<{tg}>{_html.escape(l)}</{tg}>"); continue
        m = _BUL.match(l); n = _NUM.match(l)
        if m or n:
            kind = "ul" if m else "ol"
            if lst != kind: close(); out.append(f"<{kind}>"); lst = kind
            out.append(f"<li>{linkify(_html.escape(l[(m or n).end():]))}</li>"); continue
        close(); out.append(f"<p>{linkify(_html.escape(l))}</p>")
    close()
    body = "\n".join(out)
    body = _re.sub(r"<h3[^>]*>[^<]*</h3>\s*(?=<h[23][ >]|$)", "", body)                                      # h3 with nothing under it
    body = _re.sub(r"<h2[^>]*>[^<]*</h2>\s*$", "", body)                                                     # chapter titles followed by a section stay
    if toc and len(heads) >= 4:
        body = ('<nav class="toc" aria-label="On this page"><p class="kicker">On this page</p><ol>' + "".join(f'<li><a href="#{h}">{_html.escape(t)}</a></li>' for h, t in heads) + "</ol></nav>\n" + body)
    return body

FULLTEXT = lambda inner, label="Full text as published by AGI": f'<details class="fulltext"><summary>{label}</summary><div class="fulltext-body">{inner}</div></details>'
DOC_CSS = """
details.fulltext{border:1px solid var(--line);background:var(--paper);margin:8px 0 0}
details.fulltext summary{cursor:pointer;padding:16px 20px;font-weight:600;color:var(--navy);list-style:none}
details.fulltext summary::before{content:"+ ";color:var(--red)}details.fulltext[open] summary::before{content:"– "}
details.fulltext .fulltext-body{padding:4px 20px 20px;border-top:1px solid var(--line);background:#fff}
.doc{display:grid;grid-template-columns:minmax(0,1fr);max-width:820px}
.doc h2{font-family:var(--serif);font-weight:400;font-size:clamp(24px,2.2vw,30px);color:var(--navy);margin:1.8em 0 .5em;line-height:1.2}
.doc h3{font-family:var(--sans);font-weight:600;font-size:17px;color:var(--ink);margin:1.4em 0 .4em}
.doc p,.doc li{font-size:16px;line-height:1.75;color:var(--text)}
.doc ul,.doc ol{padding-left:22px;margin:0 0 1em}
.toc{border:1px solid var(--line);background:var(--paper);padding:20px 24px;margin:0 0 28px}
.toc ol{margin:0;padding-left:20px;columns:2;column-gap:32px}.toc li{font-size:14px;line-height:1.9;break-inside:avoid}
.source-note{font-size:13px;color:var(--grey);border-top:1px solid var(--line);padding-top:16px;margin-top:36px}
@media (max-width:700px){.toc ol{columns:1}}
"""
POLICY_LINKS = [("handbook.html", "Academic handbook"), ("attendance.html", "Attendance"), ("promotion-retention.html", "Promotion & retention"),
                ("placement-policy.html", "Provisional placement & assessment"), ("parent-responsibility.html", "Parent responsibility"),
                ("refunds-complaints.html", "Refunds & complaints"), ("media-policy.html", "Media"), ("homework.html", "Homework"),
                ("volunteer-hours.html", "Volunteer hours"), ("supplies.html", "School supplies list")]
def policy_page(name, title, lede, parts, desc):
    body = "".join(render(SRC(p)["text"], toc=(i == 0), privacy=True) for i, p in enumerate(parts))
    others = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in POLICY_LINKS if h != name)
    srcs = ", ".join(f'“{_html.escape(SRC(p)["title"])}” (former AGI website)' for p in parts)
    page(name, f"{title} – American Group International, Agadir", desc,
         hero(f'<a href="admissions.html">Admissions</a> / <a href="policies.html">Policies</a> / <span>{title}</span>', title, lede)
         + f'''<section class="section bg-white"><div class="wrap split">
  <div class="doc" data-verify="policy-text:{name}">{body}<p class="source-note">Text as published by AGI. Please check with the office for the current version. Source: {srcs}</p></div>
  <aside class="intro"><p class="kicker">All policies</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">{others}</ul>
    <p style="margin-top:24px"><a class="link" href="forms.html#enquiry/programs">Ask the office a question</a></p></aside>
</div></section>''', DOC_CSS)

policy_page("handbook.html", "Academic handbook", "AGI's mission, vision and beliefs, and the rules and routines that shape every school day – in full.",
            ["agi-academic-school-handbook"], "The AGI academic handbook in full: mission, vision, beliefs, school routines, behavior, communication and family partnership.")
policy_page("attendance.html", "Attendance", "Why attendance matters, what counts as excused, and what happens after unexcused absences or late arrivals.",
            ["attendance-policy", "importance-of-school-attendance"], "AGI attendance policy: 90% attendance for promotion, excused absences, late arrivals and consequences.")
policy_page("promotion-retention.html", "Promotion & retention", "How AGI decides promotion to the next grade, and the support offered when a student is retained.",
            ["promotion-and-retention"], "AGI promotion and retention policy: 64% in core subjects, 90% attendance, English assessment and summer remediation.")
policy_page("placement-policy.html", "Provisional placement & assessment", "How new students are assessed and placed – and why no child is moved down a grade for a language gap.",
            ["provisional-placement"], "AGI provisional placement and assessment policy: grade placement is not lowered for missing documents, language gaps or academic gaps.")
policy_page("parent-responsibility.html", "Parent responsibility", "What AGI asks of families, from the 90-day adjustment period to communication and payments.",
            ["parent-policy"], "AGI parent policy and responsibility: adjustment period, communication, safeguarding and fees.")
policy_page("refunds-complaints.html", "Refunds & complaints", "One procedure for all AGI divisions: enrollment, refunds, complaints and counseling.",
            ["policies-procedures"], "AGI policies and procedures for refunds and complaints across all divisions.")
policy_page("media-policy.html", "Media", "How photos, video and live streams of school events are used – always with consent and safeguarding first.",
            ["media-policy"], "AGI media policy: photos, video and live streams, consent for students under 18.")
policy_page("homework.html", "Homework", "How much homework to expect at each grade, and how families can help.",
            ["homework-guidelines"], "AGI homework guidelines: how many minutes of homework to expect each night, by grade, from kindergarten to grade 12.")
policy_page("volunteer-hours.html", "Volunteer hours", "Forty hours of service before graduation: what counts and how hours are recorded.",
            ["volunteer-hours"], "AGI in-service volunteer hours for high school: 40 hours, ten per year.")
policy_page("supplies.html", "School supplies list", "What to bring on the first day, for elementary and high school.",
            ["supplies-list"], "AGI school supplies list for elementary (K3–8) and high school (grades 9–12).")

DOC_CSS += """
.docwrap{display:grid;grid-template-columns:minmax(0,1fr) 260px;gap:clamp(32px,5vw,72px);align-items:start}
.docwrap aside{position:sticky;top:calc(var(--header) + 24px)}
.docwrap aside li a{font-size:14px}
.fee-table td:last-child,.fee-table th:last-child{text-align:right;white-space:nowrap}
.cal h3{font-family:var(--sans);font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--red);margin:26px 0 8px}
.cal table{min-width:0}.cal td:first-child{white-space:nowrap;font-weight:600;color:var(--navy);width:34%}
details.archive{border:1px solid var(--line);padding:4px 20px;background:var(--paper);margin-top:24px}
details.archive summary{cursor:pointer;padding:14px 0;font-weight:600;color:var(--navy)}
@media (max-width:900px){.docwrap{grid-template-columns:minmax(0,1fr)}.docwrap aside{position:static}}
"""
# policy pages: put the document in the wide column
for _n, _ in POLICY_LINKS:
    PAGES[_n] = PAGES[_n].replace('<section class="section bg-white"><div class="wrap split">\n  <div class="doc"', '<section class="section bg-white"><div class="wrap docwrap">\n  <div class="doc"', 1)

# ------------------------------------------------------------------ TUITION & FEES
_f = FACTS["fees"]; _ins = _f["inscription"]["value"]
_ins_rows = "".join(f"<tr><td>{g}</td><td><b>{v}</b></td></tr>" for g, v in _ins.items())
_fee_src = SRC("admission-fee")["text"]
page("fees.html", "Tuition & fees – American Group International, Agadir",
 "AGI fees 2026–27: inscription by grade (6,500–11,000 MAD), tuition 2,600 MAD a month, all-inclusive package, high school options, class prices.",
 hero('<a href="admissions.html">Admissions</a> / <span>Tuition &amp; fees</span>', "Tuition &amp; fees.",
      "Clear and simple: one annual inscription, ten monthly payments, and the essentials included. Fees are the same for every family – they are already set as low as possible.",
      APPLY + '<a class="btn btn-ghost" href="calendar.html">Calendar 2026–27</a>') + f"""
<section class="section bg-white" id="school"><div class="wrap docwrap"><div class="doc">
  <h2 style="margin-top:0">K–12 school</h2>
  <h3>Annual inscription (paid once a year at enrollment, non-refundable)</h3>
  <div class="table-wrap"><table class="fee-table"><thead><tr><th>Grade</th><th>Inscription</th></tr></thead><tbody>{_ins_rows}
    <tr><td>High school – American High School Online (LMS)</td><td><b>US$2,500</b></td></tr></tbody></table></div>
  <h3>Monthly tuition</h3>
  <p><b>2,600 MAD a month, paid over 10 months only</b> – 26,000 MAD for the school year.</p>
  <h3>All-inclusive education package</h3>
  <ul><li>Books and learning materials</li><li>Mathematics examinations</li><li>Anglia English examinations</li><li>Enrollment in the USA and Morocco</li><li>Student insurance coverage</li></ul>
  <h3>Summer school option (high school)</h3>
  <p>For students who need to catch up or enroll late: <b>3,000 MAD</b> for a one-month summer program.</p>
  <h2 id="high-school">High school options</h2>
  <p><b>Option 1 – High School Books Program, grades 9–12 (Florida accredited).</b> All students in grades 9 to 11 take the CAT assessment.</p>
  <p><b>Option 2 – High School Online in school, grades 9–12 (Cognia accredited).</b> Yearly inscription fee US$2,500 paid to a U.S. bank account; tuition 2,600 MAD a month.</p>
  <p>Grade 12 students pay a graduation fee, announced later – it may cover the diploma, apostille legalization, gown and shipping.</p>
  <h2 id="good-to-know">Good to know</h2>
  <ul><li>The inscription is annual and non-refundable.</li><li>Tuition is paid monthly over ten months.</li><li>Places are limited – secure your child's place early.</li>
    <li>Fees cannot be negotiated: they are already set as low as possible to keep AGI inclusive, and discounts are already applied for all families.</li>
    <li>A required Anglia English assessment takes place in April.</li></ul>
  <h2 id="requirements">Requirements at enrollment</h2>
  {render(_fee_src, start="All children enrolling", stop="Required Exam in April")}
  <p><a class="link" href="refunds-complaints.html">Refunds &amp; complaints policy</a> · <a class="link" href="attendance.html">Attendance policy</a></p>

  <h2 id="english">English &amp; Anglia classes</h2>
  <div class="table-wrap"><table class="fee-table"><thead><tr><th>Class</th><th>Price</th></tr></thead><tbody>
    <tr><td>Saturday classes, ages 5–18 (Saturdays 2–4 pm, October–June, yearly Anglia exam included)</td><td><b>500 MAD a month</b></td></tr>
    <tr><td>One-to-one (English or mathematics)</td><td><b>200 MAD a session</b></td></tr>
    <tr><td>Small group, 2–3 students</td><td><b>150 MAD per person, per session</b></td></tr>
    <tr><td>Group course, 4–10 students, 12 weeks</td><td><b>100 MAD a week (1,200 MAD)</b></td></tr>
    <tr><td>Level test</td><td><b>Free</b></td></tr></tbody></table></div>
  <p class="muted" style="font-size:13px">Prices effective November 2024. Books and insurance not included.</p>
  <h2 id="services">Other programs and services</h2>
  <div class="table-wrap"><table class="fee-table"><thead><tr><th>Service</th><th>Price</th></tr></thead><tbody>
    <tr><td>Exam proctoring</td><td><b>200 MAD (15 EUR) admin + 200 MAD (15 EUR) per exam hour</b></td></tr>
    <tr><td>USA private-school teacher sponsorship</td><td><b>US$60</b></td></tr>
    <tr><td>Holistic play therapy</td><td><b>{PH_TXT("price-play-therapy", "150 MAD per session")}</b></td></tr>
    <tr><td>Online tutoring (American Group USA)</td><td><b>{PH_TXT("price-online-tutoring", "US$10 – US$50 per session")}</b></td></tr>
    <tr><td>Independent course studies (per module)</td><td><b>{PH_TXT("price-modules", "US$49.95 / US$79.95")}</b></td></tr></tbody></table></div>
</div>
<aside><p class="kicker">Admissions</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">
  <li><a href="admissions.html">How to apply</a></li><li><a href="calendar.html">Calendar 2026–27</a></li><li><a href="policies.html">Policies</a></li><li><a href="forms.html#payment">Payment notice</a></li><li><a href="forms.html#enrollment">Apply</a></li></ul></aside>
</div></section>
""" + cta("Questions about fees?", "The office will explain every option for your family.", GOLD_APPLY + '<a class="btn btn-light" href="forms.html#enquiry/programs">Ask a question</a>'), DOC_CSS)

# ------------------------------------------------------------------ CALENDAR
_MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
def exam_table(text):
    rows, month, levels = [], None, []
    for l in text.split("\n"):
        t = l.strip().replace("▶", "").replace("\u25b6", "").strip()
        if not t or t.startswith("Anglia Exam Dates") or "EXAM DATES" in t or t.startswith("Book order"): continue
        if _re.fullmatch(f"({_MONTHS})", t): month, levels = t, []; continue
        if t.startswith("#"): levels.append(t.lstrip("# ").strip()); continue
        if _re.search(r"(Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day|^—$", t) and month:
            rows.append((month, ", ".join(levels) or "All levels", t)); levels = []; continue
        if t.startswith("*"): rows.append(("", "", t.lstrip("* "))); continue
    if not rows: return render(text)
    return ('<div class="table-wrap"><table><thead><tr><th>Month</th><th>Levels / session</th><th>Exam days</th></tr></thead><tbody>'
            + "".join(f"<tr><td>{_html.escape(m)}</td><td>{_html.escape(lv)}</td><td>{_html.escape(d)}</td></tr>" for m, lv, d in rows) + "</tbody></table></div>")

def cal_render(text, start, stop=None):
    lines = text.split("\n"); i = next((k for k, l in enumerate(lines) if start in l), 0)
    j = next((k for k, l in enumerate(lines) if stop and stop in l and k > i), len(lines)); out = []; rows = []
    def flush():
        if rows: out.append('<div class="table-wrap"><table><tbody>' + "".join(f"<tr><td>{_html.escape(a)}</td><td>{_html.escape(b)}</td></tr>" for a, b in rows) + "</tbody></table></div>"); rows.clear()
    for l in lines[i + 1:j]:
        l = l.strip()
        if not l: continue
        mm = _re.match(r"^(January|February|March|April|May|June|July|August|September|October|November|December|[A-Z]{3,})(\s+\d{4})?$", l)
        if mm: flush(); out.append(f"<h3>{_html.escape(l.title())}</h3>"); continue
        parts = _re.split(r"\s+[–—-]\s+", l, maxsplit=1)
        if len(parts) == 1: parts = _re.split(r"(?<=\d)-\s*", l, maxsplit=1)
        if len(parts) == 2 and _re.search(r"\d", parts[0]): rows.append((parts[0], parts[1]))
        else: flush(); out.append(f"<p>{_html.escape(l)}</p>")
    flush(); return "\n".join(out)
_cal = SRC("school-calandar")["text"]
page("calendar.html", "Calendar 2026–27 – American Group International, Agadir",
 "AGI school calendar 2026–27: registration Aug 28 & 31, first day Sept 7, holidays and breaks, last day June 17; Saturday classes and Anglia exam sessions.",
 hero('<a href="admissions.html">Admissions</a> / <span>Calendar</span>', "Calendar 2026–27.",
      "Every school day, holiday and break, plus Saturday classes and Anglia exam sessions. Religious holidays are movable and confirmed nearer the date.",
      APPLY + '<a class="btn btn-ghost" href="fees.html">Tuition &amp; fees</a>') + f"""
<section class="section bg-white" id="school-year"><div class="wrap docwrap"><div class="doc cal">
  <h2 style="margin-top:0">School year 2026–27</h2>
  {cal_render(_cal, "2026–2027 ACADEMIC CALENDAR", "July 2027")}
  <h2 id="ahead">Looking ahead: 2027–28</h2>
  {cal_render(_cal, "July 2027")}
  <h2 id="saturday">Saturday Anglia classes</h2>
  <p>{PH_TXT("saturday-2026-27", "The 2026–27 Saturday schedule will be published here.")} The 2025–26 schedule is below for reference.</p>
  <details class="archive"><summary>Saturday classes 2025–26</summary>{render(SRC("saturday-classes-yearly-schedule")["text"])}</details>
  <h2 id="anglia-exams">Anglia exam sessions 2026</h2>
  {exam_table(SRC("anglia-exam-dates")["text"])}
  <p><a class="link" href="english-anglia.html">English &amp; Anglia exams</a></p>
  <details class="archive"><summary>Archive: school calendar 2025–26</summary>{render(_cal, stop="AMERICAN GROUP INTERNATIONAL")}</details>
</div>
<aside><p class="kicker">Key dates</p><dl class="rows" style="border-top:0">
  <div><dt>Registration</dt><dd>Aug 28 &amp; 31</dd></div><div><dt>First day</dt><dd>Sept 7</dd></div><div><dt>Last day &amp; graduation</dt><dd>June 17, 2027</dd></div></dl>
  <p><a class="link" href="forms.html#visit">Book a visit</a></p></aside>
</div></section>""", DOC_CSS)

# ------------------------------------------------------------------ SPECIAL EDUCATION: full source text (private contact details filtered)
_se = render(SRC("location-physical")["text"], privacy=True, stop="Dear Mrs")      # the parent letter that follows names a child: hidden until written consent
PAGES["special-education.html"] = PAGES["special-education.html"].replace("\n</main>", f'''
<section class="section bg-white" id="details"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">Special education services in detail</h2>{FULLTEXT(_se)}</div>
<aside><p class="kicker">Related</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="placement-policy.html">Placement policy</a></li><li><a href="parents.html">For parents</a></li><li><a href="forms.html#visit">Book a visit</a></li></ul></aside></div></section>
</main>''', 1)

PAGES["special-education.html"] = PAGES["special-education.html"].replace("</head>", f"<style>{DOC_CSS}</style>\n</head>", 1)

# ------------------------------------------------------------------ POLICIES INDEX: link every full text
PAGES["policies.html"] = PAGES["policies.html"].replace("\n</main>", '''
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Read the full texts</h2><p>Every policy as published by AGI.</p></div>
  <div class="cards">''' + "".join(f'<a class="card" href="{h}"><h3>{t}</h3><span class="more">Read</span></a>' for h, t in POLICY_LINKS) + '''</div>
</div></section>
</main>''', 1)

# ------------------------------------------------------------------ FAQ HUB (every answer from a source page; unconfirmed items marked)
FAQ = [
 ("Admissions", [
  ("Who can enroll at AGI?", "Children aged 5 by September 1 (kindergarten) up to students under 21 on the first day of school. AGI admits students of any race, religion, color, national or ethnic origin.", "admissions.html"),
  ("What documents do we need?", "Proof of age (birth certificate, passport or similar), proof of residency less than three months old, immunization and physical examination records, two years of previous school records with a behavior report, three recent photos, and transfer papers translated into English.", "admissions.html"),
  ("How does the admissions process work?", "1) Application with the non-refundable enrollment deposit, 2) an interview with parent and child, 3) an offer of admission and the tuition agreement.", "admissions.html"),
  ("Is there an entrance test?", "Yes – a free placement assessment in English and academic subjects. Grade placement is not lowered due to missing documents, language gaps, or academic gaps.", "placement-policy.html"),
  ("Can my child join in the middle of the year?", "Yes. Students are welcome at any stage; they sit the placement assessment and start with the right support.", "parents.html"),
  ("My child doesn't speak English yet. Can they join?", "Yes. Students join their age group with English as a second language support and are benchmarked on the CEFR with Anglia exams.", "placement-policy.html"),
  ("Do you support children with special needs?", "Yes: Individualized Education Plans, small-group classes and therapy and behavioral support. Documentation from a licensed practitioner is required – a parent's description alone is not enough.", "special-education.html")]),
 ("Fees", [
  ("How much is tuition?", "2,600 MAD a month, paid over ten months (26,000 MAD a year).", "fees.html"),
  ("How much is the annual inscription?", "Kindergarten–grade 1: 6,500 MAD · grades 2–6: 7,500 MAD · grades 7–8: 7,800 MAD · grades 9–11: 10,000 MAD · grade 12: 11,000 MAD. Paid once a year, non-refundable.", "fees.html"),
  ("What is included?", "Books and learning materials, mathematics examinations, Anglia English examinations, enrollment in the USA and Morocco, and student insurance.", "fees.html"),
  ("Can fees be negotiated?", "No. Fees are already set as low as possible to keep AGI inclusive, and discounts are already applied for all families.", "fees.html"),
  ("Is there a summer school?", "Yes, for high school students who need to catch up or enroll late: 3,000 MAD for a one-month program.", "fees.html"),
  ("Is there a discount for brothers and sisters?", PH_TXT("faq-hub-siblings", "To be confirmed by the office."), "fees.html")]),
 ("School life", [
  ("When does the school year start and end?", "2026–27: registration days August 28 and 31, first day September 7, last day and graduation June 17, 2027.", "calendar.html"),
  ("What are the school hours?", PH_TXT("faq-hub-hours", "To be confirmed by the office.") + " Arrival after 9:00 counts as late, and after 10:00 as an absence.", "attendance.html"),
  ("Is there a uniform?", PH_TXT("faq-hub-uniform", "No uniform is mentioned; a dress code applies (see the handbook)."), "handbook.html"),
  ("What happens if my child is absent?", "Give the office a dated, signed excuse within two days. Students need 90% attendance to be promoted; unexcused absences lead to escalating consequences.", "attendance.html"),
  ("How is promotion decided?", "At least 64% (D) in each core subject, 90% attendance, maturity and the English assessment; summer remediation is possible.", "promotion-retention.html"),
  ("How much homework is there?", "From 10–20 minutes a night in kindergarten to 2–3 hours in the last years of high school.", "homework.html"),
  ("What do high school students need to graduate?", "Among other requirements, 40 volunteer hours – ten each year.", "volunteer-hours.html"),
  ("What should my child bring?", "See the school supplies list for elementary and high school.", "supplies.html")]),
 ("Anglia exams & English", [
  ("What are Anglia exams?", "English exams from Anglia Examinations, based in Chichester, England, since 1993 and part of Chichester College Group. They test reading, writing, listening and speaking at ten levels, from First Step to Masters (C2).", "english-anglia.html"),
  ("From what age can my child take them?", "From about four years old; there is no upper age limit.", "english-anglia.html"),
  ("How long are the exams?", "Reading and writing 1–3 hours, listening 10–30 minutes, speaking about 5–20 minutes, depending on the level.", "english-anglia.html"),
  ("Does the certificate expire?", "It is valid for life, though an institution may ask for a recent one.", "english-anglia.html"),
  ("When are the exam sessions?", "There are sessions in most months – see the 2026 exam sessions on the calendar. Other dates are possible on request.", "calendar.html"),
  ("Can candidates with dyslexia or a disability get support?", "Yes – for example extra time, supervised breaks, Braille or large print, wheelchair access or a scribe.", "english-anglia.html"),
  ("Are Saturday classes available?", "Yes: ages 5–18, Saturdays 2–4 pm, October to June, 500 MAD a month including the yearly Anglia exam, with BAC, TOEFL, IELTS, SAT and Mathematics-in-English preparation.", "english-anglia.html")]),
 ("Teachers & adults", [
  ("What is C.I.T.E.?", "Anglia's Certificate for International Teachers of English: a TESOL qualification mapped to the CEFR, with no entry qualifications and lifelong validity.", "teachers.html"),
  ("Can I teach in the United States?", "AGI offers certification sponsorship for U.S. private schools: bachelor's degree, clear background check and a sponsoring school; fee US$60. Not valid for public schools.", "teachers.html"),
  ("Can adults finish high school?", "Yes, from age 16 with American Worldwide Academy; every test is proctored in Agadir and graduation requires 80%.", "adult-diploma.html"),
  ("Do you proctor exams for other institutions?", "Yes, Monday to Thursday 9:00–17:00: a 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour.", "professional.html")]),
]
FAQ_LBL = {'admissions.html': 'Admissions', 'placement-policy.html': 'Placement policy', 'parents.html': 'For parents', 'special-education.html': 'Special education', 'fees.html': 'Tuition & fees', 'calendar.html': 'Calendar 2026–27', 'attendance.html': 'Attendance policy', 'handbook.html': 'Academic handbook', 'promotion-retention.html': 'Promotion & retention', 'homework.html': 'Homework guidelines', 'volunteer-hours.html': 'Volunteer hours', 'supplies.html': 'Supplies list', 'english-anglia.html': 'English & Anglia exams', 'teachers.html': 'For teachers', 'adult-diploma.html': 'Adult diploma', 'professional.html': 'Professional services'}
_faq_html = "".join(f'<h2 id="{_re.sub(r"[^a-z]+", "-", g.lower()).strip("-")}">{g}</h2><div class="faq">' + "".join(
    f'<details><summary>{q}</summary><p>{a} <a class="link" href="{l}">{FAQ_LBL.get(l, "Read more about this")}</a></p></details>' for q, a, l in qs) + "</div>" for g, qs in FAQ)
_faq_ld = _json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _re.sub(r"<[^>]+>", "", a)}} for _, qs in FAQ for q, a, _l in qs if "ph-text" not in a]}, ensure_ascii=False)
page("faq.html", "Questions & answers – American Group International, Agadir",
 "Answers to parents' questions about AGI: admissions, documents, fees, calendar, attendance, homework, Anglia exams, teachers and adult programs.",
 hero("<span>Questions &amp; answers</span>", "Questions &amp; answers.", "The questions families ask most, with answers taken from AGI's own policies and programs.",
      '<a class="btn btn-primary" href="forms.html#enquiry">Ask another question</a>' + WA)
 + f'<section class="section bg-white"><div class="wrap docwrap"><div class="doc">{_faq_html}</div>'
   '<aside><p class="kicker">Topics</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">'
 + "".join(f'<li><a href="#{_re.sub(r"[^a-z]+", "-", g.lower()).strip("-")}">{g}</a></li>' for g, _ in FAQ)
 + f'</ul></aside></div></section><script type="application/ld+json">{_faq_ld}</script>', DOC_CSS + FAQ_CSS)

# ------------------------------------------------------------------ static pages: full source texts (between markers, rebuilt every run)
def inject_static(fname, key, inner):
    fp = os.path.join(V2, fname); t = open(fp, encoding="utf-8", newline="").read()
    inner = split_languages('<main>' + inner, fname)[len('<main>'):]
    blk = f"<!--p1:{key}-->\n{inner}\n<!--/p1:{key}-->"
    t = _re.sub(r"<!--p1:%s-->.*?<!--/p1:%s-->\n?" % (key, key), "", t, flags=re.S)
    if "<style id=\"doc-css\">" not in t: t = t.replace("</head>", f'<style id="doc-css">{DOC_CSS}</style>\n</head>', 1)
    t = t.replace("</main>", blk + "\n</main>", 1)
    open(fp, "w", encoding="utf-8", newline="").write(t)
if False: inject_static("admissions.html", "full", '<section class="section bg-white np" id="procedure"><div class="wrap docwrap"><div class="doc">'
  + '<h2 style="margin-top:0">In AGI&rsquo;s own words</h2><p>The steps above summarize the procedure. Here is the full text, and the full list of enrollment documents.</p>'
  + FULLTEXT(render(SRC("admissions-procedure")["text"]) + render(SRC("admission-prossess")["text"]), "The admissions procedure in full")
  + FULLTEXT(render(SRC("/enrollment")["text"], stop="rification de l"), "Enrollment documents in full") + '</div><aside><p class="kicker">Next steps</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">'
  + '<li><a href="fees.html">Tuition &amp; fees</a></li><li><a href="calendar.html">Calendar 2026–27</a></li><li><a href="placement-policy.html">Placement policy</a></li><li><a href="forms.html#enrollment">Apply</a></li><li><a href="faq.html">Questions &amp; answers</a></li></ul></aside></div></section>')
import csv as _csv
_MAP = list(_csv.DictReader(open(os.path.join(os.path.dirname(V2), "docs", "content-map.csv"), encoding="utf-8-sig")))
def MAPPED(dest): return [r["url"] for r in _MAP if r["destination"] == dest and r["action"] != "drop"]
_k12_src = MAPPED("k12.html")
if False: inject_static("k12.html", "full", '<section class="section bg-white np" id="about-the-school"><div class="wrap docwrap"><div class="doc">'
  + '<h2 style="margin-top:0">About the school in detail</h2>' + FULLTEXT("".join(render(SRC(u)["text"], privacy=True) for u in _k12_src))
  + '</div><aside><p class="kicker">Related</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="handbook.html">Academic handbook</a></li><li><a href="supplies.html">Supplies list</a></li><li><a href="homework.html">Homework</a></li><li><a href="fees.html#high-school">High school options</a></li></ul></aside></div></section>')

# ================================================================== PHASE 2 – ANGLIA MOROCCO
_CRAWL = os.path.join(os.path.dirname(V2), "data", "crawl")
ANGLIA_NAV = [("anglia.html", "Anglia Morocco"), ("anglia-exams.html", "Exams & levels"), ("calendar.html#anglia-exams", "Exam dates 2026"),
              ("anglia-cefr.html", "CEFR levels"), ("anglia-practice.html", "Practice papers & audio"), ("anglia-books.html", "Step To books"),
              ("anglia-special-arrangements.html", "Special arrangements"), ("anglia-placement-test.html", "Free placement assessment"),
              ("anglia-classes.html", "Classes & prices"), ("anglia-network.html", "Network & centres"), ("partnerships.html", "Become a centre"),
              ("anglia-faq.html", "Anglia FAQ"), ("anglia-about.html", "About Anglia Examinations"), ("teachers.html#cite", "C.I.T.E. for teachers")]
def anglia_page(name, title, lede, body, desc, crumb=None):
    nav = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == name else ""}>{t}</a></li>' for h, t in ANGLIA_NAV if h != name)
    page(name, f"{title} – Anglia Morocco | AGI Agadir", desc,
         hero(f'<a href="anglia.html">Anglia Morocco</a> / <span>{crumb or title}</span>' if name != "anglia.html" else "<span>Anglia Morocco</span>", title, lede,
              '<a class="btn btn-primary" href="forms.html#enquiry/anglia">Book a free level test</a><a class="btn btn-ghost" href="calendar.html#anglia-exams">Exam dates</a>')
         + f'<section class="section bg-white"><div class="wrap docwrap"><div class="doc">{body}</div>'
           f'<aside><p class="kicker">Anglia Morocco</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">{nav}</ul>'
           f'<p style="margin-top:22px;font-size:13px" class="muted">Anglia Morocco headquarters: AGI, Agadir · <a href="mailto:j.wilburn@angliamorocco.org">j.wilburn@angliamorocco.org</a> · <a href="mailto:a.lam@angliamorocco.org">a.lam@angliamorocco.org</a></p></aside></div></section>', DOC_CSS)

def srcs_for(dest): return [SRC(u) for u in MAPPED(dest)]
def full(dest, skip=(), heading="In detail"):
    body = "".join(render(p["text"], skip=skip, privacy=True) for p in srcs_for(dest) if p["text"])
    return (f"<h2>{heading}</h2>" if heading and not body.lstrip().startswith("<h") else "") + body

LEVELS = [("First Step", "YL", "Entry level from about age 4: understands about 100 words, follows basic classroom instructions, says who they are."),
 ("Junior", "YL", "Understands around 200 words, uses useful structures and explains what they are doing."),
 ("Primary", "YL", "About 400 words (jobs, feelings, weather); forms questions, answers them and describes things."),
 ("Preliminary", "A1", "First general level for young and adult learners."), ("Elementary", "A2", "Everyday situations and simple texts."),
 ("Pre-Intermediate", "A2+", "Wider everyday communication."), ("Intermediate", "B1", "Independent use in familiar contexts."),
 ("Advanced", "B2", "Complex texts and fluent interaction."), ("Proficiency", "C1", "Effective operational proficiency."),
 ("Masters", "C2", "Expert user. The Mastery qualification carries UCAS tariff points.")]
BUSINESS = [("Practical Business English", "A2+"), ("Intermediate Business English", "B1"), ("Advanced Business English", "B2"), ("Proficiency in Business English", "C1")]
_lv = "".join(f"<tr><td><b>{n}</b></td><td>{c}</td><td>{d}</td></tr>" for n, c, d in LEVELS)
_bz = "".join(f"<tr><td><b>{n}</b></td><td>{c}</td></tr>" for n, c in BUSINESS)
anglia_page("anglia-exams.html", "Anglia exams &amp; levels",
 "Ten General English levels from First Step to Masters (C2), four Business English levels, and online exams – each testing listening, reading, writing and speaking.",
 f'''<h2 style="margin-top:0">General English – ten levels</h2>
 <div class="table-wrap"><table><thead><tr><th>Level</th><th>CEFR</th><th>What candidates can do</th></tr></thead><tbody>{_lv}</tbody></table></div>
 <p>Young-learner levels are also open to adults, so anyone can start step by step. There is no upper age limit.</p>
 <h2>Business English – four levels</h2><div class="table-wrap"><table><thead><tr><th>Exam</th><th>CEFR</th></tr></thead><tbody>{_bz}</tbody></table></div>
 <h2>How long are the exams?</h2><ul><li>Reading and writing: 1 hour minimum, 3 hours maximum, depending on the level</li><li>Listening: 10–30 minutes</li><li>Speaking: about 5–20 minutes</li></ul>
 <p>The certificate is valid for life; an institution may ask for a recent one. <a class="link" href="calendar.html#anglia-exams">Exam dates 2026</a></p>''' + full("anglia-exams.html"),
 "Anglia exams in Morocco: ten General English levels (First Step to Masters C2), Business English A2+ to C1, durations and online exams.", "Exams &amp; levels")

anglia_page("anglia-cefr.html", "CEFR levels", "How the Common European Framework of Reference describes language ability – and how AGI students progress through it.",
 '<p style="margin-top:0"><a class="link" href="english-anglia.html#cefr">English benchmarks at AGI by grade</a></p>' + full("anglia-cefr.html", heading="The CEFR explained"),
 "The CEFR levels A1 to C2 explained, and benchmarks for native speakers and language learners at AGI.")

# special arrangements: list + disability codes table
_sa = SRC("special-arrangements")["text"]; _codes = _re.findall(r"\n([A-Za-z][^\n]{2,60})\n(D\d)\b", _sa)
_sa_tbl = '<div class="table-wrap"><table><thead><tr><th>Need</th><th>Code</th></tr></thead><tbody>' + "".join(f"<tr><td>{_html.escape(a.strip(' /'))}</td><td><b>{b}</b></td></tr>" for a, b in _codes) + "</tbody></table></div>" if _codes else ""
anglia_page("anglia-special-arrangements.html", "Special arrangements", "Exams should be accessible to everyone. Candidates with learning or physical difficulties – or an injury on the day – can ask for support.",
 render(_sa, stop="Explanation the D") + ("<h2>Disability codes</h2><p>Use these codes when you request special arrangements.</p>" + _sa_tbl if _sa_tbl else "")
 + '<p><a class="btn btn-primary" href="forms.html#enquiry/anglia">Request special arrangements</a></p>',
 "Special arrangements for Anglia exams in Morocco: extra time, breaks, Braille or large print, wheelchair access, scribe, lip reading; codes D1–D8.")

# practice packs from the original page's download links
_raw = open(os.path.join(_CRAWL, "anglia", "practice-resources.html"), encoding="utf-8", errors="ignore").read()
_links = []
for h, t in _re.findall(r'<a[^>]+href="(https?://[^"]+\.(?:zip|pdf))"[^>]*>(.*?)</a>', _raw, _re.S | _re.I):
    t = _re.sub(r"<[^>]+>|\s+", " ", t).strip()
    if not t or t.lower() in ("download", "click here", "here"): t = _re.sub(r"[-_]+", " ", _re.sub(r"\.(zip|pdf)$|-[a-z]{2}\d+$", "", h.rsplit("/", 1)[-1], flags=_re.I)).strip().title()
    if t and (h, t) not in _links: _links.append((h, t))
import csv as _csv2
_dead = set()
_xp = os.path.join(os.path.dirname(V2), "docs", "external-links.csv")
if os.path.exists(_xp): _dead = {r["url"] for r in _csv2.DictReader(open(_xp, encoding="utf-8-sig")) if r["status"] == "BROKEN"}
_dj = os.path.join(V2, "_build", "dead-links.json")
if os.path.exists(_dj): _dead |= set(_json.load(open(_dj, encoding="utf-8-sig")))   # links known to be dead stay excluded
_missing_levels = sorted({next((L for L, _, _ in LEVELS if L.lower().replace(" ", "-") in h.lower()), "Other") for h, t in _links if h in _dead})
_links = [(h, t) for h, t in _links if h not in _dead]
_groups = {}
for h, t in _links:
    lv = next((L for L, _, _ in LEVELS if L.lower().replace(" ", "-") in h.lower() or L.lower() in t.lower()), "Other")
    _groups.setdefault(lv, []).append((h, t))
_pk = "".join(f"<h3>{lv}</h3><ul>" + "".join(f'<li><a href="{h}" rel="noopener">{_html.escape(t)}</a></li>' for h, t in L) + "</ul>" for lv, L in _groups.items())
_audio = "".join(f'<li><a href="{h}" rel="noopener">{lab}</a></li>' for h, lab in [
    ("https://www.anglia.nl/uploads/1/2/0/0/120044573/audiofiles_step_to_fs_-_pre-intermediate__1_.zip", "Step To audio files: First Step to Pre-Intermediate"),
    ("https://www.anglia.nl/uploads/1/2/0/0/120044573/audoifiles_step_to_intermediate_-_masters__1_.zip", "Step To audio files: Intermediate to Masters")])
anglia_page("anglia-practice.html", "Practice papers &amp; audio", "Free sample papers for every level, published by Anglia Examinations, plus the audio files for the Step To books.",
 render(SRC("practice-resources")["text"], stop="Pick Your Level") + f"<h2>Practice packs by level</h2>{_pk or '<p>Download links are on angliamorocco.org.</p>'}" + (f'<p class="note">Practice packs for {", ".join(_missing_levels)} are not available online at the moment. <a href="forms.html#enquiry/anglia">Ask Anglia Morocco</a> for a copy.</p>' if _missing_levels else "") + f"<h2>Audio files</h2><ul>{_audio}</ul>"
 + full("anglia-practice.html", skip=("Pack", "First Step", "Junior", "Primary", "Preliminary", "Elementary", "Intermediate", "Advanced", "CLICK TO DOWNLOAD")),
 "Free Anglia practice papers for every level (First Step to Advanced, Business English) and Step To audio files.")

anglia_page("anglia-books.html", "Step To books", "Preparation books for each Anglia level, with audio files – order through Anglia Morocco.",
 full("anglia-books.html", heading="Step To books") + f'<h2>Audio files</h2><ul>{_audio}</ul><p><a class="btn btn-primary" href="forms.html#books">Order books</a></p>',
 "Anglia Step To preparation books for every level, audio files and how to order in Morocco.")

anglia_page("anglia-placement-test.html", "Free placement assessment", "Find your English level on the CEFR before you choose a class or an Anglia exam.",
 '''<h2 style="margin-top:0">How it works</h2><ol><li>Book your free assessment online or by WhatsApp.</li><li>Take the assessment at AGI in Agadir: reading, listening, writing and a short conversation.</li><li>Get your CEFR level and a recommendation: a class, a learning pod or the right Anglia exam.</li></ol>
<p><a class="btn btn-primary" href="forms.html#enquiry/anglia">Book my free assessment</a></p>
<h2>Want to practice first?</h2><p>Try the official Anglia sample papers for your level. <a class="link" href="anglia-practice.html">Practice papers</a></p>''',
 "Free English placement assessment on the CEFR at Anglia Morocco headquarters in Agadir.", "Placement assessment")

_cls = full("anglia-classes.html", heading="Our English classes")
anglia_page("anglia-classes.html", "Classes &amp; prices", "One-to-one lessons, small groups, 12-week courses and Saturday classes for children and teens – with a free level test first.",
 '''<h2 style="margin-top:0">Prices</h2><div class="table-wrap"><table class="fee-table"><thead><tr><th>Class</th><th>Price</th></tr></thead><tbody>
 <tr><td>Saturday classes, ages 5–18, Saturdays 2–4 pm, October–June, yearly exam included; BAC, TOEFL, IELTS, SAT and Mathematics-in-English preparation</td><td><b>500 MAD a month</b></td></tr>
 <tr><td>One-to-one (English or mathematics)</td><td><b>200 MAD a session</b></td></tr><tr><td>Small group, 2–3 students</td><td><b>150 MAD per person</b></td></tr>
 <tr><td>Group course, 4–10 students, 12 weeks</td><td><b>1,200 MAD</b></td></tr><tr><td>Level test</td><td><b>Free</b></td></tr></tbody></table></div>
 <p class="muted" style="font-size:13px">Prices effective November 2024; books and insurance not included. <a href="calendar.html#saturday">Saturday schedule</a></p>''' + _cls,
 "English classes at Anglia Morocco, Agadir: one-to-one 200 MAD, small groups, 12-week courses 1,200 MAD, Saturday classes 500 MAD a month.", "Classes &amp; prices")

# network: regions and provinces; no political text (claims register #11)
_POL = ("Sahrawi", "United Nations", "disputed", "de facto", "See also", "annex", "Polisario", "self-determination", "auto determined", "legal instruments", "Western Sahara")
anglia_page("anglia-network.html", "Network &amp; centres", "From its Agadir headquarters, Anglia Morocco works with schools, language centres and teachers across the Kingdom's twelve regions.",
 '<p style="margin-top:0">Main headquarters: AGI, Agadir · Sales coordinator: Abdelhak Lam. Partnerships are available – regions marked "Representative available" are looking for a local partner.</p>'
 + render(SRC("angliamorocco-networks-and-centers-12-regions")["text"], skip=_POL + ("Country Manager",))
 + '<p><a class="btn btn-primary" href="partnerships.html">Become an Anglia centre</a></p>',
 "Anglia Morocco network across the 12 regions of Morocco: provinces, centres and open representative positions.", "Network &amp; centres")

anglia_page("anglia-faq.html", "Anglia FAQ", "Answers about Anglia exams – levels, ages, durations and certificates.",
 '''<div class="faq">
 <details><summary>What are the Anglia exams?</summary><p>Official English certificates from Anglia Examinations (Chichester, England, since 1993; part of Chichester College Group). They evaluate reading, listening, speaking and writing, from initiation to expertise, helping students reach the level they want step by step.</p></details>
 <details><summary>Which levels do they certify?</summary><p>10 levels in three groups – young learners (First Step, Junior, Primary, Preliminary), intermediate (Elementary, Pre-Intermediate, Intermediate) and higher (Advanced, Proficiency, Masters) – plus Business English levels with business vocabulary.</p></details>
 <details><summary>How long do the exams last?</summary><p>Reading and writing: 1 hour minimum and 3 hours maximum depending on the level. Listening: 10 to 30 minutes. Speaking: about 5 to 20 minutes.</p></details>
 <details><summary>Who can take them?</summary><p>Anyone: students of all ages from 4 years onwards, with no upper age limit. You can start at the level you or your teacher consider appropriate.</p></details>
 <details><summary>Do I need extra classes?</summary><p>No – preparation is built into the classroom curriculum. Classes at AGI are available if you want them.</p></details>
 <details><summary>Does the certificate expire?</summary><p>It lasts for life, but an institution may ask for a recent one if yours is very old.</p></details>
 <details><summary>How do I know which level to take?</summary><p>Take the free placement assessment; Anglia also offers an additional exam that determines your level.</p></details>
 <details><summary>Are Anglia certificates recognized by universities?</summary><p>The Mastery (C2) qualification carries UCAS tariff points for UK universities. ''' + PH_TXT("anglia-faq-recognition", "Further recognition statements to be confirmed with Anglia.") + '''</p></details>
 <details><summary>Are they affordable?</summary><p>Anglia exams are priced affordably compared with other international certificates.</p></details></div>''',
 "Anglia exams FAQ: levels, ages from 4, durations, lifetime certificates, UCAS tariff points for Mastery.")

anglia_page("anglia-about.html", "About Anglia Examinations", "Anglia Examinations has tested English since 1993 from Chichester, England. AGI has been the franchise holder for Morocco since 2021.",
 '<p style="margin-top:0">Anglia Examinations is a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding. The four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual.</p>'
 + full("anglia-about.html", heading="More about Anglia"), "About Anglia Examinations: Chichester since 1993, Chichester College Group, AIM and Ofqual, Anglia Morocco since 2021.", "About Anglia")

_home = _INV.get("https://angliamorocco.org/", {"text": "", "url": "", "title": ""})
_cards = "".join(f'<a class="card" href="{h}"><h3>{t}</h3><span class="more">Open</span></a>' for h, t in ANGLIA_NAV[1:])
page("anglia.html", "Anglia Morocco – English exams and classes | AGI Agadir",
 "Anglia Morocco headquarters at AGI, Agadir: Anglia English exams from First Step to Masters, exam dates, practice papers, classes and a network across 12 regions.",
 hero("<span>Anglia Morocco</span>", "Anglia Morocco.", "Official English exams from England, from a child's first words to Masters (C2) – with classes, practice papers and centres across Morocco's twelve regions.",
      '<a class="btn btn-primary" href="forms.html#enquiry/anglia">Book a free level test</a><a class="btn btn-ghost" href="calendar.html#anglia-exams">Exam dates 2026</a>')
 + f'''<section class="section bg-white"><div class="wrap"><h2 class="visually-hidden">Anglia Morocco pages</h2><div class="cards">{_cards}</div></div></section>
<section class="section"><div class="wrap docwrap"><div class="doc">{render(_home["text"], privacy=True)}
<h2>Club Anglia</h2><p>{PH_TXT("club-anglia", "Coming soon.")}</p>
<p><a class="link" href="https://angliamorocco.org/" target="_blank" rel="noopener">angliamorocco.org</a></p></div>
<aside><p class="kicker">Contacts</p><p class="muted" style="font-size:14px">Julie Wilburn · <a href="mailto:j.wilburn@angliamorocco.org">j.wilburn@angliamorocco.org</a><br>Abdelhak Lam · <a href="mailto:a.lam@angliamorocco.org">a.lam@angliamorocco.org</a></p></aside></div></section>''', DOC_CSS)

# partnerships (static page): full source text
if False: inject_static("partnerships.html", "full", '<section class="section bg-white np" id="partner-with-us"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">Partner with AGI and Anglia Morocco</h2>'
  + FULLTEXT("".join(render(SRC(u)["text"], privacy=True) for u in MAPPED("partnerships.html"))) + '</div><aside><p class="kicker">Anglia Morocco</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="anglia-network.html">Network &amp; centres</a></li><li><a href="anglia.html">Anglia Morocco</a></li><li><a href="investors.html">Partners &amp; investors</a></li></ul></aside></div></section>')

# ================================================================== PHASE 3 – TEACHERS · ADULTS · WELLBEING · ONLINE · PATHWAYS
GROUPS = {
 "Teachers": [("teachers.html", "For teachers"), ("teachers-cite.html", "C.I.T.E. / TESOL certification"), ("teachers-usa-sponsorship.html", "USA private-school sponsorship"), ("teachers-careers.html", "Teach with AGI")],
 "Adults & professionals": [("adult-diploma.html", "Adult high school diploma"), ("programs-independent-studies.html", "Independent course studies"), ("professional.html", "Business & medical English"),
                            ("programs-learning-pods.html", "Learning pods & fast track"), ("services-document-editing.html", "Document editing"), ("services-proctoring.html", "Exam proctoring")],
 "Wellbeing (i-Heart)": [("wellbeing.html", "i-Heart therapeutic services"), ("wellbeing-adhd-coaching.html", "ADHD holistic coaching"), ("wellbeing-play-therapy.html", "Holistic play therapy")],
 "Online": [("online-tutoring.html", "Online tutoring"), ("agi-usa.html", "American Group USA LLC")],
 "Pathways": [("pathways.html", "University pathways")],
}
def section_page(name, group, title, lede, intro_html, desc, buttons=None, crumb=None):
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in GROUPS[group] if h != name)
    page(name, f"{title} – American Group International, Agadir", desc,
         hero(f'<a href="programs.html">Programs</a> / <span>{crumb or title}</span>', title, lede,
              buttons or ('<a class="btn btn-primary" href="forms.html#enquiry/programs">Ask about this program</a>' + WA))
         + f'<section class="section bg-white"><div class="wrap docwrap"><div class="doc">{intro_html}{full(name)}</div>'
           f'<aside><p class="kicker">{group}</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">{links}</ul>'
           f'<p style="margin-top:22px"><a class="link" href="fees.html#services">Prices</a></p></aside></div></section>', DOC_CSS)

section_page("teachers-cite.html", "Teachers", "C.I.T.E. / TESOL certification",
 "Anglia's Certificate for International Teachers of English: recognition of your English and your teaching – for life.",
 '<p style="margin-top:0"><a class="btn btn-primary" href="https://angliamorocco.org/citem/" target="_blank" rel="noopener">Register on angliamorocco.org</a></p>',
 "Anglia C.I.T.E. (TESOL) certification in Morocco: who it is for, English level needed, preparation, when and how to take it.", crumb="C.I.T.E.")
section_page("teachers-usa-sponsorship.html", "Teachers", "USA private-school teacher sponsorship",
 "Certification sponsorship for teaching in private schools in the United States – process, requirements and fee.", "",
 "USA private-school teacher certification sponsorship through AGI: requirements, process, 30 days, US$60.", crumb="USA sponsorship")
section_page("teachers-careers.html", "Teachers", "Teach with AGI",
 "Join AGI's online teachers database and workshops – for freelance teachers, learning-pod leaders and STEM educators.",
 '<p style="margin-top:0"><a class="btn btn-primary" href="forms.html#enquiry/careers">Send your profile</a></p>',
 "Teach with AGI: online teachers database, learning pods and STEM educators workshops.", crumb="Teach with AGI")
section_page("programs-independent-studies.html", "Adults & professionals", "Independent course studies",
 "Self-paced, graduate-level modules using books and journals, with certificates approved by the American Canadian Board.", "",
 "AGI independent course studies: modules, program, prices and certificates approved by the American Canadian Board.", crumb="Independent studies")
section_page("programs-learning-pods.html", "Adults & professionals", "Learning pods &amp; fast track",
 "Small groups of about ten students, led by teacherpreneurs – including a fast-track high school route.", "",
 "AGI and Anglia Morocco learning pods: small groups of ten, teacherpreneurs, fast-track high school.", crumb="Learning pods")
section_page("services-document-editing.html", "Adults & professionals", "Document editing in English",
 "Professional editing of documents in English – applications, CVs, reports and academic work.",
 "<p style=\"margin-top:0\">Tell us about your document and deadline; the office will confirm the price and turnaround. " + PH_TXT("document-editing-details", "Prices and process to be confirmed.") + "</p>",
 "Document editing in English by AGI in Agadir: applications, CVs, reports and academic work, edited by native-level teachers.", crumb="Document editing")
section_page("services-proctoring.html", "Adults & professionals", "Exam proctoring",
 "Paper and online exams invigilated at AGI for distance learners of North American and British universities, companies and certification bodies.",
 "<p style=\"margin-top:0\"><b>Monday to Thursday, 9:00–17:00.</b> A 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour.</p>",
 "Exam proctoring at AGI in Agadir for distance learners: which exams, fees per exam hour, opening days and conditions.", crumb="Proctoring")
section_page("wellbeing.html", "Wellbeing (i-Heart)", "i-Heart therapeutic services",
 "Holistic support for children, teens and adults – coaching, therapeutic play and counseling, alongside school.",
 '<h2 style="margin-top:0">Our services</h2><div class="cards" style="--cols:2;margin-bottom:28px"><a class="card" href="wellbeing-adhd-coaching.html"><h3>ADHD holistic coaching</h3><p>Focus, organization and time management for children and adults.</p><span class="more">Learn more</span></a><a class="card" href="wellbeing-play-therapy.html"><h3>Holistic play therapy</h3><p>Guided therapeutic play for emotional, social and behavioral development.</p><span class="more">Learn more</span></a></div>',
 "i-Heart holistic therapeutic services and counseling at AGI: ADHD coaching and holistic play therapy.", crumb="Wellbeing")
section_page("wellbeing-adhd-coaching.html", "Wellbeing (i-Heart)", "ADHD holistic coaching",
 "One-to-one coaching for children and adults on focus, organization and time management – in Agadir and online.", "",
 "ADHD holistic coaching with Julie Wilburn, accredited Holistic Therapeutic Coach (IPHM, ICAHP), in Agadir and online.", crumb="ADHD coaching")
section_page("wellbeing-play-therapy.html", "Wellbeing (i-Heart)", "Holistic play therapy",
 "Therapeutic play that supports the emotional, behavioral, social and cognitive development of children.", "",
 "Holistic play therapy at AGI school, Agadir: approach, benefits and sessions.", crumb="Play therapy")
section_page("online-tutoring.html", "Online", "Online tutoring",
 "One-to-one lessons online through American Group USA LLC – prices, session length and how to join on Zoom or Teams.", "",
 "Online tutoring with American Group USA: session prices, how long a session should last, and Zoom/Teams instructions.")
section_page("agi-usa.html", "Online", "American Group USA LLC",
 "AGI's U.S.-registered company, offering programs, tutoring and coaching to clients worldwide.",
 "<p style=\"margin-top:0\">" + PH_TXT("agi-usa-address", "Registered address in Grantsville, Maryland – to be confirmed.") + "</p>",
 "American Group USA LLC: AGI's U.S. company for online programs, tutoring and coaching.", crumb="AGI USA")

# existing pages: add the full source details
def append_details(name, title, related):
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in related)
    block = f'''
<section class="section bg-white" id="details"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">{title}</h2>{FULLTEXT(full(name, heading=""))}</div>
<aside><p class="kicker">Related</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">{links}</ul></aside></div></section>
</main>'''
    PAGES[name] = PAGES[name].replace("\n</main>", block, 1)
    if "doc-css" not in PAGES[name]: PAGES[name] = PAGES[name].replace("</head>", f'<style id="doc-css">{DOC_CSS}</style>\n</head>', 1)
append_details("adult-diploma.html", "Program details and courses", GROUPS["Adults & professionals"][1:] + [("fees.html", "Prices")])
append_details("professional.html", "Business and medical English in detail", GROUPS["Adults & professionals"])
append_details("pathways.html", "Consultancy services and partner institutions", [("anglia-about.html", "Anglia & UCAS"), ("journal-ccgi-partnership.html", "Chichester College Group")])

# programs hub + teachers page: link everything
_more = "".join(f'<a class="card" href="{h}"><span class="tag">{g}</span><h3>{t}</h3><span class="more">Open</span></a>' for g, L in GROUPS.items() for h, t in L if h not in ("teachers.html", "adult-diploma.html", "professional.html", "pathways.html"))
PAGES["programs.html"] = PAGES["programs.html"].replace("\n</main>", f'\n<section class="section"><div class="wrap"><div class="section-head"><h2>More programs and services</h2><p>For teachers, adults, families and professionals.</p></div><div class="cards">{_more}</div></div></section>\n</main>', 1)
PAGES["teachers.html"] = PAGES["teachers.html"].replace("\n</main>", '\n<section class="section"><div class="wrap"><div class="section-head"><h2>In detail</h2></div><div class="cards">'
  + "".join(f'<a class="card" href="{h}"><h3>{t}</h3><span class="more">Open</span></a>' for h, t in GROUPS["Teachers"][1:])
  + '<a class="card" href="journal/early-childhood-education-and-care-degree.html"><h3>Early childhood education &amp; care diploma</h3><span class="more">Read</span></a></div></div></section>\n</main>', 1)

# ================================================================== PHASE 4 – RESOURCES & JOURNAL
RES = [("resources.html", "Resources for families"), ("resources-nursery-rhymes.html", "Nursery rhymes for Pre-K"), ("resources-mcguffey.html", "McGuffey readers &amp; sight words")]
def resource_page(name, title, lede, desc, intro=""):
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in RES if h != name)
    page(name, f"{title} – American Group International, Agadir", desc,
         hero(f'<a href="student-life.html">Student life</a> / <span>{title}</span>', title, lede, '<a class="btn btn-primary" href="forms.html#tutor-request">Request a tutor</a>' + WA)
         + f'<section class="section bg-white"><div class="wrap docwrap"><div class="doc">{intro}{full(name, heading="")}</div>'
           f'<aside><p class="kicker">Resources</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">{links}<li><a href="anglia-practice.html">Anglia practice papers</a></li></ul></aside></div></section>', DOC_CSS)
resource_page("resources.html", "Resources for families", "Free English learning helps for home: grammar self-helps, reading, rhymes and math resources.",
 "Free English resources from AGI: grammar self-helps, nursery rhymes, McGuffey readers and sight words, math resources.",
 '<h2 style="margin-top:0">Resources</h2><div class="cards" style="--cols:2;margin-bottom:28px"><a class="card" href="resources-nursery-rhymes.html"><h3>Nursery rhymes for Pre-K</h3><span class="more">Open</span></a><a class="card" href="resources-mcguffey.html"><h3>McGuffey readers &amp; sight words</h3><span class="more">Open</span></a></div>')
resource_page("resources-nursery-rhymes.html", "Nursery rhymes for Pre-K", "Traditional English rhymes to read and sing with young children.",
 "Traditional English nursery rhymes for pre-kindergarten children – read and sing at home.")
resource_page("resources-mcguffey.html", "McGuffey readers &amp; sight words", "Classic McGuffey reading lessons and sight words for reading and spelling practice at home.",
 "McGuffey readers and sight words: classic reading and spelling practice for children (public domain).")

# Journal: list posts that exist only on angliamorocco.org
_ang_posts = [r for r in _MAP if r["site"] == "anglia" and r["destination"].startswith("journal/")]
if _ang_posts:
    if False: inject_static("journal.html", "anglia-news", '<section class="section bg-white np" id="anglia-news"><div class="wrap"><div class="section-head"><h2>From Anglia Morocco</h2><p>News first published on angliamorocco.org.</p></div><div class="cards">'
      + "".join(f'<a class="card" href="{r["destination"]}"><span class="tag">Anglia Morocco</span><h3>{_html.escape(_re.sub(r"^[“\"]|[”\"]$", "", r["title"]))}</h3><span class="more">Read</span></a>' for r in _ang_posts)
      + "</div></div></section>")

# ================================================================== PHASE 5 – ABOUT · COOKIES · FORMS
PAGES["about.html"] = PAGES["about.html"].replace("\n</main>", f'''
<section class="section bg-white" id="in-julies-words"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">In Julie's words</h2>{render(SRC("about-us")["text"], privacy=True)}</div>
<aside><p class="kicker">About</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="our-story.html">Our story</a></li><li><a href="founder-letter.html">Founder's letter</a></li><li><a href="handbook.html">Mission &amp; handbook</a></li></ul></aside></div></section>
</main>''', 1)
if "doc-css" not in PAGES["about.html"]: PAGES["about.html"] = PAGES["about.html"].replace("</head>", f'<style id="doc-css">{DOC_CSS}</style>\n</head>', 1)

page("cookies.html", "Cookies – American Group International, Agadir", "This website uses no advertising or tracking cookies. What it stores on your device, and which outside services it loads.",
 hero("<span>Cookies</span>", "Cookies.", "This website does not use advertising or tracking cookies. Here is exactly what it stores and loads. Last updated October 2026.") + """
<section class="section bg-white"><div class="wrap"><div class="doc" data-verify="legal-review:cookies">
<h2 style="margin-top:0">What this site stores on your device</h2>
<p>One small setting in your browser's local storage, named <code>agi-story-popup</code>, remembers the date you last saw the "For parents" invitation, so that it is not shown again for 7 days. It contains no personal information and is never sent to us. You can clear it at any time by clearing your browser's site data.</p>
<h2>Outside services</h2>
<ul><li><b>Google Fonts</b> – the typefaces are loaded from Google, which receives your browser's standard technical information (such as your IP address).</li>
<li><b>Google Maps</b> – the maps on the home and contact pages are loaded from Google only when they appear on your screen; Google may set its own cookies when you use the map.</li>
<li><b>WhatsApp</b> – the WhatsApp button opens WhatsApp only when you tap it.</li></ul>
<h2>No tracking</h2><p>We do not use analytics, advertising or social-media tracking cookies. If this changes, this page will be updated and your consent asked first where the law requires it.</p>
<h2>Questions</h2><p>Write to <a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a>. See also our <a href="privacy.html">privacy policy</a>.</p>
</div></div></section>""", DOC_CSS)

# forms: attestation for AGI clients in the document request form
_ff = os.path.join(V2, "forms.html"); _ft = open(_ff, encoding="utf-8", newline="").read()
if "Attestation for AGI clients" not in _ft:
    _ft = _ft.replace('"Attendance attestation", ', '"Attendance attestation", "Attestation for AGI clients", ', 1)
    open(_ff, "w", encoding="utf-8", newline="").write(_ft)


# ================================================================== ADMISSIONS + K-12 rebuilt in the shared design system
page("admissions.html", "Admissions – American Group International, Agadir",
 "How to join AGI in Agadir: visit, placement assessment, documents, enrollment. Registration days Aug 28 & 31, first day Sept 7; tuition 2,600 MAD a month.",
 hero('<a href="parents.html">Parents</a> / <span>Admissions</span>', "Admissions.",
      "Tours are arranged individually – call or write for an appointment to meet us and see the school. Every new student sits placement assessments before admission, whatever system they arrive from, and registration for 2026–27 takes place on August 28 and 31.",
      '<a class="btn btn-primary" href="forms.html#enrollment">Apply online</a><a class="btn btn-ghost" href="forms.html#visit">Book a visit</a>') + f"""
<section class="section bg-white" id="journey"><div class="wrap">
  <div class="section-head"><h2>The application journey</h2><p>Four steps, with the office beside you at each one.</p></div>
  <div class="cards" style="--cols:4">
    <div><span class="num">01</span><h3>Enquire</h3><p>Call or email the admissions team to arrange a visit; tours are individual and include the school and the application process.</p></div>
    <div><span class="num">02</span><h3>Visit &amp; assess</h3><p>English/ESL proficiency and academic assessments, including the free Anglia placement test for language learners.</p></div>
    <div><span class="num">03</span><h3>Apply</h3><p>Prior school records and a behavior report, age and residency verification, immunization and physical examination records.</p></div>
    <div><span class="num">04</span><h3>Enroll</h3><p>Pay the annual inscription, confirm the monthly tuition plan, and order books from the beginning of August.</p></div>
  </div>
</div></section>
<section class="section" id="calendar"><div class="wrap split">
  <div class="intro"><h2>Key dates 2026–27</h2><p>Movable religious holidays – Eid al Mouloud, Ramadan, Eid al Fitr and Eid al Adha – are confirmed each term. Fall break runs October 12–18 and winter break December 18 – January 3. <a class="link" href="calendar.html">Full calendar</a></p></div>
  <dl class="rows">
    <div><dt>Registration days</dt><dd>August 28 &amp; 31</dd></div><div><dt>First day of classes</dt><dd>September 7</dd></div>
    <div><dt>Second semester begins</dt><dd>January 5</dd></div><div><dt>Anglia examinations</dt><dd>April</dd></div><div><dt>Last day &amp; graduation</dt><dd>June 17, 2027</dd></div>
  </dl>
</div></section>
<section class="section bg-navy" id="fees"><div class="wrap split">
  <div class="intro"><p class="kicker">Tuition &amp; fees</p><h2>2,600 MAD a month, paid over ten months.</h2></div>
  <div><p style="color:rgba(255,255,255,.85)">Plus one annual inscription at enrollment: 6,500 MAD for kindergarten–grade 1, rising to 11,000 MAD for grade 12. Books, mathematics and Anglia English examinations, dual enrollment in the USA and Morocco, and student insurance are included. The inscription is non-refundable; fees are not negotiable.</p>
  <div class="btn-row" style="margin-top:20px"><a class="btn btn-gold" href="fees.html">Tuition &amp; fees in full</a><a class="btn btn-light" href="forms.html#enquiry/programs">Request the tuition guide</a></div></div>
</div></section>
<section class="section bg-white" id="documents"><div class="wrap split">
  <div class="intro"><h2>What to bring</h2><p>A child aged 5 by September 1 and under 21 on the first day of school is eligible. AGI admits students of any race, religion, color, national or ethnic origin.</p></div>
  <dl class="rows">
    <div><dt>Age</dt><dd>Birth certificate, hospital or physician certificate, passport or visa, or birth registration.</dd></div>
    <div><dt>Residency</dt><dd>Lease or mortgage statement, utility bill, tax statement or deed, or a job contract – dated within three months.</dd></div>
    <div><dt>Health</dt><dd>Immunization certification and a physical examination record.</dd></div>
    <div><dt>Academic</dt><dd>Records from the previous school (or its address), plus a behavior report. IEP or special-needs provision requires practitioner documentation.</dd></div>
  </dl>
</div></section>
<section class="section" id="procedure"><div class="wrap docwrap"><div class="doc">
  <h2 style="margin-top:0">In AGI&rsquo;s own words</h2><p>The steps above summarize the procedure. Here is the full text, and the full list of enrollment documents.</p>
  {FULLTEXT(render(SRC("admissions-procedure")["text"]) + render(SRC("admission-prossess")["text"]), "The admissions procedure in full")}
  {FULLTEXT(render(SRC("/enrollment")["text"], stop="rification de l"), "Enrollment documents in full")}
</div><aside><p class="kicker">Before you enroll</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">
  <li><a href="fees.html">Tuition &amp; fees</a></li><li><a href="calendar.html">Calendar 2026–27</a></li><li><a href="policies.html">Family policies</a></li><li><a href="placement-policy.html">Placement policy</a></li><li><a href="faq.html">Questions &amp; answers</a></li></ul></aside></div></section>
""" + cta("Ready to apply?", "Apply online in about five minutes, or book a visit first.", '<a class="btn btn-gold" href="forms.html#enrollment">Apply</a><a class="btn btn-light" href="forms.html#visit">Book a visit</a>'), DOC_CSS)

_k12_rows = [("Kindergarten", "Foreign language, English, reading &amp; phonics, math, science, penmanship, ESL"),
 ("Grades 1–4", "Foreign language, English &amp; spelling, literature, mathematics, natural science, U.S. history strands, penmanship (grades 2–4), ESL"),
 ("Grades 5–8", "Foreign language, English &amp; spelling, American, world and Islamic history, literature, mathematics through pre-algebra, earth &amp; biological science, ESL"),
 ("Grade 9", "English I, U.S. history, algebra I, physical science, principles of music, physical education, ESL"), ("Grade 10", "English II, world history, geometry, biology, one elective, ESL"),
 ("Grade 11", "English III, algebra II, health, two electives, ESL"), ("Grade 12", "English IV, U.S. government &amp; economics, business math, science, ESL")]
page("k12.html", "K–12 school – American Group International, Agadir",
 "AGI's American-curriculum micro-school in Agadir, kindergarten to grade 12: lower, middle and upper school, inclusive education, course of study by grade.",
 hero('<a href="programs.html">Programs</a> / <span>K–12 school</span>', "K–12 school.",
      "An American-curriculum school, from the first day of kindergarten to the last day of grade twelve.",
      '<a class="btn btn-primary" href="admissions.html">Start admissions</a><a class="btn btn-ghost" href="forms.html#visit">Book a visit</a>') + f"""
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>At a glance</h2></div>
  <div><p class="prose">AGI is a child-centered micro-school in Agadir, established in 2013. Small classes, American curriculum standards, and ESL through the Anglia Examinations system of England for children who do not speak English at home. Students are welcomed at any stage and supported to adapt to the curriculum and the language immersion.</p>
  <dl class="rows"><div><dt>Ages</dt><dd>5–18</dd></div><div><dt>Curriculum</dt><dd>American</dd></div><div><dt>Languages</dt><dd>English · French · Arabic</dd></div><div><dt>Campus</dt><dd>Agadir · Hay Nahda</dd></div></dl></div>
</div></section>
<section class="section" id="schools"><div class="wrap">
  <div class="section-head"><h2>Three schools, one journey</h2></div>
  <div class="cards">
    <div>{ph("k12-lower", "Lower school classroom", "4/3")}<span class="tag">K – Grade 5</span><h3>Lower School</h3><p>English and spelling, literature, mathematics, natural science and foreign language – with penmanship in grades 2 to 4 and ESL alongside. The elementary benchmark is CEFR B1 by the end of grade 5.</p></div>
    <div>{ph("k12-middle", "Middle school class", "4/3")}<span class="tag">Grades 6 – 8</span><h3>Middle School</h3><p>American, world and Islamic history, earth and biological science, and mathematics through Foundations and Pre-Algebra. Middle school graduates at grade 8 target CEFR B2.</p></div>
    <div>{ph("k12-upper", "Upper school students", "4/3")}<span class="tag">Grades 9 – 12</span><h3>Upper School</h3><p>English I–IV, U.S. History, Algebra I and II, Geometry, Biology, Government and Economics. Two routes: the Florida-accredited books program or the Cognia-accredited American High School Online. Forty service hours are required to graduate.</p></div>
  </div>
</div></section>
<section class="section bg-white" id="inclusive"><div class="wrap split">
  <div class="intro"><h2>Inclusive by design</h2><p>AGI welcomes students with a range of special needs, learning differences and mental-health challenges, physical and developmental alike. Documentation from a licensed practitioner is required so provision can be planned properly. <a class="link" href="special-education.html">Special education</a></p></div>
  <dl class="rows">
    <div><dt>Individualized plans</dt><dd>Individualized Education Plans written to each student's needs and abilities.</dd></div>
    <div><dt>Small groups</dt><dd>Class sizes that allow personalized attention within mainstream school life.</dd></div>
    <div><dt>Therapeutic support</dt><dd>Occupational therapy, speech-language pathology and behavioral support.</dd></div>
    <div><dt>Cognitive programs</dt><dd>Energia SOI, customized for students with reading and mathematics difficulties.</dd></div>
  </dl>
</div></section>
<section class="section bg-navy"><div class="wrap">
  <div class="section-head"><h2>How the year is measured</h2></div>
  <div class="facts"><div><b>90%</b><span>Minimum attendance to qualify for promotion, K–12.</span></div><div><b>64%</b><span>Pass mark in each core subject – math, science, language arts, social studies.</span></div>
  <div><b>April</b><span>Anglia English assessment, required of every enrolled student.</span></div><div><b>40</b><span>Service hours across four years of high school – ten per year.</span></div></div>
  <p style="color:rgba(255,255,255,.8);margin-top:24px">Every new student sits English/ESL and academic placement assessments before admission, whatever system they arrive from. Grades 9 to 11 also take the CAT assessment.</p>
</div></section>
<section class="section bg-white" id="curriculum"><div class="wrap">
  <div class="section-head"><h2>The course of study, grade by grade</h2><p>A fixed set of subjects each year, with ESL alongside for language learners. Electives and AP courses are planned from grade 9.</p></div>
  <div class="table-wrap"><table><thead><tr><th>Grades</th><th>Subjects</th></tr></thead><tbody>{"".join(f"<tr><td><b>{g}</b></td><td>{x}</td></tr>" for g, x in _k12_rows)}</tbody></table></div>
  <p style="margin-top:20px">High school students complete 40 service hours (ten a year). For grades 9–12 there are two routes: the Florida-accredited books program, or American High School Online (Cognia accredited). See <a class="link" href="fees.html#high-school">tuition &amp; fees</a> and <a class="link" href="english-anglia.html#cefr">English benchmarks</a>.</p>
</div></section>
<section class="section"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">About the school in detail</h2>{FULLTEXT("".join(render(SRC(u)["text"], privacy=True) for u in MAPPED("k12.html")))}</div>
<aside><p class="kicker">Related</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="handbook.html">Academic handbook</a></li><li><a href="supplies.html">Supplies list</a></li><li><a href="homework.html">Homework</a></li><li><a href="special-education.html">Special education</a></li></ul></aside></div></section>
""" + cta("Ready to meet the school?", "Start admissions, or book a visit during the school day.", '<a class="btn btn-gold" href="admissions.html">Start admissions</a><a class="btn btn-light" href="forms.html#visit">Book a visit</a>'), DOC_CSS)


# ================================================================== PARTNERSHIPS rebuilt in the shared design system
_net = [("Souss-Massa", "Headquarters · Agadir"), ("Casablanca-Settat", "Anglia centers"), ("Tanger-Tetouan-Al Hoceima", "Anglia centers"), ("Rabat-Salé-Kénitra", "Anglia centers"),
        ("Fès-Meknès · Marrakech-Safi", "Anglia centers"), ("Oriental · Béni Mellal-Khénifra", "Open for franchise"), ("Drâa-Tafilalet · Southern Provinces", "Open for franchise")]
_partners = [("United Kingdom", "Chichester College Group International", "The international arm of a seven-college group in the south of England – Chichester, Crawley, Worthing, Brinsbury, Brighton MET, Northbrook and Haywards Heath. Signed 2025.", "journal-ccgi-partnership.html"),
 ("Teacher training", "Bridge Education Group", "A global leader in teacher training and TEFL/TESOL certification. Partnership announced November 2025, opening professional development to educators across Morocco.", "teachers.html"),
 ("University placement", "Leverage Edu", "Official regional representation for Souss and southern Morocco since March 2026 – private and public university placement with housing assistance.", "pathways.html"),
 ("Plantation, Florida", "American High School", "Cognia-accredited online diploma program and a Yass Prize awardee. Partnership announced 2025; the diploma is accepted in the U.S. and internationally.", "fees.html#high-school"),
 ("United Kingdom", "RB College", "UCAS-registered UK institution offering academic and vocational programs, including work-based Master of Business Administration routes.", "pathways.html"),
 ("Chichester, since 1993", "Anglia Examinations England", "AGI has been the Anglia franchise holder for Morocco since 2021 and has used the Anglia system in its language programs since 2013.", "anglia-about.html"),
 ("For teacherpreneurs", "AGI Learning Pods", "Small-group programs run by freelance teachers and parent groups under the Anglia system – inclusive, creative and affordable.", "programs-learning-pods.html"),
 ("Membership", "American School Counselor Association", "AGI joined the ASCA network in 2026, bringing U.S. school-counseling standards to student guidance.", "about.html#accreditation")]
page("partnerships.html", "Partnerships & franchise – American Group International, Agadir",
 "Partner with AGI and Anglia Morocco: Anglia center franchise in Morocco's twelve regions, institutional partnerships, university pathways and our partner network.",
 hero('<a href="anglia.html">Anglia Morocco</a> / <span>Partnerships &amp; franchise</span>', "Bring the AGI standard to your region.",
      "AGI holds the Anglia Examinations franchise for Morocco and operates from Agadir across the Kingdom's twelve regions. We work with schools, language centers, freelance teachers and international institutions – and franchise opportunities are open for the right candidates.",
      '<a class="btn btn-primary" href="forms.html#enquiry/partnership">Partnership enquiry</a><a class="btn btn-ghost" href="anglia-network.html">Network &amp; centres</a>') + f"""
<section class="section bg-white" id="models"><div class="wrap">
  <div class="section-head"><h2>Two ways to build with AGI</h2></div>
  <div class="cards" style="--cols:2">
    <div><span class="tag">Model I</span><h3>Franchise</h3><p>An Anglia Morocco center under your ownership, anywhere in the Kingdom's twelve regions. You get the examinations license, the placement and testing system, training, and the AGI standard behind it. Enquiries run through the Agadir headquarters.</p>
      <ul><li>Anglia examinations license &amp; materials</li><li>Teacher training and C.I.T.E. certification</li><li>Placement testing &amp; level mapping to the CEFR</li><li>Territory agreement within the 12 regions</li></ul></div>
    <div><span class="tag">Model II</span><h3>Institutional partnership</h3><p>For existing schools, language institutes and colleges: Anglia examination provision inside your campus, university pathway agreements, and co-designed English or academic programs under a shared quality framework.</p>
      <ul><li>Co-designed English &amp; academic programs</li><li>University pathway agreements (UK, USA, India)</li><li>Anglia testing center inside your campus</li><li>Shared quality framework &amp; annual review</li></ul></div>
  </div>
</div></section>
<section class="section" id="network"><div class="wrap split">
  <div class="intro"><h2>The network today</h2><p>Anglia Morocco is managed from the Agadir headquarters, with Anglia centers across the north and center of the Kingdom. Remaining regions are open for franchise. <a class="link" href="anglia-network.html">Regions, provinces and open positions</a></p></div>
  <dl class="rows">{"".join(f"<div><dt>{r}</dt><dd>{st}</dd></div>" for r, st in _net)}</dl>
</div></section>
<section class="section bg-white" id="partners"><div class="wrap">
  <div class="section-head"><h2>Who we work with</h2><p>Examination boards, colleges, placement partners and professional bodies.</p></div>
  <div class="cards">{"".join(f'<a class="card" href="{h}"><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p></a>' for t, n, d, h in _partners)}</div>
</div></section>
<section class="section"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">Partner with AGI and Anglia Morocco</h2>{FULLTEXT("".join(render(SRC(u)["text"], privacy=True) for u in MAPPED("partnerships.html")))}</div>
<aside><p class="kicker">Anglia Morocco</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="anglia.html">Anglia Morocco</a></li><li><a href="anglia-network.html">Network &amp; centres</a></li><li><a href="investors.html">Partners &amp; investors</a></li></ul></aside></div></section>
""" + cta("Start the conversation.", "Franchise and partnership enquiries are handled from the Agadir headquarters. Tell us the region, the model and your teaching or business background.", '<a class="btn btn-gold" href="forms.html#enquiry/partnership">Partnership enquiry</a><a class="btn btn-light" href="contact.html">Contact</a>'), DOC_CSS)


# ================================================================== ANGLIA REDESIGN (hub, exams ladder, exam dates, classes, become a centre)
ANGLIA_CSS = DOC_CSS + FAQ_CSS + """
.paths{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}
.paths a{background:#fff;padding:26px 22px;display:flex;flex-direction:column;gap:8px;text-decoration:none;color:var(--ink);transition:background .2s}
.paths a:hover{background:var(--paper)}.paths .who{font:600 12px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.paths h3{font-family:var(--serif);font-weight:400;font-size:24px;color:var(--navy);margin:0}.paths p{margin:0;font-size:14.5px;color:var(--text);line-height:1.6}.paths .more{margin-top:auto;font-weight:600;font-size:13px;color:var(--navy)}
.recog{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:18px}
.recog div{border-top:2px solid var(--gold);padding-top:14px}.recog b{display:block;font-family:var(--serif);font-weight:400;font-size:21px;color:#fff;margin-bottom:6px}.recog span{font-size:13.5px;color:rgba(255,255,255,.75);line-height:1.55}
.next-session{display:grid;grid-template-columns:auto 1fr auto;gap:24px;align-items:center;border:1px solid var(--line);background:#fff;padding:24px 28px}
.next-session .when{font-family:var(--serif);font-size:34px;color:var(--red);line-height:1}.next-session p{margin:4px 0 0;color:var(--text)}
.ladder{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.ladder li{display:grid;grid-template-columns:56px 150px 74px 1fr;gap:18px;align-items:center;background:#fff;border:1px solid var(--line);padding:16px 20px}
.ladder .step{font-family:var(--serif);font-size:30px;color:var(--gold);line-height:1}.ladder .name{font-weight:600;color:var(--navy)}
.ladder .cefr{font:600 12px/1 var(--sans);letter-spacing:.06em;text-align:center;padding:7px 0;border:1px solid var(--navy);color:var(--navy)}
.ladder .grp{display:block;grid-column:1/-1;font:600 11px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--red);background:none;border:0;padding:16px 0 2px}
.ladder li p{margin:0;font-size:14.5px;color:var(--text)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px}.chips button{font:600 13px/1 var(--sans);padding:9px 14px;border:1px solid var(--line);background:#fff;color:var(--navy);cursor:pointer}
.chips button[aria-pressed="true"]{background:var(--navy);color:#fff;border-color:var(--navy)}
tr.past{opacity:.45}
.offers{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.offer{background:#fff;border:1px solid var(--line);padding:24px;display:flex;flex-direction:column;gap:10px}.offer.feat{border:2px solid var(--navy)}
.offer .price{font-family:var(--serif);font-size:34px;color:var(--navy);line-height:1}.offer .per{font-size:13px;color:var(--grey)}.offer ul{margin:0;padding-left:18px;font-size:14px;color:var(--text)}.offer .btn{margin-top:auto}
.regions{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.region{background:#fff;border:1px solid var(--line);padding:20px}.region h3{font-size:19px;margin:6px 0 8px;color:var(--navy)}
.status{display:inline-block;font:600 11px/1 var(--sans);letter-spacing:.1em;text-transform:uppercase;padding:6px 9px}
.status.open{background:#e8f4ea;color:#1d6b33}.status.hq{background:var(--navy);color:#fff}.status.net{background:var(--paper);color:var(--grey)}
.region details summary{cursor:pointer;font-size:13.5px;color:var(--navy);font-weight:600}.region ul{margin:8px 0 0;padding-left:18px;font-size:13.5px;color:var(--text)}
@media (max-width:1000px){.paths,.offers{grid-template-columns:repeat(2,minmax(0,1fr))}.recog{grid-template-columns:repeat(2,minmax(0,1fr))}.regions{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.paths,.offers,.regions{grid-template-columns:minmax(0,1fr)}.ladder li{grid-template-columns:44px 1fr 64px}.ladder li p{grid-column:1/-1}.next-session{grid-template-columns:minmax(0,1fr)}}
"""
_MN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def exam_rows(text):
    rows, month, levels = [], None, []
    for l in text.split("\n"):
        t = l.strip().replace("▶", "").replace("\u25b6", "").strip()
        if not t or "EXAM DATES" in t or t.startswith(("Anglia Exam Dates", "Book order")): continue
        if t in _MN: month, levels = t, []; continue
        if t.startswith("#"): levels.append(t.lstrip("# ").strip()); continue
        if _re.search(r"(Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day", t) and month: rows.append((month, ", ".join(levels) or "All levels", t)); levels = []
    return rows
_EX = exam_rows(SRC("anglia-exam-dates")["text"])
import datetime as _dt
_now = _dt.date.today()
_next = next(((m, lv, d) for m, lv, d in _EX if _MN.index(m) + 1 >= _now.month), _EX[0] if _EX else ("", "", ""))

# ---------- 1. HUB
_paths = [("Parents &amp; students", "Certify your child's English", "Ten steps from a child's first words (about age 4) to Masters C2 – each one a certificate from England.", "anglia-exams.html"),
          ("Adults &amp; professionals", "English for work and study", "General English up to Masters, or Business English from A2+ to C1, with classes that fit a working week.", "anglia-classes.html"),
          ("Teachers", "C.I.T.E. certification", "A lifelong TESOL qualification recognized worldwide – no entry qualifications required.", "teachers-cite.html"),
          ("Schools &amp; partners", "Become an Anglia centre", "Run Anglia exams in your school or region, with training and materials from the Agadir headquarters.", "anglia-network.html")]
page("anglia.html", "Anglia Morocco – official English exams from England | AGI Agadir",
 "Anglia Morocco headquarters at AGI, Agadir: official English exams from England, First Step to Masters C2, from age 4. Exam dates, classes, free level test, centres in 12 regions.",
 hero("<span>Anglia Morocco</span>", "Official English certificates from England.",
      "Anglia Examinations has tested English since 1993 from Chichester, England. Since 2021 AGI has been the Anglia franchise holder for Morocco – exams from a child's first words to Masters (C2), classes, and centres across the Kingdom's twelve regions.",
      '<a class="btn btn-primary" href="forms.html#enquiry/anglia">Book a free level test</a><a class="btn btn-ghost" href="anglia-exam-dates.html">Exam dates 2026</a>')
 + f'''<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Where do you start?</h2></div>
  <div class="paths">{"".join(f'<a href="{h}"><span class="who">{w}</span><h3>{t}</h3><p>{d}</p><span class="more">Continue →</span></a>' for w, t, d, h in _paths)}</div>
</div></section>
<section class="section bg-navy"><div class="wrap">
  <div class="section-head"><h2>Why Anglia</h2></div>
  <div class="recog">
    <div><b>England, since 1993</b><span>Part of Chichester College Group – award winning and Ofsted Outstanding.</span></div>
    <div><b>Regulated by Ofqual</b><span>The four highest levels are awarded by AIM Qualifications and Assessment Group.</span></div>
    <div><b>UCAS tariff points</b><span>The Mastery (C2) qualification counts for UK university entry.</span></div>
    <div><b>For life</b><span>Certificates do not expire – an institution may ask for a recent one.</span></div>
    <div><b>From age 4</b><span>No upper age limit; every level tests listening, reading, writing and speaking.</span></div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <div class="next-session"><div class="when">{_next[0]}</div><div><b>Next exam session{(": " + _next[1]) if _next[1] else ""}</b><p>{_next[2]} – sessions run in most months; other dates are possible on request.</p></div><a class="btn btn-primary" href="anglia-exam-dates.html">All 2026 dates</a></div>
</div></section>
<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Everything about Anglia in Morocco</h2></div>
  <div class="cards">{"".join(f'<a class="card" href="{h}"><h3>{t}</h3><span class="more">Open</span></a>' for h, t in [("anglia-exams.html", "Exams &amp; levels"), ("anglia-exam-dates.html", "Exam dates 2026"), ("anglia-classes.html", "Classes &amp; prices"), ("anglia-practice.html", "Practice papers &amp; audio"), ("anglia-books.html", "Step To books"), ("anglia-special-arrangements.html", "Special arrangements"), ("anglia-cefr.html", "CEFR levels"), ("anglia-faq.html", "Anglia FAQ"), ("anglia-about.html", "About Anglia Examinations")])}</div>
</div></section>
<section class="section"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">Anglia Morocco in its own words</h2>{FULLTEXT(render(_home["text"], privacy=True), "The Anglia Morocco welcome text")}
<h2>Club Anglia</h2><p>{PH_TXT("club-anglia", "Coming soon.")}</p></div>
<aside><p class="kicker">Contacts</p><p class="muted" style="font-size:14px">Julie Wilburn · <a href="mailto:j.wilburn@angliamorocco.org">j.wilburn@angliamorocco.org</a><br>Abdelhak Lam · <a href="mailto:a.lam@angliamorocco.org">a.lam@angliamorocco.org</a><br><a href="https://angliamorocco.org/" target="_blank" rel="noopener">angliamorocco.org</a></p></aside></div></section>
''' + cta("Find your English level.", "The placement assessment is free and takes place at AGI in Agadir.", '<a class="btn btn-gold" href="forms.html#enquiry/anglia">Book a free level test</a><a class="btn btn-light" href="anglia-classes.html">Classes &amp; prices</a>'), ANGLIA_CSS)

# ---------- 2. EXAMS & LEVELS: the ladder
_grp = {"First Step": "Young learners", "Preliminary": "General English", "Advanced": "Higher levels"}
_lad = "".join((f'<li class="grp">{_grp[n]}</li>' if n in _grp else "") + f'<li><span class="step">{i}</span><span class="name">{n}</span><span class="cefr">{c}</span><p>{d}</p></li>' for i, (n, c, d) in enumerate(LEVELS, 1))
_bz2 = "".join(f'<li><span class="step">B{i}</span><span class="name">{n}</span><span class="cefr">{c}</span><p>Practical business functions in realistic workplace situations – all four skills.</p></li>' for i, (n, c) in enumerate(BUSINESS, 1))
page("anglia-exams.html", "Anglia exams & levels – Anglia Morocco | AGI Agadir",
 "The Anglia ladder: ten General English levels from First Step to Masters C2, four Business English levels A2+ to C1, exam durations and certificates for life.",
 hero('<a href="anglia.html">Anglia Morocco</a> / <span>Exams &amp; levels</span>', "Ten steps to Masters.",
      "Anglia's General English exams take learners from a first vocabulary of about 100 words to expert use of English (Masters, C2). Every level tests listening, reading, writing and speaking.",
      '<a class="btn btn-primary" href="forms.html#enquiry/anglia">Find my level</a><a class="btn btn-ghost" href="anglia-exam-dates.html">Exam dates</a>')
 + f'''<section class="section bg-white" id="ladder"><div class="wrap split"><div class="intro"><h2>The General English ladder</h2><p>The three young-learner levels (YL) lead up to A1. Young-learner levels are also open to adults – anyone can start at the step that fits. <a class="link" href="anglia-cefr.html">What the CEFR levels mean</a></p></div>
  <ol class="ladder">{_lad}</ol></div></section>
<section class="section" id="business"><div class="wrap split"><div class="intro"><h2>Business English</h2><p>Four steps for candidates whose special interest is business, from A2+ to C1. <a class="link" href="professional.html">Business English classes</a></p></div><ol class="ladder">{_bz2}</ol></div></section>
<section class="section bg-white" id="format"><div class="wrap split"><div class="intro"><h2>How long are the exams?</h2></div>
  <dl class="rows"><div><dt>Reading &amp; writing</dt><dd>1 hour minimum, 3 hours maximum, depending on the level</dd></div><div><dt>Listening</dt><dd>10–30 minutes</dd></div><div><dt>Speaking</dt><dd>About 5–20 minutes</dd></div><div><dt>Certificate</dt><dd>Valid for life; an institution may ask for a recent one</dd></div><div><dt>Online exams</dt><dd>Anglia exams can also be taken online in Morocco – ask the office</dd></div></dl></div></section>
<section class="section"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">In detail</h2>{FULLTEXT(full("anglia-exams.html", heading=""), "The exam descriptions in full")}</div>
<aside><p class="kicker">Next</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="anglia-practice.html">Practice papers</a></li><li><a href="anglia-special-arrangements.html">Special arrangements</a></li><li><a href="anglia-classes.html">Classes &amp; prices</a></li></ul></aside></div></section>
''' + cta("Not sure which level?", "Take the free placement assessment – we will recommend the right step.", '<a class="btn btn-gold" href="forms.html#enquiry/anglia">Book a free level test</a><a class="btn btn-light" href="anglia-practice.html">Try a practice paper</a>'), ANGLIA_CSS)

# ---------- 3. EXAM DATES (new page, filterable)
_er = "".join(f'<tr data-m="{_MN.index(m) + 1}"><td><b>{m}</b></td><td>{_html.escape(lv)}</td><td>{_html.escape(d)}</td></tr>' for m, lv, d in _EX)
page("anglia-exam-dates.html", "Anglia exam dates 2026 – Anglia Morocco | AGI Agadir",
 "Anglia exam sessions in Morocco in 2026, month by month and by level, and how to register at Anglia Morocco headquarters in Agadir.",
 hero('<a href="anglia.html">Anglia Morocco</a> / <span>Exam dates 2026</span>', "Anglia exam dates 2026.",
      "Sessions run in most months of the year. If you need an exam on a date that is not listed, contact the Anglia office.",
      '<a class="btn btn-primary" href="forms.html#enquiry/anglia">Register for an exam</a><a class="btn btn-ghost" href="anglia-exams.html">Which level?</a>')
 + f'''<section class="section bg-white"><div class="wrap">
  <div class="chips" role="group" aria-label="Show"><button type="button" data-f="up" aria-pressed="true">Upcoming</button><button type="button" data-f="all" aria-pressed="false">All of 2026</button></div>
  <div class="table-wrap"><table id="exam-dates"><thead><tr><th>Month</th><th>Levels / session</th><th>Exam days</th></tr></thead><tbody>{_er}</tbody></table></div>
  <p class="muted" style="font-size:13px;margin-top:14px">Young-learner levels (First Step, Junior, Primary) often have their own days. Special arrangements must be requested when you register. <a href="anglia-special-arrangements.html">Special arrangements</a></p>
</div></section>
<script>(function(){{var m=new Date().getMonth()+1,rows=[].slice.call(document.querySelectorAll("#exam-dates tbody tr"));
function show(f){{rows.forEach(function(r){{var past=+r.dataset.m<m;r.classList.toggle("past",past&&f==="all");r.hidden=past&&f==="up"}});
document.querySelectorAll(".chips button").forEach(function(b){{b.setAttribute("aria-pressed",b.dataset.f===f)}})}}
document.querySelectorAll(".chips button").forEach(function(b){{b.addEventListener("click",function(){{show(b.dataset.f)}})}});show("up")}})();</script>
''' + cta("Ready to register?", "Tell us the candidate's level and preferred session – the office will confirm.", '<a class="btn btn-gold" href="forms.html#enquiry/anglia">Register for an exam</a><a class="btn btn-light" href="anglia-practice.html">Practice papers</a>'), ANGLIA_CSS)

# ---------- 4. CLASSES & PRICES: comparison
_offers = [("Saturday classes", "500 MAD", "a month", ["Ages 5–18", "Saturdays 2:00–4:00 p.m., October–June", "Yearly Anglia exam included", "BAC, TOEFL, IELTS, SAT and Mathematics-in-English preparation"], True),
           ("One-to-one", "200 MAD", "a session", ["English or mathematics", "Full access to the teacher", "Times that fit a working week", "Ideal for job-related English"], False),
           ("Small group", "150 MAD", "per person, per session", ["2–3 students", "Friends, siblings or colleagues", "Same level, shared goals"], False),
           ("12-week course", "1,200 MAD", "100 MAD a week", ["4–10 students", "A structured course over 12 weeks", "Progress measured on the CEFR"], False)]
page("anglia-classes.html", "English classes & prices – Anglia Morocco | AGI Agadir",
 "English classes at Anglia Morocco, Agadir: Saturday classes 500 MAD a month, one-to-one 200 MAD, small groups 150 MAD, 12-week course 1,200 MAD. Free level test.",
 hero('<a href="anglia.html">Anglia Morocco</a> / <span>Classes &amp; prices</span>', "English classes, at every age.",
      "Start with a free level test, then choose the format that suits you – from Saturday classes for children and teens to one-to-one lessons for professionals.",
      '<a class="btn btn-primary" href="forms.html#enquiry/anglia">Book a free level test</a>' + WA)
 + '<section class="section bg-white"><div class="wrap"><div class="offers">' + "".join(
    f'<div class="offer{" feat" if feat else ""}"><span class="tag">{n}</span><span class="price">{pr}</span><span class="per">{per}</span><ul>{"".join(f"<li>{x}</li>" for x in pts)}</ul><a class="btn {"btn-primary" if feat else "btn-ghost"}" href="forms.html#enquiry/anglia">Ask about this class</a></div>'
    for n, pr, per, pts, feat in _offers) + '''</div>
  <p class="muted" style="font-size:13px;margin-top:16px">Level test free · groups of up to 10 · prices effective November 2024 · books and insurance not included. <a href="calendar.html#saturday">Saturday schedule</a> · <a href="english-anglia.html#math-english">Mathematics in English</a></p>
</div></section>''' + f'''<section class="section"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">About our classes</h2>{FULLTEXT(full("anglia-classes.html", heading=""), "Our English classes in full")}</div>
<aside><p class="kicker">Anglia Morocco</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="anglia-exams.html">Exams &amp; levels</a></li><li><a href="anglia-exam-dates.html">Exam dates</a></li><li><a href="fees.html#english">All prices</a></li></ul></aside></div></section>
''' + cta("Find the right class.", "A free level test first – then we recommend the format and the level.", '<a class="btn btn-gold" href="forms.html#enquiry/anglia">Book a free level test</a><a class="btn btn-light" href="contact.html">Contact</a>'), ANGLIA_CSS)

# ---------- 5. BECOME A CENTRE: regions with status
_nt = SRC("angliamorocco-networks-and-centers-12-regions")["text"]; _regs, _cur = [], None
for _l in _nt.split("\n"):
    _l = _l.strip()
    _m = _re.match(r"#+\s*(.+?Region)\s*-\s*(\d+)", _l)
    if _m: _cur = [_m.group(1).strip(), int(_m.group(2)), []]; _regs.append(_cur); continue
    if _cur and _l.startswith("-") and not any(k in _l for k in _POL): _cur[2].append(_l.lstrip("- ").strip())
    if _l.startswith("#") and not _m and _cur and "Region" not in _l: _cur = None
def _status(name, provs):
    if "Souss" in name: return ("hq", "Headquarters · Agadir")
    return ("open", "Representative wanted") if any("Representative Available" in x for x in provs) else ("net", "Anglia network")
_rc = "".join(f'''<div class="region"><span class="status {_status(n, pv)[0]}">{_status(n, pv)[1]}</span><h3>{_html.escape(n)}</h3>
<details><summary>{len(pv)} prefectures &amp; provinces</summary><ul>{"".join(f"<li>{_html.escape(x.replace(' – Representative Available', '').replace('- Representative Available', '').replace('-Representative Available', '').strip(' -–'))}{' <b>· representative wanted</b>' if 'Representative Available' in x else ''}</li>" for x in pv)}</ul></details></div>''' for n, num, pv in sorted(_regs, key=lambda r: r[1]))
page("anglia-network.html", "Become an Anglia centre – Anglia Morocco | AGI Agadir",
 "Anglia Morocco network across Morocco's 12 regions: open representative positions, franchise and institutional partnership models, how to become an Anglia centre.",
 hero('<a href="anglia.html">Anglia Morocco</a> / <span>Become a centre</span>', "Become an Anglia centre.",
      "From its Agadir headquarters, Anglia Morocco works with schools, language centres and teachers across the Kingdom's twelve regions. Several regions are looking for a local representative.",
      '<a class="btn btn-primary" href="forms.html#enquiry/partnership">Partnership enquiry</a><a class="btn btn-ghost" href="partnerships.html">Partnership models</a>')
 + f'''<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>The 12 regions</h2><p>Main headquarters: AGI, Agadir · Sales coordinator: Abdelhak Lam.</p></div>
  <div class="regions">{_rc}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Two ways to work with us</h2></div>
  <div class="cards" style="--cols:2">
    <div><span class="tag">Model I</span><h3>Anglia centre (franchise)</h3><p>An Anglia Morocco centre under your ownership: the examinations license, placement and testing system, teacher training and C.I.T.E., and a territory agreement within the 12 regions.</p></div>
    <div><span class="tag">Model II</span><h3>Institutional partnership</h3><p>For existing schools and institutes: an Anglia testing centre inside your campus, co-designed English programs and university pathway agreements.</p></div>
  </div>
  <p style="margin-top:18px"><a class="link" href="partnerships.html">Partnerships in detail</a></p>
</div></section>
''' + cta("Represent Anglia in your region.", "Tell us your region, the model and your teaching or business background.", '<a class="btn btn-gold" href="forms.html#enquiry/partnership">Partnership enquiry</a><a class="btn btn-light" href="contact.html">Contact</a>'), ANGLIA_CSS)
for _n, _t in [("anglia-exam-dates.html", "Exam dates 2026")]:
    if (_n, _t) not in ANGLIA_NAV: ANGLIA_NAV.insert(2, (_n, _t))

# ================================================================== ANGLIA BRAND (approved): Anglia blues + logo on Anglia pages; practice, books, exams in angliamorocco.org style
ANGLIA_LOGO = "assets/web/anglia-anglia-moroccool3.webp"
ANGLIA_THEME_CSS = """
main.anglia-theme{--navy:#03379F;--navy-deep:#000F23;--red:#0082D0;--gold:#5BC0F8}
main.anglia-theme .bg-navy,main.anglia-theme .cta-band{background:#03379F}
.anglia-hero{position:relative}.anglia-badge{position:absolute;top:clamp(28px,4vw,56px);right:clamp(20px,4vw,48px);width:clamp(72px,8vw,112px);height:auto;border-radius:10px;box-shadow:0 10px 30px -12px rgba(0,15,35,.35)}
[dir="rtl"] .anglia-badge{right:auto;left:clamp(20px,4vw,48px)}
.anglia-hub-hero{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.6fr);gap:clamp(24px,5vw,72px);align-items:center}
.anglia-hub-hero img{width:100%;max-width:300px;justify-self:end;border-radius:16px;box-shadow:0 24px 60px -24px rgba(0,15,35,.5)}
.recog-logo{display:flex;align-items:center;gap:18px;margin:0 0 26px}.recog-logo img{width:64px;height:auto;border-radius:8px}.recog-logo span{color:rgba(255,255,255,.8);font-size:14px}
.packs{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px}
.pack{background:#fff;border:1px solid var(--line);padding:18px}.packs+h2{margin-top:56px}.pack h3{font-size:18px;margin:0 0 10px;color:var(--navy)}
.pack .dl{display:flex;flex-wrap:wrap;gap:6px}.pack .dl a{font:600 12.5px/1 var(--sans);padding:8px 11px;border:1px solid var(--navy);color:var(--navy);text-decoration:none}
.pack .dl a:hover{background:var(--navy);color:#fff}
.series{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;counter-reset:s}
.series div{background:#fff;border:1px solid var(--line);padding:16px;text-align:center}.series b{display:block;font-family:var(--serif);font-weight:400;font-size:20px;color:var(--navy)}
.series small{display:block;margin-top:6px;font-size:12px;color:var(--grey)}.series .acc{color:var(--red);font-weight:600}
@media (max-width:900px){.anglia-hub-hero{grid-template-columns:minmax(0,1fr)}.anglia-hub-hero img{justify-self:start;max-width:160px}.series{grid-template-columns:repeat(2,minmax(0,1fr))}.anglia-badge{position:static;display:block;margin:0 0 16px}}
"""
# ---------- Business English: real per-level descriptions from the source
_ex_src = SRC("angliamorocco.org/exams/")["text"]
_bdesc = [p.strip() for p in _re.findall(r"(At this level, candidates are expected[^\n]+)", _ex_src)]
if len(_bdesc) >= 4:
    _bz3 = "".join(f'<li><span class="step">B{i}</span><span class="name">{n}</span><span class="cefr">{c}</span><p>{_html.escape(_bdesc[i - 1])}</p></li>' for i, (n, c) in enumerate(BUSINESS, 1))
    PAGES["anglia-exams.html"] = _re.sub(r'(<section class="section" id="business">.*?<ol class="ladder">).*?(</ol>)', lambda m: m.group(1) + _bz3 + m.group(2), PAGES["anglia-exams.html"], count=1, flags=_re.S)

# ---------- PRACTICE PAPERS (angliamorocco.org/practice-resources style): 5 categories, a card per level
_cat_rules = [("General English", r"first-step|junior|primary|preliminary|elementary|pre-intermediate|intermediate|advanced|proficiency|masters", ["First Step", "Junior", "Primary", "Preliminary", "Elementary", "Pre-Intermediate", "Intermediate", "Advanced", "Proficiency", "Masters"]),
              ("Business English", r"business", ["Practical Business English", "Intermediate Business English", "Advanced Business English", "Proficiency in Business English"]),
              ("Children's Oral Tests of Achievement", r"childrens-oral", ["Level I", "Level II", "Level III"]),
              ("Certificate & Diploma in Applied Translation", r"translation", ["Certificate in Applied Translation", "Diploma in Applied Translation"]),
              ("Teachers (C.I.T.E.)", r"cite-", ["C.I.T.E. Very Young Learners", "C.I.T.E. Young Learners", "C.I.T.E. Senior"])]
_all_links = []
for _h, _t in _re.findall(r'<a[^>]+href="(https?://[^"]+\.(?:zip|pdf))"[^>]*>(.*?)</a>', _raw, _re.S | _re.I):
    if _h not in [x for x, _ in _all_links] and _h not in _dead: _all_links.append((_h, _t))
def _level_of(h, cat, levels):
    f = h.rsplit("/", 1)[-1].lower()
    if cat.startswith("Business"): return next((L for L in levels if L.split()[0].lower() in f), levels[0])
    if cat.startswith("Children"): return {"level-i-": "Level I", "level-i.": "Level I", "level-ii-": "Level II", "level-ii.": "Level II", "level-iii": "Level III"}.get(next((k for k in ("level-iii", "level-ii-", "level-ii.", "level-i-", "level-i.") if k in f), ""), "Level I")
    if cat.startswith("Certificate"): return levels[1] if "diploma" in f else levels[0]
    if cat.startswith("Teachers"): return {"vyl": levels[0], "yl": levels[1]}.get(next((k for k in ("vyl", "yl") if f"cite-{k}" in f), ""), levels[2])
    return next((L for L in sorted(levels, key=len, reverse=True) if L.lower().replace(" ", "-") in f), "Other")
_secs = ""
for _cat, _rx, _levels in _cat_rules:
    _items = [(h, _level_of(h, _cat, _levels)) for h, t in _all_links if _re.search(_rx, h, _re.I) and (_cat != "General English" or "business" not in h.lower())]
    _cards = ""
    for L in _levels:
        _ls = [h for h, lv in _items if lv == L]
        _btns = "".join(f'<a href="{h}" rel="noopener">{"Pack " + str(i) if len(_ls) > 1 else "Download"}</a>' for i, h in enumerate(_ls, 1))
        _cards += f'<div class="pack"><h3>{_html.escape(L)}</h3><div class="dl">{_btns or "<span class=muted>Ask Anglia Morocco for a copy</span>"}</div></div>'
    _secs += f'<h2 id="{_re.sub(r"[^a-z]+", "-", _cat.lower()).strip("-")}">{_html.escape(_cat)}</h2><div class="packs">{_cards}</div>'
page("anglia-practice.html", "Practice papers & audio – Anglia Morocco | AGI Agadir",
 "Free Anglia practice papers and sample exams for every level: General English, Business English, Children's Oral Tests, Applied Translation and C.I.T.E. for teachers.",
 hero('<a href="anglia.html">Anglia Morocco</a> / <span>Practice papers</span>', "Practice resources.",
      "Practice papers and sample exams for every Anglia level, published by Anglia Examinations. Pick your level and download – then check your answers with your teacher.",
      '<a class="btn btn-primary" href="#general-english">Choose my level</a><a class="btn btn-ghost" href="anglia-books.html">Step To books &amp; audio</a>')
 + f'<section class="section bg-white"><div class="wrap"><p class="chips">' + "".join(f'<a class="btn btn-ghost" href="#{_re.sub(r"[^a-z]+", "-", c.lower()).strip("-")}">{_html.escape(c)}</a> ' for c, _, _ in _cat_rules) + f'</p>{_secs}<p class="muted" style="font-size:13px;margin-top:24px">Files are hosted by Anglia Examinations. Not sure of your level? <a href="forms.html#enquiry/anglia">Book a free level test</a>.</p></div></section>'
 + cta("Want guided preparation?", "Our classes and the Step To books prepare candidates for every level.", '<a class="btn btn-gold" href="anglia-classes.html">Classes &amp; prices</a><a class="btn btn-light" href="anglia-books.html">Step To books</a>'), ANGLIA_CSS + ANGLIA_THEME_CSS)

# ---------- STEP TO BOOKS (angliamorocco.org/step-to-books + audio files)
_series = [("First Step", ""), ("Junior", ""), ("Primary", ""), ("Preliminary", ""), ("Elementary", ""), ("Pre-Intermediate", ""), ("Intermediate", "B1 · Ofqual*"), ("Advanced", "B2 · Ofqual*"), ("Proficiency", "C1 · Ofqual*"), ("Masters", "C2 · Ofqual*")]
page("anglia-books.html", "Step To books – Anglia Morocco | AGI Agadir",
 "Anglia Step To books: ten workbooks from First Step to Masters (C2), with audio files, guided test practice and a sample exam. Order through Anglia Morocco in Agadir.",
 hero('<a href="anglia.html">Anglia Morocco</a> / <span>Step To books</span>', "Step To books.",
      "Specifically designed for students preparing for Anglia examinations from First Step to Masters (C2): 10–12 topic-based units, a QR code linking to audio files and a sample test, 110–128 full-colour pages.",
      '<a class="btn btn-primary" href="forms.html#books">Order books</a><a class="btn btn-ghost" href="#audio">Audio files</a>')
 + f'''<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>The Step To series</h2><p>Ten books set against the CEFR, from beginner to Masters.</p></div>
  <div class="series">{"".join(f"<div><b>{n}</b><small{' class=acc' if x else ''}>{x or '&nbsp;'}</small></div>" for n, x in _series)}</div>
  <p class="muted" style="font-size:13px;margin-top:12px">* Ofqual accredited through AIM Qualifications.</p>
</div></section>
<section class="section"><div class="wrap split"><div class="intro"><h2>The Step To approach</h2><p>A step-by-step approach to testing that encourages and motivates students to make clear and effective progress. Each book is researched and developed by professional ESOL experts.</p></div>
  <dl class="rows"><div><dt>Workbook</dt><dd>A Step To workbook with 10–12 topic-based units, covering high-frequency test topics and vocabulary</dd></div><div><dt>Test practice</dt><dd>Guided practice for every test section – listening, reading, writing and speaking</dd></div>
  <div><dt>Audio</dt><dd>Audio files, reached with the QR code in the book</dd></div><div><dt>Sample paper</dt><dd>A sample exam paper</dd></div><div><dt>Qualification</dt><dd>The opportunity to gain an Anglia ESOL international qualification</dd></div></dl></div></section>
<section class="section bg-white"><div class="wrap split"><div class="intro"><h2>Teachers' guide</h2></div><p class="prose">The accompanying teachers' guides make things easy: each is a comprehensive one-stop solution for test preparation, with instructions, language and cultural explanations, test tips and transcripts of all the recordings.</p></div></section>
<section class="section" id="audio"><div class="wrap"><div class="section-head"><h2>Audio files</h2><p>Free downloads for the Step To books.</p></div>
  <div class="packs"><div class="pack"><h3>First Step – Pre-Intermediate</h3><div class="dl"><a href="https://www.anglia.nl/uploads/1/2/0/0/120044573/audiofiles_step_to_fs_-_pre-intermediate__1_.zip" rel="noopener">Download audio</a></div></div>
  <div class="pack"><h3>Intermediate – Masters</h3><div class="dl"><a href="https://www.anglia.nl/uploads/1/2/0/0/120044573/audoifiles_step_to_intermediate_-_masters__1_.zip" rel="noopener">Download audio</a></div></div></div></div></section>
''' + cta("Order your Step To books.", "Order through Anglia Morocco in Agadir – the office confirms availability, price and delivery.", '<a class="btn btn-gold" href="forms.html#books">Order books</a><a class="btn btn-light" href="anglia-practice.html">Practice papers</a>'), ANGLIA_CSS + ANGLIA_THEME_CSS)

# ---------- hub hero with the logo + logo in the recognition strip
PAGES["anglia.html"] = PAGES["anglia.html"].replace('<section class="page-hero wrap">', f'<section class="page-hero wrap anglia-hub-hero"><div>', 1)
PAGES["anglia.html"] = _re.sub(r'(<section class="page-hero wrap anglia-hub-hero"><div>.*?</div>\s*)(</section>)', lambda m: m.group(1) + f'</div><img src="{ANGLIA_LOGO}" alt="Anglia Examinations England – Anglia Morocco" width="320" height="327">' + m.group(2), PAGES["anglia.html"], count=1, flags=_re.S)
PAGES["anglia.html"] = PAGES["anglia.html"].replace('<div class="section-head"><h2>Why Anglia</h2></div>', f'<div class="section-head"><h2>Why Anglia</h2></div><div class="recog-logo"><img src="{ANGLIA_LOGO}" alt="Anglia Examinations England" width="64" height="65"><span>AGI is the official Anglia Examinations franchise holder for Morocco.</span></div>', 1)
# every Anglia page: theme colors + logo badge
for _n in list(PAGES):
    if _n.startswith("anglia") and not _n.startswith(("fr/", "ar/")):
        h = PAGES[_n].replace('<main id="main" class="np">', '<main id="main" class="np anglia-theme">', 1)
        if _n != "anglia.html": h = h.replace('<section class="page-hero wrap">', f'<section class="page-hero wrap anglia-hero"><img class="anglia-badge" src="{ANGLIA_LOGO}" alt="Anglia Examinations England – Anglia Morocco" width="112" height="114">', 1)
        if "ANGLIA_THEME" not in h: h = h.replace("</head>", f"<style>/*ANGLIA_THEME*/{ANGLIA_THEME_CSS}</style>\n</head>", 1)
        PAGES[_n] = h


# ================================================================== 404 · SAFEGUARDING · ACCESSIBILITY
page("404.html", "Page not found – American Group International, Agadir", "The page you are looking for has moved or no longer exists.",
 hero("<span>Page not found</span>", "This page has moved.",
      "The AGI website has been rebuilt, so some old addresses no longer exist. Everything is still here – start from one of these pages, or ask us.",
      '<a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="contact.html">Contact</a>') + """
<section class="section bg-white"><div class="wrap"><div class="cards">
  <a class="card" href="parents.html"><span class="tag">Parents</span><h3>For parents</h3><span class="more">Open</span></a>
  <a class="card" href="admissions.html"><span class="tag">Admissions</span><h3>How to apply</h3><span class="more">Open</span></a>
  <a class="card" href="fees.html"><span class="tag">Fees</span><h3>Tuition &amp; fees</h3><span class="more">Open</span></a>
  <a class="card" href="calendar.html"><span class="tag">Dates</span><h3>Calendar 2026–27</h3><span class="more">Open</span></a>
  <a class="card" href="programs.html"><span class="tag">Programs</span><h3>All programs</h3><span class="more">Open</span></a>
  <a class="card" href="anglia.html"><span class="tag">Anglia Morocco</span><h3>English exams</h3><span class="more">Open</span></a>
  <a class="card" href="forms.html"><span class="tag">Forms</span><h3>Forms &amp; requests</h3><span class="more">Open</span></a>
  <a class="card" href="journal.html"><span class="tag">News</span><h3>Journal</h3><span class="more">Open</span></a>
  <a class="card" href="faq.html"><span class="tag">Help</span><h3>Questions &amp; answers</h3><span class="more">Open</span></a>
</div></div></section>""")
PAGES["404.html"] = PAGES["404.html"].replace("<head>", '<head>\n<meta name="robots" content="noindex">', 1)
# links in the 404 page must work from any folder depth -> absolute from the site root
PAGES["404.html"] = _re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/)', r'\1="/', PAGES["404.html"])

page("safeguarding.html", "Safeguarding & child protection – American Group International, Agadir",
 "How AGI keeps children safe: our commitments, photos and media consent, online safety, visitors, how to raise a concern, and children's personal data.",
 hero('<a href="policies.html">Policies</a> / <span>Safeguarding</span>', "Safeguarding &amp; child protection.",
      "Every child at AGI has the right to be safe, respected and heard. This page explains how the school protects children and how to raise a concern.",
      '<a class="btn btn-primary" href="#concern">Raise a concern</a><a class="btn btn-ghost" href="policies.html">All policies</a>') + f"""
<section class="section bg-white"><div class="wrap docwrap"><div class="doc" data-verify="legal-review:safeguarding">
  <h2 style="margin-top:0">Our commitments</h2>
  <ul><li>Children's safety and wellbeing come first in every decision.</li><li>Staff know the children and families they work with, and listen when a child speaks up.</li>
  <li>Concerns are taken seriously, recorded and acted on promptly.</li><li>We work with parents and, where needed, with the competent authorities.</li></ul>
  <h2 id="lead">Who is responsible</h2>
  <p>Designated safeguarding lead: {PH_TXT("safeguarding-lead", "name and role to be confirmed")}. Overall responsibility: Julie A. Wilburn, Founder · CEO &amp; Educational Director.</p>
  <h2 id="media">Photos, video and children's names</h2>
  <p>No child's photo, video or full name is published without written parental consent, in line with our <a href="media-policy.html">media policy</a> and Morocco's personal-data law (09-08). On this website, photos of children are hidden until that consent is confirmed.</p>
  <h2 id="online">Online safety</h2>
  <p>Students use school devices and online classes under the acceptable-use rules in the <a href="handbook.html">academic handbook</a>. Online lessons run on Zoom or Microsoft Teams with the school's instructions.</p>
  <h2 id="wellbeing">Wellbeing and support</h2>
  <p>Individual plans, small classes and holistic support help children who are struggling. AGI is a member of the American School Counselor Association. <a href="wellbeing.html">Wellbeing (i-Heart)</a> · <a href="special-education.html">Special education</a></p>
  <h2 id="visitors">Visitors</h2>
  <p>Visits to the school are by appointment and arranged individually. {PH_TXT("safeguarding-visitors", "Visitor sign-in and supervision procedure to be confirmed.")}</p>
  <h2 id="concern">How to raise a concern</h2>
  <p>If you are worried about a child's safety or wellbeing, speak to the school office or the safeguarding lead straight away – in person, by phone on <a href="tel:+212528843349">+212 528 843 349</a> or by email at <a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a>. You can also use the <a href="refunds-complaints.html">complaints procedure</a>. If a child is in immediate danger, contact the emergency services first.</p>
  <h2 id="data">Children's personal data</h2>
  <p>We collect only the information needed to educate and protect each child, keep it confidential and share it only with people who need it. <a href="privacy.html">Privacy policy</a></p>
  <p class="source-note">This page summarizes AGI's practice and will be completed once the full safeguarding policy is confirmed.</p>
</div><aside><p class="kicker">Related</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="media-policy.html">Media policy</a></li><li><a href="parent-responsibility.html">Parent responsibility</a></li><li><a href="handbook.html">Academic handbook</a></li><li><a href="privacy.html">Privacy</a></li></ul></aside></div></section>""", DOC_CSS)

page("accessibility.html", "Accessibility – American Group International, Agadir",
 "How the AGI website is made accessible (WCAG 2.1 AA), what is not yet fully accessible, and how to ask for help.",
 hero("<span>Accessibility</span>", "Accessibility.", "We want everyone to be able to use this website – on any device, in English, French or Arabic, with or without assistive technology.") + """
<section class="section bg-white"><div class="wrap docwrap"><div class="doc">
  <h2 style="margin-top:0">Our goal</h2><p>This website aims to meet the Web Content Accessibility Guidelines (WCAG) 2.1, level AA.</p>
  <h2>What we have done</h2>
  <ul><li>Text and background colors meet contrast requirements; text can be enlarged without breaking the layout.</li><li>Every page can be used with a keyboard, with a visible focus and a "skip to content" link.</li>
  <li>Pages use proper headings, labels and descriptions for screen readers; forms explain errors in words.</li><li>Pages work on phones and support right-to-left reading for Arabic.</li>
  <li>Animations are reduced when your device asks for reduced motion.</li></ul>
  <h2>What is not yet fully accessible</h2>
  <ul><li>Some older journal posts imported from the previous website may have long paragraphs or images without full descriptions.</li><li>Practice papers and books published by Anglia Examinations, and some older videos, are provided as they are and may not have captions or accessible formats.</li><li>French and Arabic versions cover the main pages only for now.</li></ul>
  <h2>Need help or found a problem?</h2><p>Tell us what you need and we will provide the information another way: <a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a> · <a href="tel:+212528843349">+212 528 843 349</a> · WhatsApp <a href="https://wa.me/212688739393" target="_blank" rel="noopener">+212 688 739 393</a>.</p>
  <p class="source-note">Last reviewed October 2026.</p>
</div></div></section>""", DOC_CSS)

# ================================================================== CONTENT QUALITY PASS (English pages)
for _n in list(PAGES):
    if not _n.startswith(("fr/", "ar/")): PAGES[_n] = split_languages(PAGES[_n], _n)
print("foreign blocks moved: ar", {k: len(v) for k, v in FOREIGN["ar"].items()}, "| fr", {k: len(v) for k, v in FOREIGN["fr"].items()})

# ================================================================== CLOSING CTA on every page without one
def _section_of(n):
    if n.startswith("anglia") or n in ("partnerships.html", "english-anglia.html"): return "anglia"
    if n in ("fees.html", "calendar.html", "handbook.html", "attendance.html", "promotion-retention.html", "placement-policy.html", "parent-responsibility.html",
             "refunds-complaints.html", "media-policy.html", "homework.html", "volunteer-hours.html", "supplies.html", "policies.html", "faq.html", "admissions.html"): return "admissions"
    if n.startswith(("teachers", "programs-", "services-", "wellbeing", "online-tutoring", "agi-usa", "professional", "adult-diploma", "pathways", "special-education", "k12")): return "programs"
    if n.startswith("resources") or n == "student-life.html": return "life"
    return "about"
_CTA = {"anglia": ("Find your English level.", "Book a free placement assessment, or ask us about classes and exam sessions.", '<a class="btn btn-gold" href="forms.html#enquiry/anglia">Book a free level test</a><a class="btn btn-light" href="calendar.html#anglia-exams">Exam dates</a>'),
        "admissions": ("Questions about joining AGI?", "Visit the school, or ask the office – we reply within one working day.", '<a class="btn btn-gold" href="forms.html#visit">Book a visit</a><a class="btn btn-light" href="forms.html#enquiry">Ask a question</a>'),
        "programs": ("Is this the right program?", "Tell us what you are looking for and we will help you choose.", '<a class="btn btn-gold" href="forms.html#enquiry/programs">Ask about this program</a><a class="btn btn-light" href="programs.html">All programs</a>'),
        "life": ("Come and see the school.", "Tours are arranged individually, Monday to Friday.", '<a class="btn btn-gold" href="forms.html#visit">Book a visit</a><a class="btn btn-light" href="parents.html">For parents</a>'),
        "about": ("Come and meet us.", "The best way to know AGI is to visit during the school day.", '<a class="btn btn-gold" href="forms.html#visit">Book a visit</a><a class="btn btn-light" href="contact.html">Contact</a>')}
_SKIP_CTA = {"404.html", "accessibility.html", "forms.html", "privacy.html", "terms.html", "cookies.html", "connect.html", "journal.html"}
for _n in list(PAGES):
    if _n.startswith(("fr/", "ar/")) or _n in _SKIP_CTA or "cta-band" in PAGES[_n]: continue
    _t, _x, _b = _CTA[_section_of(_n)]
    PAGES[_n] = PAGES[_n].replace("\n</main>", "\n" + cta(_t, _x, _b) + "\n</main>", 1)
