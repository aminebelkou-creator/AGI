"""Writes docs/rebuild-prompt-neutral.md: a technology- and design-neutral rebuild prompt with a description of every section of every page.
python _build/export_prompt_neutral.py   (regenerate after content changes)"""
import os, re, html, json
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
def txt(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()
def short(s, n=170): s = txt(s); return (s[:n].rsplit(" ", 1)[0] + "…") if len(s) > n else s
def main_of(s):
    m = re.search(r"<main\b.*?</main>", s, re.S); return m.group(0) if m else ""
def describe_section(sec, idx):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", sec, re.S); h2 = re.search(r"<h2[^>]*>(.*?)</h2>", sec, re.S)
    is_cta = "cta-band" in sec; full = "fulltext" in sec
    btns = [(txt(t), h) for h, t in re.findall(r'<a[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', sec, re.S)] + \
           [(txt(t), h) for h, t in re.findall(r'<a[^>]*href="([^"]+)"[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*>(.*?)</a>', sec, re.S)]
    cards = [txt(re.search(r"<h3[^>]*>(.*?)</h3>", c, re.S).group(1)) for c in re.findall(r'<a[^>]*class="[^"]*\bcard\b[^"]*"[^>]*>(.*?)</a>', sec, re.S) if re.search(r"<h3", c)]
    items = [txt(c) for c in re.findall(r"<h3[^>]*>(.*?)</h3>", sec, re.S)]
    lis = re.findall(r"<li\b[^>]*>(.*?)</li>", sec, re.S); rows = re.findall(r"<tr\b", sec); dts = re.findall(r"<dt\b[^>]*>(.*?)</dt>", sec, re.S)
    faqs = re.findall(r"<summary[^>]*>(.*?)</summary>", sec, re.S); photos = re.findall(r'data-placeholder="photo:([^"]+)"', sec)
    facts = re.findall(r'data-placeholder="fact:([^"]+)"', sec); tests = re.findall(r'data-placeholder="testimonial:', sec)
    paras = [p for p in re.findall(r"<p\b[^>]*>(.*?)</p>", sec, re.S) if len(txt(p)) > 40]
    imgs = [a for a in re.findall(r'<img[^>]*alt="([^"]*)"', sec) if a]
    if h1: title = "Page introduction"; head = txt(h1.group(1))
    elif is_cta: title = "Closing call to action"; head = txt(h2.group(1)) if h2 else ""
    else: title = txt(h2.group(1)) if h2 else ("Section " + str(idx)); head = ""
    parts = []
    if head: parts.append(f"Main heading: “{head}”.")
    if paras: parts.append("Text: " + short(paras[0]) + (f" (+{len(paras) - 1} more paragraph{'s' if len(paras) > 2 else ''})" if len(paras) > 1 else ""))
    if cards: parts.append(f"{len(cards)} linked items: " + "; ".join(cards[:10]) + ("…" if len(cards) > 10 else "") + ".")
    elif items and not faqs: parts.append(f"{len(items)} sub-items: " + "; ".join(i[:60] for i in items[:10]) + ("…" if len(items) > 10 else "") + ".")
    if dts: parts.append(f"{len(dts)} labelled facts/rows: " + "; ".join(txt(d)[:45] for d in dts[:10]) + ("…" if len(dts) > 10 else "") + ".")
    if rows: parts.append(f"A table with {len(rows)} rows" + (": " + " | ".join(txt(x) for x in re.findall(r"<th[^>]*>(.*?)</th>", sec, re.S)[:5]) if re.search(r"<th", sec) else "") + ".")
    if lis and not cards and not dts and not rows: parts.append(f"A list of {len(lis)} items: " + "; ".join(txt(l)[:50] for l in lis[:6]) + ("…" if len(lis) > 6 else "") + ".")
    if faqs: parts.append(f"{len(faqs)} questions with expandable answers: " + "; ".join(txt(q)[:60] for q in faqs[:5]) + ("…" if len(faqs) > 5 else "") + ".")
    if full: parts.append("Includes AGI's original full text in an expandable part (keep all of it).")
    if imgs: parts.append("Images: " + "; ".join(imgs[:3]) + ".")
    if photos: parts.append(f"{len(photos)} photo placeholder(s) to keep: " + ", ".join(photos[:6]) + ".")
    if tests: parts.append(f"{len(tests)} sample testimonial(s), marked as samples.")
    if facts: parts.append(f"Facts awaiting confirmation (keep marked): " + ", ".join(sorted(set(facts))[:6]) + ".")
    if btns: parts.append("Actions: " + "; ".join(f"“{t}” → {h}" for t, h in btns[:4]) + ".")
    return title, " ".join(parts) or "Supporting content."
def page_block(f):
    s = open(os.path.join(V2, f), encoding="utf-8").read(); m = main_of(s)
    title = txt((re.search(r"<title>(.*?)</title>", s, re.S) or [None, f])[1]); desc = (re.search(r'<meta name="description" content="([^"]*)"', s) or [None, ""])[1]
    secs = re.findall(r"<section\b.*?</section>", m, re.S)
    out = [f"### `{f}` – {html.unescape(title)}", f"*Purpose:* {html.unescape(desc)}", ""]
    for i, sec in enumerate(secs, 1):
        t, d = describe_section(sec, i); out.append(f"{i}. **{t}** – {d}")
    if re.search(r"<dialog", m): out.append(f"{len(secs) + 1}. **Invitation for parents (home page only)** – an invitation that appears after the visitor has read half the page or is about to leave, at most once a week, and never blocks the page on small screens; it leads to parents.html.")
    return "\n".join(out) + "\n"
ORDER = ["index.html", "parents.html", "our-story.html", "founder-letter.html", "about.html", "investors.html", "agi-usa.html",
         "admissions.html", "fees.html", "calendar.html", "faq.html", "policies.html", "handbook.html", "attendance.html", "promotion-retention.html", "placement-policy.html",
         "parent-responsibility.html", "refunds-complaints.html", "media-policy.html", "homework.html", "volunteer-hours.html", "supplies.html", "safeguarding.html",
         "programs.html", "k12.html", "special-education.html", "adult-diploma.html", "pathways.html", "professional.html", "teachers.html", "teachers-cite.html",
         "teachers-usa-sponsorship.html", "teachers-careers.html", "programs-independent-studies.html", "programs-learning-pods.html", "services-document-editing.html",
         "services-proctoring.html", "wellbeing.html", "wellbeing-adhd-coaching.html", "wellbeing-play-therapy.html", "online-tutoring.html",
         "anglia.html", "anglia-exams.html", "anglia-exam-dates.html", "anglia-classes.html", "anglia-practice.html", "anglia-books.html", "anglia-cefr.html",
         "anglia-special-arrangements.html", "anglia-placement-test.html", "anglia-network.html", "anglia-faq.html", "anglia-about.html", "english-anglia.html", "partnerships.html",
         "student-life.html", "resources.html", "resources-nursery-rhymes.html", "resources-mcguffey.html", "journal.html", "journal-ccgi-partnership.html",
         "forms.html", "contact.html", "connect.html", "privacy.html", "terms.html", "cookies.html", "accessibility.html", "404.html"]
ORDER += [f for f in sorted(os.listdir(V2)) if f.endswith(".html") and f not in ORDER and not f.startswith("_")]
GROUPS = [("Home and parents", ORDER[0:7]), ("Admissions, fees, calendar and policies", ORDER[7:23]), ("Programs and services", ORDER[23:41]),
          ("Anglia Morocco section", ORDER[41:55]), ("Student life, resources and journal", ORDER[55:61]), ("Forms, contact and legal", ORDER[61:])]
spec_forms = open(os.path.join(ROOT, "docs", "website-content-spec.md"), encoding="utf-8").read()
forms = re.findall(r"#### Form: (.+?) \(`forms\.html#([a-z-]+)`\)", spec_forms)
journal_n = len([f for f in os.listdir(os.path.join(V2, "journal")) if f.endswith(".html") and not f.startswith("_")])
fr = sorted(os.listdir(os.path.join(V2, "fr"))); ar = sorted(os.listdir(os.path.join(V2, "ar")))
facts = json.load(open(os.path.join(V2, "_build", "facts.json"), encoding="utf-8"))
F = lambda g, k: facts[g][k]["value"]
doc = [f"""# Rebuild prompt – AGI website (technology- and design-neutral)

*Generated by `v2/_build/export_prompt_neutral.py` from the built site. It describes **what** the website must contain and do – every page and every section – and leaves **all technology and visual design choices** to you.*

**Attach:** `docs/website-content-spec.md` (exact copy of every page and form) and `v2/_build/facts.json` (fees, dates, contacts). Optional: `data/export/AGI_Website_Content_Export.json` (journal articles), `v2/_build/redirects.csv` and `docs/angliamorocco-redirects.htaccess` (old addresses), `v2/assets/` (logos, images, files).

---

## The prompt

```
Build the website of American Group International (AGI) – an American-curriculum school in Agadir,
Morocco (kindergarten to grade 12, special education, adult diploma, teacher certification,
professional English) and the headquarters of Anglia Examinations Morocco (official English exams
from England). It is ONE website: the former angliamorocco.org site becomes its "Anglia Morocco"
section and its old addresses redirect there.

You choose the technology, the visual design, the colors, the typography and the layout.
What you must reproduce is the content, the structure, the behaviors and the rules below.
The section descriptions in this document say what each part of each page is for and what it
contains; the attached content spec gives the exact wording. Use the exact wording.

Audiences: parents (priority), students and English learners, adults and professionals, teachers,
schools and partners, current families (forms).
Brand line: "Affordable · Creative · Inclusive" and "School + Home + Community = Student Success".
Two brands live on the site: AGI (whole site) and Anglia Examinations / Anglia Morocco (its section,
with its own approved logo and brand colors – ask for the logo file and colors; keep that section
recognizably Anglia while consistent with the rest of the site).

Build:
- {len(ORDER)} main pages (listed below with every section), {journal_n} journal articles, a journal list grouped by year,
  French pages ({", ".join(fr)}) and Arabic pages ({", ".join(ar)}; right-to-left).
- One navigation menu and one footer on every page; a language switch EN / FR / AR; breadcrumbs on inner pages;
  a WhatsApp contact on every page; a "page not found" page.
- {len(forms)} forms (listed below) – each can be opened directly from a link; forms must never collect card numbers.
- Keep the same page addresses (URLs) so the old redirects keep working.

Rules (non-negotiable):
- Use only the facts in the spec and facts.json. Never invent fees, dates, names or claims.
- Items marked as placeholders – photos to supply, facts "to confirm", sample testimonials, team names,
  translation reviews – stay visibly marked AND machine-detectable until AGI resolves them.
- Never publish a child's name or photo without written parental consent: some journal posts must show
  "Photo hidden until parental consent is confirmed" instead of their photos.
- Do not publish unconfirmed claims ("exclusive" franchise; expansion to other cities, Mauritania or the
  USA; "Director of Global Operations"; Anglia "dependent on the UK Ministry of Education", British Council
  or QCA recognition). Anglia wording: "official partner in Morocco of Chichester College Group, UK";
  "the four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual";
  "the Mastery (C2) qualification carries UCAS tariff points".
- Quote exactly: "Grade placement is not lowered due to missing documents, language gaps, or academic gaps."
- Journal posts older than 12 months show a note that fees and dates may have changed, linking to the
  current fees and calendar.
- One official email (americanecoleagadir@gmail.com); never link to angliamorocco.org.

Quality: accessible (WCAG 2.1 AA), fast on mobile, readable on any screen without sideways scrolling,
search-engine ready (the titles and descriptions given), no broken links. Report every remaining placeholder.
Ask before deviating; flag contradictions instead of guessing.
```

---

## 1. Key facts (from facts.json – change them only there)

- Contact: {F("contact","address")} · {F("contact","phone_main")} · Arabic {F("contact","phone_arabic")} · WhatsApp {F("contact","whatsapp_english")} · {F("contact","email_official")}
- Tuition: {F("fees","tuition_monthly")}; inscription by grade: {"; ".join(f"{k}: {v}" for k, v in F("fees","inscription").items())}; {F("fees","included")}
- 2026–27: registration August 28 & 31 · first day September 7 · last day and graduation June 17, 2027
- Eligibility: {F("school","eligibility")} · attendance minimum {F("school","attendance_minimum")} · pass mark {F("school","pass_mark")} · service hours {F("school","service_hours")}

## 2. Site-wide elements

- **Navigation menu:** About · Programs (K–12 school, special education, adult diploma, English & Anglia exams, teachers, professional & medical English, university pathways, wellbeing, online tutoring, all programs) · Admissions · Student life · Journal · Anglia Morocco · Contact; plus "Forms", "Apply" and the language switch.
- **Footer:** short description of AGI; links to programs, school pages, services and legal pages (privacy, terms, cookies, accessibility, safeguarding); full contact details.
- **Every page ends with a call to action** suited to its section (book a visit, ask a question, book a free English level test, ask about a program).
- **Long original texts** (policies, handbook, program texts) are kept in full; where a page already summarizes them, the full text sits in an expandable part.

## 3. Pages and their sections
"""]
for g, files in GROUPS:
    doc.append(f"\n## {g}\n")
    for f in files:
        if os.path.exists(os.path.join(V2, f)): doc.append(page_block(f))
doc.append(f"""
## Journal articles ({journal_n})
Each article: page introduction (category, title, date), the article text with its images (or the privacy note), an "archived" note when older than 12 months, links to the previous/next articles and to the journal list. The journal list groups all articles by year, newest first, with category and a short excerpt.

## French and Arabic pages
French: {", ".join(fr)}. Arabic (right-to-left): {", ".join(ar)}. They mirror the English pages' sections in shorter form (the Arabic Anglia hub and seven Arabic pages use AGI's own Arabic texts). Every translated page is marked for native-speaker review.

## Forms ({len(forms)}) – fields in section 5 of the content spec
""" + "\n".join(f"- **{t}** (`forms.html#{i}`)" for t, i in forms) + """

Each form shows: what it is for, how long it takes, what to have ready, what happens next, grouped fields with clear required/optional marks, and a confirmation after sending. Until a backend exists, sending opens the visitor's email to americanecoleagadir@gmail.com with the details, with "copy details" and WhatsApp as alternatives.

## Behaviors to reproduce
- Invitation for parents on the home page (see the home page description).
- Anglia exam dates: a filter between upcoming sessions and the whole year; the Anglia home shows the next session automatically.
- Language switch goes to the same page in the other language when it exists.
- Old addresses (147 from the former AGI site, 33 from angliamorocco.org) redirect permanently to their new pages.
""")
open(os.path.join(ROOT, "docs", "rebuild-prompt-neutral.md"), "w", encoding="utf-8").write("\n".join(doc))
print(f"docs/rebuild-prompt-neutral.md: {len(ORDER)} pages described, {len(forms)} forms, {len(' '.join(doc).split())} words")
