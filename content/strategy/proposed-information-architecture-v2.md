# AGI website — proposed information architecture and content model

**Status:** proposed target structure for review; not an approved live navigation or route migration.  
**Date:** 17 November 2026  
**Editorial master:** English (en-US); French (fr-MA) and Arabic (ar-MA) are reviewed localisations.  
**Principle:** one canonical content item, multiple audience paths, no duplicate pages for the same service.

## 1. Strategic architecture

AGI should be presented as the institutional organisation and school in Agadir, with clearly distinguished divisions and programmes. The website should not make visitors decode internal company structures.

The information architecture should answer five user questions quickly:

1. What is AGI and what does it provide?
2. Is there a school or learning programme that fits me/my child?
3. How do English courses and Anglia examinations work?
4. What professional, adult or international pathways are available?
5. How can I apply, ask a question or access an existing service?

AGI Morocco and Anglia Morocco should be visibly related but not conflated. Anglia is an examination/education brand and franchise relationship whose exact authorised scope must be stated precisely. AGI USA should have a distinct regional/operating identity only if its current legal and operational status is confirmed.

## 2. Proposed top-level navigation

| Navigation label | Primary audience | Purpose |
|---|---|---|
| **About AGI** | All visitors, partners | Explain the organisation, school, mission, people and approach |
| **Our School** | Parents, students | K–12 programme, inclusive learning, student life, admissions and parent information |
| **English & Examinations** | Learners, parents, professionals | English courses, Anglia exams, business English, placement and centres |
| **Teacher Development** | Teachers, schools | C.I.T.E., professional learning, workshops and verified pathways |
| **Adult & Global Pathways** | Adult learners, professionals | Adult diploma pathway, education consultancy, proctoring and verified partner routes |
| **Resources** | Parents, learners, teachers | Guides, learning resources, policies, forms and news |
| **Contact** | All visitors | Contact details, appointment and application enquiry |

Persistent primary CTA: **Enquire / Apply**.  
Secondary CTA on relevant pages: **Book a consultation** or **Find an examination centre** only where the destination and service are operational.

### Navigation rules

- Do not place every policy, downloadable resource or news item in the main navigation.
- Use audience-focused landing pages with clear next steps.
- Keep News/Stories as a separate editorial section, with date, author/source, image rights and review status.
- Keep forms out of the general page model; forms need their own access, consent, security and retention design.
- Do not display unverified partner logos, accreditations, centre locations, prices or current schedules.
- Arabic navigation, breadcrumbs, page layout and forms must support RTL; translation is not just a translated menu.

## 3. Detailed site tree

```text
/
├── About AGI
│   ├── Overview and story
│   ├── Mission, vision and values
│   ├── Our school in Agadir
│   ├── Our approach to learning
│   └── Partners and affiliations (verified only)
│
├── Our School
│   ├── School overview
│   ├── Academic programme (K–12; authorised grades only)
│   ├── Inclusive learning and student support
│   │   ├── Learning support approach
│   │   ├── ADHD coaching (if currently offered and approved)
│   │   └── Play-based support (only after specialist review)
│   ├── Student life
│   ├── Admissions
│   │   ├── How to apply
│   │   ├── Placement and assessment
│   │   ├── Fees and payment information
│   │   └── Request school documents
│   ├── Parent information
│   │   ├── Parent handbook
│   │   ├── School calendar
│   │   ├── Attendance
│   │   ├── Promotion and retention
│   │   ├── Parent responsibilities
│   │   ├── Homework guidance
│   │   ├── Supplies list
│   │   ├── Volunteer hours
│   │   └── Media and image consent
│   └── School policies
│       └── Refunds and complaints (shared policy hub; service-specific terms)
│
├── English & Examinations
│   ├── English courses
│   │   ├── General English / EFL
│   │   ├── One-to-one English
│   │   ├── Business English
│   │   ├── Medical English
│   │   └── Learning pods
│   └── Anglia Morocco
│       ├── About Anglia examinations
│       ├── Exam levels and formats
│       ├── Business English examinations
│       ├── Recognition and accreditation (qualification-specific)
│       ├── C.I.T.E. examination for teachers
│       ├── Find a verified centre
│       ├── Current examination schedule
│       ├── Fees (dated and approved)
│       └── Resources
│           ├── Placement/practice test
│           └── CEFR guidance
│
├── Teacher Development
│   ├── C.I.T.E. examination
│   ├── Independent study courses (verified credentials only)
│   ├── Workshops and events
│   └── USA teacher pathways (only if legally and operationally verified)
│
├── Adult & Global Pathways
│   ├── Adult high-school completion pathway (awarding body and recognition disclosed)
│   ├── Education consultancy
│   ├── Verified university partners
│   └── Examination proctoring
│
├── Resources
│   ├── English learning library
│   ├── Early-years resources (rights-cleared)
│   ├── Reading and sight-word resources (curated links; no unlicensed copying)
│   ├── Online learning access guide
│   ├── Forms and administrative services
│   └── News and stories
│
├── AGI USA (regional landing page, conditional on verification)
│   ├── Overview and actual service scope
│   ├── Tutoring information (if active)
│   └── Resources
│
├── Contact
│   ├── Contact details
│   ├── Appointment booking
│   └── Apply / request consultation
│
└── Legal
    ├── Privacy notice
    ├── Website terms
    ├── Service-specific terms
    └── Cookie information (if applicable)
```

