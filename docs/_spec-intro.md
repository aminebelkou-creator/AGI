# AGI website – content and structure specification

*For rebuilding the website of American Group International (AGI), Agadir. Version 1 · October 2026.*

**This document describes what the website must contain and do – not how it should look.** It contains no visual design decisions (no colors, fonts, layouts, imagery style or component styling). Section 4 and 5 are generated from the current site by `v2/_build/export_spec.py`; re-run it after content changes.

**How to use it:** build every page in section 4 with its sections in the given order and its exact copy; implement the forms in section 5; follow the requirements in 3.5 and the content rules in 3.6. Items marked `[TO CONFIRM]`, `[PHOTO NEEDED]` or `[SAMPLE]` are placeholders – keep them clearly identifiable so they can be replaced before launch.

---

## 1. Overview

**Organization.** American Group International (AGI) – an American-curriculum school in Agadir, Morocco, founded in 2013 with five children in one room. Today: a K–12 micro-school in Hay Nahda (eight multi-grade classrooms, students of 46+ nationalities), programs for adults, English learners, teachers and professionals, and the headquarters of **Anglia Examinations Morocco** (franchise holder since 2021, official partner in Morocco of Chichester College Group, UK).

**Founder.** Julie A. Wilburn – Founder · CEO & Educational Director · Anglia Examinations Morocco, American Group International of Agadir.

**Brand line.** Slogan: **Affordable · Creative · Inclusive**. Motto: **School + Home + Community = Student Success**. Mission line: **Global Minds with a Global Perspective**.

**Website purpose.**
1. Earn parents' trust and turn it into **visits booked** and **applications**.
2. Present every program clearly to its audience.
3. Let families do school business online (absence reports, consent, payments notices, documents) through forms.
4. Replace the old WordPress site (americangroup-international.com) without losing search rankings (redirects) or news history (journal).

**Language.** English (US spelling). French and Arabic (right-to-left) versions are planned for the main pages; the structure must allow adding languages later.

---

## 2. Audiences and goals

| Audience | What they need | Main page | Primary action |
|---|---|---|---|
| **Parents** (priority) | Trust, a fair price, support for their child, clear admissions | `parents.html`, `our-story.html`, home | Book a visit · WhatsApp · Apply |
| **Students & English learners** | Certified English, classes, prices | `english-anglia.html` | Book a free level test |
| **Teachers** | C.I.T.E. certificate, training, internship | `teachers.html` | Register for C.I.T.E. · Ask about the internship |
| **Professionals & clinicians** | Business / medical English, proctoring | `professional.html` | Book a level test · Request a team course |
| **Partners & investors** | The model, partnership routes | `investors.html`, `partnerships.html` | Request the partner brief |
| **Current families** | Absence, consent, feedback, payment notice, documents | `forms.html` | Send a form |

---

## 3. Structure and global elements

### 3.1 Sitemap

```
Home (index.html)
├── About (about.html)
│   ├── Our story (our-story.html)              ← landing page, linked from the home popup
│   └── A letter from our founder (founder-letter.html)
├── Programs (programs.html)
│   ├── K–12 school (k12.html)
│   ├── Special education (special-education.html)
│   ├── Adult high school diploma (adult-diploma.html)
│   ├── English & Anglia exams (english-anglia.html)
│   ├── For teachers – C.I.T.E. (teachers.html)
│   ├── Professional & medical English (professional.html)
│   └── University pathways (pathways.html)
├── Admissions (admissions.html)  – incl. tuition & fees (#fees)
│   └── Policies (policies.html)
├── For parents (parents.html)
├── Student life (student-life.html)
├── Journal (journal.html)
│   ├── journal/<slug>.html  (59 articles from the old site)
│   └── journal-ccgi-partnership.html (featured article)
├── Partnerships & franchise (partnerships.html)
│   └── Partners & investors (investors.html)
├── Forms & requests (forms.html)  – 10 forms, deep-linkable (#enrollment, #visit, #absence, #consent, #feedback, #payment, #tutor-request, #tutor-schedule, #documents, #enquiry)
├── Contact (contact.html)
│   └── AGI Connect – preview (connect.html)
├── Privacy (privacy.html)
└── Terms (terms.html)
```

### 3.2 Header navigation (identical on every page)

