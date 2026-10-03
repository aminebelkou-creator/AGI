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
_BUL = _re.compile(r"^\s*(?:[-•*·]|ÔÇó|\u2022)\s+")
_NUM = _re.compile(r"^\s*(\d{1,2})[.)]\s+")
def _is_heading(l):
    if l.startswith("#"): return True
    t = l.strip(); letters = _re.sub(r"[^A-Za-z]", "", t)
    return 3 < len(t) < 70 and len(letters) > 3 and t.upper() == t and not _re.search(r"\d{3,}", t)
def render(text, skip=(), privacy=False, start=None, stop=None, toc=False):
    """Turn crawled text into clean HTML: headings, lists, paragraphs. Keeps every line (except skip/privacy)."""
    lines = text.split("\n")
    if lines and _re.search(r"[–-] American Group International|W25317017|[–-] Anglia Morocco\s*$", lines[0]): lines = lines[1:]
    if start: lines = lines[next((i for i, l in enumerate(lines) if start in l), 0):]
    if stop: lines = lines[:next((i for i, l in enumerate(lines) if stop in l), len(lines))]
    out, lst, heads = [], None, []
    def close():
        nonlocal lst
        if lst: out.append(f"</{lst}>"); lst = None
    for l in lines:
        l = l.strip()
        if not l or any(s in l for s in skip): continue
        if privacy and (_re.search(r"[\w.+-]+@[\w-]+\.\w+", l) and "americanecoleagadir" not in l or _re.search(r"(?:\+?212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}", l)): continue
        if _is_heading(l):
            close(); t = l.lstrip("#").strip(); lvl = 2 if (l.startswith("#") and len(l) - len(l.lstrip("#")) <= 2) or not l.startswith("#") else 3
            if len(t) > 90: out.append(f"<p><strong>{_html.escape(t)}</strong></p>"); continue
            hid = _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:50]
            if lvl == 2: heads.append((hid, t.title() if t.isupper() else t))
            out.append(f'<h{lvl} id="{hid}">{_html.escape(t.title() if t.isupper() else t)}</h{lvl}>'); continue
        m = _BUL.match(l); n = _NUM.match(l)
        if m or n:
            kind = "ul" if m else "ol"
            if lst != kind: close(); out.append(f"<{kind}>"); lst = kind
            out.append(f"<li>{_html.escape(l[(m or n).end():])}</li>"); continue
        close(); out.append(f"<p>{_html.escape(l)}</p>")
    close()
    body = "\n".join(out)
    if toc and len(heads) >= 4:
        body = ('<nav class="toc" aria-label="On this page"><p class="kicker">On this page</p><ol>' + "".join(f'<li><a href="#{h}">{_html.escape(t)}</a></li>' for h, t in heads) + "</ol></nav>\n" + body)
    return body

DOC_CSS = """
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
    srcs = ", ".join(f'<a href="{SRC(p)["url"]}" rel="nofollow">{_html.escape(SRC(p)["title"])}</a>' for p in parts)
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
            ["homework-guidelines"], "AGI homework guidelines by grade, from kindergarten to grade 12.")
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
 "AGI tuition and fees 2026–27: annual inscription by grade (6,500–11,000 MAD), tuition 2,600 MAD a month, all-inclusive package, high school options, Anglia class prices.",
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
  {render(SRC("anglia-exam-dates")["text"])}
  <p><a class="link" href="english-anglia.html">English &amp; Anglia exams</a></p>
  <details class="archive"><summary>Archive: school calendar 2025–26</summary>{render(_cal, stop="AMERICAN GROUP INTERNATIONAL")}</details>
</div>
<aside><p class="kicker">Key dates</p><dl class="rows" style="border-top:0">
  <div><dt>Registration</dt><dd>Aug 28 &amp; 31</dd></div><div><dt>First day</dt><dd>Sept 7</dd></div><div><dt>Last day &amp; graduation</dt><dd>June 17, 2027</dd></div></dl>
  <p><a class="link" href="forms.html#visit">Book a visit</a></p></aside>
</div></section>""", DOC_CSS)