## 4. Page and content disposition principles

The companion file `route-content-review.csv` maps all 68 legacy routes to a proposed destination, content type, action, priority and review gate.

Recommended consolidation decisions:

- Merge the two C.I.T.E. pages into one canonical Anglia Morocco page. Preserve both existing URLs with a tested redirect only after approval. The source content itself says C.I.T.E. is not in itself a teaching qualification; do not market it as a teaching licence or a standalone TESOL qualification.
- Merge the two Learning Pods pages into one service page, unless the programme owner confirms that AGI and Anglia pods are materially different offerings.
- Compare the English Castle and STEM Educators Workshop pages. If they describe the same workshop, create one dated event/case-study record and preserve both URLs through aliases/redirects.
- Merge the nearly empty attendance explainer into the approved attendance policy/resource.
- Split refunds and complaints into separate policy content where their procedures differ.
- Split school admission fees from unrelated attendance/policy text found inside that page.
- Move the 2022 important-dates content to historical archive; do not present it as current.
- Replace the McGuffey/sight-words mega-page with a short curated resource page linking to authorised external resources. Do not republish third-party materials without permission.
- Treat nursery rhymes, songs, worksheets and images as rights-controlled assets; publish only licensed, public-domain or original materials.
- Keep school handbook and other policies versioned, with owner, approval date, effective date and superseded versions.
- Keep News as a separate content type, not part of the 12 core marketing pages.

## 5. CMS content types

The CMS should use a small set of reusable content types rather than creating a different schema for every page.

| Content type | Use | Important fields |
|---|---|---|
| **Page** | About, school, landing and service pages | stable ID, slug, locale, title, summary, sections, CTA, SEO, status |
| **Programme / Service** | English courses, inclusive support, proctoring, adult pathways | audience, eligibility, delivery mode, duration, location, fees reference, owner, claims |
| **News / Story** | News, announcements, event reports and case studies | title, slug, publication date, event date, author, excerpt, body, media rights, related entities |
| **Policy / Document** | Handbook, admissions, attendance, refunds, media and privacy policies | version, owner, approver, effective date, review date, downloadable file, scope |
| **Partner / Credential** | Institutions, awarding bodies, accreditations, centres | legal name, relationship type, scope, territory, agreement dates, proof/source, logo permission |
| **Resource** | Guides, practice tests, downloadable materials | subject, audience, age/level, format, source/rights, accessibility, review date |
| **Event / Schedule** | Exam sessions, school dates, workshops | start/end, timezone, location, capacity, status, booking link, year/season |
| **Centre / Location** | Anglia centres and school locations | verified name, address, contact, territory, status, map coordinates, consent |
| **Form / Workflow** | Applications, document requests, appointments | form owner, fields, purpose, consent, access, retention, destination, spam controls |

