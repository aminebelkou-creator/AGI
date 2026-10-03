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
| **Parents** (priority) | Trust, a fair price, support for their child, clear admissions | `parents.html` (single landing page); `our-story.html` for the longer story | Book a visit · WhatsApp · Apply |
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
│   ├── Our story (our-story.html)              ← long-form brand story; links to the parents page
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
├── For parents (parents.html)               ← THE parent landing page (target of the home popup)
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
- **Parents popup (home page only).** Invites parents to the parent landing page (`parents.html`); its headline matches that page's headline.
  - Content: kicker "For parents" · heading **"Your child, known by name."** · text *"Since 2013, AGI has grown from one small classroom into a school trusted by families from more than 46 nations. Discover why parents choose us."* · three labels: Affordable, Creative, Inclusive · [PHOTO NEEDED – AGI's early days, or Julie with students] · actions **See why parents choose AGI** (→ parents.html) and **Not now** (closes).
  - Behavior: never on the first screen. Opens once the visitor has scrolled past half of the page, or – on desktop – when the pointer leaves the window (exit intent). Then not again for 7 days (remembered in the browser).
  - **Phones:** a compact, non-blocking bar at the bottom of the screen (headline, one sentence, the two actions; no photo, no backdrop) – the page stays usable. **Desktop:** a modal dialog that traps focus and returns it afterwards.
  - Closes with the close button, "Not now", the Escape key, or (desktop) a click outside. Must not open if another dialog is open. [TO CONFIRM: behavior with Julie]
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

---

## 4. Pages – sections and content

Content is listed in reading order. Notation: **Section:** = a main section heading · **bold line** = a sub-heading · `→ Label (target)` = a button or link · `[PHOTO NEEDED – …]` = photo to supply · `[TO CONFIRM: …]` = fact awaiting confirmation · `[SAMPLE …]` = placeholder testimonial.

### 4.1 `index.html`

- **Browser title:** American Group International – American school in Agadir, Morocco
- **Meta description:** The first American school in Agadir: K–12, special education, adult diploma, English and Anglia exams. Established 2013. Now enrolling for 2026–27.

Affordable · Creative · Inclusive — since 2013
**Page title (H1):** An American education, close to home.
American Group International is the first American school in Agadir – a K–12 micro-school with programs for adults, English learners and educators, and the headquarters of Anglia Examinations in Morocco.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
→ **Our story** (`our-story.html`)
Now enrolling Academic year 2026–27, all programs. Registration days are August 28 and 31.
2013 Founded in Agadir, starting with five children
46+ Nationalities hosted over eleven years
4 U.S. state departments of education recognize AGI
12 Regions served by Anglia Morocco from Agadir

#### Section: Find your path
Information for each of the people AGI serves.
- Link card → `parents.html`: Parents · For your child · Admissions, support and what makes AGI different.
- Link card → `english-anglia.html`: Students · Learn & certify English · Anglia levels, classes and free level tests.
- Link card → `teachers.html`: Teachers · C.I.T.E. & training · A lifelong credential and a 30-day internship.
- Link card → `professional.html`: Professionals · Business & medical English · English for work, for you or your team.
- Link card → `investors.html`: Partners · Grow with AGI · Franchise, representation and partnership.

#### Section: One American standard, for every stage.
From a child's first day of kindergarten to an adult's diploma or teaching certificate.
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `special-education.html`: Inclusive · Special education (SEN) · Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care.
- Link card → `adult-diploma.html`: Age 16+ · Adult high school diploma · A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir.
- Link card → `english-anglia.html`: All ages · English & Anglia exams · AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults.
- Link card → `teachers.html`: Educators · For teachers (C.I.T.E.) · The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship.
- Link card → `professional.html`: Professionals · Professional & medical English · Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching.
- Link card → `pathways.html`: Next steps · University pathways · An authorized admissions agent for universities and colleges in the UK, the United States and beyond.

#### Section: Affordable, creative and inclusive.
Our promise to every family since 2013. School + Home + Community = Student Success.
[PHOTO NEEDED – A multi-grade classroom during a lesson]
[PHOTO NEEDED – A student reading or presenting]
_Affordable_
**Within reach**
An international standard for working families, with books, mathematics and Anglia exams included.
_Creative_
**Learning with imagination**
American pedagogy in small multi-grade classes, enriched by Montessori and Waldorf ideas.
_Inclusive_
**No one held back**
Grade placement is never lowered for missing documents, language gaps or academic gaps.
_English for life_
**Certified progress**
Every grade is benchmarked on the CEFR and assessed with Anglia Examinations of England.
[IMAGE: Julie A. Wilburn, CEO and Educational Director]
From the director
“AGI is a child-centered school where students take responsibility for their learning.”
We prepare children to be independent, critical thinkers and caring, contributing members of society. We hold high the value of respect – of oneself, of others and of the environment – and we believe the family is an integral part of the program.
Julie A. Wilburn CEO & Educational Director · Anglia Examinations Morocco, American Group International of Agadir
→ **About AGI** (`about.html`)

#### Section: What families say
Parents, students and graduates in their own words.
> “Our daughter arrived speaking almost no English. Two years later she reads chapter books and corrects my pronunciation.” — Parent of a grade 3 student [SAMPLE – replace with a real testimonial]
> “The teachers know every child. When our son needed extra support, the plan was in place within weeks, and we were part of it.” — Parent of a grade 7 student [SAMPLE – replace with a real testimonial]
> “AGI gave me an American diploma and the English to use it. I'm now studying at university abroad.” — AGI graduate [SAMPLE – replace with a real testimonial]

#### Section: Joining AGI
Students are welcome at any stage. Every new student sits a free placement test.
Step 01
**Enquire & visit**
Tours are arranged individually, so you can meet the team and see the classrooms.
Step 02
**Placement test**
A free assessment, including the Anglia level test for language learners.
Step 03
**Documents**
Previous school records, a behavior report, and proof of age, residency and immunization.
Step 04
**Enroll**
Pay the annual inscription and confirm the monthly plan on registration days.
Key dates 2026–27
- **Registration days** — August 28 & 31
- **First day of classes** — September 7
- **Winter break** — Dec 18 – Jan 3
- **Last day & graduation** — June 17, 2027
2,600 MAD
a month over ten months, plus an annual inscription. Books, exams and insurance included.
→ **Apply** (`forms.html#enrollment`)
→ **Admissions & fees** (`admissions.html`)

#### Section: Recognized in the United States
Accredited by the American Council of Training and Development, recognized by four state departments of education, and in compliance with NCAA, NAIA, College Board and Meridian Learning standards.
[IMAGE: seal-tennessee-clean.webp]
Tennessee Department of Education
[IMAGE: seal-florida-clean.webp]
Florida Department of Education
[IMAGE: seal-colorado-clean.webp]
Colorado Department of Education
[IMAGE: seal-alabama-clean.webp]
Alabama Department of Education
**Our programs are in compliance with**
[IMAGE: mark-ncaa-clean.webp]
NCAA Eligibility Center
[IMAGE: mark-naia-clean.webp]
NAIA Eligibility Center
[IMAGE: mark-collegeboard-clean.webp]
College Board AP & SAT programs
[IMAGE: mark-meridian-clean.webp]
Meridian Learning Curriculum standards
Official partner in Morocco of Chichester College Group, UK. AGI is the Anglia franchise holder for Morocco and home of Anglia Morocco. Anglia Examinations is a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding. English & Anglia exams [link: “English & Anglia exams” → `english-anglia.html`]
→ **All accreditation and memberships** (`about.html#accreditation`)

#### Section: From the journal
→ **All journal entries** (`journal.html`)
- Link card → `journal/4356-2.html`: Announcement · April 6, 2026 · Julie Wilburn officially accredited as a Holistic Therapeutic Coach
- Link card → `journal/american-school-counselor-association-member.html`: Membership · March 4, 2026 · AGI joins the American School Counselor Association
- Link card → `journal/leverage-edu-x-agi-join-forces-in-the-south-of-morocco.html`: Partnership · March 4, 2026 · Leverage Edu and AGI join forces in the south of Morocco

#### Section: Come and see the school.
Tours are arranged individually, Monday to Friday. Tell us when suits you and the office will confirm a time.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
Number 20, Rue Baalabek Hay Nahda, Agadir 80000, Morocco
+212 528 843 349 · WhatsApp · Email The office is closed on Sundays. [link: “WhatsApp” → `https://wa.me/212688739393`]
→ **Open in Google Maps** (`https://www.google.com/maps/search/?api=1&query=20+Rue+Baalabek+Hay+Nahda+Agadir`)

---

### 4.2 `our-story.html`

- **Browser title:** Our story – American Group International, Agadir
- **Meta description:** A school built for families like yours: why parents in Agadir trust AGI – affordable, creative and inclusive, accredited, and focused on every child since 2013.

[PHOTO NEEDED – Hero photo: children arriving at school in the morning, or Julie with students]
Home / About / Our story [link: “Home” → `index.html`] [link: “About” → `about.html`]
**Page title (H1):** A school built for families like yours.
Julie Wilburn started AGI in 2013 with five children in one room, because she believed every child deserves an American education – not only the children of the wealthy. Today, parents from more than 46 nations trust us with what matters most to them.
→ **Book a visit** (`forms.html#visit`)
→ **Read the story** (`#journey`)

#### Section: How a small classroom became your child's school
Eleven years, one promise to parents.
[PHOTO NEEDED – The first classroom, or a photo from AGI's early years]
2013
**One room, five children**
AGI's first classes began in a single room in Agadir with five children. The idea was simple: an American education that working families could afford.
[PHOTO NEEDED – The school building in Hay Nahda]
Hay Nahda
**A school of its own**
The school soon outgrew its first room and moved to Hay Nahda, where kindergarten to grade 12 is now taught in eight multi-grade classrooms.
[PHOTO NEEDED – Students of different backgrounds working together]
46+
**A world in one school**
Over eleven years, children of more than 46 nationalities have learned side by side – Moroccan families and families from across the world.
[PHOTO NEEDED – An Anglia exam day or certificate ceremony]
2021
**Home of Anglia in Morocco**
AGI became the Anglia Examinations franchise holder for Morocco and the official partner in Morocco of Chichester College Group, UK – bringing certified English to the Kingdom's twelve regions.
[PHOTO NEEDED – Julie with students or teachers today]
Today
**The same promise**
A K–12 school, programs for adults, teachers and professionals, and the same founding promise: affordable, creative and inclusive.
[IMAGE: Julie A. Wilburn, founder of AGI]
In her words
[TO CONFIRM: “Children only thrive when they feel safe, valued – and known.”]
[TO CONFIRM: “I kept meeting wonderful families who were shut out – by fees they couldn't pay, or by schools that held a child back because they were still learning a language. So we built something different.”]
Julie A. Wilburn Founder · CEO & Educational Director
→ **Read Julie's letter to parents** (`founder-letter.html`)

#### Section: Affordable. Creative. Inclusive.
The three words Julie chose for AGI – and what they mean for your child.
[PHOTO NEEDED – A family at the school gate]
_Affordable_
**Within reach**
2,600 MAD a month over ten months, with books, mathematics and Anglia exams included. An international standard for working families.
[PHOTO NEEDED – A hands-on project in class]
_Creative_
**Learning with imagination**
Small multi-grade classes, American pedagogy enriched by Montessori and Waldorf ideas, critical thinking and independent research.
[PHOTO NEEDED – Students of different backgrounds together]
_Inclusive_
**No one held back**
Grade placement is never lowered for missing documents, language gaps or academic gaps. Every child gets the support they need.

#### Section: Why parents trust AGI
Six commitments families can check for themselves.
Step 01
**Your child is known by name**
Small multi-grade classes where teachers know every child and every family.
Step 02
**Never held back for a language gap**
“Grade placement is not lowered due to missing documents, language gaps, or academic gaps.” – AGI placement policy.
Step 03
**The whole child**
Individual plans, a founder who is an accredited Holistic Therapeutic Coach, and membership of the American School Counselor Association.
Step 04
**Clear, fair fees**
One monthly fee, an annual inscription, and the essentials included.
→ **See tuition** (`admissions.html#fees`)
Step 05
**Recognized standards**
Accredited by the American Council of Training and Development and recognized by four U.S. state departments of education.
Step 06
**A partnership with you**
School + Home + Community = Student Success. You're part of your child's plan from the first day.

#### Section: What your child gains
[PHOTO NEEDED – A student presenting in English]
[PHOTO NEEDED – Friends from different countries]
- **English for life** — Certified progress with Anglia Examinations of England, from First Step to Masters (C2), benchmarked on the CEFR every year.
- **An American education** — An American curriculum from kindergarten to grade 12, with two routes to a U.S. high school diploma.
- **Friends from 46+ nations** — Confidence and openness that come from learning alongside the world.
- **Doors to university** — Guidance and partners in the UK and beyond, including Chichester College Group. University pathways [link: “University pathways” → `pathways.html`]
- **Character and service** — Respect, responsibility and 40 hours of community service before graduation.
- **Support when it's needed** — Individualized Education Plans and small-group support. Special education [link: “Special education” → `special-education.html`]

#### Section: Recognized and accredited
→ **All accreditation** (`about.html#accreditation`)
[IMAGE: seal-tennessee-clean.webp]
Tennessee Department of Education
[IMAGE: seal-florida-clean.webp]
Florida Department of Education
[IMAGE: seal-colorado-clean.webp]
Colorado Department of Education
[IMAGE: seal-alabama-clean.webp]
Alabama Department of Education
[IMAGE: mark-ncaa-clean.webp]
NCAA Eligibility Center
[IMAGE: mark-naia-clean.webp]
NAIA Eligibility Center
[IMAGE: mark-collegeboard-clean.webp]
College Board AP & SAT programs
[IMAGE: mark-meridian-clean.webp]
Meridian Learning Curriculum standards
Official partner in Morocco of Chichester College Group, UK. Accredited by the American Council of Training and Development. Anglia Examinations franchise holder for Morocco.

#### Section: Success, one student at a time
→ **The journal** (`journal.html`)
Hundreds of students placed into the American educational system with low-cost programs.
2019 AGI's first adult high school graduate. Read the story [link: “Read the story” → `journal/first-adult-high-school-graduate.html`]
Tangier AGI students in the American National Spelling Bee of Morocco. Read the story [link: “Read the story” → `journal/american-national-spelling-bee-in-morocco.html`]
> “Our daughter arrived speaking almost no English. Two years later she reads chapter books and corrects my pronunciation.” — Parent of a grade 3 student [SAMPLE – replace with a real testimonial]
> “The teachers know every child. When our son needed extra support, the plan was in place within weeks, and we were part of it.” — Parent of a grade 7 student [SAMPLE – replace with a real testimonial]
> “AGI gave me an American diploma and the English to use it. I'm now studying at university abroad.” — AGI graduate [SAMPLE – replace with a real testimonial]

#### Section: Come and see the school.
Meet the team, see the classrooms, and ask every question you have. Tours are arranged individually, Monday to Friday.
→ **Book a visit** (`forms.html#visit`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
→ **For parents: how to join** (`parents.html`)

---

### 4.3 `parents.html`

- **Browser title:** For parents – American Group International, Agadir
- **Meta description:** Your child, known by name: an affordable, creative and inclusive American school in Agadir since 2013. Small classes, no child held back, accredited in the USA.

Home / For parents [link: “Home” → `index.html`]
**Page title (H1):** Your child, known by name.
An affordable, creative and inclusive American school in Agadir – where your child is known by every teacher, supported where they need it, and never held back for a language gap.
→ **Book a visit** (`forms.html#visit`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
- Since 2013
- Students of 46+ nationalities
- Accredited by the American Council of Training and Development
- Recognized by 4 U.S. state departments of education
[PHOTO NEEDED – Parents and children arriving at school in the morning]

#### Section: Is your child thriving – or just fitting in?
Many families know the feeling: classrooms too crowded for a teacher to notice your child, grades that punish a child for still learning a language, and international schools with fees that are simply out of reach.
AGI was created for these families – and for children who deserve to be known, not just counted.

#### Section: A school that began with five children
→ **The full story** (`our-story.html`)
[PHOTO NEEDED – AGI's early years]
2013
**One room, five children**
Julie Wilburn opened AGI's first classroom in Agadir with a conviction: an American education shouldn't be only for the wealthy.
[PHOTO NEEDED – Students of different backgrounds together]
46+
**A world in one school**
Since then, children of more than 46 nationalities have learned side by side in Hay Nahda.
[PHOTO NEEDED – Julie with students or teachers today]
Today
**The same promise**
A K–12 school and the home of Anglia Examinations in Morocco – still small enough to know every child by name.
[IMAGE: Julie A. Wilburn, founder of AGI]
From our founder
[TO CONFIRM: “Children only thrive when they feel safe, valued – and known.”]
Julie A. Wilburn Founder · CEO & Educational Director
→ **Read Julie's letter to parents** (`founder-letter.html`)

#### Section: Affordable. Creative. Inclusive.
Three words Julie chose for AGI – and what they mean for your child.
_Affordable_
**Within reach**
2,600 MAD a month over ten months, with books, mathematics and Anglia exams included. No hidden extras for the essentials.
_Creative_
**Learning with imagination**
Small multi-grade classes, American pedagogy enriched by Montessori and Waldorf ideas, room for critical thinking and independent research.
_Inclusive_
**Every learner belongs**
Students of more than 46 nationalities, mainstream and special-needs learners side by side, with individual plans where they need them.
Our placement promise

#### Section: No child is held back for a language gap.
“Grade placement is not lowered due to missing documents, language gaps, or academic gaps.”
AGI Provisional Placement Policy Every new student sits a free placement assessment
Instead of moving your child down a year, we keep them with their age group and give targeted support: English as a second language, extra help where they are behind, and regular reviews with you.

#### Section: Why parents trust AGI
Six commitments you can check for yourself.
Step 01
**Known by name**
Small multi-grade classes where teachers know every child and every family.
Step 02
**Never held back**
No child moves down a grade for a language gap or a missing document.
Step 03
**The whole child**
Individual plans, a founder who is an accredited Holistic Therapeutic Coach, and membership of the American School Counselor Association.
Step 04
**Clear, fair fees**
One monthly fee, an annual inscription, and the essentials included.
Step 05
**Recognized standards**
Accredited by the American Council of Training and Development; official partner in Morocco of Chichester College Group, UK.
Step 06
**A partnership with you**
School + Home + Community = Student Success. You are part of your child's plan from day one, starting with a 90-day adjustment period.
[IMAGE: seal-tennessee-clean.webp]
Tennessee Department of Education
[IMAGE: seal-florida-clean.webp]
Florida Department of Education
[IMAGE: seal-colorado-clean.webp]
Colorado Department of Education
[IMAGE: seal-alabama-clean.webp]
Alabama Department of Education
[IMAGE: mark-ncaa-clean.webp]
NCAA Eligibility Center
[IMAGE: mark-naia-clean.webp]
NAIA Eligibility Center
[IMAGE: mark-collegeboard-clean.webp]
College Board AP & SAT programs
[IMAGE: mark-meridian-clean.webp]
Meridian Learning Curriculum standards

#### Section: What your child gains
- **English for life** — Certified progress with Anglia Examinations of England, benchmarked on the CEFR every year. English & Anglia [link: “English & Anglia” → `english-anglia.html`]
- **An American education** — An American curriculum from kindergarten to grade 12, with routes to a U.S. high school diploma. K–12 school [link: “K–12 school” → `k12.html`]
- **Care for the whole child** — Individualized Education Plans and small-group support when needed. Special education [link: “Special education” → `special-education.html`]
- **Friends from 46+ nations** — Confidence and openness that come from learning alongside the world.
- **Doors to university** — Guidance and partners in the UK and beyond. University pathways [link: “University pathways” → `pathways.html`]

#### Section: What parents say
> “Our daughter arrived speaking almost no English. Two years later she reads chapter books and corrects my pronunciation.” — Parent of a grade 3 student [SAMPLE – replace with a real testimonial]
> “The teachers know every child. When our son needed extra support, the plan was in place within weeks, and we were part of it.” — Parent of a grade 7 student [SAMPLE – replace with a real testimonial]
> “AGI gave me an American diploma and the English to use it. I'm now studying at university abroad.” — AGI graduate [SAMPLE – replace with a real testimonial]

#### Section: Three steps to joining AGI
Students are welcome at any stage of the year.
Step 01
**Reach out**
Send a message, call or WhatsApp us. We'll answer your questions and arrange a visit.
Step 02
**Visit & placement test**
Meet the team, see the classrooms, and let your child sit a free, friendly placement assessment.
Step 03
**Enroll**
Pay the annual inscription and confirm the monthly plan. Registration days for 2026–27 are August 28 and 31.
Tuition is 2,600 MAD a month over ten months, plus an annual inscription (6,500 MAD for kindergarten–grade 1, rising to 11,000 MAD for grade 12). Books, mathematics and Anglia exams are included. Tuition & fees [link: “Tuition & fees” → `admissions.html#fees`]

#### Section: Questions parents ask
- **Q: My child doesn't speak English yet. Can they join?** — A: Yes. Many of our students start with little English. They join their age group, receive ESL support, and are benchmarked with the Anglia levels as they progress.
- **Q: Can my child join in the middle of the year?** — A: Yes. We welcome students at any stage. Your child sits the placement assessment and starts with the right support.
- **Q: My child has special needs. How do you support them?** — A: We build an Individualized Education Plan with you. To put the right support in place we need documentation from a licensed practitioner, along with previous school records.
- **Q: What does it cost?** — A: Tuition is 2,600 MAD a month over ten months, plus an annual inscription paid at enrollment. Books, mathematics and Anglia exams are included. See tuition & fees.
- **Q: Is there a discount for brothers and sisters?** — A: [TO CONFIRM: Answer to confirm with the office.]
- **Q: What are the school hours?** — A: [TO CONFIRM: School day start and end times to confirm.] Arrival after 9:00 counts as late, and after 10:00 as a full-day absence.
- **Q: Do you offer transport or lunch?** — A: [TO CONFIRM: Answer to confirm with the office.]
- **Q: Is there a uniform?** — A: [TO CONFIRM: Answer to confirm with the office.]
- **Q: What do we need to bring?** — A: Previous school records and a behavior report, proof of age and residency, and immunization and physical examination records.

#### Section: Come and see the school.
The best way to know AGI is to visit during the school day. Tours are arranged individually, Monday to Friday.
→ **Book a visit** (`forms.html#visit`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

---

### 4.4 `founder-letter.html`

- **Browser title:** A letter from our founder – American Group International, Agadir
- **Meta description:** Julie A. Wilburn, founder of American Group International, on why AGI started with five children in one room in Agadir, and what it promises families today.

Home / About / A letter from our founder [link: “Home” → `index.html`] [link: “About” → `about.html`]
**Page title (H1):** A letter from our founder.
Julie A. Wilburn, on how AGI began and what it promises every family.
Dear parents,
When American Group International opened its doors in 2013, it was one room in Agadir and five children. We had a conviction more than a plan: that every child deserves an excellent education, and that an American education should not be reserved for the few families who can afford an international school.
Having lived in Morocco for many years, I saw how often good families were shut out – by fees that were out of reach, or by systems that held children back because they learned differently or were still learning a language. So we built something else: a school that is affordable, creative and inclusive.
At AGI, a child is never moved down a grade because of a language gap or a missing document. We welcome them, assess what they can do, and give them the support they need. As a Holistic Therapeutic Coach, I care as much about how our students feel as about what they learn, because children only thrive when they feel safe and valued.
Since that first room, students of more than 46 nationalities have learned together with us. We outgrew our beginnings, moved to Hay Nahda, and in 2021 AGI became the Anglia Examinations franchise holder for Morocco, bringing internationally recognized English certification to students across the Kingdom.
[TO CONFIRM: Today we also serve families beyond Agadir – in other Moroccan cities, in Mauritania and in the United States.]
Our motto says what we believe: School + Home + Community = Student Success. Trusting a school with your child is trusting it with what matters most to you. We take that trust seriously, every day.
I would be delighted to welcome you, show you our classrooms and introduce you to our team.
Julie A. Wilburn Founder · CEO & Educational Director, American Group International of Agadir · Anglia Examinations Morocco [TO CONFIRM: · Director of Global Operations]

#### Section: Visit AGI.
Meet Julie and the team, and see the school for yourself.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)

---

### 4.5 `about.html`

- **Browser title:** About AGI – American Group International, Agadir
- **Meta description:** The story, mission and people of American Group International, the first American school in Agadir, and its accreditation.

Home / About [link: “Home” → `index.html`]
**Page title (H1):** The first American school in Agadir.
AGI began in 2013 with five children in one room. Today it is a K–12 micro-school, a center for adult and English education, and the home of Anglia Examinations in Morocco.

#### Section: Our story
[PHOTO NEEDED – The school building in Hay Nahda]
→ **The full story, in pictures** (`our-story.html`)
American Group International School is a small private school in the Berber community of the Souss, in Agadir. The first classes started in 2013 with five children. The school soon outgrew its one-room beginnings and moved to Hay Nahda, where kindergarten to grade 12 is now taught in eight multi-grade classrooms.
Over eleven years, AGI has welcomed students of more than 46 nationalities. Its enrollment is open: the school was created for students who need a program the Moroccan system may not offer – an American curriculum, English immersion, or support for learning differences.
In 2021 AGI became the Anglia Examinations franchise holder for Morocco, and it now runs the Anglia network across the Kingdom's twelve regions from its Agadir headquarters. Its mission remains the same: an international education that working families in Morocco can afford.
[TO CONFIRM: Today AGI also works beyond Agadir [to confirm with AGI: other Moroccan cities, Mauritania, and the United States through American Group USA LLC].]

#### Section: Mission, philosophy and vision
Affordable, creative and inclusive. “Global Minds with a Global Perspective.” School + Home + Community = Student Success.
_Mission_
To serve the Agadir region by giving children a strong educational foundation following American philosophy and practice, so that they become independent, critical thinkers and caring, contributing members of society.
_Philosophy_
Academic excellence, discipline, ethical standards and respect for others. We develop the whole child – intellectual, social, emotional, character and physical – and foster a general respect for all humanity.
_Vision_
Lifelong learners who pursue excellence, model integrity and honor cultural diversity, equipped to serve their community in Morocco and the wider world with wisdom and compassion.
[IMAGE: Julie A. Wilburn]
Founder & leadership

#### Section: Julie A. Wilburn
CEO & Educational Director · Anglia Examinations Morocco, American Group International of Agadir [TO CONFIRM: · Director of Global Operations]
Julie Wilburn founded AGI and leads all of its educational programs: the primary and high school, curriculum, testing and assessment, staff training and the social-skills program. She also teaches in the classroom.
She has lived in Morocco for many years and holds dual [TO CONFIRM: American-Moroccan] citizenship. In 2026 she was accredited as a Holistic Therapeutic Coach by IPHM and ICAHP, and she offers ADHD holistic coaching for children and adults.
“We believe in equality, and that an international education empowers students to open global opportunities for their personal growth and success.”
→ **Read Julie's letter to parents** (`founder-letter.html`)

#### Section: The team
A small team, so families always know who to call.
**Julie A. Wilburn**
CEO & Educational Director
[PHOTO NEEDED – Portrait]
**Abdelhak Lam**
Sales Coordinator, main headquarters
[PHOTO NEEDED – Portrait]
**[TO CONFIRM: Teacher name]**
Lower school · grades K–5
[PHOTO NEEDED – Portrait]
**[TO CONFIRM: Teacher name]**
Middle & upper school · English
[PHOTO NEEDED – Portrait]
**[TO CONFIRM: Teacher name]**
Mathematics & science
[PHOTO NEEDED – Portrait]
**[TO CONFIRM: Teacher name]**
Special education support
[PHOTO NEEDED – Portrait]
**[TO CONFIRM: Name]**
Anglia Morocco coordinator
[PHOTO NEEDED – Portrait]
**[TO CONFIRM: Name]**
Admissions office ·
→ **Forms & requests** (`forms.html`)

#### Section: Accreditation & memberships
Where AGI's standards come from, and who holds us to them.
[IMAGE: seal-tennessee-clean.webp]
Tennessee Department of Education
[IMAGE: seal-florida-clean.webp]
Florida Department of Education
[IMAGE: seal-colorado-clean.webp]
Colorado Department of Education
[IMAGE: seal-alabama-clean.webp]
Alabama Department of Education
- **American Council of Training and Development Accreditation** — AGI's institutional accreditor for the American-curriculum school and its programs.
- **U.S. state departments of education Recognition** — Recognized by the departments of education of Tennessee, Florida, Colorado and Alabama.
- **Cognia Accreditation** — The American High School Online program for grades 9–12 is Cognia accredited; the high school books program is Florida accredited.
- **QAHE Accreditation** — Quality Assurance in Higher Education covers AGI's independent course studies and professional programs.
- **American Canadian Board Certification** — Professional training certificates, including the Early Childhood Education and Care diploma, are approved by the American Canadian Board.
- **Chichester College Group, UK Official partner** — AGI is proud to be the official partner in Morocco of Chichester College Group, UK – award winning and Ofsted Outstanding – which owns Anglia Examinations. AGI became the Anglia franchise holder for Morocco in 2021.
- **AIM Qualifications · Ofqual Regulation** — Anglia's four highest levels of exam are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual in England.
- **UCAS Recognition** — The Anglia Proficiency examination is listed by UCAS as evidence of English competence for British universities.
- **Global Schools Program Membership** — An initiative of the UN Sustainable Development Solutions Network, supporting education for sustainable development. Member since 2023.
- **American School Counselor Association Membership** — AGI joined ASCA in 2026, bringing U.S. school-counseling standards to student guidance.
**Our programs are in compliance with**
[IMAGE: mark-ncaa-clean.webp]
NCAA Eligibility Center
[IMAGE: mark-naia-clean.webp]
NAIA Eligibility Center
[IMAGE: mark-meridian-clean.webp]
Meridian Learning Curriculum standards
[IMAGE: mark-collegeboard-clean.webp]
College Board AP & SAT programs

#### Section: The AGI network
Divisions, partners and the institutions we work with.
[IMAGE: net-agi-seal.png]
American Group International School The American school of Agadir: a micro-school and K–12 campus, established 2013.
[IMAGE: net-awa.png]
AWA High School for Adults Our U.S.-registered company, offering support programs to clients worldwide.
[IMAGE: net-anglia.png]
Anglia Examinations England AGI is the Anglia franchise holder and headquarters for Morocco.
[IMAGE: net-pods.png]
AGI Learning Pods & Fast Track Small-group programs led by teacherpreneurs.
[IMAGE: net-ahs.png]
American High School Online A Cognia-accredited online high school for grades 9–12.
[IMAGE: net-iheart.png]
I-Heart Women & Family Institute Emotional and behavioral support, accredited by IPHM and ICAHP.
[IMAGE: net-ccg.png]
Chichester College Group Seven colleges in the south of England, with UK progression routes.
[IMAGE: net-leverage.png]
Leverage Edu University placement with housing assistance.

#### Section: Meet us in Agadir.
Visits are arranged individually, Monday to Friday.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)

---

### 4.6 `programs.html`

- **Browser title:** Programs – American Group International, Agadir
- **Meta description:** AGI programs: K–12 school, special education, adult high school diploma, English and Anglia exams, teacher training and university pathways.

Home / Programs [link: “Home” → `index.html`]
**Page title (H1):** Programs for every stage.
Every AGI program shares one American academic standard. Each has its own curriculum, calendar and admission requirements – and every learner starts with a free placement test.

#### Section: Choose a program
Each program page explains who it is for, how it works and how to apply.
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `special-education.html`: Inclusive · Special education (SEN) · Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care.
- Link card → `adult-diploma.html`: Age 16+ · Adult high school diploma · A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir.
- Link card → `english-anglia.html`: All ages · English & Anglia exams · AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults.
- Link card → `teachers.html`: Educators · For teachers (C.I.T.E.) · The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship.
- Link card → `professional.html`: Professionals · Professional & medical English · Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching.
- Link card → `pathways.html`: Next steps · University pathways · An authorized admissions agent for universities and colleges in the UK, the United States and beyond.

#### Section: Not sure which program fits?
Book a visit or send a question – the office will help you choose and arrange a free placement test.
→ **Apply** (`forms.html#enrollment`)
→ **Ask a question** (`forms.html#enquiry/programs`)

---

### 4.7 `k12.html`

- **Browser title:** K–12 school – American Group International, Agadir
- **Meta description:** An American-curriculum micro-school in Agadir, from kindergarten to grade 12, with English support through Anglia.

Home / Programs / K–12 Education [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** K–12 Education
An American-curriculum school, from the first day of kindergarten to the last day of grade twelve.
AGI is a child-centered micro-school in Agadir, established in 2013. Small classes, American curriculum standards, and ESL through the Anglia Examinations system of England for children who do not speak English at home. Students are welcomed at any stage and supported to adapt to the curriculum and the language immersion.
At a Glance
Ages 5 – 18
Curriculum AGI · American
Languages EN · FR · AR
Campus Agadir · Hay Nahda

#### Section: Three schools, one journey
[PHOTO NEEDED – Lower school classroom]
K – Grade 5
**Lower School**
English and spelling, literature, mathematics, natural science and foreign language — with penmanship in Grades 2 to 4 and ESL alongside. The elementary benchmark is CEFR B1 by the end of Grade 5.
[PHOTO NEEDED – Middle school class]
Grades 6 – 8
**Middle School**
American, world and Islamic history, earth and biological science, and mathematics through Foundations and Pre-Algebra. Middle school graduates at Grade 8 target CEFR B2.
[PHOTO NEEDED – Upper school students]
Grades 9 – 12
**Upper School**
English I–IV, U.S. History, Algebra I and II, Geometry, Biology, Government and Economics. Two routes: the Florida-accredited books program or the Cognia-accredited American High School Online. Forty service hours are required to graduate.

#### Section: Inclusive by design
AGI welcomes students with a range of special needs, learning differences and mental-health challenges, physical and developmental alike. Documentation from a licensed practitioner is required so provision can be planned properly.
Individualised plans
Individualized Education Plans written to each student's needs and abilities.
Small groups
Class sizes that allow personalised attention within mainstream school life.
Therapeutic support
Occupational therapy, speech-language pathology and behavioral support.
Cognitive programs
Energia SOI, customised for students with reading and mathematics difficulties.
How the year is measured
90%
Minimum attendance to qualify for promotion, K–12.
64%
Pass mark in each core subject — math, science, language arts, social studies.
April
Anglia English assessment, required of every enrolled student.
40
Service hours across four years of high school — ten per year.
Every new student sits English/ESL and academic placement assessments before admission, whatever system they arrive from. Grades 9 to 11 also take the CAT assessment.

#### Section: The course of study, grade by grade
A fixed set of subjects each year, with ESL alongside for language learners. Electives and AP courses are planned from grade 9.
| Grades | Subjects |
|---|---|
| Kindergarten | Foreign language, English, reading & phonics, math, science, penmanship, ESL |
| Grades 1–4 | Foreign language, English & spelling, literature, mathematics, natural science, U.S. history strands, penmanship (grades 2–4), ESL |
| Grades 5–8 | Foreign language, English & spelling, American, world and Islamic history, literature, mathematics through pre-algebra, earth & biological science, ESL |
| Grade 9 | English I, U.S. history, algebra I, physical science, principles of music, physical education, ESL |
| Grade 10 | English II, world history, geometry, biology, one elective, ESL |
| Grade 11 | English III, algebra II, health, two electives, ESL |
| Grade 12 | English IV, U.S. government & economics, business math, science, ESL |
High school students complete 40 service hours (ten a year). For grades 9–12 there are two routes: the Florida-accredited books program, or American High School Online (Cognia accredited). See
→ **tuition & fees** (`admissions.html#fees`)
and
→ **English benchmarks** (`english-anglia.html#cefr`)
.

#### Section: Ready to meet the school?
Start Admissions Ask AGI Connect Book a Visit [link: “Start Admissions” → `admissions.html`] [link: “Ask AGI Connect” → `connect.html`] [link: “Book a Visit” → `forms.html#visit`]

---

### 4.8 `special-education.html`

- **Browser title:** Special education (SEN) – American Group International, Agadir
- **Meta description:** Special education at AGI Agadir: Individualized Education Plans, small groups, therapy support and a special-needs high school program.

Home / Programs / Special education [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Every child, supported.
AGI welcomes students with learning differences, mental health challenges, physical or developmental disabilities, and gifted learners – in small classes, with a plan built for each child.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
[PHOTO NEEDED – Special education – students in class or activity]

#### Section: Our approach
Mainstream and special-needs students learn in the same community. Support is planned with parents and, where needed, with the child's doctors and therapists.
- **Individualized Education Plans** — Each student's plan sets goals and accommodations for their needs and abilities, and is reviewed with parents through the year.
- **Small-group classrooms** — Small classes mean personal attention and a calm, supportive place to learn.
- **Therapy and behavioral support** — From occupational therapy to speech-language pathology and behavioral care, working with professional caregivers.
- **An inclusive community** — Every student is valued, respected and given the chance to thrive alongside their classmates.

#### Section: Special-needs high school
A program designed around the academic, social and emotional needs of teenagers with special needs.
The high school program focuses on life skills, vocational training and preparing for independence, so students leave with the tools to succeed after graduation.
Subjects follow the AGI spine with individual accommodations: English, mathematics, science, history, reading, spelling, Arabic, physical education, fine arts and ESL.
**Before you apply**
To provide an IEP or special-needs support, AGI needs documentation from a licensed practitioner, together with the student's previous school records and a behavior report. A parent's description alone isn't enough to put the right support in place.
Related services: ADHD holistic coaching for children and adults, and emotional and behavioral support through our partner, the I-Heart Women & Family Institute. [link: “ADHD holistic coaching” → `professional.html#adhd`]

#### Section: Talk to us about your child.
Book a visit to meet the team, or send a question first – everything you share is handled in confidence.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)

#### Section: Other programs
→ **All programs** (`programs.html`)
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `adult-diploma.html`: Age 16+ · Adult high school diploma · A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir.
- Link card → `english-anglia.html`: All ages · English & Anglia exams · AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults.
- Link card → `teachers.html`: Educators · For teachers (C.I.T.E.) · The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship.
- Link card → `professional.html`: Professionals · Professional & medical English · Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching.
- Link card → `pathways.html`: Next steps · University pathways · An authorized admissions agent for universities and colleges in the UK, the United States and beyond.

---

### 4.9 `adult-diploma.html`

- **Browser title:** Adult high school diploma – American Group International, Agadir
- **Meta description:** Earn an American high school diploma in Agadir: a self-paced program for learners aged 16 and over, with American Worldwide Academy and tests proctored on site.

Home / Programs / Adult high school diploma [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Finish high school, on your schedule.
For learners aged 16 and over who left school before graduating: a low-cost, self-directed American high school completion program, studied by correspondence or online.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
[PHOTO NEEDED – Adult high school diploma – students in class or activity]

#### Section: How it works
Offered in partnership with American Worldwide Academy. AGI's first adult graduate received their diploma in 2019.
- **Study at your own pace** — Work through each course independently, online or by correspondence, with tutorial help when you need it.
- **Tests in Agadir** — Every test is proctored on site at the AGI center. Graduation requires a passing score of 80 percent.
- **English included** — All students learn English and sit an English exam as part of the program.
- **Support after graduation** — Enrollment and graduation verification, letters of recommendation and official transcripts for further study.

#### Section: Courses
A nationally accredited program. Course examples:
| Course | Credits | Covers |
|---|---|---|
| English language writing skills | 2 | Usage, grammar, sentence structure, mechanics, punctuation and spelling |
| English literature | 2 | Classical and contemporary fiction, poetry, prose and non-fiction |
| General mathematics | 3 | Arithmetic, consumer mathematics, data analysis, algebra and geometry |
| Social science I – American history | 2 | From the colonial period to the Second World War |

#### Section: Ready to finish your diploma?
Apply online and the office will explain the next steps, fees and test dates.
→ **Apply** (`forms.html#enrollment`)
→ **Ask a question** (`forms.html#enquiry/programs`)

#### Section: Other programs
→ **All programs** (`programs.html`)
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `special-education.html`: Inclusive · Special education (SEN) · Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care.
- Link card → `english-anglia.html`: All ages · English & Anglia exams · AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults.
- Link card → `teachers.html`: Educators · For teachers (C.I.T.E.) · The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship.
- Link card → `professional.html`: Professionals · Professional & medical English · Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching.
- Link card → `pathways.html`: Next steps · University pathways · An authorized admissions agent for universities and colleges in the UK, the United States and beyond.

---

### 4.10 `english-anglia.html`

- **Browser title:** English & Anglia exams – American Group International, Agadir
- **Meta description:** Anglia Examinations Morocco headquarters in Agadir: ten CEFR levels, Saturday English classes for children, adult courses and free level testing.

Home / Programs / English & Anglia exams [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** English, measured step by step.
AGI is the headquarters of Anglia Examinations in Morocco. Children and adults learn English in small groups and certify their level with exams from England – starting with a free level test.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
[PHOTO NEEDED – English & Anglia exams – students in class or activity]

#### Section: Anglia Examinations
Based in Chichester, England, since 1993. AGI has used the Anglia system in its language programs since 2013, and in 2021 became the [TO CONFIRM: exclusive] Anglia franchise holder for Morocco. AGI is proud to be the official partner in Morocco of Chichester College Group, UK. [TO CONFIRM: Anglia was first introduced in Morocco in 2010 by Suzanne Linsen.]
- **Ten levels** — From young learner to expert user, mapped to the Common European Framework (CEFR). There is no minimum age; young learners start at about four.
- **All four skills** — Every level tests listening, reading, writing and speaking.
- **Business English** — Anglia International Business English, at four levels from A2+ to C1.
- **Recognized in the UK** — Anglia Examinations is a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding. The four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual. The Proficiency level is listed by UCAS as evidence of English for British universities.

#### Section: Classes & prices
Groups never exceed ten students. Level testing is free; class times are agreed after the test.
| Option | Who | Price |
|---|---|---|
| Saturday classes for children and teens | Ages 5–18, Saturdays 2:00–4:00 p.m., October to June. Interactive Anglia classes with preparation for the BAC, TOEFL, IELTS, SAT and Mathematics in English | 500 MAD a month, yearly Anglia exam included |
| One-to-one | English or mathematics, with full access to the teacher – ideal for professionals who want English for their job | 200 MAD per session |
| Small group | 2–3 students | 150 MAD per person, per session |
| Group course | 4–10 students, 12 weeks | 100 MAD a week per student (1,200 MAD) |
Prices effective November 2024. Books and insurance are not included.

#### Section: Free to start
Find your level before you choose a class.
- Link card → `forms.html#enquiry/anglia`: Free · English placement assessment on the CEFR · A free assessment of your English level, from beginner to expert, so we can recommend the right class or Anglia level.
- Link card → `https://angliamorocco.org/practice-resources/`: Free · Practice Anglia examinations · Sample papers and practice material for every Anglia level, on angliamorocco.org.
- Link card → `#math-english`: Exam preparation · Mathematics in English · Mathematics taught in English for SAT and IELTS candidates, plus certification workshops.

#### Section: Mathematics in English
Courses and tutors for students and teachers.
- **For students** — Mathematics taught in English to prepare for the SAT and IELTS, with one-to-one tutoring or small groups.
- **For teachers** — For classroom teachers who want to add mathematics to their skills, and new teacher candidates who are not math majors: teach mathematics in English and qualify as a mathematics specialist or coach. For teachers [link: “For teachers” → `teachers.html#math`]
- **Certification** — Mathematics certification in English is available through specialized workshops.

#### Section: Courses for teenagers and adults
- **Exam preparation** — Practice for the BAC, TOEFL, IELTS, SAT and British exams.
- **Conversation** — Speaking practice and new vocabulary.
- **ESL 100 – 300** — From beginner to advanced (B2): academic reading, essays and research writing.
- **English writing** — Narrative and descriptive writing, job applications and CVs.
- **Business & medical English** — For organizations and clinicians – see professional programs. [link: “professional programs” → `professional.html`]

#### Section: Anglia Morocco online
Exam dates, books and practice material are published on the official Anglia Morocco website.
- Link card → `https://angliamorocco.org/anglia-exam-dates-2/`: angliamorocco.org · Exam dates · The year's exam sessions for every level, from First Step to Masters.
- Link card → `https://angliamorocco.org/step-to-books-2/`: angliamorocco.org · Step To books & audio · Preparation books for each level, the book order form and the audio files.
- Link card → `https://angliamorocco.org/practice-resources/`: angliamorocco.org · Practice resources · Sample papers and practice material to prepare for the exams.
- Link card → `https://angliamorocco.org/citem/`: angliamorocco.org · C.I.T.E. for teachers · Register for the Certificate for International Teachers of English.
- Link card → `https://angliamorocco.org/angliamorocco-networks-and-centers-12-regions/`: angliamorocco.org · Network & centers · The Anglia Morocco network across the twelve regions, and open representative positions.
- Link card → `https://angliamorocco.org/faq/`: angliamorocco.org · Questions about the exams · How long each exam lasts, what it assesses and how levels are grouped.

#### Section: English benchmarks at AGI
How English develops through the K–12 school. Students who don't speak English at home often start half a level lower and catch up by middle school.
| Grade | Age | CEFR level | What students can do |
|---|---|---|---|
| Kindergarten | 5–6 | Pre-A1 / A1 | Understands simple classroom instructions and basic vocabulary. |
| Grades 1–2 | 6–8 | A1 – A2 | Speaks in simple sentences; reads short stories and writes simple sentences. |
| Grades 3–4 | 8–10 | A2 – A2+ | Follows lessons, writes short paragraphs and explains ideas in discussion. |
| Grade 5 | 10–11 | B1 | Reads chapter books and writes organized paragraphs. Elementary graduation benchmark. |
| Grades 6–8 | 11–14 | B1+ – B2 | Understands academic vocabulary and lectures; writes essays and analyses texts. |
| Grades 9–11 | 14–17 | B2 – C1 | Handles academic reading, research, debate and complex presentations. |
| Grade 12 | 17–18 | C1 | University-level reading and academic writing. |

#### Section: Anglia across Morocco
From its Agadir headquarters, Anglia Morocco works with schools, language centers and teachers in the Kingdom's twelve regions. Schools can become Anglia exam centers, and franchise opportunities are open in several regions, [TO CONFIRM: including Oujda, Fès, Agadir and Taroudant].
Anglia Morocco contacts: j.wilburn@angliamorocco.org · a.lam@angliamorocco.org
→ **Partnerships & franchise** (`partnerships.html`)
→ **angliamorocco.org** (`https://angliamorocco.org/`)

#### Section: Find your level.
Book a free Anglia level test – the office will suggest the right class afterwards.
→ **Book a level test** (`forms.html#enquiry/anglia`)
→ **Request a tutor** (`forms.html#tutor-request`)

#### Section: Other programs
→ **All programs** (`programs.html`)
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `special-education.html`: Inclusive · Special education (SEN) · Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care.
- Link card → `adult-diploma.html`: Age 16+ · Adult high school diploma · A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir.
- Link card → `teachers.html`: Educators · For teachers (C.I.T.E.) · The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship.
- Link card → `professional.html`: Professionals · Professional & medical English · Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching.
- Link card → `pathways.html`: Next steps · University pathways · An authorized admissions agent for universities and colleges in the UK, the United States and beyond.

---

### 4.11 `teachers.html`

- **Browser title:** For teachers – C.I.T.E. & training – AGI Agadir
- **Meta description:** Teach English with a lifelong credential: Anglia C.I.T.E. (TESOL), teacher training in Agadir, a 30-day internship and U.S. private-school sponsorship.

Home / Programs / For teachers [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Teach English with a lifelong credential.
Earn the C.I.T.E. from Anglia Examinations England, practice in AGI classrooms, and open a path to teaching abroad – with support from Morocco's Anglia headquarters.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
[PHOTO NEEDED – For teachers – students in class or activity]
Anglia Examinations England

#### Section: C.I.T.E. – Certificate for International Teachers of English
A TESOL qualification that proves both your English and your ability to teach it.
→ **Register on angliamorocco.org** (`https://angliamorocco.org/citem/`)
- **Lifelong** — A qualification with no expiration date, recognized worldwide.
- **Open to all** — No entry qualifications are required. It suits current teachers who want to validate their skills and aspiring teachers starting out.
- **Mapped to the CEFR** — Your certificate shows your English level on the same European framework schools and employers use.
- **Specializations** — [TO CONFIRM: General English, Young Learners and Very Young Learners]

#### Section: The 30-day teacher internship
Learn by doing, in real AGI classrooms in Agadir.
Step 01
**Week 1**
Orientation to the school and its methods, and classroom observation.
Step 02
**Week 2**
[TO CONFIRM: Co-teaching with a mentor teacher and lesson planning.]
Step 03
**Week 3**
[TO CONFIRM: Leading lessons with feedback, and assessment practice.]
Step 04
**Week 4**
Professional development workshops, a final survey and wrap-up.

#### Section: More for educators
- **USA teacher sponsorship** — Certification sponsorship for teaching in U.S. private schools. Requires a bachelor's degree, a clear background check and a sponsoring school. Fee: US$60. Not valid for U.S. public schools.
- **Mathematics in English** — For classroom teachers adding mathematics to their skills, and new teacher candidates who are not math majors: teach mathematics in English (SAT, IELTS) and qualify as a mathematics specialist or coach. Courses [link: “Courses” → `english-anglia.html#math-english`]
- **Teacher training program** — English teachers test and train in AGI classrooms to strengthen their language and their teaching.
- **TEFL / TESOL with Bridge** — Accredited TEFL/TESOL courses through AGI's partnership with Bridge Education Group.
- **Independent course studies** — Graduate-level, self-paced modules using books and journals; certificates approved by the American Canadian Board.
- **Teach a learning pod** — Freelance teachers can lead Anglia learning pods: small groups of about ten students over ten weeks, with materials supplied.

#### Section: Start your next step as a teacher.
Register for C.I.T.E. on angliamorocco.org, or ask us about the internship and sponsorship.
→ **Register for C.I.T.E.** (`https://angliamorocco.org/citem/`)
→ **Ask about the internship** (`forms.html#enquiry/programs`)

#### Section: Other programs
→ **All programs** (`programs.html`)
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `special-education.html`: Inclusive · Special education (SEN) · Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care.
- Link card → `adult-diploma.html`: Age 16+ · Adult high school diploma · A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir.
- Link card → `english-anglia.html`: All ages · English & Anglia exams · AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults.
- Link card → `professional.html`: Professionals · Professional & medical English · Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching.
- Link card → `pathways.html`: Next steps · University pathways · An authorized admissions agent for universities and colleges in the UK, the United States and beyond.

---

### 4.12 `professional.html`

- **Browser title:** Professional & medical English – AGI Agadir
- **Meta description:** Business and medical English in Agadir and online: Anglia Business English, team courses, medical English, exam proctoring and ADHD coaching.

Home / Programs / Professional & medical English [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Speak the language of your profession.
Practical English for the way you work – in business, in medicine and across borders – certified with Anglia Examinations England.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
[PHOTO NEEDED – Professional & medical English – students in class or activity]

#### Section: English for work
Start with a free level test; we'll recommend the right course and schedule.
- **Business English** — Anglia International Business English, certified in four steps from A2+ to C1: meetings, presentations, emails and negotiation.
- **Medical English** — For doctors, nurses and clinicians: the terms of the body systems, medical vocabulary and grammar, patient communication, handovers and medical papers – taught by a teacher with experience in the U.S. health system.
- **Courses for organizations** — Group courses for your team, on site at your company or at AGI, with progress measured on the CEFR.
- **One-to-one** — Private sessions at 200 MAD each, at times that fit a working schedule. All class prices [link: “All class prices” → `english-anglia.html#classes`]

#### Section: Professional services
- **Exam proctoring** — Paper and online exams invigilated at AGI for distance learners of North American and British universities, companies and certification bodies. Monday to Thursday, 9:00–17:00. A 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour.
- **ADHD holistic coaching** — One-to-one coaching for children and adults on focus, organization and time management, in Agadir and online, with Julie Wilburn, an accredited Holistic Therapeutic Coach (IPHM, ICAHP).
- **For teachers** — C.I.T.E. certification, teacher training and the 30-day internship have their own page. For teachers [link: “For teachers” → `teachers.html`]

#### Section: Find the right course.
Book a free level test, or tell us what your team needs and we'll reply within one working day.
→ **Book a level test** (`forms.html#enquiry/anglia`)
→ **Request a team course** (`forms.html#enquiry/programs`)

#### Section: Other programs
→ **All programs** (`programs.html`)
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `special-education.html`: Inclusive · Special education (SEN) · Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care.
- Link card → `adult-diploma.html`: Age 16+ · Adult high school diploma · A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir.
- Link card → `english-anglia.html`: All ages · English & Anglia exams · AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults.
- Link card → `teachers.html`: Educators · For teachers (C.I.T.E.) · The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship.
- Link card → `pathways.html`: Next steps · University pathways · An authorized admissions agent for universities and colleges in the UK, the United States and beyond.

---

### 4.13 `pathways.html`

- **Browser title:** University pathways – American Group International, Agadir
- **Meta description:** AGI Education Consultancy: an authorized admissions agent helping students in Morocco reach universities and colleges in the UK, the USA and beyond.

Home / Programs / University pathways [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** From Agadir to university.
AGI Education Consultancy is an authorized admissions agent. We help students choose a university, apply, and arrive ready – whether on campus abroad or studying online.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)
[PHOTO NEEDED – University pathways – students in class or activity]

#### Section: What we help with
Each case is studied individually, with a plan built around the student's goals.
- **Choosing and applying** — Matching programs to your goals and handling applications to partner universities, locally, abroad or online.
- **Moving abroad** — Accommodation, visa applications, health insurance and support for families.
- **Funding** — Help with scholarship and financial-aid applications.
- **More than one diploma** — Double-diploma programs and language training alongside your studies.
- **Career guidance** — Career counseling and cultural orientation before you leave.

#### Section: Partners
Part of a wider network of universities and colleges in the United States, Europe and Asia.
_United Kingdom_
**Chichester College Group**
Seven colleges in the south of England – Chichester, Crawley, Worthing, Brinsbury, Brighton MET, Northbrook and Haywards Heath – with UK progression routes for AGI learners.
→ **Read about the partnership** (`journal-ccgi-partnership.html`)
_Placement_
**Leverage Edu**
Our regional partner for the Souss and southern Morocco: private and public university placement, with housing assistance.
_English requirement_
**Anglia Proficiency**
Listed by UCAS as evidence of English for British universities – and taken right here in Agadir.
→ **English & Anglia exams** (`english-anglia.html`)
**Partner universities and colleges**
_United Kingdom_
**[TO CONFIRM: Royale Business College (RB College)]**
Academic and vocational programs.
_United Kingdom_
**[TO CONFIRM: Britts Imperial University College]**
Undergraduate and postgraduate pathways.
_United Kingdom_
**[TO CONFIRM: University of London]**
Distance-learning degrees.
_Spain_
**[TO CONFIRM: UCAM]**
Catholic University of Murcia.
_Switzerland_
**[TO CONFIRM: Geneva Business School]**
Business degrees.
_British education_
**[TO CONFIRM: SIST British Education]**
British-curriculum pathways.

#### Section: Plan your next step.
Tell us where you'd like to study. The office will reply within one working day.
→ **Start a conversation** (`forms.html#enquiry/programs`)
→ **Book a visit** (`forms.html#visit`)

#### Section: Other programs
→ **All programs** (`programs.html`)
- Link card → `k12.html`: Ages 5–18 · K–12 school · An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home.
- Link card → `special-education.html`: Inclusive · Special education (SEN) · Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care.
- Link card → `adult-diploma.html`: Age 16+ · Adult high school diploma · A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir.
- Link card → `english-anglia.html`: All ages · English & Anglia exams · AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults.
- Link card → `teachers.html`: Educators · For teachers (C.I.T.E.) · The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship.
- Link card → `professional.html`: Professionals · Professional & medical English · Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching.

---

### 4.14 `admissions.html`

- **Browser title:** Admissions – American Group International, Agadir
- **Meta description:** How to apply to American Group International in Agadir: steps, calendar, tuition and documents.

Home / Admissions [link: “Home” → `index.html`]
**Page title (H1):** Admissions
Tours are scheduled individually, so call for an appointment to meet us and see the school. Every new student sits placement assessments before admission — whatever system they arrive from — and registration for the coming year takes place on August 28 and 31.

#### Section: The application journey
01
**Enquire**
Call or email the admissions team to arrange a visit; tours are individual and include the school and the application process.
02
**Visit & Assess**
English/ESL proficiency and academic assessments, including the free Anglia placement test for language learners.
03
**Apply**
Prior school records and a behavior report, age and residency verification, immunization and physical examination records.
04
**Enroll**
Pay the annual inscription, confirm the monthly tuition plan, and order books from the beginning of August.

#### Section: Academic calendar
Registration days Aug 28 & 31
First day of classes September 7
Second semester begins January 5
Anglia examinations April
Graduation exercises June 17
Movable religious holidays — Eid al Mouloud, Ramadan, Eid al Fitr and Eid al Adha — are confirmed each term. Fall break runs October 12–18 and winter break December 18 – January 3.
Tuition & Fees
2,600 MAD per month, paid over ten months.
Plus one annual inscription at enrollment: 6,500 MAD for Kindergarten–Grade 1, rising to 11,000 MAD for Grade 12. Books, mathematics and Anglia English examinations, dual enrollment in the USA and Morocco, and student insurance are included. Inscription is non-refundable; fees are not negotiable.
Request the Tuition Guide

#### Section: What to bring
A child aged 5 by September 1 and under 21 on the first day of school is eligible for enrollment. AGI admits students of any race, religion, color, national or ethnic origin.
Apply Online Book a Visit [link: “Apply Online” → `forms.html#enrollment`] [link: “Book a Visit” → `forms.html#visit`]
Age
Birth certificate, hospital or physician certificate, passport or visa, or birth registration.
Residency
Lease or mortgage statement, utility bill, tax statement or deed, or a job contract — dated within three months.
Health
Immunization certification and a physical examination record.
Academic
Records from the previous school (or its address), plus a behavior report. IEP or special-needs provision requires practitioner documentation.

#### Section: Before you enroll
- **Family policies** — Attendance, promotion, placement, refunds and more, in brief. Read the policies [link: “Read the policies” → `policies.html`]
- **Ready to apply?** — Apply online in about five minutes, or book a visit first. Apply Book a visit [link: “Apply” → `forms.html#enrollment`] [link: “Book a visit” → `forms.html#visit`]

---

### 4.15 `policies.html`

- **Browser title:** Policies – American Group International, Agadir
- **Meta description:** AGI school policies: attendance, promotion and retention, placement, parent responsibility, refunds and complaints, media and service hours.

Home / Admissions / Policies [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`]
**Page title (H1):** Policies for families.
The rules we hold ourselves and our families to, in brief. The full texts are part of the AGI Academic Handbook and are available from the office.
→ **Request the full texts** (`forms.html#enquiry/programs`)
→ **Report an absence** (`forms.html#absence`)
- **Attendance** — K–12 students must attend 90% of the school year to be promoted. Parents give a dated, signed excuse for any absence within two days of the student's return. Arriving after 9:00 is a late arrival; after 10:00 it counts as a full-day absence. Five unexcused late arrivals equal one unexcused absence.
- **Promotion & retention** — Promotion follows the grade-level criteria: at least 64% (D) in each core subject – mathematics, science, language arts and social studies – 90% attendance, maturity shown through the year and the English assessment. Students who are not promoted may attend summer remediation and be retested.
- **Provisional placement** — Every new student sits English/ESL and academic assessments before admission, whatever system they come from, so placement holds even when previous records are incomplete.
- **Parent responsibility** — Enrollment begins with a 90-day adjustment period and shared expectations on attendance, participation, safeguarding and following up on learning at home.
- **Refunds & complaints** — One procedure across all divisions – the school, AGI Learning Pods, iHeart therapeutic services and Anglia Morocco – covering enrollment, refunds, complaints and counseling. The annual inscription is non-refundable.
- **School counseling** — Guidance from the school counselor is advisory: it supports academic success and personal growth but is not medical diagnosis or therapy.
- **Media** — How photos, video and live streams of school events may be used on the website, social media and print – always with consent and safeguarding first.
- **Service hours** — High school graduation requires 40 documented volunteer hours, ten each year, approved by the school.
- **Homework** — Nightly homework grows from 10–20 minutes in kindergarten to 2–3 hours in the last years of high school.

---

### 4.16 `student-life.html`

- **Browser title:** Student life – American Group International, Agadir
- **Meta description:** Life at AGI: a small international community in Agadir, service hours, homework, Saturday classes and events through the year.

Home / Student life [link: “Home” → `index.html`]
**Page title (H1):** A small school with a big world inside.
Students from more than 46 nationalities learn together in small multi-grade classes, where teachers know every child and every family.

#### Section: Life at AGI
A school day in Hay Nahda.
[PHOTO NEEDED – Morning circle or classroom discussion]
[PHOTO NEEDED – Science or art project]
[PHOTO NEEDED – Saturday Anglia class]
[PHOTO NEEDED – Students at a park outing]
[PHOTO NEEDED – Graduation day]
[PHOTO NEEDED – Spelling bee or school event]

#### Section: Voices of AGI
Parents, students and graduates.
> “Our daughter arrived speaking almost no English. Two years later she reads chapter books and corrects my pronunciation.” — Parent of a grade 3 student [SAMPLE – replace with a real testimonial]
> “The teachers know every child. When our son needed extra support, the plan was in place within weeks, and we were part of it.” — Parent of a grade 7 student [SAMPLE – replace with a real testimonial]
> “AGI gave me an American diploma and the English to use it. I'm now studying at university abroad.” — AGI graduate [SAMPLE – replace with a real testimonial]

#### Section: The school year
Highlights from the AGI calendar.
- **Moroccan & American holidays** — The calendar marks both: Green March and Independence Day, Thanksgiving, Amazigh New Year and the Eids.
- **Global Play Day** — A day each February given over to unstructured play, joined by schools around the world.
- **Anglia exams** — Every spring, students certify their English level with Anglia Examinations of England.
- **Spelling bee** — AGI students compete in the American National Spelling Bee of Morocco, held at the American Legation in Tangier. Read the story [link: “Read the story” → `journal/american-national-spelling-bee-in-morocco.html`]
- **Graduation** — The year ends in June with graduation for the senior class. Journal [link: “Journal” → `journal.html`]

#### Section: Service to the community
A graduation requirement for every high school student.
High school students complete 40 volunteer hours – ten each year – documented and approved by the school. Activities must benefit the community, be unpaid, and not be part of a regular job or family obligation.
Examples include community clean-ups, helping at local libraries and non-profits, tutoring younger students and helping at school events outside school hours.

#### Section: Homework
A guide to nightly homework by grade, so learning at home stays balanced.
| Grades | Per night | Typical work |
|---|---|---|
| K – 1 | 10–20 min | Reading with parents, simple math, basic writing |
| 2 – 3 | 20–30 min | Reading, spelling, math problems, short writing |
| 4 – 5 | 30–60 min | Reading, vocabulary, math, small projects |
| 6 – 8 | 60–90 min | All core subjects, foreign language, project work |
| 9 – 10 | 90–120 min | Core subjects, foreign language, electives |
| 11 – 12 | 120–180 min | Core subjects, AP courses, college preparation |

#### Section: For parents
The forms families use most.
- Link card → `forms.html#absence`: Report an absence · Before 9:00 on the day, for absences, late arrivals and early pick-ups.
- Link card → `forms.html#consent`: Park & outing consent · Permission for park visits and outdoor activities.
- Link card → `forms.html#feedback`: Parent feedback · Suggestions, praise or a concern, reviewed every week.

#### Section: See it for yourself.
The best way to know AGI is to visit during the school day.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)

---

### 4.17 `journal.html`

- **Browser title:** Journal – American Group International, Agadir
- **Meta description:** News, announcements and stories from American Group International and Anglia Morocco.

Home / The AGI Journal [link: “Home” → `index.html`]
**Page title (H1):** The AGI Journal
Announcements, partnerships, graduations and campus news, from the school's first years in Agadir to today.

#### Section: Archive
All 60 posts, grouped by year (newest first). Each row: date, category (Partnership, Achievement, Admissions, Programs, News), title, link to the article page. Full list in Appendix B.

---

### 4.18 `journal-ccgi-partnership.html`

- **Browser title:** AGI and Anglia Morocco partner with Chichester College Group – AGI Journal
- **Meta description:** AGI and Anglia Morocco partner with Chichester College Group International, opening UK progression routes.

Home / The AGI Journal / Article [link: “Home” → `index.html`] [link: “The AGI Journal” → `journal.html`]
Partnership · Agadir & Chichester
**Page title (H1):** AGI and Anglia Morocco join forces with Chichester College Group International
A new agreement links AGI's Agadir campuses to a seven-college group in the south of England — and opens a UK progression route for learners across the Souss and southern Morocco.
Anglia Morocco Newsroom · August 22, 2025 · 4 min read
C hichester College Group International is the international arm of Chichester College Group, which runs seven colleges in the south of England — Chichester, Crawley, Worthing, Brinsbury, Brighton MET, Northbrook and Haywards Heath. It is a familiar name in Agadir: Anglia Examinations has been based in Chichester since 1993, and AGI has used the Anglia system in its language programs since 2013.
The agreement gives AGI and Anglia Morocco learners a defined route into UK further and higher education, and gives CCGi a partner on the ground in the south of Morocco. AGI has held the Anglia franchise for the Kingdom since 2021 and manages the network's twelve regions from the Agadir headquarters.
“Anglia’s Proficiency examination is listed by UCAS — which means the English our students sit for in Agadir is the English a British university will recognize.”
For families, the practical effect is continuity: one English standard, assessed each April, that carries from a Grade 5 benchmark through to a UK college application. Enquiries about the pathway run through the Agadir admissions office.
Partnerships Anglia Morocco United Kingdom

#### Section: More from the Journal
Announcement
**Empowering educators in Morocco: our partnership with Bridge Education Group**
November 11, 2025
Partnership
**Leverage Edu and AGI join forces in the south of Morocco**
March 4, 2026
News
**Anglia Examinations celebrates thirty years**
October 1, 2023
All journal entries

---

### 4.19 `partnerships.html`

- **Browser title:** Partnerships & franchise – American Group International, Agadir
- **Meta description:** Franchise and institutional partnerships with AGI and Anglia Morocco across the Kingdom's twelve regions.

Global Network · Franchise & Partnerships
**Page title (H1):** Bring the AGI standard to your region.
AGI holds the Anglia Examinations franchise for Morocco and operates from Agadir across the Kingdom's twelve regions. We work with schools, language centers, freelance teachers and international institutions — and franchise opportunities are open in the English market for the right candidates.

#### Section: Two ways to build with AGI
Model I
**Franchise**
An Anglia Morocco center under your ownership, anywhere in the Kingdom's twelve regions. You get the examinations license, the placement and testing system, training, and the AGI standard behind it. Enquiries run through the Agadir headquarters.
— Anglia examinations license & materials — Teacher training and C.I.T.E. certification — Placement testing & level mapping to the CEFR — Territory agreement within the 12 regions
Model II
**Institutional Partnership**
For existing schools, language institutes and colleges: Anglia examination provision inside your campus, university pathway agreements, and co-designed English or academic programs under a shared quality framework.
— Co-designed English & academic programs — University pathway agreements (UK, USA, India) — Anglia testing center inside your campus — Shared quality framework & annual review

#### Section: The network today
Anglia Morocco is managed from the Agadir headquarters, with Anglia centers across the north and center of the Kingdom. Remaining regions are open for franchise. The full network and open representative positions are listed on angliamorocco.org. [link: “angliamorocco.org” → `https://angliamorocco.org/angliamorocco-networks-and-centers-12-regions/`]
Souss-Massa Headquarters · Agadir
Casablanca-Settat Anglia centers
Tanger-Tetouan-Al Hoceima Anglia centers
Rabat-Salé-Kénitra Anglia centers
Fès-Meknès · Marrakech-Safi Anglia centers
Oriental · Béni Mellal-Khénifra Open for franchise
Drâa-Tafilalet · Southern Provinces Open for franchise
graphic: network map — USA → Morocco → World

#### Section: Who we work with
Examination boards, colleges, placement partners and professional bodies.
United Kingdom
Chichester College Group International
The international arm of a seven-college group in the south of England — Chichester, Crawley, Worthing, Brinsbury, Brighton MET, Northbrook and Haywards Heath. Signed 2025.
Teacher training
Bridge Education Group
A global leader in teacher training and TEFL/TESOL certification. Partnership announced November 2025, opening professional development to educators across Morocco.
University placement
Leverage Edu
Official regional representation for Souss and southern Morocco since March 2026 — private and public university placement with housing assistance.
Plantation, Florida
American High School
Cognia-accredited online diploma program and a Yass Prize awardee. Partnership announced 2025; the diploma is accepted in the U.S. and internationally.
United Kingdom
RB College
UCAS-registered UK institution offering academic and vocational programs, including work-based Master of Business Administration routes.
Chichester, since 1993
Anglia Examinations England
AGI has been the Anglia franchise holder for Morocco since 2021 and has used the Anglia system in its language programs since 2013.
For teacherpreneurs
AGI Learning Pods
Small-group programs run by freelance teachers and parent groups under the Anglia system — inclusive, creative and affordable.
Membership
American School Counselor Association
AGI joined the ASCA network in 2026, bringing U.S. school-counseling standards to student guidance.

#### Section: Start the conversation
Franchise and partnership enquiries are handled from the Agadir headquarters. Tell us the region, the model and your teaching or business background, and we will come back to you.
Partnership Enquiry Meet AGI Connect [link: “Partnership Enquiry” → `forms.html#enquiry/partnership`] [link: “Meet AGI Connect” → `connect.html`]

---

### 4.20 `investors.html`

- **Browser title:** Partners & investors – American Group International, Agadir
- **Meta description:** Grow with AGI: a K–12 micro-school, the Anglia Morocco examinations network across twelve regions, teacher certification and professional English programs.

Home / Partnerships / Partners & investors [link: “Home” → `index.html`] [link: “Partnerships” → `partnerships.html`]
**Page title (H1):** Grow with AGI.
Since 2013, AGI has grown from a single room in Agadir into a K–12 school, an English examinations network across Morocco's twelve regions, and programs for teachers and professionals. We welcome conversations with partners who share our mission.
→ **Request the partner brief** (`forms.html#enquiry/partnership`)
→ **Partnerships & franchise** (`partnerships.html`)

#### Section: One mission, five activities
Affordable, creative and inclusive education, delivered through complementary programs.
_Since 2013_
**K–12 micro-school**
An American-curriculum school in Agadir: eight multi-grade classrooms and students of more than 46 nationalities.
_Since 2021_
**Anglia Morocco**
Anglia Examinations franchise holder for Morocco, with a network of centers and representatives across the twelve regions.
_Educators_
**Teacher certification**
C.I.T.E. (TESOL), teacher training, a 30-day internship and U.S. private-school sponsorship.
_Professionals_
**Professional English & services**
Business and medical English, team courses and exam proctoring.
_Pathways_
**University placement**
An authorized admissions agent with partners including Chichester College Group and Leverage Edu.
_International_
**American Group USA LLC**
AGI's U.S.-registered company [TO CONFIRM: (Maryland)], offering programs and coaching to clients worldwide.

#### Section: Why the model works
- **Built for working families** — An international standard at an accessible price reaches families that traditional international schools do not. AGI has placed hundreds of students into the American educational system with low-cost programs.
- **Recognized standards** — Accredited by the American Council of Training and Development, recognized by four U.S. state departments of education, and official partner in Morocco of Chichester College Group, UK. Accreditation [link: “Accreditation” → `about.html#accreditation`]
- **A format that travels** — Micro-schools and learning pods – small groups of about ten students – can open where demand is, without large campuses.
- **Presence today** — [TO CONFIRM: Agadir headquarters; Anglia network across Morocco's twelve regions; [to confirm: other Moroccan cities, Mauritania, United States]]

#### Section: Ways to partner
- Link card → `partnerships.html`: Open an AGI school or center · Franchise and institutional partnerships for schools and language centers.
- Link card → `https://angliamorocco.org/angliamorocco-networks-and-centers-12-regions/`: Represent Anglia in your region · Open representative positions in the Anglia Morocco network.
- Link card → `forms.html#enquiry/partnership`: Strategic partnership or investment · Request the partner brief and a conversation with Julie Wilburn.

#### Section: Let's talk.
Request the partner brief and we'll arrange a conversation.
→ **Request the partner brief** (`forms.html#enquiry/partnership`)
→ **Contact** (`contact.html`)

---

### 4.21 `contact.html`

- **Browser title:** Contact – American Group International, Agadir
- **Meta description:** Contact AGI in Agadir: 20 Rue Baalabek, Hay Nahda. Phone +212 528 843 349, WhatsApp +212 688 739 393, americanecoleagadir@gmail.com.

Home / Contact [link: “Home” → `index.html`]
**Page title (H1):** Contact AGI.
Send a message, call or visit. The office replies within one working day and is closed on Sundays.

#### Section: Send us a message
Full name
Enter your name
Email
Enter an email address, for example name@example.com
Phone or WhatsApp optional
Enter a phone number with the country code, for example +212 6 12 34 56 78
Topic
Choose…
Programs & admissions
Anglia examinations
Fees & payments
Documents & records
Partnership or franchise
Other
Choose a topic
Message
Write your message
Send message
Your message goes only to the AGI office in Agadir. See our privacy policy. [link: “privacy policy” → `privacy.html`]
Visit
Number 20, Rue Baalabek Hay Nahda, Agadir 80000 Open in Google Maps [link: “Open in Google Maps” → `https://www.google.com/maps/search/?api=1&query=20+Rue+Baalabek+Hay+Nahda+Agadir`]
Call
+212 528 843 349 Administration · in Arabic: +212 618 639 911
WhatsApp
+212 688 739 393 [link: “+212 688 739 393” → `https://wa.me/212688739393`]
Email
americanecoleagadir@gmail.com
Opening hours
[TO CONFIRM: Monday to Friday, 9:00–17:00] Closed on Sundays

#### Section: Looking for a specific request?
These forms go straight to the right person.
- Link card → `forms.html#visit`: Book a visit · Tours are arranged individually, Monday to Friday.
- Link card → `forms.html#enrollment`: Apply · Apply for a place in any AGI program.
- Link card → `forms.html#documents`: Request a document · Transcripts, certificates and attestations.

---

### 4.22 `connect.html`

- **Browser title:** AGI Connect (preview) – American Group International, Agadir
- **Meta description:** A preview of AGI Connect, the planned digital front desk of American Group International in Agadir: answers, visits and requests in one place.

AGI's Digital Front Desk
**Page title (H1):** AGI Connect
A virtual receptionist that welcomes every family, answers every question, books every visit and prepares every document — in any language, at any hour.
A conversation with AGI Connect Scripted preview
Visit AGI
With pleasure. Would you prefer a visit this week or next week?
This Week
Thursday at 10:00 is available at the Agadir campus, Hay Nahda. Shall I reserve it and send the details by email?
Reserve Thursday 10:00 See other times
Scripted demonstration. AGI Connect is in development – until it launches, reach the office through the contact page or the forms. [link: “contact page” → `contact.html`] [link: “forms” → `forms.html`]

#### Section: What the front desk handles
Welcome
**Visits & enquiries**
Books a visit to the Agadir campus and routes enquiries to admissions, Anglia or the front office.
Guide
**Program discovery**
Matches learners to K–12, adult diploma, Anglia English or SEN, and explains the placement assessments each requires.
Serve
**Documents**
Prepares transcript, attestation and enrollment-document requests before a human confirms them.
Grow
**Partner intake**
Qualifies franchise and Anglia territory enquiries for the Agadir headquarters team.
The exchange above is scripted for demonstration; the interaction system is architected for a real AI backend.
Prefer a form? Book a visit, request a document or send an enquiry. [link: “Book a visit” → `forms.html#visit`] [link: “request a document” → `forms.html#documents`] [link: “send an enquiry” → `forms.html#enquiry`]

---

### 4.23 `privacy.html`

- **Browser title:** Privacy policy – American Group International, Agadir
- **Meta description:** How American Group International and Anglia Morocco handle personal information on this website.

Home / Privacy [link: “Home” → `index.html`]
**Page title (H1):** Privacy policy.
How American Group International and Anglia Morocco handle the information you share on this website. Last updated October 2026.

#### Section: What we collect
When you send a form, write to us or call, we receive the details you give us – usually your name, contact details and information about the student or request. This website does not use advertising or tracking cookies. Fonts are loaded from Google Fonts, which receives your browser's standard technical information.

#### Section: How we use it
Only to handle your request and to provide the programs and services you ask about – for example to answer an enquiry, process an application or prepare a document. We do not sell your information.

#### Section: How forms are sent
Website forms are delivered to the AGI office by email. Information sent over the internet can never be guaranteed to be completely secure; please don't include more than the form asks for.

#### Section: Payments
We never ask for card numbers in our forms and do not store card details. Online card payments are made on a separate, secure payment provider's page, under that provider's privacy policy.

#### Section: Sharing
We share personal information only when the law requires it, to prevent fraud, or when you ask us to – for example sending your documents to a university.

#### Section: Links to other sites
Links to other websites are provided for convenience. We are not responsible for their privacy practices.

#### Section: Your questions
To ask about, correct or remove information you have given us, write to americanecoleagadir@gmail.com.

---

### 4.24 `terms.html`

- **Browser title:** Terms of use – American Group International, Agadir
- **Meta description:** Terms of use for the American Group International and Anglia Morocco website.

Home / Terms [link: “Home” → `index.html`]
**Page title (H1):** Terms of use.
The terms that apply to using this website. Last updated October 2026.

#### Section: About this website
This website is published by American Group International and Anglia Morocco, Number 20, Rue Baalabek, Hay Nahda, Agadir, Morocco.

#### Section: Information on the site
We work to keep program details, dates and fees accurate, but they can change. The office confirms fees, dates and availability before enrollment. Enrollment in any program is governed by the enrollment agreement and the AGI policies provided by the office.

#### Section: Using the forms
Please provide accurate information in our forms. Sending a form is a request; it does not by itself confirm a place, a booking or a payment.

#### Section: Content and marks
Text and images on this site belong to AGI or are used with permission. Partner names, seals and logos belong to their respective institutions.

#### Section: Links
Links to other websites are provided for convenience; we are not responsible for their content.

#### Section: Contact
Questions about these terms: americanecoleagadir@gmail.com.

---

## 5. Forms – fields and behavior

All forms live on one page (`forms.html`) with a list of forms and one form shown at a time; each can be opened directly by its address. An overview panel ("How it works") is shown when no form is selected: 1) Choose a form, 2) Fill it in – every field is required unless marked optional, 3) The office replies within one working day, Monday to Friday. Most-used shortcuts: Report an absence, Apply for a place, Payment notice, Request a transcript. Side panel: "Prefer to talk?" with phone numbers, WhatsApp, and "The office is closed on Sundays." Every form ends with: *Your details go only to the AGI office in Agadir and are used to handle this request.*

#### Form: Enrollment application (`forms.html#enrollment`)
- **Duration shown:** Takes about 5 minutes
- **Introduction:** Apply for a place at AGI, from kindergarten to grade 12, the adult high school diploma, Anglia English or special education. Send one application per student.
- **Have ready:** The student's previous school records and a behavior report; Proof of age and residency; Immunization and physical examination records; For an IEP or special-needs support: documentation from a licensed practitioner
- **What happens next:** Admissions contacts you to arrange the free placement test and a visit. Registration days for 2026ÔÇô27 are August 28 and 31. The annual inscription is paid once at enrollment and is non-refundable.

**Student**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Student's full name | text | yes |  |
| Date of birth | date | yes |  |
| Nationality | text | no |  |
| Program | select | yes | Options: KÔÇô12 school, Adult high school diploma (16+), English & Anglia exams, Special education (SEN), Teacher training & C.I.T.E., Education consultancy |
| Grade applying for | select | no | For the KÔÇô12 school; Options: Kindergarten, Grade 1, Grade 2, Grade 3, Grade 4, Grade 5, Grade 6, Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12, Not applicable |
| Preferred start | select | yes | Options: September 2026, January 2027, As soon as possible |
| Current or previous school | text | no |  |
| Languages spoken at home | text | no | Helps us plan English support |
| Learning support or health needs | textarea | no | Tell us about any IEP, diagnosis, allergy or condition we should know about. |

**Parent or guardian**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Relationship to the student | select | yes | Options: Mother, Father, Guardian, Self (adult learner), Other |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

**Confirm**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| I confirm the information is accurate and understand that the annual inscription is non-refundable. | checkbox | yes |  |

- **Submit button:** Send application

#### Form: Visit the school (`forms.html#visit`)
- **Duration shown:** Takes about 2 minutes
- **Introduction:** Tours are arranged individually so you can meet the team, see the classrooms and ask about the application process.
- **Have ready:** Two or three dates that suit you; The program you are interested in
- **What happens next:** The office confirms a time by phone or email. Visits take place Monday to Friday at 20 Rue Baalabek, Hay Nahda.

**Your visit**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Preferred date | date | yes |  |
| Preferred time | select | yes | Options: Morning (9:00ÔÇô12:00), Afternoon (14:00ÔÇô17:00) |
| Number of visitors | number | yes |  |
| Program of interest | select | yes | Options: KÔÇô12 school, Adult high school diploma, English & Anglia exams, Special education (SEN), Not sure yet |
| Anything we should know | textarea | no |  |

**Your details**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

- **Submit button:** Request a visit

#### Form: Report an absence (`forms.html#absence`)
- **Duration shown:** Takes about 2 minutes
- **Introduction:** Let the office know before 9:00 on the day if your child will be absent, arrive late or leave early.
- **Have ready:** Your child's name and grade; The dates, and the reason for the absence
- **What happens next:** The office records your notice. School policy still asks for a dated, signed excuse within two days of your child's return. Arriving after 10:00 counts as a full-day absence, and promotion requires 90% attendance.

**Student**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Student's full name | text | yes |  |
| Grade | select | yes | Options: Kindergarten, Grade 1, Grade 2, Grade 3, Grade 4, Grade 5, Grade 6, Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12 |

**Absence**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Type of notice | single choice | yes | Options: Full-day absence, Late arrival, Early pick-up |
| Date | date | yes | First day of the absence |
| Last day | date | no | Leave empty for a single day |
| Arrival or pick-up time | time | no | For a late arrival or early pick-up |
| Reason | select | yes | Options: Illness, Medical appointment, Family reason, Religious observance, Travel, Other |
| Details | textarea | no |  |

**Parent or guardian**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Relationship to the student | select | yes | Options: Mother, Father, Guardian, Other |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

- **Submit button:** Send absence notice

#### Form: Park & outdoor activity consent (`forms.html#consent`)
- **Duration shown:** Takes about 2 minutes
- **Introduction:** Give permission for your child to join a park visit or outdoor microschool activity. Send one form per child, per activity, before the activity date.
- **Have ready:** The name and date of the activity; An emergency phone number for the day; Any allergies, medication or health notes
- **What happens next:** Teachers receive your consent before the activity. If anything changes on the day, call the office.

**Student & activity**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Student's full name | text | yes |  |
| Grade | select | yes | Options: Kindergarten, Grade 1, Grade 2, Grade 3, Grade 4, Grade 5, Grade 6, Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12 |
| Activity | text | yes | For example: park visit, nature walk |
| Activity date | date | yes |  |
| Emergency contact name | text | yes |  |
| Emergency phone | tel | yes | Reachable during the activity |
| Allergies, medication or health notes | textarea | no |  |

**Parent or guardian**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Relationship to the student | select | yes | Options: Mother, Father, Guardian, Other |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

**Consent**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| I give permission for my child to take part in this activity, supervised by AGI staff. | checkbox | yes |  |
| Signature | text | yes | Type your full name as your signature |
| Date | date | yes |  |

- **Submit button:** Give consent

#### Form: Parent feedback (`forms.html#feedback`)
- **Duration shown:** Takes about 2 minutes
- **Introduction:** Tell us what is working, what could be better, or a concern you want the administration to know about. You can stay anonymous.
- **Have ready:** A specific example helps us act on your feedback
- **What happens next:** The administration reviews all feedback every week. If you ask for a reply, we contact you.

**Your feedback**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Topic | select | yes | Options: Teaching & learning, Communication, Safety & wellbeing, Facilities, Fees & administration, Other |
| Grade it concerns | select | no | Options: Kindergarten, Grade 1, Grade 2, Grade 3, Grade 4, Grade 5, Grade 6, Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12, Whole school |
| Your feedback | textarea | yes |  |
| Would you like a reply? | single choice | yes | Options: Yes, please reply, No reply needed |

**Your details**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | no | Leave empty to stay anonymous |
| Email | email | if reply = Yes, please reply | Needed if you want a reply |

- **Submit button:** Send feedback

#### Form: Payment notice (`forms.html#payment`)
- **Duration shown:** Takes about 3 minutes
- **Introduction:** Let the office know about a payment you have made, so it is matched to the right student and a receipt is issued.
- **Have ready:** Your transfer reference, cheque number or receipt number; The student's name and the months the payment covers
- **What happens next:** The office checks the payment and confirms by email. As a reminder: the annual inscription is paid once at enrollment, then tuition is 2,600 MAD a month over ten months.
- **Notice:** Never type card numbers into this or any other form. To pay by card, use AGI's secure online payment page, then send this notice with the receipt number.

**Payment**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Student's full name | text | yes |  |
| Payment for | select | yes | Options: Annual inscription, Monthly tuition, Summer school, Anglia examination, Graduation fee, Tutoring, Other |
| Months covered | multiple choice | no | For monthly tuition; Options: Sep, Oct, Nov, Dec, Jan, Feb, Mar, Apr, May, Jun |
| Amount (MAD) | number | yes |  |
| Date paid | date | yes |  |
| Payment method | select | yes | Options: Bank transfer, Cash at the office, Cheque, Card (online payment page) |
| Reference or receipt number | text | yes | Transfer reference, cheque number or online receipt number |
| Note | textarea | no |  |

**Payer**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

- **Submit button:** Send payment notice

#### Form: Request a tutor (`forms.html#tutor-request`)
- **Duration shown:** Takes about 2 minutes
- **Introduction:** Ask for one-to-one tutoring in English, mathematics or another subject, in Agadir or online.
- **Have ready:** The subject and the learner's current level or grade; What you want to achieve; When the learner is free
- **What happens next:** The office matches you with a qualified tutor, usually within 48 hours, and confirms the price and schedule with you.

**Learner**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Learner's full name | text | yes |  |
| Grade or level | text | yes | For example: Grade 7, Anglia Intermediate, adult |
| Subjects | multiple choice | at least one | Options: English, Mathematics, Science, Anglia exam preparation, Reading & phonics, French, Arabic, Other |
| What would you like to achieve? | textarea | yes |  |
| Where | single choice | yes | Options: In person in Agadir, Online, Either |
| Availability | textarea | no | Days and times the learner is free |

**Your details**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

- **Submit button:** Request a tutor

#### Form: Schedule tutoring sessions (`forms.html#tutor-schedule`)
- **Duration shown:** Takes about 3 minutes
- **Introduction:** Already matched with a tutor? Set the days and times of your sessions, or change an existing schedule.
- **Have ready:** Your tutor's name, if you know it; The days and times that work for you
- **What happens next:** Your tutor confirms the schedule, or proposes another time if a slot is taken.

**Sessions**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Learner's full name | text | yes |  |
| Tutor's name | text | no |  |
| This is | single choice | yes | Options: A new schedule, A change to my schedule |
| Subject | text | yes |  |
| Start date | date | yes |  |
| Preferred days | multiple choice | at least one | Options: Mon, Tue, Wed, Thu, Fri, Sat |
| Preferred start time | time | yes |  |
| Frequency | select | yes | Options: One session, Once a week, Twice a week, Three times a week |
| Session length | select | yes | Options: 45 minutes, 60 minutes, 90 minutes |
| Notes | textarea | no |  |

**Your details**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

- **Submit button:** Send schedule

#### Form: Request a document (`forms.html#documents`)
- **Duration shown:** Takes about 3 minutes
- **Introduction:** Order a transcript, enrollment certificate, attestation or diploma copy for a current or former student.
- **Have ready:** The student's full name and date of birth as on school records; The years the student attended; Where the document needs to go
- **What happens next:** The office confirms the processing time and any fee before preparing the document.

**Student**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Student's full name | text | yes |  |
| Date of birth | date | yes |  |
| Years attended | text | yes | For example: 2019ÔÇô2024 |
| Last grade completed | select | no | Options: Kindergarten, Grade 1, Grade 2, Grade 3, Grade 4, Grade 5, Grade 6, Grade 7, Grade 8, Grade 9, Grade 10, Grade 11, Grade 12, Adult high school diploma |

**Document**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Document | select | yes | Options: Academic transcript, Enrollment certificate, Attendance attestation, Diploma copy, Apostille-legalised copy, Other |
| Number of copies | number | yes |  |
| Language | select | yes | Options: English, French, Arabic |
| Purpose | text | no | For example: university application, visa, transfer |
| Delivery | single choice | yes | Options: Collect at the office, By email (PDF), By courier |
| Courier address | textarea | if delivery = By courier | Only needed for courier delivery |

**Requested by**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Relationship to the student | select | yes | Options: Former student (myself), Current student (myself), Parent or guardian, Other |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

- **Submit button:** Request document

#### Form: General enquiry (`forms.html#enquiry`)
- **Duration shown:** Takes about 2 minutes
- **Introduction:** A question that doesn't fit another form: programs, Anglia examinations, partnerships and franchise, careers or anything else.
- **Have ready:** Your question, with as much detail as you can give
- **What happens next:** The office passes your message to the right person and replies by email or phone within one working day.

**Your enquiry**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Topic | select | yes | Options: Programs & admissions, Anglia examinations, Partnership or franchise, Careers at AGI, Other |
| Organization | text | no | For partnership and franchise enquiries |
| Message | textarea | yes |  |

**Your details**

| Field | Type | Required | Hint / options |
|---|---|---|---|
| Full name | text | yes |  |
| Email | email | yes |  |
| Phone or WhatsApp | tel | yes | Include the country code, for example +212 |

- **Submit button:** Send enquiry


---

## Appendix B. Journal posts (60)

Full text of each post: `data/export/AGI_Website_Content_Export.json` → `news[]` (title, slug, date, markdown).

| Date | Title | Article page |
|---|---|---|
| 2026-06-16 | American National Spelling Bee in Morocco | `journal/american-national-spelling-bee-in-morocco.html` |
| 2026-04-06 | Julie Wilburn Officially Accredited as a Holistic Therapeutic Coach | `journal/4356-2.html` |
| 2026-03-04 | American School Counselor Association Member | `journal/american-school-counselor-association-member.html` |
| 2026-03-04 | LEVERAGE Edu X AGI Join forces in the South of Morocco. | `journal/leverage-edu-x-agi-join-forces-in-the-south-of-morocco.html` |
| 2025-12-13 | Celebrating Excellence with Our Partner | `journal/4292-2.html` |
| 2025-11-11 | Empowering Educators in Morocco: Our New Partnership with Bridge Education Group | `journal/empowering-educators-in-morocco-our-new-partnership-with-bridge-education-group.html` |
| 2025-08-22 | “American Group International and Anglia Morocco Join Forces with Chichester College Group International (CCGi) to Empower Global Learners” | `journal-ccgi-partnership.html` |
| 2025-06-24 | Back to School September 8th, 2025 | `journal/back-to-school-september-3-2025.html` |
| 2025-06-24 | Job Fair under Dar America | `journal/job-fair-under-dar-america.html` |
| 2025-06-24 | Graduation 2025 | `journal/graduation-2025.html` |
| 2025-03-09 | Partnership Through-out Morocco | `journal/partnership-through-out-morocco.html` |
| 2024-06-28 | Congratulations to the Class of 2024 | `journal/congratulations-to-the-class-of-2024.html` |
| 2024-06-28 | Have a Great Summer! | `journal/have-a-great-summer.html` |
| 2024-06-28 | Anglia Examinations Will Soon Offer Online Exams in Morocco | `journal/anglia-examinations-will-soon-offer-online-exams-in-morocco.html` |
| 2023-11-24 | Anglia Morocco Newsletter November 24, 2023 | `journal/anglia-morocco-newsletter-november-24-2023.html` |
| 2023-10-01 | Anglia Examinations Celebrates 30 years! | `journal/anglia-examinations-celebrates-30-years.html` |
| 2023-03-13 | RB College of United Kingdom | `journal/rb-college-of-united-kingdom.html` |
| 2023-03-13 | American Group International is now a member of The Global Schools Program | `journal/american-group-international-is-now-a-member-of-the-global-schools-program.html` |
| 2022-10-10 | Anglia Testing Session November 13-28, 2022 | `journal/anglia-testing-session-november-13-28-2022.html` |
| 2022-10-10 | Energia Structure of Intellect | `journal/energia-structure-of-intellect.html` |
| 2022-07-09 | School Starts on September 6, 2022 | `journal/school-starts-on-september-6-2022.html` |
| 2022-05-21 | A brief note from the Principal. Graduation 2022. | `journal/a-brief-note-from-the-principal-graduation-2022.html` |
| 2022-01-07 | First Semester Ends January 28th, 2022 for American School Students K-Grade 12. | `journal/first-semester-ends-january-28th-2022.html` |
| 2021-12-19 | Franchise Opportunities throughout Morocco | `journal/franchise-opportunities-throughout-morocco.html` |
| 2021-10-08 | Early Childhood Education and Care Diploma | `journal/early-childhood-education-and-care-degree.html` |
| 2021-10-07 | CEO of American Group International is the new Director of Operations of AngliaMorocco | `journal/ceo-of-american-group-international-is-the-new-director-of-operations-of-angliamaroc.html` |
| 2021-09-23 | Headquarters of AngliaMaroc in Agadir | `journal/headquarters-of-angliamaroc-in-agadir.html` |
| 2021-09-05 | Back to School | `journal/back-to-school.html` |
| 2021-06-14 | Congratulations Graduates 2021 | `journal/congratulations-graduates-2021.html` |
| 2021-06-08 | Inscriptions 2021-2022 | `journal/inscriptions-2021-2022.html` |
| 2021-06-08 | Summer School | `journal/summer-school.html` |
| 2021-03-08 | Graduation Set projected June 11th, 2021. | `journal/graduation-set-projected-june-11th-2021.html` |
| 2020-05-23 | Free Dyslexia Resource Test | `journal/free-dyslexia-resource-test.html` |
| 2020-05-19 | Last Day of School June 17, 2020 | `journal/last-day-of-school-june-17-2020.html` |
| 2020-05-14 | Online Classes for Language Students starting in June 2020. | `journal/online-classes-for-language-students-starting-in-june-2020.html` |
| 2020-04-20 | English Math Resources | `journal/english-math-resources.html` |
| 2020-04-16 | Admissions 2020-2021 | `journal/admissions-2020-2021.html` |
| 2019-06-13 | Congrats to Said El Ouahbi awarded his Masters of Business Administration and Management | `journal/congrats-to-said-el-ouahbi-awarded-his-masters-of-business-administration-and-management.html` |
| 2019-06-13 | First Adult High School Graduate! | `journal/first-adult-high-school-graduate.html` |
| 2019-06-12 | Congrats Dr. Kamal Sarjdine | `journal/congrats-dr-kamal-sarjdine.html` |
| 2019-06-12 | Back to School September 2, 2019 | `journal/back-to-school-september-2-2019.html` |
| 2019-04-18 | Inscriptions for 2019-2020 | `journal/inscriptions-for-2019-2020.html` |
| 2019-03-28 | Proctoring Services Available | `journal/proctoring-services-available.html` |
| 2018-11-12 | Anglia Testing Starting January 14th, 2019 | `journal/anglia-testing-starting-january-14th-2019.html` |
| 2018-11-08 | Lane Community College International Programs | `journal/lane-community-college-international-programs.html` |
| 2018-11-02 | Continuation of the work! | `journal/continuation-of-the-work.html` |
| 2018-11-02 | Anglia C.I.T.E. International Teachers Certification is available. TESOL. | `journal/anglia-c-i-t-e-international-teachers-certification-is-here.html` |
| 2018-09-23 | Languages Classes for Adults begin on Monday, September 24th and Tuesday September 25th. | `journal/languages-classes-for-adults-begin-on-monday-september-24th-and-tuesday-september-25th.html` |
| 2018-09-23 | Teachers Training Program in English | `journal/teachers-training-program-in-english.html` |
| 2018-09-14 | Educational Psychology Course October 2nd-December 12th, 2018 | `journal/educational-psychology-course.html` |
| 2018-05-25 | First Day of School is September 5, 2018 | `journal/first-day-of-school-is-september-5-2018.html` |
| 2018-05-25 | Programme d'études secondaires pour adultes en anglais et en espagnol | `journal/programme-detudes-secondaires-pour-adultes-en-anglais-et-en-espagnol.html` |
| 2018-05-06 | Summer School for Academic and Language EFL Students 2018 | `journal/summer-school-for-academic-and-language-efl-students-2018.html` |
| 2018-04-19 | Work Experience Degree Celebration | `journal/work-experience-degree-celebration.html` |
| 2018-04-19 | Awarding of Language Students April 17, 2018 | `journal/awarding-of-language-students-april-17-2018.html` |
| 2018-04-19 | A Day At The Seamstress | `journal/a-day-at-the-seamstress.html` |
| 2018-01-09 | Birthday Celebration At Fine Burger | `journal/decision-making-by-coaches-and-athletes-in-sport.html` |
| 2018-01-09 | Fun Times In Our Conversation Classes | `journal/successful-students-celebrating-graduation-degree.html` |
| 2018-01-09 | American Group International's New Year Eve Party 2017 | `journal/software-and-computer-workshop-and-conference.html` |
| 2018-01-09 | Holiday Celebrations | `journal/student-using-microscope-in-science.html` |
