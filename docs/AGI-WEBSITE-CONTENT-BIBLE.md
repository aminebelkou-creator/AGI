# AGI — Website Content Bible
## Master editorial document and source-of-truth governance

**Version:** 1.0 · 16 November 2026  
**Project:** American Group International (AGI), Agadir, Morocco  
**Source branch reviewed:** `cms-test-smartsite`  
**Document status:** Editorial master framework — repository-derived; institutional approvals remain pending where explicitly marked  
**Intended users:** AGI leadership, content editors, SmartSite/CMS implementers, SEO and translation teams, AI content agents

> **Purpose.** This document governs the meaning, evidence, ownership, approval, publication and maintenance of all AGI website content. It is the editorial control layer above the detailed page-by-page content specification. It does not replace original AGI texts, the structured content exports, source HTML, policy documents, or the facts/claims/privacy registers.

---

# 0. How to use this master document

## 0.1 Document hierarchy

Use the following source hierarchy. When two sources disagree, do not silently choose one; record the conflict and request an authorized decision.

| Priority | Source | Role | Change rule |
|---|---|---|---|
| 1 | `v2/_build/facts.json` | Single structured register for fees, dates, contacts and operational facts | Edit the register, then regenerate dependent outputs |
| 1 | `v2/_build/claims.json` | Publication gate for contested institutional, accreditation, recognition and reach claims | An `open` claim is not approved copy |
| 1 | `v2/_build/privacy.json` | Child-image and identifying-content publication holds | No release without recorded approval and written consent |
| 1 | Current approved institutional policies / signed approvals | Authority for policy, legal status, recognition and institutional statements | Preserve exact wording and source |
| 2 | `docs/website-content-spec.md` | Detailed content, page order, copy, metadata, global elements and forms | Preserve original copy; propose edits separately |
| 2 | `data/export/AGI_Website_Content_Export.json` | Source content export, original text and source metadata | Retain provenance; do not treat legacy content as currently valid automatically |
| 2 | `data/export/work/content_pages.json`, `data/export/work/news.json` | Structured content working exports | Generated/working material; compare to approved sources |
| 2 | `v2/*.html`, `v2/journal/*.html` | Current rendered page content and implementation | Check against specification and registers |
| 3 | `docs/content-inventory.csv`, `docs/content-map.csv`, `docs/page-review.csv`, `docs/content-quality.csv`, `docs/privacy-review.csv` | Migration, review and QA evidence | Treat as review inputs, not policy authority |
| 3 | `docs/AI-ASSISTANT-BRIEF.md`, `v2/LAUNCH-CHECKLIST.md` | Open questions, assigned work and release blockers | Regenerate/update as source registers change |
| 4 | Old WordPress and Anglia Morocco sites, crawls and archived articles | Historical source evidence | Historical material must be dated, contextualized and revalidated |

**Conflict rule:** retain both source statements, add a row to the relevant conflict/approval register, mark affected content `HOLD`, and ask the responsible approver. Do not resolve a factual contradiction by copy-editing.

## 0.2 Content status vocabulary

Use these statuses consistently in the CMS, content agent and document:

- **APPROVED** — exact content has an identified authoritative source or named approver and may be published.
- **SOURCE / NOT YET APPROVED** — found in a source, but no current approval is recorded.
- **PROPOSED** — editorial rewrite or new organization suggested for review; not publishable until approved.
- **TO CONFIRM** — the fact, date, price, role or claim needs confirmation.
- **HOLD** — do not publish while a material conflict, legal check, consent or rights issue remains.
- **PLACEHOLDER** — missing image, quote, person, evidence or data; keep visibly marked.
- **OUTDATED / ARCHIVED** — preserve as historical material, but do not present as current.
- **RETIRED** — intentionally removed from navigation or current promotion; preserve archive/redirect treatment as appropriate.

Every page, section and important claim should carry a status, source, owner and last-reviewed date.

## 0.3 Required metadata record

Each content entity should expose (where applicable):

```yaml
content_id: stable machine-readable id
title: editorial title
slug: canonical slug
canonical_url: canonical URL
content_type: page | program | policy | form | article | faq | campaign | dataset
parent: parent content_id
audience: [parents, students, teachers, professionals, partners, current_families]
purpose: informational | trust | conversion | support | legal | editorial
primary_conversion: action id or null
secondary_conversions: []
language: en | fr | ar
source_refs: []
fact_refs: []
claim_refs: []
privacy_refs: []
owner: role or named owner
approver: role or named approver
status: controlled vocabulary above
last_reviewed: YYYY-MM-DD
next_review_due: YYYY-MM-DD
seo:
  title: ""
  description: ""
  keywords: []
media:
  assets: []
  consent_status: not_applicable | pending | approved | refused
  alt_text: ""
```

---

# 1. Brand identity, positioning and editorial guidelines

## 1.1 Institutional identity

**Organization name:** American Group International (AGI), Agadir.  
**Institutional context:** American-curriculum school and education provider in Agadir, Morocco, with K–12 schooling and additional programs for adults, English learners, educators, professionals and partner organizations. The organization also operates the Anglia Examinations Morocco franchise/representation described in the existing approved wording.

**Brand line:** Affordable · Creative · Inclusive  
**Motto:** School + Home + Community = Student Success  
**Mission line in the existing specification:** Global Minds with a Global Perspective

These lines are source copy in the existing website specification. Leadership should confirm which are formal brand assets and whether punctuation/capitalization must remain fixed.

## 1.2 Positioning

The website should communicate four consistent ideas:

1. **Accessible American-curriculum education in Agadir** — explain the offer and its actual eligibility, structure and fees without overclaiming legal or accreditation status.
2. **A personal and inclusive learning environment** — explain what the school does, how assessment and support work, and what families can expect.
3. **Learning across life stages** — distinguish K–12 school, adult high-school diploma, English/Anglia learning, teacher development, professional English, university pathways and wellbeing services.
4. **A Morocco-facing Anglia examinations network** — clearly separate the examination awarding/qualification framework, local delivery, classes, registration and centre partnership information.

## 1.3 Relationship between AGI, AGI programs and Anglia Morocco

Use this organizational model throughout the information architecture:

- **AGI School** is the K–12 American-curriculum school in Agadir.
- **AGI Programs** is the umbrella for additional education, tutoring, professional, teacher, adult-learning, pathway and wellbeing offers. Each offer must identify the delivering entity, eligibility, location/online status, actual credential (if any), fees and responsible contact.
- **Anglia Examinations Morocco** is a dedicated section within the AGI website, not a separate destination website. The specification says the former Anglia Morocco domain redirects into this section. Do not create links that send users to that former domain.
- **American Group USA LLC / AGI USA** is a related entity referenced in the repository. Its exact legal relationship, address, ownership and role in delivering services require confirmation before legal or financial claims are published.
- **External awarding bodies, partners and institutions** must be named precisely, with the relationship described accurately. A partnership, membership, franchise, course-provider relationship and accreditation are not interchangeable.

Do not use “AGI,” “AGI School,” “American Group International,” “American Group USA LLC,” “Anglia Examinations,” “Anglia Morocco” or “Chichester College Group” as interchangeable names.

## 1.4 Audiences and conversion priorities

