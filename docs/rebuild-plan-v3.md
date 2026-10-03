# AGI website v3 – complete content plan

*Study and plan before building · Version 1 · October 2026*
*Sources studied: americangroup-international.com (148 pages and posts, live crawl) and angliamorocco.org (36 pages incl. 6 in Arabic). Data: `data/crawl/inventory.json`, `docs/content-inventory.csv`, `data/crawl/key-outlines.txt`.*

---

## 1. Why we missed content before – and the rules that prevent it

| What went wrong | Rule for v3 |
|---|---|
| We worked from an **export of 128 items**; the live site has **149** | Source of truth = **live crawl of both sites** (`v2/_build/crawl_sites.ps1`), re-run before launch |
| Pages were designed first, content poured in after | **Content first:** every source page is mapped to a destination *before* a page is built |
| No link between old pages and new pages | **Content map** (`docs/content-map.csv`): one row per source URL → destination page + section + action (keep / merge / expand / archive / drop) + reason. No source row may stay unmapped |
| Facts typed in several places (fees on 4 pages, dates on 3) | **Fact register** (`v2/_build/facts.json`): fees, dates, contacts, numbers, prices defined once; pages read them from there |
| Coverage checked at the end, with noisy text | **Coverage gate** after each phase: boilerplate removed (lines repeated on >30% of a site's pages), every source fact present or deliberately excluded; a phase is not done until the gate passes |
| angliamorocco.org studied late | Both sites in scope from day one; Anglia Morocco becomes a full section, not a link |
| Unverified claims crept in | **Claims register** (section 9): anything not confirmed by AGI/Anglia stays a `[TO CONFIRM]` placeholder |

---

## 2. What the two sites contain

| | americangroup-international.com | angliamorocco.org |
|---|---|---|
| Items | 148 (80 pages, 62 posts, 6 archives) | 36 (27 English, 6 Arabic, 2 archives) |
| Words (before boilerplate removal) | ~123,000 | ~16,500 |
| Thin pages (<150 words) | 9 | 9 |
| Already in our site (first estimate) | 66 covered · 79 partial · 3 missing | 13 covered · 13 partial · 7 missing |

**Old AGI menu = full list of services** (all must exist in v3): About · Forms · AGI School Agadir · Academic English K–12 micro-school · Homework guidelines · Volunteer hours · Student life · Special education · ADHD holistic coaching · Holistic play therapy · i-Heart holistic therapeutic services & counselling · Anglia Examinations · C.I.T.E. teacher training/TESOL · Business examinations · Anglia accreditation with AIM · Programs · Adult HS diploma · Document editing · Proctoring · USA private-school teacher sponsorship · AGI learning pods · Admissions procedure · Enrollment · Admission fees · Attestation document request · Mission & academic handbook · Attendance policy · Promotion & retention · Parent policy · Provisional placement policy · Policies, refunds & complaints · CEFR benchmarks · Calendar 2026–27 · Privacy · Saturday classes schedule · EFL classes · Class pricing · Medical EFL · One-on-one EFL · C.I.T.E. · News · Book an appointment · Partnerships · Contact · American Group USA LLC · How long should a tutoring session last · Online tutoring prices · Zoom/Teams instructions · Online teachers database · Education consultancy · English university agent worldwide · Network of partners · Independent course studies · Early childhood education & care diploma · Nursery rhymes · McGuffey readers/sight words · English self-helps · English practice test.

**angliamorocco.org pages:** Home (EN/AR) · About (AR) · Exams (all levels with descriptions) · Business English exams · CEFR · Exam dates 2026 · Special arrangements · Practice resources (EN/AR) · Audio files · Step To books + order form · C.I.T.E. · Club Anglia (coming soon) · Network & centers (12 regions, provinces, open representatives) · FAQ · News (UCAS Mastery, "Julie our newest franchisee") · Privacy · Terms · Cookies.

---

## 3. Site structure v3 (merged)

```
Home · For parents · Our story
About ─ Our story · Founder's letter · Team · Accreditation & memberships · Network & partners · American Group USA LLC
School (K–12) ─ Overview & curriculum · Special education · High school options (books program, American High School Online, summer school)
               · Student life · Homework · Volunteer hours · Supplies list · CEFR benchmarks
Admissions ─ How to apply · Enrollment documents · Tuition & fees (full table) · Calendar 2026–27 (full) · Placement policy · Apply
Policies & handbook ─ Academic handbook (full, by chapter) · Attendance · Promotion & retention · Parent responsibility · Provisional placement
                     · Refunds & complaints · Media · Homework · Volunteer hours · Privacy · Terms · Cookies
Anglia Morocco (English) ─ Anglia Examinations · Levels & exams (General, Young learners, Business, Translation) · CEFR · Exam dates 2026
                           · Special arrangements · Practice resources & audio · Step To books & order form · Free placement test (online)
                           · Classes: Saturday (with yearly schedule), one-on-one, small groups, EFL courses, Mathematics in English · Class prices
                           · Network: 12 regions & centres · Become a centre / representative (franchise) · Anglia FAQ · Arabic pages
Teachers ─ C.I.T.E./TESOL (full) · Teacher training & 30-day internship · USA private-school sponsorship · Early childhood education & care diploma
          · Online teachers database / careers · STEM educators workshop
Adults & professionals ─ Adult high school diploma (full course list) · Independent course studies (modules & prices) · Business/corporate English
                        · Medical English · One-on-one EFL · Document editing · Proctoring · Learning pods & fast-track high school
Wellbeing (i-Heart) ─ ADHD holistic coaching · Holistic play therapy · Therapeutic services & counselling
Online (American Group USA LLC) ─ Online tutoring & prices · How long should a tutoring session last · Zoom/Teams instructions
University pathways ─ Education consultancy · English university agent worldwide · Partner universities (10) · Chichester College Group · Leverage Edu
Journal ─ all 62 AGI posts + Anglia news · Events · Graduations & achievements
Resources ─ Nursery rhymes (Pre-K) · McGuffey readers & sight words · English self-helps · English math resources · Dyslexia resource test
Forms & requests (+ attestation request, book order) · Contact · FAQ hub
Languages: English → French → Arabic (reuse angliamorocco.org's Arabic pages)
```

Navigation: About · School · Admissions · Anglia Morocco · Teachers · Adults · Pathways · Journal · Contact (+ Forms, Apply, language switch).

---

## 4. Page-by-page plan (destination ← sources)

Status today: ✅ in v2 · ◐ partial · ✗ missing.

| Destination | Sources (old URL slug) | Content to include | Today |
|---|---|---|---|
| **Tuition & fees** | admission-fee, anglia-language-class-pricing-and-details, online-tutoring-session-prices-for-agi-usa, independent-course-studies, proctoring, usa-private-school-teacher-sponsorship | Inscription by grade (K–1 6,500 · 2–6 7,500 · 7–8 7,800 · 9–11 10,000 · 12 11,000 MAD); tuition 2,600 MAD × 10; American High School Online LMS US$2,500; summer school 3,000 MAD/month; all-inclusive package; Anglia class prices; online tutoring US$10–50; modules US$49.95/79.95; proctoring; sponsorship US$60 | ◐ |
| **Calendar 2026–27** | school-calandar, last-day-for-students, saturday-classes-yearly-schedule, angliamorocco exam dates | Every school date and holiday (~30 dates); Saturday classes week by week; Anglia exam sessions 2026 by month/level | ◐ |
| **Academic handbook** | agi-academic-school-handbook (7,458 words) | Full text by chapter: mission, philosophy, arrival/dismissal, pick-up, behavior, dress code, discipline levels, acceptable use, acceleration, communication, fees references | ◐ |
| **Attendance** | attendance-policy, admission-fee (repeats it) | Rights, responsibilities, 1/3/5-day consequences, excused absences, family obligations, attendance contract | ◐ |
| **Promotion & retention · Parent responsibility · Placement · Refunds & complaints · Media** | the 5 policy pages | Full texts (refund 50%/80%, 7 days; media consent for under-18s) | ◐ |
| **How to apply · Enrollment** | admissions-procedure, enrollment, admission-prossess, applyform | Steps, application fields, offer of admission, age/residency/health documents, verification rules (3 months, 2 years) | ◐ |
| **K–12 overview & curriculum** | american-group-international-school, academic-english-k-to-12, curriculum pages | Correspondence school status [TO CONFIRM], multi-grade, 36-week year, transcripts | ◐ |
| **High school options** | admission-fee (Option 1…), american high school online LMS, summer school | Books program (Florida accredited), AHS Online (Cognia, US$2,500), summer school | ✗ |
| **Supplies list** | agi-academic-school-supplies-list | Full list by grade | ✗ |
| **Student life** | student-life, events posts | Clubs, events, celebrations, photos | ◐ |
| **Anglia exams & levels** | anglia (AGI), angliamorocco exams, business-examinations, cefr, benchmarks | Every level with vocabulary size and skills; Business 4 steps A2+–C1; durations; certificate for life; translation diploma | ◐ |
| **Exam dates 2026** | angliamorocco anglia-exam-dates-2 | Month × level table; "contact us for unlisted dates" | ✗ |
| **Special arrangements** | angliamorocco special-arrangements | Arrangements list; disability codes D1–D8; how to request | ✗ |
| **Practice resources & audio** | angliamorocco practice-resources (+ AR), audio files | Packs 1–4 for each level; Business; children's oral tests; translation; teachers | ✗ (link only) |
| **Step To books & order** | angliamorocco step-to-books, book order form | Books per level; order form → native form | ✗ |
| **Free placement test** | english-practice-test (2,368 words) | Online test as an interactive form with scoring | ✗ |
| **Saturday classes** | children-and-teens classes, saturday schedule | Program, BAC/TOEFL/IELTS/SAT prep, schedule, 500 MAD | ◐ |
| **Network & centres / franchise** | angliamorocco networks (12 regions + provinces), angliamorocco-networks-and-centers, franchise-opportunities, partnerships, headquarters post | Regions with provinces, open representatives (Oujda, Fès, Agadir, Taroudant), partnership process | ◐ |
| **C.I.T.E.** | cite, teacher-assistant-trainings (2,890 words), anglia-c-i-t-e post | Who, levels, preparation, when/how, reference letter | ◐ |
| **USA teacher sponsorship** | usa-private-school-teacher-sponsorship | Process steps, 30 days, benefits, US$60 | ◐ |
| **ECEC diploma** | early-childhood-education-and-care-degree | American Canadian Board diploma | ✗ |
| **Online teachers database / careers** | online-teachers-database, stem-educators-workshop | Freelance teachers, how to apply | ✗ |
| **Adult HS diploma** | adult-high-school-diploma-program, French post | Full course list with credits, AWA, proctoring, 80% | ◐ |
| **Independent course studies** | independent-course-studies (1,894 words) | All modules, prices, 20% discount | ✗ |
| **Document editing** | document-editing-in-english | Service, process | ✗ |
| **Learning pods & fast track** | anglia-learning-pods, agi-learning-pods, learning-pod-pdf | Pods of 10, 10 weeks, teacherpreneurs, fast-track HS | ✗ |
| **Wellbeing (i-Heart)** | adhd coaching, holistic-play-therapy (150 MAD), i-heart counselling | Three services, prices, approach | ◐ |
| **American Group USA LLC / online tutoring** | american-group-international-usa, online-tutoring prices, how-long-should, zoom/teams instructions | US entity (Grantsville, MD [TO CONFIRM]), tutoring prices, session-length guide, how to join online | ✗ |
| **Pathways** | agi-education-consultancy, english-university-agent, network-of-partners (10 institutions), lane CC post | Services; 10 partner institutions with descriptions | ◐ |
| **Team** | front page team, about-us | Julie Wilburn; Prof. Abdelhak Lam; Prof. Latifa Amhari; Prof. Mohamed Saih; Mr Rachid Oussalh [Julie removed Rachid → TO CONFIRM roles] | ◐ |
| **Journal** | 62 AGI posts + angliamorocco news | All posts, categorized; events tagged | ◐ (59) |
| **Resources** | nursery-rhymes, mcguffey (21,603 words, public domain), english self-helps, english-math-resources, dyslexia test | Resource pages | ✗ |
| **Forms** | forms, document-request, attestation, book-an-appointment, applyform, book order | Native forms incl. attestation & book order | ◐ |
| **Legal** | privacy (both sites), terms (both), cookies (Anglia) | One privacy, one terms, cookies (site sets none) – legal review | ◐ |
| **Arabic** | angliamorocco /ar/ home, about, practice resources | Arabic versions in v3 Arabic phase | ✗ |

The full row-by-row list (all 181 sources) is generated in `docs/content-map.csv` at the start of Phase 0.

---

## 5. Calendar (to consolidate in the fact register)

- **School year 2026–27**: ~30 dates from the old calendar page (start, holidays, Green March, Independence Day, Christmas, New Year, Amazigh New Year, Ramadan, Eids, spring break, Labour Day, last day, graduation).
- **Saturday Anglia classes**: weekly sessions Nov 2025 – Jun 2026 (32 dates) → needs the **2026–27 schedule** from AGI.
- **Anglia exam sessions 2026**: Jan, Apr, May (3 sessions), Jun, Jul, Aug, Sep, Oct, Nov, Dec by level group.
- **Events**: open mornings, registration days (Aug 28 & 31), graduation (Jun 17, 2027), Global Play Day, spelling bee.
One calendar page with filters (school · Anglia exams · Saturday classes · events) + "add to calendar".

## 6. Thin content (18 pages <150 words) – actions

| Type | Action |
|---|---|
| Announcement posts (inscriptions, back to school, testing sessions) | Keep in journal archive; merge facts into calendar |
| Elementor fragments ("Floating Element", "Recent Posts", empty archives) | Drop |
| Anglia "news", "audio files", Arabic duplicates | Merge into practice resources / Arabic phase |
| Short service pages (document editing, attestation) | Expand with process, price [TO CONFIRM], form |

## 7. Events

All event posts (graduations 2021/2022/2024, spelling bee, STEM workshop, English Castle workshop, holiday celebrations, New Year party 2017, seamstress visit, birthday, conversation classes, awarding of language students, CCGi, Leverage, ASCA, Global Schools) → journal with category **Event** + photos; the 4–6 strongest become proof on Student life and Our story.

## 8. FAQ (draft, with sources)

Answers use only sourced facts; ⚠ = needs AGI/Anglia confirmation.

**Admissions & school**
1. *Who can enroll?* – Children aged 5 by September 1 (kindergarten) to under 21 on the first day; open enrollment for any race, religion, color, national or ethnic origin. (enrollment)
2. *What documents are needed?* – Age verification, residency verification (lease, utility bill or similar), immunization and physical examination records, previous school records and a behavior report. (enrollment, admissions-procedure)
3. *Is there an entrance test?* – Yes, a free placement assessment in English/ESL and academics; grade placement is not lowered for missing documents, language gaps or academic gaps. (provisional placement policy)
4. *Can my child join mid-year?* – Yes; students are welcome at any stage. (front page)
5. *My child doesn't speak English yet.* – They join their age group with ESL support and Anglia benchmarks. (placement policy, CEFR benchmarks)
6. *What is a multi-grade classroom?* – Several grades learn together in one of eight classrooms, with individual pacing. (school page)
7. *Do you support special needs?* – Yes: IEPs, small groups, therapy and behavioral support; documentation from a licensed practitioner is required. (special-education)
8. *Is there a uniform?* – No uniform is mentioned; a dress code applies (see handbook). ⚠ (handbook)
9. *What are the school hours? Transport? Lunch? Sibling discount?* – ⚠ not on either site – Julie.
10. *What happens if my child is absent?* – A dated, signed excuse within two days; late after 9:00, absent after 10:00; 90% attendance needed for promotion; consequences escalate 1/3/5 days for unexcused absences. (attendance policy)
11. *How is promotion decided?* – 64% (D) in each core subject, 90% attendance, maturity and the English assessment; summer remediation possible. (promotion policy)
12. *Is homework heavy?* – From 10–20 minutes (K–1) to 2–3 hours (grades 11–12). ⚠ conflicts with "limited homework". (homework policy)
13. *What must high school students complete?* – 40 volunteer hours (10 a year). (volunteer hours)
14. *Which diploma do graduates receive?* – American diploma via the Florida-accredited books program or American High School Online (Cognia). ⚠ (admission-fee, front page)

**Fees**
15. *How much is tuition?* – 2,600 MAD a month over ten months. (admission-fee)
16. *How much is the inscription?* – K–1 6,500 · grades 2–6 7,500 · 7–8 7,800 · 9–11 10,000 · 12 11,000 MAD, non-refundable. (admission-fee)
17. *What is included?* – Books, mathematics and Anglia exams, insurance (all-inclusive package). (admission-fee)
18. *Is there a summer school?* – High school summer school: 3,000 MAD for one month. (admission-fee)
19. *What is the refund policy?* – Inscription non-refundable; other refunds per the policy (50% / 80% rules, 7-day window). ⚠ wording (policies-refunds-complaints)

**Anglia exams**
20. *What are Anglia exams?* – English exams from Anglia Examinations (Chichester, England, since 1993; owned by Chichester College Group), testing reading, writing, listening and speaking at ten levels, First Step to Masters (C2). (exams, about)
21. *Which levels exist?* – Young learners: First Step, Junior, Primary, Preliminary; intermediate: Elementary, Pre-Intermediate, Intermediate; higher: Advanced, Proficiency, Masters; plus Business English (A2+–C1). (FAQ, exams)
22. *From what age?* – From about four; no upper age limit. (FAQ)
23. *How long are the exams?* – Reading & writing 1–3 hours, listening 10–30 minutes, speaking 5–20 minutes, depending on level. (FAQ)
24. *Does the certificate expire?* – It lasts for life, though an institution may ask for a recent one. (FAQ)
25. *When are the exams?* – Sessions every month in 2026 (table); unlisted dates on request. (exam dates)
26. *Can candidates with dyslexia or a disability get help?* – Yes: extra time, supervised breaks, Braille or large print, wheelchair access, a scribe, lip reading. (special arrangements)
27. *Is Anglia recognized by UK universities?* – The Mastery (C2) qualification carries UCAS tariff points. ⚠ exact wording (UCAS news)
28. *How do I find my level?* – Free placement assessment on the CEFR; free practice papers for every level. (front page, practice resources)
29. *Where can I take Anglia in Morocco?* – At AGI in Agadir and Anglia Morocco centres across the 12 regions. (network)

**Classes**
30. *Saturday classes?* – Ages 5–18, Saturdays 2–4 pm, October–June, 500 MAD a month including the yearly exam; BAC, TOEFL, IELTS, SAT and math-in-English prep. (pricing, front page)
31. *Private lessons?* – One-to-one 200 MAD/session; small groups (2–3) 150 MAD/person; groups up to 10: 1,200 MAD for 12 weeks; level test free. (pricing)
32. *Online lessons?* – Through American Group USA LLC: US$10–50 per session ⚠; Zoom/Teams instructions provided. (AGI USA pages)

**Teachers**
33. *What is C.I.T.E.?* – Anglia's Certificate for International Teachers of English, a TESOL qualification aligned with the CEFR; no entry qualifications; lifelong. (cite)
34. *Is there an internship?* – A 30-day teacher internship at AGI. ⚠ weeks 2–3 (teacher training)
35. *Can I teach in the USA?* – Private-school certification sponsorship: bachelor's degree, background check, sponsoring school, US$60; not for public schools. (sponsorship)
36. *Can I teach for AGI?* – Join the online teachers database / learning pods. ⚠ (teachers database, pods)

**Adults & services**
37. *Can adults finish high school?* – Yes, from age 16 with American Worldwide Academy; tests proctored in Agadir; 80% to pass. (adult diploma)
38. *Do you proctor exams?* – Yes, Mon–Thu 9:00–17:00; 200 MAD (15 EUR) admin + 200 MAD per hour. (proctoring)
39. *Do you edit documents in English?* – Yes ⚠ price/process. (document editing)
40. *Do you help with university abroad?* – Yes: authorized admissions agent; 10 partner institutions incl. Coventry, University of London, UCAM, Geneva Business School. (consultancy, network of partners)

**Partners**
41. *How can my school become an Anglia centre?* – Anglia Morocco partnerships in all 12 regions; representatives sought in Oujda, Fès, Agadir, Taroudant. ⚠ (network, franchise)

Unanswerable from sources (→ Julie): hours, transport, lunch, sibling discount, uniform (confirm), document-editing price, online tutoring current prices.

## 9. Conflicts & claims to verify (claims register)

| # | Issue | Sources | Decision needed |
|---|---|---|---|
| 1 | "dependent on the UK Ministry of Education", "recognised by the British Council", "QCA accreditation" (QCA closed 2010), "ASCENTIS" | angliamorocco FAQ | Anglia to confirm current wording; not published until confirmed |
| 2 | Proficiency vs **Mastery** for UCAS | v2 vs angliamorocco news | Use **Mastery (C2) carries UCAS tariff points** – correct v2 now |
| 3 | 45+ vs 46+ nationalities | front page vs school page | Julie |
| 4 | "private correspondence school" | front page | Julie (legal status) |
| 5 | Julie: "Country Manager" vs "CEO & Educational Director" vs "Director of Operations of AngliaMaroc" | angliamorocco, signature, 2022 post | Julie |
| 6 | Team: Latifa Amhari, Mohamed Saih, Rachid Oussalh on old front page | front page | Julie (who is current) |
| 7 | Admin email groupinternationala@gmail.com vs official americanecoleagadir@gmail.com vs agiangliama@gmail.com | menus | Julie: one email per purpose |
| 8 | Saturday schedule is 2025–26 | schedule page | 2026–27 dates needed |
| 9 | Homework "limited" vs policy minutes | K-12 vs policy | Julie |
| 10 | American Group USA LLC address (Grantsville = Maryland) | AGI USA page | Confirm and publish |
| 11 | Western Sahara political text on Anglia network page | angliamorocco | Do **not** reproduce; list regions only |
| 12 | Old prices (online tutoring, modules, proctoring) may be outdated | various | Julie |

---

## 10. Build phases and gates

| Phase | Scope | Gate (must pass) |
|---|---|---|
| **0. Foundation** | Re-run crawl; boilerplate removal in `inventory.py`; generate `content-map.csv` (181 rows, auto-suggested, then reviewed); `facts.json` fact register; `coverage_gate.py`; claims register as data | Every source row has a destination and action |
| **1. Parents' essentials** | Tuition & fees (full), Calendar 2026–27 (full), How to apply, Enrollment, all policies in full, Academic handbook by chapter, FAQ hub v1 | Gate on all admission/fee/policy/calendar sources = 100% facts present or excluded |
| **2. Anglia Morocco** | Exams & levels, exam dates, special arrangements, practice resources, Step To books & order form, placement test (interactive), classes & prices, Saturday schedule, network & centres, become a centre, Anglia FAQ | Gate on all 36 angliamorocco.org pages + AGI Anglia pages |
| **3. Teachers, adults, wellbeing, online, pathways** | C.I.T.E., internship, sponsorship, ECEC, teachers database; adult diploma (full courses), independent studies, business/medical EFL, document editing, proctoring, learning pods; i-Heart services; AGI USA & online tutoring; consultancy, university agent, 10 partners | Gate on all service/program sources |
| **4. Journal, events, resources** | All 62 + Anglia posts, event category, resources pages (nursery rhymes, McGuffey, self-helps, math, dyslexia test) | Gate on all posts and resources |
| **5. About, team, legal, forms** | Team, network & partners, AGI USA LLC, legal (one privacy/terms/cookies), attestation & book-order forms | Gate on remaining sources = 0 unmapped |
| **6. QA & preview** | Link check, site audit, content audit, Lighthouse ≥95, prelaunch report, spec regenerated, Vercel preview | All checks green; preview shared |
| **7. French, then Arabic** | Main pages FR; AR pages (start from angliamorocco.org Arabic) | Native review |

**Definition of done (whole site):** 181/181 source pages mapped; every fact from every kept source present (or excluded with a reason); every claim either confirmed or placeholder-marked; Lighthouse ≥95; 0 broken links; FAQ answers each linked to a source.

## 11. Open decisions for Julie (in addition to `LAUNCH-CHECKLIST.md`)

Claims register items 1–12 · school hours, transport, lunch, sibling discount · 2026–27 Saturday schedule · current prices (online tutoring, modules, document editing) · which Anglia Morocco content stays on angliamorocco.org vs moves here (recommendation: **this site becomes the single home; angliamorocco.org redirects** to the Anglia Morocco section, keeping its Arabic pages).