- Brand: "AGI" + "American Group International School · Agadir" → home.
- Main menu: **About** · **Programs** (submenu: K–12 school – *American curriculum, kindergarten to grade 12*; Special education (SEN) – *IEPs, small groups, therapy support*; Adult high school diploma – *U.S. diploma for learners 16 and over*; English & Anglia exams – *Anglia Morocco headquarters, classes and exams*; For teachers (C.I.T.E.) – *Lifelong certificate, training, 30-day internship*; Professional & medical English – *Business and medical English, proctoring, coaching*; University pathways – *Admissions agent for universities abroad*; All programs) · **Admissions** · **Student life** · **Journal** · **Partnerships** · **Contact**.
- Utility link: **Forms** → forms.html. Primary action: **Apply** → forms.html#enrollment.
- The current page/section is indicated in the menu. On small screens the menu collapses into an openable panel listing all items (programs as sub-items) plus "Forms & requests" and Apply.
- A "Skip to content" link is the first focusable element.

### 3.3 Footer (identical on every page)

- About line: *American Group International – the first American school in Agadir, since 2013, and headquarters of Anglia Examinations in Morocco.*
- **Programs:** the seven programs.
- **School:** About AGI · Our story · For parents · Admissions · Tuition & fees · Policies · Student life · Journal.
- **Services:** Forms & requests · Report an absence · Request a document · Book a visit · Partnerships & franchise · Partners & investors · AGI Connect (preview) · Anglia Morocco ↗ (angliamorocco.org, new tab).
- **Contact:** Number 20, Rue Baalabek, Hay Nahda, Agadir 80000, Morocco · +212 528 843 349 · +212 618 639 911 (Arabic) · WhatsApp +212 688 739 393 · americanecoleagadir@gmail.com.
- Bottom line: © 2026 American Group International · Agadir, Morocco · Privacy · Terms · Contact.

### 3.4 Global elements and behaviors