| Audience | Core question | Key destinations | Primary conversion | Secondary conversion |
|---|---|---|---|---|
| Parents considering K–12 | Can my child learn here, be supported and fit the family budget? | Parents, K–12, Special Education, Admissions, Fees, Policies | Book a visit / Apply | WhatsApp, request information |
| Current families | How do I complete school administration? | Forms, Policies, Calendar, Contact | Submit relevant form | Call / WhatsApp |
| Children and adult English learners | Which level, class or exam is right for me? | Anglia, English & Anglia, Classes, Exams, Placement Test | Book level test / Register | Download practice, enquire |
| Teachers and teacher candidates | What is C.I.T.E., what does it qualify me for, and how do I apply? | Teachers, C.I.T.E., Careers, Sponsorship | Register / Enquire | Request details |
| Professionals and clinicians | Can the program improve workplace or clinical English? | Professional English, Medical English, Proctoring | Request level test / Team course | WhatsApp |
| Adult diploma learners | What is the route, eligibility, cost and credential? | Adult Diploma, Fees, Forms | Enquire / Apply | Request transcript or information |
| University applicants/families | What pathway support is provided and what is not guaranteed? | Pathways, Partnerships | Request consultation | Enquire |
| Prospective school/centre partners | What relationship is offered, what evidence exists and what are the requirements? | Investors, Partnerships, Anglia Network | Request partner brief | Submit partnership enquiry |
| Prospective tutors / learning-pod families | What is offered, who delivers it and how does scheduling work? | Online Tutoring, Learning Pods, Independent Studies | Request tutor / enquire | Schedule |
| Press/community | What has AGI done and what is verifiable? | About, Journal, Contact | Media enquiry | Share article |

**Conversion principle:** give each page one primary next action appropriate to its audience. Do not make every page push an application. Use a consistent CTA hierarchy: Apply / Book a visit / Book a level test / Register / Request information / Contact.

## 1.5 Voice and style

**Voice:** warm, direct, credible, inclusive, practical and respectful. Speak to the reader’s real decision. Avoid inflated claims and institutional jargon without explanation.

**English:** US English in the current specification: enrollment, behavior, center, program, grade, school year. Use consistent title case and numerals.

**Sentence style:** short paragraphs; descriptive headings; lists and tables where they improve scanning; explain acronyms at first use; use concrete verbs and clear calls to action.

**Do:**
- Explain what a learner will do, what support is available and what happens next.
- Distinguish requirements from recommendations.
- State the source and date for prices, calendars, credentials and recognition.
- Use respectful, person-first language and avoid deficit framing.
- Keep AGI policy/handbook language faithful to source; suggest rather than impose substantive rewrites.

**Do not:**
- Invent student outcomes, testimonial quotations, staff credentials, accreditations, recognition, university acceptance, pass rates, success rates, geographical reach or partnership terms.
- Use “guaranteed,” “internationally recognized,” “accredited,” “official,” “exclusive,” “first,” “best” or equivalent superlatives without specific evidence and approval.
- Present an external provider's credential as an AGI-issued credential.
- promise admission, grade placement, exam results, university entry or visa outcomes.

## 1.6 Institutional terminology

Maintain a shared glossary. Current source terminology includes:

| Preferred term | Usage note |
|---|---|
| American Group International (AGI) | First mention of institution |
| AGI School / K–12 school | Use only when referring specifically to the school |
| American curriculum / American-curriculum | Describe curriculum; do not imply US government operation |
| K–12 | Define as kindergarten through Grade 12 where needed |
| Special education / inclusive learning | Explain actual services and scope; do not imply clinical treatment unless substantiated |
| SEN | Expand as special educational needs at first use; use terminology approved by leadership |
| Adult high school diploma | Identify actual provider/awarding organization, transcript and eligibility |
| Anglia Examinations | Use official name |
| Anglia Examinations Morocco | Local franchise/network context |
| CEFR | Common European Framework of Reference for Languages |
| C.I.T.E. | Expand using the exact current official Anglia terminology approved by Anglia |
| Ofqual | Refer only in the precise approved relationship to AIM Qualifications and Assessment Group |
| UCAS tariff points | State only for Mastery (C2), according to project-approved wording |
| Learning pods | Define delivery model, supervision, location and responsibility |
| Proctoring | Clarify the exam provider and whether AGI is only the venue/proctor |

Add new terms through an approved glossary change, not ad hoc edits.

---

# 2. Website sitemap and content architecture

## 2.1 Page-count definition and branch snapshot

Repository inventory for `cms-test-smartsite` was checked on 16 November 2026. The HTML count reconciles to the “151 pages” total in the detailed specification:

| Inventory class | Files |
|---|---:|
| Primary-language pages in `v2/` (excluding journal article directory, build templates and legacy files) | 69 |
| Journal article pages in `v2/journal/` | 66 |
| French localized pages in `v2/fr/` | 4 |
| Arabic localized pages in `v2/ar/` | 12 |
| **Total HTML pages** | **151** |

This is a file count for the checked branch, not a claim that all page copy, translations, content approvals or functionality are launch-ready. The 69 primary pages include a 404 page and a preview/connect page.

## 2.2 Canonical content hierarchy

The following groups express the intended information architecture. Actual URL and implementation details must be reconciled with the page register in section 4 and the existing 151-page specification.

### A. Home and orientation
- Home — `index.html`
- For parents — `parents.html`
- Our story — `our-story.html`
- Founder’s letter — `founder-letter.html`
- About AGI — `about.html`
- Contact — `contact.html`

### B. School and student experience
- K–12 school — `k12.html`
- Special education — `special-education.html`
- Wellbeing hub — `wellbeing.html`
- ADHD coaching — `wellbeing-adhd-coaching.html`
- Play therapy — `wellbeing-play-therapy.html`
- Student life — `student-life.html`
- Resources — `resources.html`
- Nursery rhymes — `resources-nursery-rhymes.html`
- McGuffey resources — `resources-mcguffey.html`

### C. Admissions and family administration
- Admissions — `admissions.html`
- Fees — `fees.html`
- Academic calendar — `calendar.html`
- FAQ — `faq.html`
- Policies — `policies.html`
- Handbook — `handbook.html`
- Attendance — `attendance.html`
- Promotion and retention — `promotion-retention.html`
- Placement policy — `placement-policy.html`
- Parent responsibility — `parent-responsibility.html`
- Refunds and complaints — `refunds-complaints.html`
- Media policy — `media-policy.html`
- Homework — `homework.html`
- Volunteer hours — `volunteer-hours.html`
- Supplies — `supplies.html`
- Safeguarding — `safeguarding.html`
- Forms and requests — `forms.html`

### D. Programs and services
- Programs hub — `programs.html`
- Adult high-school diploma — `adult-diploma.html`
- University pathways — `pathways.html`
- Professional and medical English — `professional.html`
- Teachers — `teachers.html`
- C.I.T.E. — `teachers-cite.html`
- Teacher careers — `teachers-careers.html`
- Teacher USA sponsorship — `teachers-usa-sponsorship.html`
- Independent studies — `programs-independent-studies.html`
- Learning pods — `programs-learning-pods.html`
- Online tutoring — `online-tutoring.html`
- Document editing — `services-document-editing.html`
- Exam proctoring — `services-proctoring.html`
- Partnerships — `partnerships.html`
- Partners and investors — `investors.html`
- AGI USA — `agi-usa.html`
- AGI Connect preview — `connect.html`

### E. Anglia Morocco
- Anglia hub — `anglia.html`
- About Anglia — `anglia-about.html`
- Exams and levels — `anglia-exams.html`
- Examination dates — `anglia-exam-dates.html`
- Classes and prices — `anglia-classes.html`
- Practice — `anglia-practice.html`
- Step To books — `anglia-books.html`
- CEFR benchmarks — `anglia-cefr.html`
- Special arrangements — `anglia-special-arrangements.html`
- Placement test — `anglia-placement-test.html`
- Network and centres — `anglia-network.html`
- FAQ — `anglia-faq.html`
- English & Anglia overview — `english-anglia.html`

### F. Journal, legal and utility pages
- Journal index — `journal.html`
- Chichester College Group partnership feature — `journal-ccgi-partnership.html`
- 66 individual journal articles under `journal/`
- Privacy — `privacy.html`
- Terms — `terms.html`
- Cookies — `cookies.html`
- Accessibility — `accessibility.html`
- 404 — `404.html`

