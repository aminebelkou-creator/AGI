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
    if lines and _re.search(r"[–-] American Group International|W25317017", lines[0]): lines = lines[1:]
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
