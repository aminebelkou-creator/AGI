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

#### Section: Come and meet us.
The best way to know AGI is to visit during the school day.
→ **Book a visit** (`forms.html#visit`)
→ **Contact** (`contact.html`)

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
- **UCAS Recognition** — The Anglia Mastery (C2) qualification carries UCAS tariff points for British universities.
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

#### Section: In Julie's words
As Educational Director and Franchise Director of Anglia Morocco, I’m responsible for developing, administering, and overseeing all educational programs at the Learning Center. I supervise both the full-time high school and primary school international American programs, lead curriculum development, testing, and student and staff assessments, and plan staff training, teacher evaluations, and professional development. I manage student recruitment, community outreach, and staff and student relations, as well as the social skills and discipline program. I also actively teach in the classroom.
We believe in equality and that an international education empowers students to open global opportunities for their personal growth and success. While we offer a complete education from age five through grade 12, we welcome students at any stage and help them adapt to the AGI curriculum and language immersion process, enabling them to learn English while preserving their native languages.
Our diverse program embraces many nationalities, with a focus on student happiness, as we believe a happy child is more likely to succeed. We teach social skills for the whole development of the child and integrate Montessori and Waldorf theories into our American correspondence program.
We also offer programs for adults, associations, small groups, and one-on-one studies, including adult correspondence programs to help learners master English in order to succeed in their chosen fields. Please visit us as we embark on a wonderful journey together.
Thank you,

#### Section: Julie Wilburn, Director
شكرا لك،
About
- Our story [link: “Our story” → `our-story.html`]
- Founder's letter [link: “Founder's letter” → `founder-letter.html`]
- Mission & handbook [link: “Mission & handbook” → `handbook.html`]

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

#### Section: More programs and services
For teachers, adults, families and professionals.
- Link card → `teachers-cite.html`: Teachers · C.I.T.E. / TESOL certification
- Link card → `teachers-usa-sponsorship.html`: Teachers · USA private-school sponsorship
- Link card → `teachers-careers.html`: Teachers · Teach with AGI
- Link card → `programs-independent-studies.html`: Adults & professionals · Independent course studies
- Link card → `programs-learning-pods.html`: Adults & professionals · Learning pods & fast track
- Link card → `services-document-editing.html`: Adults & professionals · Document editing
- Link card → `services-proctoring.html`: Adults & professionals · Exam proctoring
- Link card → `wellbeing.html`: Wellbeing (i-Heart) · i-Heart therapeutic services
- Link card → `wellbeing-adhd-coaching.html`: Wellbeing (i-Heart) · ADHD holistic coaching
- Link card → `wellbeing-play-therapy.html`: Wellbeing (i-Heart) · Holistic play therapy
- Link card → `online-tutoring.html`: Online · Online tutoring
- Link card → `agi-usa.html`: Online · American Group USA LLC

---

### 4.7 `k12.html`

- **Browser title:** K–12 school – American Group International, Agadir
- **Meta description:** AGI's American-curriculum micro-school in Agadir, kindergarten to grade 12: lower, middle and upper school, inclusive education, course of study by grade.

Home / Programs / K–12 school [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** K–12 school.
An American-curriculum school, from the first day of kindergarten to the last day of grade twelve.
→ **Start admissions** (`admissions.html`)
→ **Book a visit** (`forms.html#visit`)

#### Section: At a glance
AGI is a child-centered micro-school in Agadir, established in 2013. Small classes, American curriculum standards, and ESL through the Anglia Examinations system of England for children who do not speak English at home. Students are welcomed at any stage and supported to adapt to the curriculum and the language immersion.
- **Ages** — 5–18
- **Curriculum** — American
- **Languages** — English · French · Arabic
- **Campus** — Agadir · Hay Nahda

#### Section: Three schools, one journey
[PHOTO NEEDED – Lower school classroom]
_K – Grade 5_
**Lower School**
English and spelling, literature, mathematics, natural science and foreign language – with penmanship in grades 2 to 4 and ESL alongside. The elementary benchmark is CEFR B1 by the end of grade 5.
[PHOTO NEEDED – Middle school class]
_Grades 6 – 8_
**Middle School**
American, world and Islamic history, earth and biological science, and mathematics through Foundations and Pre-Algebra. Middle school graduates at grade 8 target CEFR B2.
[PHOTO NEEDED – Upper school students]
_Grades 9 – 12_
**Upper School**
English I–IV, U.S. History, Algebra I and II, Geometry, Biology, Government and Economics. Two routes: the Florida-accredited books program or the Cognia-accredited American High School Online. Forty service hours are required to graduate.

#### Section: Inclusive by design
AGI welcomes students with a range of special needs, learning differences and mental-health challenges, physical and developmental alike. Documentation from a licensed practitioner is required so provision can be planned properly.
→ **Special education** (`special-education.html`)
- **Individualized plans** — Individualized Education Plans written to each student's needs and abilities.
- **Small groups** — Class sizes that allow personalized attention within mainstream school life.
- **Therapeutic support** — Occupational therapy, speech-language pathology and behavioral support.
- **Cognitive programs** — Energia SOI, customized for students with reading and mathematics difficulties.

#### Section: How the year is measured
90% Minimum attendance to qualify for promotion, K–12.
64% Pass mark in each core subject – math, science, language arts, social studies.
April Anglia English assessment, required of every enrolled student.
40 Service hours across four years of high school – ten per year.
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
→ **tuition & fees** (`fees.html#high-school`)
and
→ **English benchmarks** (`english-anglia.html#cefr`)
.

#### Section: About the school in detail
- **Q: Full text as published by AGI** — A: *School Subjects can change depending on the child. We also include ESL for non-native English speakers using the Anglia Examinations of England System.* Native means that the main language in the home is English. If you do not use English in the home your child is considered a language learner. American Group International Curriculum Standards Elementary/Junior High Subjects Students in elementary and junior high have a standard set of subjects to take each year. Below is a list of the normal schedule for each of these grade levels. 1 st Grade 5 th Grade F105 E105 L105 M105 S105 Foreign Language English and Spelling 1 Literature 1 Mathematics 1 Natural Science ESL F125 E125 H125 L125 M125 S125 English and Spelling 5 The Beginner’s Amer. Hist. Literature 5 Mathematics 5 Beginner’s Phys. & Health 2 nd Grade 6 th Grade F110 E110 H110 L110 M110 S110 V702 English and Spelling 2 The U.S. Presidents Literature 2 Mathematics 2 Penmanship* F130 E130 H130 L130 M130 S130 English and Spelling 6 U.S. Geography/Moroccan History Literature 6 Mathematics 6 Earth Science 3 rd Grade 7 th Grade F115 E115 H115 L115 M115 S115 English and Spelling 3 Great American Heroes Literature 3 Mathematics 3 Creation F135 E135 H135 L135 M135 S135 English and Spelling 7 World Geography/Islamic History Literature Math 7 Biological Science 4 th Grade 8 th Grade F120 E120 H120 L120 M120 S120 English and Spelling 4 Our Fifty United States Literature 4 Mathematics 4 F140 E140 H140 L140 M140 S140 English and Spelling 8 Intro. World /European History Math Foundations. /Pre-Algebra General Science/ *Penmanship is recommended to be taken each year from 2 nd grade through 4 th grade. High School Graduation Plan For our high school students, we have a plan of what classes are needed to be able to obtain a high school diploma. We have included the plan below broken down by grade level. Students are placed into the program for high school that fits the student’s needs. 9 th Grade F145 E145 H145 M145 S145 V730 PE English I U.S. History Algebra I Physical Science Principles of Music Physical Education 10 th Grade Kindergarten F150 E150 H150 M150 S150 EL English II World History Geometry Biology Elective F100 E100 L100 M100 S100 English Reading Phonics Math Science 11 th Grade F155 E155 M155 S155 English III Algebra II Health High School Learning service hours are 10 per year at 40 over the 4-year high school plan. 12 th Grade F160 E160 H160 M160 S160 English IV U.S. Government/Economics Business Math Scientific Creationism Other electives and AP courses are available for students to take, but this should be planned out starting in Grade 9. Students and parents, she be involved in the type of high school program they need the student to be enrolled in. This will be important for the type of studies they would like to obtain. *Special Education* English / Arabic Math / ESL Science / Electives History / Electives Our Schools Techniques and Vision: Montessori/Forest Practices 3 to 6-year-old- early learning through work play. Learner led explorations Skill teaching and curious learners are driven. Personal development Guide children in self-directed activity/activities. Community based program Children’s freedom in the classroom. Holistic Positive discipline Student leading activities are encouraged Children learn at their pace. Inclusive learning/Diversity Waldorf Practices 3 to 7 learning by play. Importance of home native language. Children wait till age 7 to start formal education. Anglia Examinations Exams, UK. Spirituality World University Partnerships. The use of art in language learning formation in painting and drawing. Free thinking is encouraged. Social Skills learning from Boys Town, USA American Curriculum 36 Week program. No focusing on major testing until after the 8 th grade. 180 school days CAT Testing after the 8 th grade. California Achievement Test 10 month/2 month summer Traditional American Grading system. Summer school for challenged students. American Transcripts K3-Grade 12. Ages 3 to 18. Yearly Language Testing No child left behind/ Small class ratio. Limited Homework-Homework policy posted Additional Techniques Working with special needs children. Global love and respect for all people. Learning love and respect for animals and nature. Chores for learning responsibility. Small class ratio. Enforce critical thinking skills. No lecture teaching. Micro-school pod environment. Exploration of the activities, emphasis on critical thinking, and independent research. AP classes, SAT and ACT prep. Limited homework- mostly prefers children to have bonding time with family. Sports Diploma Available for Athletes. Online Franchise School through our institution throughout Morocco American High School American Worldwide Academy Online School LMS for High School Online for High School Fast Track. One Year. Preferred for Ivy League student/ Cognia Both Programs Must know English of B1 or higher. We combined these principles for our own specialized program! Assessment of each individual child. We are a supporter of Inclusive Education. All children deserve a chance at an education. Our Institution’s accreditation is currently with The American Council of Training and Development and Meridian Learning Micro School Grassroots movement. AGI does not guarantee the transferability of its credits to any other institution or acceptance of its diploma to meet college/university entrance requirements or requirements of potential employers or in other language systems. The acceptance of transfer academic credits and academic credentials to another institution is determined by the receiving institution. Courses in AGIs high school program may or may not transfer to other institutions and depends solely on the receiving institution’s criteria and determination. It is advisable that parents talk with our educational consultant to see what programs our institution offers for your situation. - School + Home + Community = Student Success AGIC School in Agadir is a customized private school nestled in the Berber community of Souss Draa in Morocco, North Africa. The first classes of the small school were started in 2013 with five children. In the last 11 years, our program has hosted more than 46+ nationalities. We soon outgrew the one-room school so we moved to our location in Nahda, Agadir. Our institution has an open enrollment policy as we are a specialized school for students that need special programs that the Moroccan system might not fill. Today American Group International School hosts Kindergarten through 12th-grade students and they are taught in eight multi-grade classrooms. AGI Philosophy The philosophy of AGI stresses on academic excellence, discipline, ethical standards, and respect for others and for AGI. This philosophy encompasses the intellectual, social, emotional, character, and physical development of students. We want students to foster a general respect for all humanity. AGI Vision Since 2013, American Group Internationals faculty and staff have provided students and families with an educational culture best described in our Vision Statement. AGI inspires students to become Inclusive students through language. lifelong learners who pursue excellence, model integrity, and honor cultural diversity. We educate the whole person by equipping minds and building character, empowering students to serve their local community, in Morocco and the global world community, with wisdom and compassion and understanding. American Group International is a K-12 American International School which has served students from over 46+ plus different countries. AGI is the first American school in Agadir. Currently our mission focuses on affordability for the local community and programs in place that will help the normal working class in the Kingdom.
Related
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Supplies list [link: “Supplies list” → `supplies.html`]
- Homework [link: “Homework” → `homework.html`]
- Special education [link: “Special education” → `special-education.html`]

#### Section: Ready to meet the school?
Start admissions, or book a visit during the school day.
→ **Start admissions** (`admissions.html`)
→ **Book a visit** (`forms.html#visit`)

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

#### Section: Special education services in detail
- **Q: Full text as published by AGI** — A: Embracing Diversity: Our Commitment to Special Education (SEN) At American Group International, we are proud to offer a warm and inclusive environment that welcomes students with a wide range of special needs, learning differences, mental health challenges, and specific disabilities—both physical and developmental. We understand that each child is unique, and we are dedicated to providing the support and resources necessary for their success. Our Approach – Individualized Support: We create Individualized Education Plans (IEPs) tailored to the specific needs and abilities of each student. – Small Group Settings: Our small class sizes ensure personalized attention and a supportive learning environment. – Comprehensive Services: From occupational therapy to speech-language pathology and behavioural support, we provide a holistic approach to education and development. – Inclusive Education: We believe in fostering an inclusive community where every student feels valued, respected, and empowered to thrive. Special Needs High School Program (SEN) Our high school program is specially designed to meet the academic, social, and emotional needs of high school students with special needs. With a focus on life skills, vocational training, and preparing for independence, we aim to equip students with the tools they need to succeed beyond graduation. Join Our Community Whether you’re exploring educational options for your child or seeking a supportive environment that understands and celebrates diversity, American Group International is here for you. Contact us today to learn more about how we can support your child’s educational journey. Please see us if you know a child who could benefit from our Special Education Services. Physical Education Arabic English Math Science History Reading Spelling Fine Arts-Random ESL Thank you, Julie Wilburn Educational Director References of Services American Group International School Attn: Mr. Julie Wilburn, Director Agadir, Morocco May 24, 2024
Related
- Placement policy [link: “Placement policy” → `placement-policy.html`]
- For parents [link: “For parents” → `parents.html`]
- Book a visit [link: “Book a visit” → `forms.html#visit`]

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

#### Section: Program details and courses
- **Q: Full text as published by AGI** — A: American Worldwide Academy American Worldwide Academy in partnership with American Group International School. Wants to give you success and…… All the students will learn English and be required to take an English Exam. We will not fraud the American Educational System. Make your dreams come true…. We proctor all tests onsite in our centre. Available in English! AGI seeks to serve individuals 16 years or older. 18 or older in age, and older who terminated their secondary education prior to matriculating by offering a nationally accredited, low-cost, self-directed, independent-study high school completion program through correspondence-based or online-based studies. We provide this service at a very modest fee that is inclusive of all support to ensure success; tutorial assistance, and post-graduation services such as official enrolment or graduation verification; letters of recommendation to authorized third parties, and official academic transcripts on behalf of those graduates seeking to pursue higher education. Pictured below is the first student that graduated from the program and received a diploma from the USA. This program is supported by the Department of Education in Florida. ENGLISH LANGUAGE WRITING SKILLS (2 Credits) English Usage, Essentials of Grammar, Sentence Structure, English Mechanics, Punctuation, Rules of Spelling, ENGLISH LITERATURE (2 Credits) Classical Literature: Fictional Novels, Poetry, and Prose Contemporary Literature: Non-Fiction – Biographies and Commentaries GENERAL MATHEMATICS (3 Credits) Arithmetic: Basic functions using whole numbers, fractions, decimals, and percentages; Consumer Mathematics: standard measurements- perimeter, area & volume, distance, interest, and cost; Number Relationships: ratio and proportion, using the percent triangle; Comparing and Ordering Numbers; Number Relationships: using order of operations to solve multi-step problems: Data Analysis: tables and charts, bar graphs, line graphs, and pie charts, mean and median, ratio and probability; Algebra & Geometry. SOCIAL SCIENCE I – AMERICAN HISTORY (2 Credits) Early American History: Pre-colonial, Colonial, British rule of the Colonies, the American Revolution, French-Indian Wars, The Louisiana Purchase, The Texas Revolution and Mexican War, The American Civil War: Overview, Slavery and its role in the Civil War, Cessation of Southern States, Fighting the War. World War I – An American Historical Perspective. The Great Depression – causes and solutions, FDR and The New Deal. World War II – Rise of Fascism and formation of the Axis powers, United States’ involvement, Allied powers’ victory, the defeat of Japan, Birth of the United Nations, IMF, and World Bank. Post-World War II and the beginnings of the Cold War – The rise of Communism and the arms race, the NATO Alliance, the expansion of Communism and the growing threat to the US. Contemporary American History – The Korean War; the Civil Rights Movement; The Kennedy Era; End of the Civil Rights Movement; Crises in Southeast Asia- The Vietnam War; Invasion of Laos, Conflicts in Cambodia, US withdrawal, Nixon’s resignation and a final end to the war. SOCIAL SCIENCE II – AMERICAN GOVERNMENT (2 Credits) Structure and functions of City, County, and State Governments. The Federal Government: Office of the President, Executive Powers, the Executive Cabinet structure and functions. United States Congress: structure and functions of the US Senate and the US House of Representatives. The Supreme Court: structure and functions of the federal judiciary, Supreme Court procedures, historical “landmark” cases. SOCIAL SCIENCE III – WORLD HISTORY (3 Credits) Ancient Egypt, Mesopotamia, Phoenicians, Hebrews, The Persian Empire, Ancient Greece, Macedonia, The Roman Empire: the conquest of Italy, early Roman government, the Punic Wars, Roman Law. India and Southeast Asia – Buddhism, Hinduism, and Islam; History of the Far-East: China, Japan, and Korea; Origins of the Chinese Feudal system, unification of China’s regions and development of a “Great Civilization”, the final dynasties, Chinese philosophers, the “People’s Revolution, Communist rule of China. History of South America: Native Ancestry, the Mayas, the Aztecs, the Incas. History of Africa: Early North Africa, Ancient Africa, contact between the Ancient World and Africa, the spread of Christianity, how Islam influenced Africa, Empires of West Africa, the Atlantic Slave Trade, Early East Africa, Early Central Africa, Kongo, and Portuguese influence, Early Southern Africa, formation of states in Southern Africa, the discovery of South Africa’s mineral wealth, European influences and exploits, abolition of the slave trade, Africa and the World Wars. Rise and Fall of The Byzantine Empire, Western Europe, and the Middle Ages, Early history of England, the influence of the Catholic Church in Medieval Europe, and the Crusades. Modern History- the Renaissance and the Reformation, the Age of Discovery, the rise of nation-states and the expansion of empires, How Russia became a nation, the Age of Absolutism, the Age of Reason – Enlightenment and the birth of the Scientific Method, the French Revolution, the Agricultural and Industrial Revolutions, Communism, the Triumph of Democracy and the struggle for equality SCIENCE I – BIOLOGY (2 Credits) Cellular biology, comparisons between plans and animal cells, function of organized cells and tissues, compounds in living cells, cell division, reproduction and differentiation, the Animal Kingdom – descriptions of phyla: vertebrates and invertebrates, SCIENCE II – HUMAN BIOLOGY (2 Credits) The Skeletal System, the Muscular System, the Nervous System, the Endocrine System, the Respiratory System, the Circulatory System, the Digestive and Excretory Systems, and the Reproductive System. The above outlines the subject matter comprising our nationally accredited high school diploma program designed for individuals who prefer home schooling or an online high school completion program. Upon successful completion of these subjects, students will be administered a proctored final exam whose results will be factored into the student’s cumulative academic record. This is an accredited program in the USA and approved by the Department of Education in the State of Florida. American Worlwide Academy (Awa) High School Diploma Programs Students will have the option of choosing either the Standard High School Diploma with Career Training Certificate (24 credits) or the Standard High School Diploma (24 credits). Each course is worth either one (1) credit or half (.5) credit. STANDARD HIGH SCHOOL DIPLOMA WITH CAREER TRAINING CERTIFICATE This 24 credit program prepares students for entry for careers in various fields, while earning a high school diploma. The program emphasizes: customer service, retail sales, sales, hospitality, marketing, and management. Students will be provided with all books, supplies, study materials, class schedule, and direct teacher and counsellor contact information. Each semester must be concluded with a final exam to ensure understanding of course materials. Students must complete: 4 credits in English, 4 credits in Math (including Algebra 1 & Geometry), 3 credits in Natural Science, 3 credits in Social Studies (with 1 credit American History, 1 credit in World History, and 1/2 credit each in US Government and Economics), 1 credit of Health, 5 credits of electives, and 4 credits of focus on Career Certificate. Additionally, students must complete a capstone workshop to earn the Career Certificate. A minimum GPA of a 2.0 on a 4.0 scale is required for graduation.NOTE: Students are required to meet with their school counsellor at least once per month. Evening and Weekend classes available. If you are not 18 you need to attend classes as a regular school student. Standard High School Diploma This 24 credit program prepares students for life after high school for those seeking to continue their education or enter into the job market. Students will be provided with all books, supplies, study materials, class schedule, and direct teacher and counsellor contact information. Each semester must be concluded with a final exam to ensure understanding of course materials. Students must complete: 4 credits in English, 4 credits in Math (including Algebra 1 & Geometry), 3 credits in Natural Science, 3 credits in Social Studies (with 1 credit American History, 1 credit in World History, and 1/2 credit each in US Government and Economics), 1 credit of Health, and 9 credits of electives. A minimum GPA of a 2.0 on a 4.0 scale is required for graduation. NOTE: Students are required to meet with their school counsellor at least once per month. Credit Recovery Program Students can take credits from AWA and transfer them back to the secondary institution (i.e. High School) that he or she currently attends. The student bears the responsibility to verify that the credits will be accepted and approved by the secondary institution prior to enrolling into AWA. A maximum of 2 credits can be taken for this program.
Related
- Independent course studies [link: “Independent course studies” → `programs-independent-studies.html`]
- Business & medical English [link: “Business & medical English” → `professional.html`]
- Learning pods & fast track [link: “Learning pods & fast track” → `programs-learning-pods.html`]
- Document editing [link: “Document editing” → `services-document-editing.html`]
- Exam proctoring [link: “Exam proctoring” → `services-proctoring.html`]
- Prices [link: “Prices” → `fees.html`]

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
- **Recognized in the UK** — Anglia Examinations is a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding. The four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual. The Mastery (C2) qualification carries UCAS tariff points for British universities.

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

#### Section: In detail
- Link card → `teachers-cite.html`: C.I.T.E. / TESOL certification
- Link card → `teachers-usa-sponsorship.html`: USA private-school sponsorship
- Link card → `teachers-careers.html`: Teach with AGI
- Link card → `journal/early-childhood-education-and-care-degree.html`: Early childhood education & care diploma

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

#### Section: Business and medical English in detail
- **Q: Full text as published by AGI** — A: Corporate EFL Trainings/ Business English Business English Classes and International Exams English is the lingua-franca of business. No matter where in the world you live or work, the ability to communicate effectively in English is a definite advantage when conducting business. In an increasingly globalised world, being proficient in business English gives you a competitive edge. The four steps of the Anglia Business English exams, ranging in level from A2+ to C1 on the CEFR, test the English proficiency level of students whose special interest is business. Candidates may be considering a future in an international workplace or may already be working in the professional world and be keen to evaluate their linguistic competence. With an emphasis on practical business application in realistic situations, our communicative exams offer a progressive choice of levels: A2+, B1, B2 and C1, and test all four skills of reading, writing, listening and speaking. English is the number one language that connects speakers of different languages, and it is impossible to underestimate the importance of business English in opening the door to a vast number of potential markets and clients. Miscommunication across global business costs companies billions of dollars each year. The solution could be as straightforward as training delegates through a standard ‘General English’ program – alternatively, it may be necessary to train ESL teachers in aspects of technical English or industry specific English, to your industry or business. The return on investment from a business English training course cannot be underrated, watch as employee efficiency and communication dramatically improves, allowing you more time and money to focus on the decisions that really matter. We can make a time table to accommodate your companies’ needs with on-site job training or using the classroom space available in our institution. Our experience extends into Imports and Exports, Agriculture, and working with international companies located in the Agadir Port. No matter your specialty, as a medical professional your foremost concern should always be the tongue. It is the tongue – and the language that is generated by it – that allows health providers to communicate with patients and medical colleagues, speak at seminars and medical meetings – ultimately – how to read and write medical papers. Though patients – and their mother tongues – come in all different shapes and sizes, more and more it is English that is on the tips of the tongues of patients around the world. That is because even though in today’s increasingly globalized world a doctor’s patients may speak many different languages, the special status that English enjoys as the 21st Century’s lingua franca means that it is increasingly called upon to unite doctor and patient in examining rooms around the world. After all, in addition to the 500 million people worldwide who speak English natively, more than a billion more – or all together a quarter of the world’s population – speak it as a second language. Thus the role of English in medicine cannot be overstated. So whether you are working in an English-speaking country or even in your own home country, there will come a time when you will need to rely on English to communicate. All this, then, explains why it is important to learn medical English. In so doing, medical professionals of all types – be they general practice physicians, specialists, nurses, pharmacists, paramedics, and even medical volunteers – will be able to meet the needs of their patients, be better equipped to console the loved ones of their patients, and be better prepared to communicate with other medical professionals who speak English. Given the obvious advantages, it is easier to understand why you learn medical English than it is to understand exactly how. Fortunately, a growing number of English language programs are offered throughout the English-speaking world to meet the needs of aspiring medical professionals. Be forewarned, however: such medical English courses are not like normal intensive English programs. As specialized programs, designed to foster the ability to communicate in English in a hospital or clinical setting, students should already have mastery of general (conversational) English at an intermediate or advanced level and be ready to add to their working knowledge of the language. In much the same way, because the focus is on language and not science, students should have an understanding of anatomy, physiology, and indeed of their medical concentration in general in their native language, as well. Students will be best able to learn medical English by using a strong foundation in both conversational English and medical science as a springboard for success. Though courses may vary depending on the provider, when it comes time to choose a medical English course, there are certain things to look for. A quality program, for example, will help international students comes to terms with the intricacies of medical terminology in areas as diverse as history-taking, trauma care, and treatment procedures. In addition to a focus on industry-specific vocabulary, good programs should highlight commonly used grammatical structures used in the field of medicine and help candidates master the kind of medical idioms that are at the heart of doctor-to-doctor and doctor-to-patient interaction. Finally, with an eye on advancement, comprehensive may even provide modules that explain the inner workings of the U.S. healthcare system and contribute to the growth of medical writing skills. Upon completion of such a course, providers should feel comfortable working not just on tongue but in the English tongue. After all, as both working and aspiring medical professionals both know, no matter our mother tongue, all tongues themselves are the same and deserving of the same standard of care.
Related
- Adult high school diploma [link: “Adult high school diploma” → `adult-diploma.html`]
- Independent course studies [link: “Independent course studies” → `programs-independent-studies.html`]
- Business & medical English [link: “Business & medical English” → `professional.html`]
- Learning pods & fast track [link: “Learning pods & fast track” → `programs-learning-pods.html`]
- Document editing [link: “Document editing” → `services-document-editing.html`]
- Exam proctoring [link: “Exam proctoring” → `services-proctoring.html`]

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
**Anglia Mastery (C2)**
Carries UCAS tariff points for British universities – and taken right here in Agadir.
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

#### Section: Consultancy services and partner institutions
- **Q: Full text as published by AGI** — A: Empowering Your Global Academic Journey Navigating Your Future: From Admission to Achievement! What is AGI Education Consultancy? AGI Education Consultancy offers a comprehensive suite of personalized education consultancy and enrollment solutions for students and professionals. As an authorized admission agent representing a wide array of prestigious institutions, we streamline your application process for higher education, whether it’s locally, abroad, or online. Our services extend beyond administrative tasks; we provide holistic support tailored to your unique circumstances. From accommodation arrangements and visa applications to health insurance and family support for international students, we’ve got you covered. Additionally, AGI facilitates double diplomation programs, offers language training, assists with scholarships and financial aid applications, and provides career counseling and cultural orientation workshops. Our goal is to empower you to maximize your educational experience at every stage of your journey. Check our Network of Partners Why Choose AGI Education Consultancy? Tailored Guidance for Individual Success At AGI, we understand that every student has unique aspirations, strengths, and circumstances. Our personalized approach means we take the time to listen to your goals and craft a customized educational plan that aligns with your academic and career objectives. We study each case individually, collaborating with you to identify the best pathways for your success. Authorized Admission Agency As an authorized admission agency, AGI Education Consultancy is officially recognized to facilitate student placements in various educational institutions worldwide. Our status ensures that we are well-equipped to guide you through the entire admission process, providing you with the latest information and resources to make informed decisions about your education. Expertise of Our Professional Team Led by Julie Wilburn, our CEO who has lived in Morocco for many years and holds dual citizenship, AGI boasts an expert team with extensive experience in the education consultancy field. Julie has successfully guided hundreds of students in achieving their academic dreams. Her deep understanding of the local education system, combined with international insights, ensures you receive unparalleled support throughout your educational journey. Extensive University Network With established partnerships with numerous prestigious universities worldwide, AGI offers a diverse selection of programs across various fields of study. This extensive network allows you to choose an institution that best fits your academic interests, budget, and career aspirations, ensuring you receive a high-quality education. Comprehensive Application Support Navigating the application process can be overwhelming. AGI provides end-to-end assistance, from reviewing and refining your application materials to providing interview preparation and ensuring that your submissions meet all requirements. Our experienced consultants guide you through every step, maximizing your chances of acceptance. Expertise in Scholarships and Financial Aid Higher education can be financially challenging. AGI helps you identify scholarship opportunities, grants, and financial aid packages tailored to your profile. We assist in preparing applications and gathering necessary documentation, allowing you to secure funding and reduce financial burdens. Language Training and Preparation Proficiency in the required language is essential for success in an international academic environment. AGI provides specialized language training programs and resources for exams like IELTS, TOEFL, GMAT, and GRE. Our training ensures you are fully prepared to meet the language requirements of your chosen institution. Visa and Legal Assistance Understanding visa regulations can be daunting. AGI’s experienced consultants guide you through the visa application process, ensuring you have the correct documentation and understanding of legal requirements for studying abroad. Our support minimizes the complexities associated with obtaining a student visa. Accommodation Solutions AGI recognizes the importance of a safe and comfortable living environment during your studies. We assist in finding suitable accommodation options—whether on-campus or off-campus—tailored to your preferences and budget. Our goal is to ensure you feel at home in your new environment. Cultural Orientation Programs Transitioning to a new country can be challenging. AGI offers cultural orientation programs designed to familiarize you with the local customs, social norms, and academic expectations of your destination. These programs help ease your transition, enhancing your study experience and enabling you to adapt quickly. Career Counseling and Internship Opportunities Our commitment to your future extends beyond education. AGI provides career counseling services to help you align your academic pursuits with long-term career goals. We connect you with internship opportunities and job placement services, ensuring you gain relevant experience and professional connections in your field. 24/7 Support and Emergency Services Studying abroad can present unexpected challenges. AGI offers round-the-clock support to address your needs—whether it’s an urgent health issue, housing problem, or academic concern. Our local representatives are always available to provide assistance and guidance, ensuring your peace of mind. Ongoing Post-Study Support Your journey doesn’t end with graduation. AGI continues to support you after your studies, offering guidance on post-study work visas and connecting you with job opportunities in your field. We are dedicated to helping you successfully transition from academia to your professional career. Proven Track Record of Success AGI Education Consultancy has a strong history of successfully assisting students in achieving their academic goals. Our clients’ testimonials reflect our commitment to excellence and the impactful results of our services. We take pride in the positive experiences of our students and their successful transitions into the world of higher education. Community and Networking Opportunities Joining AGI means becoming part of a broader community of students, alumni, and professionals. Our networking events, workshops, and mentorship programs foster connections that can benefit you throughout your academic and professional journey. Holistic Approach to Education At AGI, we believe in nurturing the whole student. We focus not only on academic success but also on your personal development and well-being. Our holistic approach ensures that you are supported in all aspects of your educational journey. Ready to Take the Next Step in Your Educational Journey? we are here to guide you every step of the way. With our expert team, personalized approach, and comprehensive support services, we’ll ensure you make the most of your educational opportunities. Get started today American Group USA LLC and American Group International is proud to announce our official role as an English University agent for the following esteemed institutions: Explore Global Education Opportunities with Our University Partnerships Welcome to American Group USA LLC your gateway to world-class English education in Agadir, Morocco, and beyond. We proudly partner with universities across the United States, Europe, and Asia to offer students in Morocco and around the world an opportunity to pursue higher education with international standards and recognition. Whether you’re based in Agadir, elsewhere in Morocco, or anywhere in the world, our team is here to help you discover the best educational path. As an authorized agent and admissions counselling centre, we guide students in selecting the university that best matches their career goals, academic needs, and personal ambitions. Our mission is to make English education accessible to everyone. Through our partnerships, we offer a range of programs, from on-campus experiences to fully online degrees, allowing you to study from the comfort of your home. Our dedicated counsellors provide personalized support throughout the application process, helping you make informed decisions and ensuring a smooth journey into higher education. Join us in shaping your future with a globally recognized degree and access to a world of opportunities. Start Your Journey Today! Contact us to learn more about our university partnerships and how we can help you find the right fit for your academic dreams. Cardiff Metropolitan University Chichester College Group International SIST in Morocco International Institute of Engineering and Management Coventry University Brits Imperial University College Geneva Business School College de Paris We are excited to partner with these prestigious universities to help students access world-class education and opportunities for academic and professional growth. Through our partnerships, we provide guidance and support for students seeking to study at these institutions, ensuring a smooth admissions process and an enriching educational journey. Thank you for choosing American Group USA / American Group International as your trusted educational partner! Ms. Julie Wilburn Educational Consultant and CEO Network of Partners Our Prestigious Network of Partners At AGI Education Consultancy, we take pride in our extensive network of partnerships with leading universities and institutions around the globe. These trusted relationships allow us to offer our students access to a wide range of high-quality programs and study opportunities. From undergraduate degrees to postgraduate programs, our partner institutions are committed to academic excellence and provide the perfect environment for personal and professional growth. By partnering with these respected institutions, AGI ensures that you have access to the best educational pathways tailored to your unique aspirations. Explore the endless possibilities through our diverse partner network and take the next step in shaping your future! Royale Business College UK RB College, a prestigious UK institution, offers a variety of academic and vocational programs focused on student success and career readiness. As a trusted AGI Education Consultancy partner, RB College provides top-quality education and hands-on training, ensuring students achieve their academic and professional aspirations. See details Britts Imperial College University Britts Imperial University College is a dynamic academic center and an education partner of top British and European universities. Offering globally recognized Undergraduate, Postgraduate, and Doctorate degree programs, Britts Imperial empowers students from over 31 countries to achieve their academic and professional goals. With hybrid learning, campus transfer options, and post-study work opportunities, the university provides a globally accessible and practical education experience. UCAM Universidad Católica San Antonio de Murcia UCAM (Universidad Católica de Murcia) in Spain is offering a wide range of English-taught programs and promoting both academic excellence and values-based education. With a campus in the beautiful region of Murcia and over 340 international partnerships, including UC Berkeley and Stanford, UCAM provides students with a globally enriched learning experience. Its focus on combining theoretical and practical knowledge prepares students for success in both academic and professional spheres. Eucléa Business School Eucléa Business School, part of the Collège de Paris, specializes in commerce and management through work-study programs. With campuses in Strasbourg, Metz, Mulhouse, and Reims, Eucléa offers a comprehensive range of programs from Post-Bac to Bac+5. The school is committed to educational excellence, with recognized professional certifications from the RNCP. University of London The University of London is a globally recognized institution offering a wide range of flexible undergraduate and postgraduate programs. Known for its academic excellence, it provides both on-campus and distance learning opportunities to over 50,000 students worldwide. With a strong emphasis on accessibility, the university partners with leading institutions to deliver high-quality education across the globe. SIST British Education SIST (Superior Institute of Science and Technology) has been offering British education in Morocco for 20 years, providing undergraduate, master's, and MBA degrees in partnership with Cardiff Metropolitan University. As a unique higher education institution in Morocco that operates entirely in English, SIST students benefit from globally recognized degrees. The institute is also accredited by the Moroccan Ministry of Higher Education. Graduates from SIST stand out in the global business world, equipped with proficiency in three languages and high-level professional skills imparted by the rigorous British curriculum geneva business school Geneva Business School stands as a globally recognized Swiss institution, offering top-tier education with students from over 80 nationalities and partnerships across all continents. Through our four Educational Pillars, we aim to shape a sustainable society, ensuring quality through a rigorous Assurance Model. Ranked in the top 100 business schools worldwide, we continue to foster excellence and innovation. Coventry University Coventry University is a modern, global institution known for shaping future leaders and fostering innovation. With a Gold rating in the 2023 Teaching Excellence Framework (TEF), the university excels in teaching, learning, and student outcomes. Students benefit from immersive, real-life learning experiences, strong career support, and multiple entry dates throughout the year. Ranked as a top student city, Coventry provides a rich academic environment with guaranteed accommodation and a dedicated success coach for each student. College de Paris Founded in 2010, the Collège de Paris is a network of higher education institutions and training organizations focused on making academic excellence accessible. With an emphasis on international openness, personalized support, and pedagogical excellence, the network spans across France and internationally. The Digital Campus offers an online learning platform with the same rigor as physical schools, featuring digital modules, videos, and interactive content. Students benefit from personalized guidance and have access to masterclasses, graduation ceremonies, and more, ensuring a comprehensive educational experience. Nest Academy of Management Education Dubai Innovative Learning Hub: Nest Academy of Management Education Dubai offers cutting-edge programs designed to equip students with essential skills for today's dynamic job market. Career-Focused Approach: We emphasize practical training and real-world experiences, enabling students to seamlessly transition from education to successful careers. Empowering Future Leaders: Committed to fostering talent, we support students in turning their passions into professions through mentorship, scholarships, and industry connections. We are continuously expanding our network of academic partnerships, and while we’ve highlighted a few of our esteemed collaborators here, we are proud to work with dozens more institutions around the world. Stay tuned as we update our list to reflect the full range of universities and educational bodies that we collaborate with to provide the best opportunities for our students. back to AGI Education Consultancy schedule your free consultation RB College of the United Kingdom The UK degree is an internationally recognised and respected academic qualification and many of our graduates come from outside the European Union. Employers across the world recognise and value the quality of a UK university education, however, it is up to the student to ensure that their potential employers in their respective countries recognise the professional doctorate qualification. Students may need to obtain equivalence certification at their own expense in order for their degree to be recognised outside of the European Union. The UK’s higher education provision is among the best in the world and it’s universities consistently perform well in world rankings. As published in the Times Higher Education World Rankings 2018 with 3 UK universities in the top 10 across the world and a further 7 UK universities are in the top 50. We are thrilled to announce that RBC is UCAS registered, which means that all international students can apply to one of our courses via the largest UK admissions portal. UCAS, the Universities and Colleges Admissions Service, and the UK’s shared admissions service for higher education. UCAS supports 1.5 million students every year to explore entering higher education, employment and apprenticeships and manage almost three million applications, from around 700,000 people each year, for full-time undergraduate courses at over 380 universities and colleges across the UK. Together with RB College and American Group International we will offer these programs at our institution in Agadir, Morocco. RB College – Welcome (rb-college.co.uk)
Related
- Anglia & UCAS [link: “Anglia & UCAS” → `anglia-about.html`]
- Chichester College Group [link: “Chichester College Group” → `journal-ccgi-partnership.html`]

---

### 4.14 `admissions.html`

- **Browser title:** Admissions – American Group International, Agadir
- **Meta description:** How to join AGI in Agadir: visit, placement assessment, documents, enrollment. Registration days Aug 28 & 31, first day Sept 7; tuition 2,600 MAD a month.

Home / Parents / Admissions [link: “Home” → `index.html`] [link: “Parents” → `parents.html`]
**Page title (H1):** Admissions.
Tours are arranged individually – call or write for an appointment to meet us and see the school. Every new student sits placement assessments before admission, whatever system they arrive from, and registration for 2026–27 takes place on August 28 and 31.
→ **Apply online** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)

#### Section: The application journey
Four steps, with the office beside you at each one.
Step 01
**Enquire**
Call or email the admissions team to arrange a visit; tours are individual and include the school and the application process.
Step 02
**Visit & assess**
English/ESL proficiency and academic assessments, including the free Anglia placement test for language learners.
Step 03
**Apply**
Prior school records and a behavior report, age and residency verification, immunization and physical examination records.
Step 04
**Enroll**
Pay the annual inscription, confirm the monthly tuition plan, and order books from the beginning of August.

#### Section: Key dates 2026–27
Movable religious holidays – Eid al Mouloud, Ramadan, Eid al Fitr and Eid al Adha – are confirmed each term. Fall break runs October 12–18 and winter break December 18 – January 3.
→ **Full calendar** (`calendar.html`)
- **Registration days** — August 28 & 31
- **First day of classes** — September 7
- **Second semester begins** — January 5
- **Anglia examinations** — April
- **Last day & graduation** — June 17, 2027
Tuition & fees

#### Section: 2,600 MAD a month, paid over ten months.
Plus one annual inscription at enrollment: 6,500 MAD for kindergarten–grade 1, rising to 11,000 MAD for grade 12. Books, mathematics and Anglia English examinations, dual enrollment in the USA and Morocco, and student insurance are included. The inscription is non-refundable; fees are not negotiable.
→ **Tuition & fees in full** (`fees.html`)
→ **Request the tuition guide** (`forms.html#enquiry/programs`)

#### Section: What to bring
A child aged 5 by September 1 and under 21 on the first day of school is eligible. AGI admits students of any race, religion, color, national or ethnic origin.
- **Age** — Birth certificate, hospital or physician certificate, passport or visa, or birth registration.
- **Residency** — Lease or mortgage statement, utility bill, tax statement or deed, or a job contract – dated within three months.
- **Health** — Immunization certification and a physical examination record.
- **Academic** — Records from the previous school (or its address), plus a behavior report. IEP or special-needs provision requires practitioner documentation.

#### Section: In AGI’s own words
The steps above summarize the procedure. Here is the full text, and the full list of enrollment documents.
- **Q: The admissions procedure in full** — A: Welcome to American Group International of Agadir We are thrilled that you are considering our school as a potential educational home for your child, and we are excited to embark on this journey together. We are delighted to extend a warm welcome to you and your family and to invite you to our small school located in Agadir city limits. We invite prospective parents, guardians, and applicants to visit our school. Our tours are scheduled on an individual basis and include information about the school and the application process. We strongly encourage all prospective parents to call us for an appointment to meet with us and tour the school. Should you have any questions or require any assistance, please do not hesitate to contact our admissions team at americanecoleagadir@gmail.com. We are here to support you every step of the way. We look forward to meeting you and your family and making our school family, your school family. Sincerely, American Group International The procedure for admission consists of the following: Application for Admission You are required to fill out an application form and submit it along with a deposit of Enrollment fees that are non-refundable to the Institution or Academy. Fees vary depending on program and grade level. Please talk to Administration regarding this. Upon receipt, we will acknowledge your application, and you will be advised about an interview date when we can meet with you and your child/children. Interview with Parent and Child All prospective parents are required to come for an interview, accompanied by the child. We will set a date and time that is convenient for both parties. At the time of the interview, please feel free to ask any questions you may have concerning our programs. Offer of Admission Following the interview, the Institution will offer your child/children admission. We will ask you to submit the following: Tuition Agreement-email for updates or visit to the school. Photocopy of birth certificate Three recent photographs Fee payment and schedule signed and agreed with the first payment. Past educational papers which should include 2 years, and attached a behaviour report and any information on IEPs or regards to other SEN needs in children. All files must have a complete file and email, phone, address and information and fees paid in full, or the child cannot enter the classroom. Papers of transfer from other schools must be given and all of them must be translated in English! All returning students must pay for their books between June 15th and August 1st to have them the first day of school. The admission process will be considered complete at this stage. You than will be asked to sign the contract of enrolment. Thank you, Julie Wilburn, Director Americanecoleagadir@gmail.com Please copy these forms and fill them out and return to us in a PDF format with all the documents below. The application form is now online: apply on the forms page.
- **Q: Enrollment documents in full** — A: Verification of Age A child age 5, Grade K, by September 1 and under age 21 on the first day of school is eligible for enrollment. Acceptable age verification includes: • Birth certificate • Hospital certificate • Physician certificate • Passport/Visa • Birth registration Acceptable residency verification includes: Lease or mortgage bill/statement Utility bill (water/sewer/gas/electric/oil) Real estate tax bill/statement/Deed Job Contract Current within 3 months of enrollment; must include name, address, and date; to be provided for each change of address. • Immunization Certification Physical Examination Record Students’ records from past school must be given or the address of the school to obtain records! For further information AGI admits students of any race, religion, color, national or ethnic origin to all of the rights, privileges, programs, and activities generally accorded or made available to the students of AGI. It does not discriminate on the basis of race, religion, color, or national or ethnic origin in the administration of its educational policies, admissions policies, or other school-administered programs.
Before you enroll
- Tuition & fees [link: “Tuition & fees” → `fees.html`]
- Calendar 2026–27 [link: “Calendar 2026–27” → `calendar.html`]
- Family policies [link: “Family policies” → `policies.html`]
- Placement policy [link: “Placement policy” → `placement-policy.html`]
- Questions & answers [link: “Questions & answers” → `faq.html`]

#### Section: Ready to apply?
Apply online in about five minutes, or book a visit first.
→ **Apply** (`forms.html#enrollment`)
→ **Book a visit** (`forms.html#visit`)

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

#### Section: Read the full texts
Every policy as published by AGI.
- Link card → `handbook.html`: Academic handbook
- Link card → `attendance.html`: Attendance
- Link card → `promotion-retention.html`: Promotion & retention
- Link card → `placement-policy.html`: Provisional placement & assessment
- Link card → `parent-responsibility.html`: Parent responsibility
- Link card → `refunds-complaints.html`: Refunds & complaints
- Link card → `media-policy.html`: Media
- Link card → `homework.html`: Homework
- Link card → `volunteer-hours.html`: Volunteer hours
- Link card → `supplies.html`: School supplies list

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

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
- **Meta description:** News from American Group International and Anglia Morocco: 66 posts on graduations, partnerships, Anglia exams, events and school life.

Home / Journal [link: “Home” → `index.html`]
**Page title (H1):** Journal.
News from AGI and Anglia Morocco since 2017: graduations, partnerships, exams, events and school life. Posts older than a year are archived – fees and dates in them may have changed.

#### Section: Archive
All 60 posts, grouped by year (newest first). Each row: date, category (Partnership, Achievement, Admissions, Programs, News), title, link to the article page. Full list in Appendix B.

---

### 4.18 `journal-ccgi-partnership.html`

- **Browser title:** American Group International and Anglia Morocco Join Forces – AGI Journal
- **Meta description:** AGI and Anglia Morocco join Chichester College Group International to empower global learners.

Home / Journal / Partnership [link: “Home” → `index.html`] [link: “Journal” → `journal.html`]
**Page title (H1):** American Group International and Anglia Morocco Join Forces with Chichester College Group International (CCGi) to Empower Global Learners
Partnership

#### Section: Chichester College Group International

#### Section: (CCGi) – Overview

#### Section: A Leader in International Education
CCGi is the international arm of Chichester College Group (CCG), which has been rated ‘Outstanding’ by Ofsted, the UK’s education standards authority.
The group comprises seven colleges across ten campuses across West Sussex and Brighton & Hove.
Mission & Reputation

#### Section: CCGi’s mission: “Changing lives through learning.”.
Recognized for academic excellence and comprehensive student support—especially for international learners.

#### Section: Key Programs Offered
English Language Courses: General English (15 & 21), delivered via the British Council-accredited Chichester English Language School, ranked among the top 5% in the UK.
A-Levels & AS-Levels: Two-year A-Levels at Chichester and Worthing; one-year AS-Levels at Worthing.
Vocational Courses & BTECs: Practical, skills-focused courses in areas like hospitality, engineering, health & social care, creative arts.
University Foundation Programs: Pathways ensuring progression to UK or international universities.
Higher Education Degrees: Undergraduate degrees (HNC, HND, level 4–6) in fields like business, engineering, art, media, motorsport, animal management, music, sports, teaching—accredited by institutions such as University of the Arts London (UAL) and University of Brighton.
Study Abroad, Winter/Summer Schools: Short-term immersive experiences combining academics with British cultural activities.

#### Section: Student Support & Unique Experience
Comprehensive services: Visa guidance, accommodation assistance (homestays, halls), welfare, enrichment and social activities.
Highly equipped campuses: State-of-the-art facilities including farms, animal care centres, equine training, workshops, labs, and creative arts studios.
Cultural immersion: Organized trips to iconic UK sites like London, Oxford, Stonehenge, fostering personal growth and global citizenship.
Global student body: Enrols students from regions including East Asia, Europe, and beyond.

#### Section: Strategic Partnerships & Agents Network
CCGi maintains partnerships with academic institutions, awarding bodies, and global agents who represent them locally to prospective students.
Strategic collaborations include organisations like NOCN, supporting qualification accreditation.

#### Section: Spotlight on CCGi Colleges
1. Chichester College
Main campus in Chichester, plus Brinsbury (agricultural campus with a working farm and animal care facilities).
Offers A-Levels, BTECs, vocational programs, and some university-level courses.
2. Northbrook College
Based in Worthing with campuses in West Durrington and Shoreham-by-Sea (campus sale planned in 2025).
Strong in creative and cultural higher education: fashion, photography, media (validated by UAL), plus motorsport engineering (via University of Brighton).
3. Worthing College
Sixth-form college in Worthing offering A-Levels & AS-Levels; also, part of CCG’s broader vocational and international portfolio.
4. Brighton MET College
Former Brighton MET (merged August 2021); campuses in central and east Brighton.
Offers trades, technical subjects, adult education, and visual arts progression.
5. Crawley College and Haywards Heath College
Additional FE/Higher Education providers under the CCG umbrella—extending geographic range and offerings.
6. Brinsbury
Specialized land-based and agricultural centre; integral to Chichester College’s offerings.
American Group International is a proud partner of CCGi and we will be working on projects and educational programs to help the local Moroccan community.
→ **Partnerships & franchise** (`partnerships.html`)
·
→ **All journal entries** (`journal.html`)

#### Section: Partner with AGI.
Franchise and partnership enquiries are handled from the Agadir headquarters.
→ **Partnership enquiry** (`forms.html#enquiry/partnership`)

---

### 4.19 `partnerships.html`

- **Browser title:** Partnerships & franchise – American Group International, Agadir
- **Meta description:** Partner with AGI and Anglia Morocco: Anglia center franchise in Morocco's twelve regions, institutional partnerships, university pathways and our partner network.

Home / Anglia Morocco / Partnerships & franchise [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Bring the AGI standard to your region.
AGI holds the Anglia Examinations franchise for Morocco and operates from Agadir across the Kingdom's twelve regions. We work with schools, language centers, freelance teachers and international institutions – and franchise opportunities are open for the right candidates.
→ **Partnership enquiry** (`forms.html#enquiry/partnership`)
→ **Network & centres** (`anglia-network.html`)

#### Section: Two ways to build with AGI
_Model I_
**Franchise**
An Anglia Morocco center under your ownership, anywhere in the Kingdom's twelve regions. You get the examinations license, the placement and testing system, training, and the AGI standard behind it. Enquiries run through the Agadir headquarters.
- Anglia examinations license & materials
- Teacher training and C.I.T.E. certification
- Placement testing & level mapping to the CEFR
- Territory agreement within the 12 regions
_Model II_
**Institutional partnership**
For existing schools, language institutes and colleges: Anglia examination provision inside your campus, university pathway agreements, and co-designed English or academic programs under a shared quality framework.
- Co-designed English & academic programs
- University pathway agreements (UK, USA, India)
- Anglia testing center inside your campus
- Shared quality framework & annual review

#### Section: The network today
Anglia Morocco is managed from the Agadir headquarters, with Anglia centers across the north and center of the Kingdom. Remaining regions are open for franchise.
→ **Regions, provinces and open positions** (`anglia-network.html`)
- **Souss-Massa** — Headquarters · Agadir
- **Casablanca-Settat** — Anglia centers
- **Tanger-Tetouan-Al Hoceima** — Anglia centers
- **Rabat-Salé-Kénitra** — Anglia centers
- **Fès-Meknès · Marrakech-Safi** — Anglia centers
- **Oriental · Béni Mellal-Khénifra** — Open for franchise
- **Drâa-Tafilalet · Southern Provinces** — Open for franchise

#### Section: Who we work with
Examination boards, colleges, placement partners and professional bodies.
- Link card → `journal-ccgi-partnership.html`: United Kingdom · Chichester College Group International · The international arm of a seven-college group in the south of England – Chichester, Crawley, Worthing, Brinsbury, Brighton MET, Northbrook and Haywards Heath. Signed 2025.
- Link card → `teachers.html`: Teacher training · Bridge Education Group · A global leader in teacher training and TEFL/TESOL certification. Partnership announced November 2025, opening professional development to educators across Morocco.
- Link card → `pathways.html`: University placement · Leverage Edu · Official regional representation for Souss and southern Morocco since March 2026 – private and public university placement with housing assistance.
- Link card → `fees.html#high-school`: Plantation, Florida · American High School · Cognia-accredited online diploma program and a Yass Prize awardee. Partnership announced 2025; the diploma is accepted in the U.S. and internationally.
- Link card → `pathways.html`: United Kingdom · RB College · UCAS-registered UK institution offering academic and vocational programs, including work-based Master of Business Administration routes.
- Link card → `anglia-about.html`: Chichester, since 1993 · Anglia Examinations England · AGI has been the Anglia franchise holder for Morocco since 2021 and has used the Anglia system in its language programs since 2013.
- Link card → `programs-learning-pods.html`: For teacherpreneurs · AGI Learning Pods · Small-group programs run by freelance teachers and parent groups under the Anglia system – inclusive, creative and affordable.
- Link card → `about.html#accreditation`: Membership · American School Counselor Association · AGI joined the ASCA network in 2026, bringing U.S. school-counseling standards to student guidance.

#### Section: Partner with AGI and Anglia Morocco
- **Q: Full text as published by AGI** — A: Employment Opportunities at American Group International. Anglia Examinations Partnership. Anglia Morocco Learning Pods Program. Other Partnership ideas apply to the email. Check out our form below and register your details for the one that best fits your skills, experience, and interests. We are always open to talent that would like to join American Group International or Anglia Morocco. By joining our community by sending a direct application. We will reach-out when we have an available role that matches your experience. We also have Franchise opportunities available in the English market for the right candidates. Once again thank you for choosing us for your educational needs! Join Anglia Morocco Learning Pods! American Group International School <americanecoleagadir@gmail.com> Looking for passionate educators with Entrepreneur abilities. We partner with schools, language institutes, Teacherpreneurs, and associations. We are looking for people who want to expand the educational opportunities in Morocco. We do teacher training for schools and look for opportunities to equip teachers. Are you passionate about teaching and ready to embark on an exciting journey across Morocco? Want to be your own entrepreneur? Anglia Morocco Learning Pods is seeking dedicated educators and qualified staff to join our innovative remote teaching initiative. Why Join Us? – Remote Opportunities: Teach from the comfort of your home, reaching students all across Morocco. – Flexible Schedule: Enjoy the freedom to choose your hours and maintain a healthy work-life balance. – Supportive Environment: Join a dynamic team committed to educational excellence and personalized learning. – Professional Growth: Access ongoing training and development opportunities to enhance your skills. Positions Available: – Teachers: Experienced in a variety of subjects for primary and secondary levels. – Educational Assistants: Support our teachers in delivering engaging lessons and fostering a positive learning environment. – Administrative Staff: Help coordinate and manage our remote learning operations efficiently. Requirements: – Bachelor’s degree in education or relevant field (for teaching positions) and TESOL from an English Country that can be verified. We do not accept TESOL unless verifiable from an English-speaking country. – Strong communication skills and a passion for education. – Reliable internet connection and comfortable working remotely. How to Apply: Interested candidates can send their resume and cover letter to americanecoleagadir@gmail.com or visit our website for more information. Join us at Anglia Morocco Learning Pods and be part of transforming education in Morocco through remote learning excellence! All Teachers and staff must provide proof of background check from their countries and certified diplomas with legalization. Diplomas that are not legalized are just a piece of paper that cannot be approved. Employee Application AGI Agadir This form may be reproduced in quantities sufficient to accommodate your requirement. Tell Us About Yourself The following information is for identification purposes only. You are not required to complete information that you feel violates your privacy. The application form is now online: apply on the forms page. SOCIAL SECURITY NUMBER/ Or Tell Us About Your Teaching Experience Tell Us About Your Academic/Training Experience Tell Us About Your Character Professional References School Employer Nomination/Sponsorship (To be completed by supervisor/employer/professional associate) This is to certify that: I, as a professional in the education industry, have known/supervised/employed the applicant for a sufficient period to verify that she/he is of sound moral character ad would without reservation nominate her/him to be considered for private school professional teacher. Subject Area(S) In Which Applicant Seeks. (Choose up to three) Provide the requested information and return the completed Application. This Application is the truth to the best of my knowledge. Please send correspondence to: Email: americanecoleagadir@gmail.com Please we do appreciate your business but we ask not to contact the us on Sunday, as there will be no one available to receive your call. We also ask that if you are interested in a job, please email us as we will ask for your information to be registered by email. Thank you.
Anglia Morocco
- Anglia Morocco [link: “Anglia Morocco” → `anglia.html`]
- Network & centres [link: “Network & centres” → `anglia-network.html`]
- Partners & investors [link: “Partners & investors” → `investors.html`]

#### Section: Start the conversation.
Franchise and partnership enquiries are handled from the Agadir headquarters. Tell us the region, the model and your teaching or business background.
→ **Partnership enquiry** (`forms.html#enquiry/partnership`)
→ **Contact** (`contact.html`)

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

#### Section: Come and meet us.
The best way to know AGI is to visit during the school day.
→ **Book a visit** (`forms.html#visit`)
→ **Contact** (`contact.html`)

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

### 4.25 `agi-usa.html`

- **Browser title:** American Group USA LLC – American Group International, Agadir
- **Meta description:** American Group USA LLC: AGI's U.S. company for online programs, tutoring and coaching.

Home / Programs / AGI USA [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** American Group USA LLC
AGI's U.S.-registered company, offering programs, tutoring and coaching to clients worldwide.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
[TO CONFIRM: Registered address in Grantsville, Maryland – to be confirmed.]

#### Section: In detail
Ladies and Gentlemen,
It is with great pleasure and excitement that we announce the upcoming opening of the extension branch of American Group USA, LLC. This significant expansion marks a new chapter in our journey of growth and service excellence.
At American Group, USA, we have always been committed to delivering unparalleled educational services, driving innovation in our industry, with trustability and honour. Opening this new branch is a testament to our dedication to expanding our reach and enhancing our ability to serve our clients and partners.
We are confident that this extension branch will not only strengthen our presence in the United States, but also allow us to better meet the evolving needs of our customers across global sectors that we now have a base with.
We look forward to sharing more details with you in the coming months as we prepare for the official opening. Thank you for your continued support and trust in American Group USA, LLC.
CEO
Julie Wilburn
W25317017- Maryland LLC
Online Teacher Information Form
Online Teacher Registration Form
Personal Information:
The application form is now online: apply on the forms page. [link: “apply on the forms page” → `forms.html#enrollment`]
Documents Required:
- Passport Copy or State Issued Picture ID:
– ID/ Passport Copy (PDF):
- Degree Information:
– Degree Type: (e.g., Bachelor’s, Master’s, Ph.D.)
– Degree:(e.g., B.A. in English, M.Sc. in Mathematics)
– Discipline of the Degree:(e.g., Education, Science, Arts)
– Upload Degree Certificate (PDF):
- Subjects You Are Familiar with Teaching: (e.g., English, Mathematics, Science)
Submission Instructions:
– Please ensure all documents are in PDF format.
Thank you for your interest!
American Group International Team
Online
- Online tutoring [link: “Online tutoring” → `online-tutoring.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.26 `anglia-about.html`

- **Browser title:** About Anglia Examinations – Anglia Morocco | AGI Agadir
- **Meta description:** About Anglia Examinations: Chichester since 1993, Chichester College Group, AIM and Ofqual, Anglia Morocco since 2021.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / About Anglia [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** About Anglia Examinations
Anglia Examinations has tested English since 1993 from Chichester, England. AGI has been the franchise holder for Morocco since 2021.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Exam dates** (`calendar.html#anglia-exams`)
Anglia Examinations is a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding. The four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual.

#### Section: Regulated by Ofqual
AIM Qualifications and Assessment Group (AIM Qualifications) is an awarding organization in the UK that offers a wide range of qualifications and assessments. They are recognized for providing innovative and flexible qualifications across various sectors, including vocational qualifications, end-point assessments, and bespoke qualifications for employers.
AIM Qualifications and Their Role:
- Qualifications Offered:
– AIM Qualifications provides qualifications in multiple areas such as business, health and social care, sport, and more.
– They offer qualifications from entry-level to higher levels, catering to a diverse range of learners.
- Assessment Approach:
– AIM Qualifications emphasizes flexibility and innovation in their assessment methods, ensuring they meet the needs of learners and employers.
Affiliation with Anglia Examinations England:
- Partnership:
– AIM Qualifications collaborates with Anglia Examinations England, which is known for its English language assessments. This partnership allows both organizations to leverage their expertise and resources to offer comprehensive educational solutions.
- English Language Qualifications:
– Through this affiliation, AIM Qualifications supports the delivery and recognition of Anglia’s English language qualifications, ensuring they meet high standards and are widely recognized.
UK Recognition and Support:
- Regulatory Approval:
– AIM Qualifications is regulated by Ofqual (Office of Qualifications and Examinations Regulation), which is the regulatory body for qualifications, exams, and assessments in England. This ensures that their qualifications meet national standards for quality and rigor.
- Recognition by Educational Institutions and Employers:
– Qualifications awarded by AIM are recognized by educational institutions and employers across the UK, providing learners with valuable credentials that can support their educational and career advancement.
- Support from UK Education System:
– The recognition and regulation by Ofqual signify that AIM Qualifications are supported by the UK education system. This support is crucial for maintaining the credibility and acceptance of the qualifications both nationally and internationally.
Conclusion:
AIM Qualifications Group plays a significant role in the UK education sector by offering a variety of qualifications and assessments. Their affiliation with Anglia Examinations England enhances the reach and recognition of English language qualifications. The regulatory oversight by Ofqual ensures that their qualifications are held to high standards, thereby receiving support and recognition from educational institutions and employers within the UK.

#### Section: The Office of Qualifications & Examinations Regulation (Ofqual)
Ofqual regulate qualifications, examinations and assessments in England. Ofqual are independent of government and report directly to Parliament. Ofqual’s responsibilities are to provide confidence in the qualifications they regulate and indicate the knowledge, skills and understanding students have demonstrated.
Ofqual maintain standards and provide confidence in the rigour of qualifications in England including GCSEs, A levels, AS levels and vocational and technical qualifications, including AIM Qualifications and Assessment Group.
Anglia Examinations top four levels of English language exams are regulated by Ofqual via our partnership with AIM Qualifications and Assessment Group.
When you see the Ofqual logo endorsing a qualification you can be confident that:
- The exams are regulated qualifications
- The exams show the actual level of competency a student has achieved
- Employers and academic institutions have confidence in the exams.
Thank you for your interest in Anglia Examinations and we hope to be of service to your educational journey.
Thank you very much,
Julie A. Wilburn
CEO & Educational Director, Anglia Examinations Morocco

#### Section: The History Of Anglia In Morocco
The history of AngliaMorocco started in 2010 by Suzanne Linsen. She moved to Morocco to introduce Anglia Examinations and its wide range of English language certificates to schools and institutes. Prior to that she was selected to conduct English courses and administer Anglia exams at a language institute in Tangier.
During this year 2021, American Group International (AGI) became the Anglia franchise holder for Morocco. AGI has been an educational brand since 2012. AGI has placed hundreds of students into the American Educational System with low cost, affordable, educational programs including an American School in Agadir. They have used the Anglia system in their language programs since 2013. Julie Wilburn is the CEO and lived in Morocco for many years and also holds dual citizenship in the country.
The AGI team has now embarked on the next level in its offerings to give opportunities to thousands of people to master the international language of English in business and communication with top English training and assessments.
We strive to give back to the Moroccan community and reach the areas that desire to take international exams. AGI wants local teams based in each of the 12 regions of the country to execute local community based programs to reach the unreachable. The main headquarters are located in the cozy city of Agadir and it is centralized to the applying of the AGI mission and educating the community in English throughout the Kingdom of Morocco. AGIs number of local franchise distribution networks will hopefully grow rapidly in the next few years; as English is quickly becoming a new love for the Moroccan young people. This in return will hopefully open up new avenues for many including new international opportunities to people inside as well as international levels from the outside.
AngliaMorocco along with AGI will work closely with; multiple’ education centers, schools and businesses to develop new strategies to help all levels of schools and learners to achieve a higher standard of English. Addressing the challenges due to the COVID pandemic, AGI is offering online platforms and examinations, AGI and AngliaMaroc communities, and events to enhance greater opportunities in Moroccan communities. With AGIs mission “Global Minds with a Global Prospective”, we strive to offer a better opportunity for the Moroccan community to ‘Dare to Dream in English’ with the Step-by-Step approach. AngliaMaroc is offering Anglia English exams from Beginners to Mastery level (CEFR C2) through the European Framework.
Anglia Morocco
- Anglia Morocco [link: “Anglia Morocco” → `anglia.html`]
- Exams & levels [link: “Exams & levels” → `anglia-exams.html`]
- Exam dates 2026 [link: “Exam dates 2026” → `calendar.html#anglia-exams`]
- CEFR levels [link: “CEFR levels” → `anglia-cefr.html`]
- Practice papers & audio [link: “Practice papers & audio” → `anglia-practice.html`]
- Step To books [link: “Step To books” → `anglia-books.html`]
- Special arrangements [link: “Special arrangements” → `anglia-special-arrangements.html`]
- Free placement assessment [link: “Free placement assessment” → `anglia-placement-test.html`]
- Classes & prices [link: “Classes & prices” → `anglia-classes.html`]
- Network & centres [link: “Network & centres” → `anglia-network.html`]
- Become a centre [link: “Become a centre” → `partnerships.html`]
- Anglia FAQ [link: “Anglia FAQ” → `anglia-faq.html`]
- C.I.T.E. for teachers [link: “C.I.T.E. for teachers” → `teachers.html#cite`]
Anglia Morocco headquarters: AGI, Agadir · j.wilburn@angliamorocco.org · a.lam@angliamorocco.org

---

### 4.27 `anglia-books.html`

- **Browser title:** Step To books – Anglia Morocco | AGI Agadir
- **Meta description:** Anglia Step To books: ten workbooks from First Step to Masters (C2), with audio files, guided test practice and a sample exam. Order through Anglia Morocco in Agadir.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Step To books [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Step To books.
Specifically designed for students preparing for Anglia examinations from First Step to Masters (C2): 10–12 topic-based units, a QR code linking to audio files and a sample test, 110–128 full-colour pages.
→ **Order books** (`forms.html#books`)
→ **Audio files** (`#audio`)

#### Section: The Step To series
Ten books set against the CEFR, from beginner to Masters.
First Step
Junior
Primary
Preliminary
Elementary
Pre-Intermediate
Intermediate B1 · Ofqual*
Advanced B2 · Ofqual*
Proficiency C1 · Ofqual*
Masters C2 · Ofqual*
* Ofqual accredited through AIM Qualifications.

#### Section: The Step To approach
A step-by-step approach to testing that encourages and motivates students to make clear and effective progress. Each book is researched and developed by professional ESOL experts.
- **Workbook** — A Step To workbook with 10–12 topic-based units, covering high-frequency test topics and vocabulary
- **Test practice** — Guided practice for every test section – listening, reading, writing and speaking
- **Audio** — Audio files, reached with the QR code in the book
- **Sample paper** — A sample exam paper
- **Qualification** — The opportunity to gain an Anglia ESOL international qualification

#### Section: Teachers' guide
The accompanying teachers' guides make things easy: each is a comprehensive one-stop solution for test preparation, with instructions, language and cultural explanations, test tips and transcripts of all the recordings.

#### Section: Audio files
Free downloads for the Step To books.
**First Step – Pre-Intermediate**
Download audio [link: “Download audio” → `https://www.anglia.nl/uploads/1/2/0/0/120044573/audiofiles_step_to_fs_-_pre-intermediate__1_.zip`]
**Intermediate – Masters**
Download audio [link: “Download audio” → `https://www.anglia.nl/uploads/1/2/0/0/120044573/audoifiles_step_to_intermediate_-_masters__1_.zip`]

#### Section: Order your Step To books.
Order through Anglia Morocco in Agadir – the office confirms availability, price and delivery.
→ **Order books** (`forms.html#books`)
→ **Practice papers** (`anglia-practice.html`)

---

### 4.28 `anglia-cefr.html`

- **Browser title:** CEFR levels – Anglia Morocco | AGI Agadir
- **Meta description:** The CEFR levels A1 to C2 explained, and benchmarks for native speakers and language learners at AGI.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / CEFR levels [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** CEFR levels
How the Common European Framework of Reference describes language ability – and how AGI students progress through it.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Exam dates** (`calendar.html#anglia-exams`)
→ **English benchmarks at AGI by grade** (`english-anglia.html#cefr`)

#### Section: The CEFR explained
K–12 English CEFR Benchmark for Natives and Language Learners at AGI
Kindergarten
5–6
Pre-A1 / A1
Understand simple classroom instructions, basic vocabulary
Grade 1
6–7
A1
Speak in simple sentences, recognize common words
Grade 2
7–8
A1–A2
Read short stories, write simple sentences
Grade 3
8–9
A2
Understand lessons, write short paragraphs
Grade 4
9–10
Explain ideas and follow classroom discussions
Grade 5
10–11
B1 (Target)
Read chapter books, write organized paragraphs
Grade 6
11–12
B1
Participate in discussions, write short essays
Grade 7
12–13
Understand academic vocabulary and lectures
Grade 8
13–14
B2 (Target)
Write essays, analyse texts, present ideas
Grade 9
14–15
B2
Handle academic reading and structured writing
Grade 10
15–16
Research, debate topics, interpret literature
Grade 11
16–17
B2–C1
Write research papers, complex presentations
Grade 12
17–18
C1 (Ideal Graduation Level)
University-level reading and academic writing
Important Notes for Second-Language Learners
If students do not speak English at home, they may be:
½ to 1 CEFR level lower in early grades
but they usually catch up by middle school if immersion is consistent.
Example:
- Native English CEFR
- ESL Student Typical
- A2+ / B1
- B1+ / B2
- C1
- B2 / C1-C2
Common Benchmarks Used by International Schools.
Many American international schools use these targets:
Elementary graduation (Grade 5): B1
Middle school graduation (Grade 8): B2
High school graduation (Grade 12): B2–C1-C2
These levels match expectations for:
University preparation for SAT.
International exams
Academic writing ability and English Mathematics
Connection to International Exams
These CEFR levels align approximately with well-known exams:

#### Section: - Cefr
- Example Exams
- Beginner English tests
- Elementary English certification
- Intermediate academic English
Upper-intermediate / university readiness
C1-C2
Advanced academic English
The realistic policy for natives is:
Grade 5: Minimum B1
Grade 8: Minimum B2
Grade 12: Minimum B2 (C1 preferred)
Students that do not hit these benchmarks are considered language learners and that means they could need assistance or extra lessons or accommodations to get to the levels that would make them university ready. We use the Anglia Examinations England assessments as a high-quality standard, and it allows students to success with the proven 10 Step To program. www.angliamorocco.org
www.anglia.org
CEFR level tests for English Language Exams
We explain CEFR, what it is and how Anglia Exams relate to the Common European Framework of Reference for Languages.

#### Section: What is the Common European Framework of Reference for Languages?
The CEFR is a framework developed by the Council of Europe to measure and describe your level of proficiency for European language ability. It is especially useful if you are a non native speaker. It gives an idea of how good your language skills are and privides a guide for which levels to take English language exams at. There are a few types of framework for measuring language so it can get a bit confusing!
The Common European Framework of Reference for Languages is an international standard for establishing your language ability. You will often hear people say things like “My English language ability is at level B1 “. A school, university or college will often set a minimum CEFR level as part of their admission requirements.
The CEFR is a scale created in Europe and can be applied to any European language including English. It is growing in popularity and is used more and more worldwide as a standard for language ability. The CEFR was not made for a particular language test and so here at Anglia Exams we (like other language testing institutions), have mapped our exams to matching CEFR test levels so that you can easily understand the level of any Anglia Exam.
**Understanding CEFR Test Levels**
Read on if you want to understand how Anglia exam English levels relate to the Common European Framework Reference for Languages (CEFR).
Most non-native English language speakers will aspire to achieve English language ability at levels A1, A2, B1, B2, C1 abd C2. C2 is the higest level. That doesn’t mean you have to start at these higher English language levels though. No matter your English level or language ability, Anglia exams provide an easy Step by Step approach to mastering the English language- helping you to progress though the CEFR levels at a pace that works best for you.
Whether you are intent on progressing to university, securing employment or for personal interest- having a an Ofqual approved Anglia Exam (our four highest levels B1-C2 are Ofqual approved), is a reliable way of proving your English language ability.
**A Summary of CEFR Levels**
- English level A1 is the first level on the CEFR and is defined as “beginner”
- English level A2 is the second level of CEFR. Students at this level have learnt the basics of English can communicate simple, basic needs.
- English level B1 is the third level of CEFR and describes an “intermediate” of English ability.
- English level B2 is the fourth level in the CEFR and describes someone who is confident in everyday English speech.
- English level C1 is the fifth level in the CEFR. English speakers at this level are advanced and can function independently with precision on a wide variety of subjects and in most settings. C1 Level is suitable for most academic studies.
- English level C2 is the sixth and highest level of the CEFR. English learners C2 proficiency level are bilingual. A native English speaker with a good education is technically at a C2 level.
We help measure and test English language proficiency by working with English as a foreign language schools. We help students to progress from the very first steps of acquiring English language ability, on to levels A1 and up through the levels to CEFR level C2.
The following graphic gives an idea of how Anglia Examination levels relate to the CEFR levels. This does not mean that there is an exact equivalence between the exam levels displayed.
Anglia Morocco
- Anglia Morocco [link: “Anglia Morocco” → `anglia.html`]
- Exams & levels [link: “Exams & levels” → `anglia-exams.html`]
- Exam dates 2026 [link: “Exam dates 2026” → `calendar.html#anglia-exams`]
- Practice papers & audio [link: “Practice papers & audio” → `anglia-practice.html`]
- Step To books [link: “Step To books” → `anglia-books.html`]
- Special arrangements [link: “Special arrangements” → `anglia-special-arrangements.html`]
- Free placement assessment [link: “Free placement assessment” → `anglia-placement-test.html`]
- Classes & prices [link: “Classes & prices” → `anglia-classes.html`]
- Network & centres [link: “Network & centres” → `anglia-network.html`]
- Become a centre [link: “Become a centre” → `partnerships.html`]
- Anglia FAQ [link: “Anglia FAQ” → `anglia-faq.html`]
- About Anglia Examinations [link: “About Anglia Examinations” → `anglia-about.html`]
- C.I.T.E. for teachers [link: “C.I.T.E. for teachers” → `teachers.html#cite`]
Anglia Morocco headquarters: AGI, Agadir · j.wilburn@angliamorocco.org · a.lam@angliamorocco.org

---

### 4.29 `anglia-classes.html`

- **Browser title:** English classes & prices – Anglia Morocco | AGI Agadir
- **Meta description:** English classes at Anglia Morocco, Agadir: Saturday classes 500 MAD a month, one-to-one 200 MAD, small groups 150 MAD, 12-week course 1,200 MAD. Free level test.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Classes & prices [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** English classes, at every age.
Start with a free level test, then choose the format that suits you – from Saturday classes for children and teens to one-to-one lessons for professionals.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
_Saturday classes_
500 MAD
a month
- Ages 5–18
- Saturdays 2:00–4:00 p.m., October–June
- Yearly Anglia exam included
- BAC, TOEFL, IELTS, SAT and Mathematics-in-English preparation
→ **Ask about this class** (`forms.html#enquiry/anglia`)
_One-to-one_
200 MAD
a session
- English or mathematics
- Full access to the teacher
- Times that fit a working week
- Ideal for job-related English
→ **Ask about this class** (`forms.html#enquiry/anglia`)
_Small group_
150 MAD
per person, per session
- 2–3 students
- Friends, siblings or colleagues
- Same level, shared goals
→ **Ask about this class** (`forms.html#enquiry/anglia`)
_12-week course_
1,200 MAD
100 MAD a week
- 4–10 students
- A structured course over 12 weeks
- Progress measured on the CEFR
→ **Ask about this class** (`forms.html#enquiry/anglia`)
Level test free · groups of up to 10 · prices effective November 2024 · books and insurance not included. Saturday schedule · Mathematics in English [link: “Saturday schedule” → `calendar.html#saturday`] [link: “Mathematics in English” → `english-anglia.html#math-english`]

#### Section: About our classes
- **Q: Our English classes in full** — A: Exam prep. Course- Graduation practice from the Moroccan school system. British practice. Business English Course- Covers Economics- Four levels available for certification. Conversational ESL Course- Aimed at improving the students speaking skills and introduction of new words. Beginner Level A-0 ESL-100 Courses- Basic English, with the target to increase English fluency, a basic level of literacy is expected. Pre-Intermediate A-+ and Intermediate B-1 ESL-200 Courses- Language skills, activities emphasizing oral and written. Interpersonal communication and academic. Advanced B-2 ESL -300 Course- Requires at least an Intermediate English level. Academic activities, essay writing, research papers development, and oral discussions of academic topics. English Writing Course- Narrative writing, Descriptive writing, Job applications, Resume/CV writing, oral discussions, and a review of phonics. The term one-to-one is applied to programs that provide all students in EFL setting, the ability to have full access to the teacher. EFL one- on- one programs are great for professionals that want to ask and learn for job related tasks. One-to-one refers to one teacher for every student. Many one-on-one teachers use the internet as a means to help promote positive literary skills.
Anglia Morocco
- Exams & levels [link: “Exams & levels” → `anglia-exams.html`]
- Exam dates [link: “Exam dates” → `anglia-exam-dates.html`]
- All prices [link: “All prices” → `fees.html#english`]

#### Section: Find the right class.
A free level test first – then we recommend the format and the level.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Contact** (`contact.html`)

---

### 4.30 `anglia-exam-dates.html`

- **Browser title:** Anglia exam dates 2026 – Anglia Morocco | AGI Agadir
- **Meta description:** Anglia exam sessions in Morocco in 2026, month by month and by level, and how to register at Anglia Morocco headquarters in Agadir.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Exam dates 2026 [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Anglia exam dates 2026.
Sessions run in most months of the year. If you need an exam on a date that is not listed, contact the Anglia office.
→ **Register for an exam** (`forms.html#enquiry/anglia`)
→ **Which level?** (`anglia-exams.html`)
Upcoming
All of 2026
| Month | Levels / session | Exam days |
|---|---|---|
| January | First Step, Junior Primary | Friday 13th | Saturday 21st |
| January | Preliminary A1, Elementary A2, Pre-Intermediate A2+, Intermediate B1, Advanced B2, Proficiency C1, Masters C2 | Saturday 21st |
| April | All Levels | Thursday 9th | Saturday 18th |
| May | Session 1 | Saturday 16th | Thursday 28th | Saturday 30th |
| May | Session 2 | Thursday 22nd | Saturday 24th |
| May | Session 3 | Saturday 14th |
| June | All levels | Thursday 18th, Saturday 20th, Sunday 21st, Friday 26th, Saturday 27th |
| July | Most Levels | Saturday 4th |
| July | All levels | Saturday 4th | Friday 24th |
| August | All levels | Friday 7th |
| September | All levels | Friday 18th | Saturday 19th |
| September | All levels | Saturday 19th |
| October | All levels | Thursday 15th | Saturday 17th |
| October | All levels | Thursday 15th |
| November | All levels | Thursday 19th | Saturday 21st | Saturday 28th |
| November | All levels | Thursday 19th | Saturday 21st |
| December | All levels | Thursday 10th, Saturday 12th, Thursday 17th, Saturday 19th |
| December | All levels | Saturday 12th |
Young-learner levels (First Step, Junior, Primary) often have their own days. Special arrangements must be requested when you register. Special arrangements [link: “Special arrangements” → `anglia-special-arrangements.html`]

#### Section: Ready to register?
Tell us the candidate's level and preferred session – the office will confirm.
→ **Register for an exam** (`forms.html#enquiry/anglia`)
→ **Practice papers** (`anglia-practice.html`)

---

### 4.31 `anglia-exams.html`

- **Browser title:** Anglia exams & levels – Anglia Morocco | AGI Agadir
- **Meta description:** The Anglia ladder: ten General English levels from First Step to Masters C2, four Business English levels A2+ to C1, exam durations and certificates for life.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Exams & levels [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Ten steps to Masters.
Anglia's General English exams take learners from a first vocabulary of about 100 words to expert use of English (Masters, C2). Every level tests listening, reading, writing and speaking.
→ **Find my level** (`forms.html#enquiry/anglia`)
→ **Exam dates** (`anglia-exam-dates.html`)

#### Section: The General English ladder
The three young-learner levels (YL) lead up to A1. Young-learner levels are also open to adults – anyone can start at the step that fits.
→ **What the CEFR levels mean** (`anglia-cefr.html`)
- Young learners
- 1 First Step YL Entry level from about age 4: understands about 100 words, follows basic classroom instructions, says who they are.
- 2 Junior YL Understands around 200 words, uses useful structures and explains what they are doing.
- 3 Primary YL About 400 words (jobs, feelings, weather); forms questions, answers them and describes things.
- General English
- 4 Preliminary A1 First general level for young and adult learners.
- 5 Elementary A2 Everyday situations and simple texts.
- 6 Pre-Intermediate A2+ Wider everyday communication.
- 7 Intermediate B1 Independent use in familiar contexts.
- Higher levels
- 8 Advanced B2 Complex texts and fluent interaction.
- 9 Proficiency C1 Effective operational proficiency.
- 10 Masters C2 Expert user. The Mastery qualification carries UCAS tariff points.

#### Section: Business English
Four steps for candidates whose special interest is business, from A2+ to C1.
→ **Business English classes** (`professional.html`)
- B1 Practical Business English A2+ Practical business functions in realistic workplace situations – all four skills.
- B2 Intermediate Business English B1 Practical business functions in realistic workplace situations – all four skills.
- B3 Advanced Business English B2 Practical business functions in realistic workplace situations – all four skills.
- B4 Proficiency in Business English C1 Practical business functions in realistic workplace situations – all four skills.

#### Section: How long are the exams?
- **Reading & writing** — 1 hour minimum, 3 hours maximum, depending on the level
- **Listening** — 10–30 minutes
- **Speaking** — About 5–20 minutes
- **Certificate** — Valid for life; an institution may ask for a recent one
- **Online exams** — Anglia exams can also be taken online in Morocco – ask the office

#### Section: In detail
- **Q: The exam descriptions in full** — A: Anglia Examinations have been based in Chichester, England, since 1993. Anglia offers a comprehensive and structured program for assessing English language competence, from beginner through to full competence as an expert user. This Step-by-Step approach to testing encourages and motivates students to make clear and effective progress. Please see us for a free placement test. The official website of Anglia Anglia Levels Anglia exams measure all four language skills – listening, reading, writing, and speaking. There are no minimum age requirements for the exams. The young learner levels are taken by children as young as four years old. The upper levels and Business English exams are taken by students and adults who plan to continue their studies at an English university/college or to improve their career prospects. Anglia Examinations in English currently consist of ten different levels and the Anglia International Business English examinations are available at four levels. The Proficiency level is listed by UCAS as a qualification that can be accepted by British universities to show international student competence in the English language. The Anglia Proficiency examination has been designed to incorporate a stronger academic element within its first section. All levels of the examinations have listening, reading, writing, and speaking elements. View this PowerPoint for information on the C.I.T.E. for teachers. New Microsoft PowerPoint Presentation- The History of Anglia in Morocco angliamorocco.org The history of Anglia Morocco started in 2010 by Suzanne Linsen. She moved to Morocco to introduce Anglia Examinations and its wide range of English language certificates to schools and institutes. Prior to that she was selected to conduct English courses and administer Anglia exams at a language institute in Tangier. During this year 2021, American Group International (AGI) became the Anglia franchise holder for Morocco. AGI has been an educational brand since 2012. AGI has placed hundreds of students into the American Educational System with low-cost, affordable, educational programs including an American School in Agadir. They have used the Anglia system in their language programs since 2013. Julie Wilburn is the CEO and lived in Morocco for many years and also holds dual citizenship in the country. The AGI team has now embarked on the next level in its offerings to give opportunities to thousands of people to master the international language of English in business and communication with top English training and assessments. We strive to give back to the Moroccan community and reach the areas that desire to take international exams. AGI wants local teams based in each of the 12 regions of the country to execute local community-based programs to reach the unreachable. The main headquarters are located in the cozy city of Agadir and it is centralized to the application of the AGI mission and educating the community in English throughout the Kingdom of Morocco. AGIs number of local franchise distribution networks will hopefully grow rapidly in the next few years; as English is quickly becoming a new love for Moroccan young people. This in return will hopefully open up new avenues for many including new international opportunities for people inside as well as international levels from the outside. Anglia Morocco along with AGI will work closely with; multiple’ education centres, schools, and businesses to develop new strategies to help all levels of schools and learners to achieve a higher standard of English. Addressing the challenges due to the COVID pandemic, AGI is offering online platforms and examinations, AGI and Anglia Maroc communities, and events to enhance greater opportunities in Moroccan communities. With AGIs mission “Global Minds with a Global Perspective”, we strive to offer a better opportunity for the Moroccan community to ‘Dare to Dream in English’ with the Step-by-Step approach. Anglia Maroc is offering Anglia English exams from Beginners to Mastery level (CEFR C2) through the European Framework. To contact Anglia Morocco/ AGI American Group International Julie Wilburn – CEO & Educational Director Abdelhak Lam- Assistant of Operations Headquarters Branch Agadir/Sales Number 20, Rue Baalabek, Cite Nahda, Agadir, and Morocco.80000 Anglia Examinations England 30th year celebration in Chichester West Sussex, England. Picture with Julie Wilburn, center. September 2023. Anglia is presented by 45 plus countries worldwide. Part of the Chichester College Group, the 3rd biggest group in the United Kingdom. Robo Gallery: You didn’t select any Robo Gallery item in editor. Please select one from the list or create new gallery Anglia Exams offers a range of Business English Exams that test the English proficiency level of students whose special interest is business. The exams are divided into four steps, ranging in level from A2+ to C1 on the CEFR, and test all four skills of reading, writing, listening and speaking. The exams are designed to evaluate the linguistic competence of candidates who may be considering a future in an international workplace or may already be working in the professional world 1. If you’re interested in taking one of these exams, you can visit Anglia Exams for more information. Business English Exams English is the lingua-franca of business. No matter where in the world you live or work, the ability to communicate effectively in English is a definite advantage when conducting business. In an increasingly globalised world, being proficient in business English gives you a competitive edge. The four steps of the Anglia Business English exams, ranging in level from A2+ to C1 on the CEFR, test the English proficiency level of students whose special interest is business. Candidates may be considering a future in an international workplace or may already be working in the professional world and be keen to evaluate their linguistic competence. With an emphasis on practical business application in realistic situations, our communicative exams offer a progressive choice of levels: A2+, B1, B2 and C1, and test all four skills of reading, writing, listening and speaking. An online examination is a great way to conduct exams and tests using the internet. An online exam requires a device capable of accessing the internet. You can conduct an online exam at home or an examination centre. It is essential in the remote learning system where candidates can appear for exams from home. They need not travel to give the exam in the online examination system. A microphone and webcam are sufficient for online evaluation tests. Also, you need not invest in exam centres, security and invigilators. ￼ Unlock Your Future with Anglia Examinations England! Now Offering Online Examinations in Morocco Get internationally recognized English certifications from the comfort of your home. Join thousands of successful students and enhance your career opportunities. Why Choose Anglia Examinations England? Convenient Online Testing: Take exams from anywhere in Morocco. Wide Range of Levels: From beginners to advanced proficiency. Trusted and Recognized: Certifications valued by employers and educational institutions worldwide. Supportive Learning Environment: Access to study materials and practice tests. Enroll Today! Visit our website or contact us at americanecoleagadir@gmail.com to learn more and register. Anglia Examinations England – Your Pathway to Global Success! Anglia Exams Anglia Exams: Tests of English as a Foreign or Second Language Anglia Exams are ideal for testing the abilities of those learning English as a foreign language. The Anglia General English exam suite measures all four language skills – listening, reading, speaking and writing. Our exams are ideal for teachers and students of English as a foreign or second language and are designed to measure the ability and help guide candidates from beginner level at First Step, to Masters (C2) level. Our young-learner levels are also available for adult learners, meaning that anyone at any age can start learning English step-by-step with confidence. Anglia’s educational testing service is designed to support education providers and measure the ability of English language proficiency of leaners at all ages and ability First Step Junior Level Exam TaPrimary Level Exam b 3 Primary Level Exam Preliminary Level Exam Our entry level English language exam. Children as young as four years old can begin here. Demonstrate an understanding of about 100 words, follow basic classroom instructions and know how to say who you are Our second step in the Anglia English exam learning journey. Students need to be able to demonstrate an understanding of around 200 words, are able to use useful structures and explain what they are doing. Step 3 in our progressive exam series covers a vocabulary of about 400 words in categories like jobs, feelings and weather. Students will be able to demonstrate how to form questions, provide answers to questions, and be able to describe things. Business English Exams English is the lingua-franca of business. No matter where in the world you live or work, the ability to communicate effectively in English is a definite advantage when conducting business. In an increasingly globalised world, being proficient in business English gives you a competitive edge.English for Business EFL step by step To learn more about a specific exam level please click on the tabs below. Practical Business English Intermediate Business English Advanced Business English Exam Proficiency in Business English At this level, candidates are expected to have an A2+ level of English. The Business English exams are based on a candidate’s ability to perform certain practical functions in the workplace. Therefore the Practical Business English exam does not have a specific grammar and structures syllabus as the business context tends to demand set structures. However, the syllabus of the corresponding level (A2+) of the General English examinations gives an overview of the language expected at this level. At this level, candidates are expected to have a level of English equivalent to B1 on the CEFR. As the Business English exams are based on a candidate’s ability to perform practical functions in the workplace, this exam does not have a specific grammar and structures syllabus. The business context tends to demand set structures. However, the syllabus of the corresponding level (B1) of the General English examinations gives an overview of the language expected at this level. At this level, candidates are expected to have a level of English equivalent to B2 on the CEFR. As the Business English exams are based on a candidate’s ability to perform practical functions in the workplace, this exam does not have a specific grammar and structures syllabus. The business context tends to demand set structures. However, the syllabus of the corresponding level (B2) of the General English examinations gives an overview of the language expected at this level.
Next
- Practice papers [link: “Practice papers” → `anglia-practice.html`]
- Special arrangements [link: “Special arrangements” → `anglia-special-arrangements.html`]
- Classes & prices [link: “Classes & prices” → `anglia-classes.html`]

#### Section: Not sure which level?
Take the free placement assessment – we will recommend the right step.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Try a practice paper** (`anglia-practice.html`)

---

### 4.32 `anglia-faq.html`

- **Browser title:** Anglia FAQ – Anglia Morocco | AGI Agadir
- **Meta description:** Anglia exams FAQ: levels, ages from 4, durations, lifetime certificates, UCAS tariff points for Mastery.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Anglia FAQ [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Anglia FAQ
Answers about Anglia exams – levels, ages, durations and certificates.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Exam dates** (`calendar.html#anglia-exams`)
- **Q: What are the Anglia exams?** — A: Official English certificates from Anglia Examinations (Chichester, England, since 1993; part of Chichester College Group). They evaluate reading, listening, speaking and writing, from initiation to expertise, helping students reach the level they want step by step.
- **Q: Which levels do they certify?** — A: 10 levels in three groups – young learners (First Step, Junior, Primary, Preliminary), intermediate (Elementary, Pre-Intermediate, Intermediate) and higher (Advanced, Proficiency, Masters) – plus Business English levels with business vocabulary.
- **Q: How long do the exams last?** — A: Reading and writing: 1 hour minimum and 3 hours maximum depending on the level. Listening: 10 to 30 minutes. Speaking: about 5 to 20 minutes.
- **Q: Who can take them?** — A: Anyone: students of all ages from 4 years onwards, with no upper age limit. You can start at the level you or your teacher consider appropriate.
- **Q: Do I need extra classes?** — A: No – preparation is built into the classroom curriculum. Classes at AGI are available if you want them.
- **Q: Does the certificate expire?** — A: It lasts for life, but an institution may ask for a recent one if yours is very old.
- **Q: How do I know which level to take?** — A: Take the free placement assessment; Anglia also offers an additional exam that determines your level.
- **Q: Are Anglia certificates recognized by universities?** — A: The Mastery (C2) qualification carries UCAS tariff points for UK universities. [TO CONFIRM: Further recognition statements to be confirmed with Anglia.]
- **Q: Are they affordable?** — A: Anglia exams are priced affordably compared with other international certificates.
Anglia Morocco
- Anglia Morocco [link: “Anglia Morocco” → `anglia.html`]
- Exams & levels [link: “Exams & levels” → `anglia-exams.html`]
- Exam dates 2026 [link: “Exam dates 2026” → `calendar.html#anglia-exams`]
- CEFR levels [link: “CEFR levels” → `anglia-cefr.html`]
- Practice papers & audio [link: “Practice papers & audio” → `anglia-practice.html`]
- Step To books [link: “Step To books” → `anglia-books.html`]
- Special arrangements [link: “Special arrangements” → `anglia-special-arrangements.html`]
- Free placement assessment [link: “Free placement assessment” → `anglia-placement-test.html`]
- Classes & prices [link: “Classes & prices” → `anglia-classes.html`]
- Network & centres [link: “Network & centres” → `anglia-network.html`]
- Become a centre [link: “Become a centre” → `partnerships.html`]
- About Anglia Examinations [link: “About Anglia Examinations” → `anglia-about.html`]
- C.I.T.E. for teachers [link: “C.I.T.E. for teachers” → `teachers.html#cite`]
Anglia Morocco headquarters: AGI, Agadir · j.wilburn@angliamorocco.org · a.lam@angliamorocco.org

---

### 4.33 `anglia-network.html`

- **Browser title:** Become an Anglia centre – Anglia Morocco | AGI Agadir
- **Meta description:** Anglia Morocco network across Morocco's 12 regions: open representative positions, franchise and institutional partnership models, how to become an Anglia centre.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Become a centre [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Become an Anglia centre.
From its Agadir headquarters, Anglia Morocco works with schools, language centres and teachers across the Kingdom's twelve regions. Several regions are looking for a local representative.
→ **Partnership enquiry** (`forms.html#enquiry/partnership`)
→ **Partnership models** (`partnerships.html`)

#### Section: The 12 regions
Main headquarters: AGI, Agadir · Sales coordinator: Abdelhak Lam.
Anglia network
**Dakhla-Oued Ed-Dahab Region**
- **Q: 2 prefectures & provinces** — A: Aousserd Province Oued Ed-Dahab Province
Representative wanted
**Laâyoune-Sakia El Hamra Region**
- **Q: 4 prefectures & provinces** — A: Boujdour Province Es Semara Province Laâyoune Province · representative wanted Tarfaya Province
Representative wanted
**Guelmim-Oued Noun Region**
- **Q: 4 prefectures & provinces** — A: Assa-Zag Province Sidi Ifni Province · representative wanted Guelmim Province Tan-Tan Province
Headquarters · Agadir
**Souss-Massa Region**
- **Q: 6 prefectures & provinces** — A: Agadir-Ida Ou Tanane · representative wanted Inezgane-Aït Melloul Chtouka Aït Baha Province Taroudant Province · representative wanted Tata Province Tiznit Province
Anglia network
**Drâa-Tafilalet Region**
- **Q: 5 prefectures & provinces** — A: Errachidia Province Midelt Province Ouarzazate Province Tinghir Province Zagora Province
Anglia network
**Marrakech-Safi Region**
- **Q: 8 prefectures & provinces** — A: Marrakech Al Haouz Province Chichaoua Province El Kelâat Es-Sraghna Province Essaouira Province Rehamna Province Safi Province Youssoufia Province
Anglia network
**Tanger-Tetouan-Al Hoceima Region**
- **Q: 8 prefectures & provinces** — A: M’diq-Fnideq Prefecture Tangier-Assilah Prefecture Al Hoceïma Province Chefchaouen Province Fahs-Anjra Province Larache Province Ouezzane Province Tétouan Province
Representative wanted
**Fès-Meknès Region**
- **Q: 9 prefectures & provinces** — A: Fè s · representative wanted Meknès Boulemane Province El Hajeb Province Ifrane Province Sefrou Province Taounate Province Taza Province Moulay Yacoub Province
Anglia network
**Rabat-Salé-Kénitra Region**
- **Q: 7 prefectures & provinces** — A: Rabat Salé Skhirat-Témara Kénitra Province Khémisset Province Sidi Kacem Province Sidi Slimane Province
Anglia network
**Béni Mellal-Khénifra Region**
- **Q: 5 prefectures & provinces** — A: Azilal Province Béni-Mellal Province Fquih Ben Salah Province Khénifra Province Khouribga Province
Anglia network
**Casablanca-Settat Region**
- **Q: 17 prefectures & provinces** — A: Casablanca Casablanca Anfa Al Fida – Mers Sultan Aïn Sebaâ – Hay Mohammadi Hay Hassani Aïn Chock Sidi Bernoussi Ben M’Sick Moulay Rachid Mohammedia Ben Slimane Province Berrechid Province El Jadida Province Médiouna Province Nouaceur Province Settat Province Sidi Bennour Province
Representative wanted
**Oriental Region**
- **Q: 8 prefectures & provinces** — A: Oujda-Angad · representative wanted Berkane Province Driouch Province Figuig Province Guercif Province Jerada Province Nador Province Taourirt Province

#### Section: Two ways to work with us
_Model I_
**Anglia centre (franchise)**
An Anglia Morocco centre under your ownership: the examinations license, placement and testing system, teacher training and C.I.T.E., and a territory agreement within the 12 regions.
_Model II_
**Institutional partnership**
For existing schools and institutes: an Anglia testing centre inside your campus, co-designed English programs and university pathway agreements.
→ **Partnerships in detail** (`partnerships.html`)

#### Section: Represent Anglia in your region.
Tell us your region, the model and your teaching or business background.
→ **Partnership enquiry** (`forms.html#enquiry/partnership`)
→ **Contact** (`contact.html`)

---

### 4.34 `anglia-placement-test.html`

- **Browser title:** Free placement assessment – Anglia Morocco | AGI Agadir
- **Meta description:** Free English placement assessment on the CEFR at Anglia Morocco headquarters in Agadir.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Placement assessment [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Free placement assessment
Find your English level on the CEFR before you choose a class or an Anglia exam.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Exam dates** (`calendar.html#anglia-exams`)

#### Section: How it works
- Book your free assessment online or by WhatsApp.
- Take the assessment at AGI in Agadir: reading, listening, writing and a short conversation.
- Get your CEFR level and a recommendation: a class, a learning pod or the right Anglia exam.
→ **Book my free assessment** (`forms.html#enquiry/anglia`)

#### Section: Want to practice first?
Try the official Anglia sample papers for your level.
→ **Practice papers** (`anglia-practice.html`)
Anglia Morocco
- Anglia Morocco [link: “Anglia Morocco” → `anglia.html`]
- Exams & levels [link: “Exams & levels” → `anglia-exams.html`]
- Exam dates 2026 [link: “Exam dates 2026” → `calendar.html#anglia-exams`]
- CEFR levels [link: “CEFR levels” → `anglia-cefr.html`]
- Practice papers & audio [link: “Practice papers & audio” → `anglia-practice.html`]
- Step To books [link: “Step To books” → `anglia-books.html`]
- Special arrangements [link: “Special arrangements” → `anglia-special-arrangements.html`]
- Classes & prices [link: “Classes & prices” → `anglia-classes.html`]
- Network & centres [link: “Network & centres” → `anglia-network.html`]
- Become a centre [link: “Become a centre” → `partnerships.html`]
- Anglia FAQ [link: “Anglia FAQ” → `anglia-faq.html`]
- About Anglia Examinations [link: “About Anglia Examinations” → `anglia-about.html`]
- C.I.T.E. for teachers [link: “C.I.T.E. for teachers” → `teachers.html#cite`]
Anglia Morocco headquarters: AGI, Agadir · j.wilburn@angliamorocco.org · a.lam@angliamorocco.org

---

### 4.35 `anglia-practice.html`

- **Browser title:** Practice papers & audio – Anglia Morocco | AGI Agadir
- **Meta description:** Free Anglia practice papers and sample exams for every level: General English, Business English, Children's Oral Tests, Applied Translation and C.I.T.E. for teachers.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Practice papers [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Practice resources.
Practice papers and sample exams for every Anglia level, published by Anglia Examinations. Pick your level and download – then check your answers with your teacher.
→ **Choose my level** (`#general-english`)
→ **Step To books & audio** (`anglia-books.html`)
→ **General English** (`#general-english`)
→ **Business English** (`#business-english`)
→ **Children's Oral Tests of Achievement** (`#children-s-oral-tests-of-achievement`)
→ **Certificate & Diploma in Applied Translation** (`#certificate-diploma-in-applied-translation`)
→ **Teachers (C.I.T.E.)** (`#teachers-c-i-t-e`)

#### Section: General English
**First Step**
Ask Anglia Morocco for a copy
**Junior**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/junior-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/junior-pack-2-jj120.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/junior-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/junior-pack-4-aa119.zip`]
**Primary**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/primary-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/primary-pack-2-jj120.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/primary-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/primary-pack-4-aa119.zip`]
**Preliminary**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/preliminary-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/preliminary-pack-2-ff119.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/preliminary-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/preliminary-pack-4-aa119.zip`]
**Elementary**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/elementary-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/elementary-pack-2-ff119.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/elementary-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/elementary-pack-4-aa119.zip`]
**Pre-Intermediate**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/pre-intermediate-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/pre-intermediate-pack-2-ff119.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/pre-intermediate-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/pre-intermediate-pack-4-aa119.zip`]
**Intermediate**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/intermediate-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/intermediate-pack-2-ff119.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/intermediate-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/intermediate-pack-4-aa120.zip`]
**Advanced**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/advanced-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/advanced-pack-2-ff119.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/advanced-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/advanced-pack-4-aa120.zip`]
**Proficiency**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/proficiency-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/proficiency-pack-2-ff119.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/proficiency-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/proficiency-pack-4-aa120.zip`]
**Masters**
Pack 1 Pack 2 Pack 3 Pack 4 [link: “Pack 1” → `https://angliaexams.com/wp-content/uploads/2021/09/masters-pack-1-ff120.zip`] [link: “Pack 2” → `https://angliaexams.com/wp-content/uploads/2021/09/masters-pack-2-ff119.zip`] [link: “Pack 3” → `https://angliaexams.com/wp-content/uploads/2021/09/masters-pack-3-gg119.zip`] [link: “Pack 4” → `https://angliaexams.com/wp-content/uploads/2021/09/masters-pack-4-aa120.zip`]

#### Section: Business English
**Practical Business English**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/09/practical-business-english.zip`]
**Intermediate Business English**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/09/intermediate-business-english.zip`]
**Advanced Business English**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/09/advanced-business-english.zip`]
**Proficiency in Business English**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/09/proficiency-business-english.zip`]

#### Section: Children's Oral Tests of Achievement
**Level I**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/childrens-oral-level-i-3.zip`]
**Level II**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/childrens-oral-level-ii.zip`]
**Level III**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/childrens-oral-level-iii-1.zip`]

#### Section: Certificate & Diploma in Applied Translation
**Certificate in Applied Translation**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/certificateinappliedtranslation-7.zip`]
**Diploma in Applied Translation**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/diplomainappliedtranslation-1.zip`]

#### Section: Teachers (C.I.T.E.)
**C.I.T.E. Very Young Learners**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/cite-vyl-2.zip`]
**C.I.T.E. Young Learners**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/cite-yl-2.zip`]
**C.I.T.E. Senior**
Download [link: “Download” → `https://angliaexams.com/wp-content/uploads/2021/08/cite-sr-3.zip`]
Files are hosted by Anglia Examinations. Not sure of your level? Book a free level test. [link: “Book a free level test” → `forms.html#enquiry/anglia`]

#### Section: Want guided preparation?
Our classes and the Step To books prepare candidates for every level.
→ **Classes & prices** (`anglia-classes.html`)
→ **Step To books** (`anglia-books.html`)

---

### 4.36 `anglia-special-arrangements.html`

- **Browser title:** Special arrangements – Anglia Morocco | AGI Agadir
- **Meta description:** Special arrangements for Anglia exams in Morocco: extra time, breaks, Braille or large print, wheelchair access, scribe, lip reading; codes D1–D8.

[IMAGE: Anglia Examinations England – Anglia Morocco]
Home / Anglia Morocco / Special arrangements [link: “Home” → `index.html`] [link: “Anglia Morocco” → `anglia.html`]
**Page title (H1):** Special arrangements
Exams should be accessible to everyone. Candidates with learning or physical difficulties – or an injury on the day – can ask for support.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Exam dates** (`calendar.html#anglia-exams`)
We believe exams should be accessible to everyone, regardless of their learning or physical impairments. Please read this page before you register for your exam. It includes frequently asked questions about the provisions available for candidates with specific learning difficulties.

#### Section: Special Arrangements
Anglia il is committed to providing all students with open and fair access to opportunity. We provide a special arrangements service for candidates with hearing, speech, visual and kinetic difficulties. We also provide special arrangements for candidates with learning difficulties such as dyslexia.
We will also make special arrangements for you on the day of the exam if you have been in an accident before taking your exam and have an injury such as a broken arm.
These are the types of special arrangements we are able to make:
- extended testing time
- supervised breaks
- alternate test formats such as Braille or enlarged print
- wheelchair access
- a copier or amanuensis (someone who can type the words that you dictate to them)
- listening with lip reading.
If you need other special arrangements that are not mentioned here, we will do everything we can to meet your needs. Contact us and we will try to find the most suitable solution.

#### Section: Disability codes
Use these codes when you request special arrangements.
| Need | Code |
|---|---|
| Dyslexia | D1 |
| ADD/ADHD | D2 |
| PDD-NOS / Autism / Asperger | D3 |
| Physical Disability | D4 |
| Hearing Impairment | D5 |
| Vision Impairment | D6 |
| Illegible handwriting | D7 |
| Other (please specify in comments) | D8 |
→ **Request special arrangements** (`forms.html#enquiry/anglia`)
Anglia Morocco
- Anglia Morocco [link: “Anglia Morocco” → `anglia.html`]
- Exams & levels [link: “Exams & levels” → `anglia-exams.html`]
- Exam dates 2026 [link: “Exam dates 2026” → `calendar.html#anglia-exams`]
- CEFR levels [link: “CEFR levels” → `anglia-cefr.html`]
- Practice papers & audio [link: “Practice papers & audio” → `anglia-practice.html`]
- Step To books [link: “Step To books” → `anglia-books.html`]
- Free placement assessment [link: “Free placement assessment” → `anglia-placement-test.html`]
- Classes & prices [link: “Classes & prices” → `anglia-classes.html`]
- Network & centres [link: “Network & centres” → `anglia-network.html`]
- Become a centre [link: “Become a centre” → `partnerships.html`]
- Anglia FAQ [link: “Anglia FAQ” → `anglia-faq.html`]
- About Anglia Examinations [link: “About Anglia Examinations” → `anglia-about.html`]
- C.I.T.E. for teachers [link: “C.I.T.E. for teachers” → `teachers.html#cite`]
Anglia Morocco headquarters: AGI, Agadir · j.wilburn@angliamorocco.org · a.lam@angliamorocco.org

---

### 4.37 `anglia.html`

- **Browser title:** Anglia Morocco – official English exams from England | AGI Agadir
- **Meta description:** Anglia Morocco headquarters at AGI, Agadir: official English exams from England, First Step to Masters C2, from age 4. Exam dates, classes, free level test, centres in 12 regions.

Home / Anglia Morocco [link: “Home” → `index.html`]
**Page title (H1):** Official English certificates from England.
Anglia Examinations has tested English since 1993 from Chichester, England. Since 2021 AGI has been the Anglia franchise holder for Morocco – exams from a child's first words to Masters (C2), classes, and centres across the Kingdom's twelve regions.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Exam dates 2026** (`anglia-exam-dates.html`)
[IMAGE: Anglia Examinations England – Anglia Morocco]

#### Section: Where do you start?
Parents & students Certify your child's English Ten steps from a child's first words (about age 4) to Masters C2 – each one a certificate from England. Continue → Adults & professionals English for work and study General English up to Masters, or Business English from A2+ to C1, with classes that fit a working week. Continue → Teachers C.I.T.E. certification A lifelong TESOL qualification recognized worldwide – no entry qualifications required. Continue → Schools & partners Become an Anglia centre Run Anglia exams in your school or region, with training and materials from the Agadir headquarters. Continue → [link: “Parents & students Certify your child's English Ten steps from a child's first words (about age 4) to Masters C2 – each one a certificate from England. Continue →” → `anglia-exams.html`] [link: “Adults & professionals English for work and study General English up to Masters, or Business English from A2+ to C1, with classes that fit a working week. Continue →” → `anglia-classes.html`] [link: “Teachers C.I.T.E. certification A lifelong TESOL qualification recognized worldwide – no entry qualifications required. Continue →” → `teachers-cite.html`] [link: “Schools & partners Become an Anglia centre Run Anglia exams in your school or region, with training and materials from the Agadir headquarters. Continue →” → `anglia-network.html`]

#### Section: Why Anglia
AGI is the official Anglia Examinations franchise holder for Morocco.
England, since 1993 Part of Chichester College Group – award winning and Ofsted Outstanding.
Regulated by Ofqual The four highest levels are awarded by AIM Qualifications and Assessment Group.
UCAS tariff points The Mastery (C2) qualification counts for UK university entry.
For life Certificates do not expire – an institution may ask for a recent one.
From age 4 No upper age limit; every level tests listening, reading, writing and speaking.
October
Next exam session: All levels
Thursday 15th | Saturday 17th – sessions run in most months; other dates are possible on request.
→ **All 2026 dates** (`anglia-exam-dates.html`)

#### Section: Everything about Anglia in Morocco
- Link card → `anglia-exams.html`: Exams & levels
- Link card → `anglia-exam-dates.html`: Exam dates 2026
- Link card → `anglia-classes.html`: Classes & prices
- Link card → `anglia-practice.html`: Practice papers & audio
- Link card → `anglia-books.html`: Step To books
- Link card → `anglia-special-arrangements.html`: Special arrangements
- Link card → `anglia-cefr.html`: CEFR levels
- Link card → `anglia-faq.html`: Anglia FAQ
- Link card → `anglia-about.html`: About Anglia Examinations

#### Section: Anglia Morocco in its own words
- **Q: The Anglia Morocco welcome text** — A: Anglia English Examinations Morocco English exam board and a global family of English exam centres and specialist language schools working together to help people from all walks of life achieve their dreams. Anglia Examination’s English proficiency tests are trusted by education institutions and partners around the world Through Ten Steps Our exams are ideal for teachers and students of English as a foreign or second language and are designed to measure the ability and help guide candidates from beginner level at First Step, to Masters (C2) level. Learn More.. Through Four Steps Our Step by step General English Exams progress through ten steps- from First Step to Mastery. Our four high levels of English language exams are accredited by AIM Awards & Qualifications and are endorsed. Equal Opportunity And Diversity Anglia is committed to providing all students with open and fair access to opportunity. We provide a special arrangements service for candidates with hearing, speech, visual, kinetic, and learning difficulties such as dyslexia. C.I.T.E – Certificate for International Teachers of English (TESOL) C.I.T.E. (Certificate for International Teachers of English) is a prestigious TESOL qualification offered by Anglia Examinations England. This certification demonstrates your mastery of English and your ability to teach the language effectively. It’s a lifelong qualification with no expiration date, recognized worldwide. English Language Tests- Dare To Dream In English We are an English exam board and a global family of English exam centres and specialist language schools working together to help people from all walks of life achieve their dreams. Anglia Examination’s English proficiency tests are trusted by education institutions and partners around the world. Taking an English test with Anglia Examinations (or one of our many partners) is a good way of demonstrating your English ability. For ESOL teachers who want to know how to test English language proficiency then please do read on. Or perhaps your want to prove your English ability for an employer, school, college or University? We offer English EFL exams at all levels including CITE exams for teachers of English as a foreign language. An Anglia certificate of proficiency provides the evidence you need to accurately prove your ability. We are strict about standards- providing quality English language tests for students of English as a second language and giving our exam candidates the confidence that our proctored exams and certificates are backed awarding body AIM Qualifications and Assessment Group. We offer online tests and paper based exams in English reading, writing, listening and speaking tests for all levels of capability. Anglia Examinations is more than just another English examination board- we offer a global community of learning and professionalism combined with specialist local knowledge. Our trusted partners around the world have a shared vision; to help people from diverse backgrounds achieve their full potential. Whether you need to prove your English language skills to employers or educational establishments we never compromise on our standards and consistency. We work together with partners to help others attain proficiency in the English Language. Our partners and test centres choose us above others due to our authenticity and the strength of the bespoke and personalised relations we pride ourselves on. Based in the UK, we offer a unique S tep-by-Step approach. Our ESOL exams are designed for young learners, high school students and teachers of English as a Foreign language and are mapped to the Common European Framework CEFR, allowing English language learners to steadily gain mastery of the English language. For those in commerce we offer our Anglia Business English Exams. We price ourselves in providing a friendly and professional service and work with expert language partners, awarding organisations, universities and employers the world over to deliver an exemplary service. Learners who achieve Anglia English exams are examined to exacting, consistent and robust standards. Our partners have grown with us over many years, offering English exam takers all over the world credible and respected exams and an accessible path to English language competency. We would love to hear from you. Please do get involved, share your stories with us and help us in our mission to help others to “Dream in English”. Five Reasons to Trust Anglia Exams We have applied for our Highest level exam (Mastery General English CEFR C2), to be awarded award UCAS tariff points which will mean that holders of this qualification will secure UCAS points to count towards University admissions. We apply rigourous standards to our exams, we will never compromise on the quality and robustness of our qualifications. Our four highest level of exam are awarded by AIM Qualification & Assessments and accredited. Anglia Awards is a wholly owned subsidiary of the Chichester College Group who are award winning and Ofsted Outstanding. Our exams are mapped to the Common European of References for Languages (CEFR) so that you can see how our levels compare. Many Universities, employers and local governments around the world recognise our qualifications. New institutions are formally recognising Anglia English language exams on a regular basis Anglia Morocco Network Northern Region Franchise Opportunities Available Anglia Representative Partners We work together to ensure that the quality and rigour of Anglia Exams are maintained to ensure consistency and high standards at all times. Please note that the map below is not yet complete- we will add further partners soon. Learn More here.. Southern Region-Anglia Headquarters-Agadir This Is Who We Are We deeply believe that great companies are made by great people. We believe that the working environment is a crucial factor in the company’s development, and that a good working environment is important for the people who make a huge effort every day. Julie WILBURN CEO & Educational Director, Anglia Examinations Morocco Abdelhak LAM Main Headquarters Sales Coordinator

#### Section: Club Anglia
[TO CONFIRM: Coming soon.]
Contacts
Julie Wilburn · j.wilburn@angliamorocco.org Abdelhak Lam · a.lam@angliamorocco.org angliamorocco.org [link: “angliamorocco.org” → `https://angliamorocco.org/`]

#### Section: Find your English level.
The placement assessment is free and takes place at AGI in Agadir.
→ **Book a free level test** (`forms.html#enquiry/anglia`)
→ **Classes & prices** (`anglia-classes.html`)

---

### 4.38 `attendance.html`

- **Browser title:** Attendance – American Group International, Agadir
- **Meta description:** AGI attendance policy: 90% attendance for promotion, excused absences, late arrivals and consequences.

Home / Admissions / Policies / Attendance [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Attendance
Why attendance matters, what counts as excused, and what happens after unexcused absences or late arrivals.
On this page
- Rights [link: “Rights” → `#rights`]
- Responsibilities [link: “Responsibilities” → `#responsibilities`]
- Unexcused Absence and Tardiness Consequences [link: “Unexcused Absence and Tardiness Consequences” → `#unexcused-absence-and-tardiness-consequences`]
- First Offense (1 Day) [link: “First Offense (1 Day)” → `#first-offense-1-day`]
- Second Offense (3 day) [link: “Second Offense (3 day)” → `#second-offense-3-day`]
- Subsequent Offenses (5 day) [link: “Subsequent Offenses (5 day)” → `#subsequent-offenses-5-day`]
- Additional Options [link: “Additional Options” → `#additional-options`]
- Excused Absences [link: “Excused Absences” → `#excused-absences`]
- Family Obligations [link: “Family Obligations” → `#family-obligations`]
American Group International of Agadir, Morocco shall maintain a strict attendance policy that adheres to students’ best interests as well as the law.
As a qualification for promotion to the next grade level in grades K-12, students must be in attendance 90% of the year. In accordance with State laws, parents must provide a dated and signed excuse stating the reason for any absence. The excuse must be submitted no later than two days after the student returns to school. A student who arrives at school after 10:00 a.m. is considered absent for the full day. A student is considered late and will be marked on school records as such if he/she arrives after 9:00 a.m.
Furthermore, if a student has (5) unexcused tardies past 9:00 am, that equates to one (1) unexcused day absent.
Students have the right to make up assignments missed during any excused absence. Parents and students have the right to review school policies which clearly define what is considered an excused absence, an unexcused absence, and tardiness. Parents and students also have the right to appeal a decision concerning whether an absence is excused or unexcused.
Tardiness: When a child reports late, they must obtain a late slip from the front desk (whether he/she is arriving to school late or has arrived at school early but is late getting to the classroom). The admin office shall be responsible for recording the student’s name, date, time, and reason for tardiness on a Late Slip designed for that purpose. After recording the information, the receptionist shall give the student that slip to give to the teacher. Teachers will mark tardiness or absence on the student record. Students arriving to school after 9:00 must provide the office with a written note from the parent stating the reason the student is late or “absent”. Once the note is received the student will be given a late slip to be admitted to the classroom. If a student does not have an acceptable reason for being tardy, he/she will be marked unexcused tardy.
Arrival after 10:00 a.m.: Students arriving after 10:00 a.m. are considered and remain marked as “absent” for the full day. Parents should make every effort to have their children well rested, fed and in school on time daily.
Absences: Students who are absent must return to school with a note from a parent/guardian. A student absent for three or more days due to illness must have a signed excuse from their doctor upon returning to school. Students who are absent or sent home because they contracted a communicable disease such as COVID-19, pinkeye, head lice, ringworm, chicken pox, etc. must be seen by a physician and provide a doctor’s note indicating they can return to school. The admin office shall keep all parents notes or doctors’ excuses in the student file. Notes that state long-term absences from school, i.e., vacation, extended family trip, are not counted as excused; hence, parents are encouraged to plan voluntary, non-emergency extended absences around the school calendar. Acceptable absences, such as death in family, hospitalizations, family emergency shall require a written and signed note from the doctor or agency indicating the date(s) of absences. The school administration will determine if an absence or lateness is excused or unexcused.
Early Dismissal: in the event your child has a medical or other appointment which that may require an early dismissal (being picked up prior to the 1:30 p.m. scheduled dismissal time), please write a note and give to the administration office stating the reason and time for the early dismissal. All early dismissals will be held in the front lobby, not from the classroom. When you come to pick up your child at the office, will ensure he/she arrives to the lobby to meet you. No early dismissal will be allowed after 2:30 pm.

#### Section: Rights
Parents have the right to:
- Receive policies that clearly define absence, unexcused absence, and tardiness.
- Appeal a decision concerning whether an absence is excused or unexcused.
- Make up assignments missed during any excused absences.

#### Section: Responsibilities
Parents/Students/Clients have the responsibility to:
- Attend all classes daily and on time.
- Provide the program with a written excuse from parents/guardians explaining the reason for an absence upon return to AGI.
- Request the make-up assignments from their teachers upon the return to the office and to complete the work within the length of time specified by the teacher.

#### Section: Unexcused Absence and Tardiness Consequences

#### Section: First Offense (1 Day)
- Parent/guardian notification
- Complete missed assignments.

#### Section: Second Offense (3 day)
- Written notification

#### Section: Subsequent Offenses (5 day)
- Parent Conference (Mandatory)
- Attendance Contract

#### Section: Additional Options
- Referral to School AGI Operation Committee for possible disenrollment (after 10 days)

#### Section: Excused Absences
Only the following will be accepted as valid reasons for excused absences or tardies:
- Illness of student. The school will require doctor’s validation for absences over three consecutive days or for any single day once a student has accumulated 5 absences due to illness.
Contagious disease within the student’s home.
- Death in the student’s family.
Legal business that must be scheduled during school time that is verified by a court order, summons, or other formal documentation.
- Observance of religious holidays.
- Remedial health treatment that must be scheduled during school time, verified by a doctor’s note or receipt.
- Medical or health appointments that must be scheduled during school time, verified by a doctor’s note or receipt.
- Emergency situations as determined by the principal.
- Participation in school sponsored academic or extracurricular activities events.
- Pre-approved family obligations in accordance with the provision below:

#### Section: Family Obligations
AGI strongly encourages families to schedule family vacations to not conflict with AGI’s published calendar. However, we recognize that there are times when a student must be absent from school due to family/work obligations. Therefore, once a year, the principal may approve a one-time absence of up to five school days. To have an absence excused as a family obligation, the parent must submit a written request to the principal 30 days prior to the anticipated absence. In excusing absences for family obligations, the student’s past and current attendance, academic status, and the timing of the absence will be considered. Absences that exceed 5 days will not be excused. Students will be responsible for all missing learning and assignments and will be required to make up the work at home with the assistance of their families.
All children that miss the maximum number of days (20) without proper excuse will be required to attend the summer sessions. A full calendar year is made up of 180 days.
Regards,
Julie Wilburn, Principal
Text as published by AGI. Please check with the office for the current version. Source: “American Group International of Agadir Attendance Policy” (former AGI website), “The Importance of School Attendance” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.39 `calendar.html`

- **Browser title:** Calendar 2026–27 – American Group International, Agadir
- **Meta description:** AGI school calendar 2026–27: registration Aug 28 & 31, first day Sept 7, holidays and breaks, last day June 17; Saturday classes and Anglia exam sessions.

Home / Admissions / Calendar [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`]
**Page title (H1):** Calendar 2026–27.
Every school day, holiday and break, plus Saturday classes and Anglia exam sessions. Religious holidays are movable and confirmed nearer the date.
→ **Apply** (`forms.html#enrollment`)
→ **Tuition & fees** (`fees.html`)

#### Section: School year 2026–27
Excellence • Integrity • Global Pathways
IMPORTANT DATES
**August 2026**
| Aug 1 to 10 | Overseas book orders. |
|---|---|
| Aug 28 & 31 | Registration Days and teachers’ trainings. Teachers must report. 1 to 4 PM |
**September**
| Sept 7 | First Day of School |
|---|---|
**October**
| Oct 12–18 | Fall Break |
|---|---|
| Oct 31 | Al Wahda Day (Closed) |
**November**
| Nov 6 | Green March Day (Closed) |
|---|---|
| Nov 18 | Independence Day (Closed) |
| Nov 27–28 | Thanksgiving Break |
**December**
| Dec 18 | Jan 3 – Winter Break |
|---|---|
**January 2027**
| Jan 1 | New Year’s Day (Closed) |
|---|---|
| Jan 4 | Staff PD (No School) |
| Jan 5 | Students Return |
| Jan 14 | Amazigh New Year (Closed) |
| Jan 15 | End of 1 Semester |
**February**
| Feb 8–10 | Mid-Winter Break |
|---|---|
| Feb 17 | Global Play Day |
**March**
| Mar 8–14 | Eid Al-Fitr & Break |
|---|---|
**April**
| Apr 19–25 | Spring Break |
|---|---|
(Anglia Exams to be announced.)
**May 2027**
| May 1 | International Labour Day (Closed) |
|---|---|
| May 17–18 | Eid Al-Adha (Closed) |
**June**
| June 5 | Islamic New Year |
|---|---|
| June 17 | Last Day for Students and Graduation! |
| June 30 | Last Day for Staff |

#### Section: Looking ahead: 2027–28
Summer Vacation
**August 2027**
| 9 | Inscription begins |
|---|---|
**September 2027**
| Sept 1 through 3 | Inscription and Teachers report. |
|---|---|
| Sept 6 | School Begins |

#### Section: Saturday Anglia classes
[TO CONFIRM: The 2026–27 Saturday schedule will be published here.] The 2025–26 schedule is below for reference.
- **Q: Saturday classes 2025–26** — A: Anglia Language School Schedule 2025-2026 (October 4, 2025 – June 13, 2026 Class Time: Saturdays from 2:00 PM to 4:00 PM Start Date: October 4, 2025 End Date: June 13, 2026 Weekly Breakdown: Prix 500 DHS/ Monthly with Anglia Exam included in April/May session. The schedule runs every Saturday from the first Saturday in October 2025 until the second Saturday, June 2026. Academic Calendar 2025-2026 This schedule provides a full academic year of Anglia language classes on Saturdays from 2:00 PM to 4:00 PM, accounting for breaks and holidays. Yellow highlighted areas are the days off on the Saturday calendar. October 4, 2025 October 11, 2025 October 18, 2025 October 25, 2025 November 1, 2025 November 8, 2025 November 15, 2025 November 22, 2025 November 29, 2025 December 6, 2025 December 13, 2025 December 20, 2025 Winter Break – December 27, 2025 (No Class) January 3, 2026 January 10, 2026 January 17, 2026 January 24, 2026 January 31, 2026 February 7, 2026 February 14, 2026 February 21, 2026 February 28, 2026 March 7, 2026 March 14, 2026 March 21, 2026 March 28, 2026 April 4, 2026 April 11, 2026 Spring Break – April 18, 2026 (No Class) April 25, 2026 May 2, 2026 May 9, 2026 May 16, 2026 May 23, 2026 May 30, 2026 June 6, 2026 June 13, 2026 (Final Class) Please reach out to us by WhatsApp for questions about the yearly sessions. Please make sure you tell us who you are and what class your child/ children are enrolled in. 212 0688739393.

#### Section: Anglia exam sessions 2026
| Month | Levels / session | Exam days |
|---|---|---|
| January | First Step, Junior Primary | Friday 13th | Saturday 21st |
| January | Preliminary A1, Elementary A2, Pre-Intermediate A2+, Intermediate B1, Advanced B2, Proficiency C1, Masters C2 | Saturday 21st |
| April | All Levels | Thursday 9th | Saturday 18th |
| May | Session 1 | Saturday 16th | Thursday 28th | Saturday 30th |
| May | Session 2 | Thursday 22nd | Saturday 24th |
| May | Session 3 | Saturday 14th |
| June | All levels | Thursday 18th, Saturday 20th, Sunday 21st, Friday 26th, Saturday 27th |
| July | Most Levels | Saturday 4th |
| July | All levels | Saturday 4th | Friday 24th |
| August | All levels | Friday 7th |
| September | All levels | Friday 18th | Saturday 19th |
| September | All levels | Saturday 19th |
| October | All levels | Thursday 15th | Saturday 17th |
| October | All levels | Thursday 15th |
| November | All levels | Thursday 19th | Saturday 21st | Saturday 28th |
| November | All levels | Thursday 19th | Saturday 21st |
| December | All levels | Thursday 10th, Saturday 12th, Thursday 17th, Saturday 19th |
| December | All levels | Saturday 12th |
|  |  | If you need an exam session on an unlisted date, please contact the Anglia office. |
→ **English & Anglia exams** (`english-anglia.html`)
- **Q: Archive: school calendar 2025–26** — A: American Group International of Agadir First Day of Classes- September 8th, 2025 September 2025 September 8th -First Day of Classes September 5 th and 6 th -Eid Al Mouloud – Closed- Moveable Date October 2025 Oct. 20 th – 24 th School closed for Fall Break. November 2025 November 6 th Green March November 18 th Independence Day November 27 and 28 th Thanksgiving Holiday December 2025 December 22 nd Winter Break Starts December 25 th Christmas Day High School Orders Gowns January 2026 January 1 st – New Years- school closed January 5 th School Starts January 14 th Amazigh New Year February 2026 Feb 7 th – Global Play Day Feb 18 th – First Day of Ramadan (Movable) March 2026 March 20 th and 21 st Eid El fir- end of Ramadan (movable) Pick date for Graduation 2026 April 2026 No Days Off Anglia Exams 2026 May 2026 May 1 st – Labor Day May 27, 28, 29 th – Eid al Adha (Movable). June 2026 June 19 th – Last day for Students Teachers need to report after the 19th to close out the year. July 2026 Summer Holidays August 2026 August 25 th, Teachers Reporting and Training. Inscriptions Begin September 7 th School Starts 2026 2025- 2026 Calendar Program Please contact the administration if you have questions about the calendar: americanecoleagadir@gmail.com First Semester Ends- January 15 th, Second Semester Ends- June 15 th
Key dates
- **Registration** — Aug 28 & 31
- **First day** — Sept 7
- **Last day & graduation** — June 17, 2027
→ **Book a visit** (`forms.html#visit`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.40 `cookies.html`

- **Browser title:** Cookies – American Group International, Agadir
- **Meta description:** This website uses no advertising or tracking cookies. What it stores on your device, and which outside services it loads.

Home / Cookies [link: “Home” → `index.html`]
**Page title (H1):** Cookies.
This website does not use advertising or tracking cookies. Here is exactly what it stores and loads. Last updated October 2026.

#### Section: What this site stores on your device
One small setting in your browser's local storage, named agi-story-popup, remembers the date you last saw the "For parents" invitation, so that it is not shown again for 7 days. It contains no personal information and is never sent to us. You can clear it at any time by clearing your browser's site data.

#### Section: Outside services
- Google Fonts – the typefaces are loaded from Google, which receives your browser's standard technical information (such as your IP address).
- Google Maps – the maps on the home and contact pages are loaded from Google only when they appear on your screen; Google may set its own cookies when you use the map.
- WhatsApp – the WhatsApp button opens WhatsApp only when you tap it.

#### Section: No tracking
We do not use analytics, advertising or social-media tracking cookies. If this changes, this page will be updated and your consent asked first where the law requires it.

#### Section: Questions
Write to americanecoleagadir@gmail.com. See also our privacy policy. [link: “privacy policy” → `privacy.html`]

---

### 4.41 `faq.html`

- **Browser title:** Questions & answers – American Group International, Agadir
- **Meta description:** Answers to parents' questions about AGI: admissions, documents, fees, calendar, attendance, homework, Anglia exams, teachers and adult programs.

Home / Questions & answers [link: “Home” → `index.html`]
**Page title (H1):** Questions & answers.
The questions families ask most, with answers taken from AGI's own policies and programs.
→ **Ask another question** (`forms.html#enquiry`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: Admissions
- **Q: Who can enroll at AGI?** — A: Children aged 5 by September 1 (kindergarten) up to students under 21 on the first day of school. AGI admits students of any race, religion, color, national or ethnic origin. Admissions
- **Q: What documents do we need?** — A: Proof of age (birth certificate, passport or similar), proof of residency less than three months old, immunization and physical examination records, two years of previous school records with a behavior report, three recent photos, and transfer papers translated into English. Admissions
- **Q: How does the admissions process work?** — A: 1) Application with the non-refundable enrollment deposit, 2) an interview with parent and child, 3) an offer of admission and the tuition agreement. Admissions
- **Q: Is there an entrance test?** — A: Yes – a free placement assessment in English and academic subjects. Grade placement is not lowered due to missing documents, language gaps, or academic gaps. Placement policy
- **Q: Can my child join in the middle of the year?** — A: Yes. Students are welcome at any stage; they sit the placement assessment and start with the right support. For parents
- **Q: My child doesn't speak English yet. Can they join?** — A: Yes. Students join their age group with English as a second language support and are benchmarked on the CEFR with Anglia exams. Placement policy
- **Q: Do you support children with special needs?** — A: Yes: Individualized Education Plans, small-group classes and therapy and behavioral support. Documentation from a licensed practitioner is required – a parent's description alone is not enough. Special education

#### Section: Fees
- **Q: How much is tuition?** — A: 2,600 MAD a month, paid over ten months (26,000 MAD a year). Tuition & fees
- **Q: How much is the annual inscription?** — A: Kindergarten–grade 1: 6,500 MAD · grades 2–6: 7,500 MAD · grades 7–8: 7,800 MAD · grades 9–11: 10,000 MAD · grade 12: 11,000 MAD. Paid once a year, non-refundable. Tuition & fees
- **Q: What is included?** — A: Books and learning materials, mathematics examinations, Anglia English examinations, enrollment in the USA and Morocco, and student insurance. Tuition & fees
- **Q: Can fees be negotiated?** — A: No. Fees are already set as low as possible to keep AGI inclusive, and discounts are already applied for all families. Tuition & fees
- **Q: Is there a summer school?** — A: Yes, for high school students who need to catch up or enroll late: 3,000 MAD for a one-month program. Tuition & fees
- **Q: Is there a discount for brothers and sisters?** — A: [TO CONFIRM: To be confirmed by the office.] Tuition & fees

#### Section: School life
- **Q: When does the school year start and end?** — A: 2026–27: registration days August 28 and 31, first day September 7, last day and graduation June 17, 2027. Calendar 2026–27
- **Q: What are the school hours?** — A: [TO CONFIRM: To be confirmed by the office.] Arrival after 9:00 counts as late, and after 10:00 as an absence. Attendance policy
- **Q: Is there a uniform?** — A: [TO CONFIRM: No uniform is mentioned; a dress code applies (see the handbook).] Academic handbook
- **Q: What happens if my child is absent?** — A: Give the office a dated, signed excuse within two days. Students need 90% attendance to be promoted; unexcused absences lead to escalating consequences. Attendance policy
- **Q: How is promotion decided?** — A: At least 64% (D) in each core subject, 90% attendance, maturity and the English assessment; summer remediation is possible. Promotion & retention
- **Q: How much homework is there?** — A: From 10–20 minutes a night in kindergarten to 2–3 hours in the last years of high school. Homework guidelines
- **Q: What do high school students need to graduate?** — A: Among other requirements, 40 volunteer hours – ten each year. Volunteer hours
- **Q: What should my child bring?** — A: See the school supplies list for elementary and high school. Supplies list

#### Section: Anglia exams & English
- **Q: What are Anglia exams?** — A: English exams from Anglia Examinations, based in Chichester, England, since 1993 and part of Chichester College Group. They test reading, writing, listening and speaking at ten levels, from First Step to Masters (C2). English & Anglia exams
- **Q: From what age can my child take them?** — A: From about four years old; there is no upper age limit. English & Anglia exams
- **Q: How long are the exams?** — A: Reading and writing 1–3 hours, listening 10–30 minutes, speaking about 5–20 minutes, depending on the level. English & Anglia exams
- **Q: Does the certificate expire?** — A: It is valid for life, though an institution may ask for a recent one. English & Anglia exams
- **Q: When are the exam sessions?** — A: There are sessions in most months – see the 2026 exam sessions on the calendar. Other dates are possible on request. Calendar 2026–27
- **Q: Can candidates with dyslexia or a disability get support?** — A: Yes – for example extra time, supervised breaks, Braille or large print, wheelchair access or a scribe. English & Anglia exams
- **Q: Are Saturday classes available?** — A: Yes: ages 5–18, Saturdays 2–4 pm, October to June, 500 MAD a month including the yearly Anglia exam, with BAC, TOEFL, IELTS, SAT and Mathematics-in-English preparation. English & Anglia exams

#### Section: Teachers & adults
- **Q: What is C.I.T.E.?** — A: Anglia's Certificate for International Teachers of English: a TESOL qualification mapped to the CEFR, with no entry qualifications and lifelong validity. For teachers
- **Q: Can I teach in the United States?** — A: AGI offers certification sponsorship for U.S. private schools: bachelor's degree, clear background check and a sponsoring school; fee US$60. Not valid for public schools. For teachers
- **Q: Can adults finish high school?** — A: Yes, from age 16 with American Worldwide Academy; every test is proctored in Agadir and graduation requires 80%. Adult diploma
- **Q: Do you proctor exams for other institutions?** — A: Yes, Monday to Thursday 9:00–17:00: a 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour. Professional services
Topics
- Admissions [link: “Admissions” → `#admissions`]
- Fees [link: “Fees” → `#fees`]
- School life [link: “School life” → `#school-life`]
- Anglia exams & English [link: “Anglia exams & English” → `#anglia-exams-english`]
- Teachers & adults [link: “Teachers & adults” → `#teachers-adults`]

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.42 `fees.html`

- **Browser title:** Tuition & fees – American Group International, Agadir
- **Meta description:** AGI fees 2026–27: inscription by grade (6,500–11,000 MAD), tuition 2,600 MAD a month, all-inclusive package, high school options, class prices.

Home / Admissions / Tuition & fees [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`]
**Page title (H1):** Tuition & fees.
Clear and simple: one annual inscription, ten monthly payments, and the essentials included. Fees are the same for every family – they are already set as low as possible.
→ **Apply** (`forms.html#enrollment`)
→ **Calendar 2026–27** (`calendar.html`)

#### Section: K–12 school
**Annual inscription (paid once a year at enrollment, non-refundable)**
| Grade | Inscription |
|---|---|
| K–Grade 1 | 6,500 MAD |
| Grades 2–6 | 7,500 MAD |
| Grades 7–8 | 7,800 MAD |
| Grades 9–11 | 10,000 MAD |
| Grade 12 | 11,000 MAD |
| High school – American High School Online (LMS) | US$2,500 |
**Monthly tuition**
2,600 MAD a month, paid over 10 months only – 26,000 MAD for the school year.
**All-inclusive education package**
- Books and learning materials
- Mathematics examinations
- Anglia English examinations
- Enrollment in the USA and Morocco
- Student insurance coverage
**Summer school option (high school)**
For students who need to catch up or enroll late: 3,000 MAD for a one-month summer program.

#### Section: High school options
Option 1 – High School Books Program, grades 9–12 (Florida accredited). All students in grades 9 to 11 take the CAT assessment.
Option 2 – High School Online in school, grades 9–12 (Cognia accredited). Yearly inscription fee US$2,500 paid to a U.S. bank account; tuition 2,600 MAD a month.
Grade 12 students pay a graduation fee, announced later – it may cover the diploma, apostille legalization, gown and shipping.

#### Section: Good to know
- The inscription is annual and non-refundable.
- Tuition is paid monthly over ten months.
- Places are limited – secure your child's place early.
- Fees cannot be negotiated: they are already set as low as possible to keep AGI inclusive, and discounts are already applied for all families.
- A required Anglia English assessment takes place in April.

#### Section: Requirements at enrollment
All children enrolling must have some prior school paperwork and a behaviour report. Children that are considered to have IEPs and other special needs, must have documentation to this. Just a parent saying that they are, is not from a licensed doctor. We have a right to reject students who have not a clear educational pathway. Special accommodations will be made available if needed. All parents much have a valid email, phone and address.
→ **Refunds & complaints policy** (`refunds-complaints.html`)
·
→ **Attendance policy** (`attendance.html`)

#### Section: English & Anglia classes
| Class | Price |
|---|---|
| Saturday classes, ages 5–18 (Saturdays 2–4 pm, October–June, yearly Anglia exam included) | 500 MAD a month |
| One-to-one (English or mathematics) | 200 MAD a session |
| Small group, 2–3 students | 150 MAD per person, per session |
| Group course, 4–10 students, 12 weeks | 100 MAD a week (1,200 MAD) |
| Level test | Free |
Prices effective November 2024. Books and insurance not included.

#### Section: Other programs and services
| Service | Price |
|---|---|
| Exam proctoring | 200 MAD (15 EUR) admin + 200 MAD (15 EUR) per exam hour |
| USA private-school teacher sponsorship | US$60 |
| Holistic play therapy | [TO CONFIRM: 150 MAD per session] |
| Online tutoring (American Group USA) | [TO CONFIRM: US$10 – US$50 per session] |
| Independent course studies (per module) | [TO CONFIRM: US$49.95 / US$79.95] |
Admissions
- How to apply [link: “How to apply” → `admissions.html`]
- Calendar 2026–27 [link: “Calendar 2026–27” → `calendar.html`]
- Policies [link: “Policies” → `policies.html`]
- Payment notice [link: “Payment notice” → `forms.html#payment`]
- Apply [link: “Apply” → `forms.html#enrollment`]

#### Section: Questions about fees?
The office will explain every option for your family.
→ **Apply** (`forms.html#enrollment`)
→ **Ask a question** (`forms.html#enquiry/programs`)

---

### 4.43 `forms.html`

- **Browser title:** Forms & requests – American Group International, Agadir
- **Meta description:** Apply for a place, report an absence, request a document, give consent, book tutoring or tell the AGI office about a payment.

Home / Forms [link: “Home” → `index.html`]
**Page title (H1):** Forms & requests
Apply for a place, report an absence, request a document or tell the office about a payment. Every form explains what to have ready and what happens after you send it.

#### Section: How it works
Choose the request from the list. Each form takes two to five minutes and goes straight to the AGI office in Agadir.
- Choose a form Pick the request that matches what you need. If nothing fits, use the general enquiry.
- Fill it in Every field is required unless it says optional. Your browser can fill in your name and contact details for you.
- The office replies Requests are answered within one working day, Monday to Friday. Urgent? Call or send a WhatsApp message.
**Most used**
Report an absence Apply for a place Payment notice Request a transcript [link: “Report an absence” → `#absence`] [link: “Apply for a place” → `#enrollment`] [link: “Payment notice” → `#payment`] [link: “Request a transcript” → `#documents/transcript`]

---

### 4.44 `handbook.html`

- **Browser title:** Academic handbook – American Group International, Agadir
- **Meta description:** The AGI academic handbook in full: mission, vision, beliefs, school routines, behavior, communication and family partnership.

Home / Admissions / Policies / Academic handbook [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Academic handbook
AGI's mission, vision and beliefs, and the rules and routines that shape every school day – in full.
On this page
- Welcome Letter [link: “Welcome Letter” → `#welcome-letter`]
- Mission, Vision And Beliefs [link: “Mission, Vision And Beliefs” → `#mission-vision-and-beliefs`]
- Mission Statement [link: “Mission Statement” → `#mission-statement`]
- School Vision [link: “School Vision” → `#school-vision`]
- We Believe [link: “We Believe” → `#we-believe`]
- Pedagogy/Theory Of The North American Educational System—- [link: “Pedagogy/Theory Of The North American Educational System—-” → `#pedagogy-theory-of-the-north-american-educational-`]
- Daily Schedule [link: “Daily Schedule” → `#daily-schedule`]
- Communication [link: “Communication” → `#communication`]
- School Contact Information [link: “School Contact Information” → `#school-contact-information`]
- Communicating With Us [link: “Communicating With Us” → `#communicating-with-us`]
- Meetings [link: “Meetings” → `#meetings`]
- How We Communicate [link: “How We Communicate” → `#how-we-communicate`]
- Conduct/Behavioral Expectations/Code Of Conduct [link: “Conduct/Behavioral Expectations/Code Of Conduct” → `#conduct-behavioral-expectations-code-of-conduct`]
- Dress Code [link: “Dress Code” → `#dress-code`]
- General Appearance [link: “General Appearance” → `#general-appearance`]
- Discipline Policy– [link: “Discipline Policy–” → `#discipline-policy`]
- Levels Of Offenses And Levels Of Consequences [link: “Levels Of Offenses And Levels Of Consequences” → `#levels-of-offenses-and-levels-of-consequences`]
- Discipline Committee [link: “Discipline Committee” → `#discipline-committee`]
- Acceptable Use Policy [link: “Acceptable Use Policy” → `#acceptable-use-policy`]
- Electronic Devices [link: “Electronic Devices” → `#electronic-devices`]
- Confiscation And Liability [link: “Confiscation And Liability” → `#confiscation-and-liability`]
- Academics [link: “Academics” → `#academics`]
- Plagiarism [link: “Plagiarism” → `#plagiarism`]
- Cheating [link: “Cheating” → `#cheating`]
- Homework Policy [link: “Homework Policy” → `#homework-policy`]
- Homework Guidelines [link: “Homework Guidelines” → `#homework-guidelines`]
- Tutoring [link: “Tutoring” → `#tutoring`]
- Academic Reinforcement [link: “Academic Reinforcement” → `#academic-reinforcement`]
- Textbooks, Resources & How We Teach [link: “Textbooks, Resources & How We Teach” → `#textbooks-resources-how-we-teach`]
- Grades And Reporting / Report Cards [link: “Grades And Reporting / Report Cards” → `#grades-and-reporting-report-cards`]
- Parent/Teacher Conferences [link: “Parent/Teacher Conferences” → `#parent-teacher-conferences`]
- Student Records [link: “Student Records” → `#student-records`]
- Attendance Is Important….. [link: “Attendance Is Important…..” → `#attendance-is-important`]
- Attendance Policy [link: “Attendance Policy” → `#attendance-policy`]
- Notification Of Absence [link: “Notification Of Absence” → `#notification-of-absence`]
- Make-Up Work [link: “Make-Up Work” → `#make-up-work`]
- Extended Absences [link: “Extended Absences” → `#extended-absences`]
- Tardy For Class [link: “Tardy For Class” → `#tardy-for-class`]
- Early Departure [link: “Early Departure” → `#early-departure`]
- Student Activities And Services [link: “Student Activities And Services” → `#student-activities-and-services`]
- Student Supplies [link: “Student Supplies” → `#student-supplies`]
- Lost Items [link: “Lost Items” → `#lost-items`]
- Health Service [link: “Health Service” → `#health-service`]
- Medication In School [link: “Medication In School” → `#medication-in-school`]
- Sick Children Guidelines [link: “Sick Children Guidelines” → `#sick-children-guidelines`]
- General Policies And Procedures [link: “General Policies And Procedures” → `#general-policies-and-procedures`]
- Promotion/Retention/Accelleration Policy [link: “Promotion/Retention/Accelleration Policy” → `#promotion-retention-accelleration-policy`]
- Promotion [link: “Promotion” → `#promotion`]
- Retention [link: “Retention” → `#retention`]
- Acceleration [link: “Acceleration” → `#acceleration`]
- Class Size [link: “Class Size” → `#class-size`]
- Grade Level Placement [link: “Grade Level Placement” → `#grade-level-placement`]
- Withdrawal From Agi [link: “Withdrawal From Agi” → `#withdrawal-from-agi`]
- Visitors To Agi [link: “Visitors To Agi” → `#visitors-to-agi`]
- Abuse [link: “Abuse” → `#abuse`]
- Snacks And Lunches [link: “Snacks And Lunches” → `#snacks-and-lunches`]
- Arrival & Dismissal [link: “Arrival & Dismissal” → `#arrival-dismissal`]
- Morning Drop-Off [link: “Morning Drop-Off” → `#morning-drop-off`]
- Afternoon Pick-Up [link: “Afternoon Pick-Up” → `#afternoon-pick-up`]
- Safety & Security /In Loco Parentis [link: “Safety & Security /In Loco Parentis” → `#safety-security-in-loco-parentis`]
- Emergency Plans [link: “Emergency Plans” → `#emergency-plans`]
- Use Of School Phone [link: “Use Of School Phone” → `#use-of-school-phone`]

#### Section: Welcome Letter
Welcome to American Group International ***AGI. Our caring and nurturing staff is pleased to have the opportunity to educate your child and we look forward to the new school year with the same hopes and dreams you have for your child. We are eager to challenge all of our students to be successful both academically and socially as we prepare them for their future.
AGI is a child-centered school with an environment that enables students to take responsibility for their learning and behavior. Students are at the center of each decision we make as educators, and we believe that is what makes our school stand out as a school that strives for excellence.
We pride ourselves on our team of highly qualified teachers who bring a wealth of knowledge and skills. We are confident students receive a quality education each day under the guidance of our faculty.
Thank you for choosing American Group [TO CONFIRM: International Correspondence] as your educational Institution.
Julie Wilburn, Director
Email: americanecoleagadir@gmail.com

#### Section: Mission, Vision And Beliefs

#### Section: Mission Statement
AGIs mission is dedicated to serve the Agadir region of Morocco by providing children with a strong educational foundation following American philosophy and practices, so that they become independent, critical thinkers, and caring, contributing members of society. The AGI strives to develop the whole child and therefore, not only do we focus on achieving academic excellence but promote a high level of self-esteem, co-operation with others and creativity. We hold high the value of respect, strongly encouraging respect of oneself, respect of others, as well as respect for the environment.
Paramount to our program is our belief in the family as integral component of the program, and communication between school and home being essential to each child’s success. We offer a safe, caring, engaging environment, where our dedicated team encourages and supports the developing child in their quest for personal growth.

#### Section: School Vision
AGIs aim is to a leader in being a center of excellence in teaching, from pre-school through middle years, empowering children with the knowledge, confidence and ability to pursue successful careers in university and become responsible citizens of the world.

#### Section: We Believe
We are a community of learners-students, faculty, and parents-working together to build a safe, supportive, and challenging environment for educational excellence.
Student opinions and ideas are vital; students are empowered to achieve at their highest potential when they are actively involved and share responsibility for their own learning.
A quality education enables students to make positive life choices in caring for themselves, others, and the environment.
Independence of spirit is essential in exploring, communicating, and defending our beliefs.
Diversity strengthens and enriches the climate and culture of our school; it helps us to recognize and appreciate the unique qualities and contributions of each individual.
Multilingual learning encourages respectful collaboration and leads to better cultural understanding.
In order to grow we must embrace change, take chances, and be challenged by high expectations in a climate where ongoing improvements are valued and achieved.
Education is a life-long process which offers great opportunity while imposing the responsibility of courage, integrity, and ethical conduct.
The learning process is more important than the outcome; knowing how to find an answer or ask a question is often more useful than the answer itself.
Teachers, administrators, and staff will flourish in a community that provides opportunities to grow, develop, and learn together in all aspects of their professional lives.

#### Section: Pedagogy/Theory Of The North American Educational System—-
In the North American education system, students are the first priority; they are partners in the educational experience. Student thinking is valued even when it is flawed, with their errors used as opportunities for educational growth. Teachers, while respected, are not viewed as fully informed experts who transmit their knowledge, but as professionals who facilitate and model cooperative learning. North American education emphasizes learning experiences in which children actively participate, learning by hands-on work and experimentation, solving problems that are real and important to them. The learning process utilizes interactive instruction methods such as discussions, debates, teamwork activities, and community service projects to elicit imaginative thinking, problem solving and decision making toward a goal of meaningful insight. Learning how to learn is key to the students’ ultimate success in life, and the North American education system places great importance on this principle.
As students’ progress, they are given increasing autonomy in the direction of their work, while also discovering how to work cooperatively with others. The ultimate goal is not just to prepare students for the next examination, but to develop the individual and make him or her passionate about learning.
Fees
Places in AGI are for the entire school year, September to June. Parents, guardians or either accepting financial responsibility, are accountable for the full yearly fees of students are withdrawal during the school year. Monthly payments are due on the 5th of each month, with no exceptions. AGI does not have your monthly payment, there is a 150 DH administration cost. Any changes in the method of payment for a student must be submitted in writing. For students enrolled in the school at a time other than September, fees will be prorated as of the first day of the month of enrollment. Inscription fees vary. Discounts for multi-student families.
Elementary 2600 DH monthly
Middle School 2600 DH monthly
High School 2600 DH monthly

#### Section: Daily Schedule
9:00- Arrival
10:30- 11:00- Break/Snack
12:00 – 1:00 – Lunch
3:00 Dismissal
With the exception of Friday then the dismissal time is at 12:00.
Please make sure that your children are picked up on time.
Students are not supervised after 15 minutes when school is dismissed.
School calendar is available on the school website: www.americangroup-international.com

#### Section: Communication

#### Section: School Contact Information
The AGI main office is open 9 a.m. to 3:30 p.m. Monday through Friday and on Saturday by appointment during the school year. The office is also open during the summer, with scheduled appointments except during the months of July and part of August. You may contact the office by mail, phone, or e-mail. All books that need to be brought from the USA should be paid for by June for the next September for high school students.
Mail: Number 20, Rue Baalabek, Cite Nahda, Agadir, Morocco 80000
Phone: +212 (0)528 843 349
E-mail: americanecoleagadir@gmail.com
Website: www.americangroup-international.com/
HOME CONTACT INFORMATION- All information must be up to date and reviewed yearly.
Communication with the school is crucial for your child. Making sure that we do it well is important and every effort is made to make sure that you are informed of what takes place at school. An essential part of this process is having up-to-date information regarding telephone and email. Parents change locations, businesses, internet service providers and telephone numbers and we don’t always hear about it immediately. You cannot assume that your child will tell us. Therefore, we ask that whenever there is change that we are told immediately. The best person to contact is Julie Wilburn, the Admission Manager- Administrator/Director in the main office.
EMERGENCY CONTACT INFORMATION-All information must be up to date and reviewed yearly.
The school also needs to keep updated information regarding emergency contacts for each student. In the event of an emergency we need to be in touch with the parent or designated guardian as quickly as possible. Please ensure that the office has been given names and phone numbers for your child’s emergency contact. If your child’s emergency contact information changes, please contact the office immediately to update our database. Please keep us updated with home, mobile and emergency contact phone numbers. Remember to let us know if you are going to be away from Agadir.

#### Section: Communicating With Us
Teachers know that education is a partnership with parents. They always welcome your communication.

#### Section: Meetings
You are encouraged to call the office to make an appointment with your child’s teacher to discuss any questions or concerns you may have. Of course, during the school day, the teacher’s primary responsibility is the students. In order not to disrupt the learning process in our school, our Director will consult the teacher’s schedule and provide you with an appointment at a time when the teacher has no classroom or supervisory responsibility. We will try to accommodate within 3 working days.

#### Section: How We Communicate
We all want the best for our students. When conflicts or problems arise, we pledge to treat you and your family with respect. We ask that you do the same when dealing with any member of our faculty or staff. Our goal is always to act in the best interest of the child. The school will communicate with you in a number of ways: Often the best and most effective means of communication is talking. Doing so face-to-face is not always easy but usually resolves issues more effectively. If a teacher wishes to speak with you, they will make contact by telephone or email to schedule a conference.
Telephone
Teachers are encouraged to get in touch with you on any important issue that involves your child. They will contact you to discuss your child’s successes and challenges in the classroom.
Email
Teachers may contact you using e-mail. Please provide your email in your child’s file. If your e-mail address changes at any time during the year, it is crucial that we find out as soon as possible to keep the communication channels open. Also, you are encouraged to e-mail teachers or Administrator regarding any issue. We currently use WhatsApp school group as parent/teacher contacts.
Reports
There are two different types of reports for all students, progress reports and semester report cards. Parents should check the student announcements on the website frequently to remain aware of what is happening at AGI.
Program of Studies/Course Syllabus
Teachers will provide information about their classroom schedule.
Announcements
The announcements are posted on the school website as needed.
The application form is now online: apply on the forms page. [link: “apply on the forms page” → `forms.html#enrollment`]
Homework, class assignments Your Child’s Teacher
Student files, records, attendance, health issues Julie Wilburn
Payments Julie Wilburn/Abdelhak Lam
Transport Private drivers are available and freelance with parents.
Admissions Julie Wilburn/Abdelhak Lam-Arabic
Personal Educational Plans Educational Director-Julie Wilburn
Student activities Your Childs Teacher/Director
ES/MS/HS curriculum, grades, discipline Julie Wilburn, Matthew Wilburn,
Language Program for EFL and ESL Julie Wilburn/Anglia Morocco Country Coordinator
Arabic Support Abdelhak Lam
Mental Health Responder and Counselor- Julie Wilburn

#### Section: Conduct/Behavioral Expectations/Code Of Conduct
At AGI, students are expected to meet certain behavioural standards at all times:
Students will respect themselves, others, and belongings.
Students will demonstrate responsibility, both academically and socially.
Students will display honesty and personal integrity.
Students will be generous and responsible citizens.
Students will contribute positively to the school environment.
Students will not be a disruption to the learning of others or display violence to students or teachers.
Students will express themselves in a manner that does not infringe upon the rights of others.
Students will practice tolerance towards differences in culture, gender, race or beliefs.
Students will enrich their language skills be speaking only English in the classroom unless they are doing lessons in their native language.

#### Section: Dress Code
School rules including PE rules, recess rules, and general classroom rules will be distributed to students by the appropriate teachers/staff each school year.
Comfortable environment, conducive to learning and respectful of our host culture. Additionally, we want students to take responsibility for dressing for school while maintaining autonomy. AGI students are expected to be appropriately groomed and dressed throughout the school day. The school expects students to be neat, clean, and modest in their appearance and to present a good image of the school within the community.
Enrollment at The AGI presumes that parents agree to and students will comply with the following Student Dress Code:

#### Section: General Appearance
1- Underclothes should not be visible.
2- Any jewellery deemed by the school to be dangerous or a distraction to the learning environment is not acceptable.
3- All clothing and personal items must be free of impolite or improper messages.
4- Hair should be clean and neat.
5- Clothing must not be ripped, torn, excessively worn or stained. Be free to have your own style.
6- Approved garments must be of a length and fit that are suitable to the build and stature of the student. Hemlines must be conservative.
7- Clothing excessively large or small is unacceptable. Students who come to school in inappropriate clothing will be asked to change.

#### Section: Discipline Policy–
The AGI Discipline Policy is designed to encourage the growth of mature self-discipline within students, while at the same time fostering a positive learning environment at AGI. The following lists provide examples of offenses and their consequences. The lists are not necessarily all-inclusive and, therefore, teachers and the
Administration is not limited in application because an item was not on the list. Repeated occurrence of offenses may result in an escalation in consequences. The teacher, administrator or staff member assigning consequences has the authority to choose the appropriate consequence, guided, but not limited, by the lists below.
Tutoring of students by AGI teachers and trainers are forbidden unless prior permission is received. Some assistants are not qualified to teach subjects. It is also forbidden in Morocco for teachers to give lessons outside of the school with the students they serve. We will not be held responsible if you decide to go against our policy as this will put the teacher or volunteer at danger of losing their position as this means they are using their energies outside of the school and they will not improve in the job performance here.

#### Section: Levels Of Offenses And Levels Of Consequences
- Level 1 Offenses
- Inciting minor disruptions
- Defiance
- Lateness or absence
- Dress code violation
- Lunchroom violation
Eating outside of designated areas or times (lunchroom or courtyard at recess)
Coming to class unprepared
Missing or late homework assignments
Failure to return letters, etc. from home
Level 1 Consequences
Verbal or written warning
Correction of Situation (For example, change clothes for a dress code violation)
Letter of Apology
“Time out” or loss of privilege such as recess, field trip or computer use
Phone call to parents
Detention room (repeated offenses)
Referral
Discipline Committee will meet and choose any combination of consequence deemed appropriate
Level 2 Offenses
Inciting major disruptions
Disrespect to any community member (including obscene language or gestures)
Being “out of bounds” e.g. being anywhere on school grounds without permission
Littering
Possession of a prohibited electronic device; i.e. video game, portable music player during classroom times.
Computer lab violation
Bullying/Hazing/Intimidation
Level 2 Consequences
Write “reflection paper” or apology letter
Detention
Clean-up/School improvement
Special Assignment
Confiscation of items
Restitution or replacement of damaged or taken property
Receive zero/no credit on assignment
Detention room
In-school suspension
Discipline Committee will meet and choose any combination of consequences deemed appropriate.
Level 3 Offenses
Willful disobedience/insubordination
Vandalism (damage to or destruction of school property or property of a community member)
Verbal abuse
Theft
Forgery/Falsifying documents
Threats to a community member
Not informing/Conspiracy
Leaving school grounds without school’s permission
Failure to attend detention or meeting with teacher, etc.
Cheating/Plagiarism
Taking items that belong to another community member without permission
Level 3 Consequences
Parent conference
Present “reflection paper” or apology letter to school community
Restitution or replacement of damaged or stolen property
Off-campus suspension (No credit for missed assignments will be given)*
Discipline Committee will meet and choose any combination of
consequences deemed appropriate
Level 4 Offenses
Endangering the physical safety of others (Fighting, horseplay, etc.)
Tobacco/Alcohol/Drugs (Including unauthorized medication)
Weapons or harmful products
Level 4 Consequences
Notification of civil authorities (i.e. police)*
Expulsion*
If a student has been inappropriate, a teacher or staff member may assign the student to detention during lunchtime or after school.

#### Section: Discipline Committee
In cases of serious or repeated offenses, the Parent Liaison, or Head of School will convene a committee to hear the complaint brought against the offending student. AGI school administration reserves the right to make decisions unique to each situation, and they shall have the final say on all student consequences.
AGI is not responsible for any damage, theft, or loss of any personal electronic devices a student brings to school, including items confiscated.
AGI policy is to keep students in a learning environment when possible. If it becomes necessary to remove a student from the classroom due to major disruptions, s/he may be placed in in-school suspension. The student will be supervised in a solitary environment for the prescribed period of time. The student will be required to complete his/her normal assignments. The student will receive no credit for classroom or participation grades, and the discipline committee may determine if the student will be allowed credit for written work.

#### Section: Acceptable Use Policy

#### Section: Electronic Devices
Mobile phones are not allowed in use – Students are discouraged from bringing mobile phones to school. They must remain in the office and not of use in the building. Mobile phones may be used in the morning, during lunchtime, and after the dismissal outside of the school building. At these times, talking, texting, game applications, music (with headphones), and internet are permitted, while taking photos with one’s mobile is prohibited unless you have another permission.
Laptops – Students may bring laptops or other devices that aid in schoolwork-related tasks clearly in keeping with the schools educational mission. However, these devices must be pre-approved by each classroom. Each student cannot let another student use the PC device.
Teacher for use in his/her classroom. When a student exits the school, use of the electronic device is not supervised or monitored by AGI staff. The student is responsible for the content. Parents should know what their children are bringing to school, and share responsibility for those decisions.
AGI is not responsible for the permission given to students to leave the building during break and lunch. We forbidden children in Grade 4 and under to go outside for any activities unsupervised.

#### Section: Confiscation And Liability
PLAGIARISM IS CHEATING! Students caught cheating at AGI will receive a mark of 0 (zero)!

#### Section: Academics

#### Section: Plagiarism
Plagiarism occurs when a student presents another person’s work as his or her own. This includes copying in part or whole from any source, without acknowledgment of authorship. Plagiarizing someone else’s ideas is perceived as stealing their intellectual property. Whether it is intentional or not, it is taken as a serious matter in any educational institution. To avoid plagiarism, make sure you acknowledge the source of any material you use which belongs to someone else. Your teachers will show you how to do this. As a guide, follow these three rules:
Exact words from a source must be put in quotation marks and the source acknowledged.
Even if you reword a passage, you must give credit to the source.
Even if you summarize a passage, you must give credit to the source.
The intention is to acknowledge your use of ideas originating with someone else. The penalty for plagiarism at AGI is a mark of O (zero) for the offending assignment and possible referral to Administration for further disciplinary action, including possible Academic Probation or Suspension. The teacher concerned, or Administration will also notify parents.

#### Section: Cheating
Cheating means gaining an unfair advantage in academic work. This implies using deceit or dishonesty in any way, so that the work handed in is not entirely the student’s own. Cheating also involves violating the rules set down for the task by the teacher and the AGI Behaviour Expectations. The penalty for cheating is a zero mark for the task, and possible referral to the Administration for further disciplinary action, including Academic Probation or suspension. If more than one person is intentionally involved in the cheating, the same penalty will apply to all.

#### Section: Homework Policy
AGI maintains that the purpose and benefits of homework are to:
Reinforce the educational lessons being taught in school by providing practice and review.
Reinforce the behavioural/social skills that students are learning by teaching students responsibility, organization, and time management skills.
Provide opportunities for extensions of learning and creativity.
Help parents to understand and be involved in their student’s learning.

#### Section: Homework Guidelines
The following guidelines help parents and students understand the AVERAGE amount of time a student typically might spend on homework:
Grades 1 to 2– 30 minutes
Grades 3 to 4– 40 minutes
Grades 5– 1 hour
**Home Work**
Students are responsible for completing all assignments given to them by their teacher. Some students who process information at a slower rate will need more time to complete their homework; others will need less. The time frame above is meant to be an average guideline for an average student on an average day. Study time before tests, exams and project due dates is bound to increase. Tests given will be expected to be taken if the student does not have a doctors note. Teachers do have the decision to let them take the test a second time. Please know that a child sick without a note is considered a personal day.

#### Section: Tutoring
AGI faculty members offer private tutoring to students who need additional support. If you would like to arrange private tutoring sessions, contact the AGI main office. We do not allow our staff to teach the students inside their private homes and this will result in the employee losing their position.

#### Section: Academic Reinforcement
Teachers can be asked to work during recess times if a parent requests or if the Lead Teacher feels that the child needs extra help.

#### Section: Textbooks, Resources & How We Teach
Gone are the days when a teacher begins a course by studying page 1 of a textbook and progresses through to page 300. Today’s teachers have more resources at their fingertips than ever before.
Current teaching methods utilize not only textbooks but also video media, newspapers, websites, etc. Teachers are required to follow the school curriculum and teach to standards and benchmarks for the appropriate great level. How they reach that goal is where teaching becomes art. The modern teacher has been trained to use a great variety of resources, and when planning his/her lessons, a great teacher will combine several resources to meet the needs of the students.

#### Section: Grades And Reporting / Report Cards
At the end of each academic quarter, report cards are available to monitor the achievement of students as they move toward the semester grade. These reports contain a grade, as well as a comment from each of your child’s teachers. Grades from semesters1 & 2 are averaged to produce semester grades. These grades are the result of a complete semester’s work. They represent a student’s achievement when measured against the outcomes specified for each course. Progress Reports can be given 2 times yearly only if the Educational Supervisor approves.

#### Section: Parent/Teacher Conferences
Parent-Teacher conferences are held at the end of quarter 1 and 3. Report cards will be published and distributed at conferences. Parents are expected to attend Parent Teacher Conference but we do request that you reach out to us to set up the appointed time, to speak personally with each teacher to understand your child’s progress. Parents must ask to schedule these conferences as many in the past do not attend when we schedule. So, you must show an interest.

#### Section: Student Records
Student records are kept in the AGI main office. A student’s permanent file includes all documentation regarding that student and his/her history at AGI, including grades. Parents may review their child’s school records at the school.
Please give the school office 72 hours’ notice to allow sufficient time to make the records available.

#### Section: Attendance Is Important…..

#### Section: Attendance Policy
At AGI, we believe that each student’s regular attendance of 180 days is essential to ensure academic achievement. A student should be absent from school only when it is absolutely unavoidable. If your child is going to be absent or if diagnosed with a communicable disease, please call the school office. Each student/parent will fill out an absence form when absent.

#### Section: Notification Of Absence
Parents should notify the school of pre-arranged absences. If a student is absent from classes for more than two days, teachers may notify the AGI main office. If no advance notification has been received, the school receptionist will phone home to confirm the reason for the absence. Parents need to phone the school office by 9:00am if their child is absent for sickness.

#### Section: Make-Up Work
If a student is absent for any reason, it is the responsibility of the middle year student or elementary parent to meet with teachers to determine what missed work needs to be completed. There is no guarantee that a student will be allowed to make up the same assignments that s/he missed. Teachers may set the policy in their individual classroom according to what assignments or quizzes are to be repeated. Missing work may result in a score of zero for the missed assignments. If make-up work is allowed, a student may be allowed an amount of time equal to the number of days absent to submit missed work (e.g. a student who is absent three (3) days will be allowed three (3) days from the day of return to school to submit make-up work). If a student is allowed to make up a test or quiz, it should be made up on the day of his/her return to school. No student work is accepted after 4th quarter grades are due to the Office.

#### Section: Extended Absences
Parents are strongly discouraged from taking their children out of school for extended vacations. These days will be included in the total number of absences. If an extended leave is essential, parents should notify the school as soon as possible. Students and parents are responsible for communicating with the student’s teachers about any assignments that may be prepared in advance or made up upon the student’s return.

#### Section: Tardy For Class
It is the responsibility of all AGI students to get to class in a prompt and prepared manner.

#### Section: Early Departure
Any student who leaves the AGI campus before the 3:00 dismissal must be signed out by a parent in the AGI main office. Students who leave school early (before 12:30 p.m.) will be counted for a half-day of attendance.

#### Section: Student Activities And Services
**INDIVIDUAL EDUCATION PLANS (IEPs)**
AGI recognizes that each student has individual academic and social needs. When it becomes necessary to address the student’s individual needs, programs for modification and advancement are completed.

#### Section: Student Supplies
It is essential that each student be prepared with all materials needed for responsible classroom learning. At the beginning of each school year, students or parents may obtain grade level supply lists from the AGI website. Each student should bring his/her complete supply packet on the first day of school. Parents may purchase supplies from any store of their choice or the school will charge supply fees.

#### Section: Lost Items
All found items are to be turned into the AGI main office. Students or staff members who have lost items should report the loss to the receptionist as soon as possible after the realization that the item is missing. Administrative personnel will check to see if the item has been turned in to the lost and found AGI is not responsible for lost or stolen items; however, every effort will be made to help recover the article. Students are encouraged not to bring valuables to school. All items brought to school should be clearly marked with the student’s name for easy identification. Students should bring money to school only when necessary. Losses should be reported to the office immediately.

#### Section: Health Service
Only prescription lifesaving medication will be administered. Parents must have a completed medication form stating dosage, time and have signed an Authorization form for Administration of Medicine. The medicine must be in the original container with the prescription clearly printed. This form is available from the Administration Office.
All medicine, as well as basic first aid care, is dispensed in the main office by the Admissions Manager. If a more serious injury occurs, then the school will notify the parents immediately and transport the student to a local medical clinic for further evaluation and treatment. Students are automatically taken to the closest clinic. The school keeps a record of all treatment administered at AGI and the Admission Manager- Administrator is in charge of maintaining up-to-date records on each student’s immunizations and medical situations. If a student’s permanent file is missing any medical information, the Admission Manager- Administrator will contact the student’s parents to request updated information. In the event of an accident serious enough for a student to be sent to the office, the following procedures will be followed. The office staff will inform the parents of an accident or injury to their child upon…
The request of the child.
The need to seek outside medical attention.
The presence of blood, broken skin or significant bruising.
Any possible injury to the head, neck or spine.
Any other incident where it is in the opinion of the office staff that the injury is serious enough to have the parents or guardian informed.

#### Section: Medication In School
The Admission Manager stores and administers ALL medications required by students. The Admission Manager will administer some over-the-counter medications (i.e. Tylenol/Panadol, ibuprofen, cough syrup, Tums, throat lozenges) if we have parental permission on file. We are very concerned about your child’s safety and health. If your child requires other medication, we request that you bring the medication to the AGI main office yourself.

#### Section: Sick Children Guidelines
Children should remain at home if any of these conditions appear:
Fever 38.5 degrees.
Respiratory Symptoms: difficult or rapid breathing or severe coughing.
Vomiting: One episode of vomiting within the 24 hours.
Diarrhea: An increased number or abnormally loose stools in the previous 24 hours or three or more loose stools pre day without obvious dietary, drug, or medical cause.
Eye/Nose Drainage: Thick mucus or pus drainage from an eye or nose.
Sore Throat: sore throat especially when other symptoms such as fever or visibly swollen glands in the neck are present.
Skin Problems: Rashes which are undiagnosed or contagious sores.
Itching: Persistent itching or scratching of body or scalp.
Appearance/Behavior: Child looks or acts differently; usually tired, pale, lacking appetite, confused, irritable, or difficulty staying awake.
Usual color: eyes or skin-yellow; stool-grey or white
Mental Instability- Any child displaying mental issues or threatening to do harm to themselves or others shall be removed from school and immediately requested to have an official paper from a doctor to be back in school. This is an environment that we want all children to study without judgment and stigma and think of it as an illness that should be taken seriously for all.
If staff notices any of these symptoms during the day, parents will be contacted to pick up their child immediately. Please ensure an emergency number is available for your child. Please contact us if any of your contact numbers have changed.

#### Section: General Policies And Procedures

#### Section: Promotion/Retention/Accelleration Policy
AGI recognizes that each student develops socially, emotionally, and intellectually at a rate unique to that student and that each student must be afforded the opportunity to progress continually through school in environments that meet their individual needs. AGI will use the following guidelines to assure that students are placed in the academic environment best suited to their needs and abilities.

#### Section: Promotion
Grading and evaluation ensure the proper monitoring of the academic progress of students. Classroom teachers will recommend for promotion students who successfully complete the academic program approved by AGI for the grade in which the student is placed. The principal will consider this recommendation along with the student’s attendance.

#### Section: Retention
Students may be retained if they demonstrate inability to be successful at the next level and/or when an additional year at the same level is likely to produce a beneficial result academically, socially and emotionally, as determined by the Head of School. When a student struggles to meet grade-level standards, AGI faculty, students, and parents/guardians will work together to customize support services to help the student succeed. Retention will be considered as a last resort and will take place only after very careful consideration and implementation of a retention intervention plan. A student who has been retained once in elementary or middle school and has been recommended for a second retention may be asked not to return to AGI for the following year. At the elementary and middle school levels, the decision to retain a student shall be made by the Head of School, in consultation with appropriate faculty members and parents/guardians. No student shall be promoted to the next grade level based upon age or any other social reason unrelated to academic performance. The promotion standards and retention criteria apply to all regular education students. However, in every case, the principal shall make the final determination regarding the promotion or retention of students in accordance with AGI policy. It is the intent of AGI to provide parents with timely information regarding the possible retention of their child through conferences, phone conversations, and/or written notices (such as report cards, special reports, etc.). Decisions will be made in the best interest of the child and not solely on grades or test scores.
Regular Parent – Teacher conferences are scheduled with requests of the parent or guardian. They may be cancelled if the parents do not show an interest. Additionally, parents or teachers may request a conference at any time to discuss student progress. Head of School will maintain a list of students to be considered for possible retention. This list will be updated after each grading period and notification will be sent to parents at the end of the second, and fourth quarters regarding possible retention. A letter indicating retention of the student will be sent to parents at the end of the fourth grading period. Included in the letter will be information regarding any available summer school option. Promotion or retention will also be indicated on the student’s semester 2 report cards.

#### Section: Acceleration
In truly exceptional circumstances, where a student’s academic, social and emotional development are all significantly beyond the performance of his or her classmates, AGI may consider the acceleration of a student beyond what would be considered the age appropriate grade. Acceleration will only be considered when enrichment activities to challenge the student are insufficient. The Head of School will consult with parents, teachers and other relevant faculty before making such a recommendation.
In the case of considering any student for promotion, the following criteria will be considered in addition to academic performance:
English language skills of the child.
Social maturity of the child.
Emotional maturity of the child.
Physical development of the child.
Attendance patterns of the child.
Health of the child and absences from school due to illness.
Family support.

#### Section: Class Size
Class size is limited to 20 or less. Only under exceptional circumstances will this number exceed the limit (for example, a student who must repeat or the arrival of a student who has priority acceptance due to agreements with international embassies). The AGI Committee will make the final decision. Should we receive an application for entry to a class which is already full, we will place the child’s name on the waiting list for that class, providing the registration fee has been paid. In the event enrollment at any grade level reaches its capacity, AGI will maintain a waiting list. Any places that become available will be allocated according to the criteria of the priority of admission.

#### Section: Grade Level Placement
AGI believes it is important to ensure children are placed in classes along with their same-age peers, especially at elementary grade levels. Admission and placement decisions are made by the Admissions Committee. The following details are considered:
The student’s age at the time of enrollment.
Academic history.
Results on entrance screening, particularly writing samples.
Space availability in the appropriate grade level.
Level of English language ability in relation to the demands of the grade level for which the student is applying.
Age is the first criterion considered for the placement of students at any grade level. Age will be verified by the child’s original passport or birth certificate. Children should meet the following age requirements to be eligible for our classes:
Grade k 5 years old on or before September 1
1st Grade- 6 years old on or before September 1
Plus one year of age for each additional grade level. Older students who enter AGI from another American style school will normally be placed in the appropriate grade level consistent with the level from the previous school; however, exceptions may be made when it is determined that the student may benefit from placement in a different grade level. Prospective students who have not been in a school prior to acceptance into AGI will be initially placed according to their birth date. After evaluation and observation by AGI administrators and teachers, the child may be moved to a higher or lower grade, as appropriate.

#### Section: Withdrawal From Agi
Whenever a student leaves AGI, the parent must complete a withdrawal form that can be obtained from the AGI main office. At the time of withdrawal, all tuition and fees must be paid, any educational Items that belong to AGI must be returned, and lost/damaged Items must be reimbursed. A student’s grade reports and records will be held until all school items are returned/all fees are paid. If a student officially withdraws from AGI, s/he will be considered as a new student if and when s/he returns to the school. This may include the requirement to sit an admissions exam and complete a new application form. The student’s academic and social history at AGI will be considered in this instance. If a student has been absent from school for two consecutive weeks without notice given or contact with the school, the student may be administratively withdrawn from the school roster.

#### Section: Visitors To Agi
In order to ensure students’ safety, and that AGI’s educational processes and other school operations are consistently optimized, parents and visitors to the school must check in at the main office. Parents and visitors are NOT permitted to enter the school building or go to classrooms without prior authorization from the Head of School or Admission Manager. Parents are always welcome to visit classrooms with an administrator. Simply phone the office to make an appointment. The requirement to check in with the office does not apply when parents and visitors are attending, by invitation, an assembly or other school program or when parents are attending activities clearly for the purpose of parent involvement such as an open house or parent-teacher conferences. AGI students, teachers, and staff are not allowed to bring family members or other guests to campus without prior approval from the Head of School.

#### Section: Abuse
AGI is fully committed to protecting the dignity and rights of our students and staff. Abuse in form is against everything we stand for and will not be tolerated. Abuse is in the form of Emotional, Mentally and Physically.

#### Section: Snacks And Lunches
In order to fuel them for a productive learning day, students should eat a healthy breakfast before arriving at AGI, and a healthy lunch here on campus. Students should not have carbonated beverages (soda). They should bring healthy snacks/lunches instead of chocolate, candy, chips, or fast food. The lunch should be of a nutritional value from each of the four food groups. All students may eat a snack during their morning break and all students have a lunch break during their daily schedule. Students must bring a snack or lunch to school with them at the beginning of the day.

#### Section: Arrival & Dismissal

#### Section: Morning Drop-Off
Parents and drivers are asked to drop students off in the morning by 8:55. To facilitate a smooth arrival process and to show respect to all parties involved, please do not park your car in front of the school. We need to keep the traffic flowing for the safety of our children. The school day begins at 9.

#### Section: Afternoon Pick-Up
Promptness in a child’s life is very important. Lateness can set patterns for life that care difficult to break. School age children should be picked up at 3:00 p.m. and for the other programs the children should be picked up promptly to avoid paying a late pick up fee after the first 30 minutes, After 15 minutes there is a late fee of 20 DH per each additional 15 minutes. We are all human and circumstances arise, please try to do your best to adhere to times. If you are going to be away from your place work for the day, be sure to leave a phone number where you can be reached in case you are needed for a medical emergency. Told to staff when dropping your child off call the school at ….or cell…….
Parents of students are asked to wait until the security/staff has retrieved your student remain in the waiting area until their child exits the building… Only parents/guardians or designated drivers are allowed to pick up students. If you wish to have another individual pick up your child, it is the parent’s responsibility to inform the office of this in advance students may not go home with other students without permission from both parents given to the AGI office. This is enforced for the safety of your child.

#### Section: Safety & Security /In Loco Parentis
In loco parentis is a Latin phrase that means “in place of parents.” When a student enters the door of AGI, the teachers and administrators are in loco parentis. This means we are the temporary parental figure for your child, and we will care for children as parents during the school day as best we see fit. In any emergency situation, students must remain with school officials until the Head of School determines that the situation is secure enough to dismiss students to their parents.

#### Section: Emergency Plans
Throughout each year, students could be involved in drills and practice situations for various emergency plans such as fire drills and site evacuations.

#### Section: Use Of School Phone
Students will be permitted to use the school office phone during the day in the case of emergency only. Students must have permission from an administrator in order to make a personal call. This Handbook can be updated when found to benefit the AGI and the protection of our students and faculty.
Updated January 17, 2024
© 2024 American Group International School.
Text as published by AGI. Please check with the office for the current version. Source: “AGI Mission Statement and Academic Handbook” (former AGI website)
All policies
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.45 `homework.html`

- **Browser title:** Homework – American Group International, Agadir
- **Meta description:** AGI homework guidelines: how many minutes of homework to expect each night, by grade, from kindergarten to grade 12.

Home / Admissions / Policies / Homework [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Homework
How much homework to expect at each grade, and how families can help.
Creating a nightly average homework schedule can help ensure students balance their academic responsibilities with other activities. Here’s a suggested schedule by grade levels:
Elementary School (Grades K-5)
– Kindergarten to Grade 1:
– 10-20 minutes
– Activities: Reading with parents, simple math exercises, basic writing practice.
– Grades 2-3:
– 20-30 minutes
– Activities: Reading, spelling practice, basic math problems, short writing assignments.
– Grades 4-5:
– 30-60 minutes
– Activities: Reading, spelling/vocabulary practice, math exercises, small projects, introductory science/social studies tasks.
Middle School (Grades 6-8)
– Grade 6:
– 60-70 minutes
– Subjects: Reading, math, science, social studies, language arts.
– Grade 7:
– 70-80 minutes
– Subjects: Reading, math, science, social studies, language arts, introductory foreign language.
– Grade 8:
– 80-90 minutes
– Subjects: Reading, math, science, social studies, language arts, foreign language, project work.
High School (Grades 9-12)
– Grades 9-10:
– 90-120 minutes
– Subjects: English, math, science, social studies, foreign language, electives.
– Grades 11-12:
– 120-180 minutes
– Subjects: English, math, science, social studies, foreign language, advanced placement (AP) or international baccalaureate (IB) courses, college prep activities.
Key Considerations:
- Consistency: Encourage a regular homework routine.
- Breaks: Integrate short breaks to maintain focus.
- Prioritization: Start with the most challenging or important assignments.
- Organization: Use planners or digital tools to track assignments and deadlines.
- Balance: Ensure time for extracurricular activities, family, and relaxation.
- Environment**: Create a quiet, well-lit space for homework.
Adjustments may be needed based on individual student needs, school requirements, and specific assignments. This schedule serves as a general guideline to help manage and balance students’ academic workloads.
Text as published by AGI. Please check with the office for the current version. Source: “Homework Guidelines Policy AGI” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.46 `media-policy.html`

- **Browser title:** Media – American Group International, Agadir
- **Meta description:** AGI media policy: photos, video and live streams, consent for students under 18.

Home / Admissions / Policies / Media [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Media
How photos, video and live streams of school events are used – always with consent and safeguarding first.

#### Section: Media Policy
The purpose of this policy is to define the use of media at American Group International, including but not exclusively for American Group International School.
By using the term ‘media’, we are covering the following:
- Photographs
- Videos
- Live streaming
and how they might be used.
American Group International may take photographs and/or videos of gatherings and events to present them to the rest of the world, primarily on our website or social media sites. Some images may be used in printed materials, displays or promotional videos.
We are acutely aware of the safety and sensitivity of those involved and therefore have put this policy in place to govern media use at American Group International. No commercial photography will be permitted without prior permission of the Senior CEO and/or the Operations coordinator or in their absence an officer or member of the school board.
The types of media collected, may include:
- General group or crowd photographs or videos
- Individual adult or small group photographs or videos
- Individual or small group photographs of children and young people
American Group International reserves the right to take photographs and video recordings at gatherings or any other school/academy related activities in which individuals are not prominently featured and no identifying information is presented. We also reserve the right to use any of these photographs or recordings for promotional purposes in media such as, but not limited to, booklets, flyers, websites, and social media, without seeking or requiring the consent of each person represented.
In addition to an event or gathering taking place on school property, school-related activities also include gatherings at other locations such as parks, educational sites, sporting events etc. and external venues such as class trips.
Any individual who objects to potentially being photographed or videoed as part of American Group International should make their wishes known at the earliest opportunity, such as during inscription of the schools’ services on arrival. We still cannot be held accountable if it was something out of the school’s control.
Any individual who sees themselves, or a member of their family, in a group photograph online and would like it removed, may follow the photo removal procedure outlined below.
Individual adults or small group photographs or videos
When individual adults or small groups of individuals are captured in photograph or video, whether posed or candid, each person will be asked for either written or verbal consent before any use of the material is made. Verbal consent will be deemed sufficient to use an individual adults or small group image that
contains no identifying information. Written consent will be obtained for any images that contain any identifying information.
Photographing children & young people
When those under the age of 18 attend one of our children’s or young people’s groups, whether as part of our main school gathering or another event, at least one parent/guardian will be asked to complete a registration form for each child in their care. This registration will include permissions for media use.
A Looked After Child, vulnerable child or adult should not be photographed (except as part of a general group or crowd as outlined above). In this instance, those with parental responsibility must make known to group/event leaders that this is the case.
In addition, the following guidelines will be enforced:
- Under no circumstances will any identifying information (first or last name, family members, email addresses, school names) of anyone under 18 years of age be included in or associated with any photographs displayed, posted or published in any way.
- All registration forms for events, activities or programs, whether on or off our main site, will contain a reference to this policy and provide a clear opportunity for parents to opt-in to media permissions.
- Separate registration forms will be required for events away from our main gatherings (e.g. Holiday Club, Youth Club etc.) Forms for specific events cover that event only. Registration forms will be reissued annually for re-occurring events or gatherings (usually in-line with school academic years).
- American Group International will make every effort to exclude any child or young person who has been ‘opted-out’ from media inclusion. However, parents/guardians should note that children may still be included in general groups or crowd photographs and videos without identifying information, as explained However, any parent/guardian may request that any photo be removed from display or withdraw their child/young person from any photograph or video at the point it is taken.
- Parents/guardians associated directly with the school can amend permission settings via written communications at any time. The form will be available to parents in the office.
Requesting removal of a photograph or video
Any individual who appears in a photograph/video (or whose minor appears) that has been posted online may request that it be removed for any reason, even if prior permission has been granted.
The request should be made in writing to the Administration Office (either as a written note or email), stating the person(s) involved and the photograph or video in question. It will then be removed promptly from the website and/or social media platforms it had been posted to. However, American Group International cannot be held responsible for existing screenshots, copies of postings made of photographs and videos by others within the school and/or the general public.
**Our Media Team**
American Group International Media Team incorporates those with responsibility for taking photographs and videos, storing and uploading images to our website and social media platforms. This team will be both employees of American Group International and volunteers approved by leadership from time to time.
**Storage of Images**
Images and videos will be stored on equipment belonging to American Group International or within their management and control. These devices are secure, password protected and can only be accessed by those with authorized permissions.
Updates & reviews
This policy will be reviewed regularly, and American Group International may update the content of this policy without notice. Where any change greatly impacts individuals or groups of people, we will make every effort to communicate that to those affected.
American Group International, June 21, 2024
Text as published by AGI. Please check with the office for the current version. Source: “Media Policy” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.47 `online-tutoring.html`

- **Browser title:** Online tutoring – American Group International, Agadir
- **Meta description:** Online tutoring with American Group USA: session prices, how long a session should last, and Zoom/Teams instructions.

Home / Programs / Online tutoring [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Online tutoring
One-to-one lessons online through American Group USA LLC – prices, session length and how to join on Zoom or Teams.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: In detail
Depending on who you ask, the word “tutoring” could mean a multitude of things. For some, it’s a quick bit of homework help. For others, it’s an every-other-day support system and confidence booster. If you’re just getting started with tutoring, it’s tough to figure out which approach is best. So, how long should a tutoring session last, and how many sessions should you schedule?
It’s no wonder why this is one oof our frequently asked questions!To put it plainly, it depends. Every student is different and has different needs. For those with a greater attention span, you can get away with longer sessions. Longer is not always better though, and some students get more value out of shorter sessions.

#### Section: Based on Age, How Long Should Tutoring Sessions Be?
When kids are younger, they tend to get distracted more easily. Asking them to sit down for any period feels like a lot, so shorter sessions suit them better. Conversely, older students can usually handle working for longer periods of time.
A tutoring session should be no shorter than 45 minutes. Less than that isn’t enough time for students to gain new information and internalize it. This is especially true if tutoring is only happening once a week. If your student can’t stay focused for more than 45 minutes, consider having tutoring sessions twice per week.
As your child gets older, you can stretch the tutoring sessions to get more accomplished in a day. This is great if you have a busy schedule because you can have one fully dedicated tutoring day each week. It’s not unheard of to have a three-hour tutoring session, but two hours is usually a good upper limit. Extending it too long can sometimes do more harm than good.
For a general guideline, we’ve created an age-based chart to help you get started.
| Grade Level | Session Length | Sessions Per Week |
|---|---|---|
| K to 5 | 45 minutes to 1 hour | 1 to 2 |
| 6 to 9 | 1 to 1.5 hours | 1 to 3 |
| 10 to 12 | 1 to 2 hours | — |
**Traditional Schooling vs Homeschooling**
The nature of tutoring will vary depending on whether your child is attending brick-and-mortar school. Make sure you take this into account when scheduling your tutoring sessions. Should they be online or in person.
**Traditional Schooling**
Students attending traditional school can greatly benefit from the extra support a tutor provides. A one-hour session once per week is a solid start, but you might want to supplement that with an additional session for best results.
Homeschooling
If you’re homeschooling your child, especially if they’re in high school, you’ll want to provide more tutoring time. Consider scheduling at least two sessions per week, both anywhere from one to two hours each. This will ensure that your student receives the assistance they need.
Tutors can function as teachers, so you can ask them to teach your child’s curriculum. Make sure you allocate enough time to accomplish the goals you would like your tutor to achieve. To simulate a school environment, you can experiment with longer sessions divided by short breaks to improve engagement. Two-hour or even three-hour sessions work well in this case.
**Choose a Productive Time of Day**
It’s important to determine how long a tutoring session should last, but you want to make sure the session is during a productive time of day. Conducting a session too late could lead to your child fatiguing and losing interest. If the session is too early, they might not be fully awake yet.
Tutoring sessions immediately after school tend to be quite effective. The child will not have settled into the away-from-school mindset just yet, leading to higher levels of focus.
If you’re homeschooling, sessions in the late morning and early afternoon can maximize your child’s accomplishments. These are peak hours for productivity, giving your student a head-start on success.
**Ask Your Child How Long Should a Tutoring Session Last**
Ultimately, your child is the one receiving the tutoring, so they should have a say in the matter. Check in with them to see what they would like and use that information to plan accordingly. Also, try different times of day to see what works best for them.
**Consult Your Tutor**
Your tutor will get to know your child quite well, and they’ll be able to provide useful information about your child’s habits. Ask for progress reports to see if anything can be adjusted. They’ll let you know if they’re spending too much time trying to keep a lid on things during a long session or if they often wish for more time during shorter ones. Communication is key!
**We Can Help You Decide How Long a Tutoring Session Should Last**
Thank you for your interest in our Tutor’s.
Online Applications for Class Instructions for Students and Parents
Downloading and Accessing Zoom
- Download Zoom:
– For Computers: Go to the Zoom website zoom.us/download and click on “Download” under “Zoom Client for Meetings.” [link: “zoom.us/download” → `https://zoom.us/download`]
– For Mobile Devices: Search for “Zoom Cloud Meetings” in the App Store (iOS) or Google Play Store (Android) and install the app.
- Creating an Account:
– Open the Zoom application.
– Click “Sign Up” and follow the prompts to create an account using your email address.
- Joining a Meeting:
– Open the Zoom application and sign in.
– Click “Join a Meeting.”
– Enter the Meeting ID and password provided by the teacher.
Downloading and Accessing Microsoft Teams
- Download Microsoft Teams:
– For Computers: Go to the Microsoft Teams website teams.microsoft.com/downloads and click “Download for desktop.” [link: “teams.microsoft.com/downloads” → `https://teams.microsoft.com/downloads`]
– For Mobile Devices: Search for “Microsoft Teams” in the App Store (iOS) or Google Play Store (Android) and install the app.
– Open the Microsoft Teams application.
– Sign in using your Microsoft account. If you don’t have one, click “Sign Up” and follow the prompts to create an account.
– Open the Microsoft Teams application and sign in.
– Click on “Calendar” in the side menu.
– Click “Join” next to the scheduled meeting.
Instructions for Teachers
Scheduling Zoom Meetings
- Sign in to Zoom:
– Open the Zoom application or go to [ zoom.us ]( zoom.us) and sign in to your account. [link: “zoom.us” → `https://zoom.us`]
- Schedule a Meeting:
– Click “Schedule a Meeting” from the main dashboard.
– Fill in the meeting details: topic, description, date, time, duration, etc.
– Adjust the meeting settings as needed (e.g., require a password, enable waiting room).
– Click “Save.”
- Share Meeting Details:
– After scheduling the meeting, you will see the meeting details page.
– Click “Copy the Invitation” and share the meeting ID and password with the students via email or your preferred communication method.
Scheduling Microsoft Teams Meetings
- Sign in to Microsoft Teams:
– Open the Microsoft Teams application or go to [ teams.microsoft.com ]( teams.microsoft.com) and sign in to your account. [link: “teams.microsoft.com” → `https://teams.microsoft.com`]
– Click “New Meeting” at the top right corner.
– Fill in the meeting details: title, participants, date, time, and description.
– Adjust the meeting options as needed (e.g., require lobby, enable meeting chat).
– Once the meeting is scheduled, you will see it in your calendar.
– Click on the meeting and select “Share via email” or copy the meeting link and share it with the students.
Directions and Scheduling for Students and Parents
- Weekly Schedule:
– The teacher will provide a weekly schedule with the days and times of each tutoring session.
– Ensure you have the correct meeting links, IDs, and passwords for each session.
- Preparing for the Session:
– Make sure your device (computer, tablet, or phone) is charged and has a stable internet connection.
– Log in to Zoom or Microsoft Teams a few minutes before the session starts to ensure everything is working properly.
– Have any necessary materials (books, notebooks, pens) ready before the session begins.
- During the Session:
– Join the meeting at the scheduled time using the provided meeting link.
– Participate actively and complete any assignments or activities as instructed by the tutor.
– Ask questions if you need clarification on any topics.
- After the Session:
– Review the session’s materials and complete any homework or practice activities assigned by the tutor.
– Reach out to the teacher via email or messaging if you have any questions or need further assistance.
By following these directions, both students and teachers can ensure smooth and productive tutoring sessions.

#### Section: Price of Online Tutoring Sessions
The average cost of online tutoring varies widely based on the subject, the tutor’s qualifications, and the tutoring platform. Generally, here are the price ranges for one-on-one online tutoring: at American Group International.
- Mathematics, Physics, Biology, Computer Science:
– Professional tutors: $20.00 to $50.00 per session of 45 minutes to 1.5 hours
– Student tutors: $10.00 to $25.00 per session of 45 minutes to 1.5 hours
– Online group sessions: $10.00 per student to $50.00 per class at least 5 person per class, normally these are 1.5-hour sessions.
- Languages (English, Arabic, French, Spanish):
– Rates range from $15.00 to $25.00 per 1.5-hour session depending on the platform and the student’s Level). Beginners range from 15.00 per 1.5-hour session. B1 or higher on the CEFR normally starts at $20.00 per 1.5-hour session. Accelerated classes will be $25.00 per 1.5-hour session.
- General Academic Subjects:
– Prices typically range from $20.00 to $25.00 per session for private tutoring sessions. Online group tutoring can be less expensive, generally ranging from $15.00 to $40.00 per 1.5 hour session.
These rates are influenced by factors such as the tutor’s experience, the complexity of the subject, and the platform through which the tutoring is provided.
Cancelation of classes are not refundable. The teacher has been paid and has booked the spot for your time. Please be aware that if you do not show up for the scheduled session that no refund will be given, and time will only be rescheduled if you pay for the new sessions.
The Administration
American Group International USA
2246 Amish Road
Grantsville, Maryland 21536
Online
- American Group USA LLC [link: “American Group USA LLC” → `agi-usa.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.48 `parent-responsibility.html`

- **Browser title:** Parent responsibility – American Group International, Agadir
- **Meta description:** AGI parent policy and responsibility: adjustment period, communication, safeguarding and fees.

Home / Admissions / Policies / Parent responsibility [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Parent responsibility
What AGI asks of families, from the 90-day adjustment period to communication and payments.
This outlines the policies, expectations, safeguarding rules, and academic procedures for all enrolled
students and families. By enrolling, parents/guardians agree to follow these terms to ensure a safe, structured, and effective learning environment.
- First 90-Day Adjustment Period
The first 90 days of enrollment are an adjustment period. Students must attend regularly, participate, and complete assigned work. Concerns must be addressed early. After this period, late concerns may not result in major academic changes.
- Academic Responsibility
Students must maintain attendance, participation, and completion of coursework. The school cannot evaluate academic level accurately without consistent attendance and work completion.
- Parent Responsibility
Parents are responsible for ensuring attendance, supporting learning at home, and addressing concerns early. The school does not replace parental responsibility.
- Learning Difficulties & Documentation
If a learning difficulty is suspected, parents must obtain professional evaluation and provide documentation. Without documentation, standard academic expectations apply.
- Academic Placement Testing
If a student is placed incorrectly, the school may conduct assessments in subjects such as Math or English.
Placement decisions are based on testing, performance, and teacher evaluation.
- Timeline for Academic Concerns
All concerns must be raised within the first 90 days or first semester. Late-year changes are not guaranteed.
- Program Structure & Attendance
In-person attendance is required for school-based documentation. Pod/umbrella programs are separate and do not qualify for local attendance records.
- Financial Responsibility
Fees must be paid on time. Continued enrollment depends on financial compliance.
- School Limitations
The school provides education only and does not offer legal, immigration, or personal services.
- Home-Based Learning Policy
Students not attending school must arrange independent tutoring. School staff will not provide home instruction.
- Safeguarding Policy
All learning must take place in safe, supervised environments. Staff are not permitted to conduct lessons in private homes or unsupervised locations.
- External Tutoring
External tutors may be recommended but are not school staff and are not supervised by the school.
- Teacher Tutoring Policy
School teachers may provide extra support only with approval and only on school premises or approved platforms. No cafes, homes, or informal locations are permitted.
- Safeguarding & Professional Boundaries
All interactions must remain professional and occur within school-approved settings to protect students and staff.
- Policy Agreement
Enrollment confirms agreement to all policies in this handbook. Failure to comply may result in withdrawal from the program. This Policy can be updated to reflect new situations that arise.
The Administration
Text as published by AGI. Please check with the office for the current version. Source: “Parent Policy and Responsibility” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.49 `placement-policy.html`

- **Browser title:** Provisional placement & assessment – AGI Agadir
- **Meta description:** AGI provisional placement and assessment policy: grade placement is not lowered for missing documents, language gaps or academic gaps.

Home / Admissions / Policies / Provisional placement & assessment [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Provisional placement & assessment
How new students are assessed and placed – and why no child is moved down a grade for a language gap.
Purpose:
This policy ensures that all new students admitted to American Group International (AGI) are placed appropriately in their grade and academic tracks, even when prior school documentation is missing or incomplete.
It reflects AGI’s commitment to inclusive education, student safety, and the academic success of every student.
- Mandatory Assessment for All New Students
All students entering AGI for the first time, whether from a French system, English system, or any other educational system, must complete assessment tests before admission.
Required assessments include:
English / ESL proficiency- Anglia Examinations Assessment Level
Mathematics (CAT)
Language Arts / Reading (CAT)
Other core academic subjects if needed
Placement into academic tracks will be determined based on these assessments, even if prior school records are provided. Normally we let children in the grade placement for their age.
- Provisional Admission
Students may be admitted provisionally if:
Required prior-school documentation (transcripts, report cards, assessment results) is missing.
Provisional admission is temporary, valid for a maximum of 60 calendar days from the student’s first day of school.
During this period, the student’s grade placement and academic support will be determined using internal assessments.
- Placement Decisions (Inclusive Education Approach)
Grade Placement:
Students are kept in the grade they enter, consistent with AGI’s commitment to inclusive education.
Grade placement is not lowered due to missing documents, language gaps, or academic gaps.
Academic Support:
Students who are behind in specific subjects will receive targeted support to help them reach grade-level expectations.
Support may include:
ESL classes
Simplified or scaffolded materials
Additional tutoring or guided practice
Progress is monitored regularly, and support is adjusted as the student improves.
Provisional Placement Exceptions:
In rare cases where a student demonstrates severe gaps that prevent participation at grade level, temporary adjustments may be made with administrative approval.
- Documentation Follow-Up
Parents/guardians must provide all prior academic records within 60 calendar days of the student’s first day of school.
It is the parents’ responsibility to submit documentation. The school is not required to repeatedly request missing records.
After 60 calendar days, if records are not provided, the school will determine grade placement and academic support based on internal assessments and the student’s performance.
All communications with parents regarding the initial request for documentation must be logged by the administration office.
- Support for Students with Academic Gaps
Students identified as behind in English, math, or other subjects will receive:
Supplemental instruction
Simplified or scaffolded curriculum materials
Targeted ESL support
Progress will be monitored regularly to ensure the student reaches grade-level expectations.
- Transparency and Compliance
Parental Responsibility:
Parents/guardians must provide complete and accurate information regarding their child’s:
Learning differences or disabilities (e.g., ADHD, dyslexia)
Special needs
Medical or psychological conditions relevant to schooling
Reports from doctors, therapists, or specialists
School Review and parental dishonesty:
If it is discovered that critical information has been intentionally withheld, the school administration will:
Conduct a review meeting with relevant administrative staff.
Evaluate the student’s needs, safety, and the school’s ability to provide appropriate support.
Administrative Action:
Based on the review, the school reserves the right to dismiss a student if parents are not complying with disclosure requirements.
The decision to dismiss is not a reflection on the student, but a measure to ensure:
Proper educational support
Safety and well-being of the student and other students
Compliance with school rules and policies.
Documentation:
All meetings, decisions, and communications regarding withheld information will be documented in the student’s file.
- Responsibilities
Role
Responsibility

#### Section: Principal / Academic Director
Approves provisional placement, oversees assessment administration, ensures students receive necessary support.
Teachers
Conduct assessments, document results, provide modified instruction, report progress.
**Administration Office**
Maintains communication with parents, logs all requests for missing documentation, tracks 60-day deadlines.
- Policy Review
This policy is reviewed annually and updated as needed to align with best practices in international education and accreditation standards.
Approved by:
Julie Wilburn, Director
American Group International
Policy 2026
Text as published by AGI. Please check with the office for the current version. Source: “American Group International – Provisional Placement & Assessment Policy” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.50 `programs-independent-studies.html`

- **Browser title:** Independent course studies – American Group International, Agadir
- **Meta description:** AGI independent course studies: modules, program, prices and certificates approved by the American Canadian Board.

Home / Programs / Independent studies [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Independent course studies
Self-paced, graduate-level modules using books and journals, with certificates approved by the American Canadian Board.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: INDEPENDENT Course STUDIES (Modules and Program)
This is an exciting new learning format for learners to gain certified certificates as they choose one or more courses that are of interest to them as well as beneficial for their classroom or organization. AGIs self-paced Independent Course Studies offer the ultimate in convenience for busy educators.
These flexible self-lead- self-taught classes offer the learner graduate level college level training and the support materials from this site; and completing the associated assignments.
Independent Course Studies are a new format. This format allows the learner to use Books and Journals as the focus of their research. Our certificates will be approved by American Canadian Board for Professional Training. Our school is accredited by American Council of and Development and QAHE.
To find courses, just visit the catalogue listing and send us the topic you want to study.
Each program has a no cost for the materials. Cost is only for the certificate for the completed courses for $49.95 for PDF certificate or delivery by mail for $79.95. Our instructors will evaluate your completed work and examination. All examinations must have an overall grade of 80 percent or Distinction.
Thank you for your interest.
American Group International
Email: americanecoleagadir@gmail.com
We offer these courses for short time study.
- Courses by Subject
- • Business +
- o Accounting
- o Finance
- o Human Resources
- o Management
- Introduction to Entrepreneurship
o Marketing
- Computer Science +
o Databases
o Information Systems
o Programming Languages
- Education +
o Curriculum & Instruction
- Opening Eyes into Inclusion and Diversity
- Introduction to curriculum for Early Childhood Education
o Distance Education
o Early Childhood
- Early Childhood Mathematics English
- Pre-School Training
- Early Childhood Education Course
- Child Development 101
o Elementary Education
- Mathematics for Elementary Teachers
- o Higher Education
- o Secondary Education
- • Engineering +
- o Civil Engineering
- o Electrical Engineering
- o Mechanical Engineering
- • Humanities +
- o Arts
- o History
- History of the Middle East
o Languages
- Sharing Knowledge: Best Practices for Language Learners in School.

#### Section: - Tefl/Tesol Course
o Linguistics
- Moroccan Arabic
o Literature, Rhetoric, and Poetry
o Music
o Philosophy
o Religion
- Journalism, Media Studies & Communications +
o New Media Journalism
- • Law +
- o Administrative Law
- o Civil Law
- o Constitutional Law
- o Contract Law
- o Criminal Law
- o Procedural Law
- o Property Law
- • Mathematics +
- o Algebra
- o Analysis
- o Applied
- o Calculus
o Geometry and Trigonometry
o Pure
o Statistics
- Medicine +
o Nursing
- Nursing Management and Professional Concepts
- Nursing Assistant
- Nursing: Mental Health and Community Concepts
- Nursing Foundations
o Nutrition
- Natural Sciences +
o Biology
o Chemistry
o Earth Sciences
o Physics
- Social Sciences +
o Anthropology
o Cultural & Ethnic Studies
o Economics
- Introduction to Business and Economics
o Gender & Sexuality Studies
o Geography
o Political Science
o Psychology
- Trauma Informed School Practices
o Sociology
- Student Success Courses
- Guide of fundmental writing
**Book Learning/ Critical Review Grading Rubric**
Essay. Please remember that it needs to be 12 Font. Times Roman. The essay should be about what you learned from the course. If you agree or disagree. It should be at least 1000 words, typed and double-spaced.
- A 8-10
- B 7-7.9
- C 6-6.9
- D 5-5.9
- F <5
- Summary (20%)
How well does the student summarize the text?
Clearly presents author’s thesis and describes his/ her strategies for supporting it.
Presents author’s thesis and describes his/her strategies for supporting it.
Presents author’s thesis but may not provide sufficient description of strategies for supporting it.
Insufficient explanation of author’s thesis, and/or insufficient description of strategies for supporting thesis.
No explanation of author’s thesis, and/or no description of strategies for supporting thesis.
Clearly and succinctly describes organization and presentation of text.
Describes organization and presentation of text.
Describes organization and presentation of text, but may need more details
Insufficient description of text’s organization and presentation.
Poor or no description of text’s organization and presentation.
Overall Quality of Analysis (20%)
How well does the student analyze the text?
Exhibits clarity, complexity, perceptiveness, originality, and depth of thought about the topic.
Exhibits clarity, and some depth about the topic, but lacks the qualities of complexity, perceptiveness, and originality exhibited in level A.
Exhibits some clarity, though only minimal depth of thought about the topic.
Exhibit some faulty logic, and/or stereotypical or superficial thinking about the topic.
Exhibit little or no evidence of effective thinking about the topic (please note that there may be effective thinking in the composition, but not about the topic).
Provides excellent evaluation of text’s weaknesses or strengths; evaluative criteria are unique and interesting.
Provides clear evaluation of text’s weaknesses or strengths; evaluative criteria are unique and interesting.
Makes some attempt to present the weaknesses or strengths of the text; evaluative criteria are used.
Insufficient attempt to present the weaknesses or strengths of the text; evaluative criteria are unclear.
Poor to no attempt to present the weaknesses or strengths of the text; no obvious criteria for evaluation.
Uses creativity to interpret text (e.g., places it in interesting context or compares / contrasts with other relevant texts).
Puts text in meaningful context when interpreting it.
Places text in context.
Insufficient attempt to put text in context
Poor to no attempt to put text in context.
Support of Analysis (20%)
How well does the student select, summarize and/or paraphrase supporting evidence from the text to demonstrate and support analysis?
Exhibits command of focus, coherent organization, and interesting development (with carefully chosen, insightful details, examples, arguments, etc.) of the topic.
Exhibits control of focus, organization, and development (all of the subject matter is relevant to the topic but is not as insightfully selected as a response at level A) of the topic.
Exhibits some control of focus, organization (structure may be formulaic or be organized loosely around the topic), and development (may contain some poorly chosen information, but major ideas are adequately supported).
Exhibit insufficient control of focus, organization (way ramble, be repetitious, or locked into a formula), and/or development (it may be mostly descriptive or lack adequate support) of the topic.
Exhibit a basic/elementary sense of organization (may be purely descriptive or strictly formulaic), but ideas about the topic are generally undeveloped, illogical, irrelevant, or inconsistent.
Organization & Content (20%)
Review is very well organized, containing an introduction, body paragraphs, and conclusion.
Review is well organized, containing an introduction, body paragraphs, and conclusion.
Review has separate introduction, body paragraphs, and conclusion, but connections among these could be improved.
Distinction between introduction, body paragraphs, and conclusion is unclear.
General structure of review is difficult to follow, and/or student failed to follow the prescribed format.
Paragraphs contain clear topic sentences, focus on a single issue, are coherent, and organized according to an obvious pattern of argument.
Effective use of transitional expressions and other signposts that make the structure of the document clear.
All paragraphs contain topic sentences, focus on a single issue and are coherently structured.
Some use of transitional expressions and other signposts that make the structure of the document clear.
Most paragraphs focus on a single topic and are coherently structured.
Topic sentences signal the structure of argument but may require more focus. Transitions are present and help connect parts of argument.
Paragraph structure needs improvement (some may be incomplete, or focus on too many issues, or be incoherent).
Topic sentences do not effectively signal structure of argument or lack focus / clarity.
More transitions are needed to develop argument.
Paragraphs are unfocused, incoherent or require restructuring.
Topic sentences are absent or unconnected to the paragraphs that follow.
Transitions are absent or used incorrectly.
Student’s tone and diction enhance the argument being made about the text under review.
Student’s tone and diction are appropriate for the argument being made about the text under review.
Student’s tone and diction are occasionally inappropriate for the target audience.
Student’s tone and diction are marginal.
Paper is much longer or shorter than the assignment requirement.
Student’s tone and diction are inappropriate.
Paper is unreasonably too long or too short.
Grammar & Mechanics (20%)
Clear, concise sentences.
Mostly clear, concise sentences.
Adequate sentence structure but may require editing for clarity/wordiness.
Poor sentence structure. Writing may be wordy or difficult to follow in places.
Very poor sentence structure, and/or uses inappropriate language or language that is too informal.
No grammatical errors.
Citations are included in the correct ACM format.
May have some minor grammatical errors.
Citations are included in the correct ACM format; may have minor errors.
Some grammatical errors, but these do not impede understanding.
Citations are included with some issues in ACM formatting.
Many grammatical errors.
Citations are included but not in the ACM format.
Significant grammatical errors, and/or
Contains errors that are identified by MS Word software but were not corrected.
Citations are missing.
The application form is now online: apply on the forms page. [link: “apply on the forms page” → `forms.html#enrollment`]
**American Group International School of Agadir**
Email as a PDF file with your name and date of birth and course of study to: americanecoleagadir@gmail.com
All courses will be processed as quickly as possible. For mailing copies please included your exact name and address with the essay submission.
Adults & professionals
- Adult high school diploma [link: “Adult high school diploma” → `adult-diploma.html`]
- Business & medical English [link: “Business & medical English” → `professional.html`]
- Learning pods & fast track [link: “Learning pods & fast track” → `programs-learning-pods.html`]
- Document editing [link: “Document editing” → `services-document-editing.html`]
- Exam proctoring [link: “Exam proctoring” → `services-proctoring.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.51 `programs-learning-pods.html`

- **Browser title:** Learning pods &amp; fast track – AGI Agadir
- **Meta description:** AGI and Anglia Morocco learning pods: small groups of ten, teacherpreneurs, fast-track high school.

Home / Programs / Learning pods [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Learning pods & fast track
Small groups of about ten students, led by teacherpreneurs – including a fast-track high school route.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: In detail
Add Your Heading Text Here

#### Section: Empowering Freelance Teachers and Parents with Innovative Learning Solutions

#### Section: Join Us if You Are a Freelance Teacher or a Group of Parents!
Unlock endless possibilities for learning the English language with Anglia Learning Pods. Designed to consist of 10 students in 10-week periods, our pods provide all necessary supplies to ensure a seamless educational experience.

#### Section: Anglia Learning Pods in Morocco?
Learning pods are small groups of students who gather regularly in a shared space to learn. These pods can be formed by parents, caregivers, or educators, and are typically supervised by an adult, either a hired tutor or a rotation of parents. They offer a flexible and customizable educational environment that can focus on academic learning, socialization, or both.

#### Section: Small Group Sizes
We want to offer freelancers the opportunity to work
with 10 clients a session.

#### Section: Customized Curriculum:
Tailored programs to meet specific needs.

#### Section: Flexible Structure and Schedule:
Adaptable to family needs.

#### Section: Safe Environment:
Controlled and supportive learning space.

#### Section: Why Choose Anglia Learning Pods?
At Anglia Learning Pods, we believe in providing a dynamic and enriching educational experience that goes beyond the traditional classroom. Our innovative learning pods are designed to inspire curiosity, foster creativity, and cultivate a love for learning in a nurturing environment.

#### Section: Benefits for Freelance Teachers
**Entrepreneurial Opportunities:**
Run your own educational venture.
**Flexibility:**
Design and implement customized programs.
**Professional Growth:**
Network with other educators and access professional development.

#### Section: Benefits for Parents and Students
**Personalized Attention:**
Tailored learning experiences.
**Experienced Educators:**
Qualified and passionate teachers.
**Safe and Supportive Environment:**
Nurturing space for growth.

#### Section: How Learning Pods Work?
One of the advantages of learning pods is that there are no set rules on how they should operate. Everything is determined by the parents/instructor who organize them and the common goals they want to achieve. Here’s a breakdown of how learning pods can be structured:
**Flexibility in Operation:**
Learning pods can have students enrolled in the same school attending online or video-based classes together. Alternatively, parents might take their children out of school and opt for full-time pod learning instead.
**Session Types:**
Pods may have in-person sessions, while others limit their classes to online instruction.
**Tutoring and Oversight:**
In some groups, parents hire a tutor or experienced teacher to teach and oversee students. This ensures proper guidance and adequate hands-on instruction.
Whether your learning pod aims to supplement a school-based curriculum or provide full-time instruction, it is crucial to provide your children with the best support to ensure optimum academic growth.

#### Section: We offer the following services:
- • English Examinations with book included.
- • Comprehension – Listening and Reading Intervention
- • Reading Comprehension Tutoring
- • English Math services
- • Phonics Exams
- • Math Tutoring
- • Business Exams
- • CITE Teachers Examinations TESOL
- • We want to offer freelancers the opportunity ( to work with 10 clients a session.)

#### Section: Our Tutoring Services
We are prepared to offer you comprehensive tutoring services for all your pod learning needs. We provide:
**In-Home and Live in Class Pods:**
Personalized instruction within your home or community
**One-on-One Tutoring Sessions:**
Available both in-home and online.

#### Section: About AGI
AGI is an American-Moroccan private tutoring company offering fun, individualized, and dynamic tutoring and coaching services for children and teens. Our services include:
**Multidisciplinary and Personalized Services:**
We work one-on-one with students of all ages.
**Traveling Learning Specialists:**
Academic tutors and executive functioning coaches.
**In-Home and Micro-Pod Services:**
Available throughout Morocco.

#### Section: AGI and Anglia Morocco Services
**Exam Services**
Our private-pay and doorstep language services, as well as math tutoring for all ages and skill levels, are individualized and adapted based on your child’s and peers’ needs
**For more information or to start your learning pod, please contact us at:**
- email: americanecoleagadir@gmail.com
- Headquarters: Number 20 Rue Baalabek, Cite Nahda, Agadir, Morocco
Explore More...

#### Section: Anglia Morocco Learning Pods….
What is a learning pod?
Join us if you are a freelanced teacher, a group of parents. The possibilities are endless to learn the English language with us. We want Pods to consist of 10 students in 10-week periods. Supplies are supplied.
- Learning Pods:
- Definition: Learning pods are small groups of students who gather regularly to learn in a shared space.
- Structure: These pods can be formed by parents, caregivers, or educators. They typically consist of a handful of students who come together for educational purposes.
- Supervision: Pods are often led by an adult, either a hired tutor or a rotation of parents.
- Purpose: Some pods focus on academic learning, while others serve as socialization groups.
- Flexibility: Families can customize the pod’s schedule, location, and curriculum to meet their specific needs.
- In summary, pod schools offer a creative and adaptable approach to education, emphasizing personalized learning and community collaboration. Whether for health concerns or educational preferences, these models provide an alternative to traditional schooling.

#### Section: Discover Anglia Learning Pods in Morocco: Unlock Your Child’s Potential!
**Why Choose Anglia Learning Pods?**
Key Features:
– Personalized Learning: Tailored programs to meet your child’s unique needs and learning style.
– Experienced Educators: Qualified and passionate teachers dedicated to your child’s success.
– Self-directed Curriculum: Engaging lessons that make learning fun and effective.
– Safe Environment: A secure and supportive space where your child can thrive.
Join Our Community:
Located in the heart of Morocco, Anglia Learning Pods offers a unique blend of local culture and global education standards. Our unrestricted facilities and innovative teaching methods ensure your child receives the best possible education.
Programs Offered:
– Early Childhood Education
– Primary and Secondary Education
– English Language Immersion Programs
– Mathematics Activities
– Extracurricular Enrichment
– Others
Enroll Today!
Give your child the gift of a world-class education with Anglia Learning Pods. Limited spots are available, so don’t miss out!
Visit Us: www.angliamorocco.org
Anglia Morocco Learning Pods – Empowering Young Minds for a Brighter Future in English!
Adults & professionals
- Adult high school diploma [link: “Adult high school diploma” → `adult-diploma.html`]
- Independent course studies [link: “Independent course studies” → `programs-independent-studies.html`]
- Business & medical English [link: “Business & medical English” → `professional.html`]
- Document editing [link: “Document editing” → `services-document-editing.html`]
- Exam proctoring [link: “Exam proctoring” → `services-proctoring.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.52 `promotion-retention.html`

- **Browser title:** Promotion & retention – American Group International, Agadir
- **Meta description:** AGI promotion and retention policy: 64% in core subjects, 90% attendance, English assessment and summer remediation.

Home / Admissions / Policies / Promotion & retention [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Promotion & retention
How AGI decides promotion to the next grade, and the support offered when a student is retained.
Promotion and Retention Procedures Policy Promotion from one grade to another normally occurs at the end of the school year. Students are allowed to the next grade by completing grade level criteria set up by the curriculum. The following criteria will be used to decide the student’s placement into the next grade or retention in the current grade: Promotion • The student’s understanding of current grade level curriculum in all the following subjects:
- Math, Science, Language Arts and Social Studies.
- Students must pass each core subject with at least a 64% (D) or above to be considered as “passing.”
- The student’s attendance record (90% of enrolled days) • The student’s maturity level is proven throughout the year.
- English Assessment Testing for guaranteed levels completed. Retention
- Student’s inability to receive a 64% or above in two or more of the subject areas above.
- Poor attendance • Immaturity; and,
- Consensus of teacher and Principal.
- Students who have not met the above promotion requirements will not be promoted into the next grade. Students who have not met the attendance requirement due to excused illness or injury will be promoted supplied their grades are adequate.
- Students who have been kept may attend summer remediation to see if the grade-level aims can be met. Once they have successfully completed this remediation, they will need to be retested at AGI to figure out if they can pass the course of study. The student will need to successfully pass the test given at the school to be placed into the next grade level. The school has final determination on promotion and retention of students.
- These procedures are non-negotiable.
Text as published by AGI. Please check with the office for the current version. Source: “Promotion and Retention Procedures Policy” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.53 `refunds-complaints.html`

- **Browser title:** Refunds & complaints – American Group International, Agadir
- **Meta description:** AGI policies and procedures for refunds and complaints across all divisions.

Home / Admissions / Policies / Refunds & complaints [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Refunds & complaints
One procedure for all AGI divisions: enrollment, refunds, complaints and counseling.

#### Section: Refunds, Complaints and Counseling Support
Welcome! At American Group International (AGI), we are committed to providing a safe, supportive, and high-quality experience for every student and client. These policies are designed to help you understand how we handle enrollment, refunds, complaints, and counseling support. Our goal is to make your experience with us clear, fair, and positive.
These policies apply to all divisions of AGI, including:
- AGI Learning Pods – Small group learning programs.
- iHeart Therapeutic Services – Counseling and social-emotional support
- Anglia Morocco – English language programs and testing
- Anglia Examinations – Ofqual-regulated exams and certifications
- American Group USA – International programs and partnerships
Whether you are a parent, student, or client, we want you to feel confident that your concerns will be heard, your questions answered, and your child’s well-being is our priority.
**Refund Policy**
At AGI, we strive to provide excellent programs and services. The following refund policy applies to all programs and services across all divisions.
Registration & Enrollment Fees All registration and enrollment fees are non-refundable, as they secure placement and cover administrative costs.
Tuition & Program Fees Refund requests must be submitted in writing and are processed as follows:
- Before the program start date: Up to 80% refund (excluding registration fees)
- Within the first 7 days of the program: Up to 50% refund
- After 7 days: No refunds will be issued
Short Courses, Workshops & Testing No refunds will be issued for:
- Completed sessions
- Missed classes
- Examination fees once scheduled
Rescheduling may be offered at the discretion of administration.
Special Programs & Partner Services Refund policies may vary depending on partner institutions or third-party providers. All third-party fees are non-refundable.
Exceptional Circumstances Partial refunds or credits may be considered in cases such as:
- Documented medical emergencies
- Relocation or unavoidable circumstances
All requests are reviewed individually.
Refund Processing Approved refunds are processed within 14–30 business days and issued via the original payment method where possible.
**Complaints Policy**
We value your feedback and are committed to resolving concerns fairly, respectfully, and efficiently.
How to Submit a Complaint Complaints must be submitted in writing and include:
- Full name
- Program or service involved
- Description of the issue
- Supporting documentation (if applicable)
Complaints may be submitted via email, official communication channels, or in person at administration which should be in writing when reported.
Complaint Process
- Acknowledgment: Within 2–3 business days
- Review: Investigation by the appropriate department
- Response: Within 7–10 business days
Escalation If a complaint is not resolved, it may be escalated to senior management. A final decision will be issued within an additional 7 business days.
Confidentiality All complaints are handled confidentially and shared only with relevant parties involved in the resolution.
Fair Treatment No student, parent, or staff member will face retaliation for submitting a complaint. We are committed to maintaining a safe and respectful environment.
**Counseling & Therapeutic Disclaimer**
At AGI, we care about the emotional and social well-being of our students. Therapeutic Services may provide counseling support to students and families to help with general guidance, academic success, and personal growth.
Nature of Services
- All guidance provided by the school counselor is advisory in nature only.
- The school counselor is not a medical doctor and does not provide medical diagnoses, treatment, or clinical therapy.
These services are intended to support:
- Student well-being
- Academic success
- Social and emotional development
**Referral to External Professionals**
- If needed, the school counselor may recommend that a student or client seek support from a licensed professional, such as a psychologist, psychiatrist, or medical doctor.
- Responsibility for seeking external care remains with the student and/or parent or guardian.
**Limitation of Liability**
- AGI and its divisions are not responsible for outcomes resulting from decisions made based on counseling advice.
- School-based counseling services do not replace professional medical or mental health care.
Regards,AGI
Text as published by AGI. Please check with the office for the current version. Source: “Policies & Procedures American Group International & Divisions, Refunds and Complaints” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.54 `resources-mcguffey.html`

- **Browser title:** McGuffey readers &amp; sight words – AGI Agadir
- **Meta description:** McGuffey readers and sight words: classic reading and spelling practice for children (public domain).

Home / Student life / McGuffey readers & sight words [link: “Home” → `index.html`] [link: “Student life” → `student-life.html`]
**Page title (H1):** McGuffey readers & sight words
Classic McGuffey reading lessons and sight words for reading and spelling practice at home.
→ **Request a tutor** (`forms.html#tutor-request`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: McGuffey’s Online Tutor/Sight Words Helps for Reading/Spelling
This is a reading site for McGuffey’s Reading program. They have all online reproducible worksheets and Youtube videos to go with all lessons. If you need a reading book from McGuffey’s let the school know by email. Files for the books are listed at the bottom for free.
mcguffeysonlinetutor.blogspot.com [link: “mcguffeysonlinetutor.blogspot.com” → `https://mcguffeysonlinetutor.blogspot.com/2015/10/0-12-object-lesson-xii-fox-mcguffeys.html?m=0`]
Dolch Words and Sight Word Charts
Full Spelling Curriculum!

#### Section: Eclectic Educational Series.
Full Book Without Pictures!
McGUFFEY’S ®

#### Section: Eclectic

#### Section: Spelling-Book.

#### Section: Revised Edition.
McGuffey Editions and Colophon are Trademarks of
John Wiley & Sons, Inc.

#### Section: New York-Chichester-Weinheim-Brisbane-Singapore-Toronto

#### Section: Preface.
In revising this book, care has been taken to preserve all the excellences that have so long and so favorably distinguished McGUFFEY’S ECLECTIC SPELLING-BOOK: and the chief changes that have been made, have been suggested by the evident plan of the original work.
The old system of indicating the pronunciation by numerals, called “superiors,” has been abandoned, and the diacritical marks used by Webster have been adopted. The Revised Speller conforms in orthography, pronunciation, and syllabication to the latest edition of Webster’s Unabridged Diction­ary. Exercises have been given on each of the distinctive marks used in the book, as will be seen by reference to Lessons 36-57.
A number of lessons have been added in the department of prefixes and suffixes, and now nearly all the more common of these etymological principles have been explained. (See Les­sons 136-167.)
In arranging the text of the several lessons, the object has been not to appeal merely to arbitrary memory, but to asso­ciate each lesson with some principle of sound, meaning, or accent, which would tend to aid the pupil in acquiring a knowledge of our language. Several distinct lessons on pro­nunciation are given, and towards the close of the book numerous lessons of difficult words in orthography have been introduced.
Instead of indicating silent letters by italics, as has hitherto been done, a new type has been made in which such letters are canceled, thus enabling the pupil to discover their status at a glance.
The pages have been enlivened, as in the other books of this Series, by attractive engravings.
The publishers take pleasure in acknowledging the valu­able services of W. B. Watkins, D. D., who planned and executed this revision.
DECEMBER, 1879.
16
Copyright, 1879, by Van Antwerp, Bragg & Co.
(ii)

#### Section: The English Alphabet.
The English Alphabet consists of twenty-six letters, viz.: a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z.
Letters are divided into VOWELS and CONSONANTS.
The Vowels are those letters which can be perfectly sounded without the aid of any other letter. The vowels are a, e, i, o, u, w, and y.
The vowel sounds of w and y are the same as those of u and i. A, e, and o are always vowels. I, u, w, and y are sometimes consonants.
A Diphthong is the union of two vowels in one sound. When both vowels are sounded, the diphthong is called PROPER, because then it is really a DIPHTHONG, or double sound; that is, the sounds of the vowels unite; as, oi in oil; ou in sound.
When only one of the vowels is sounded, the diphthong is called IMPROPER, because then, as one of the vowels is silent, it is not properly a DIPHTHONG, though it takes that name; as, oa in boat, ui in suit, where a and i are silent.
The following diphthongs are in common use, viz.: oi, oy, ou, ow, ae, ai, au, aw, ay, ea, ei, eo, eu, ew, ey, ia, ie, oa, oe, ua, ue, ui; as in toil, boy, round, plow, seal, coal, head, sail, say, aught, yeoman. Of these, oi, oy, ou, and ow are gener­ally proper diphthongs; though sometimes ou and ow are improper, as in famous, where o is silent, and in slow, where w is silent.
A Triphthong is the union of three vowels in one syllable; as, eau in beau, iew in view. The triphthong is properly a union of letters, not sounds.
(iii)

#### Section: 4 Eclectic Series.

#### Section: Of The Various Sounds.
All the vowels, and some of the consonants, have several sounds; in this book these sounds are indicated by diacritical marks, as in the following tables:

#### Section: Table Of Vocals.
Long Sounds.
- Sound
- as is
- as in
- a
- ate
- e
- eve
- care
- err
- arm
- i
- ice
- last
- o
- ode
- all
- u
- use
- oo
- fool
Short Sounds.
- am
- odd
- elm
- up
- in
- look
Diphthongs.
oi,oy,as in oil, boy ou,ow, as in out, owl

#### Section: - Table Of Subvocals
- b
- bib
- v
- valve
- d
- did
- th
- this
- g
- gig
- z
- zinc
- j
- jug
- zh
- azure
- n
- nine
- r
- rare
- m
- maim
- w
- we
- ng
- hang
- y
- yet
- l
- lull

#### Section: - Table Of Aspirates
- f
- fife
- t
- tart
- h
- him
- sh
- she
- k
- cake
- ch
- chat
- p
- pipe
- thick
- s
- same
- wh
- why

#### Section: - Spelling Book. 5
NOTE.–The foregoing forty-four sounds are those most employed in the English language. Some of these sounds are represented by other letters, as shown in the following table. For further instruction concerning the sounds, see Lessons 36-57.

#### Section: Table Of Substitutes.
- for
- what
- myth
- there
- c
- can
- feint
- cite
- police
- chaise
- sir
- chaos
- son
- gem
- to
- ink
- wolf
- as
- fork
- sure
- work
- x
- gz
- exact
- full
- gh
- laugh
- burn
- ph
- phlox
- rude
- qu
- pique*
- fly
- kw
- quit
W, in its vowel sounds, corresponds with u; an in new ( pro. nu).
A has, in a few words, the sound of e; as in any ( pro. en’ny).
U has, in a few words, the sound of e; as in bury ( pro. ber’ry); or that of i, as in busy ( pro. biz’y).

#### Section: Of The Consonants.
The Consonants are those letters which can not be perfectly sounded without the aid of a vowel. The consonants are b, c, d, f, g, h, l, k, l, m, n, p, q, r, s, t, v, x, z, and sometimes i, u, w, and y. The consonants are divided into MUTES and SEMI-VOWELS.
The Mutes are those consonants that admit of no sound without the aid of a vowel. They are b, d, k, p, q, t, and c and g hard.
*Note.–The u is canceled in this book when qu is sounded like k.

#### Section: 6 Eclectic Series.
The Semi-vowels are those consonants that can be sounded imperfectly by themselves. They are f, h, j, l, m, n, r, s, v, x, z, and c and g soft.
Four of the semi-vowels are called LIQUIDS; viz., l, m, n, and r. They are called liquids because they unite so readily with other sounds, or flow into them.

#### Section: Of Syllables And Words.
A Syllable is a sound, or a combination of sounds, uttered by a single impulse of the voice: it may have one or more letters; as
a, bad, bad-ness.
A Word is either a syllable or a combination of syllables; as, not, notion.
A word of one syllable is called a Monosyllable; as, man.
A word of two syllables is called a Dissyllable; as, manly.
A word of three syllables is called a Trisyllable; as, manliness. Words of more than three syllables are called Polysyllables.
Accent is a stress of voice placed upon some one sylla­ble more than the others. Every word composed of two or more syllables has one of them accented. This accent is denoted by a mark (‘) at the end of the accented syllable; as, mid’night, a ban’don.
A Primitive Word is one which is not derived from any other word; as, man, great, full.
A Derivative Word is one which is formed from some other word by adding something to it; as, manful, greatness, fully.
A Simple Word is one which is not composed of more than one word; as, kind, man, stand, ink.
A Compound Word is one that is composed of two or more simple words; as, ink-stand, wind-mill.
Spelling is naming or writing the letters of a word.

#### Section: Spelling-Book. 7
Script Alphabet

#### Section: Capital Letters.

#### Section: A B C D E F G H I

#### Section: J K L M N O P Q R

#### Section: S T U V W X Y Z

#### Section: Lower-Case Letters.

#### Section: 8 Eclectic Series.

#### Section: The Alphabet.
Q

#### Section: Spelling-Book. 9

#### Section: 10 Eclectic Series.

#### Section: Pictorial Alphabet.
- A B
- C D
- E F
- G H

#### Section: - Spelling Book. 11
- I J
- K L
- M N
- O P
- Q R

#### Section: 12 Eclectic Series.
S T
U V
W X
Y Z

#### Section: Eclectic Spelling-Book.
Lesson 1.

#### Section: Short Sounds Of Vowels.
Short Sound of A.
am cat gap ban cap
an bad bag can map
as mad gag fan nap
at pad hag pan rap
ax sad lag ran hap
rat gad tag tan jam
sat sap fag van ham
Short Sound of E.
bed den net sell tent
led ken pet nest rent
red men set zest sent
wed wen yet test went
beg jet sex pest felt
leg let fell rest pelt
hen met bell jest melt
(13)

#### Section: 14 Eclectic Series.
Lesson 2.

#### Section: Short Sounds Of Vowels.–Continued.
Short Sound of I.
if rid him sin jig
it lid rim tin rig
is sip fix dig bib
bit tip six fig jib
hit nip din big rib
sit lip pin pig fib
Short Sound of O.
on cob nod box dot
ox job pod hop jot
got rob rod mop lot
cot sob log sop pot
jot cod hog pop rot
lot God dog top not
Short Sound of U.
up mud rum rut gush
us dug sum hung dust
cub mug bun bung must
hub pug dun lung rust
rub tug run sung gust
bud jug sun hulk drum

#### Section: Spelling-Book. 15
Lesson 3.

#### Section: Review Of Short Sounds Of Vowels.
man lap pat tap had
fin get ten wet peg
fit dim mix hid his
hot rot fob dot con
rug hum fun hut cut
had fun hug gum flog
den fog dip nag dram
did tub fog bet help
sod hod gun pen lift
lad bet did cog rush

#### Section: 16 Eclectic Series
Lesson 4.
Long Sound of A.
date jade came cage bane
late fade dame page lace
mate rate same sage wake
Long Sound of E.
me we she heed weed
fee jeer feed deed deep
feel leer meek keep peep
seek veer beef reel weep
Long Sound of I.
pile dike fire life bide
file like tire rife hide
mile pike sire wife ride
Long Sound of O.
code dolt bone hope dote
node jolt cone pope note
bode molt hone rope vote
rove bolt tone cope hold
Long Sound of U.
lure cube mute lune huge
cure tube duke dune pule
pure lute jute use cue

#### Section: Spelling-Book. 17
Lesson 5.
crab bled chip shot bump
grab fled ship blot lump
drab sled whip spot pump
slab sped slip plot jump
stab then drip trot hump
brag bent spit clog bulk
cram best crib frog just
clan hemp gift plod drug
clad vest king stop shut
dash west grit clod hush
Lesson 6.
Various Vowel Sounds.
bard deal tank dell ill
card veal rank tell bill
hard meal sank well fill
bark neat hank yell rill
dark heat dank belt hill
dint bang dime rave cull
hint fang lime gave dull
lint gang tine lave gull
mint hang fine pave hull
tint rang mine save mull
Sp.2.

#### Section: 18 Eclectic Series.
Lesson 7.
Long Sounds of Vowels.
blaze sneer drive globe dean
craze creed tribe drone bean
shape steep brine stone bead
state sleek spire probe beam
crape fleet bride shore lean
fume smite blame clear mope
spume spite flame drear mold
fluke quite slate blear tore
flume whine spade spear robe
dure spine prate smear poke
Lesson 8.
Various Sounds of Vowels.
clasp small cramp bring moan
grasp stall stamp cling coast
flask fall grand sling toast
graft wall stand swing roast
craft squall lamp thing roach
book boon stork wad pod
good spoon horse was rob
took bloom snort wash rock
foot broom short wast soft
hook stool north what lost

#### Section: Spelling-Book 19
Lesson 9.
Long Sounds of Vowels under the Accent.
fa’tal le’gal lo’cal cu’bit
na’tal re’gal fo’cal du’el
pa’pal re’al vo’cal hu’man
pa’gan pe’nal o’ral u’nit
ba’by ta’per o’val du’ly
la’dy di’al to’tal fu’ry
la’zy tri’al bo’ny ju’ry
ma’zy fi’nal co’ny pu’ny
na’vy vi’tal go’ry pu’pil
ra’cy ri’val ro’sy hu’mid
Sa’tan vi’al po’sy tu’mid
Lesson 10.
Short Sounds of Vowels under the Accent.
al’um el’der civ’il cul’prit
al’to hec’tic dit’ty clum’sy
can’ter helm’et gid’dy dul’cet
mar’ry fen’nel fil’ly fun’nel
ral’ly ken’nel sil’ly gul’ly
nap’kin bel’fry liv’id buck’et
hap’py ed’dy lim’it gus’set
pan’try en’try lim’ber sul’len
ram’mer en’vy riv’et sum’mon
mam’mon test’y lin’en hur’ry
tab’let self ‘ish mil’let mul’let

#### Section: 20 Eclectic Series.
Lesson 11.
Various Sounds of A.
care fast charm camp war
mare mast chart damp warp
share cask lard hand warm
spare mask arm land ward
snare past yard sand warn
game scar lake waft fray
lame spar dale raft play
name star gale chaff gray
fame garb cape aft stay
tame barb shame staff bray
Lesson 12.
dan’ger am’ber lard’er clat’ter
man’ger ban’ter mar’gin flat’ter
quak’er ban’ner ar’dent lat’ter
qua’ver hand’y ar’my mat’ter
dra’per man’na art’ist pat’ter
wa’ger can’cer har’vest tat’ter
fa’vor pan’der par’ty rag’ged
fla’vor tam’per tar’dy rack’et
sa’vor plan’et ar’dor van’ish
ma’jor ham’per car’pet gal’lant
ca’per stam’mer gar’ment pat’tern

#### Section: Spelling-Book. 21
Lesson 13.
Various Sounds of E.
sheep ce’dar bet’ter cler’gy
creep fe’ver fet’ter fer’vor
sleep tre’mor let’ter her’mit
sweep ge’nus en’ter mer’cy
speed se’cret ev’er ser’mon
breeze re’bus nev’er ser’pent
teeth se’quel sev’er mer’chant
sneeze se’quence dex’ter ver’bal
breed he’ro mem’ber ver’dict
bleed ze’ro plen’ty per’son
freed se’cant ven’om fer’ment
Lesson 14.
Various Sounds of I.
bird bri’er bib’ber thir’ty
birch ci’der bit’ter thirst’y
chirp mi’ser dif ‘fer third’ly
flirt spi’der din’ner birch’en
girl vi’per frit’ter chirp’er
shirt cli’ent lit’ter girl’ish
squirm gi’ant riv’er gird’er
squirt i’tem shiv’er stir’less
third i’cy sil’ver first’ly
girt spi’ral in’ner birth’day
gird i’vy liv’er mirth’ful

#### Section: 22 Eclectic Series.
Lesson 15.
Various Sounds of O.
bro’ker col’ic cor’net worst
clo’ver ton’ic cor’set come
drov’er top’ic or’gan love
gro’cer mor’al sor’did dove
o’ver com’ma tor’pid shoot
o’dor dog’ged form’al moon
so’lar doc’tor for’ty moose
po’lar cop’per lord’ly tooth
pok’er fod’der morn’ing gorge
home’ly fos’ter orb’it most
po’em pon’der mor’tal prop
Lesson 16.
Various Sounds of U.
hu’mor but’ter mur’der pru’dent
ju’ror mut’ter mur’mur fru’gal
tu’mor rud’der tur’ban tru’ly
stu’por shut’ter tur’nip tru’ant
tu’tor suf ‘fer tur’key cru’et
cu’rate sup’per pur’port bru’in
lu’cid mum’my curl’y dru’id
stu’dent mus’ket fur’ry ru’in
stu’pid num’ber fur’nish ru’by
lu’nar nut’meg cur’vet bru’tal
tu’mult stut’ter bur’den gru’el

#### Section: Spelling-Book 23
Lesson 17.
Various Sounds of the Vowels.
June furl husk from halt
dupe hurl musk pomp malt
tune turn rusk romp salt
flute churn stung long waltz
plume hurt pluck song swan
glue curl drunk strong wasp
droop deck chill for sheath
gloom neck drill corn shell
loop next quill fork shorn
hoof text skill form shout
roof desk spill sort shrub
proof nest frill torch shrug

#### Section: 24 Eclectic Series.
Lesson 18.
Words Accented on the last Syllable.
a wake’ be hest’ be hind’ re cede’
be came’ be set’ be side’ con crete’
be have’ ca det’ be tide’ com pete’
be take’ de fend’ de rive’ se crete’
e late’ de pend’ re cite’ con cede’
per vade’ re pel’ re tire’ con vene’
for sake’ at tend’ re vile’ im pede’
a bate’ con sent’ re mise’ re plete’
cre ate’ im pend’ re vive’ un seen’
es tate’ im pel’ con nive’ su preme’
re late’ com pel’ ex cite’ re lease’
Lesson 19.
be rate’ a bode’ ex pire’ a cute’
a pace’ a lone’ con fide’ a buse’
re bate’ a tone’ con fine’ con fuse’
de bate’ af ford’ con spire’ de duce’
de face’ ca jole’ po lite’ de lude’
de fame’ de pose’ re cline’ ma ture’
se date’ com pose’ re fine’ pol lute’
col late’ en force’ re pine’ pro cure’
re gale’ en robe’ re quire’ re buke’
em pale’ ex plore’ re spire’ re duce’
en gage’ ex pose’ u nite’ se clude’
en rage’ im port’ en twine’ se cure’

#### Section: Spelling-Book. 25
Lesson 20.
blade plash bream dress twine
glade clash cream swim blind
grade crash dream spend grind
shade smash gleam speck spike
trade trash steam fresh smile
skate slash stream whelp while
brisk drove blush cheap carve
quilt grove flush peach farce
filth stove slush teach parse
pinch clove brush reach barge
flinch smote crush bleach large
mince store thrush glean snarl
Lesson 21.
ab’bey rec’ord pit’y col’ter
ab’bot check’er dis’tant fo’cus
atom ed’it din’gy glo’ry
ash’es lev’el diz’zy lo’cust
cap’tor meth’od fin’ish mo’ment
car’rot splen’did gim’let po’tent
cav’il ves’per spir’it co’gent
ehap’ter west’ern tim’id do’tage
chat’tel bed’lam pig’gin no’ted
fath’om des’pot tin’sel stor’age
gal’lon ren’der tip’pet sto’ry
gal’lop tem’pest wit’ness pro’test

#### Section: 26 Eclectic Series.
Lesson 22.
shake chose march pine oil
snake prose parch wild moil
baste those starch mild coil
haste froze larch tile foil
taste force lark slide soil
paste porch stark glide toil
bunch broth prism spent boy
hunch cloth sixth fence coy
lunch froth stint hence hoy
punch moth smith pence joy
plump botch whist thence toy
stump stock midst whence cloy
Lesson 23.
Monosyllables miscellaneously arranged.
free clip shelf quest shine
spin hate chide flax wore
shad tape fringe still think
band race clock trim marsh
pack mire cheek door booth
bath kite full clung wince
dock bank frock loft spray
gold fell troop pulp join
pipe pink glass grape friz
club hilt lurk pose brow
shop last cloud zest grace

#### Section: Spelling-Book 27
Lesson 24.
Words in which the final e is silent.
ca’ble nee’dle rab’ble bub’ble
fa’ble Bi’ble sam’ple bun’dle
ga’ble ti’tle sim’ple crum’ble
sa’ble ri’fle tem’ple muf ‘fle
sta’ble no’ble dim’ple muz’zle
cra’dle fick’le fid’dle pud’dle
la’dle am’ple kin’dle ruf ‘fle
ma’ple ap’ple lit’tle tum’ble
sta’ple baffle bot’tle pur’ple
bee’tle bat’tle cob’ble cir’cle
fee’ble cat’tle fond’le sad’dle
Lesson 25.
an’gel ab’sent bish’op blun’der
ba’sis ac’rid big’ot blus’ter
ca’ter blank’et bil’let cus’tom
fla’grant clas’sic blis’ter cut’ler
fra’grant crag’gy cin’der cut’ter
has’ty dam’sel crick’et sum’mer
ha’tred dan’dy fif ‘ty sun’der
la’bel fab’ric fil’let shud’der
pa’tent fam’ish lim’pid thun’der
sa’cred fran’tic pil’fer tum’bler
state’ment lath’er pil’lar ul’cer
va’cate lav’ish print’er un’der

#### Section: 28 Eclectic Series.
Lesson 26.

#### Section: Dictation Exercises.
NOTE TO TEACHERS.–These lessons are intended as exercises in the meaning as well as the spelling of words. Distinguish carefully words of similar sound, but which differ in their spelling. At the recitation the sentences should be read aloud by the teacher, and the pupils required to write them out neatly and correctly upon their slates or on the black­board.
He ate seven or eight apples. Send the pale maid with the pail of milk. He owed for the paper on which he wrote an ode to the moon. We are not quite ready for the quiet man. Age gives edge to wine. He said the idol looked like a satyr. Clever satire often rouses the idle.
Lesson 27.
Sounds of ai, ou, ow, and ea,
paid bound cow cheat head
grain found how treat dead
staid ground town beast stead
waif hound growl bleat tread
rail mound clown preach dread
flail pound frown speak thread
quail round crown streak sweat
snail sound drown feast death

#### Section: Spelling-Book. 29
Lesson 28.
Dissyllables with short Sounds of Vowels.
ad’age fren’zy bick’er blos’som
bal’last emp’ty crit’ic cot’ton
bant’ling gen’try dig’it com’ic
can’to mer’it flim’sy drop’sy
ras’cal men’tal flip’pant flor’id
las’so sher’iff frig’id frol’ic
an’tic ten’dril in’fant gos’pel
sad’ness vel’lum in’gress gos’sip
sal’ver vel’vet in’mate hor’rid
sand’y nec’tar in’quest jol’ly
mag’got ves’try in’sect rock’et
Lesson 29.
Trisyllables with short Sounds of the Vowels.
bal’co ny del’i cate lib’er ate
bar’o ny des’o late lim’i tate
cav’i ty der’o gate im’mo late
fac’ul ty dev’as tate in’di cate
grav’i ty em’u late in’ti mate
mal’a dy hes’i tate in’du rate
van’i ty med’i tate in’vo cate
am’pu tate pet’ri fy ir’ri tate
ab’so lute plen’i tude lit’i gate
al’ti tude rec’ti tude mil’i tate
am’bu lance res’o lute stip’u late

#### Section: 30 Eclectic Series.
Lesson 30.
Miscellaneous Sounds.
prime swine straw crawl
brawn snore gloss flank
brick charge crow quench
green tinge shark Scotch
chest goose brand thrift
space prow twist flange
crank wealth slice twain
limp screw throb thrice
chess flake soon flesh
finch flash flaw twelve
flung clean loaf scale
Lesson 31.
Long Sounds of I and U, and short Sounds of E and I.
a bide’ ac cuse’ con tend’ ad mit’
a like’ im pure’ con tent’ ad dict’
a live’ im pute’ in tend’ as sist’
a rise’ as sume’ in tent’ com mit’
de cide’ com mute’ dis sect’ con sist’
de file’ com mune’ de ject’ de pict’
de fine’ com pute’ de test’ dis till’
de ride’ con clude’ de tect’ emit’
de sire’ con fute’ in spect’ en list’
di vide’ dis pute’ ob ject’ en rich’
di vine’ en dure’ re spect’ for bid’

#### Section: Spelling-Book. 31
Lesson 32.
Silent Letters.
B is silent after m and before t, and p is silent before s. The silent letters are canceled in this lesson, as they are throughout the book.
lamb numb debt debt’or
comb bomb doubt doubt’ful
tomb crumb psalm sub’tle
dumb thumb pshaw psal’ter

#### Section: Dictation Exercises On The Above.
The lamb is a dumb animal. He climbed the hill to the tomb, but his limbs became numb. Comb your hair, but do not thumb your book. Bombs are now commonly called “shells.” The debtor, who was a subtle man, doubted his word, and gave not a crumb of comfort. Take your psalter and select a joy­ous psalm. His answer was, “Pshaw!”
Lesson 33.
Sounds of igh, oa, shr, and thr.
nigh load coax shrank thrash
thigh oats hoax shrewd threat
fight boat oath shrift throng
light oak coach shrike throve
flight foal float shrunk thrust
fright goat poach thrill throat
tight soap hoarse three thrum

#### Section: 32 Eclectic Series.
Lesson 34.
Long and short Sounds of A, and short Sound of E.
gain a bash’ dis patch’ pre tend’
nail ca bal’ dis tract’ re flect’
taint ca nal’ ex pand’ re fresh’
trail cra vat’ a bet’ re lent’
aim de camp’ be deck’ re ject’
maim pro tract’ be held’ re quest’
train re cant’ be quest’ re bel’
strain re fract’ de fect’ re gress’
chain re lax’ e lect’ re press’
paint at tack’ e rect’ sub ject
quaint at tract’ e vent’ neg’lect’
Lesson 35.
ac’ci dent ben’e fit dif ‘fer ent
ad’a mant brev’i ty dif ‘fi cult
am’i ty clem’en cy fil’a ment
an’i mal des’ti ny in’cre ment
an’nu al neg’li gent in’do lent
can’is ter pend’u lum his’to ry
flat’ter y rem’e dy in’ju ry
fam’i ly reg’u lar pil’lo ry
lax’i ty rel’e vant sim’i lar
man’i fest pen’i tence tit’u lar
man’i fold pen’e trate tim’or ous

#### Section: Spelling-Book. 33
Lesson 36.

#### Section: Sounds Of The Vowels, Diphthongs, And Consonants.
In this lesson, and in the pages immediately following, will be found forty-three exercises on the various sounds of the English language. Some of these have been given already, but are repeated here for the more thorough instruction of the pupil Let the teacher carefully discriminate between the different sounds of the vowels, and fully drill the scholars in their correct enunciation.
- Regular Long Sound of A, marked a.
make la’tent brave a base’ment
safe cham’ber crave a bate’ment
gaze pas’try grave ad ja’cent
saint man’gy shave a wa’ken
Lesson 37.
- Regular Short Sound of A, marked a.
span ad’der crack can’di date
trap an’vil gland cal’i co
plat ban’ish slack grat’i tude
sham bran’dy plaid mag’is trate
- Sound of A before r in such words as air, care, marked a.
dare af fair’ chair trans par’ent
rare de spair’ prayer for bear’ance
flare be ware’ scare par’ent age
glare com pare’ square care’ful ness
Sp.3.

#### Section: 34 Eclectic Series.
Lesson 38.
- Sound of the Italian A, as in arm, marked a.
farm ar’bor guard ar’gu ment
harm ar’mor daunt ar’ti choke
barn bar’ber harsh car’di nal
yarn car’go jaunt car’pen ter
- Sound of A in certain words before ff, ft, ss, st, sk, sp, and in a few before nce and nt, marked a, as in staff.
mass chance gasp chan’cel lor
class pass’port quaff chan’cer y
vast mas’ter chant craft’i ness
task graft’ed prance ad van’tage
Lesson 39.
- Sound of broad A. as in all, marked a.
thrall de bauch’ drawl au’di ence
tall de fault’ pawn laud’a ble
wart de fraud’ sprawl plaus’i ble
awe as sault’ warmth talk’a tive
- Short Sound of broad A, as in what, marked a.
wan wan’ton squash squal’id ness
wand wan’der squab was’ish ly
squat squan’der squad watch’ful ness
wat’ch wal’low swamp what ev’er

#### Section: Spelling-Book. 35
Lesson 40.
- Regular Long Sound of E, as in eve, marked e.
feel fe’male wean de’i ty
keel pee’vish these de’cen cy
glee que’ry priest e gre’gious
deem nei’ther cheer fre’quen cy
- Regular Short Sound of E, as in end, marked e.
ebb pen’ny sledge, en’e my
fret sec’ond spread rec’og nize
helm ten’der knelt len’i ty
them rec’tor cleft mem’o ry

#### Section: 36 Eclectic Series.
Lesson 41.
- Sound of E as in there, marked e, This corresponds with the sound of a in care.
ne’er par terre’ where up on’
where ere long’ where un to’
there of ‘ there by’ where a bouts’
heir’ess where at’ where with al’
- Sound of E like a, as in prey, marked e.
they neigh’bor neigh’bor hood
whey hei’nous sur vey’or
freight o bey’ pur vey’ance
deign in veigh’ con vey’ance
Lesson 42.
- Sound of E before r, verging toward the sound of u in urge, and marked e.
term er’mine terse ter’ma gant
pearl ear’ly merge per’son al
err per’fect yearn mer’chan dise
learn mer’cer swerve ser’mon ize
- Regular Long Sound of I. as in ice, marked i.
fife di’et Christ brib’er y
crime qui’et spice di’a dem
shrine fi’at strive li’a ble
thrive pli’ant slime i’ci cle

#### Section: Spelling-Book. 37
Lesson 43.
- Regular Short Sound of I, as in ill, marked i.
sting piv’ot spring dif ‘fi dent
bliss splin’ter twitch pin’a fore
inch tin’der thick in’fa my
strip wick’ed sphinx lit’ur gy
- Sound of I like that of long e, as in pique, marked i.
pe tite’ fa tigue’ mag a zine’
an tique’ in trigue’ sub ma rine’
ca price’ po lice’ ver’di gris
fas cine’ va lise’ quar’an tine
Lesson 44.
- Sound of I before r, verging toward u in urge, marked i.
stir birth’right girth girl’ish ness
first gird’le thirst mirth’ful ness
firm irk’some firth thir’ti eth
skirt vir’gin smirch flirt’ing ly
- Regular Long Sound of O, as in old, marked o.
host po’et chrome fo’lio
smoke to’ry blown glo’ri fy
sport lo’cate scold o’pi ate
slope so’lo droll po’et ry

#### Section: 38 Eclectic Series.
Lesson 45.
- Regular Short Sound of O, as in not, marked o.
bond mon’ster croft lon’gi tude
frost pot’ter sconce prompt’i tude
lodge lodg’ment mosque nom’i nate
prong yon’der frond ob’li gate
- Sound of O like short u, as in dove, marked o.
month blood’shed sponge cov’ert ly
glove love’ly tongue cov’e nant
shove noth’ing flood broth’er hood
front cov’et blood moth’er Iy
Lesson 46.
- Sound of O like oo long, as in do, marked o.
whom tour’ist group who ev’er
move rou tine’ prove shoe’-mak er
tour through out’ douche en tomb’ment
shoe en tomb’ youth mov’ing ly
- Sound of O like oo short, as in wolf, marked o.
wolf bo’som em bo’som wol ver ene’
would wom’an un bo’som wom’an ly
could wolf ‘ish wom’an hood wom’an ish
should wolf ‘-net worst’ed wolf ‘ish ly

#### Section: Spelling-Book. 39
Lesson 47.
- Sound of 0 like a (broad a), as in form, marked o.
born tort’ure corpse form’al ist
horn fork’ed thorn cor’mo rant
morse’ for’mer scorn hor’ta tive
lorn for’ward scorch mor’ti fy
- Another mark has been added in this book to indicate a sound of O where it precedes r, as in work, marked o.
work wor’thy worse wor’thi ly
word wor’ship world world’li ness
worm ef ‘fort whorl wor’ship er
wort world’ly whort work’ing-man
Lesson 48.
- Regular Long Sound of double 0, as in moon, marked 00.
tool moon’shine groom boor’ish ness
noon noon’tide school gloom’i ly
spool bloom’ing soothe room’i ness
groove gloom’y smooth sooth’say ing
- Regular Short Sound of double O, as in wool, marked oo.
wool hood’wink brook coop’er age
look look’out crook rook’er y
rook wood’land shook book’-bind er
hood wool’ly stood crook’ed ness

#### Section: 40 Eclectic Series.
Lesson 49.
- Regular Long Sound of U, as in mute. marked u.
sue beau’ty deuce beau’ti ful
lieu feud’al sluice cu’ti cle
nude cu’bic juice mu’ti ny
suit flu’id fugue pu’ri ty
- Regular Short Sound of U, as in but, marked u.
lungs slum’ber clump but’ter y
plush rus’set stunt cus’to dy
dunce duch’ess skulk 1ux’u ry
trump scuf ‘fle young sum’ma ry
Lesson 50.
- Sound of U when preceded by r in the same syllable, as in rude, marked u. It is the same sound as oo.
true ru’mor prune cru’di ty
crude ru’ral truce rhru’ma tism
cruse truf fle spruce pru’dent ly
rule bru’tish cruise pru’ri ent
- Sound of U like that of short oo, as in put, marked u.
bull pul’pit ful’ly ful fill’ment
pull pul’ley bush’y bul’le tin
put cush’ion puss’y bull’ion ist
push bul’wark butch’er bush’i ness

#### Section: Spelling-Book. 41
Lesson 51.
- Sound of U before r in such words as urge, marked u.
urge jour’ney spurn ur’gen cy
burn stur’geon nurse curl’i ness
spur church’man curst jour’nal ist
curb bur’gess burst hurt’ful ness
- Regular Long Sound of Y, as in fly, marked y.
ap ply’ ty’rant pyre dy’nas ty
de ny’ hy’dra type an’ti type
re ly’ ty’phus fyke a sy’lum
re ply’ ty’ro chyme hy e’na
Lesson 52.
- Regular Short Sound of Y, as in hymn, marked y.
pyx sys’tem lymph sym’me try
cyst syn’tax nymph syn’co pe
tymp phys’ic tryst syn’dic ate
Styx lyr’ic rynd syn op’sis
- The sound of oi or oy (unmarked), as heard in oil, oyster.
oint re coil’ spoil en joy’ment
voice re joice’ moist dis joint’ed
troy de stroy’ broil em ploy’ment
poise em ploy’ choice ap point’ment

#### Section: 42 Eclectic Series.
Lesson 53.
- The sound of ow (unmarked), as heard in owl. When the ow is sounded as in blown, the o is marked long (blown).
howl al low’ crowd flow’er y
gown en dow’ prowl pow’er ful
cowl vow’el scowl em bow’el
down row’el brown en dow’ment
- The diphthong ou has two leading sounds: that of ow in words derived from the Anglo-Saxon, as in out; and that of oo in words derived from the French, as in soup.
sour found’ling fount an nounce’ment
pout ground’less mount un found’ed
soup rou lette’ croup crou’pi er
roup group’ing wound trou’ba dour
Lesson 54.
- The consonant C has two regular sounds: as soft c in cede, marked c; as hard c in cot, where it has the sound of k, and is marked c.
cives ac’id trace De cem’ber
mace sol’ace brace in ces’sant
clot tac’tic curd en act’ment
acts traf’fic cave e lect’or
- The sound of N as heard in link, is marked thus, n, which is the same sound as that represented by ng.
lank monk’ey drink con’gru ous
monk con’gress trunk sin’gu lar
sunk lan’guage conch drunk’en ness

#### Section: Spelling-Book. 43
Lesson 55.
- S bas two regular sounds: when unmarked it has its sharp or hissing sound, as in yes; when marked thus, s, it has the buzzing sound of z in zeal.
sick mass’y smelt pos sess’ive
pest vest’ment gross as sess’or
has a muse’ grows re sem’ble
ease in fuse’ ruse res’o nant
- Ch has three sounds: unmarked (English ch), it has nearly the sound of tsh, as in child; marked thus, eh (French ch), it has the sound of sh, as in chaise; and marked thus, ch (Latin ch), it has the sound of k, as in chorus.
such speech’less child choc’o late
chef ma chine’ chaise chiv’al ry
chasm chem’ist chrism char’ac ter
Lesson 56.
- G has two regular sounds: marked thus, g ( g hard), it has the sound of g in go; marked thus, g ( g soft), it has the compound sound of j, as in gem.
gear’ing gew’gaw slug gid’di ness
gen’tile slug’gish crag guil’lo tine
gen’der gest’ure gibe gen’er al
- Th has two sounds: its sharp sound, as in thing, which is unmarked, and its soft sound, as in thine, marked th.
thin the’ist breath myth’ic al
thaw the’sis theft the’o ry
this gath’er thine hith’er to
than both’er breathe oth’er wise

#### Section: 44 Eclectic Series.
Lesson 57.
- X has three sounds: its regular sharp sound (unmarked) like ks, as in expect, and its soft or flat sound like gz, as in exist, marked x;. At the beginning of words x has the sound of z as in xebec (ze’bec).
ex’it ex pan’sive’ ex tra’ne ous
ex cel’ ex’pi ate ex te’ri or
ex alt’ ex am’ple ex ec’u tive’
ex empt’ ex ult’ant ex or’di um
- Q is followed in all cases by u, and has usually the sound of kw, as in queen; but in a few words derived from the French, qu is sounded like k, as in coquette.
quack queer’ly quoit qui e’tus
queen quo’rum quote quo ta’tion
plaque piqu’ant bisque co quet’tish
clique’ co quet’ torque piqu’an cy
Lesson 58.
cas cade’ a base’ in clude’ a larm’
ex change’ a maze’ ad jure’ a far’
in flame’ a brade’ de pute’ re mark’
ob late’ cru sade’ re fuse’ de bark’
par take’ de base’ ma nure’ em bark’
ad dress’ re gret’ in ject’ ac quit’
re flex’ ex cept’ in vent’ a drift’
ar rest’ ex pect’ mo lest’ re miss’
con test’ ex pend’ op press’ be fit’
de press’ ex press’ re dress’ per sist’

#### Section: ` Spellingbook. 45
Lesson 59.

#### Section: Homophonous Words.
NOTE.–These exercises on words of similar sound, instead of being gathered into a single department, are interspersed throughout the book.
raised, lifted up. plait, a fold.
razed, destroyed. plate, flattened metal.
pries, inspects closely. plumb, perpendicular.
prize, to value. plum, a fruit.
pray, to supplicate. place, site; spot.
prey, a spoil. plaice, a fish.
pore, a small opening. please, to gratify.
pour, to cause to flow. pleas, excuses.
poll, the head. bell, a sounding vessel.
pole, a rod; a perch. belle, a fine young lady.
Lesson 60.
bight, a bay. piece, a part.
bite, to seize with the teeth. peace, quietness.
bloat, to swell. new, not old.
blote, to dry and smoke. knew, did know.
board, a plank. gnu, a quadruped.
bored, did bore. limb, a branch.
bread, food. limn, to draw or paint.
bred, reared. arc, part of a circle.
blue, a color. ark, a vessel.
blew, did blow. prays, supplicates.
boar, the male swine. praise, honor.
bore, to pierce. preys, spoils.

#### Section: 46 Eclectic Series,
Lesson 61.
ab rupt’ dis cuss’ a cross’ a gree’
an nul’ de duct’ a dopt’ a sleep’
con struct’ in duct’ a loft’ es teem’
in struct’ re but’ a non’ de cree’
in trust’ re sult’ be long’ de gree’
at tire’ in vite’ com port’ dis close’
en tice’ o blige’ re port’ dis pose’
en tire’ per spire’ con sole’ re store’
in cline’ sub lime’ re pose’ en throne’
in cite’ sur vive’ con voke’ ex plode’

#### Section: Spelling-Book. 47
Lesson 62.
Dost consider that dust thou art? He paid the servant his hire, and the wages were higher than last year. With whoop and hurra they tore the hoop from the barrel. The mower will cut more grass to-morrow. The foreign consul took counsel with the enemy, and called a council of war. English consols are high. Kings are sometimes guilty of flagrant wrongs. Many a fragrant flower blooms unseen. He tore his clothes in a struggle to close the door. His course toward that coarse lad was wrong.
Lesson 63.
Words accented on the first Syllable.
con’tact nos’tril cur’ry pun’gent
for’est prod’uct ful’crum rus’tic
hob’by prob’lem hud’dle rub’bish
loft’y ros’ter pub’lic sulk’y
log’ic tor’rent pub’lish sul’try
af ‘flux bank’rupt kin’dred scrib’ble
am’bush cam’phor pick’et trip’let
an’them hav’oc tick’et trick’le
an’nals hag’gard wick’et liz’ard
as’pect hatch’et in’voice vil’la

#### Section: 48 Eclectic Series.
Lesson 64.
cam’bric de’ist cy’press trib’al
ca’dence e’qual Fri’day cri’sis
da’tive free’dom ice’berg hy’drant
na’tive need’ful li’bel sci’ence
pave’ment meet’ing mi’grate si’lent
duke’dom boun’ty pow’der boy’hood
dur’ance coun’ty prow’ess clois’ter
cu’beb cow’ard sound’ings joy’ous
pu’trid drow’sy tow’el loi’ter
pur’ist fount’ain tow’er loy’al
Lesson 65.
beard build palm verse witch
crease built calf search script
eaves squint half fern guess
heave live talk kern start
leap stick walk sperm wrath
knee cliff chalk serve floor
spleen writ lawn were czar
have bronze daub herb haunch
frank buzz fault strength flaunt
slake snatch spawn sneak haunt
smack dredge drift purse sharp
clamp church fund clutch kneel

#### Section: Spelling-Book. 49
Lesson 66.
en no’ble, in duce’ment a bu’sive,
e lope’ment a cu’men pe ru’sal
ex po’nent ac cu’sant pur su’ant
he ro’ic al lure’ment re fus’al
pro mo’tive a muse’ment sul phu’ric
de tach’ment es tab’lish at tend’ant
dog mat’ic fa nat’ic as sem’blage
dra mat’ic fan tas’tic ap pend’ant
ec stat’ic gi gan’tic in tes’tate
e las’tic in hab’it com’pen sate
Lesson 67.
cit, a citizen. wreak, to revenge.
sit, to rest on a seat. reek, vapor.
duct, a channel. bier, a carriage for the dead.
ducked, plunged under. beer, fermented liquor.
chuff, a clown. rest, quietness; ease.
chough (chuf), a bird. wrest, to turn; to twist.
coin, metal stamped. ring, a circle.
coigne, a corner. wring, to twist.
cole, a kind of cabbage. rote, repetition.
coal, carbon. wrote, did write.
find, to discover. strait, a narrow channel.
fined, did fine; mulcted. straight, not crooked.
prints, calicoes. wave, an undulation.
prince, a king’s son. waive, to refuse.
Sp.4.

#### Section: 50 Eclectic Series.
Lesson 68.
bole, the body of a tree. hist, hush!
bowl, a vessel. hissed, did hiss.
boll, a pod. paws, the feet of beasts.
nose, part of the face. pause, a stop.
knows, does know. faun, a sylvan god.
mote, a particle. fawn, a young deer.
moat, a ditch. pride, vanity.
toled, allured. pried, did pry.
told, did tell. wain, a wagon.
tolled, did toll. wane, to decrease.
rein, part of a bridle. see, to behold.
rain, falling water. sea, a body of water.
reign, to rule. si, a term in music.
Lesson 69.
a float’ post pone’ di lute’ de mure’
be low’ pro rogue’ a new’ de plume’
be moan’ dis course’ dis use’ re cruit’
be stow’ de port’ en sue’ re cluse’
de plore’ re mote’ im bue’ re fute’
a breast’ at tempt’ a bridge’ e clipse’
a head’ dis tress’ dis miss’ e vince’
be friend’ con nect’ a midst’ ex tinct’
be held’ bur lesque’ be twixt’ for give’
in flect’ de flect’ be witch’ in flict’

#### Section: Spelling Book. 51
Lesson 70.
au stere’ de crease’ ap peal’ dis creet’
be queath’ in crease’ ap pear’ en treat’
re vere’ de mean’ ap pease’ ex treme’
be seech’ fu see’ ar rear’ gran dee’
bo hea’ re peal’ blas pheme’ im peach’
a light’ de scribe’ ac quire’ dis guise’
a wry’ de spise’ at trite’ es quire’
be guile’ pre scribe’ as sign’ ig nite’
be lie’ de cline’ de mise’ in quire’
de prive’ re quite’ com prise’ ma lign’
Lesson 71.
Words accented on the Penult.
a mend’ed con tent’ed di lem’ma
an gel’ic re flect’ive dis tem’per
ap pen’dix de crep’it do mes’tic
as sem’bly de fend’ant em bel’lish
as sess’ment de mer’it em bez’zle
pa rent’al re fresh’ing re dun’dant
po et’ic re plen’ish a sun’der
pre sent’ed re sent’ment con cur’rent
pu tres’cent re splen’dent ef ful’gent
pre vent’ive sur ren’der en cum’ber

#### Section: 52 Eclectic Series.
Lesson 72.
Trisyllables with the short Sounds of the Vowels.
ac quit’tal de liv’er in sip’id
be nig’nant di min’ish in trin’sic
be wil’der con sist’ent ma lig’nant
com mit’ment con tin’gent pa cif’ic
con sid’er e nig’ma pro hib’it
a bol’ish car bon’ic em bod’y
ab hor’rent co los’sus har mon’ic
ad com’plish de mol’ish im pos’tor
ad mon’ish a pos’tate la con’ic
al lot’ment des pot’ic ma son’ic
Lesson 73.
hart, the male deer. hour, sixty minutes.
heart, the seat of life. our, belonging to us.
hear, to perceive by the ear in, within.
inn, a hotel.
here, in this place. key, a fastener.
heard, did hear. quay (ke), a wharf.
herd, a drove. rhyme, poetry.
hie, to hasten. rime, white frost.
high, lofty. knot, a fastening of cord.
him, objective case of he.
hymn, a song of praise. not, negation.
hole, an opening. know, to understand.
whole, all; entire. no, not so.

#### Section: Spelling-Book. 53
Lesson 74.
The Vowel in the last Syllable silent.
ba’con sweet’en dam’son bit’ten
to’ken trea’son fat’ten driv’en
bra’zen weak’en flax’en kit’ten
ha’ven wea’sel glad’den pris’on
ha’zel height’en hap’pen quick’en
maid’en light’en mad’den ris’en
ma’son lik’en rav’el smit’ten
ra’ven rip’en sad’den stiff ‘en
shak’en tight’en red’den swiv’el
wea’zen wid’en fresh’en writ’ten
tak’en bro’ken o’pen fast’en
wak’en clo’ven leav’en glis’ten
spok’en froz’en length’en drunk’en
dea’con gold’en reck’on mut’ton
Lesson 75.
The Vowel in the last Syllable not silent.
cray’on asp’en tal’on glu’ten
de’mon cab’in wag’on cit’ron
ci’on drag’on sud’den kitch’en
si’phon flag’on fel’on mit’ten
co’lon lin’den lem’on pis’ton
o’men grav’el mel’on her’on
bar’rel bev’el chan’nel flan’nel
par’cel plat’en chick’en slov’en

#### Section: 54 Eclectic Series.
Lesson 76.
Dissyllables with the long Sounds of the Vowels.
a’gue fa’mous cai’tiff ci’pher
ca’lyx fail’ure fra’cas high’land
cha’os faith’ful gate’-way mo’hair
dai’ly frail’ty name’sake oak’um
dai’sy game’ster stra’tum poul’tice
bea’dle neat’ly mea’sles trea’cle
bea’ver clear’ance peo’ple trea’tise
drear’y cre’dence le’gion treat’ment
ea’ger flee’cy re’gion twee’zers
mean’ness greed’y stee’ple wea’ry
Lesson 77.
Words ending with ow, the last Letter being silent.
ar’row sal’low fel’low win’dow
har’row tal’1ow mel’low win’now
nar’row shal’low fal’low wid’ow
mar’row shad’ow mead’ow bor’row
spar’row el’bow bil’low mor’row
Words containing ei or ie, promiscuously arranged.
grieve re trieve’ be siege’ de ceiv’er
thieve ag grieve’ bre vier’ de ceit’ful
ceiled a piece’ de ceive’ dis sei’zin
pieced con ceit’ re lief ‘ a chiev’ing
sheik be lieve’ re lieve’ re ceiv’er

#### Section: Spelling-Book. 55
Lesson 78.
aught, any thing. oar, for rowing.
ought, should. ore, unrefined metal.
wry, crooked. o’er, over.
rye, a kind of grain. ow’er, one who owes.
lead, a metal. adds, joins to.
led, did lead. adz, a joiner’s tool.
read, perused. ale, a liquor.
red, a color. ail, to feel pain.
read, to peruse. ate, did eat.
reed, a plant. eight, twice four.
all, the whole. ant, an insect.
awl, a sharp instrument. aunt, a relation.

#### Section: 56 Eclectic Series
Lesson 79.
bald, without hair. air, the atmosphere.
bawled, cried out. ere, before.
bad, ill; vicious. e’er, ever.
bade, past tense of bid. heir, one who inherits.
baize, a kind of cloth. aisle, walk in a church.
bays, plural of bay. isle, an island.
bear, an animal. I’ll, I will.
bare, naked. cere, to cover with wax.
bay, part of the ocean. sear, to burn; dry.
bey, a Turkish officer. seer, a prophet.
be, to exist. ball, a round body.
bee, an insect. bawl, to cry out.
Lesson 80.
gai’ter plant’ain shriv’el jaun’dice
clev’er das’tard jos’tle si’lex
paint’er scab’bard but’ton mas’tiff
way’ward scaf ‘fold pic’nic sar’casm
di’gest sham’bles grum’ble tar’nish
light’ning tran’script hus’tle tar’tar
por’trait nest’ling mur’rain ha rangue’
nov’ice men’ace rum’ble re lapse’
Tues’day pen’ance troub’le pro fess’
cli’mate shep’herd ar’gue re venge’
wrist’let whole’some pin’cers flight’y

#### Section: Spelling-Book. 57
Lesson 81.
To essay the task, requires courage. The discourse was an able essay. An agent will assay the ore, and forward a receipt. Con­temn a mean act; but do not always condemn the actor. They were to seize the fort, and cease firing. They affect great grief; but do not effect their purpose. Do you dissent from my opinion? The hill was difficult of descent. A decent regard for others’ ills is human. They advise the young to take the advice of the old. The enemy will invade the rich province. They were strongly inveighed against.
Lesson 82.
ed’u cate em’er y meth’od ist
eb’on y ex’o dus pen ‘i tent
ef ‘fi gy fel’o ny sen’ti nel
el’e phant gen’e sis fel’low ship
em’bas sy fed’er al res’i dent
ad’mi ral can’ni bal myr’i ad
ag’ o ny fac’to ry slip’per y
al’i ment gal’ler y min’u end
al’co hol man’u al tyr’an ny
am’nes ty par’a sol sym’pho ny

#### Section: 58 Eclectic Series,
Lesson 83.
mul’ber ry cul’ti vate am’ulet
mus’cu lar jus’ti fy an’ces try
pun’ish ment mul’ti ply Cal’va ry
sub’se quent mul’ti tude cav’al ry
sup’pli cant sub’sti tute mar’i gold
am’pli fy cam’o mile bat’ter y
grat’i fy pan’to mime can’o py
pac’i fy rad’i cal char’i ty
rar’e fy pat’ron ize chas’ti ty
sanc’ti fy sat’el lite maj’es ty
Lesson 84.
bail, surety. bold, brave.
bale, a pack of goods. bowled, did bowl.
bait, a lure. bourn, a limit.
bate, to lessen. borne, carried.
base, low; vile. bow, a weapon.
bass, a part in music. beau (bo), a man of dress.
beach, the shore. break, to sever by force.
beech, a kind of tree. brake, a thicket.
beat, to strike. bruise, to crush.
beet, a vegetable. brews (bruz), does brew.
bin, a box. by, near.
been (bin), existed. buy, to purchase.

#### Section: Spelling-Book. 59
Lesson 85.
berth, a sleeping-place. cast, to throw.
birth, coming into life. caste, an order or class.
braid, to weave. cede, to yield.
brayed, did bray. seed, to sow; to scatter.
breach, a gap. coarse, not fine.
breech, the hinder part. course, way; career.
broach, a spit; to pierce. dam, mother of beasts.
brooch, an ornament. damn, to condemn.
but, except. cane, a reed; a staff.
butt, a cask; a mark. Cain, a man’s name.
call, to name. ceil, to line the top of
caul, a kind of net-work. seal, a sea animal.
Lesson 86.
The ensign would not sign the paper. His design was known. He maligned his rival, and suffered condign punishment. A benign face. He was arraigned after the campaign. He deigned not to feign surprise. Squirrels gnaw the bark. He affirmed it with phlegm. The knight carried a knapsack. He had a knack for rhymes. She knew how to knead the dough. They cut the knot with a knife. The curfew tolls the knell of parting day. The knave had hard knuckles, but little knowledge.

#### Section: 60 Eclectic Series,
Lesson 87.
Sounds of O and U.
con’dor sol’id or’ange spon’dee
doc’trine loz’enge os’trich toc’sin
cos’tive of’fal pomp’ous jock’ey
fos’sil of ‘fice pon’tiff mot’ley
frost’y ol’ive prom’ise nos’trum
ton’nage nov’el cum’brous buck’le
won’der boot’y cus’tard bus’tle
won’drous move’ment flour’ish dud’geon
wont’ed stuc’co hun’dred dun’geon
wor’ry buz’zard hus’band lunch’eon
Lesson 88.
doub’le bed’stead eb’on fend’er
knuck’le cher’ub eph’od heav’y
nour’ish cres’cent es’sence heif ‘er
south’ ern crev’ice eth’ics jeal’ous
frus’trate dex’trous feath’er jel’ly
rep’tile ster’ile brim’stone ab’bess
ref ‘use ves’tige dic’tate ad’junct
sen’tence wed’lock frig’ate dag’ger
skep’tic Wednes’day pil’lage bram’ble
speck’le zeal’ous trib’ute cal’lous

#### Section: Spelling-Book. 61
Lesson 89.
cell, a small room. cart, a vehicle.
sell, to barter away. carte, a bill of fare.
cent, a small coin. dear, costly; beloved.
sent, did send. deer, an animal.
scent, odor; smell. due, owing; fit.
chased, did chase. dew (du), moisture ondensed.
chaste, pure.
clause, part of a sentence. doe, the female deer.
claws, the nails of a beast. dough, unbaked paste.
cord, a small rope. dram, a glass of spirits.
chord, musical tones drachm, a small weight.
in hamony fane, a temple.
cote, a pen; a fold. fain, gladly.
coat, an outer garment. feign, to pretend.
Lesson 90.
be speak’ ab solve’ ad judge’ in dulge’
nan keen’ de volve’ be grudge’ re pulse’
im plead’ dis solve’ sub duct’ suc cumb’
con ceal’ re solve’ be numb’ af front’
con geal’ re spond’ con vulse’ a mong’
re frain’ re print’ re proach’ re take’
re main’ re strict’ en croach’ re trace’
re strain’ re sist’ pa trol’ re pay’
re tain’ sub mit’ pa role’ de lay’
re tail’ dis tinct’ be fore’ al lay’

#### Section: 62 Eclectic Series.
Lesson 91.
dust, powdered earth. day, twenty-four hours.
dost, second person of do. dey, a Turkish title.
earn, to gain by labor. ewe (yu), a female sheep.
urn, a kind of vase. you, the person spoken to.
ern, the sea-eagle.
die, to expire. yew (yu), a kind of tree.
dye, to color. eye, the organ of sight.
draught (draft), drawing I, myself.
ay, yes.
draft, a bill of exchange. aye, an affirmative vote.
dun, a dark color. flee, to run away.
done, performed. flea, an insect.
fate, destiny. flew (flu), did fly.
fete, a festival. flue, a passage for smoke.
Lesson 92.
ag’ile hack’ney pas’sive bis’cuit
al’oes knap’sack prac’tice fil’bert
dac’tyl lad’der rab’id im’age
fash’ion lat’tice rap’id im’pulse
gal’ley lan’cet tac’tics mil’dew
bit’tern crys’tal crim’son kid’ney
brisk’et dis’tance grid’dle lin’tel
cis’tern dis’taff live’long liq’uid
chim’ney dwin’dle gyp’sy liq’uor
chis’el pick’le hith’er rid’dance

#### Section: Spelling-Book. 63
Lesson 93.
slui’cy bol’ster cer’tain driz’zle
jui’cy court’ship sur’ly tick’le
stew’ard fro’ward sur’geon twink’le
jew’el co’coa ear’nest thim’ble
neu’tral nose’gay jour’nal vil’lain
cor’ner gor’gon au’dit so’da
cor’sair lord’ship caus’tic so’fa.
corse’let mor’bid awk’ward so’ber
for’feit mort’gage gaud’y sto’ic
gor’geous mor’sel lau’rel to’paz
Lesson 94.
The awl is used by all shoe-makers. He said that he would do aught that he ought to do. The man who stole the bale of goods gave bail. The Bey rode a bay horse around the bay. Deer break through the brake and brush. He had just lain down in the narrow lane. The horse with the long mane ran through the main street of a town in Maine. Which of the pair of fine pears will you pare for the child? The joiner’s plane will smooth the plain door. You can rein your horse, if it should rain. The kings reign wisely.

#### Section: 64 Eclectic Series.
Lesson 95.
bal’us trade fab’ri cate bev’er age
al’ka li gal’ax y cher’u bim
al’ka line mas’to don dem’o crat
ap’o gee mack’er el den’i zen
al’i quot mar’i ner den’si ty
as’ter isk par’a graph ex’or cist
az’i muth par’al lax ed’i fy
bach’e lor par’a gon em’a nate
cal’a bash par’a pet em’pha size
cal’a mus par’a phrase ep’i cure
Lesson 96.
fir, a kind of tree. fort, a stronghold.
fur, soft hair. forte, one’s strong point.
faint, weak; languid. forth, forward.
feint, a pretense. fourth, the next after third.
fair, clear; handsome.
fare, food; cost of passage. frays, quarrels.
phrase, part of a sentence,
feet, plural of foot. fore, toward the front.
feat, an exploit. four, twice two.
floe, a large piece of ice. foul, impure.
flow, a current. fowl, a bird.
flour, ground wheat. freeze, to become ice.
flow’er, a blossom. frieze, a kind of cloth.

#### Section: Spelling-Book. 65
Lesson 97.
ex’pe dite’ ped’i ment cur’ren cy
hel’le bore pel’i can ful’some ly
per’i gee pet’u lant nul’li ty
reg’i cide rec’om pense sub’si dy
rec’on dite’ spher’ic al sub’ter fuge
fif’ti eth syn’o nym con’ju gate
mir’a cle tyr’an nize con’tro vert
nim’ble ness witch’er y con’se crate
rig’or ous wil’der ness cor’o net
ris’i ble whim’si cal dom’i nant
Lesson 98.
ar’bi trate hard’i hood for’mu la
ar’ma ment har’le quin gor’mand ize
ar’mis tice car’ni val or’der ly
ar’chi tect car’bon ate or’di nal
arch’er y gar’den er or’di nate
bar’ba rism gar’ni ture or’phan age
dec’i mal met’a phor crit’i cism
des’pot ism ed’it or cyl’in der
em’pha sis sen’a tor mys’ter y
ep’i taph ser’a phim mys’ti fy
leth’ar gy spec’i men phys’ic al
pen’ta teuch spec’u late typ’i fy
Sp. 5.

#### Section: 66 Eclectic Series.
Lesson 99.
Short and long Sounds of the Vowels.
but’ler com’mon dis’mal blem’ish
buck’ler dog’ma dis’trict elem’ent
cud’gel dol’phin mim’ic cher’ry
judg’ment hos’tile mis’sive cred’it
snuff ‘ers mod’ern syn’od em’bers
bond’age con’vent cli’max aid’ance
cot’tage soph’ist fi’brous bail’iff
for’age sor’rel hy’brid base’ment
hos’tage stop’ple hy’men brace’let
pros’trate tod’dy hy’phen brave’ly

#### Section: Spelling-Book. 67
Lesson 100.
furs, skins with soft hair. groan, a deep sigh.
furze, a prickly shrub. grown, increased.
gage, to pledge. gall, bile.
gauge, to measure. Gaul, old name of France.
gate, door; entrance. gild, to overlay with gold.
gait, manner of walking. guild, a corporation.
gilt, adorned with gold. gloze, to smooth over.
guilt, crime. glows, shines.
great, large; vast. guest, a visitor.
grate, a range of bars. guessed, did guess.
grease, soft fat. hale, sound; healthy.
Greece, a country. hail, frozen rain.
Lesson 101.
a lert’ ex pert’ sub vert’ re move’
as sert’ in ert’ su perb’ a do’
a ver’ in fer’ ab surd’ a loof ‘
a vert’ in sert’ re cur’ bal loon’
con cern’ in vert’ de mur’ buf foon’
per vert’ pre fer’ dis turb’ hal loo’
a vail’ re claim’ dis play” be fall’
a wait’ ab stain’ en tail’ re call’
de cay’ ac quaint’ ob tain’ en thrall’
de claim’ af fray’ con tain’ re sort’
de fray’ as suage’ per suade’ as sort’
pre vail’ block ade’ a broad’ be sought’

#### Section: 68 Eclectic Series.
Lesson 102.
al’pha pad’lock ad’dle hon’ey
an’ise plac’id bar’rack com’fort
brack’et Sab’bath man’date moth’er
dam’ask saf ‘fron man’ly oth’er
mad’der stag’nant stag’nate smoth’er
clos’et con’trite cher’ish ves’tal
com’ment oc’tave den’tist leg’ate
con’course vol’ume fresh’et mem’brane
con’text bon’fire rel’ish mes’sage
con’vex con’quer rem’nant res’cue
Lesson 103.
flout a fresh’ fir’kin a’er ate’
meant con temn’ serv’ile la’i ty
wren con tempt’ skir’mish de’vi ous
quick com mand’ ster’ling re’al ize
solve com mence’ sur’feit re’qui em
wrong com mend’ ur’gent co’gen cy
quince com pact’ fur’lough no’ti fy
shrimp com plaint’ jas’mine po’ten cy
cause es tray’ lack’ey o’ri ole
gauze ap proach’ latch’et o’ri ent
quoin cor rode’ mat’in jo’vi al
squaw cur tail’ scat’ter vo’ta ry
cross re pute’ sav’age zo’di ac

#### Section: Spelling-Book. 69
Lesson 104.
I accept all your presents except the last. His joy was in excess, at the news of his access to fortune. Though your terms exceed my ex­pectations, I must accede to them. The best cosmetic is air and exercise. He pretended to exorcise evil spirits. Both assent to go up the ascent. He was indicted for inditing a false letter. Champagne is made in France. The soldiers crossed the champaign. The law will levy a tax to build a levee. The levee was held at the mayor’s residence. The senior brother was addressed as seignior.
Lesson 105.
cer’ti fy for’ti fy cog’ni zance
fer’ti lize for’ti tude con’ju gal
herb’al ist fort’u nate glob’u lar
serv’i tude or’di nance or’i gin
ter’mi nate or’gan ism hom’i ly
fer’ven cy ar’bi ter af ‘flu ent
mer’cu ry ar’ter y bal’us ter
nurs’er y har’mo ny bar’ri er
per’fi dy lar’ce ny bar’ris ter
per’ju ry har’mo nize car’ri on

#### Section: 70 Eclectic Series.
Lesson 106.
cler’ic al fes’ti val li’bra ry
el’e gy eth’ic al like’li hood
em’i grant her’ald ry mi’cro cosm
em’per or her’e tic mi’cro scope
ep’i gram her’o ism ni’tro gen
pa’pa cy di’a lect ped’ant ry
fla’gran cy di’a gram ped’es tal
fra’gran cy di’a ry med’i cine
ra’di ance fin’er y lex’i con
sla’ver y i’vo ry sed’u lous
main’te nance pli’a ble quer’u lous
Lesson 107.
Monosyllables representing different Sounds.
stray sleet strike trope curse
ache fleece trite grope hearse
bathe steer splice broke purge
lathe speech stripe stroke scourge
plaint sphere tithe cloak verge
brain fief yield crock squeal
slave field fierce block league
quake thief pierce flock plead
stave fiend tierce shock squeak
plague shriek niece mock heath

#### Section: Spelling-Book. 71
Lesson 108.

#### Section: Synthetic Exercises.
Make Sentences containing the following Words.
bough, a branch of a tree. grieves, laments.
bow, to bend. greaves, armor for the legs.
brute, a beast. hew (hu), to cut; to chop.
bruit, to noise abroad. hue, a color; dye.
cite, to summon. Hugh, a man’s name.
site, a situation. kill, to deprive of life.
sight, the sense of seeing. kiln, a large oven.
climb, to ascend. leaf, of a tree or book.
clime, climate; region. lief, willingly; gladly.
core, the inner part. maze, an intricate place.
corps, a body of soldiers. maize, Indian corn.
creek, a narrow inlet. mean, low; middle point.
creak, a grating noise. mien, air; manner.
Lesson 109.
bul’let coop’er nor’mal pre cise’
bull’y wool’en or’phan pre side’
bull’ock cool’ly tor’por pro scribe’
bul’rush scoun’drel quar’ter com mode’
bush’el bal’sam ac claim’ en gross’
bull’ion squad’ron o paque’ con sume’
crup’per war’rant sca lene’ pre sume’
cuck’oo quad’rant se cede’ be dew’

#### Section: 72 Eclectic Series.
Lesson 110.
false naught pitch batch edge
quart sought flitch match hedge
sward bought stitch hatch ledge
swarm bright fitch latch wedge
thwart plight hitch patch fledge
bilge budge fosse breadth twinge
bridge judge thong breast print
ridge drudge notch cleanse fling
hinge grudge blotch friend string
cringe plunge prompt knell swift
Lesson 111.
hall, a large room. hoop, a ring; a band.
haul, to drag by force. whoop, to make a noise.
hay, dried grass. hied, made haste.
hey! an exclamation. hide, to conceal.
hare, an animal. hoard, to lay up.
hair, of the head. horde, a tribe.
heal, to cure. hoes, plural of hoe.
heel, hinder part of the foot. hose, stockings.
jam, a conserve of fruit.
hire, wages. jamb, the sidepiece of a
high’er, more high. door or fireplace.
hoe, a farming tool. knead, to work dough.
ho! an exclamation. need, want.

#### Section: Spelling-Book. 73
Lesson 112.
faith theme length sor’row sol’emn
scrape chime launch dur’ing hire’ling
strange whilst morgue gib’bet tres’pass
greet smart pledge bod’kin shil’ling
perch badge gourd gos’ling mat’tock
champ dodge schist lob’by ram’part
drench brawl flounce tan’sy tran’quil
squeeze dwarf screech lock’et cun’ning
grist yawl spasm van’dal her’ring
shrink grant starve ex’tra drug’gist
copse spunk scalp cut’lass spon’sor
Lesson 113.
knight, a title of honor. lee, the sheltered side.
night, time of darkness. lea, a meadow; field.
knave, a wicked person. lie, to deceive.
nave, hub of a wheel. lye, water passed through
ashes.
loan, any thing lent. links, parts of a chain.
lone, solitary. lynx, an animal.
knap, a small protuberance. loch, a lake.
nap, a short sleep. lough (lok), a lake.
lac, a kind of gum. lock, to fasten a door.
lack, to want; need. lax, loose; vague.
laid, placed. lacks, wants; needs.
lade, to load. lacs, plural of lac.

#### Section: 74 Eclectic Series:
Lesson 114.
Words containing I consonant, sounded like Y consonant; as alien, pronounced al’yen.
al’ien on’ion bat tal’ion
sav’ior bil’ious pe cul’iar
pan’nier brill’iant re bell’ion
un’ion fil’ial dis un’ion
sen’ior mill’ion o pin’ion
jun’ior pill’ion do min’ion
gal’liard pin’ion com mun’ion
span’iel trill’ion mut’u al
val’iant coll’ier punc til’io
bill’iards pon’iard punc til’ious
bill’ion ruff ‘ian ver mil’ion
In’dian Chris’tian aux il’ia ry
Lesson 115.
The following words, according to the analogy of the En­glish language, should he spelled with the termination er, with the exception of the last word of each line.
cen’ter mi’ter spec’ter sep’ul cher
fi’ber ni’ter o’cher the’a ter
lus’ter som’ber mau’ger ma neu’ver
mea’ger sa’ber um’ber cal’i ber
me’ter scep’ter om’ber ac cou’ter
a’cre na’cre lu’cre mas’sa cre

#### Section: Spelling-Book. 75
Lesson 116.
In the following words, ng is pronounced as if the g were doubled; as anger, pronounced ang’ger.
an’ger lan’guor jin’gle youn’ger
an’gle lan’guid min’gle con’ger
an’gry man’gle sin’gle bun’gler
an’guish man’go tin’gle hun’ger
clan’gor san’guine din’gle hun’gry
dan’gle span’gled lon’ger wran’gler
fan’gled span’gle lon’gest fin’ger
jan’gle tan’gle stron’ger lan’guish
ban’gle wran’gle bun’gle un’guent

#### Section: 76 Eclectic Series.
Lesson 117.
In the following, S has the sound of sh as sure, (pro. shure).
sure’ly cen’sure fis’sure is’su ance
sure’ness press’ure ton’sure as sur’ance
sure’ty is’sue as sure’ in sur’ance
sug’ar tis’sue in sure’ in sur’er
The following words are spelled, according to analogy, with the termination se.
con dense’ dis pense’ im mense’ pre tense’
de fense’ ex pense’ of fense’ sus pense’
re cense’ in cense’ pre pense’ li’cense
Lesson 118.
lane, a narrow passage. main, chief
lain, past participle of lie. mane, hair on the neck
of a horse.
mail, armor.
lapse, to fall. male, masculine.
laps, plural of lap. mark, a sign.
leak, to run out. marque, letters of reprisal.
leek, a kind of onion. mead, a drink.
lo! behold! meed, reward.
low, not high. meet, fit; proper.
lore, learning. mete, to measure.
low’er, more low. meat, food in general.
maid, a maiden. might, strength; power.
made, finished. mite, a small insect.

#### Section: Spelling-Book. 77
Lesson 119.
mode’, way; manner. nay, no.
mowed, cut down. neigh, to cry as a horse.
mule, an animal. nit, egg of an insect.
mewl (mul), to squall. knit, to unite.
mist, fine rain. gneiss, a kind of mineral.
missed, did miss.
more, a greater quantity. nice, delicate; fine.
mow’er, one who mows. owe, to be bound.
muse, to meditate. oh! alas!
mews (muz), an inclosure. ode, a poem.
owed, indebted.
none, not one. one (wun), a single thing.
nun, a religious woman. won, gained.
Lesson 120.
a mal’gam ate cheese e man’ci pate
as sas’sin ate dirt e rad’i cate
ca pac’i tate bleak e vac’u ate
co ag’u late goad a ban’don ment
con cat’e nate slouch in fat’u ate
con fab’u late gone in val’i date
con grat’ulate scarf be at’i fy
con tam’i nate nerve pro cras’ti nate
de cap’i tate raid re tal’i ate
e jac’u late graze e vap’o rate
e lab’o rate stale pre var’i cate

#### Section: 78 Eclectic Series.
Lesson 121.
cir’cus ca pac’i ty an’a gram
cur’few com par’i son am’bi ent
cur’tain com par’a tive al’li gate
fer’tile com pat’i ble cal’a mine
fer’vid con cav’i ty hal’cy on
fur’nace de clar’a tive Jes’u it
fur’long di ag’o nal ped’i gree
mer’maid di am’e ter reg’is ter
nerv’ous dog mat’ic al rev’el ry
pur’chase em bas’sa dor skep’tic al
sur’face de prav’i ty ver’i ly
Lesson 122.
In words like the following, sier, zier, sure, zure, su, sion, and sia are pronounced zhur, zhur, zhu, zhun, and zha.
bra’sier em bra’sure cas’u al ly
gla’zier e ras’ure cas’u ist ry
gra’zier e va’sion treas’ur er ship
ras’ure in va’sion us’u al ly
seiz’ure, per sua’sion pleas’ur a ble
ho’sier ad he’sion meas’ur a ble
o’sier co he’sion oc ca’sion al
fu’sion am bro’sia pro vis’ion al
az’ure, dis clos’ure u su’ri ous
meas’ure ex plo’sion dis com pos’ure
pleas’ure col lu’sion in de cis’ion

#### Section: Spelling-Book 79
Lesson 123.

#### Section: Synthetic And Dictation Exercises.
brid’al, belonging to a bride. met’al, a substance.
met’tle, spirit.
bri’dle, a check; a curb. vice, defect; fault.
les’son, a task for recitation. vise, an instrument.
wail, to lament.
less’en, to make less. wale, to mark with stripes.
Filled with choler, he seized the youth by the collar. The priest filled the censer. He is a censor of the press. The ship took divers persons as divers for pearls. The plaintiff assumed a plaintive air. To lessen the number of exercises, will make an easier lesson.
Lesson 124.
scrive’ner friv’o lous fru gal’i ty
slug’gard im’age ry gram mat’ic al
stub’born in’di go hi lar’i ty
sub’urbs in’sti gate hu man’i ty
symp’tom liq’ui date in hab’it ant
med’ley pil’grim age i ras’ci ble
peas’ant fish’er y le gal’i ty
pheas’ant hick’o ry lo cal’i ty
pen’sive in’ter est lo quac’i ty
pres’ence mit’ti mus men dac’i ty
read’y min’strel sy ra pac’i ty

#### Section: 80 Eclectic Series.
Lesson 125.
NOTE.–These words are not exactly alike in sound, and should be carefully distinguished.
as sist’ance, help; relief rab’bit, an animal.
as sist’ants, helpers. rab’bet, a term in carpentry.
de vis’er, an inventor.
di vi’sor, a term in lin’e a ment, a feature.
Arithmetic. lin’i ment, an ointment.
def ‘er ence, respect. prin’ci pal, chief
dif ‘fer ence, variation. prin’ci ple, rule of action.
in gen’u ous, open; free. li’ar, one who tells lies.
in gen’ious, having skill. lyre, a kind of harp.
Lesson 126.
His assistants gave him great assistance. He was the deviser of the machine. Which is the larger, the divisor or the quotient? This difference being settled, he will pay due deference to your opinion. The ingenious me­chanic was also an ingenuous man. Not a lineament could be recognized by his friends. Apply to the wound a healing liniment. The principal in the agreement was devoid of moral principle. Though a great liar, he could play upon the lyre. The rabbit was tame. The carpenter will rabbet the boards.

#### Section: Spelling-Book 81
Lesson 127.
In words like the following, U should receive its proper con­sonant sound; as nature, pronounced nat’yur.
nat’ure sig’na ture ag’ri cult ure
creat’ure sep’ul ture leg’is la ture
feat’ure fur’ni ture ar’chi tect ure
fut’ure for’feit ure tem’per a ture
capt’ure lig’a ture lit’er a ture
rapt’ure ap’er ture flo’ri cult ure
text’ure quad’ra ture ju’di ca ture
pict’ure ad vent’ure hor’ti cult ure
script’ure con ject’ure man u fact’ure
Lesson 128.
pail, a wooden vessel. Paul, a man’s name.
pale, not bright. pall, a covering.
pear, a fruit. pique, to give offense.
pare, to cut thin. peak, the top.
pair, a couple. peer, a nobleman.
raze, to pull down. pier, a wharf
raise, to lift up. quartz, a kind of rock.
rays, beams of light. quarts, measures.
pain, uneasiness. plain, smooth.
pane, a square of glass. plane, a surface; tool.
peel, rind; skin. quire, twenty-four sheets of
peal, a sound of bells. paper
port, a harbor. choir (kwir), a band of
Porte, a Turkish court. singers.
Sp.6.

#### Section: 82 Eclectic Series.
Lesson 129.
X with the sound of gz; as exact, pronounced egz act’.
ex act’ ex act’ly ex ag’g’er ate
ex ist’ ex am’ine ex an’i mate
ex ult’ ex em’plar ex as’per ate
ex hale’ ex er’tion ex ec’u trix
ex haust’ ex hib’it ex hil’a rate
ex ert’ ex ist’ence ex on’er ate
ex hort’ ex ist’ent ex em’pli fy
ex ude’ ex ot’ic ex or’bi tant
ex ergue’ ex haust’ive ux o’ri ous
Lesson 130.
Ti has often the sound of sh: followed by on, it is pronounced shun.
na’tion ces sa’tion de vi a’tion
pa’tient col la’tion dep re da’tion
fac’tious cre a’tion des per a’tion
frac’tious dic ta’tion lib er a’tion
sta’tion do na’tion me di a’tion
lo’tion du ra’tion mod er a’tion
mo’tion e qua’tion nu mer a’tion
no’tion tes ta’tion op er a’tion
po’tion for ma’tion tol er a’tion
por’tion frus tra’tion trep i da’tion
quo’tient gra da’tion val u a’tion

#### Section: Spelling-Book 83
Lesson 131.
Other examples in which final tion is pronounced shun.
men’tion ab strac’tion ed u ca’tion
sec’tion at trac’tion em ula’tion
frac’tion de trac’tion ex cla ma’tion
dic’tion dis trac’tion ex pec ta’tion
fic’tion ex trac’tion ex por ta’tion
fric’tion in frac’tion fer men ta’tion
junc’tion pro trac’tion gen er a’tion
ac’tion re frac’tion grav i ta’tion
cap’tion re trac’tion hab i ta’tion
op’tion con trac’tion il lus tra’tion
fac’tion sub trac’tion im por ta’tion
Lesson 132.
Examples in which sci, ti, and ci have the sound of sh.
auc’tion au da’cious ab er ra’tion
cau’tion ca pa’cious ad mi ra’tion
cau’tious ve ra’cious ad o ra’tion
gla’cial fal la’cious ad u la’tion
gra’cious fu ga’cious ag gra va’tion
spa’cious lo qua’cious ap pli ca’tion
Gre’cian ra pa’cious ap pro ba’tion
spe’cious sa ga’cious prep a ra’tion
par’tial te na’cious pres er va’tion
con’science vi va’cious proc la ma’tion
spe’cie vo ra’cious prof a na’tion

#### Section: 84 Eclectic Series.
Lesson 133.
Ci, ce, and si with the sound of sh.
spe’cies ju di’cial ac ces’sion
o’cean lo gi’cian com pres’sion
so’cial ma gi’cian de clen’sion
spe’cial mu si’cian ex pres’sion
cru’cial tac ti’cian im pres’sion
pre’cious op ti’cian op pres’sion
pas’sion pa tri’cian pre ten’sion
man’sion phy si’cian suc ces’sion
pen’sion pro vin’cial trans gres’sion
ten’sion fi nan’cial ad mis’sion
tor’sion om nis’cient con cus’sion
Lesson 134
They propose to alter the place of the altar. He cast his ballot for mayor. The ballet dancer and the ballad singer arrived. The wine seller lived in a cellar. He said that the cymbal was a symbol of music. They sent an arrant rogue on the errand. His manner of conducting the manor did not suit the lord. The prophet of Mammon foretold great profit. The relics of the kingdom were saved by the relict of the king. The stature of the statue of Liberty is fixed by statute.

#### Section: Spelling-Book. 85
Lesson 135.
rack, an engine of torture. write, to make letters.
wrack, a sea-plant. wright, a workman.
rap, to strike. roe, eggs of a fish.
wrap, to roll together. row, to impel with oars.
reck, to heed; to care. rose, a flower.
wreck, destruction. rows, does row.
rice, a kind of grain. roes, plural of roe.
rise, increase; ascent. sees, beholds.
rite, a ceremony. seas, large bodies of water.
right, not wrong. seize, to lay hold of
Lesson 136.

#### Section: Of Affixes.
Many words are formed by adding something to the end of another word. The added part is called an affix; as ly, added to man, forms manly. In this, and the following seventeen les­sons, the more common affixes are indicated.
Plurals formed by adding s to the Singular.
roofs so’los ty’ros al bi’nos
hoofs ha’los jun’tos me men’tos
scarfs las’sos can’tos oc ta’vos
truths ze’ros quar’tos si roc’cos
Plurals formed by adding es to the Singular.
ech’oes to ma’toes po ta’toes
car’goes mu lat’toes bra va’does
mot’toes vol ca’noes por’ti coes
grot’toes mos qui’toes vi ra’goes

#### Section: 86 Eclectic Series.
Lesson 137.
Words in which f and fe are changed into ves in the Plural: as, leaf, leaves; wife, wives.
beeves lives thieves calves our selves’ sheaves wives wolves halves them selves’ leaves knives loaves shelves your selves’
Words in which Y final is changed into ies in the Plural.
skies la’dies to’ries gro’cer ies
spies du’ties can’dies for’ger ies
cries beau’ties tro’phies gal’ler ies
Lesson 138.
Words ending in Y which form the Plural by adding a.
toys chim’neys al’leys at tor’neys
drays val’leys pul’leys Sat’ur days
buoys mon’eys tur’keys hol’i days
whys jour’neys mon’keys cor du roys’
Words in which the Plurals are formed irregularly. As the Plural only is given, the teacher might require the pupil to ascertain the Singular, and to spell it.
mice cri’ses ter’mi ni { kine, cows }
chil’dren neb’u lae a lum’ni { staves, staffs}
ver’te brae { broth’ers,breth’ren } { pease, peas}
stra’ta syn op’ses geese { dies, dice}

#### Section: Spelling-Book. 87
Lesson 139.
Ing signifies continuing to; as talkin g, continuing to talk. The following words, in taking their suffix, double the final letter. The last letter is doubled when the word ends with a single consonant preceded by a single vowel.
plan’ning win’ning stop’ping a bet’ting
fret’ting blot’ting gun’ning re bel’ling
bid’ding rob’bing shut’ting o mit’ting
Other words ending with consonants, which do not double the final letter.
act’ing fail’ing mean’ing ex pand’ing
land’ing rain’ing coax’ing con sent’ing
build’ing sail’ing suit’ing vis’it ing

#### Section: 88 Eclectic Series.
Lesson 140.
Words ending in e silent, generally drop the e in adding ing.
mak’ing seiz’ing rul’ing ex pir’ing
nam’ing forc’ing lin’ing re fus’ing
plagu’ing hedg’ing squeez’ing in trigu’ing
ach’ing writ’ing schem’ing alleg’ing
The final e is retained when it is necessary to prevent a change of pronunciation, or to maintain the identity of a word.
hoe’ing shoe’ing change’a ble
toe’ing singe’ing trace’able
tinge’ing dye’ing peace’a ble
foe’man blue’ness charge’a ble
Lesson 141.
Ed, as a suffix, generally signifies did. In words like the following the e in ed is silent, and the wards, though of two and three syllables, are pronounced in one and two.
blazed wedged boiled be reaved
drained solved coiled be sieged’
hailed called soiled blas phemed’
lamed hauled bowed ac quired’
paved mauled crowned con trol1ed’
stowed warmed plowed a bused’
saved warned roused ac cused’
feared warped scoured com muned’
flowed proved soured con fused’
glued shoved dodged de coyed’
begged loved filled en joyed’

#### Section: Spelling·Book. 89
Lesson 142.
In words like the following, ed is pronounced as t; and, al­though of two and three syllables, the words are pronounced in one and two.
graced fixed es caped’ at tacked’
scraped mixed em braced’ con fessed’
cracked boxed en grossed’ op pressed’
In other words formed by the affix ed, the last letter is doubled in words of one syllable, or in words accented on the last syllable, when they end with a single consonant preceded by a single vowel; as, wed, wed’ded. If the word ends in any other consonant than d or t, the e in ed becomes silent, and the two syllables become one; as, hem, hemmed, pronounced hemd.
jut’ted shunned com pelled o mit’ted
fret’ted tapped e quipped’ im bed’ded
fit’ted rubbed de murred’ com mit’ted
Lesson 143.
Words not included in the ahove rule, do not double the final consonant.
act’ed failed quar’reled ex pand’ed
land’ed rained bar’reled mer’it ed
rest’ed coaxed trav’eled vis’it ed
Y is sometimes changed into i; as cry, cried.
cried dried mar’ried glo’ried
tried fried tar’ried sto’ried
shied spied car’ried wor’ried

#### Section: 90 Eclectic Series.
Lesson 144.
Ar, er, and or signify one who does, or that which does; as, baker, one who bakes. If the word ends in e, r only is added. After a consonant y is generally changed into i. Another letter is sometimes united to the affix; as law, law’yer. The final consonants are doubled, as in Lesson 142.
beg’gar bank’er bak’er cre a’tor
dig’ger plant’er pa’cer cru sad’er
dip’per build’er pav’er dic ta’tor
clip’per giv’er stran’ger en grav’er
trot’ter 1aw’yer writ’er sur viv’or
los’er saw’yer boast’er be liev’er
woo’er read’er mourn’er ad vis’er
vouch’er rid’er own’er as sign’er
wres’tler dy’er rul’er in vei’gler
Lesson 145.
Words formed by the Affixes er or or.
be gin’ner la’bor er nav’i ga tor
in dors’er rea’son er ded’i ca tor
de sert’er li’bel er cal’cu la tor
dis turb’er wag’on er spec’u la tor
u surp’er con’quer or pros’e cu tor
con duct’or for’eign er cul’ti va tor
tor ment’or cus’tom er mul’ti pli er
en chant’er mur’der er nu’mer a tor
sup port’er gov’ern or gen’er a tor
ag gress’or pen’sion er ra’di a tor

#### Section: Spelling-Book. 91
Lesson 146.
In adjectives, er is generally added to form the compara­tive, and est to form the superlative; as, rich, richer, richest.
strict’er fierc’est wealth’i er wor’thi est
broad’er slow’est greed’i er read’i est
bright’er gaunt’est drear’i er haugh’ti est
Ly is an abbreviation of like; as manly for man-like, or like a man. Ly is still further shortened into y; as, rock, rocky.
bright’ly eas’y heav’i ly thor’oug ly
gay’ly earth’y heart’i ly might’i ly
no’bly speed’y read’i ly has’ti ly
wind’y spon’gy tar’di ly stead’i ly
Lesson 147.
Ness is from the Saxon nesse, and means state or quality; as, neatness, state of being neat.
bleak’ness smooth’ness come’li ness
fierce’ness numb’ness drow’si ness
hoarse’ness wrong’ness naught’i ness
calm’ness sweet’ness wea’ri ness
The termination full adds its own meaning to the word; as, joyful, full of joy. The final l is omitted in the derivatives.
change’ful mourn’ful skill’ful fan’ci ful
fright’ful woe’ful will’ful pit’i ful
spite’ful wrath’ful aw’ful du’ti ful

#### Section: 92 Eclectic Series.
Lesson 148.
The termination less gives a negative meaning to the deriva­tive; as graceless, without grace.
brain’less sight’less friend’less worth’less
cease’less soul’less head’less house’less
guile’less friut’less guilt’less noise’less
The affix age signifies the pay for, a state of being, or composed of; as cartage, the pay for carting.
mar’riage fer’ri age vag’a bond age
herb’age her’mit age dis ad van’tage
wharf ‘age pat’ron age es’pi on age
Lesson 149.
The suffix al signifies relating to; an signifies pertaining to; ant and ent, in many instances, signify the agent or doer.
tid’al com’ic al me dic’i nal
ur’ban pub’li can di oc’e san
claim’ant as sist’ant i tin’er ant
a’gent pres’i dent cor re spond’ent
Able and ible signify that may be, capable of being, fit or worthy to be, or capacity.
eat’a ble blam’a ble am’i ca ble
sal’a ble laugh’a ble nav’i ga ble
leg’i ble for’ci ble com bus’ti ble
cred’i ble au’di ble in del’i ble

#### Section: Spelling-Book. 93
Lesson 150.
Ist, ster, ee, and ess, generally signify the person who, or thing which. The last is an affix denoting the feminine gender.
aur’ist phys’i cist pi a’nist
tap’ster chor’is ter for’est er
grant ee’ mort ga gee’ as sign ee’
em’press shep’herd ess mar’chion ess
Dom signifies the office of or state of bein g; hood, the state of being; ish, somewhat, like; and ism, the condition or doctrines of.
king’dom chris’ten dom hea’then dom
child’hood maid’en hood live’li hood
knav’ish yel’low ish a’gu ish
Bud’dhism Meth’od ism Mor’mon ism
Lesson 151.
Eer or ier generally signifies one who has charge of; en means made of, or, with adjectives, to make; ic signifies pertaining to, belonging to, or like; and ise or ize, to make, to become, or to assimilate.
cash ier’ fin an cier’ gon do lier’
cloth’ier en gi neer’ can non eer’
beech’en be hold’en em bold’en
bright’en en light’en en liv’en
civ’ic ce phal’ic me tal’lic
u’til ize cat’e chise crit’i cise
sat’ir ize civ’il ize os’tra cize

#### Section: 94 Eclectic Series.
Lesson 152.
Ion and ment denote the state of being, or the act of; fy, to make or become; ance or ence, the act or state of; ive, having a tendency to, or the power or nature of; ory, the power or nature of, or belonging to; and ous, partaking of, or full of.
dis per’sion di ver’sion as per’sion
ex cep’tion e lec’tion con di’tion
a tone’ment a gree’ment dec’re ment
de’i fy stu’pe fy sat’is fy
an noy’ance ac cord’ance con cord’ance
oc cur’rence ab hor’rence in dul’gence
a mu’sive con clu’sive of fen’sive
cur’so ry ar’mo ry man’da to ry
dan’ger ous li’bel ous har mo’ni ous
Lesson 153.
Kin, ling, let, and ule indicate smallness or diminution.
lamb’kin man’i kin la’dy kin
duck’ling un’der ling fos’ter ling
leaf ‘let riv’u let flag’eo let
glob’ule mol’e cule an i mal’cule
Some means like or same, full of, or very; ward denotes in the direction of; ure means state of; and y, full of, or composed of.
tire’some cum’ber some vent’ure some
east’ward heav’en ward aft’er ward
verd’ure cur’va ture im post’ure
smok’y sin’ew y sil’ver y

#### Section: Spelling-Book. 95
Lesson 154.
ruff, an article of dress. roar, to make a loud noise.
rough (ruf), uneven. row’er, one who rows.
retch, to vomit. sail, a sheet of canvas.
wretch, a miserable person. sale, the act of selling.
rode, did ride. seen, beheld.
road, a way; route. scene, a view.
rowed, did row. seine, a net for fishing.
room, an apartment. slay, to kill.
rheum, a serous fluid. sleigh, a vehicle on
runners.
sow, to scatter seed. sley, a weaver’s reed.
sew (so), to use a needle. seem, to appear.
so, thus; in like manner. seam, a line of junction.
Lesson 155.
rude, uncivil; rough. slow, not fast.
rood, fourth of an acre. sloe, a kind of fruit.
serf, a slave; servant. sun, the source of light.
surf, a swell of the sea. son, a male child.
serge, a kind of cloth. steel, refined iron.
surge, to rise; to swell. steal, to rob; to pilfer.
sheer, pure; clear. stile, steps over a fence.
shear, to cut or clip. style, manner of writing.
side, a part; a margin. stare, to look fixedly.
sighed, did sigh. stair, a step.
slew (slu), did slay. sweet, pleasing to the
taste.
slue, to slip aside. suite (swet), retinue.

#### Section: 96 Eclectic Series.
Lesson 156.

#### Section: Of Prefixes.
When a syllable or word is placed before another word, it is called a prefix. The prefix re generally gives the idea of repetition or return; as, recall, to call back.
re build’ re ap pear’ re an’i mate
re touch’ re as cend’ re gen’er ate
re seat’ re im burse’ re sus’ci tate
re view’ ro doub’le re ver’ber ate
The prefix un generally gives a negative meaning; as, unapt, not apt.
un paid’ un friend’ly un court’ly
un clean’ un health’y un ea’sy
un known’ un stead’y un fruit’ful
un nerve’ un err’ing un learn’ed
Lesson 157.
In, also, has a negative meaning; it often becomes im, il, ir, or ig, for the sake of sound.
in act’ive in sin cere’ ir res’o lute
im prop’er im po lite’ ir re lig’ious
il le’gal il lu’sive irre spect’ive
ig no’ble ig’no rant ir’ri ta ble
im ma te ri al’i ty im prac ti ca bil’i ty
in di vis i bil’i ty in de struc ti bil’i ty
in com pat i bil’i ty ir re sist i bil’i ty
in com press i bil’i ty im pen e tra bil’i ty

#### Section: Spelling-Book. 97
Lesson 158.
Dis is a Latin particle, and has the force of a negative or priv­ative; as, disagree, not to agree, disarm, to deprive of arms.
dis please’ dis ap pear’ dis con tin’ue
dis joint’ dis be lieve’ dis in her’it
dis lodge’ dis o blige’ dis or’gan ize
dis charge’ dis cour’age dis sim’i lar
dis grace’ dis cov’er dis crim’i nate
The prefix after conveys its own meaning.
aft’er piece aft’er noon aft’er most
aft’er guard aft’er math aft’er-thought
Lesson 159.
Post is a Latin word, meaning after.
post’script post-di lu’vi an post me rid’i an
post’-date post po si’tion post’hu mous ly
Other words are formed by prefixing the English word post, a letter-carrier.
post’al post’man post’mark
post’-chaise post’-town post’-office
post-haste’ post’boy post’mas ter
Bene is a Latin prefix, signifying well.
ben’e dict ben e fac’tion be nef ‘i cence
ben’e fice ben e fi’cial be nev’o lence
Sp.7.

#### Section: 98 Eclectic Series.
Lesson 160.
Fore adds its own meaning to the word; as foretaste, to taste before; pre is from the Latin prae, before; ante (Latin), before. Anti (Greek), means against or opposite.
fore’sight fore tell’er fore bod’ing ly
fore’most fore knowl’edge fore de ter’mine
fore know’ fore’cas tle pre med’i tate
pre fix’ pre cau’tion pre oc’cu py
pre judge’ pre ced’ing pre-em’i nent
pre serve’ pre des’tine an te pas’chal
pre sage’ an’te past an te mun’dane
pre text’ an’te date an te nup’tial
fore warn’ an’ti pode an ti cli’max
fore’front an’ti dote an ti feb’rile
Lesson 161.
The word miss signifies to err, to go wrong; in the compound the last s is omitted.
mis guide’ mis be lief ‘ mis reck’on
mis spell’ mis con ceive’ mis con’strue
mis choose’ mis di rect’ mis gov’ern
mis chance’ mis re cite’ mis guid’ance
Words formed by the prefixes up and under.
up raise’ un der lay’ un’der hand
up heave’ un der write’ un’der growth
up’right un der sign’ un’der brush
up’ward un der neath’ un’der shot

#### Section: Spelling-Book. 99
Lesson 162.
Words formed by the prefixes out and over.
out brave’ o ver reach’ o’ver board
out grow’ o ver awe’ o’ver alls
out pour’ o ver flow’ o’ver night
out talk’ o ver freight’ o’ver sight
Counter, from the Latin contra, against.
coun’ter pane coun’ter sign coun ter move’
coun’ter feit coun’ter point coun ter weight’
Extra (Latin), beyond.
ex tra ju di’cial ex tra phys’ic al
ex tra pro vin’cial ex tra trop’ic al
Lesson 163.
Semi (Latin), and hemi (Greek), ha1f; super (Latin), over or above; trans (Latin), beyond or through; and inter (Latin), among or between.
sem’i breve sem’i co lon sem’i qua ver
sem’i tone sem’i cir cle sem i ton’ic
hem’i sphere hem’i cy cle hem i morph’ic
hem’i trope hem i he’dral hem i spher’ic
su per add’ su per fi’cial su per in duce’
su per scribe’ su per’flu ous su per struct’ure
tran scend’ent trans at lan’tic tran’si to ry
trans fig’ure trans fus’i ble trans mis’si ble
in’ter course in ter mit’tent in ter reg’num
in’ter lude in ter ces’sor in ter sec’tion
100 ECLECTIC SERIES.
Lesson 164.
Ad signifies to, and for euphony takes the forms of ac, af, ag, al, an, ap, ar, and as; as ad and verto, advert, to turn to.
ad duce’ al lure’ as sail’ ag’gre gate
ac count’ an nex’ ad vance’ ag’gra vate
ac cord’ ar rive’ ad’verb ap pend’age
af fix’ as cend’ ad’verse ar’ro gance
Bi (from Latin bis, twice) means two, double, or in two.
bi’fid bi den’tate bi no’mi al
bi’form bi cor’nous bi en’ni al
bi’nate bi fur’cate bi noc’ular
bi’ped bi lin’gual bi valv’u lar
bi sect’ bi par’tite bi sul’phu ret
Lesson 165.
Con (Latin cum, with) signifies with or together; it takes the forms of com, col, co, cog, and cor, for ease in pronunciation.
con vert’ con de scend’ con ven’tion al
com press’ com pan’ion com pen sa’tion
col lect’ col’lo quy col lat’er al
co here’ co-ex ist’ co-ex ten’sive
cog’nate cog’ni zant cog nos’ci ble
cor rect’ cor re spond’ cor o na’tion
con cur’ con vul’sion con sec’u tive
con dign’ con vey’er con se quen’tial
con form’ con tu’sion con nat’u ral
SPELLING-BOOK. 101
Lesson 166.
De signifies down or from; epi significs on, near, during; and ex has the meaning out of. Ex also becomes e, ec, or ef.
de scend’ ex tract’ ep i dem’ic
de tract’ e vade’ ep’i lep sy
de note’ ef fuse’ ep i glot’tis
de vote’ ec’logue ep i derm’is
Dia, ob, per, and circum mean respectively apart, against, through, and around. With English words, dis gives a negative meaning.
dis tend’ dis sev’er dis em bar’rass
ob trude’ ob lique’ly ob lit’er ate
per plex’ per fect’ive per sist’en cy
cir’cuit cir cum volve’ cir cum ja’cent
102 ECLECTIC SERIES.
Lesson 167.
Mal signifies evil, ill; mono is from Greek monos, single; pan (Greek), signifies all, every thing; and poly (Greek polus), many.
mal’con tent ma li’cious ma lev’o lent
mon’o tone mon’o gram mo nop’o Iy
pan’o ply pan’the ist pan o ra’ma
pol’y gon pol’y pus pol’y the ism
Pro is a Latin preposition signifying for, before, and forth; uni (Latin unus, one) signifies one or producing one; syn (some­times syl and sym) signifies together; and sub (sometimes suf, sup, and sug) denotes under, below.
pro’noun u’ni ty syn’the sis sub scribe’
pro pel’ u’ni form syl’la ble suf ‘fix
pro duce’ u’ni corn sym’pa thy sup press’
pro vide’ u’ni val ve syn tac’tic sug gest’
Lesson 168.
Compound Words promiscuously arranged.
- ale’-house lime’-kiln hedge’hog
- hail’stone boat’man pen’knife
- lay’man four’score grist’-mill
- safe’guard load’stone mid’night
- waist’coat oat’meal pitch’fork
- bee’-hive pole’-star ship’wreck
- key’-stone snow’-drop wrist’band
- knee’-pan sports’man block’head
- bride’groom jew’s’-harp cross’-bow
light’-house luke’warm off ‘spring
SPELLING-BOOK. 103
Lesson 169.
Compound Words.
Lisle’-glove night’fall harts’horn
north-east’ book’-case corn’-stalk
joint’-stock foot’stool loop’-hole
well’-bred cork’screw bur’dock
snuff ‘-box watch’-word whirl’pool
towns’man broom’stick fools’cap
house’wife dooms’day work’shop
char’coal brown’-bread for sooth’
out weigh’ down’right down’cast
horn’pipe tooth’ache noon’day
heir’loom air’brake law’suit
Lesson 170.
can’dle stick post’al-card but’ter fly
hand’ker chief cop’y-book wa’ter-fall
bed’-cham ber oft’en times gas’-me ter
ev’er green type’-writ er cler’gy man
gen’tle man jour’ney man bric’-a-brac
pep’per mint hum’ming-bird na’vy-yard
camp’-meet ing musk’-mel on fool’-hard y
mas’ter piece blood’-ves sel al might’y
pass’o ver hon’ey-comb by’stand er
fowl’ing-piece stem’-wind er bass’-vi ol
pow’der-horn school’-mas ter tale’-bear er
104 ECLECTIC SERIES.
Lesson 171.
A’bel, a man’s name. de scend’ent, falling.
a’ble, powerful. cough’er, one who coughs.
al’ley, a narrow passage. coffer, a chest.
al ly’, one who assists. can’died, covered with sugar.
al lu’sion, a reference. can’did, honest; truthful.
il lu’sion, mockery. cent’u ry, 100 years.
de scend’ant, offspring. sen’try, a guard.
The able man’s name was Abel. A narrow alley. France was an ally of England in the Crimean war. He made an allusion to the illusion that possessed him. His descendant was descendent from the same line. The cougher sat on the coffer. The candid youth ate the candied cakes. The sentry wore a costume of the last century.
Lesson 172.
Words spelled alike, whose Pronunciation and Meaning differ.
aye, always. conjure, to enchant.
aye, an affirmative vote. bow, a weapon.
chose, did choose. bow, part of a ship.
chose, a thing; a chattel. chap, a boy.
bass, a term in music. chap, the jaw.
bass, a fish. gout, a disease.
conjure’, to implore. gout, taste; relish.
SPELLING-BOOK. 105
Lesson 173.
mall, a public walk. scald, a poet.
mall, a mallet. sew’er (so’er), one who sews.
slough (sluf), a snake’s skin. sew’er (su’er), a drain.
slough, a miry place. court’e sy, civility.
wear, a dam in a river. courte’sy, a slight bow.
wear, waste. slav’er, a slave ship.
min’ute (min’it), sixty seconds. slav’er, spittle.
mi nute’, very small. i’ron y (i’urn y), of iron.
hind’er, in the rear. i’ron y, ridicule.
hin’der, to obstruct. worst’ed, a kind of yarn.
scald, a burn. worst’ed, defeated.
Lesson 174.
Words in which the letter A is often mispronounced. Some of the words in this and succeeding lessons have two pronunciations, but in all cases the preferable one is given.
hearth mam ma’ an’cient fra’ter nize
grass a slant’ la’va com man dant’
slant pa pa’ saun’ter ti a’ra
gape a las’ pal’frey al ter’nate
gaunt al’mond rap’ine af fla’tus
far scath’less dra’ma hi a’tus
swathe pag’eant la’ma ba na’na
lance stal’wart da’ta sul ta’na
calm aft’er ma’gi man da’mus
laugh par’ent pa’thos oc ta’vo
106 ECLECTIC SERIES.
Lesson 175.
Words in which A is frequently mispronounced.
chal’dron ar ca’num u ra’ni urn
na’tant er ra’tum a qua’ri um
hal’berd ver ba’tim ap pa ra’tus
tas’sel val’en tine ig no ra’mus
sau’cy ca’ri ous ir ra’tion al
mael’strom tra’che a lit er a’ti
squa’lor bar bar’ic lit er a’tim
dai’ry bar ri cade’ ul ti ma’tum
ca’ret ra’di us mar a nath’a
gra’tis chol’e ra gym na’si um
ra’dix ca na’ry ex pa’ti ate
Lesson 176.
Sounds of A frequently mispronounced.
gla’mour sac’ra ment glance al’ways
raft’er a’pri cot zouave a mass’
scal’lop gar’ru lous drain Ar’ab
craft’y bra va’do stanch ba’thos
grass’y de fal’cate scarce cal’dron
em balm’ ca ca’o cant chas’ten
a ghast’ rail’ler y can’t fac’ile
was’sail an dan’te strap fair’y
balm’y hal’i but yacht ga’la
al’der na’ive te scath qua’si
Al’dine fi na’le calk lo cale’
SPELLING-BOOK. 107
Lesson 177.
Sounds of A often mispronounced.
swath pau’per gra va’men a men’
halve ha’rem to ma’to gua’no
jean pa sha’ sa’li ent na’ive
catch fac’et pa’ri ah har’ass
balm fal’chion far ra’go sat’ire
groat laugh’ter tap’es try jal’ap
trance tar’iff de ca’dence e clat’
yea ba salt’ a’re a prai’rie
are hur ra’ va ga’ry ra’tion
shaft ba ton’ cu’po la Sal’ic
scared quag’mire cu ra’tor ta’pis
Lesson 178.
Words in which the Sounds of E are often mispronounced.
ei’ther eq’ui ty leg’end a ry
pre’cept ten’a ble ab ste’mi ous
weap’on e’go tism a me’na ble
prel’ate ter’ra pin a pe’ri ent
yel’low al le’gro ste’re o type
ven due’ in her’ent sac ri le’gious
for get’ le’ni ent be nef ‘i cent
stead’y yes’ter day a men’i ty
en’gine e’qua ble e le’gi ac
ket’tle pe’o ny hy men e’al
treb’le e’qui poise em py re’an
108 ECLECTIC SERIES.
Lesson 179.
leant pet’rel cere’ment les see’
dreamt se’ries lei’sure me lee’
eyre seam’stress ef fete’ deaf ‘en
rear steel’yard en feoff ‘ rou’e
deaf sex’ton keel’son e lite’
teat fe’brile’ seck’eI khe dive’
pert fec’und bes’tial res’pite
tete sen’na fet’id there’fore
feoff ten’et fe’tich pref ‘ace
egg tep’id se’nile tet’ter
yet le’ver he’lot met’ric
Lesson 180.
per’uke nep’o tism ter’ri ble
neth’er as cet’ic res’in ous
pet’al red’o lent rec’i pe
res’in co te rie’ tet’a nus
ra ceme’ em ploy e’ ref ‘lu ent
pre’lude at ta che’ hy e’mal
me’grim pre’mi er cer’e brum
ven’ue o bei’sance ve’he ment
bre vet’ gen’er a def ‘i cit
car tel’ Ma dei’ra splen’e tic
e’pact her’o ine i de’a
SPELLING-BOOK. 109
Lesson 181.
Words in which the Sounds of I are often mispronounced.
fi’nite mer’can tile pa ri’e tal
pro’file pi az’za rec i ta tive’
de bris’ he gi’ra an ni’hi late
A’pril de cli’vous cal li’o pe
fi nanec’ O ri’on he li’ac al
ox’ide i tal’ic zo di’ac al
ar’chives ho ri’zon i soch’ro nous
vis’or si’ne cure men in gi’tis
sir’up so ri’tes ma ni’ac al
bas tile’ bron chi’tis scar la ti’na
rib’ald trip’ar tite i so therm’al
Lesson 182.
rid ti rade’ py ri’tes
vive ton tine’ fa ri’na
rinse bro’mine mar’i time
shire li’chen pi a’no
width ob lique’ vir’u lent
si’ren vis’count cyn’o sure
ti’ny vi’rile is’o late
li’en spike’nard vol’a tile
an’ile trib’une en fran’chise
ei’der qui’nine, de ci’sive,
tri’o di late’ pu’er ile
110 ECLECTIC SERIES.
Lesson 183.
fu’tile as pir’ant ad ver tis’er
ar tiste’ in quir’y tri syl’la ble
fi nesse’ sub sid’ence’ ka lei’do scope
stir’rup chas’tise ment ad ver’tise ment
sub’tile di gres’sion in ter ne’cine
chlo’rine di men’sion lar yn gi’tis
Al’pine di plo’ma mi rac’u lous
chi cane’ sim’o ny in ci’so ry
cui sine’ crin’o line vi vip’a rous
li’lac par’a digm is o la’tion
vic’ar e chi’nus si mul ta’ne ous
Lesson 184.
Words in which 0 is sometimes mispronounced.
holm tro’phy mon’as ter y
yolk on’ly proc’u ra tor
scoff mon’grel mi cros’co py
nonce be troth’ drom’e da ry
cost proc’ess zo ol’o gy
won’t doc’ile al lop’a thy
wont prov’ost au tom’a ton
shone grov’e1 hy drop’a thy
sloth fore’head La oc’o on
forge joc’und pho tog’ra phy
doth don’key in ter loc’u tor
SPELLING-BOOK. 111
Lesson 185.
Words in which O is sometimes mispronounced.
front’ier ap ro pos’ ab do’men
plov’er vo’ca ble dis com’fit
a mour’ pos til’ion court’e ous
hov’er pre co’cious pa rot’id
sur tout’ o’o lite con do’lence
sloth’fu1 dol’or ous cog no’men
Sou chong’ ca lor’ic op po’nent
caout’choue front’is piece co ro’na
re volt’ prob’i ty col’port eur
fort’night pome gran’ate po’ta ble
com’pass sov’er eign a ro’ma
Lesson 186.
Words in which U is sometimes mispronounced.
tulle col’umn in au’gu rate
joust sut’ure ce ru’le an
guide pup’pet vi tu’per ate
yours su’mac ac cu’mu late
ghoul ful’some co ad ju’tor
gi’aour con’duit pu’pil la ry
de but cu’cum ber in’sti tute
duc’at tru’cu lent eu re’ka
U’lan con nois seur’ cae su’ra
sup’ple ju’gu lar con’sti tute
du’ty nu’mer ous tour’na ment
112 ECLECTIC SERIES.
Lesson 187.
Words properly accented on the first Syllable.
con’strue com’bat ant pu’is sance
trav’erse dis’pu tant in’ter im
ramp’ant gon’do la au’top sy
ath’lete pleth’o ra tym’pa num
syr’inge mis’chiev ous wise’a cre
ex’tant blas’phe mous or’ches tral
brig’and con’ver sant im’po tent
con’cord san’he drim con’gru ent
dis’cord con’tra ry im’be cile
do’nate pro’te an pha’e ton
ob’long dis’ci pline ret’i na
Lesson 188.
roll, to turn over and over. soar, to mount upward.
role, a part performed. stake, a pointed stick.
sign, a token; a mark. steak, a slice of flesh.
sine, a line in geometry. step, a pace; a foot-print.
skull, part of the head. steppe, a dreary plain.
scull, to impel a boat. stoop, to bend forward.
sleeve, an arm cover. stoup, a basin; a pitcher.
sleave, untwisted silk. sum, the amount; whole.
slight, to neglect; feeble. some, a part; a portion.
sleight, dexterity. tale, that which is told.
soul, the immortal spirit. tail, terminal appendage.
sole, bottom of the foot. tare, allowance in weight.
sore, a hurt; painful. tear, to rend; to lacerate.
SPELLING-BOOK. 113
Lesson 189.
tacks, small nails. toe, part of the foot.
tax, import; duty. tow, coarse part of flax.
throne, seat of a king. tract, a region.
thrown, cast. tracked, followed.
team, horses hitched together their, belonging to them.
teem, to bring forth. there, in that place.
tear, water from the eye. throw, to cast; to hurl.
tier, a row or rank. throe, agony.
threw (thru), did throw. tide, rising of the sea.
through, from end to end. tied, bound; fastened.
time, duration. toad, a harmless reptile.
thyme, a pungent herb. towed, drawn by a rope.
Lesson 190.
prog’ress eq’ui page ex’qui site ly
in’grate phos’phor us com’pa ra ble
pae’an lu’di crous per’emp to ry
cou’pon vic’i nage or’tho e py
du’ress in’te gral ex’em pla ry
good’man in’te ger lam’en ta ble
o’zone an’ces tor in’ter est ing
a’corn an’ti podes con’tu me ly
pro’logue at’ro phy sub’lu na ry
thir’teen com’plai sant va’ri o loid
sar’dine det’o nate e’ti o late
Sp.8.
114 ECLECTIC SERIES.
Lesson 191.
Words properly accented on the second Syllable.
trust ee’ he ral’dic ap pel’la tive
mon soon’ ple thor’ic a nem’o ne
pro lix’ re cu’sant ar tif i cer
back slide’ ple be’ian ar bit’ra ment
where as’ pre ced’ence con sum’mate ly
gain say’ le the’an ca mel’o pard
re cess’ il lus’trate con not’a tive
pla card’ im mob’ile in ter’po late
a dept’ phi lip’pic te leg’ra phy
suc cess’ o de’on pe riph’ra sis
ro mance’ e la’ine re con’nais sance
SPELLING-BOOK. 115
Lesson 192.
cos tume’ so no’rous re med’i less
with draw’ ly ce’um pre ced’en cy
suc cinct’ mu se’um hy per’bo le
ex cess’ e ner’vate py ram’i dal
de funct’ ac cli’mate te leph’o ny
ca nine’ in un’date il lus’tra tive’
mo rale’ con den’sate ex ec’u tor
re lay’ Lin nae’an ex tem’po re
si moom’ ob jur’gate gla di’o lus
re course’ ad um’brate in fer’a ble
ac cess’ cho re’us chal ced’o ny
Lesson 193.
ex traor’di na ry in ter’po la tor
in com’pa ra ble con sol’a to ry
ir ref ‘ra ga ble de lib’er a tive
ir rep’a ra ble’ pro thon’o ta ry
ir rev’o ca ble dis crim’i na tive
in dis’so lu ble com mem’o ra tive
in dis’pu ta ble ac cel’er a tive
in ex’o ra ble sa lu’ta to ry
ab sol’u to ry pa ri’e ta ry
de mon’stra tive ly nun cu’pa to ry
oc tog’e na ry in ex’pli ca ble
116 ECLECTIC SERIES.
Lesson 194.
Words properly accented on the third Syllable.
rev er ie’ am a teur’ dem o ni’ac al
ob li gor’ bom ba zine’ ho me op’a thy
jag u ar’ tam bour ine’ ap o the’o sis
im pro vise’ ric o chet’* her e dit’a ment
or mo lu’ mule teer’ spon ta ne’i ty
et i quette’ mau so le’um ep i zo’o ty
av a lanche con ser va’tor hy per bo’re an
as sign or’ cot y le’don ep i cu’re an
po lo naise’ no men clat’ure Pyth a go’re an
cat a falque’ hy men e’an hip po pot’a mus
dis ha bille’ den u da’tion rec i proc’i ty
Lesson 195.
Words frequently mispronounced, or improperly accented.
mulet sa’chem jave’lin hos’tler
soot asth’ma chest’nut de’tail *
noose le’gend wres’tle fa cade’
twice de sign’ * or’chis strych’nine
niche isth’mus list’en per’fume *
salve this’tle bay’ou mus tache’
height rai’sn gib’bous bas’ket
milch a dult’ gla’cier Gae’lic
browse * psalm’ist griev’ous Le vant’ *
vase oft’en na’sal soft’en
- As a noun.
SPELLING-BOOK. 117
Lesson 196.
though goose’ber ry da guerre’o type
gist sooth’say er cab ri o let’
fifth ju’ve nile min i a ture’
drought lic’o rice leg er de main’
nook a pos’tle char i ot eer’
poor ar’gen tine an i mad vert’
roil Ar min’ian av oir du pois’
sauce de co’rous Cy clo pe’an
rhythm cyc’la men Eu ro pe’an
schism so’journ er spo li a’tion
root cov’et ous in’ter est ed
Lesson 197.
pom’mel ab’jeet ness nu mis’ma tist
bel’lows ab’a cus ig nit’i ble
fig’ure ad’verse’ly Jan’u a ry
di rect’ Bur’gun dy Feb’ru a ry
as’sets Bed’ou in in’ven to ry
je june’ en vi’rons cor’ol la ry
ver’min ex’ple tive vi’o la ble
ran’sack um’pi rage rep’a ra ble
short’-lived o’a sis des’pi ca ble
so’journ ar’se nic bap’tis ter y
cais’son ar’ti san pres’by ter y
118 ECLECTIC SERIES.
Lesson 198.
in’nate chol’er ic se’cre to ry
ter’mites gon’fa lon dec’re to ry
way’lay cen’tu ple ex’ple to ry
slaugh’ter re’tro cede con sis’to ry
frag’ile nu’cle us pre cep’to ry
car’riage cen’tau ry rep’er to ry
thor’ough co quet’ry chi rur’ger y
sched’ule sto mach’ic sperm a ce’ti
grand’eur in’ter stice pan e gyr’ist
hir sute’ ce ram’ic pan’e gy rize
ben’zine re volt’ing mel lif ‘lu ous
Lesson 199.
Words frequently mispronounced, or impropedy accented.
ag’gran dize dem’on strate tur’mer ic
al’der man tre men’dous mne mon’ic
Al’co ran stu pen’dous vir’e lay
al’ge bra gov’ern ment ex’pur gate
mis’tle toe Ar’a bic am’ber-gris
pres’by ter com’bat ive min’a ret
rasp’ber ry com’mu nist or’de al
ven’i son com’plai sance plat’i num
pos’i tive con’verse ly fem’i nine
dis hon’est dis as’ter gen’u ine
chiv’al ric dram’a tist por tent’ous
SPELLING-BOOK. 119
Lesson 200.
Words to be carefully discriminated.
cor’po ral, an officer. ve’ni al, pardonable.
cor po’re al, bodily. ve’nal, mercenary; base.
du’al ist, a believer in two gods. ap’po site, suitable; fit.
op’po site, over against.
du’el ist, one who fights a duel ac cla ma’tion, a slout.
ac cli ma’tion, inurement to climate. de scen’sion, descent.
dis sen’sion, strife. an’a lyze, to separate.
ce’re ous, like wax. an’nal ize. to record.
se’ri ous, grave; solemn. or’a cle, a prophet.
Sir’i us, the dog-star. au’ri cle, the external ear.
Lesson 201.
The words opposite one another in the lines have nearly the same meaning, and are called Synonyms.
au’thor ize com mis’sion em pow’er
ap par’ent ob’vi ous ev’i dent
ac cord’ant con’so nant a gree’ing
de port’ment de mean’or be hav’ior
di dac’tic pre cep’tive in struc’ive
fla gi’tious a tro’cious out ra’geous
ad her’ent par’ti san fol’low er
in’di gence pen’u ry pov’er ty
syc’o phant par’a site flat’ter er
har’bin ger pre cur’sor fore run’ner
120 ECLECTIC SERIES.
Lesson 202.
to, towards; unto. vane, a weathercock.
too, also. vain, proud; empty.
two, one and one. vein, a blood-vessel.
trey, three at cards. waste, to consume; loss.
tray, a shallow vessel. waist, part of the body.
vale, a valley; a dell. ware, merchandise.
veil, a cover; a curtain. wear, to use; to waste.
wait, to tarry; to stay. way, a road; manner.
weight, heaviness; load. weigh, to balance.
weighted, balanced. week, seven days.
wade, to walk in water. weak, not strong.
weth’er, a sheep. wood, timber; a forest.
weath’er, state of the air. would, preterit of will.
Lesson 203.
Words sometimes incorrectly pronounced alike, but which should be carefully discriminated.
line loin creek crick sex sects
loam loom pint point yon yawn
lose loose sat sot least lest
morn mourn phase face scrawl scroll
rout route laud lord tents tense
stalk stock east yeast with withe
can ken dawn don close clothes
blanch blench dose doze coarse corse
want wont wen when white wight
wax whacks alms arms moor more
SPELLING-BOOK. 121
Lesson 204.
Words nearly alike in Sound, to be carefully distinguished.
as say’ es say’ ep’ic ep’och
de cease’ dis ease’ bea’con beck’on
de scent’ dis sent’ coffin cough’ing
de vice’ de vise’ grist’ly gris’ly
huz za’ hus sar’ di’vers di’verse
in tense’ in tents’ cho’ral cor’al
a loud’ al lowed’ gant’let gaunt’let
im merse’ a merce’ mu’sic mu’cic
af fect’ ef fect’ rad’ish red’dish
e lude’ al lude’ sculp’tor sculpt’ure
Cas’tile cast’-steel hum’ble um’bel
Lesson 205.
as cent’, steepness. bur’y (ber’ry), to cover with earth.
as sent’, agreement.
an’chor, for a ship. ber’ry, a small fruit.
ank’er, a liquid measure. can’non, a great gun.
al’ter, to change. can’on, a rule or law.
al’tar, a place for sacrifice. ceil’ing, top of a room.
au’ger, an instrument. seal’ing, as with wax.
au’gur, to foretell. cel’lar, a lower room.
bur’row, hole for shelter. sel’ler, one who sells.
bor’ough, a corporate town. ces’sion, a giving up.
ses’sion, a sitting.
bold’er, more bold. cous’in, a relation.
bowl’der, a large pebble. c oz’en, to cheat.
122 ECLECTIC SERIES.
Lesson 206.
cen’su al, of the census. phil’ter, a love-charm.
sen’su al, carnal. great’er, larger.
coun’cil, an assembly. gra’ter, that which grates.
coun’sel, advice. ho’ly, sacred; pure.
can’vas, a kind of coarse cloth. whol’ly, entirely.
can’vass, to discuss. mar’tin, a bird.
crew’el, worsted yarn. mar’ten, a kind of weasel.
cru’el, inhuman; savage. man’ner, form; method.
cyg’net, a young swan. man’or, district.
sig’net, a seal. man’tel, shelf over a fireplace.
chol’er, anger; wrath. man’tle, a cloak.
col’lar, for the neck. mar’tial, warlike.
fil’ter, to strain. mar’shal, an officer.
Lesson 207.
con’so nance con’so nants cen’sus sen’ses
e lys’i an e lis’ion Lat’in lat’ten
e mer’sion im mer’sion con’cert con’sort
for’mer ly form’ally cor’nice Corn’ish
pass’a ble pas’si ble hal’low halo
pe ti’tion par ti’tion rel’ic rel’ict
com’i ty com mit’tee or’der ord’ure
dep ra va’tion dep ri va’tion fa’ther far’ther
ve rac’i ty vo rac’i ty plaint’iff plaint’ive
sta’tion a ry sta’tion er y pa’tience pa’tients
SPELLING-BOOK. 123
Lesson 208.
bile boil ad her’ence ad her’ents
wig whig con fi dant’ con’fi dent
God gaud at tend’ance at tend’ants
dance daunts ac’ci dence ac’ci dents
dome doom e lic’it il lic’it
wheel weal em’i nence im’mi nence
lease lees e rup’tion ir rup’tion
sense since sal’a ry cel’er y
dross draws bar’ren ness bar’on ess
whit wit proph’e cy proph’e sy
Lesson 209.
med’al, a stamped coin. pen’cil, used for writing.
med’dle, to interfere. pen’sile, hanging.
mi’nor, one under age. pet’ty, small; little.
mi’ner, a worker in mines. pet’it’, a term in law.
mit’y, full of mites. pom’ace, ground apples.
might’y, powerful. pum’ice, a spongy stone.
na’val, of ships. rig’or, severity; stiffness.
na’vel, the central part. rig’ger, one who rigs.
cen’sor, one who censures. suck’er, a kind of fish.
cens’er, a pan for incense. suc’cor, help; assistance.
pan’nel, a kind of saddle. sur’plus, excess.
pan’el, a jury roll. sur’pluce, a clerical dress.
124 ECLECTIC SERIES.
Lesson 210.
pal’let, a small bed. com’pli ment, regard.
pal’ate, part of the mouth. com’ple ment, fullness.
pal’ette, an oval board. coun’sel or, an adviser.
em’i grate, to move out. coun’cil or, member of a council.
im’mi grate, to move in.
cas’tor, the beaver. straight’en, to make straight.
cast’er, one who casts. strait’en, to narrow.
cur’rent, running. cal’en dar, an almanac.
cur’rant, a small fruit. cal’en der, a hot press.
cap’i tol, a public edifice. sut’ler, an army trader.
cap’i tal, principal. sub’tler, more subtle.
Lesson 211.
Words which require Care in Spelling.
jilt dol’lar rip’ple nat’u ral
gyre schol’ar trip’le gut’tur al
jow1 grap’ple pop’py lit’er al
troll chap’el cop’y diz’zi ly
goal ren’net sun’ny bus’i ly
knoll sen’ate mon’ey ver’ti cal
dole freck’le glim’mer ar’ti cle
turf shek’el prim’er du’te ous
verb wit’ty tread’le beau’te ous
pirn cit’y ped’dle fin’i cal
perk hop’per cod’dle pin’na cle
surd prop’er mod’el cyn’ic al
SPELLING-BOOK. 125
Lesson 212.
scream com’et peb’ble in ter cede’
screen vom’it reb’el su per sede’
sheave plum’met sib’yl col’o nize
sheet sum’mit spin’et ad ver tise’
shield ver’y lin’net par’a lyze
twirl mer’ry cam’el se’cre cy
churl bod’y tram’mel ec’sta sy
clerk shod’dy mam’mal vac’il late
quirk mud’dy sev’en fas’ci nate
fraud stud’y heav’en co er’cion
broad guin’ea par’rot de ter’sion
awe’d nin’ny clar’et ex er’tion
Lesson 213.
grief do’ing a byss’ hid’e ous
sheaf stew’ing a miss’ pre’vi ous
guile, yeo’man as sess’ im’pi ous
chyle chlo’ral ab’scess a’que ous
rend know’ing sick’le par’ti cle
wrench go’ing nick’el crit’ic al
dearth con dole’ tal’ents dil’i gent
worth con trol’ bal’ance el’e gant
mirth en roll’ si’lence fal’li ble
earth dis pel’ com peer’ prel’a cy
spurt fore tell’ ad here’ jeal’ous y
126 ECLECTIC SERIES.
Lesson 214.
which stom’ach re prieve’ in i’tial
ditich sau’sage con ceive’ of fi’cial
feud word’y de grade’ es sen’tial
sued tur’gid a fraid’ sol sti’tial
prude ver’ger pre pare’ a bun’dant
wooed vir’tue for bear’ de pend’ent
balk leop’ard bar’ter in veigh’er
shawl lep’er tar’tar be tray’er
guise fam’ine mar’tyr di’a logue
sighs gam’mon suc ceed’ dy nam’ics
flies salm’on ac cede’ me chan ics
SPELLING-BOOK. 127
Lesson 215.
wield scan’dal se rene’ an’no tate
weird han’dle un clean’ an’o dyne
swale clam’or be tween’ col on nade’
swain gram’mar ma rine’ ser e nade’
storm ham’mer com plete’ dom i neer’
swarm palm’er de feat’ bel ve dere’
scythe sa’tyr de ceit’ pen’ni less
writhe trai’tor co erce’ mon’ey less
sieve wait’er dis burse’ joc’u lar
give cra’ter dis perse’ jock’ey ing
Lesson 216.
skein val’id kir’tle pol’i cy
slain sal’ad tur’tle leg’a cy
crane mal’let fer’tile cur’ti lage
sword val’et myr’tle syn’a gogue
boast breez’y wid’geon cod’i cil
ghost greasy pig’eon dom’i cile
queer gar’den mal’ice ver’sa tile
brief par’don pal’ace hyp’o crite
spoke e’vil tor’toise hip’po drome
croak ea’gle mor’tise scen’er y
self pole’ax sel’vage ple’na ry
sylph poult’ry por’ridge dean’er y
128 ECLECTIC SERIES,
Lesson 217.
zinc col’lege con fer’ u ten’sil
brink knowl’edge a stir’ pre hen’sile
fought leath’er oc cur’ fa tigu’ing
caught teth’er ef face’ be lea’guer
wrought cau’cus e rase’ si li’ceous
fuse mawk’ish chas tise’ vex a’tious
news au’thor bap tize’ fa ce’tious
views awn’ing a chieve’ sus pi’cion
choose ar’id per ceive’ po si’tion
wooes heir’ship be reave’ in cis’ion
ooze air’y re nown’ de ris’ion
whose car’ry re nounce’ e di’tion
Lesson 218.
earl ran’cor in vade’ di ur’nal
knurl can’ker up braid’ hi ber’nal
shirk flux’ion ur bane’ at tor’ney
jerk suc’tion or dain’ de ter’gent
pith hos’pice a dieu’ con ta’gion
myth au’spice im brue’ her ba’ceous
growth bot’tom pre cede’ frol’ic some
loath au’tumn pro ceed’ frol’ick ing
loathe trunn’ion re deem’ de pres’sion
clothe bun’ion ex treme’ dis cre’tion
SPELLING-BOOK, 129
Lesson 219.
risk coup’le wry’ness ve’hi cle
wrist cup’board ri’ot typ’ic al
shred cho’rus ly’rist ob’sta cle
dread po’rous li’vre pro’to col
scheme hill’y ten’on mys’tic al
chief lil’y pen’non mis’ti ness
siege san’dal ros’trum rec’re ant
seat can’dle phan’tom reck’on er
seethe nu’tant fan’ion wretch’ed ly
keyed neu’ter ver’sion of ‘fi cer
tweed nui’sance ter’tian oph’i cleide
Lesson 220.
Words containing silent Letters.
thought hand’some re doubt’ hec’a tomb
wreathe vict’uals re scind’ sci’o list
wreath scis’sors gneis’sose co a lesce’
rhomb schot’tish be nign’ ap’a thegm
gnat g’no’mon cam paign’ di’a phragm
rogue’ for’eign ar raign’ psy’chic al
gnaw dough’ty op pugn’ sac’cha rine
gnash haugh’ty re sign’ rheu mat’ic
gnarl chron’ic de light’ rhap’so dy
gnome daugh’ter ex pugn’ rhet’o ric
phlegm ghast’ly af fright’ ca tarrh’al
Sp.9.
130 ECLECTIC SERIES.
Lesson 221.
taught hon’est ca tarrh’ pneu mat’ics
source gher’kin con demn’ psal’ter y
brought chalk’y de mesne’ pneu mo’ni a
realm isl’and de pot’ rhi noc’e ros
vault naph’tha burgh’er ren’dez vous
knob gris’tle calk’er jeop’ard y
qualm thros’tle, rhom’boid hem’or rhage
wroth chris’ten tme’sis rhiz’o pod
fraugt jeop’ard ptis’an ptar’mi gan
knock wrig’gle, psy’chic pseu’do nym
knife bris’tle rhym’er psalm’ist ry
Lesson 222.
Words liable to be misspelled.
tres’tle glu’ey ness collect’i ble’
pa paw’ crys’tal line e ras’a ble
gey’ser chrys’a lis ac cor’di on
gaug’ing lach’ry mose sac er do’tal
co log’ne ker’o sene’ ef fer ves’cence
qua drille’ glyc’er ine tran quil’li ty
sky’ey ar’go naut com mit’ti ble
sor’ghum fore’bod’ing cor us ca’tion
sur vey’ ex cheq’uer mac a ro’ni
starve’ling sib’yl line pic’ca lil li
pro’gramme sib’i lant fil’i bus ter
SPELLING-BOOK. 131
Lesson 223.
fleam ey’ing gen e al’o gy
glyph wee’vil bac ca lau’re ate
liege lac’quer ab o rig’i nes
cuish du et’ ar chae ol’o gy
taunt quar tet’ as a fet’i da
drap phe’nix er y sip’e las
fleche rogu’ish ho mo ge’ne ous
frere whey’ey hy per crit’i cism
jardes ledg’er ich thy ol’o gy
crypt sach’el ig’nis-fat u us
sou lar’ynx lack a dai’si cal
Lesson 224.
Words frequently mispronounced.
for’tress dan’druff prod’uce con cise’
car’bine fran’chise com’bat dis own’
chlo’ride hom’age thith’er dis dain’
cof ‘fee rhu’barb o’nyx di vulge’
com’rade cov’ert dis arm’ ex tol’
sau’cer ma’tron jo cose’ for bade’
dec’ade mon’ad bour geois’ suf fuse’
quin’sy pa’tron Cay enne’ pos sess’
gal’lows lith’arge con tour’ fare well’
mis’le par’tridge di verge’ be neath’
fau’cet wa’ter di vert’ re source’
132 ECLECTIC SERIE8.
Lesson 225.
di’a mond par’a dise cin cho’nit
chan de lier’ a’li as in vei’gle
gran’a ry par’a chute stra te’gic
cou’ri er pot-pour ri’ ex cur’sion
eg’lan tine hy’gi ene a cous’tics
sor’cer y con’fis cate an cho’vy
ex’tir pate psal’mo dy pa la’ver
cor’di al guard’i an Cau ca’sian
cor’ri dor com’mu nism ap par’el
gas’e ous sub al’tern so pra’no
doc’i ble cou ra’geous im mor telle’
Lesson 226.
som’er sault how’itz er bar’y tone
stim’u lus syc’a more bil’lings gate
sil’hou ette a bridg’ment bry’o ny
pa vil’ion ad’di ble cen’ti ped
quin till’ion aes thet’ic cim’e ter
ci vil’ian al’che my col’an der
cen’ti gram ar’que buse cop’i er
ma nil’la ai’lan’tus nas tur’tium
eu’pho ny as bes’tus chic’o ry
pros’e lyte as cend’ant hei’nous ness
pu’tre fy syz’y gy deb o nair’
pro bos’cis bar’be cue por’phy ry
SPELLING-BOOK. 133
Lesson 227.
bal’dric mal fea’sance cal lig’ra phy
ban’yan sur’cin gle dys’en ter y
bau’ble pleu’ri sy rem i nis’cence
la pel’ por’ce lain hy poc’ri sy
ker’chief os’cil late hy pot’e nuse
gnos’tic del’e ble syn ec’do che
but’-end lau’da num si de’re al
cam’phene crys’tal lize ad sci ti’tious
catch’up pol’y glot am au ro’sis
cess’-pool guer ril’la lill i pu’tian
ci gar’ quin tes’sence lil i a’ceos
Lesson 228.
clew coif ‘fure con fec’tion er y
clinch fledge’ling klep to ma’ni a
sleuth af ‘ghan cor nu co’pi a
blonde che nille’ cot y led’o nous
glebe che mise’ di u tur’ni ty
gyves chas’seur terp sich o re’an
guy chev’ron me temp sy cho’sis
crutch cor’ymb me te or’o lite
touch e leve’ per ip neu’mo ny
kraal hogs’head phar ma co poe’ia
chintz meer’scham phar ma ceu’tic al
ceirge buhr’-stone sac cha rif ‘er ous
134 ECLECTIO SERIES.
Lesson 229.
Words liable to be misspelled or mispronounced.
el e phan ti’a sis ir re cog’ni za ble
par a di si’ac al gu ber na to’ri al
par a pher na’li a el ee mos’y na ry
ver i si mil’i tude pol y cot y le’don
tin tin nab u la’tion het er o ge’ne ous
su per e rog’a tive hi e ro glyph’ic al
pu sil la nim’i ty hyp o chon dri’ac al
phan tas ma go’ri a his to ri og’ra pher
ob’li ga to ri ly in dis’so lu ble’ness
id i o syn’cra sy in dis’pu ta ble’ness
ir re me’di a ble’ er y si pel’a tous
ip e cac u an’ha ir ref ‘ra ga ble ness
Lesson 230.
Words of irregular Pronunciation.
of (ov) tough (tuf) trough (trawf)
sice (siz) hough (hok) bus’y (biz’y)
tige (tej) fiord (fyord) ma’ny (men’y)
says (sez) bouy (bwoy) pret’ty (prit’ty)
said (sed) cough (kawf) wom’en (wim’en)
loir (lwar) mont (mong) cann on’ (kan yun’)
a’ny (en’y) rouge (roozh) sa lon’ (sa long’)
newt (nut) mauve (mov) chap’eau (shap’o)
beaux (boz) ruche (roosh) cha teau’ (sha to’)
once (wuns) Czech (tchek) cro quet (kro ka’)
i’ron (i’urn) caf ‘e (kaf ‘a) men age’ (-azh’)
SPELLING-BOOK. 135
Lesson 231.
pa tois’ (pat wa’) bou quet’ (boo ka’)
bi jou (be zhoo’) breech’es (brich’ez)
phthis’ic (tiz’ik) por’poise (por’pus)
bu’reau (bu’ro) a gain’ (a gen’)
En’glish (ing’glish) dis cern’ (diz zern’)
flam’beau (flam’bo) e nough’ (e nuf ‘)
haut’boy (ho’boy) en nui’ (ong nwe’)
hic’cough (hik’kup) ron deau’ (ron do’)
right’eous (ri’chus) vign ette’ (vin yet’)
cham’ois (sham’my) squir’rel (or skwur’rel)
bou’doir (boo’dwor) suf fice’ (suf fiz’)
ser’geant (sar’jent) cor’tege (kor’tazh)
Lesson 232.
sough (suf) men ag’e rie (men azh’e ry)
myrrh (mer) ci ce ro’ne (che che- or sis’e-)
suave (swav) chev’aux-de-frise (shev’o de frez)
shew (sho) pap’ier-ma che (pap’ya ma sha)
strew (stru) de col le te’ (da kol le ta’)
bouffe (boof) tic-dou lou reux’ (tik doo lo roo’)
nom (nong) ver mi cel’li (-chel’li or -sel’li)
clough (kluf) su per fi’cies (su per fish’ez)
nee (na) ra tion a’le (rash un a’le)
ghat (gawt) ha bit u e (a bit n a’)
creux (kru) hal le lu jah (hal le lu’ya)
136 ECLECTIC SERIES.
Lesson 233.
bus’i ness (biz’nes) roq’ue laure (rok’e lor)
colo nel (kur’nel) sac’ri fice (sak’ri fiz)
hau teur’ (ho tur’) chef-d’oeuvre’ (sha doovr’)
bdell’ium (del’yum) es cri toire’ (es kri twor’)
cui rass’ (kwe ras’) belles-let’tres (bel let’ter)
gauch rie’ (gosh re’) res tau rant’ (res to rang’)
trous seau’ (troo so’) mign on ette’ (min yon et’)
gun’wale (gun’nel) fuch’si a (fook’si a)
dah’lia (dal’ya) re veil’le (re val’ya)
soi ree’ (swa ra’) pap e terie’ (pap a tre’)
sap’phire’ (saf ‘ir) sur veil’lance’ (-val’yans)
cog’nac (kon’yak) Ple’ia des (ple’ya dez)
Lesson 234.
nes’cience (nesh’ens) re cher che’ (ruh sher sha’)
ba rege’ (ba razh’) so bri quet’ (so bre ka’)
diph’thong (dif-) aid’-de-camp (ad’de kong)
sol’dier (sol’jer) mag gio’re (mad jo’ra)
fort’une’ (fort’yun) made moi selle’ (-mwa zel’)
neph’ew (nef ‘yu) fleur-de-lis’ (flur de le’)
let’tuce (let’tis) deb au chee’ (deb o she’)
en tree’ (ong tra’) res er voir’ (rez er vwor’)
re gime’ (ra zhem’) eis tedd’fod (is teth’fod)
scru toire’ (skru twor’) pro te ge’ (pro ta zha’)
phy sique’ (fe zek’) de noue’ment (-noo’mong)
SPELLING-BOOK. 137
Lesson 235.
cri tique’ (kri tek’) en core’ (ong kor’)
pen chant’ (pong shong’) se ance’ (sa ongs’)
chig’non (shen’yong) mor ceau’ (mor so’)
cha let’ (sha la’) dan seuse’ (dong zurz’)
e lan’ (a lang’) sang-froid’ (song frwa’)
mem’oir (mem’wor) qui vive (ke vev)
mon sieur’ (mo ser’) faux pas’ (fo pa’)
blanc-mange’ (blo-monj’) bon ton (bong tong)
a mende’ (a mongd’) bon’mot (bong’mo)
cen time’ (son tem’) mil lier’ (mi lya’)
biv’ouac (biv’wak) sa vant’ (sa vong’)
138 ECLECTIC SERIES.
Lesson 236.
Names of Men.
Charles Ad’am Har’old A’sa
Frank Al’bert Hen’ry Bas’il
George An’drew Ho’mer Ca’leb
Hugh Ar’thur I’saac Ce’phas
James Clar’ence Ja’cob Cy’rus
Job Da’vid Jo’seph Eu’gene
John Ed’ward Lew’is Fe’lix
Luke Ed’win No’ah Ja’bez
Mark Ez’ra Pat’rick Leon’ard
Saul Fran’cis Pe’ter Mo’ses
Ralph Gil’bert Will’iam Rob’ert
Lesson 237.
Her’bert Ab’sa lom Al ex an’der
Hi’ram An’tho ny An dro ni’cus
Hor’ace Ben’ja min Bar thol’o mew
Ja’son E li’jah Eb en e’zer
Jes’se Fer’di nand Em man’u el
Law’rence Fred’er ick E ze’ki el
Le’vi I sa’iah (-ya) Jer e mi’ah
Lu’ther Le an’der Le on’i das
Os’car Ol’i ver Na po’le on
Phil’ip Sam’u el The oph’i lus
Rich’ard Tim’o thy Zech a ri’ah
SPELLING-BOOK. 139
Lesson 238.
Names of Women.
Anne A’da Es’ther Lo’is
Blanche Ag’nes Eu’nice Lu’cy
Eve Al’ice E’va Ma’bel
Grace An’na Fan’ny Mar’tha
Jane Ber’tha Flo’ra Ma’ry
Jean Clar’a Fran’ces My’ra
Kate Co’ra Ger’trude Nan’cy
Maud E’dith Hel’en Ra’chel
May Ed’na Han’nah Rho’da
Pearl El’la I’da Sa’rah
Ruth Em’ma Lau’ra Su’san
Lesson 239.
A’my Ad’e line A me’li a
Bet’sey A man’da Ar a bel’la
Bridg’et Bar’ba ra Dor o the’a
Char’lotte Be’a trice E liz’a beth
Chlo’e Deb’o rah E van’ge line
Dor’cas E li’za Fe lic’i a
Di’nah Em’i ly Fred er i’ca
El’len Mar’ga ret Ge’or gi an’a
Flor’ence’ Pris cil’la Is a bel’la
Ja net’ Re bec’ca La vin’i a
Ro’sa Su san’na Vic to’ri a
140 ECLECTIC SERIES.
Lesson 240.
Abbreviations used in Writing and Printing.
- or Am., Answer. Bro., Brother.
- B., Bachelor of Arts. C. H., Court-House.
- C., or B. C., Before Christ. Co., Company; County.
- D., In the year of our Lord. Cr., Credit.
Bart., Baronet. D. D., Doctor of Divinity.
Bbl., Barrel; barrels. Do., or ditto, The same.
- L., Bachelor of Laws. Dr., Doctor; Debtor.
C.O.D., Collect on delivery.
- g. (exempli gratia), For example.
- M., Master of Arts; Before noon; In the year of the world.
Lesson 241.
Ed., Editor; Edition. H. B. M., Her Britannic Majesty.
Eng., England; English. Hhd., Hogshead.
Esq., Esquire. H.R., House of Representatives.
Fri., Friday. G.P.O., General Post-Office.
Fahr., Fahrenheit. Ibid., In the same place.
Gen., General; Genesis. Id. (idem), The same.
Gov., Governor. i. e. (id est), That is.
Jas., James. Jun. or Jr., Junior.
Lat., Latitude. Lb., Pound; pounds.
Etc. (et cetera), And so forth.
F.R.S., Fellow of the Royal Society.
SPELLING-BOOK. 141
Lesson 242.
- D., Doctor of Laws. Mrs., Mistress.
Long., Longitude. N., North.
- S., Place of the Seal. N. A., North America.
M., Monsieur. MS., Manuscript.
- C., Member of Congress. No., Number.
Mon., Monday. N. B. (nota bene), Take notice.
- D., Doctor of Medicine. pp., Pages.
Messrs., Gentlemen. Per., By the.
- P., Member of Parliament. P. M., Postmaster; Afternoon.
P.O., Post-Office.
Mr., Mister; Master. Prof, Professor.
Lesson 243.
- S., Postscript. St., Saint; Street.
Pub. Doc., Public Document. Sun., Sunday.
Supt., Superintendent.
Pxt., He painted it. Thurs., Thursday.
Sc., He engraved it. Tues., Tuesday.
- M., Quartermaster. V., vid., or vide, See.
Rec’d., Received. Viz. (videlicet), Namely.
Rev., Reverend. Vol., Volume.
S., Shilling; South. Vs. (versus), Against.
- A., South America. Wed., Wednesday.
Sat., Saturday. W.I., West Indies.
Sen., Senior; Senator. Wt., Weight.
142 ECLECTIC SERIES.
Lesson 244.
Abbreviations of the States, with their Pronunciation.
Ala., Al a ba’ma. Ia., I’o wa.
Ark., Ar’kan sas. Kan., Kan’sas.
Cal., Cal i for’ni a. Ky., Ken tuck’y.
Col. or Colo., Col o ra’do. Lou. or La., Lou i si a’na.
Conn. or Ct., Con nect’i cut Mass., Mas sa chu’setts.
Md., Ma’ry land.
Del., Del’a ware. Me., Maine.
Flor. or Fla., Flor’i da. Mich., Mich’i gan.
Geo. or Ga., Geor’gi a. Minn., Min ne so’ta.
Ill., Il li nois’. Miss., Mis sis sip’pi.
Ind., In di an’a. Mo., Mis sou’ri.
Lesson 245.
Neb., Ne bras’ka. R. I., Rhode Is1’and.
- C., North Car o li’na. S. C., South Car o li’na.
- H., New Hamp’shire Tenn., Ten nes see’.
Tex., Tex’as.
- J., New Jer’sey. Uh., U’tah (yoo’ta).
Nev., Ne va’da. U.S.A., U nit’ed States of A mer’i ca.
- Y., New York.
Or., Or’e gon. Va., Vir gin’i a.
O., O hi’o. Vt., Ver mont’.
Pa. or Penn., Penn syl va’ni a. Wis., Wis con’sin.
W Va., West Vir gin’i a.
SPELLING-BOOK. 143
Lesson 246.
American and Foreign Geographical Names.
Al’ba ny Ba’den Al le ghe’ny
Ayr (ar) Bal’ti more A’si a (a’shi a)
Aulne (on) Bor deaux’ (-do’) Cin cin na’ti
Bos’ton Chi ca’go Eu phra’tes
Chey enne’ Cai’ro Ha wai’i
Main Cey’lon’ Pal’es tine
Mo bile’ I’ser (e’zer) Phil a del’phi a
Pau (po) Mad rid’ Pyr’e nees
Saone Mil wau’kee Szeg ed in’
Seine Mon ta’na Vi en’na
Thames (temz) New Or’leans Wash’ing ton
Lesson 247.
Other Geographical Names of frequent Mispronunciation.
Guanaxuato (gwa na hwa’to) Aube (ob)
Poughkeepsie (po kip’si) Caen (kon)
Worcester (woos’ter) Dieppe (dyep)
Youghiogheny (yoh’ho ga’ni) Foix (fwa)
Newfoundland (nu’fund land) Joux (zhoo)
Chuquisaca (choo ke sa’ka) Lisle (lel)
Guatemala (ga te ma’la) Moux (moo)
Winnipiseogee (-pis sok’ki) Oude (owd)
Venezuela (ven e zwe’la) Sioux (soo)
Altamaha (al ta ma ha’) Thau (to)
Chautauqua (sha ta’kwa) Y (i)
144 ECLECTIC SERIES.
Lesson 248.

#### Section: Of Characters Used In Punctuation.
A Comma [, ] denotes the slightest degree of separation be­tween the elements of a sentence.
A Semicolon [; ] denotes a degree of separation somewhat greater than that indicated by a comma.
A Colon [:] marks a still greater degree of separation than a semicolon.
A Period [.] usually indicates the close of a sentence.
The Interrogation Point [?] is used at the end of a ques­tion.
The Exclamation Point [!] denotes astonishment or other emotion.
A Hyphen [ – ] is used to join words or syllables.
A Dash [-] marks a sudden break or stop in a sentence.
A Parenthesis [()] includes words which might be left out without injuring the sense.
Brackets [ ] inclose words, etc., intended to explain or rec­tify what precedes or follows.
An Apostrophe [‘] indicates the omission of one or more letters; or denotes the possessive case.
Quotation Marks [” “] show that the passage included, is taken from some other author.

#### Section: Of Capital Letters.
A Capital should begin: (1) the first word of every sentence, and of every line of poetry; (2) proper names of persons, places, months, and days; (3) all appellations of the Deity; (4) titles of honor; (5) names of things personified; (6) names denoting the race or nation of individuals; (7) adjectives de­rived from proper names; (8) the first word of a direct quo­tation or speech; (9) the principal words in the titles of books; (10) words denoting important events, the chief sub­ject of a composition, etc. (11) The pronoun I and the interjection O are always capitals.
End of the Project Gutenberg EBook of McGuffey’s
by W. H. McGuffey
*** END OF THIS PROJECT GUTENBERG EBOOK MCGUFFEY’S ECLECTIC SPELLING BOOK ***
Primer K Mcguffeys
First reader Mcguffeys
Resources
- Resources for families [link: “Resources for families” → `resources.html`]
- Nursery rhymes for Pre-K [link: “Nursery rhymes for Pre-K” → `resources-nursery-rhymes.html`]
- Anglia practice papers [link: “Anglia practice papers” → `anglia-practice.html`]

#### Section: Come and see the school.
Tours are arranged individually, Monday to Friday.
→ **Book a visit** (`forms.html#visit`)
→ **For parents** (`parents.html`)

---

### 4.55 `resources-nursery-rhymes.html`

- **Browser title:** Nursery rhymes for Pre-K – American Group International, Agadir
- **Meta description:** Traditional English nursery rhymes for pre-kindergarten children – read and sing at home.

Home / Student life / Nursery rhymes for Pre-K [link: “Home” → `index.html`] [link: “Student life” → `student-life.html`]
**Page title (H1):** Nursery rhymes for Pre-K
Traditional English rhymes to read and sing with young children.
→ **Request a tutor** (`forms.html#tutor-request`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: Nursery Rhymes for Pre-K

#### Section: Printable Nursery Rhymes Booklet
Nursery-Rhymes-Songs-Fingerplays-Printable-Cards

#### Section: Rhymes and Songs
for
Babies and Toddlers
Rhymes and songs provide a wonderful way for you to bond with your child.
Your child will love being able to spend time with you in this way.
Saying rhymes and singing songs is fun! Your child is naturally drawn to the beat,
and you might be impressed to see how well your child bounces or dances to the
rhythm of a favorite song or rhyme.
Rhymes and songs are great tools for helping your child explore the fun and
beauty of language. The rhythm that your child naturally finds so appealing also
helps your child to hear all of the individual sounds that make up the words. This
is important for helping children learn to speak when they are very young. As they
grow older, it will help them learn to read on their own.
Rhymes and songs allow your child to experience language with many senses. For
example, your child may enjoy a rhyme with his/her ears (hearing), body (moving
or bouncing), and/or with touch (tickles) all at the same time. The more senses a
child uses, the stronger the activity’s impact will be.
We have tried to include a wide variety of different kinds of rhymes and songs in
this collection. We hope that you and your child enjoy trying some of these out
together!
Higglety Pigglety Pop
The dog has eaten the mop.
The pig’s in a hurry,
The cat’s in a flurry,
Humpty Dumpty
Humpty Dumpty sat on a wall.
Humpty Dumpty had a great fall.
All the king’s horses and all the king’s men,
Couldn’t put Humpty together again.
Little Boy Blue
Little boy blue, come blow your horn,
The sheep’s in the meadow; the cow’s in the corn.
Where is the boy who looks after the sheep?
He’s under the haystack fast asleep.
Little Bo Peep
Little Bo Peep has lost her sheep
And doesn’t know where to find them.
Leave them alone and they’ll come home
Wagging their tails behind them.
Old Mother Hubbard
Old Mother Hubbard. Went to her cupboard,
To fetch her poor dog a bone.
But when she got there the cupboard was bare,
And so her poor dog had none.
Hey Diddle Diddle
Hey Diddle Diddle, the cat, and the fiddle,
The cow jumped over the moon,
The little dog laughed to see such fun,
And the dish ran away with the spoon.
Little Miss Muffet
Little Miss Muffet sat on her tuffet,
Eating her curds and whey.
Along came a spider. Who sat down beside her,
And frightened Miss Muffet away.
Wee Willie Winkie
Wee Willie Winkie runs through the town,
Upstairs, downstairs in his nightgown.
Tapping at the window, crying through the lock,
Are the children in their beds? For now, it’s eight o’clock.
Mary, Mary, Quite Contrary
How does your garden grow?
With silver bells and cockle shells,
And pretty maids all in a row.
Old King Cole
Old King Cole was a merry old soul,
And a merry old soul was he.
He called for his pipe, and he called for his bowl,
And he called for his fiddlers three.
Pussy Cat, Pussy Cat
Pussy cat, pussy cat, where have you been?
I’ve been to London to see the fair Queen.
Pussy cat, pussy cat, what did you there?
I frightened a little mouse, under her chair.
It’s Raining, It’s Pouring
The old man is snoring.
He went to bed and bumped his head,
And he wouldn’t get up in the morning.
Icka Bicka Soda Cracker
Icka bicka boo.
Up goes you!
I love you!
*Bounce as you say this rhyme. Lift
your child at the end of the first verse.
Huge your child at the end of the
second verse.*
Little Red Wagon
Bumping up and down in my little red wagon,
Won’t you be my darling!
*Bounce your child as you say this rhyme.*
From Wibbleton to Wobbleton
From Wibbleton to Wobbleton is fifteen miles.
From Wobbleton to Wibbleton is fifteen miles.
Wibbleton to Wobbleton,
Wobbleton to Wibbleton,
*Rock or bounce baby from side to side.*
Zoom, Zoom, Zoom
We’re going to the moon.
If you want to take a trip,
Climb aboard my rocket ship.
5, 4, 3, 2, 1 – Blastoff!
Babies can be lifted up at the appropriate time
during this rhyme. Older toddlers can “blast
off” themselves.
Just about any rhyme can be a bouncing rhyme, but these are especially built for it.
Bouncing Rhymes
Jack Be Nimble
**Jack be nimble, Jack be quick,**
Jack jump over the candlestick!
lifting your child at the end.*
Moses Supposes
Moses supposes his toeses are roses,
But Moses supposes erroneously,
For nobody’s toeses are posies of roses,
As Moses supposes his toeses to be.
*Bounce your baby, or tap your baby’s
feet/toes to the beat of this rhyme.*
Trit Trot to Boston
Bounce baby on knee
Trit trot to Lynn,
Trit trot over the bridge,
Lift up
But don’t fall in!
Drop through legs, or tip to the side
Giddyap!
Giddyap, giddyap, ride to town,
*Bounce baby on knees, facing forward.*
Giddyap, giddyap, up and down.
Giddyap fast,
Bounce quickly
Giddyap slow,
Bounce slowly
Giddyap, giddyap, giddyap, WHOA!
*Dip baby backwards gently.*
These Are Baby’s Fingers
These are baby’s toes,
Here is baby’s belly button,
Round and round it goes.
*Point out your child’s respective body
pars as they are mentioned in this
rhyme. If you like, substitute your
child’s name for the word “baby.”*
Here is the Beehive
Hold up fist
Where are the bees?
Shrug
Hidden away where nobody sees.
Watch as the bees come out of the hive,
1, 2, 3, 4, 5.
Count on fingers
Buzzzzz!
Tickle
*This rhyme is both a tickle rhyme and a
fingerplay all in one! It is especially great
for older toddlers and preschoolers, who
will enjoy the extra interaction.*
Hickory Dickory Dock
The mouse ran up the clock.
Tickle up your child’s arm
The clock struck one, The mouse ran down,
Clap once, tickle down your child’s arm
…The clock struck two, and down he flew,
…The clock struck three, the mouse said “Wheee!”
Round and Round the Garden
Went the teddy bear,
One step, two steps,
Tickle you under there!
*Jump fingers up baby’s arm. End
with a tickle.*
There Was a Little Mouse
Looking for his house.
Not here,
But here, here, here!
*Gently tickle baby in different places,
ending with the belly.*
This Little Piggy
This little piggy went to market.
This little piggy stayed home.
This little piggy had roast beef.
And this little piggy had none.
This little piggy cried “Wee, wee, wee!”
All the way home.
*Count off “piggies” on your baby’s fingers
or toes. Tickle your baby when you reach
the last piggy!
Get ready for lots of giggles when you say these rhymes together.*
Tickle Rhymes
Arabella Miller
Arabella Miller had a fuzzy caterpillar.
Make a caterpillar with your finger
First, it climbed upon her mother,
Put it on your hand
And then upon her baby brother.
*Tickle up baby’s arm*
They said, “Arabella Miller! Put away your caterpillar!”
Two Little Blackbirds
Two little blackbirds sitting on a hill,
One named Jack, the other named Jill.
Fly away, Jack! Fly away, Jill!
Come back, Jack! Come back, Jill!
Two little blackbirds sitting on a cloud,
One named soft, the other named loud.
Fly away soft! Fly away loud!
Come back soft! Come back loud!
Two little blackbirds sitting on a stick,
One named slow, the other named quick.
Fly away slow! Fly away quick!
Come back slow! Come back quick!
Here is a Bunny
Here is a bunny with ears so funny,
Hold up two fingers
And here is his hole in the ground.
*Make a circle with fingers*
When a noise he hears,
He pricks up his ears,
And jumps in his hole in the ground!
Make your bunny jump into the hole.
Five Little Monkeys
Five little monkeys jumping on the bed.
Hold up five fingers and make them bounce.
One fell off and bumped his head.
*Tap your own/baby’s head.*
Mama called the doctor and the doctor said,
Hold fingers like a telephone.
“No more monkeys jumping on the bed!”
*Shake finger as if scolding.
Repeat, taking away one finger/monkey each time
until no more “monkeys” remain.
These rhymes have small actions that children can do with their hands.*
I Had a Little Turtle
Put one hand on top of the other, sticking out thumbs
He lived in a box.
*Draw a square with finger
He swam in a puddle.
*Swim
He climbed on the rocks.
*Climb
He snapped at the mosquito,
*Clap
He snapped at the flea,
He snapped at the minnow,
And he snapped at me.
*Clap, point to self*
He caught the mosquito,
He caught the flea,
He caught the minnow,
But he didn’t catch me!
*Clap, point to self, and shake head.*
Fingerplays
One, Two, Three, Four, Five
Once I caught a fish alive.
*Clap hands together*
Six, seven, eight, nine, ten.
Count on the other hand
Then I let him go again.
*Open arms wide*
Why did you let him go?
*Hands-on hips*
Because he bit my finger so.
Which finger did he bite?
The little finger on the right.
*Grab and wiggle the pinky finger*
Way Up High in the Apple Tree
*Hold arms up high*
Two red apples looked down at me.
*Make fists for apples*
I shook that tree as hard as I could,
*Shake the tree*
And down fell the apples
*Hands to ground*
Mmmm, were they good!
Take a bite, rub your tummy.
The Itsy Bitsy Spider
The itsy bitsy spider climbed up the water spout.
*Walk fingers upward*
Down came the rain and washed the spider out.
Wiggle fingers downward
Out came the sun and dried up all the rain
*Put arms in a circle*
And the itsy bitsy spider climbed up the spout again.
I Put My Arms Up High
I put my arms down low.
I put them straight out to the side,
And then I let them go.
Suit actions to words.
Pat-A-Cake
Pat-a-cake, pat-a-cake,
Baker’s man,
Bake me a cake as fast as you can.
Clap in rhythm as you say this verse
Roll it, and pull it,
Roll hands
And mark it with a “B”
Tickle your child’s belly
And put it in the oven for Baby and me!
Clap in rhythm
Feel free to substitute your child’s name for
“baby” in this song when you say this rhyme.
With Our Hands
With our hands, we clap, clap, clap.
With our feet, we stamp, stamp, stamp.
We jump three times as high as can be.
Then we say, “Hey, look at me!”
One, Two, Buckle My Shoe
Pretend to tie shoe
Three, four, shut the door.
Clap hands
Five, six, pick up sticks.
Pretend to pick sticks up
Seven, eight, lay them straight.
Move arms in a “smoothing” motion
Nine, ten, a big fat hen.
Use arms to create around the belly
These rhymes are especially great for older toddlers and preschoolers, who will
enjoy doing the actions along with the words.
Action Rhymes
Ring Around the Rosie
Pocket full of posies,
Ashes, ashes, we all fall down!
Hold hands and walk in a circle.
Everyone sits down at the end.
The Grand Old Duke of York
Oh, the grand old Duke of York,
He had ten thousand men;
He marched them up to the top of the hill,
March in place
And he marched them down again.
And when they were up, they were up,
Stretch up
And when they were down, they were down,
Crouch
And when they were only halfway up,
Bend knees
They were neither up nor down.
Stretch up and crouch low, quickly.
Where is Thumbkin?
Where is thumbkin? Where is thumbkin?
Here I am! Here I am!
How are you today sir?
Very well, I thank you,
Runaway! Runaway!
Bring out and hide thumbs as appropriate.
Repeat if desired for more fingers.
Row, Row, Row Your Boat
Gently down the stream.
Merrily, merrily, merrily, merrily,
Life is but a dream.
Rock, rock, rock your boat,
Gently to the shore.
If you see a lion there,
Don’t forget to roar!
If you see a crocodile,
Don’t forget to scream!
Sit with your child on your lap.
Rock together as you sing this song.
This Old Man
This old man, he played one,
Hold up one finger
He played knick-knack on my thumb.
Tap your thumb
With a knick-knack, paddywhack,
Give a dog a bone,
This old man came rolling home.
This old man, he played two,
He played knick-knack on my shoe…
This old man, he played three,
He played knick-knack on my knee…
This old man, he played four,
He played knick-knack on the floor…
If You’re Happy and You Know It
If you’re happy and you know it, clap your hands.
And you really want to show it,
…stomp your feet.
…shout, “hooray!”
…do all three.
I’m a Little Teapot
I’m a little teapot short and stout.
Here is my handle, here is my spout.
(Hand motions)Put one hand on the hip.
Stick the other arm out to the side
When I get all steamed up hear me shout,
“Tip me over and pour me out!”
Lean-to the side.
I’m a very special pot it’s true.
Here let me show you what I can do.
I can change my handle and my spout.
Arms switch positions
These songs are especially great for older toddlers and preschoolers, who will
Action Songs
Head, Shoulders, Knees, and Toes
Head and shoulders, knees and toes, knees, and toes.
Eyes and ears and mouth and nose.
Point to each body part as you say it. Repeat as many
times as desired, doing it faster and faster each time.
Old McDonald
Old McDonald had a farm. E-I-E-I-O!
And on that farm, he had a cow. E-I-E-I-O!
With a “moo, moo” here, and a “moo, moo” there,
Here a “moo,” there a “moo,”
Everywhere a “moo, moo!”
- Pig…oink
- Goose…honk
- Dog…woof
- Cat…meow
- Sheep…baa
- Hen…cluck
Horse…neigh.
Baa Baa Black Sheep
Baa, baa, black sheep, have you any wool?
Yes sir, yes sir, three bags full.
One for my master, and one for my dame.
And one for the little boy who lives down the lane.
Ball, ball, black sheep, have you any wool?
The Wheels on the Bus
The wheels on the bus go round and round,
Round and round, round and round,
All through the town.
The horn on the bus goes beep, beep, beep…
The wipers on the bus go swish, swish, swish…
The lights on the bus go blink, blink, blink…
The babies on the bus go, “Wah, wah, wah”…
The mommies on the bus say, “I love you”…
Remember, your child doesn’t care if you have perfect pitch or not. S/he only
cares that you are spending time together. Sing away!
If you’re looking for more great music to listen to, check out a CD of children’s
music from the library or www.youtube.com. You have lots to choose from!
Songs
Are You Sleeping?
Are you sleeping? Are you sleeping?
Brother John? Brother John?
Morning bells are ringing. Morning bells are ringing.
Ding, ding, dong! Ding, ding, dong!
Twinkle Twinkle Little Star
How I wonder what you are.
Up above the world so high,
Like a diamond in the sky.
Rock-a-Bye Baby
Rock-a-bye baby, in the treetop.
When the wind blows, the cradle will rock.
When the bough breaks, the cradle will fall.
And down will come baby, cradle and all!
Five Little Ducks
Five little ducks went out one day,
Over the hills and far away.
Mother duck said, “Quack, quack, quack, quack!”
But only four little ducks came back.
Four little ducks…
Three little ducks…
Two little ducks…
One little duck…
So sad mother duck went out one day,
And all of the five little ducks came back!
Resources
- Resources for families [link: “Resources for families” → `resources.html`]
- McGuffey readers & sight words [link: “McGuffey readers & sight words” → `resources-mcguffey.html`]
- Anglia practice papers [link: “Anglia practice papers” → `anglia-practice.html`]

#### Section: Come and see the school.
Tours are arranged individually, Monday to Friday.
→ **Book a visit** (`forms.html#visit`)
→ **For parents** (`parents.html`)

---

### 4.56 `resources.html`

- **Browser title:** Resources for families – American Group International, Agadir
- **Meta description:** Free English resources from AGI: grammar self-helps, nursery rhymes, McGuffey readers and sight words, math resources.

Home / Student life / Resources for families [link: “Home” → `index.html`] [link: “Student life” → `student-life.html`]
**Page title (H1):** Resources for families
Free English learning helps for home: grammar self-helps, reading, rhymes and math resources.
→ **Request a tutor** (`forms.html#tutor-request`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: Resources
- Link card → `resources-nursery-rhymes.html`: Nursery rhymes for Pre-K
- Link card → `resources-mcguffey.html`: McGuffey readers & sight words

#### Section: English Self Helps
English Tenses
Forms, Mains uses, and Signal words
Past
Present
Future
Simple Past
Affirmative: Subject + verb in the past
e.g. She ate fish yesterday.
Negative: Subject+ did not + verb (infinitive)
e.g. They did not come to school last week.
Interrogative(?): Did + subject + verb (infinitive)
e.g. Did he understand the grammar lesson?
Simple Present
Affirmative: Subject + verb (s/es/ies)
e.g. I drink Coffee every morning.
Negative: Subject+ do not/does not + verb (infinitive)
e.g. She does not like watching football.
Interrogative(?): Do/Does + subject + verb (infinitive)
e.g. Do you like drama movies?
Simple Future
Affirmative: Subject +will+ verb
e.g. I will visit Japan next year.
Negative: Subject+ will not/won’t + verb (infinitive)
e.g. He will not come to school tomorrow.
Interrogative(?): Will + subject + verb (infinitive)
e.g. Will visit us next summer?
To talk about past events.
Describing an action or an event in the past.
General fact, repeated actions (routine),
For timetables (school, restaurant, club …)
Warnings …
To express future planning, ideas, decisions …
To talk about future events, predictions, expectations
To make a request or an offer.
last night, yesterday,
last month, last year, a year ago …
usually, always,
every, often …
tomorrow
Next week, month, year
Later, soon …
Past Continuous
Affirmative: Subject + was/were + verb + ing
e.g. She was playing football yesterday.
Negative: Subject + was not/were not + verb + ing
e.g. He was not studying last week.
Interrogative(?): Was/Were + subject + verb + ing
e.g. were you drawing during the lecture?
Present Continuous
Affirmative: Subject+ am/is/are + verb + ing
e.g. I am studying now.
Negative: Subject + am not/is not/are not + verb + ing
e.g. He is working at this moment.
Interrogative(?): Am/Is/Are + subject + verb + ing
e.g. Are you talking to somebody now.
Future Continuous
Affirmative: Subject + will + be + verb + ing
e.g. By Christmas I will be skiing like a pro.
Negative: Subject + will/won’t + be + verb + ing
e.g. She will be eating with Jane this evening.
Interrogative(?): Will + subject + be + verb + ing
e.g. Will we be studying this summer?
The action started at a specific time and finished in the past.
Action interrupted in the past.
Action in progress no
Near Future plan, intentions …
Actions that will happen at a specific time in the future
Talking about future predictions, expectations …
Last night, yesterday, last month,
Last year, a year ago …
Right now, at this moment …
Currently, at present time, now …
This time next week/next month/ next year …
At this moment in the future, by this time next year …
Past Perfect
Affirmative: Subject + had + verb in past participle
e.g. They had finished their meals.
Negative: Subject + had not + past participle
e.g. He had not done his homework.
Interrogative(?): Had + subject + past participle
e.g. Had she finished cleaning her bedroom?
Present Perfect
Affirmative: Subject + have/has + verb in past participle
e.g. He has finished readings moments ago.
Negative: Subject + have not/has not + past participle
e.g. I have not eaten my lunch yet.
Interrogative(?): Have/Has + subject + past participle e.g. Have you got any pets?
Future Perfect
Affirmative: Subject +will+ have + verb in past participle
e.g. I will have done my homework before you arrive.
Negative: Subject + will + have not + verb
e.g. She will not have finished by 5 o’clock.
Interrogative(?): Will + subject + have + past participle
e.g. Will you have finished painting your house by Sunday?
2 actions, one finished before the other.
An action happened in the recent past.
The precise time of the action is not important or not known.
When the period referred to has not finished.
Action 1 will be finished before action 2 in the future
After, before, already …
By the time, by …
Just, before, yet, after …
Never, since, yet, never …
By the time, by (day, time …)
When,
Past Perfect Continuous
Affirmative: Subject + had + been + verb + ing
e.g. I was tired because I had been working all day.
Negative: Subject + had not + been + verb + ing
e.g. She had not been working.
Interrogative(?): Had + subject + been + verb + ing
e.g. Had they been working?
Present Perfect Continuous
Affirmative: Subject + have/has + been + verb + ing
e.g. He has been living in London for two years.
Negative: Subject + have not/has not + been + verb + ing
e.g. She has not been doing anything.
Interrogative(?): Have/Has + subject + been + verb + ing
e.g. Have they been talking to each other?
Future Perfect Continuous
Affirmative: Subject + will + have + been + verb + ing
e.g. I will have been waiting here till you come.
Negative: Subject + will not/won’t + have + been + V + ing
e.g. He will not have been waiting for you.
Interrogative(?): Will + Subject + have + been + verb + ing
e.g. Will you have been waiting for me?
The action started and continued up in the past.
Showing a cause of past action
Unfinished actions which started in the past and continue to the present.
For temporary habits or situations.
Action will continue up until a particular event or time in the future.
To show cause and effect in the future
Because, after, before
Since, when …
Resources
- Nursery rhymes for Pre-K [link: “Nursery rhymes for Pre-K” → `resources-nursery-rhymes.html`]
- McGuffey readers & sight words [link: “McGuffey readers & sight words” → `resources-mcguffey.html`]
- Anglia practice papers [link: “Anglia practice papers” → `anglia-practice.html`]

#### Section: Come and see the school.
Tours are arranged individually, Monday to Friday.
→ **Book a visit** (`forms.html#visit`)
→ **For parents** (`parents.html`)

---

### 4.57 `services-document-editing.html`

- **Browser title:** Document editing in English – AGI Agadir
- **Meta description:** Document editing in English by AGI in Agadir: applications, CVs, reports and academic work, edited by native-level teachers.

Home / Programs / Document editing [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Document editing in English
Professional editing of documents in English – applications, CVs, reports and academic work.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
Tell us about your document and deadline; the office will confirm the price and turnaround. [TO CONFIRM: Prices and process to be confirmed.]

#### Section: In detail
These services are accessed on a view of the document/documents and the time it would take to fulfill the project.
Adults & professionals
- Adult high school diploma [link: “Adult high school diploma” → `adult-diploma.html`]
- Independent course studies [link: “Independent course studies” → `programs-independent-studies.html`]
- Business & medical English [link: “Business & medical English” → `professional.html`]
- Learning pods & fast track [link: “Learning pods & fast track” → `programs-learning-pods.html`]
- Exam proctoring [link: “Exam proctoring” → `services-proctoring.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.58 `services-proctoring.html`

- **Browser title:** Exam proctoring – American Group International, Agadir
- **Meta description:** Exam proctoring at AGI in Agadir for distance learners: which exams, fees per exam hour, opening days and conditions.

Home / Programs / Proctoring [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Exam proctoring
Paper and online exams invigilated at AGI for distance learners of North American and British universities, companies and certification bodies.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
Monday to Thursday, 9:00–17:00. A 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour.

#### Section: In detail
The American Group International offers proctoring services for students enrolled in a distance learning program at North American colleges or universities, or British Universities and English Exam testing with Anglia Examinations. We also can work with companies, certification programs, and government officials.

#### Section: Exams
- We invigilate paper-based as well as online exams.
- The tests are taken at the American Group International.
- Proctoring is only offered during regular office hours (Monday-Thursday, 9 AM to 5 PM) and not on weekends.
Please check your preferred date with us well in advance. Different events in our Institution might make it impossible for us to provide a room or staff on certain dates to proctor your exam. Due to these restraints, we unfortunately cannot proctor multiple exams on one day.
**Fees per exam**
- a non-refundable administrative fee of 15 EUR or 200 Dirhams.
- 15 EUR per scheduled exam hour or 200 Dirhams an hour.
- postage costs if needed and also fees for the proctor for traveling to the desired destination. (Varies)
If you cancel your appointment less than 24 hours in advance, we will charge the full amount.
If you arrive late for your exam, we will charge you extra for the delay.
**Conditions**
Please check with your college or university administration or language center or academic institution about the conditions for off-campus exams before contacting us. In order to get AGI registered with your home institution as a proctoring center, you may need to provide the following proctor details:
Julie Wilburn, Director
American Group International
Number 20, Rue Baalabek, Nahda, Agadir, Morocco 80000
Email: americanecoleagadir@gmail.com
Adults & professionals
- Adult high school diploma [link: “Adult high school diploma” → `adult-diploma.html`]
- Independent course studies [link: “Independent course studies” → `programs-independent-studies.html`]
- Business & medical English [link: “Business & medical English” → `professional.html`]
- Learning pods & fast track [link: “Learning pods & fast track” → `programs-learning-pods.html`]
- Document editing [link: “Document editing” → `services-document-editing.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.59 `supplies.html`

- **Browser title:** School supplies list – American Group International, Agadir
- **Meta description:** AGI school supplies list for elementary (K3–8) and high school (grades 9–12).

Home / Admissions / Policies / School supplies list [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** School supplies list
What to bring on the first day, for elementary and high school.

#### Section: AGI Academic School Supplies List

#### Section: AGI Supplies List
Elementary K3-8th
Change of clothes!
Tissues or toilet paper
2- 5 subject notebooks
3- packs of pencils
2- packs of erasers
2- pencil sharpeners
2- packs of white paper
1- pack of colored paper
1- pack of colored markers or pencils
1- whiteboard markers
1 – pack highlighters
1- scissors
2- glue sticks
2- paint and paint brushes
2- wet wipes
High School Supplies Grade 9-12th
3- white-out
3- packs pencils
Text as published by AGI. Please check with the office for the current version. Source: “AGI Academic School Supplies List” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- Volunteer hours [link: “Volunteer hours” → `volunteer-hours.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.60 `teachers-careers.html`

- **Browser title:** Teach with AGI – American Group International, Agadir
- **Meta description:** Teach with AGI: online teachers database, learning pods and STEM educators workshops.

Home / Programs / Teach with AGI [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Teach with AGI
Join AGI's online teachers database and workshops – for freelance teachers, learning-pod leaders and STEM educators.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
→ **Send your profile** (`forms.html#enquiry/careers`)

#### Section: In detail
Professor Jimmy
Qualifications- B-2 CEFR
BA degree
Courses:
English B-2 and conversational lessons.
Delivery Online/In Person
Professor Taiwo
5 years’ Experience
BA-MA degrees.
- Public Speaking
- Humanities
- International Business
- English Literature
- Creative Writing
Secondary Education.
ESL/EFL Classes

#### Section: Professor Asma
I am a TESOL-certified educator with hands-on classroom experience and a passion for creating inclusive, student-centred learning environments. With a degree in Human Resources and a strong interest in psychology, I bring valuable insight into student motivation and behaviour, enabling me to address both academic and emotional needs effectively.
My experience studying and living abroad has deepened my appreciation for diverse cultures and educational systems, which I draw upon to foster globally minded classrooms where all learners feel valued and engaged. Over the course of my teaching journey, I have developed strong classroom management skills and the ability to adapt lessons to different learning styles, encouraging critical thinking and active participation to build confidence and independence.
Fluent in Arabic, French, and English—with Spanish in progress—I am well-prepared to support multilingual learners and bridge language barriers. I view language as more than a means of communication: it is a gateway to broader opportunities and richer perspectives.
Delivery Online

#### Section: STEM Educators Workshop Job Interviews
Empowering the Next Generation of STEM Educators in Morocco!
Our workshop at English Castle Center – Bouskoura and Anglia Examinations and AGI were a true milestone in teacher development:
“Teaching in English – Succeeding in STEM Classrooms & Job Interviews”.
Co-led by international experts Ms. Julie Wilburn (AGI) and Ms. Nadya Eve Mezeli (TEFL Expert), alongside our Executive Director Mr. Noureddine Khizani.
This high-impact session welcomed Master’s & PhD holders for the Faculté des sciences Ben M’Sik looking to thrive in CLIL/EMI environments.
What participants gained:
Proven strategies for teaching STEM (Science, Technology, Engineering and Maths) in English.
Interview prep for local & international schools
Insight into Anglia STEM teachers’ certifications
CLIL/EMI demo lesson
Special thanks to Mrs. Sanaa EL FIlALI (Faculté des sciences Ben M’Sik) for her continued trust and partnership.
Morocco’s future STEM teachers are ready to lead — and English Castle Center – Bouskoura and AGI are proud to support them every step of the way.
Teachers
- For teachers [link: “For teachers” → `teachers.html`]
- C.I.T.E. / TESOL certification [link: “C.I.T.E. / TESOL certification” → `teachers-cite.html`]
- USA private-school sponsorship [link: “USA private-school sponsorship” → `teachers-usa-sponsorship.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.61 `teachers-cite.html`

- **Browser title:** C.I.T.E. / TESOL certification – AGI Agadir
- **Meta description:** Anglia C.I.T.E. (TESOL) certification in Morocco: who it is for, English level needed, preparation, when and how to take it.

Home / Programs / C.I.T.E. [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** C.I.T.E. / TESOL certification
Anglia's Certificate for International Teachers of English: recognition of your English and your teaching – for life.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)
→ **Register on angliamorocco.org** (`https://angliamorocco.org/citem/`)

#### Section: Elevate Your Teaching Career

#### Section: C.I.T.E - Certificate for International Teachers of English (TESOL)
Enhance your teaching skills and gain recognition for your proficiency with the prestigious C.I.T.E. certification offered by Anglia Examinations England. This lifelong qualification demonstrates your mastery of English and your ability to teach the language effectively. Register now to elevate your teaching career!

#### Section: What is C.I.T.E?
C.I.T.E. (Certificate for International Teachers of English) is a prestigious TESOL qualification offered by Anglia Examinations England. This certification demonstrates your mastery of English and your ability to teach the language effectively. It’s a lifelong qualification with no expiration date, recognized worldwide.
**Who is C.I.T.E. for?**
The C.I.T.E. test recognizes your competence in English language skills necessary for teaching. It is suitable for:
**Current English Teachers**
Validate and enhance your English teaching skills.
**Aspiring Teachers**
Start your teaching career with a recognized certification.
**High School Teachers**
Add English teaching to your skill set.
**Primary School Teachers**
Meet new curriculum requirements with confidence.
**How to Register**
- Determine Your English Level: Visit www.angliaonline.com or schedule an appointment with an authorized Anglia partner.
- Register Online: [Register Here]
- Payment and Confirmation: After registration, you will be contacted via email to arrange payment for the examination.
**Prepare for Success**
Anglia Morocco offers the necessary training and resources to help you succeed. Recommended books include:
- Brown, H. Douglas. Principles of Language Learning and Teaching. Prentice Hall Regents, 2000.
- Brown, Douglas H. Teaching by Principles: An Interactive Approach to Language Pedagogy. Prentice Hall Regents, 2001.
- Harmer, Jeremy. The Practice of English Language Teaching. Longman, 1983.
- Hewings, Martin. Advanced Grammar in Use. Cambridge University Press, 2005.
- Ioannou-Georgiou, Sophie, and Pavlos Pavlou. Assessing Young Learners. Oxford University Press, 2003.
- Slattery, Mary, and Jane Willis. English for Primary Teachers. Oxford University Press, 2001.
- Vale, D., and A. Feunteun. Teaching Children English. Cambridge University Press, 1995.
**Examination Process**
- Format: Paper format at Anglia partnerships in Morocco or online via the Anglia Examinations UK Portal.
- Duration: The C.I.T.E test lasts 3 hours.
- Guidance: Candidates will receive login details and a guide prior to the exam session.
**Results and Certificates**
- Results: 5-6 weeks after tests are received at the control centre in Chichester, England.
- Certificates: Up to 8 weeks after completion of testing.
- Results will be sent electronically to the email provided during the application.

#### Section: Why Choose Anglia C.I.T.E.?
**No Entry Requirements**
Inclusive Approach: The C.I.T.E. certification is accessible to all, regardless of prior qualifications, making it ideal for both current and aspiring English teachers.
Flexible Levels: Candidates can choose the level that best suits their needs, from C.I.T.E. Master to versions tailored for young and very young learners.
**Lifelong Qualification**
Permanent Certification: Once earned, the C.I.T.E. certification is valid for life, providing lasting value without the need for renewal.
**Recognition and Accreditation**
Internationally Recognized: The C.I.T.E. certification is respected worldwide, ensuring your qualifications are valued by educational institutions and employers globally.
Accredited Standards: Anglia Examinations England ensures that the C.I.T.E. certification meets high standards of quality and rigor.
**Practical Focus**
Teaching Competence: The C.I.T.E. certification demonstrates your proficiency in essential English language skills needed for effective teaching.
Diverse Application: Suitable for a wide range of teaching contexts, from primary schools to high schools, and for teachers with varied backgrounds.
**Comprehensive Preparation**
Support and Training: Anglia Morocco offers extensive preparatory support, including practice exams and recommended reading materials.
Professional Development: The certification process and associated resources help enhance your teaching skills and knowledge.
**Flexible Examination Options**
Convenient Testing: Choose to take the C.I.T.E. test in paper format at Anglia partnerships in Morocco, at the headquarters in Agadir, or online through the Anglia Examinations UK Portal.
**Accreditation**
The C.I.T.E. (Certificate for International Teachers of English) is accredited by Anglia Examinations England, a recognized body in the UK that ensures the highest standards of quality and rigor in English language teaching certifications.
**Recognition**
- International Recognition: The C.I.T.E. certification is globally recognized and accepted by educational institutions, language schools, and employers worldwide.
- Career Advancement: With a C.I.T.E. certification, you enhance your career prospects in the field of English language teaching, gaining recognition for your proficiency and teaching skills.
- Professional Development: The certification opens doors for further professional development opportunities, making you a more competitive candidate in the job market.
For more information on accreditation and recognition, visit the Anglia Examinations England official website.
**Contact Us**
Have questions or need more information? Reach out to us at:
Number 20, Rue Baalabek, Hay Nahda Agadir, Morocco 80000
Ready to elevate your teaching career?
Get Certified Now

#### Section: GET YOUR TESOL WITH US! CITE with Anglia Examinations

#### Section: About the C.I.T.E Exams: Exams for Teachers of English TESOL.
C.I.T.E. is Anglia Examinations’ Certificate for International Teachers of English. These exams provide teacher certification for English teachers, who may or may not have any other English teaching qualifications, and gives them an opportunity to obtain recognition for their English language teaching skills, knowledge and experience. Our C.I.T.E. exams work on the same principle as any other test of English for special purposes. In this case the special purpose is teaching English. The tests are mapped to the Common European Framework of Reference for Languages (CEFR) and our C.I.T.E certificate provides evidence of English teaching ability.
**Who is C.I.T.E. for?**
There are no entry qualifications for the C.I.T.E. test. Although you may well have previous qualifications in English, none are compulsory requirements. The C.I.T.E. test is not in itself a teaching qualification, but recognition of your competence in the relevant English language skills needed for teaching. It can, therefore, equally be taken by teachers who are currently teaching English, or students who are planning to, and have gained knowledge of classroom language and practice through study. It may, for example, be taken by High School mathematics teachers who find themselves timetabled with two lessons of English a week, by Primary school teachers who have been co-opted into teaching English under a government initiative, or English teachers whose original qualification concentrated on 19th Century literature and who want to have a focus for updating their practical, classroom-language skills.
The C.I.T.E. tests recognise that teaching young learners and teaching higher-level, older, learners may require different language levels, theory and practice. For this reason, candidates are offered three versions of the test:

#### Section: C.I.T.E.
C.I.T.E. (Young Learners)
C.I.T.E. (Very Young Learners).
Referring to a sample paper should help a candidate or their representative decide which level is the most appropriate. Primary school teachers are not obliged to take either of the Young Learner versions, but the opportunity is available.
**What level of English do you need?**
You need the level of English required to be a competent teacher. If you think you have this, it is likely that you are at the right level for the C.I.T.E. test.
For the C.I.T.E. it is likely that your level of English will be C1 on the CEFR. For the C.I.T.E. (YL) your level of English should be at least B2 on the CEFR. For the C.I.T.E. (VYL) your level of English should be at least B1 on the CEFR.
It isn’t easy to relate the level required to any general English test. However, the English required in the C.I.T.E. tests is related to knowledge of grammatical terms and functions in English included in the main-suite syllabus, together with classroom language in English.
What preparation is necessary for the examination?
To a certain extent you must make your own judgement on this by looking at the overview of the test, test specifications and sample papers. Although your representative may be able to indicate where you can find a suitable local course or study group, there is no set course either in English or in teaching which leads to the C.I.T.E. test.
However, below is a list of books which would help you to prepare for the test and which, if you do not know them already, we recommend you read for your own professional development as an English teacher.
- Brown, H. Douglas. 2000. Principles of Language Learning and Teaching. Prentice Hall Regents.
- Brown, Douglas H. 2001. Teaching by Principles: An Interactive Approach to Language Pedagogy. Prentice Hall Regents.
- Harmer, Jeremy. 1983. The Practice of English Language Teaching. Harlow: Longman.
- Hewings, Martin. 2005. Advanced Grammar in Use. Cambridge: Cambridge University Press.
- Ioannou-Georgiou, Sophie and Pavlos Pavlou. 2003. Assessing Young Learners. Oxford: Oxford University.
- Slattery, Mary and Jane Willis. 2001. English for Primary Teachers. Oxford: Oxford University Press.
- Vale, D. and A. Feunteun. 1995. Teaching Children English. Cambridge: Cambridge University Press.
**When and how can you take the C.I.T.E test?**
If you are interested in taking a C.I.T.E. test then go to the Anglia Worldwide section. There you can find details of your local representative who will tell you how to register, and give you the time and place of the next test session most local to you. If you don’t know who your local representative is, or do not have one, or would like to find out more information about CITE contact Anglia Examinations via the online enquiry form, click here.
**C.I.T.E. Sample Papers**
Training for teachers is also important for them to have effective class management skills. … Training sessions are needed to help the teachers learn or create new teaching strategies that will bring back the interest of their students in the classrooms and encourage learning. Also, this will enable the teachers in the area of Morocco the many international skills and concepts that they can not learn in the university program. B.A. is required for this volunteer/training program.
If you are interested in volunteering for this program please send us this form in a PDF format and your B.S. degree with passport or national identity card to apply. You will also be asked to take an exam to see what level of English you have using the Anglia system that is from the European Common Framework.
We also welcome to receive applicants to take the TESOL CITE with us as you sit with one of our testing administrators. Apostille and legalization is available to the document. We kindly will evaluate your skills prior and counsel you on which one of the three levels are for you.
We welcome all applicants from all countries and all disciples of studies.
Thank you
Julie Wilburn, Director
**Reference Letter from one of our Teachers…..**
October 28 th, 2019
To Whom it May Concern:
I am very happy to write this letter to let you know about the time I spent in the American Group International School from September 2018 to June 2019.
The experience I had in AGI was very unique. After I spent one fruitful year, I felt that I belong to an amazing family. Every day I spent there was beneficial and enjoyable. I always learned something new and improved different skills such as my English, language teaching, communication, and translation. I am proud to be trained by Juliana Wilburn, a wonderful school director that is always ready to teach you something and help others. I admit that I learned from her what I did not learn from the university. I think that AGI is a perfect place to learn for both students and junior teachers.
I highly recommend the teacher training program for junior English teachers who want to sharpen their language teaching skills and build a strong personality.
Yours Sincerely,
Abdelmajid El Yacouby

#### Section: About the C.I.T.E Exams: Exams for Teachers of English
There are no entry qualifications for the C.I.T.E. test. Although you may well have previous qualifications in English, none are compulsory requirements. The C.I.T.E. test is not in itself a teaching qualification, but a recognition of your competence in the relevant English language skills needed for teaching. It can, therefore, equally be taken by teachers who are currently teaching English, or students who are planning to, and have gained knowledge of classroom language and practice through study. It may, for example, be taken by High School mathematics teachers who find themselves timetabled with two lessons of English a week, by Primary school teachers who have been co-opted into teaching English under a government initiative, or English teachers whose original qualification concentrated on 19th Century literature and who want to have a focus for updating their practical, classroom-language skills.
The C.I.T.E. tests recognize that teaching young learners and teaching higher-level, older, learners may require different language levels, theory, and practice. For this reason, candidates are offered three versions of the test:
To a certain extent, you must make your own judgment on this by looking at the overview of the test, test specifications and sample papers. Although your representative may be able to indicate where you can find a suitable local course or study group, there is no set course either in English or in teaching which leads to the C.I.T.E. test.
However, below is a list of books that would help you to prepare for the test and which, if you do not know them already, we recommend you read for your own professional development as an English teacher.
If you are interested in taking a C.I.T.E. test then go to the Anglia Worldwide section. There you can find details of your local representative who will tell you how to register and give you the time and place of the next test session most local to you. If you don’t know who your local representative is, do not have one, or would like to find out more information about CITE contact Anglia Examinations via the online inquiry form, click here.
س.

#### Section: C.I.T.E - Certificate for International Teachers of English (TESOL)

#### Section: What is C.I.T.E?
**Who is C.I.T.E. for?**
**Current English Teachers**
**Aspiring Teachers**
**High School Teachers**
Add English teaching to your skill set.
**Primary School Teachers**
**How to Register**
- Register Online: [Register Here]
**Prepare for Success**
**Examination Process**
- Duration: The C.I.T.E test lasts 3 hours.
**Results and Certificates**

#### Section: Why Choose Anglia C.I.T.E.?
**No Entry Requirements**
**Lifelong Qualification**
**Recognition and Accreditation**
**Practical Focus**
**Comprehensive Preparation**
**Flexible Examination Options**
**Accreditation**
**Recognition**
**Contact Us**
Ready to elevate your teaching career?
Get Certified Now
Teachers
- For teachers [link: “For teachers” → `teachers.html`]
- USA private-school sponsorship [link: “USA private-school sponsorship” → `teachers-usa-sponsorship.html`]
- Teach with AGI [link: “Teach with AGI” → `teachers-careers.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.62 `teachers-usa-sponsorship.html`

- **Browser title:** USA private-school teacher sponsorship – AGI Agadir
- **Meta description:** USA private-school teacher certification sponsorship through AGI: requirements, process, 30 days, US$60.

Home / Programs / USA sponsorship [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** USA private-school teacher sponsorship
Certification sponsorship for teaching in private schools in the United States – process, requirements and fee.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: In detail
- USA Private School Teacher Certification Sponsorship Program
- Welcome to our Teacher Certification Sponsorship Program! This program is designed to help aspiring educators achieve certification for private school teaching positions in the USA.
Program Details:
- Eligibility Requirements:
- Proof of a Bachelor’s degree (BA) from an accredited institution.
- Clear character or background check (details on what this entails).
- School sponsor with proof of teaching experience.
- Certification Type:
- This certification is specifically for private school teaching positions and may not be accepted for public school systems.
- Notarization:
- All documentation provided will be notarized for authenticity.
Benefits of Certification:
- Career Advancement:
- Elevate your career with our certification, opening doors to teaching positions in private schools.
- Supportive Environment:
- Guidance and support throughout the certification process.
Cost:
- The cost of the certification sponsorship is $60.00.
Application Process:
- Step 1: Application Submission
- Submit your application with the required documents (BA degree proof, background check, and school sponsor documentation).
- Step 2: Review Process
- Our team will review your application for eligibility.
- Step 3: Notarization and Certification
- Upon approval, documents will be notarized and certification will be issued.
Contact Information:
Disclaimer:
- This certification is valid for private school systems only and may not meet the requirements for public school teaching positions.
- Build your career with us. Join our Teacher Certification Sponsorship Program today!
- Internship of 30 days Available.
- Week 1: Orientation & Classroom Observation
- Day 1-2:
- Orientation: Introduction to the school’s mission, values, curriculum, and teaching
- standards.
- Training on Policies and Procedures: Review school policies on student behaviour,
- safety, and inclusivity.
- Day 3-5:
- Classroom Observations: Observe various grade levels and subjects. Take notes on
- teaching styles, classroom management techniques, and student engagement
- strategies.
- Week 2: Assisting in the Classroom
- Day 6-7:
- Reflection Session: Reflect on observed teaching practices and discuss questions
- with a mentor teacher.
- Team Teaching: Assist the lead teacher with small group instruction, classroom
- organization, and learning activities.
- Activity Preparation: Help prepare materials for lessons, such as worksheets,
- multimedia resources, or visual aids.
- Day 8-10:
- Focused Observation on Classroom Management: Learn strategies to manage
- student behaviour and maintain a positive learning environment.
- Mentor Feedback: Discuss observations and receive feedback from a mentor on how
- to improve classroom presence and interaction.
- Classroom
- Week 3: Independent Teaching with Supervision
- Day 11-15:
- Lesson Planning: Design and prepare lesson plans under the guidance of the lead
- teacher, focusing on objectives, student engagement, and assessment.
- Teaching Practice: Teach 1-2 lessons per day with mentor observation and
- feedback.
- Daily Reflections: Reflect on the teaching experience, noting successes and areas
- for improvement.
- Week 4: Independent Teaching & Classroom Management
- Day 16-20:
- Full Lesson Execution: Take on more responsibility by teaching entire lessons,
- managing classroom activities and handling unexpected situations.
- Classroom Management Techniques: Apply classroom management strategies with
- minimal assistance from the lead teacher.
- Student Assessment: Begin assessing student work and providing constructive
- feedback with guidance from a mentor.
- Week 5: Assessment & Reflection
- Day 21-25:
- Student Assessments and Grading: Learn grading practices, complete student
- assessments, and analyse performance to guide future lesson planning.
- Parent Communication: Observe or participate in parent-teacher communication (if
- applicable), focusing on effective, positive interactions.
- Mid-Internship Review: Meet with a mentor for a mid-internship review to discuss
- progress, challenges, and professional goals.
- Week 6: Professional Development and Wrap-Up
- Day 26-28:
- American Group International Agadir | TEACHER INTERSHIP 30 DAYS PLUS SURVEY
- American Group International Internship 30 days
- Professional Development: Attend workshops on topics such as differentiation,
- technology in education, or special education.
- Self-Evaluation: Reflect on personal growth and set professional goals for the future.
- Day 29-30:
- Final Reflection and Presentation: Present a summary of the internship experience
- to the teaching staff, highlighting key lessons, insights, and growth.
- Exit Interview: Meet with the school administration and mentor to discuss strengths,
- areas of improvement, and future career plans.
- This outline balances observation, practice, and reflection, enabling (you) the intern
- to gradually build confidence and proficiency in the classroom.
Teachers
- For teachers [link: “For teachers” → `teachers.html`]
- C.I.T.E. / TESOL certification [link: “C.I.T.E. / TESOL certification” → `teachers-cite.html`]
- Teach with AGI [link: “Teach with AGI” → `teachers-careers.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.63 `volunteer-hours.html`

- **Browser title:** Volunteer hours – American Group International, Agadir
- **Meta description:** AGI in-service volunteer hours for high school: 40 hours, ten per year.

Home / Admissions / Policies / Volunteer hours [link: “Home” → `index.html`] [link: “Admissions” → `admissions.html`] [link: “Policies” → `policies.html`]
**Page title (H1):** Volunteer hours
Forty hours of service before graduation: what counts and how hours are recorded.
Overview In-service volunteer hours are an essential component of the high school experience, providing students with the opportunity to give back to the community, develop leadership skills, and gain real-world experience. These hours are also a requirement for graduation at American Group International. Requirements To fulfil the graduation requirement, students must complete a minimum of 40 volunteer hours (10 each year) over the course of their high school career. These hours should be documented and approved by the school. Eligible Activities Volunteer activities should:
- Benefit the community or an organization.
- Be unpaid and voluntary.
- Not be part of a regular job or family obligation.
- Be approved by the school coordinator in advance if the organization is not on the
pre-approved list.
Examples of Eligible Activities:
- Volunteering at local non-profits (soup kitchens, shelters, etc.).
- Participating in community clean-up projects.
- Assisting in local libraries or museums.
- Helping at school events outside regular school hours.
- Tutoring or mentoring younger students.
- Involvement in faith-based service projects (if open to the wider community).
Non-Eligible Activities:
- Tasks that are part of a paid job.
- Family chores or personal family business.
- Activities without prior approval from the volunteer coordinator.
- Court-ordered community service.

#### Section: Documentation and Approval Process
- Pre-Approval: Before starting a new volunteer activity, students should seek preapproval from the volunteer coordinator if the organization is not on the pre-approved
list.
- Log Hours: Students must maintain a volunteer log to document their hours.
This log should include:
- Date of service
- Grades 9, 10, 11, 12.
- Description of the activity
- Number of hours completed
- Supervisor’s name and contact information
- Supervisor’s signature
- Submission: Completed volunteer logs should be submitted to the volunteer
coordinator by [Specific Deadlines], usually at the end of each semester.
- Verification: The volunteer coordinator will verify the hours with the organization or
supervisor listed on the log.
- Approval: Once verified, hours will be recorded in the student’s file towards their
graduation requirement.
Benefits of Volunteering
- Skill Development: Gain skills in leadership, teamwork, and problem-solving.
- Career Exploration: Explore potential career interests and gain experience.
- College Applications: Enhance college applications and resumes with documented
community service.
- Personal Growth: Build self-esteem, compassion, and a sense of responsibility.
Text as published by AGI. Please check with the office for the current version. Source: “In-Service Volunteer Hours for High School” (former AGI website)
All policies
- Academic handbook [link: “Academic handbook” → `handbook.html`]
- Attendance [link: “Attendance” → `attendance.html`]
- Promotion & retention [link: “Promotion & retention” → `promotion-retention.html`]
- Provisional placement & assessment [link: “Provisional placement & assessment” → `placement-policy.html`]
- Parent responsibility [link: “Parent responsibility” → `parent-responsibility.html`]
- Refunds & complaints [link: “Refunds & complaints” → `refunds-complaints.html`]
- Media [link: “Media” → `media-policy.html`]
- Homework [link: “Homework” → `homework.html`]
- School supplies list [link: “School supplies list” → `supplies.html`]
→ **Ask the office a question** (`forms.html#enquiry/programs`)

#### Section: Questions about joining AGI?
Visit the school, or ask the office – we reply within one working day.
→ **Book a visit** (`forms.html#visit`)
→ **Ask a question** (`forms.html#enquiry`)

---

### 4.64 `wellbeing-adhd-coaching.html`

- **Browser title:** ADHD holistic coaching – American Group International, Agadir
- **Meta description:** ADHD holistic coaching with Julie Wilburn, accredited Holistic Therapeutic Coach (IPHM, ICAHP), in Agadir and online.

Home / Programs / ADHD coaching [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** ADHD holistic coaching
One-to-one coaching for children and adults on focus, organization and time management – in Agadir and online.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: In detail
Dear Clients and Students: May 4, 2025
I hope this message finds you well. I’m excited to share that American Group USA now offers specialized ADHD coaching services both here in Agadir and online to individuals around the world!
As part of our mission to support individuals with ADHD, I, Julie Wilburn, am personally offering one-on-one ADHD Holistic Practitioner Coaching. These services are available for both children and adults and are designed to help individuals manage ADHD symptoms, improve focus, organization, time management, and achieve personal and professional goals.
Given that we are deeply involved in education, we are highly qualified to handle ADHD-related challenges, especially in children, with a strong focus on early education. Our expertise allows us to offer tailored coaching strategies that help children develop skills for success in their academic and social lives from an early age.
I firmly believe that holistic therapy—without medication—combined with diet regulation, exercise, and play therapy provides significant benefits for children with ADHD. By addressing the root causes and supporting healthy development, this approach can help children thrive and reach their full potential. Additionally, learning time management skills and developing strategies to help children stay on track with their day and follow a schedule is crucial in helping them navigate daily life more effectively.
Whether you’re seeking support for yourself or a loved one, my ADHD coaching services can make a real difference. I offer personalized sessions tailored to the unique needs of each individual, helping them overcome obstacles and succeed in various areas of life.
If you or someone you know could benefit from my ADHD coaching services, please feel free to reach out. I’d be happy to provide more information or schedule a consultation.
Looking forward to hearing from you!
Best regards,
Julie Wilburn
ADHD Holistic Practitioner
American Group USA

#### Section: What is an ADHD Holistic Practitioner?
ADHD Holistic Practitioners offer a comprehensive, non-medical approach to managing Attention Deficit Hyperactivity Disorder (ADHD) by using natural and supportive strategies to address the underlying symptoms. Their work focuses on enhancing an individual’s overall well-being and empowering them to manage ADHD effectively in various aspects of life. Here’s a breakdown of what ADHD Holistic Practitioners do:
- Individualized Coaching:
Holistic practitioners offer personalized coaching, working closely with clients to understand their specific challenges. They create customized strategies and plans to help individuals manage ADHD symptoms, such as inattention, impulsivity, and hyperactivity.
- Behavioral and Cognitive Strategies:
Practitioners help individuals develop skills to regulate emotions, improve focus, and enhance organizational abilities. This includes teaching practical strategies like time management, task prioritization, and setting achievable goals.
- Diet and Nutrition Guidance:
A significant part of holistic therapy involves addressing diet and nutrition. ADHD Holistic Practitioners often recommend dietary changes, emphasizing foods that support brain health and emotional regulation. They might suggest eliminating processed foods or additives and incorporating more whole foods, essential fatty acids, and micronutrients to enhance cognitive function and emotional balance.
- Exercise and Physical Activity:
Exercise is a key component in managing ADHD symptoms. Holistic practitioners encourage physical activities that help improve focus, release excess energy, and reduce anxiety. Regular exercise, like walking, yoga, or sports, is incorporated into a treatment plan to boost overall health and mental clarity.
- Play Therapy (for Children):
For children with ADHD, play therapy is often used to help them express emotions, develop social skills, and improve focus in a non-threatening, fun environment. It encourages creativity and self-expression while providing a structured way for children to work through their challenges.
- Mindfulness and Stress Management Techniques:
Holistic practitioners often incorporate mindfulness, meditation, and relaxation techniques into their coaching sessions. These practices help reduce stress, improve concentration, and enhance emotional regulation. Mindfulness helps individuals with ADHD to stay grounded and become more aware of their thoughts and behaviors in the present moment.
- Support in Developing Routines and Time Management:
Creating a structured routine is critical for individuals with ADHD. Holistic practitioners help clients—especially children—develop time management skills, build schedules, and learn how to stick to a routine. This structure helps reduce anxiety, improves focus, and allows individuals to manage their day more effectively.
- Family Support and Education:
Holistic practitioners also work with families to provide support and education on ADHD. They teach families how to best support the individual, offer coping mechanisms, and help set realistic expectations.
By taking a holistic, individualized approach, ADHD Holistic Practitioners aim to not only alleviate the symptoms of ADHD but also help individuals thrive by improving their overall quality of life through sustainable lifestyle changes, emotional well-being, and practical skills development.
Wellbeing (i-Heart)
- i-Heart therapeutic services [link: “i-Heart therapeutic services” → `wellbeing.html`]
- Holistic play therapy [link: “Holistic play therapy” → `wellbeing-play-therapy.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.65 `wellbeing-play-therapy.html`

- **Browser title:** Holistic play therapy – American Group International, Agadir
- **Meta description:** Holistic play therapy at AGI school, Agadir: approach, benefits and sessions.

Home / Programs / Play therapy [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** Holistic play therapy
Therapeutic play that supports the emotional, behavioral, social and cognitive development of children.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: Holistic Play Therapy Practitioner Services at Our School

#### Section: Supporting the Whole Child Through Therapeutic Play
At our school, we are proud to offer Holistic Play Therapy sessions facilitated by a certified Holistic Play Therapy Practitioner. This specialized service supports the emotional, behavioural, social, and cognitive development of children through guided therapeutic play in a safe, supportive environment.
**What Is Holistic Play Therapy?**
Holistic Play Therapy integrates traditional play therapy techniques with a whole-child approach—focusing on the mind, body, and emotional well-being. It is especially effective for children experiencing anxiety, trauma, behavioural challenges, learning differences, or social-emotional delays.
What Does a Holistic Play Therapy Practitioner Do?
Facilitates one-on-one or small-group therapeutic play sessions
Uses creative tools such as art, storytelling, sensory play, movement, and role-playing
Helps children express emotions they may not yet have the words for
Encourages emotional regulation, problem-solving, and self-awareness
Collaborates with parents, teachers, and specialists to support the child’s overall development
Provides individualized strategies and tools to support progress at school and home
**Availability & Cost**
Our certified Holistic Play Therapy Practitioner is available for appointments during school hours.
Sessions are 150 dirhams per hour
Services can be scheduled weekly, biweekly, or as needed.
If you believe your child could benefit from holistic therapeutic play, please contact our school office to book a consultation or learn more.
Wellbeing (i-Heart)
- i-Heart therapeutic services [link: “i-Heart therapeutic services” → `wellbeing.html`]
- ADHD holistic coaching [link: “ADHD holistic coaching” → `wellbeing-adhd-coaching.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

---

### 4.66 `wellbeing.html`

- **Browser title:** i-Heart therapeutic services – AGI Agadir
- **Meta description:** i-Heart holistic therapeutic services and counseling at AGI: ADHD coaching and holistic play therapy.

Home / Programs / Wellbeing [link: “Home” → `index.html`] [link: “Programs” → `programs.html`]
**Page title (H1):** i-Heart therapeutic services
Holistic support for children, teens and adults – coaching, therapeutic play and counseling, alongside school.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **WhatsApp us** (`https://wa.me/212688739393?text=Hello%20AGI%2C%20`)

#### Section: Our services
- Link card → `wellbeing-adhd-coaching.html`: ADHD holistic coaching · Focus, organization and time management for children and adults.
- Link card → `wellbeing-play-therapy.html`: Holistic play therapy · Guided therapeutic play for emotional, social and behavioral development.

#### Section: In detail
This page is under construction. Please check back soon!
Wellbeing (i-Heart)
- ADHD holistic coaching [link: “ADHD holistic coaching” → `wellbeing-adhd-coaching.html`]
- Holistic play therapy [link: “Holistic play therapy” → `wellbeing-play-therapy.html`]
→ **Prices** (`fees.html#services`)

#### Section: Is this the right program?
Tell us what you are looking for and we will help you choose.
→ **Ask about this program** (`forms.html#enquiry/programs`)
→ **All programs** (`programs.html`)

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