### G. Localized variants currently present
- French: `fr/index.html`, `fr/parents.html`, `fr/fees.html`, `fr/contact.html`
- Arabic: `ar/index.html`, `ar/about.html`, `ar/parents.html`, `ar/fees.html`, `ar/contact.html`, `ar/anglia.html`, `ar/anglia-classes.html`, `ar/anglia-practice.html`, `ar/professional.html`, `ar/promotion-retention.html`, `ar/special-education.html`, `ar/teachers-cite.html`

## 2.3 Global navigation requirements

The detailed specification defines a shared header, including:
- AGI brand/home link;
- About;
- Programs dropdown with the core program pathways;
- Admissions;
- Student life;
- Journal;
- Anglia Morocco;
- Contact;
- EN / FR / Arabic language switch;
- Forms utility link;
- Apply primary action;
- skip-to-content link and keyboard-accessible responsive navigation.

The final navigation labels, order and destinations should be approved against the final sitemap. Do not expose hidden preview or retired pages as primary navigation.

## 2.4 Footer requirements

Maintain a consistent footer containing:
- Short institutional description;
- School, programs and services navigation;
- Forms and parent resources;
- Contact details from the facts register;
- Current legal, safeguarding and accessibility links;
- Social and messaging links only where the official accounts and destinations are confirmed.

All phone, email and address strings must be sourced from `facts.json` or another approved contact record.

## 2.5 Relationship and cross-link rules

- Home → audience-specific path → detail page → conversion action.
- Parent landing page links to K–12, special education, admissions, fees, policies and visit/application forms.
- Every program has a clear link to its own enquiry/registration action and to the responsible provider.
- Anglia hub links to exams, levels, dates, classes, practice, books, special arrangements, test, network and FAQ.
- Anglia pages can cross-link to relevant AGI English classes, teacher training or centre partnerships, but must make the offering/provider boundary clear.
- Policies link to relevant admissions forms only where appropriate.
- Journal articles link to current pages for current fees/dates; archived articles must not act as current operational instructions.
- Do not create a navigation loop between AGI and the old Anglia domain.

---

# 3. Global content elements and reusable components

## 3.1 Reusable content entities

| Entity/component | Required fields | Governance |
|---|---|---|
| CTA | Label, destination, action type, audience, tracking label | Use approved action names; never misleading button text |
| Program card | Name, age/audience, short description, provider, location/delivery, CTA | Each card links to a full program record |
| Statistic | Value, label, period, source, last verified | No source = do not publish |
| Testimonial | Exact quote, speaker label, context, consent file, approval date, channels | No sample testimonial on production |
| Staff profile | Name, role, short biography, qualifications, photo, consent | Current role and portrait approval required |
| Accreditation/recognition badge | Issuer, legal entity recognized, scope, validity, evidence, approved logo | Never display a badge without evidence and usage rights |
| Partner logo | Organization, relationship description, permission, asset source | Confirm logo permission and relationship |
| FAQ item | Question, approved answer, owner, fact references, language | Answers must match current registers |
| Price card | Program, amount, currency, billing unit, inclusions, effective date, expiry/review date | Dataset-driven; never hardcode on many pages |
| Date/event | Event name, start/end, target group, location, status, source | Use timezone/date rules and expire after event |
| Media asset | File, subject, caption, alt, rights, consent, location, publish scope | Child data under strict privacy hold |
| Form | Form ID, purpose, fields, consent, processor, delivery, retention, owner | Privacy/legal review before collection |
| Trust block | Claim, evidence, issuer, scope and date | Must point to claims/evidence register |

## 3.2 Global CTA library

Use standard intent-based labels:
- Apply
- Book a visit
- Request information
- Contact AGI
- WhatsApp AGI
- Book a free level test
- Register for an examination
- Explore examination levels
- View classes and prices
- Download practice resources
- Request a tutor
- Request a document
- Send an absence notice
- Give consent
- Submit an enquiry
- Request the partnership brief

Avoid generic “Click here,” “Learn more” where a more specific label can be used, and CTAs whose destination does not match their wording.

## 3.3 Header, footer and global messaging

The existing specification contains detailed header, footer, WhatsApp, homepage popup, map and breadcrumb rules. Preserve them as implementation requirements and maintain their exact current wording in `docs/website-content-spec.md` until approved changes are made.

**Special handling:** the parent popup copy includes the 46+ nationalities claim, which is still recorded as needing confirmation due to the earlier 45+ source. The popup must not publish that statement as settled until the conflict is closed.

---

# 4. Page-by-page content specification and page register

## 4.1 Canonical page brief template

Every page must have a detailed record with the following fields:

1. **Identity:** page name, stable ID, URL, parent, category, canonical status.
2. **Purpose:** user problem, business role, intended outcome.
3. **Audience:** primary and secondary.
4. **Journey:** entry sources, next expected step, related pages.
5. **SEO:** title, meta description, slug, canonical, indexation, social metadata, primary topic.
6. **Hero:** eyebrow, H1, introduction, primary CTA, secondary CTA, media brief and alt text.
7. **Section sequence:** ordered section list with section ID, purpose and complete copy.
8. **Components:** cards, tables, stats, FAQs, testimonials, badges, accordions, downloads.
9. **Conversion:** form/WhatsApp/call/book/register CTA; exact target; fallback.
10. **Media:** photo/illustration/diagram/audio/video requirements, caption, rights and consent.
11. **Trust/evidence:** claims, accreditation, policy or credential references.
12. **Internal links:** incoming/outgoing links and anchor intent.
13. **Localization:** EN source, FR/AR availability, translation status, RTL checks.
14. **Status:** approved/source/proposed/to-confirm/hold/placeholder/outdated.
15. **Ownership:** content owner, fact owner, approver, review date.
16. **Implementation:** CMS type, fields, reusable blocks, structured data and redirect.

## 4.2 Page register

This register is a repository inventory and editorial planning baseline, not a substitute for the complete copy in `docs/website-content-spec.md`. All rows inherit status **SOURCE / NEEDS PAGE-LEVEL APPROVAL** until the detailed record explicitly records approval.