# ------------------------------------------------------------------ SPECIAL EDUCATION: full source text (private contact details filtered)
_se = render(SRC("location-physical")["text"], privacy=True)
PAGES["special-education.html"] = PAGES["special-education.html"].replace("\n</main>", f'''
<section class="section bg-white" id="details"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">Special education services in detail</h2>{_se}</div>
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
_faq_html = "".join(f'<h2 id="{_re.sub(r"[^a-z]+", "-", g.lower()).strip("-")}">{g}</h2><div class="faq">' + "".join(
    f'<details><summary>{q}</summary><p>{a} <a class="link" href="{l}">More</a></p></details>' for q, a, l in qs) + "</div>" for g, qs in FAQ)
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
    blk = f"<!--p1:{key}-->\n{inner}\n<!--/p1:{key}-->"
    t = _re.sub(r"<!--p1:%s-->.*?<!--/p1:%s-->\n?" % (key, key), "", t, flags=re.S)
    if "<style id=\"doc-css\">" not in t: t = t.replace("</head>", f'<style id="doc-css">{DOC_CSS}</style>\n</head>', 1)
    t = t.replace("</main>", blk + "\n</main>", 1)
    open(fp, "w", encoding="utf-8", newline="").write(t)
inject_static("admissions.html", "full", '<section class="section bg-white np" id="procedure"><div class="wrap docwrap"><div class="doc">'
  + '<h2 style="margin-top:0">Admissions procedure in full</h2>' + render(SRC("admissions-procedure")["text"])
  + '<h2 id="enrollment-documents">Enrollment documents</h2>' + render(SRC("/enrollment")["text"], stop="rification de l")
  + render(SRC("admission-prossess")["text"]) + '</div><aside><p class="kicker">Next steps</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px">'
  + '<li><a href="fees.html">Tuition &amp; fees</a></li><li><a href="calendar.html">Calendar 2026–27</a></li><li><a href="placement-policy.html">Placement policy</a></li><li><a href="forms.html#enrollment">Apply</a></li><li><a href="faq.html">Questions &amp; answers</a></li></ul></aside></div></section>')
import csv as _csv
_MAP = list(_csv.DictReader(open(os.path.join(os.path.dirname(V2), "docs", "content-map.csv"), encoding="utf-8-sig")))
def MAPPED(dest): return [r["url"] for r in _MAP if r["destination"] == dest and r["action"] != "drop"]
_k12_src = MAPPED("k12.html")
inject_static("k12.html", "full", '<section class="section bg-white np" id="about-the-school"><div class="wrap docwrap"><div class="doc">'
  + '<h2 style="margin-top:0">About the school in detail</h2>' + "".join(render(SRC(u)["text"], privacy=True) for u in _k12_src)
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
    return "".join(f'<h2>{heading if i == 0 else ""}</h2>' * (i == 0) + render(p["text"], skip=skip, privacy=True) for i, p in enumerate(srcs_for(dest)) if p["text"])

LEVELS = [("First Step", "Pre-A1", "Entry level from about age 4: understands about 100 words, follows basic classroom instructions, says who they are."),
 ("Junior", "Pre-A1", "Understands around 200 words, uses useful structures and explains what they are doing."),
 ("Primary", "A1-", "About 400 words (jobs, feelings, weather); forms questions, answers them and describes things."),
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
    if t and (h, t) not in _links: _links.append((h, t))
_groups = {}
for h, t in _links:
    lv = next((L for L, _, _ in LEVELS if L.lower().replace(" ", "-") in h.lower() or L.lower() in t.lower()), "Other")
    _groups.setdefault(lv, []).append((h, t))
_pk = "".join(f"<h3>{lv}</h3><ul>" + "".join(f'<li><a href="{h}" rel="noopener">{_html.escape(t)}</a></li>' for h, t in L) + "</ul>" for lv, L in _groups.items())
_audio = "".join(f'<li><a href="{h}" rel="noopener">{lab}</a></li>' for h, lab in [
    ("https://www.anglia.nl/uploads/1/2/0/0/120044573/audiofiles_step_to_fs_-_pre-intermediate__1_.zip", "Step To audio files: First Step to Pre-Intermediate"),
    ("https://www.anglia.nl/uploads/1/2/0/0/120044573/audoifiles_step_to_intermediate_-_masters__1_.zip", "Step To audio files: Intermediate to Masters")])
anglia_page("anglia-practice.html", "Practice papers &amp; audio", "Free sample papers for every level, published by Anglia Examinations, plus the audio files for the Step To books.",
 render(SRC("practice-resources")["text"], stop="Pick Your Level") + f"<h2>Practice packs by level</h2>{_pk or '<p>Download links are on angliamorocco.org.</p>'}<h2>Audio files</h2><ul>{_audio}</ul>"
 + full("anglia-practice.html", skip=("Pack", "First Step", "Junior", "Primary", "Preliminary", "Elementary", "Intermediate", "Advanced", "CLICK TO DOWNLOAD")),
 "Free Anglia practice papers for every level (First Step to Advanced, Business English) and Step To audio files.")

anglia_page("anglia-books.html", "Step To books", "Preparation books for each Anglia level, with audio files – order through Anglia Morocco.",
 full("anglia-books.html", heading="Step To books") + f'<h2>Audio files</h2><ul>{_audio}</ul><p><a class="btn btn-primary" href="forms.html#enquiry/anglia">Order books</a></p>',
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
 + f'''<section class="section bg-white"><div class="wrap"><div class="cards">{_cards}</div></div></section>
<section class="section"><div class="wrap docwrap"><div class="doc">{render(_home["text"], privacy=True)}
<h2>Club Anglia</h2><p>{PH_TXT("club-anglia", "Coming soon.")}</p>
<p><a class="link" href="https://angliamorocco.org/" target="_blank" rel="noopener">angliamorocco.org</a></p></div>
<aside><p class="kicker">Contacts</p><p class="muted" style="font-size:14px">Julie Wilburn · <a href="mailto:j.wilburn@angliamorocco.org">j.wilburn@angliamorocco.org</a><br>Abdelhak Lam · <a href="mailto:a.lam@angliamorocco.org">a.lam@angliamorocco.org</a></p></aside></div></section>''', DOC_CSS)

# partnerships (static page): full source text
inject_static("partnerships.html", "full", '<section class="section bg-white np" id="partner-with-us"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">Partner with AGI and Anglia Morocco</h2>'
  + "".join(render(SRC(u)["text"], privacy=True) for u in MAPPED("partnerships.html")) + '</div><aside><p class="kicker">Anglia Morocco</p><ul style="list-style:none;padding:0;margin:0;display:grid;gap:10px"><li><a href="anglia-network.html">Network &amp; centres</a></li><li><a href="anglia.html">Anglia Morocco</a></li><li><a href="investors.html">Partners &amp; investors</a></li></ul></aside></div></section>')

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
 "Document editing in English by AGI, Agadir.", crumb="Document editing")
section_page("services-proctoring.html", "Adults & professionals", "Exam proctoring",
 "Paper and online exams invigilated at AGI for distance learners of North American and British universities, companies and certification bodies.",
 "<p style=\"margin-top:0\"><b>Monday to Thursday, 9:00–17:00.</b> A 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour.</p>",
 "Exam proctoring at AGI Agadir: exams, fees per exam and conditions.", crumb="Proctoring")
section_page("wellbeing.html", "Wellbeing (i-Heart)", "i-Heart therapeutic services",
 "Holistic support for children, teens and adults – coaching, therapeutic play and counseling, alongside school.",
 '<div class="cards" style="--cols:2;margin-bottom:28px"><a class="card" href="wellbeing-adhd-coaching.html"><h3>ADHD holistic coaching</h3><p>Focus, organization and time management for children and adults.</p><span class="more">Learn more</span></a><a class="card" href="wellbeing-play-therapy.html"><h3>Holistic play therapy</h3><p>Guided therapeutic play for emotional, social and behavioral development.</p><span class="more">Learn more</span></a></div>',
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
<section class="section bg-white" id="details"><div class="wrap docwrap"><div class="doc"><h2 style="margin-top:0">{title}</h2>{full(name, heading="")}</div>
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
 '<div class="cards" style="--cols:2;margin-bottom:28px"><a class="card" href="resources-nursery-rhymes.html"><h3>Nursery rhymes for Pre-K</h3><span class="more">Open</span></a><a class="card" href="resources-mcguffey.html"><h3>McGuffey readers &amp; sight words</h3><span class="more">Open</span></a></div>')
resource_page("resources-nursery-rhymes.html", "Nursery rhymes for Pre-K", "Traditional English rhymes to read and sing with young children.",
 "Traditional English nursery rhymes for pre-kindergarten children – read and sing at home.")
resource_page("resources-mcguffey.html", "McGuffey readers &amp; sight words", "Classic McGuffey reading lessons and sight words for reading and spelling practice at home.",
 "McGuffey readers and sight words: classic reading and spelling practice for children (public domain).")

# Journal: list posts that exist only on angliamorocco.org
_ang_posts = [r for r in _MAP if r["site"] == "anglia" and r["destination"].startswith("journal/")]
if _ang_posts:
    inject_static("journal.html", "anglia-news", '<section class="section bg-white np" id="anglia-news"><div class="wrap"><div class="section-head"><h2>From Anglia Morocco</h2><p>News first published on angliamorocco.org.</p></div><div class="cards">'
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