- **WhatsApp contact** available on every page (link `https://wa.me/212688739393` with a pre-filled "Hello AGI," message, opens in a new tab), labelled "WhatsApp"; on small screens it may show an icon only but must keep an accessible label.
- **Story popup (home page only).** A modal dialog inviting parents to the Our story page.
  - Content: kicker "Our story" · heading **"Your child, known by name."** · text *"Since 2013, AGI has grown from one small classroom into a school trusted by families from more than 46 nations. Discover why parents choose us."* · three labels: Affordable, Creative, Inclusive · [PHOTO NEEDED – AGI's early days, or Julie with students] · actions **Discover our story** (→ our-story.html) and **Not now** (closes).
  - Behavior: opens once, 6 seconds after load **or** when the visitor has scrolled 25% of the page, whichever comes first; then not again for 7 days (remembered in the browser). Closes with the close button, "Not now", the Escape key, or a click outside. Must trap focus while open and return focus afterwards. Must not open if another dialog is open. [TO CONFIRM: timing and frequency with Julie]
  - The home hero also contains a permanent "Our story" link.
- **Map** of the school (20 Rue Baalabek, Hay Nahda, Agadir) on the home and contact pages, plus an "Open in Google Maps" link. [TO CONFIRM: pin location]
- **Breadcrumbs** on inner pages (e.g. Home / Programs / English & Anglia exams).
- **No cookies or tracking** are used by the site itself; fonts or maps from third parties must be mentioned in the privacy policy.

### 3.5 Functional requirements

1. **Accessibility:** WCAG 2.1 AA – semantic headings (one H1 per page), keyboard-operable menus and dialogs, visible focus, text contrast ≥ 4.5:1, labels and error messages tied to form fields, alt text for meaningful images, reduced-motion respected.
2. **Performance:** mobile-first; images in modern formats and lazy-loaded below the first screen; fonts must not block rendering; target Lighthouse ≥ 95 in all categories on mobile.
3. **SEO:** unique title (≤ 65 characters) and meta description (70–160) per page (provided in section 4); canonical URLs; Open Graph/Twitter tags; `School` structured data on the home page (name, address, phone, email, founding year 2013); `sitemap.xml`; `robots.txt`.
4. **Redirects:** 301 redirects from every old WordPress address (68 pages, 60 posts) to the matching new page – mapping in `v2/_build/redirects.csv`; news posts move from `/<slug>/` to `/journal/<slug>.html`.
5. **Forms:** see section 5. Validation messages appear after a field is left, not while typing. Until a backend exists, a submitted form opens the visitor's email app pre-filled to americanecoleagadir@gmail.com, with "Copy details" and WhatsApp as fallbacks. With a backend: one endpoint receiving `{type, name, email, phone, payload}`, storing submissions and emailing the office. **Never collect card numbers**; card payments go to AGI's existing secure payment page (Omella).
6. **Deep links:** every form and key section must be addressable (e.g. `admissions.html#fees`, `about.html#accreditation`, `forms.html#documents/transcript` preselects "Academic transcript", `forms.html#enquiry/partnership` preselects the partnership topic).
7. **Journal:** a list of all posts grouped by year with category labels, and one page per post with date, category, full text, images stored on the new site, and links to newer/older posts.
8. **Placeholders:** photos, sample testimonials, team names and unconfirmed facts must remain visibly identifiable and machine-detectable until replaced.
9. **Multilingual-ready:** text must not be embedded in images; layouts must work right-to-left for a future Arabic version.

### 3.6 Content rules

- **Verified facts only.** Unconfirmed items stay marked `[TO CONFIRM]`. Do not add: expansion to other cities, Mauritania or the USA; "exclusive" franchise; "Director of Global Operations" – until confirmed.
- **Anglia wording:** "official partner in Morocco of Chichester College Group, UK"; Anglia Examinations is "a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding"; "the four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual". Do **not** state that Anglia depends on the UK Ministry of Education.
- **Placement promise (quote exactly):** "Grade placement is not lowered due to missing documents, language gaps, or academic gaps." – AGI Provisional Placement Policy.
- **No invented testimonials** on a live site; real ones need written consent. No financial claims on the investors page without documents.
- **Tone:** warm, direct, parent-first; US English (enrollment, behavior, center, program).
- **angliamorocco.org** is the official Anglia Morocco site: link to it (exam dates, books, practice, C.I.T.E. registration, network) rather than duplicating it.

### 3.7 Content status

The site is complete in structure and copy, but before launch it needs: ~38 photos (all `[PHOTO NEEDED]` slots), real testimonials, team names and portraits, Julie's approval of the founder's letter and story quotes, and confirmation of the `[TO CONFIRM]` facts. The full list with owners is in `v2/LAUNCH-CHECKLIST.md`; questions for Julie in `docs/email-julie-review.md`; for Anglia in `docs/email-anglia-approval.md`.

### 3.8 Appendix A – key facts reference

| Topic | Fact |
|---|---|
| Address | Number 20, Rue Baalabek, Hay Nahda, Agadir 80000, Morocco |
| Phone / WhatsApp / Email | +212 528 843 349 · Arabic +212 618 639 911 · WhatsApp +212 688 739 393 · americanecoleagadir@gmail.com |
| Anglia Morocco contacts | j.wilburn@angliamorocco.org · a.lam@angliamorocco.org · angliamorocco.org |
| Office | Monday–Friday 9:00–17:00 [TO CONFIRM], closed Sunday; tours Monday–Friday |
| Founded | 2013, five children, one room; now Hay Nahda, eight multi-grade classrooms; 46+ nationalities over eleven years |
| Tuition | 2,600 MAD a month over ten months; annual inscription 6,500 MAD (K–Grade 1) to 11,000 MAD (Grade 12), non-refundable; books, mathematics and Anglia exams included |
| 2026–27 calendar | Registration Aug 28 & 31 · first day Sept 7 · fall break Oct 12–18 · winter break Dec 18 – Jan 3 · second semester Jan 5 · Anglia exams April (date TBA) · last day & graduation June 17, 2027 |
| Eligibility | Aged 5 by September 1, under 21 on the first day |
| Policies | 90% attendance for promotion; late after 9:00, absent after 10:00; 5 unexcused tardies = 1 absence; pass mark 64% (D); 40 service hours (10 per year); 90-day adjustment period |
| Programs | K–12 school · Special education (SEN) · Adult high school diploma (16+, with American Worldwide Academy, 80% pass score, first graduate 2019) · English & Anglia exams · For teachers (C.I.T.E., 30-day internship, USA sponsorship US$60) · Professional & medical English (proctoring 200 MAD/15 EUR admin + 200 MAD/15 EUR per hour) · University pathways |
| Anglia classes | Saturday classes ages 5–18, Sat 14:00–16:00, Oct–June, 500 MAD/month incl. yearly exam · one-to-one 200 MAD/session · small group (2–3) 150 MAD per person · group course (4–10) 1,200 MAD for 12 weeks · level test free · groups max 10 · prices effective Nov 2024 |
| Recognition | Accredited by the American Council of Training and Development · recognized by the Departments of Education of Tennessee, Florida, Colorado and Alabama · in compliance with NCAA, NAIA (Eligibility Centers), College Board (AP & SAT), Meridian Learning · Cognia (American High School Online), QAHE, American Canadian Board · Global Schools Program member (2023) · American School Counselor Association member (2026) · official partner in Morocco of Chichester College Group, UK |
| Network & partners | American Group International School · AWA High School for Adults · Anglia Examinations England · AGI Learning Pods & Fast Track · American High School Online · I-Heart Women & Family Institute · Chichester College Group · Leverage Edu · Bridge Education Group (TEFL/TESOL) |