| Page / route | Audience | Page purpose | Primary goal | Key governance note |
|---|---|---|---|---|
| Home — `index.html` | All; parents priority | Orient visitors and communicate the full offer | Book visit / Apply | Claims, statistics, fees, dates, testimonials and hero images require evidence/approval |
| Parents — `parents.html` | Parents | Parent-first decision page | Book a visit / Apply | Testimonial and family-story proof must be real and consented |
| Our story — `our-story.html` | Parents, partners, community | Institutional history | Build trust / Visit | Timeline and founder quotes need approval |
| Founder letter — `founder-letter.html` | Parents | Personal leadership message | Visit / Enquire | Draft exists; founder approval outstanding |
| About — `about.html` | All | Explain AGI identity and model | Enquire | Legal status, titles, recognition and reach claims are gated |
| AGI USA — `agi-usa.html` | Partners, adult learners | Explain related US entity and services | Enquire | Legal relationship/address and service scope require confirmation |
| Investors — `investors.html` | Prospective partners/investors | Explain partnership and investment pathways | Request partner brief | No financial/return claims without documentary proof |
| K–12 — `k12.html` | Parents | Explain school model and curriculum | Book visit / Apply | Curriculum, state recognition and delivery provider need evidence |
| Special education — `special-education.html` | Parents | Explain inclusive support and services | Enquire / Visit | Clinical service boundaries, consent and 2024 parent letter privacy hold |
| Student life — `student-life.html` | Families and students | Show the learning experience | Visit | Photos require consent; dates must be current |
| Resources — `resources.html` | Students, families, teachers | Provide learning resources | Use resource / Enquire | Third-party copyright and broken source content review |
| Nursery rhymes — `resources-nursery-rhymes.html` | Families, young learners | Early learning resources | Use resources | Copyright/license review |
| McGuffey — `resources-mcguffey.html` | Students, teachers | Reading/spelling resource library | Use resource | Public-domain/source attribution and imported text QA |
| Admissions — `admissions.html` | Prospective families | Explain application path | Apply | Requirements, dates and form behavior |
| Fees — `fees.html` | Parents and learners | Transparent current pricing | Apply / Enquire | All amounts from facts register; effective dates required |
| Calendar — `calendar.html` | Families and students | Current term/school dates | Plan / Contact | 2026–27 material must be reconciled with source dates |
| FAQ — `faq.html` | All | Answer recurring questions | Continue journey | Every answer has owner and fact source |
| Policies — `policies.html` | Families | Policy index | Read policy / Contact | No policy paraphrase may change meaning |
| Handbook — `handbook.html` | Current families | Full school guidance | Read / Contact | 7,118-word page flagged; privacy and policy integrity review |
| Attendance — `attendance.html` | Families | Explain attendance policy | Send absence notice | Policy owner approval |
| Promotion/retention — `promotion-retention.html` | Families | Explain progression rules | Enquire | Grade placement promise must remain exact |
| Placement policy — `placement-policy.html` | Parents | Explain placement/assessment | Book assessment | Exact quote and requirements must be preserved |
| Parent responsibility — `parent-responsibility.html` | Parents | Clarify parent obligations | Acknowledge / Contact | Policy/legal review |
| Refunds/complaints — `refunds-complaints.html` | Families | Explain process | Submit complaint | Current process, timelines and recipient confirmation |
| Media policy — `media-policy.html` | Families | Explain image/media permissions | Consent | Law 09-08 and minor-image process review |
| Homework — `homework.html` | Families/students | Explain homework expectations | Read policy | Conflict with “limited homework” messaging open |
| Volunteer hours — `volunteer-hours.html` | Families/students | Explain service hours | Contact / Submit | Requirement confirmation |
| Supplies — `supplies.html` | Families | Current supply list | Prepare for school | Academic-year review |
| Safeguarding — `safeguarding.html` | Families/staff | Publish safeguarding contact and process | Contact safeguarding lead | Named officer/process must be confirmed; sensitive legal review |
| Forms — `forms.html` | Current/prospective families, learners | Centralize requests | Submit correct form | Data protection, backend, retention and form routing are launch blockers |
| Programs — `programs.html` | All program audiences | Programs index | Select program | Provider and service boundaries must be clear |
| Adult diploma — `adult-diploma.html` | Adult learners | Explain diploma route | Enquire / Apply | Exact awarding provider, recognition, cost and eligibility |
| Pathways — `pathways.html` | Students/families | Explain higher education support | Request consultation | Partner status and university claims need current verification |
| Professional — `professional.html` | Professionals/clinicians | Explain professional/medical English | Book level test / Request team course | Medical claims and prices require review |
| Teachers — `teachers.html` | Teachers | Overview of professional development | Enquire / Register | Offer and provider relationship |
| C.I.T.E. — `teachers-cite.html` | Teachers | Detail certificate, exam and requirements | Register / Enquire | Official qualification wording and approval from Anglia |
| Teacher careers — `teachers-careers.html` | Prospective teachers | Explain current roles | Apply / Enquire | Do not imply current vacancies without confirmation |
| USA sponsorship — `teachers-usa-sponsorship.html` | Teachers | Explain sponsorship offer | Request details | Cost, eligibility, immigration/legal wording |
| Independent studies — `programs-independent-studies.html` | Learners/families | Explain course-study model | Enquire | Pricing and provider confirmation |
| Learning pods — `programs-learning-pods.html` | Parents, tutors | Explain pod model | Enquire | Delivery, supervision, safeguarding and partner model |
| Online tutoring — `online-tutoring.html` | Learners/families | Match tutors and learners | Request tutor | Rates, tutor vetting, scheduling and response-time claims |
| Document editing — `services-document-editing.html` | Learners/professionals | Explain editing service | Request service | Scope, confidentiality and prices |
| Proctoring — `services-proctoring.html` | Exam candidates/institutions | Explain invigilation service | Request booking | Exam-provider rules and rates |
| Wellbeing — `wellbeing.html` | Families/women/families | Explain wellbeing offer | Enquire | Entity/provider and professional scope |
| ADHD coaching — `wellbeing-adhd-coaching.html` | Families/individuals | Explain coaching offer | Enquire | No medical diagnosis/treatment claims without evidence |
| Play therapy — `wellbeing-play-therapy.html` | Families | Explain service | Enquire | Qualification, supervision, safeguarding and price approval |
| Anglia hub — `anglia.html` | Learners, parents, teachers, centres | Anglia Morocco entry point | Book test / Register | Approved relationship wording, brand and scope |
| Anglia about — `anglia-about.html` | All Anglia audiences | Explain examination organization | Enquire | History and corporate claims require partner confirmation |
| Anglia exams — `anglia-exams.html` | Candidates, teachers | Explain levels and qualification ladder | Register | Current exam structure and awarding-body details |
| Exam dates — `anglia-exam-dates.html` | Candidates/centres | Publish current sessions | Register | 2026 dates need rollover; never leave expired dates as current |
| Anglia classes — `anglia-classes.html` | Learners/parents | Explain local classes and pricing | Enquire / Register | Old rates effective Nov 2024 need reapproval |
| Practice — `anglia-practice.html` | Candidates | Practice materials | Use/download | Copyright, access rights and file integrity |
| Books — `anglia-books.html` | Learners/centres | Step To range and ordering | Order books | Catalogue, stock, audio rights and pricing |
| CEFR — `anglia-cefr.html` | Candidates/teachers | Explain CEFR mapping | Choose level | Mapping claim evidence and privacy check |
| Special arrangements — `anglia-special-arrangements.html` | Candidates/parents | Explain adjustments process | Request arrangement | Official policy and deadlines |
| Placement test — `anglia-placement-test.html` | Learners | Help select entry level | Take test / Book test | Test intellectual property and data policy |
| Network — `anglia-network.html` | Centres/partners | Explain regional centre network | Become a centre | Current 12 regions and open representatives must be verified |
| Anglia FAQ — `anglia-faq.html` | Candidates/parents/centres | Candidate support | Enquire / Register | Must follow approved Anglia facts |
| English & Anglia — `english-anglia.html` | English learners | Explain learning and certification | Book level test | Remove “exclusive” claim; use controlled corporate wording |
| Partnerships — `partnerships.html` | Teachers/centres/organizations | Explain cooperation options | Submit enquiry | Partner terms, screening questions and privacy |
| Journal — `journal.html` | Community and search visitors | Editorial archive | Read / Enquire | 66 posts; dates, photo consent, archive notices and links |
| CCGi partnership feature — `journal-ccgi-partnership.html` | Community/partners | Preserve partnership announcement | Read | Wording and historical context review |
| Contact — `contact.html` | All | Contact routes and location | Call / WhatsApp / Enquire | Contact data must come from facts register |
| Privacy — `privacy.html` | All | Explain data processing | Understand rights | Must match actual forms, analytics, map, fonts, hosting and processors |
| Terms — `terms.html` | All | Terms of website/services | Understand terms | Legal review |
| Cookies — `cookies.html` | All | Cookies/consent disclosure | Manage preference | Must match real implementation |
| Accessibility — `accessibility.html` | All | Explain accessibility support | Report issue | Test actual site and contact method |
| Connect preview — `connect.html` | Internal/selected users | Preview future service | None or gated | Must remain clearly labeled preview/no public promises |
| 404 — `404.html` | All | Recover from broken URL | Navigate | Noindex and working links |

The 66 journal article routes are individually inventoried in `docs/website-content-spec.md` Appendix B and physically present in `v2/journal/`. Their individual titles, slugs and original copy should be pulled from the article export rather than manually duplicated here.

## 4.3 Required full-copy location