Do not use a generic Page record for news, policies, events or forms if their lifecycle and permissions are different.

## 6. Editorial workflow and governance

Recommended lifecycle:

```text
Draft
  → Editorial review
  → Subject-matter review
  → Legal / partner / safeguarding review (when triggered)
  → Translation review
  → Approved
  → Scheduled / Published
  → Periodic review
  → Superseded / Archived
```

Required roles:
- Author/editor
- Translator
- Subject-matter reviewer
- Legal/partner/safeguarding reviewer (restricted assignment)
- Publisher (separate permission)
- CMS administrator

No content should be publicly published merely because it exists in the CMS. The public API must expose approved/published records only. A translation must not silently fall back to English while being labelled Arabic or French.

## 7. Localisation

- English: master editorial source (`en-US`).
- French: Moroccan French localisation (`fr-MA`).
- Arabic: Modern Standard Arabic, RTL (`ar-MA`).
- Each locale variant shares a stable content ID and translation group.
- Each variant has its own slug, SEO title/description, canonical URL and publication state.
- Use language alternate links only for genuinely equivalent, reviewed translations.
- Prices, dates, legal entity names, addresses, phone numbers, currencies and local terms require locale-aware formatting and owner confirmation.
- Do not translate partner/qualification names or legal designations loosely.

## 8. SEO and URL strategy

- Preserve the 68 legacy URLs until each redirect is approved and tested.
- Build a redirect map with source URL, destination, reason, status code, owner and test result.
- Avoid redirect chains; use one direct permanent redirect when consolidation is approved.
- Keep canonical URLs locale-specific and use `hreflang` only for complete equivalents.
- Give each page one search intent and one primary conversion action.
- Add structured data only where the entity and facts are accurate (Organisation, EducationalOrganization/School, Course, Event, Article, FAQ only when visible).
- No fabricated reviews, ratings, partner counts, accreditations or outcomes.
- Review image alt text, dimensions, licensing and metadata.
- Do not index private teacher records, application details or protected portal content.

## 9. Priority remediation before any staging content import

**P0 — block public reuse until resolved**
- `/about/vision`: Lorem ipsum placeholder.
- `/special-education/i-heart-counselling`: under-construction page.
- `/admissions/calendar`: 2026–2027 title conflicts with 2025 calendar body.
- `/admissions/important-dates`: contains 2022 dates.
- `/anglia/saturday-schedule`: 2025–2026 schedule ended 13 June 2026.
- `/efl-classes/sight-words`: very large third-party content copy; rights and link review.
- `/admissions/document-request`: only a Forminator shortcode in the content body.
- `/usa/zoom-teams-instructions`: malformed Zoom download URL.
- `/apply`: Ninja Forms shortcode and internal links need route/form verification.

**P1 — specialist/owner approval**
- Fees, discounts, course prices and schedules.
- C.I.T.E. and AIM/Ofqual wording.
- Adult high-school diploma/awarding-body claims.
- Inclusive-learning, ADHD coaching and play therapy descriptions.
- USA teacher sponsorship and visa/work authorisation wording.
- University/college agency and partnership claims.
- Privacy, terms, refunds, media consent and all child/student policies.
- Public teacher database and any personal data.
- Student images, nursery rhymes, worksheets and partner logos.

## 10. Implementation sequence

1. Approve the target information architecture and brand boundaries.
2. Assign one owner and one subject-matter reviewer to every page/service/policy.
3. Complete evidence and rights checks; freeze or archive expired claims and dates.
4. Create CMS content types and editorial roles in an isolated pilot.
5. Import only a small sample of approved content; retain legacy IDs and URLs.
6. Generate a versioned locale-aware API for the existing React/Vite application.
7. Test route coverage, redirects, forms, search metadata, accessibility, Arabic RTL and fallback behaviour.
8. Prepare a staging-only comparison, backup/restore evidence and rollback plan.
9. Request explicit approval before any production deployment or merge.

## 11. Release boundary

This IA is a proposal, not an instruction to change the live website. The 68 legacy routes, 60 news records and existing page JSON files remain preserved. No redirects, content deletion, production CMS, public API switch or live publication is authorised by this document.