For each page, the complete copy—including eyebrow, H1, introduction, every section in reading order, CTA labels/targets, cards, tables, FAQs and image prompts—remains in the page-by-page specification:

`docs/website-content-spec.md` — Sections 4 and 5.

That specification is 617 KB and includes 151-page scope, forms and journal index information. It must remain preserved as the detailed copy layer. Any editorial rewrite should be delivered as a proposed delta referencing the exact page/section, not as an untraceable replacement.

---

# 5. Programs and academic content library

Every program needs a structured product/content record with: name; audience; age/grade eligibility; objectives; learning outcomes; curriculum/content; duration; delivery mode; location; class size; schedule; prerequisites; assessment; certificate/credential; actual issuer; teacher/tutor qualifications; accessibility/support; price; inclusions/exclusions; cancellation/refund terms; contact; source; status; last-verified date.

## 5.1 K–12 American school

**Core story:** American-curriculum learning from Kindergarten through Grade 12 in Agadir.

The K–12 page family should clearly answer:
- Who may apply and the age rule;
- Which grades and pathways are currently delivered;
- Curriculum, subjects and how grade-level expectations are assessed;
- English-language support and Anglia-related benchmarking, carefully distinguishing language assessment from academic grade placement;
- Multi-grade classroom model, class-size information and teaching approach (only if current);
- Student support, inclusion and safeguarding;
- Academic calendar, attendance and promotion/retention;
- What is included in fees and what is not;
- Documents and enrollment process;
- Whether records are issued by AGI, a correspondence provider or another partner.

**Do not infer accreditation from curriculum style.** State the exact legal/educational provider for each pathway.

## 5.2 Special education and inclusive learning

The program family must describe only services that AGI can currently deliver and staff appropriately.

Required content:
- Learner needs the service is designed to support;
- Referral and intake process;
- Assessment and individualized planning;
- Family participation and review cadence;
- Classroom accommodations and small-group support;
- Services delivered by AGI versus external professionals;
- Qualifications, supervision and scope of each practitioner;
- Safeguarding and privacy arrangements;
- Fees and availability;
- Clear statement that website information is not a diagnosis or substitute for clinical advice.

**Hold:** the repository contains a 2024 parent letter that names a child and is hidden. Do not republish without explicit, documented consent and privacy review.

## 5.3 Admissions and enrollment

Content must cover:
- Eligibility and age calculation;
- Available grades/seats and admission windows;
- School visit;
- Placement and assessment;
- Required records/documents;
- Treatment of missing documents and language gaps;
- Enrollment steps and payment instructions;
- Start date and calendar;
- Contact and response expectation.

The exact placement statement from the existing policy must be preserved:

> “Grade placement is not lowered due to missing documents, language gaps, or academic gaps.”

## 5.4 Tuition, fees and payment

All pricing must be read from `v2/_build/facts.json`, with a visible effective date and an owner/review date. The current register contains source values, not a blanket confirmation that all prices remain current.

Source-listed items include:
- K–12 monthly tuition: 2,600 MAD × 10 months;
- Annual inscription bands from 6,500 MAD to 11,000 MAD;
- American High School Online price source: US$2,500 per year;
- Summer school price source: 3,000 MAD for one month;
- Anglia Saturday classes source: 500 MAD/month;
- Anglia one-to-one source: 200 MAD/session;
- Anglia small group source: 150 MAD/person/session;
- Anglia group-course source: 1,200 MAD for 12 weeks;
- Proctoring source: 200 MAD administration + 200 MAD per exam hour (also shown in EUR in the source);
- Teacher sponsorship source: US$60;
- Other prices marked `to-confirm`, including online tutoring, independent modules and play therapy.

**Publication rule:** do not call a price current unless an owner has reconfirmed it. Never accept card data in site forms; the detailed spec directs card payments to the existing secure payment page.

## 5.5 Academic policies and resources

Each policy page needs:
- Policy title and policy owner;
- Effective date/version;
- Who it applies to;
- Rule in full;
- Exceptions/appeal route;
- Related form/contact;
- Approval record.

The current source facts include 90% attendance, 64% pass mark, 40 service hours (10 per year), 90-day adjustment period and tardy/absence timing rules. These are source-listed policy facts and must remain tied to the current approved policy version.

Academic resource pages must include:
- Resource title and intended level;
- Learning objective;
- Download/stream/access method;
- Publisher/author and copyright license;
- File format and last checked date;
- Whether it is an AGI original or third-party material.

## 5.6 Adult high-school diploma

Must clearly differentiate:
- AGI’s local advising/administrative role;
- American Worldwide Academy or other actual provider;
- Awarding body and transcript issuer;
- Credits and course requirements;
- Assessment/proctoring;
- Eligibility and minimum age;
- Completion pace;
- Recognition/acceptance caveat;
- Full fee and refund details.

Do not state that AGI awards the diploma unless evidence confirms that role.

## 5.7 English learning and Anglia examinations

Keep separate content records for:
- General English classes;
- Anglia exam preparation;
- Anglia examination registration;
- Examination delivery/centre arrangements;
- Level test / placement test;
- Practice resources;
- Books and audio;
- Corporate/business English;
- Medical English.

Every offer should clearly identify whether the learner is buying tuition, examination entry, books, a test, or a bundle.

## 5.8 C.I.T.E. teacher training

Confirm the current official full name, provider, qualification type, level, exam format, entry requirements, duration, validity, assessment and recognition. Avoid describing a certificate as a degree or teaching license unless the awarding body confirms this exact status.

## 5.9 Professional and medical English

Describe intended learners, course format, placement, objectives, schedule, group size, learning outcomes and fees. Medical-English language training must not be described as a medical qualification or clinical authorization.

## 5.10 University pathways

List only active partnerships/agency agreements and their exact scope. Distinguish:
- university admissions agency;
- referral/consultancy;
- articulation/pathway agreement;
- course provider;
- scholarship provider.

Never guarantee admission, credit transfer, visa issuance or employment.

## 5.11 Wellbeing and i-Heart

Define the legal provider/entity, actual service, practitioner qualifications, age group, setting and safeguarding. Separate coaching, education support, therapeutic services and regulated clinical services. Any mental-health or medical claims require professional and legal review.

## 5.12 Online tutoring

Record subjects, age groups, tutor screening, safeguarding, online platform, session durations, rates, cancellations, scheduling and response commitments. Do not publish “within 48 hours” as a service promise until operationally confirmed.

## 5.13 Learning pods and independent studies

Explain how the pod is formed, who supervises, whether it is a school enrollment or supplemental service, who is responsible for curriculum/assessment, maximum group size, learning location and parent role.

## 5.14 Partnerships and international opportunities

Describe the specific route, legal parties, eligibility, fees, responsibilities, geography, agreement status and supporting evidence. Historic announcements should be labeled as historic unless the relationship remains active.

---

# 6. Anglia Morocco content library

This section is a dedicated editorial domain. Anglia claims and logo use must follow partner approval. AGI copy must not imply ownership of Anglia Examinations or award authority beyond the documented role.

## 6.1 Approved relationship wording

The project rules require the wording:

> “official partner in Morocco of Chichester College Group, UK”

The project rules also specify that the four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual, and that the **Mastery (C2)** qualification carries UCAS tariff points.

These statements should be published only with the evidence and approval reflected in the current project registers. Do not say:
- Anglia depends on the UK Ministry of Education;
- Anglia is recognized by the British Council;
- Anglia has QCA accreditation;
- Anglia Mastery is the Proficiency examination;
- AGI is the exclusive franchise holder.

The `claims.json` register is the publication gate for claims still open.

## 6.2 History and organization

The repository’s source register lists Anglia as based in Chichester since 1993 and AGI’s Anglia franchise relationship since 2021. Treat these as source facts pending current written confirmation by Anglia, as requested in `docs/email-anglia-approval.md`.

The Anglia history page should:
- Provide a short chronology;
- Name the relevant organization accurately;
- Explain the Morocco relationship;
- Distinguish examination owner, awarding organization, local partner and local centre;
- Provide current official source links;
- Avoid unsupported regulatory/ministry claims.

## 6.3 Levels and qualification framework

The current site content describes a ten-level progression from First Step through Masters (C2), and a Business English pathway. The exact approved names, sequence, CEFR correspondence, assessment format and award issuer must be checked against the current official Anglia handbook before being treated as authoritative.

Required level record:
- Official level name and code;
- Learner profile / intended age;
- CEFR mapping and evidence;
- Skills assessed;
- Exam components and duration;
- Progression route;
- Certificate/qualification issued;
- Awarding organization;
- Current practice material;
- Current exam fee and entry date.

## 6.4 CEFR mapping

Use the full name “Common European Framework of Reference for Languages (CEFR)” on first mention. For every mapping, provide the Anglia level, mapped CEFR level, evidence/source, scope and caveat. Do not claim equivalence to a national school qualification unless formally documented.

## 6.5 Examination dates and registration

The repository contains a 2026 dates source and a separate 2025–26 Saturday classes schedule. These are not automatically valid for the 2026–27 cycle.

Every exam-session dataset must include:
- Exam date and local time;
- Level(s);
- Registration opening and closing dates;
- Centre/location;
- Mode (paper/online, only when currently available);
- Fee and payment instructions;
- Required candidate documents;
- Special-arrangements deadline;
- Contact and cancellation/change rules;
- Status: draft / confirmed / registration open / full / closed / completed.

Automatically mark completed sessions as historical. Never show expired exam dates as upcoming.

## 6.6 Special arrangements

Explain:
- Who may request arrangements;
- Which arrangements are available under Anglia rules;
- Required supporting documentation;
- Submission deadline;
- Decision-maker;
- Confidentiality;
- Candidate appeal/contact route.

Do not promise an arrangement before the examination authority confirms it.

## 6.7 Practice resources and audio

Organize by category, level and skill. Each resource must include source rights, correct audio pairing, file size/format, intended use and last test date. Do not rehost third-party tests/audio unless permission or license allows it.

## 6.8 Step To books

The catalogue must include:
- Official title and level;
- Edition/year;
- Student/teacher version;
- ISBN (if applicable);
- Audio resource and access rights;
- Stock status;
- Price and currency;
- Ordering process;
- Delivery/collection options.

The order form should not imply a confirmed order until stock, price and delivery are approved.

## 6.9 Placement tests

Identify the owner/licensor of each test. The repository explicitly excludes an old Pearson Total English placement test because of copyright concerns. Do not restore it without a valid license. Explain what the placement result can and cannot determine.

## 6.10 English classes and pricing

Keep the classes page distinct from exam registration. Record ages, schedule, level, teacher, group size, duration, location, course fee, examination inclusion, books and effective date. Source-listed rates from 2024 must be reconfirmed.

## 6.11 Centres and regional network

The source material mentions 12 regions and a list of open representatives. The current list of operational regions, centre names, local contacts and recruitment status requires confirmation. Each centre record needs written appointment/authorization, address, service scope, contact and current status.

Do not reproduce geographic/political wording flagged in the original network page. The project rules direct the site to list regions and provinces without the contentious text.

## 6.12 Anglia FAQ

FAQ answers should be derived from official Anglia rules and current local operating procedures. Each answer requires source, version date and approval. Never use an old Anglia Morocco page as sole authority for current examination rules.

---

# 7. Journal, news, resources and archives

## 7.1 Journal model

The detailed specification and repository include 66 journal articles. Keep each article as an individual content record with:
- Title and slug;
- Original publication date;
- Last updated date (separate from original date);
- Author/source;
- Category;
- Full source text;
- Edited summary (if any);
- Original media and rights;
- Consent status;
- Related program/page;
- Current/historical label;
- SEO title/description;
- Redirect from old URL.

## 7.2 Historical accuracy

Preserve the original article date and do not rewrite old announcements as current facts. Where editorial corrections are needed, add an editorial note rather than changing the historical meaning.

## 7.3 Archive warning

The project rule says journal posts older than 12 months should display a clear notice that fees, dates and programs may have changed, and direct readers to current fees/calendar pages. Apply this rule consistently.

## 7.4 Privacy holds

The repository’s privacy register lists 36 journal pages whose photos remain hidden until parental consent has been confirmed. It also flags a 2024 parent letter naming a child. The current approved list is empty in the checked register. Do not reveal or infer consent from the fact that an image was historically published.

## 7.5 Journal editorial QA

The editorial review identifies long paragraphs, duplicated text, old WordPress shortcodes, raw links, hashtags, generic link text and formatting issues. Fix presentation without altering factual meaning. Keep original source text available where the project specification requires a “Full text as published by AGI” disclosure.

---

# 8. Forms, FAQs and conversion content

## 8.1 Form inventory

The page specification describes 11 forms. The page-level source should remain the detailed form specification, including introductions, prerequisites, expected response, field types, required flags and submit labels.

The current form families include:
- Enrollment/application;
- Visit/appointment;
- Absence notice;
- Activity/park consent;
- Parent feedback;
- Payment notice;
- Step To book order;
- Tutor request;
- Tutoring schedule;
- Document request;
- General enquiry.

Confirm the final 11-form list and route IDs against Section 5 of `docs/website-content-spec.md` before CMS migration.

## 8.2 Form content requirements

Every form must state:
- Purpose;
- Who should use it;
- Time required;
- Information to prepare;
- Which fields are mandatory;
- Why personal information is collected;
- What happens after submission;
- Expected response time (only when service owner confirms);
- Contact route if the form fails;
- Data controller/processor information and privacy notice;
- Retention and deletion rules.

## 8.3 Sensitive data and payment controls

- Do not collect card numbers, security codes or full card credentials.
- Do not request unnecessary health, disability or child information.
- Limit access to family and learner submissions.
- Define where data is stored, who processes it, retention, access controls and deletion before launch.
- Forms that collect children's or family information require privacy/legal review.
- The repository’s SmartSite skill notes that form submissions contain family data and that storage location must be decided before launch.

## 8.4 FAQ content governance

FAQ entries should be reusable structured content with category, question, answer, audience, language, fact refs, approver and review date. Avoid duplicating answers on many pages; link to the authoritative page or dataset.

## 8.5 Conversion measurement

If analytics/measurement is introduced, disclose it in the privacy policy and cookie controls. The existing spec states that the site itself uses no cookies or tracking, but actual third-party map/font/analytics implementation must be audited before repeating that claim.

---

# 9. SEO and structured content metadata

## 9.1 Per-page SEO requirements

The detailed spec sets:
- Unique browser title, ideally no more than 65 characters;
- Meta description between 70 and 160 characters;
- Canonical URL;
- Open Graph and Twitter metadata;
- Sitemap and robots directives;
- Correct index/noindex treatment;
- Internal links and redirect preservation.

These are implementation targets to test, not a promise that every current page already satisfies them.

## 9.2 Structured data

The original specification proposes School structured data for the home page. Implement only properties that are factually supported and consistent with Google’s current structured-data guidance. Do not add ratings, reviews, accreditation, price or location attributes without evidence.

Potential types should be chosen per entity and content type, not applied indiscriminately:
- School / EducationalOrganization for verified institution details;
- Organization for AGI and separately for related legal entities if needed;
- Course for real courses with current details;
- Event for actual exam sessions/events;
- Article for journal articles;
- FAQPage only when its eligibility and implementation rules are satisfied;
- BreadcrumbList for page hierarchy.

Recheck current schema.org and search-engine guidance before deployment.

## 9.3 Keyword strategy

Assign one main search intent per page. Avoid keyword stuffing. Use natural local context (Agadir, Morocco) where it accurately describes the service. Keep Anglia brand queries distinct from general English-class queries.

## 9.4 Redirect and canonical governance

The repository has:
- AGI legacy URL redirect mapping in `v2/_build/redirects.csv`;
- Anglia Morocco redirect mapping in `docs/angliamorocco-redirects.csv` / `.htaccess`.

Keep 301 redirects, check destination relevance, avoid chains and loops, preserve old journal article history, and validate canonical tags against actual routes.

---

# 10. Multilingual content: EN / FR / AR

## 10.1 Language model

English is the current source language in the specification. French and Arabic are partial localized page sets. Do not imply the whole site is fully translated until the page inventory shows it.

## 10.2 Translation workflow

1. Freeze approved English source copy.
2. Identify language-specific terms, legal references and institutional names.
3. Translate by qualified human translator.
4. Review with AGI subject-matter owner.
5. Review Arabic by a fluent Arabic editor with educational terminology knowledge.
6. QA the page visually and functionally.
7. Record translation status, source revision and approval.

## 10.3 Arabic RTL requirements

- Use `lang="ar"` and `dir="rtl"` on the content root.
- Ensure header, navigation, footer, breadcrumbs, form labels, validation, tables, dropdowns, pagination and modal flows work right-to-left.
- Avoid embedding copy into images.
- Check mixed-script strings, phone numbers, dates and Latin accreditation names.
- Use Arabic numerals or Western numerals consistently according to the chosen language style.
- Use the Arabic font specified in the current project design system only after confirming font availability/licensing.
- Do not use italics for Arabic as specified in the project skill.
- Ensure form fields maintain correct text direction based on content type (email/phone can be LTR).
- Test at narrow mobile widths and keyboard/screen-reader navigation.

## 10.4 Current localization inventory

Current checked branch includes 4 French HTML pages and 12 Arabic HTML pages. This count should be recalculated automatically after every route addition. The target language coverage, not only the page count, needs leadership approval.

---

# 11. Facts, claims, source references and approvals

## 11.1 Facts register

`v2/_build/facts.json` is explicitly identified by the AGI website skill as the only place where a fee, date or contact should be changed. It contains contact, school, fees, Anglia, calendars and people sections.

**Important distinction:** the register uses statuses such as `confirmed`, `source` and `to-confirm`. A `source` value is evidence that a source says something; it is not necessarily current approval. Publication workflows must preserve that distinction.

## 11.2 Known claim decisions

The current `v2/_build/claims.json` contains 13 claim records. The following issues are explicitly open or controlled:

1. Anglia relationship to UK Ministry of Education, British Council, QCA and ASCENTIS — do not publish pending written confirmation.
2. Proficiency versus Mastery UCAS wording — replace with approved Mastery (C2) wording.
3. 45+ versus 46+ nationalities — leadership confirmation required.
4. “Private correspondence school” legal description — confirm with leadership.
5. Founder/CEO/Country Manager/Director titles — confirm current role.
6. Current team list and roles — confirm; a former staff name has been marked for removal.
7. Current official/admin/Anglia email purposes — confirm.
8. Anglia Saturday class schedule — 2026–27 schedule required.
9. Homework messaging versus policy minutes — leadership decision.
10. American Group USA LLC address — confirm.
11. Western Sahara political text in network content — do not reproduce; use regions/provinces only.
12. Old prices — reconfirm.
13. “CSALC” in the old home-page legal name — confirm whether part of legal name.

Never resolve an open item by deleting it from copy alone. Close the claim register with a decision, source and approver.

## 11.3 Source/approval record

Each significant claim should have:
- Claim ID;
- Exact claim;
- Page/section locations;
- Source URL or internal file reference;
- Issuer/authority;
- Evidence document;
- Scope and legal entity;
- Validity/effective date;
- Approver and approval date;
- Expiry/review date;
- Publication status.

## 11.4 Accreditation and recognition language

The source spec includes several claimed accreditations, recognitions, memberships, NCAA/NAIA/College Board compliance and partner relationships. Do not group these under a single vague heading such as “Accredited by.” Each must be separately documented with:
- The entity receiving the recognition;
- The issuing authority;
- What exactly is recognized/accredited;
- The level/program/scope;
- Whether it is current;
- Whether logo/name use is permitted.

---

# 12. Editorial operations, ownership and launch readiness

## 12.1 Roles

The following are proposed governance roles; names must be assigned by AGI leadership:

| Role | Responsibility |
|---|---|
| Institutional approver | Final approval of positioning, leadership bio, institutional history and public claims |
| Academic owner | Curriculum, placement, policies, student support and safeguarding |
| Admissions/fees owner | Enrollment, dates, tuition and fees |
| Anglia liaison | Anglia corporate wording, levels, exams, arrangements, centres and logo approval |
| Privacy/legal reviewer | Forms, minors' data, image consent, terms, privacy and retention |
| Editorial owner | Copy quality, terminology, style, page register and change log |
| Translation reviewers | FR and AR accuracy, terminology and RTL quality |
| CMS/content engineer | Structured fields, previews, links, forms and publication controls |
| SEO/QA owner | Metadata, schema, redirects, indexing, links and release checks |

## 12.2 Editorial change workflow

1. Identify the page/component/data record and its owner.
2. Record current published text and source.
3. Make a proposed edit separately from approved text.
4. Check fact, claim, privacy, copyright and language implications.
5. Obtain the required approval.
6. Update the authoritative register first for facts/prices/dates/contacts.
7. Regenerate dependent pages/exports.
8. Run content/fact/privacy/link/build checks.
9. Preview all affected languages and responsive variants.
10. Publish with change-log entry and review date.
11. Verify live page and redirects.
12. Retain approval evidence.

## 12.3 Content cadence

| Content type | Review trigger |
|---|---|
| Tuition and fees | Before each enrollment cycle and whenever pricing changes |
| School calendar | Each academic year and on any date change |
| Anglia exam dates | Each published session; expire completed dates |
| Anglia schedule/classes | Each course cycle |
| Staff/leadership | When roles or employment change; at least annually |
| Accreditation/recognition/partnership | On renewal/change and at least annually |
| Policies | On policy revision and before each academic year |
| Contact details | Quarterly and when details change |
| FAQ | Quarterly and whenever a referenced fact changes |
| Journal | Before publication and at annual archive review |
| Translations | Whenever approved source changes |
| Legal/privacy/cookies | On processing/vendor changes and at least annually |

## 12.4 Existing repository review findings

The checked source repository provides useful review evidence:
- `docs/editorial-review.md` identifies text-quality issues including long paragraphs, duplicate paragraphs, raw URLs, WordPress shortcodes, generic “click here” links, hashtags and malformed lists.
- `docs/page-review.csv` flags outdated dates, open claims, empty headings, overlapping copy and very long pages.
- `docs/content-quality.csv` is a machine-generated issue list.
- `docs/privacy-review.csv` flags possible identifying names requiring review.
- `v2/LAUNCH-CHECKLIST.md` states there are 107 open items.
- `v2/_build/privacy.json` currently has a list of 36 pages with hidden photos and an empty `approved` list.
- `v2/_build/claims.json` has 13 claim records.

These are repository-derived snapshots from the checked branch, not guarantees that the counts remain unchanged. Re-run the checks/register generation before using them as the current operational status.

## 12.5 Launch gate

Do not declare launch-ready until all of the following are true:
- No open high-impact claim appears on a live page;
- No outdated price/date is presented as current;
- Every form has an approved data-processing path, retention rule and recipient;
- Every image of a minor has consent documented and retrievable;
- No sample testimonial remains on production;
- Legal/privacy/terms/cookies wording matches actual site behavior;
- Current partner/recognition/logo permissions are documented;
- EN/FR/AR language status is transparent and all published versions are reviewed;
- Every internal link works and every legacy URL has the correct redirect;
- No duplicate/empty headings, broken lists, raw shortcodes or broken media remain;
- Accessibility, performance, mobile, indexation and structured-data QA pass;
- `python v2/_build/check_all.py` and `prelaunch.py` (per project instructions) pass their blocking checks;
- Leadership gives final approval.

---

# 13. Missing content and editorial task register

The following work is evidenced in the repository. Reconfirm live status before assigning tasks.

| Priority | Task | Current evidence/status | Owner to assign | Completion evidence |
|---|---|---|---|---|
| P0 | Confirm 45+ vs 46+ nationalities | Open claim | Institutional approver | Signed/recorded answer and source |
| P0 | Confirm legal status and whether “CSALC” is part of legal name | Open claims | Institutional approver/legal | Legal documentation |
| P0 | Confirm leadership titles and current staff/team | Open claims | Institutional approver | Approved names, titles and biographies |
| P0 | Confirm official/admin/Anglia email purposes | Open claim | Operations | Written contact routing |
| P0 | Confirm current tuition and all ancillary prices | Multiple source/to-confirm values | Admissions/fees owner | Current fee sheet, effective date |
| P0 | Approve current 2026–27 calendar | Mixed old/current calendar source material | Academic owner | Signed academic calendar |
| P0 | Obtain 2026–27 Anglia Saturday class schedule | Current source is 2025–26 | Anglia liaison | Approved session calendar |
| P0 | Confirm Anglia claims, levels, award bodies and logo use | Approval email drafted; open claims | Anglia liaison | Written Anglia response |
| P0 | Confirm form data storage, processors and retention | SmartSite skill says location undecided | Privacy/legal + CMS | Data-flow and retention approval |
| P0 | Clear minor-photo consent holds | 36 hidden journal pages; approved array empty | Privacy owner | Consent evidence by asset/page |
| P0 | Review hidden 2024 parent letter naming child | Privacy hold | Privacy owner | Written consent or permanent redaction |
| P0 | Replace sample testimonials | Parent-story guide exists | Editorial + admissions | Real approved quote, consent and source |
| P1 | Supply missing photography | Spec notes approximately 38 photo slots | Editorial/media owner | Approved asset library and captions |
| P1 | Approve founder letter and story quotes | Draft exists; approval required | Founder | Written approval |
| P1 | Review accreditation and recognition statements individually | Several source claims across pages | Institutional/legal | Evidence and approved wording per claim |
| P1 | Confirm AGI USA legal relationship and address | Open claim | Institutional/legal | Legal entity record |
| P1 | Review clinical/wellbeing credentials and scope | Source service copy | Wellbeing owner/legal | Qualification and service description |
| P1 | Reconcile homework messaging and policy detail | Open claim | Academic owner | Approved policy-aligned copy |
| P1 | Verify university partner status and pathway wording | Some dates and partnerships may be old | Pathways owner | Current agreements |
| P1 | Complete French and Arabic localization plan | 4 FR and 12 AR HTML pages | Translation owner | Approved route coverage matrix |
| P1 | Complete legal/privacy/cookie review | Current implementation needs audit | Privacy/legal | Signed review |
| P2 | Resolve editorial quality flags | `docs/editorial-review.md` | Editorial owner | QA report with no blocking findings |
| P2 | Resolve page-review flags | `docs/page-review.csv` | Editorial + page owners | Updated page audit |
| P2 | Review external links and copyright | Content inventory/resources | Editorial/legal | Link/copyright report |
| P2 | Consolidate content fields for SmartSite | Existing structured export and POC | CMS owner | Schema and import mapping |
| P2 | Establish periodic content reviews | No owner schedule in source | Editorial owner | Approved calendar and named owners |

---

# 14. AI content agent and SmartSite operating rules

The AI content agent must be governed by the following rules:

1. Read `docs/skills/agi-website/SKILL.md` before editing the website.
2. Read the relevant facts, claims and privacy registers before generating or changing a page.
3. Never invent or infer facts, institutional status, prices, dates, staff roles, testimonials or accreditations.
4. If a source conflict exists, stop and ask the assigned approver.
5. Keep all placeholders visibly present and machine-readable.
6. Never publish child names/photos unless written parental consent is confirmed and recorded.
7. Keep one authoritative facts record; do not independently edit repeated price/date/contact strings on pages.
8. Preserve original AGI wording in policies and handbook unless the authorized owner approves a change.
9. Never import copyrighted third-party examination content without rights.
10. Keep all language versions linked to the approved source revision.
11. Do not remove hidden review metadata or `data-placeholder` / `data-verify` attributes during imports.
12. Before large CMS changes, list revisions and preserve a restore point.
13. After imports/edits, run fidelity comparison and the static build QA scripts.
14. Preview the actual page and verify the final output; do not rely only on generated source.
15. Never publish or deploy to production without final human approval.

The existing `docs/skills/agi-website/SKILL.md` remains the operational skill file. This master document defines editorial policy; the skill defines the agent's execution workflow.

---

# 15. Source map and references

## 15.1 Core source files

| File | Why it matters |
|---|---|
| `docs/website-content-spec.md` | Exact page-by-page content, page hierarchy, global behaviors, SEO, functional rules and form specifications |
| `v2/_build/facts.json` | Single structured source for facts, fees, calendars and contacts |
| `v2/_build/claims.json` | Open/closed publication claims |
| `v2/_build/privacy.json` | Image privacy holds and approved exceptions |
| `v2/LAUNCH-CHECKLIST.md` | Open confirmation and launch work |
| `docs/AI-ASSISTANT-BRIEF.md` | Questions, editorial tasks and AI assistant instructions |
| `docs/email-julie-review.md` | Founder/institutional approval questions |
| `docs/email-anglia-approval.md` | Anglia fact and logo approval request |
| `docs/editorial-review.md` | Human editorial corrections |
| `docs/page-review.csv` | Page-level review flags |
| `docs/content-inventory.csv` | Crawled original content inventory |
| `docs/content-map.csv` | Source-to-destination content migration map |
| `docs/content-quality.csv` | Automated content QA issues |
| `docs/privacy-review.csv` | Possible privacy issues |
| `docs/parent-stories-guide.md` | Testimonial interview and consent process |
| `data/export/AGI_Website_Content_Export.json` | Structured source export with pages/news |
| `data/export/work/content_pages.json` | Structured work-in-progress page export |
| `data/export/work/news.json` | Structured journal content export |
| `v2/_build/redirects.csv` | Old AGI URL redirects |
| `docs/angliamorocco-redirects.csv` | Former Anglia-domain redirects |
| `docs/skills/agi-website/SKILL.md` | Agent operating constraints and CMS/build workflow |

## 15.2 Related external/source domains

Historical source records include:
- `americangroup-international.com` — legacy AGI site and published source material;
- `angliamorocco.org` — legacy Anglia Morocco site, now intended to redirect into the AGI Anglia section;
- Official Anglia / Chichester College Group / AIM / Ofqual resources — use the current official source for any examination, qualification or regulatory assertion.

Do not use the historical domains as substitutes for current approval.

---

# 16. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 16 November 2026 | Created repository-derived editorial master framework; reconciled 151 HTML-page count; documented content hierarchy, source authority, status vocabulary, audience journeys, page register, programs, Anglia content library, forms, SEO, localization, evidence/approval controls, editorial operations and launch gates |

---

## Final governance statement

**The Website Content Bible is the single editorial governance reference.** The detailed specification remains the canonical page-copy source until each page is migrated to an approved structured CMS record. Facts, claims, privacy holds and approvals remain in their designated registers. No document or AI-generated output may silently override those registers.

A page is not approved merely because it exists, has copy, appears in the sitemap or has been rendered in the current build. Publication requires accurate source material, the correct owner and approval, current facts, valid permissions and completed QA.
