# Brief for Julie's AI assistant – American Group International website
*Generated October 03, 2026 by `v2/_build/assistant_brief.py` from the project's registers. Re-generate after every change; do not edit by hand.*

## 1. Who you are working for and what the job is

You are helping **Julie A. Wilburn** (Founder · CEO & Educational Director, American Group International of Agadir · Anglia Examinations Morocco) verify the new website of her school before it launches. The site is built and every page exists. Your job is to **ask Julie the questions below, one topic at a time, record her answers in the right file, and never publish anything she has not confirmed.**

- Preview: https://agi-preview.vercel.app (not indexed by search engines). French: `/fr/`, Arabic: `/ar/`.
- Text in **gold** on a page = a fact waiting for confirmation. A grey **"Photo"** frame = a photo to supply. "Photo hidden until parental consent is confirmed" = privacy hold.
- The site will move to a CMS (Sitewright) where you will edit it through MCP. Section 7 explains what must survive the move.

## 2. Rules you must follow

1. **Ask, never guess.** If Julie does not know or is unsure, leave the item open. A placeholder is better than a wrong fact.
2. **Children's privacy (Moroccan law 09-08).** Never show a child's name or photo unless Julie confirms *written parental consent* is on file for that child. When in doubt, keep it hidden.
3. **Third-party data.** No personal email, phone or address of anyone outside AGI without their agreement.
4. **Anglia wording.** Use only: "official partner in Morocco of Chichester College Group, UK"; "the four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual"; "the Mastery (C2) qualification carries UCAS tariff points". Do **not** write that Anglia depends on the UK Ministry of Education, is recognized by the British Council, or is accredited by QCA, unless Anglia confirms it in writing.
5. **Copyright.** Do not paste text, tests or images from other organizations (the old Pearson "Total English" placement test was removed for this reason).
6. **Fees and dates live in one place** (`v2/_build/facts.json`). Change them there, never on a single page.
7. **One email per purpose.** Official contact: americanecoleagadir@gmail.com; Anglia Morocco: j.wilburn@ / a.lam@angliamorocco.org.
8. **Tone:** warm, direct, parent-first, US English. Keep AGI's own wording in policies and the handbook; suggest edits, don't impose them.
9. **Keep the safety nets:** after any change run the checks in section 6; the launch is allowed only when `prelaunch.py` says **READY FOR LAUNCH**.

## 3. Questions to ask Julie

### 3.1 Claims to confirm or correct

- **[1]** Anglia is dependent on the UK Ministry of Education; recognised by the British Council; QCA accreditation; ASCENTIS support — *needed:* Do not publish until Anglia confirms current wording
- **[3]** 45+ vs 46+ nationalities — *needed:* Julie
- **[4]** AGI is a private correspondence school — *needed:* Julie (legal status)
- **[5]** Julie's titles (CEO, Country Manager, Director of Operations, Director of Global Operations, Founder) — *needed:* Julie
- **[6]** Team: Latifa Amhari, Mohamed Saih, Rachid Oussalh — *needed:* Julie: current team and roles
- **[7]** Three emails in use (official, admin, agiangliama) — *needed:* Julie: one email per purpose
- **[8]** Saturday schedule is for 2025–26 — *needed:* Get 2026–27 dates
- **[9]** Limited homework vs homework policy minutes — *needed:* Julie
- **[10]** American Group USA LLC address in Grantsville (Maryland) — *needed:* Confirm and publish
- **[12]** Old prices (online tutoring, modules, proctoring, play therapy) may be outdated — *needed:* Julie
- **[13]** Old home page title: 'American Group International CSALC of Agadir' – is CSALC part of the legal name? — *needed:* Julie

### 3.2 Facts to confirm (each appears in gold on the site)

- **contact › email_admin_old:** groupinternationala@gmail.com — Shown as 'Admin' on the old site header – still used?
- **contact › office_hours:** not known yet — Not on either site
- **school › nationalities:** 46+ — Old front page says 45+
- **school › status_wording:** private correspondence school — Legal description on old front page
- **school › school_hours:** not known yet — Not on either site
- **school › transport:** not known yet
- **school › lunch:** not known yet
- **school › sibling_discount:** not known yet
- **school › uniform:** No uniform mentioned; dress code in the handbook
- **fees › online_tutoring_usd:** US$10 – US$50 per session (by length/package) — Exact grid to transcribe in Phase 3; prices may be outdated
- **fees › independent_modules:** US$49.95 / US$79.95 per module; 20% discount mentioned
- **fees › play_therapy:** 150 MAD per session
- **fees › handbook_fees_mentions:** 150 DH, 20 DH (see handbook text) — Identify what these fees are in Phase 1
- **anglia › open_representatives:** Oujda-Angad, Fès, Agadir-Ida Ou Tanane, Taroudant
- **calendars › saturday_classes_2025_26_source_text:** - Anglia Examinations Saturday Classes Yearly Schedule 2025-2026 – American Group International American Group USA LLC W25317017-
# Anglia L… — 2026–27 schedule needed
- **people › julie_other_titles:** Founder (ASCA 2026 post), Country Manager (angliamorocco.org), Director of Operations of AngliaMaroc (2022 post), Director of Global Operati…
- **people › team_old_front_page:** Prof. Abdelhak Lam, Prof. Latifa Amhari, Prof. Mohamed Saih, Mr. Rachid Oussalh — Julie asked to remove Rachid Oussalh

### 3.3 Privacy – needs Julie's decision

- **32 journal posts** show *"Photo hidden until parental consent is confirmed"*. For each post, ask whether written consent exists for every child in its photos. Only then add the page to `approved` in `v2/_build/privacy.json`:
  - `journal/a-day-at-the-seamstress.html`
  - `journal/admissions-2020-2021.html`
  - `journal/american-national-spelling-bee-in-morocco.html`
  - `journal/anglia-c-i-t-e-international-teachers-certification-is-here.html`
  - `journal/anglia-examinations-celebrates-30-years.html`
  - `journal/anglia-testing-session-november-13-28-2022.html`
  - `journal/awarding-of-language-students-april-17-2018.html`
  - `journal/back-to-school-september-2-2019.html`
  - `journal/back-to-school.html`
  - `journal/congrats-dr-kamal-sarjdine.html`
  - `journal/congrats-to-said-el-ouahbi-awarded-his-masters-of-business-administration-and-management.html`
  - `journal/congratulations-graduates-2021.html`
  - `journal/decision-making-by-coaches-and-athletes-in-sport.html`
  - `journal/energia-structure-of-intellect.html`
  - `journal/first-adult-high-school-graduate.html`
  - `journal/first-day-of-school-is-september-5-2018.html`
  - `journal/graduation-2025.html`
  - `journal/graduation-set-projected-june-11th-2021.html`
  - `journal/have-a-great-summer.html`
  - `journal/headquarters-of-angliamaroc-in-agadir.html`
  - `journal/inscriptions-2021-2022.html`
  - `journal/lane-community-college-international-programs.html`
  - `journal/last-day-of-school-june-17-2020.html`
  - `journal/online-classes-for-language-students-starting-in-june-2020.html`
  - `journal/partnership-through-out-morocco.html`
  - `journal/proctoring-services-available.html`
  - `journal/software-and-computer-workshop-and-conference.html`
  - `journal/student-using-microscope-in-science.html`
  - `journal/summer-school-for-academic-and-language-efl-students-2018.html`
  - `journal/summer-school.html`
  - `journal/teachers-training-program-in-english.html`
  - `journal/work-experience-degree-celebration.html`
- **14 possible names** were found near words like student/son/daughter/birthday (most are ordinary words). Ask Julie to confirm none is a child's name:
  - `anglia-cefr.html`: Typical
  - `handbook.html`: Hemlines
  - `pathways.html`: Coventry
  - `placement-policy.html`: Mandatory Assessment
  - `programs-independent-studies.html`: Exhibits
  - `resources-mcguffey.html`: French
  - `resources-mcguffey.html`: Singular
  - `resources-nursery-rhymes.html`: Moses Supposes
  - `resources-nursery-rhymes.html`: Nursery
  - `journal/4292-2.html`: Newer
  - `journal/first-adult-high-school-graduate.html`: Younes
  - `journal/graduation-2025.html`: Younes
  - `journal/graduation-2025.html`: Younes Nait
  - `journal/student-life.html`: Originally
- Special education: a 2024 parent letter naming a child is hidden. Publish only with the family's written consent.

### 3.4 Launch checklist (107 open items)


**1. Fees and dates — AGI**
- Monthly tuition **2,600 MAD over ten months** (home, admissions)
- Annual inscription **6,500 MAD (K–Grade 1) rising to 11,000 MAD (Grade 12)**, non-refundable (admissions)
- "Books, mathematics and Anglia exams, dual enrollment and insurance included" in tuition (home, admissions)
- 2026–27 calendar: registration **Aug 28 & 31**, first day **Sept 7**, fall break **Oct 12–18**, winter break **Dec 18 – Jan 3**, second semester **Jan 5**, Anglia exams **April (date TBA)**, last day & graduation **June 17, 2027** (home, admissions)
- Eligibility: aged **5 by September 1**, **under 21** on the first day (admissions)
- Office hours **Monday–Friday 9:00–17:00, closed Sunday** — and is the office open on Saturdays? (contact)
- Visits/tours **Monday to Friday** (home, forms, contact)
- "The office replies **within one working day**" — a promise on several pages (contact, forms, pathways, professional)

**2. School facts — AGI**
- Founded **2013** with **five children**; moved to **Hay Nahda**; **eight multi-grade classrooms** (home, about)
- **46+ nationalities** over **eleven years** (home, about, student life)
- "**The first American school in Agadir**" — used in the hero, footer and About; confirm it can be claimed
- Mission, philosophy and vision wording (about) — the old "Our Vision" page was Lorem Ipsum; text taken from the school page
- Course of study by grade (k12 curriculum table)
- English benchmarks by grade (CEFR table on english-anglia)
- Homework minutes per grade; **40 service hours** (ten a year) (student life, policies)
- Policy summaries: attendance **90%**, late after **9:00**, absent after **10:00**, **5 tardies = 1 absence**, pass mark **64% (D)**, **90-day** adjustment period (policies)
- Two high-school routes: **Florida-accredited books program** or **American High School Online (Cognia)**, US$2,500/year (k12, admissions)
- Student-life calendar highlights: Global Play Day, Spelling Bee at the American Legation in Tangier, Moroccan & American holidays (student life)

**3. People — AGI**
- Julie A. Wilburn title: **CEO & Educational Director · Anglia Examinations Morocco, American Group International of Agadir**
- Julie bio: "lived in Morocco for many years, dual citizenship", "teaches in the classroom", IPHM & ICAHP accreditation 2026 (about)
- Abdelhak Lam: **Sales Coordinator, main headquarters** — role description "Payments and the Anglia Morocco centers" (about)
- Teacher names, subjects and portraits — 4 teacher slots + Anglia coordinator + admissions contact (about › team) — *placeholders*
- Permission from every person shown or named

**4. Accreditation and partners — AGI (with documents on file)**
- Cognia (American High School Online), QAHE, American Canadian Board, Global Schools Program (member since 2023), ASCA (joined 2026) (about)
- Credit-transfer disclaimer: add back "AGI does not guarantee that credits or the diploma will be accepted by other institutions"? (about, admissions)
- Partner logos and wording: AWA, Learning Pods, American High School Online, I-Heart Women & Family Institute, Chichester College Group, Leverage Edu (about › network)
- Adult diploma: partner **American Worldwide Academy**, **80%** passing score, first adult graduate **2019**, course list & credits (adult-diploma)

**5. Anglia — Anglia / Anglia Morocco HQ**
- Anglia "based in **Chichester since 1993**"; AGI used Anglia since **2013**; **franchise holder for Morocco since 2021** (about, english-anglia, partnerships)
- **Ten levels** mapped to CEFR; **no minimum age**, young learners from about **four** (english-anglia)
- **Anglia International Business English, four levels A2+ to C1** (english-anglia, professional)
- "Official partner in Morocco of Chichester College Group, UK" (Julie's wording, angliamorocco.org) — confirm CCG is happy with it on this site (home, about, english-anglia)
- **Proficiency listed by UCAS** as evidence of English for UK universities — wording approved by Anglia (english-anglia, pathways, about)
- **C.I.T.E.** description: no entry qualifications, CEFR-mapped, lifelong recognition (professional)
- Anglia Morocco covers **twelve regions**; franchise "open in several regions" — which ones? (home, english-anglia, partnerships)
- Use of the Anglia name and logo on the site approved
- Class prices (effective Nov 2024 — still current?): Saturday classes **500 MAD/month** ages 5–18 Sat 14:00–16:00 Oct–June incl. yearly exam; one-to-one **200 MAD**; small group **150 MAD/person**; group course **100 MAD/week (1,200 MAD for 12 weeks)**; level test **free**; groups max **10** (english-anglia)

**6. Professional services — AGI**
- Proctoring: **Mon–Thu 9:00–17:00**, **200 MAD (15 EUR)** admin fee + **200 MAD (15 EUR) per exam hour** (professional)
- USA teacher sponsorship: **US$60**, bachelor's degree, background check, private schools only (professional)
- Bridge Education Group TEFL/TESOL partnership still active (professional)
- ADHD holistic coaching offered in Agadir and online (professional, special education)
- University pathways: "authorized admissions agent"; Leverage Edu regional partner for the Souss; CCG's seven colleges (pathways)

**7. Content still to supply — AGI**
- **Photos** (all `Photo` slots on the site — see `prelaunch.py` output): home ×2, about campus, team portraits, K-12 ×3, student life ×6, one per program page ×5
- A **social share image** 1200×630 (currently the seal) — set `OG_IMAGE` in `_build/build.py`
- **Real testimonials** with written permission (3 on home, 3 on student life — currently samples)
- Social media accounts to link (Instagram / Facebook / LinkedIn / YouTube), if any
- Old journal announcements to hide (e.g. "Inscriptions 2019–2020", "Back to School 2021")
- 5 journal images already missing on the old site (404): ASCA logo, two 2026 posts, one 2020 header — supply replacements or leave out
- French version: translation help for the main pages (home, admissions, programs, contact)

**8. Legal — Legal reviewer**
- Privacy policy (new draft) — Moroccan law 09-08 / CNDP requirements for personal data
- Terms of use (new draft) — replaces the old goods-sales "Terms and Conditions"
- Consent wording on the park/outing consent form and the enrollment form
- Photo/media consent for students shown on the site

**9. Technical — Tech**
- Final domain (currently `https://www.americangroup-international.com`) — `SITE_URL` in `_build/build.py`; regenerate sitemap
- Map pin location correct (Google Maps search for 20 Rue Baalabek, Hay Nahda) (home, contact)
- Hosting chosen; `.htaccess` redirects work on it (Apache) — review `_build/redirects.csv` (old pages sent to the home page)
- Forms backend live (`app/`): accept the 10 form types + contact, set `endpoint` in forms.html and contact.html, office email alerts
- Test every form end-to-end on a phone
- Google Search Console: submit `sitemap.xml`; Google Business Profile address/phone match the site
- Remove "Design preview" wording if any remains; run `python _build/prelaunch.py` → READY

**10. Consistency with angliamorocco.org — AGI / Anglia Morocco**
- Founding wording: angliamorocco.org says AGI has been "an educational brand since **2012**"; this site says the school was founded in **2013** (first classes). Use both? (about, home)
- Open Anglia representative positions listed on angliamorocco.org: **Oujda, Fès, Agadir, Taroudant** — name them on this site? (english-anglia, partnerships)
- Mention Anglia Morocco's history (introduced in Morocco in **2010** by Suzanne Linsen)? (about, english-anglia)
- Business English: this site says four levels **A2+ to C1**; angliamorocco.org says four steps "accredited by AIM" without levels — confirm (english-anglia, professional)
- Anglia Morocco contact emails shown: **j.wilburn@angliamorocco.org**, **a.lam@angliamorocco.org** (english-anglia)
- *On angliamorocco.org*: the FAQ says Anglia is "dependant on the Ministry of Education of the United Kingdom" — inaccurate (Anglia is owned by Chichester College Group; qualifications regulated by Ofqual via AIM). Correct it there.
- *On angliamorocco.org*: "Club Anglia" page still says "Coming soon"; "Country Manager" title differs from the signature used here
- Should the two sites share branding (logo, colors) and link to each other in the header/footer?

**11. Brand story and audience pages — AGI**
- Slogan **"Affordable, Creative and Inclusive"** used in the home hero, home, parents, about, founder letter
- **Founder's letter** (founder-letter.html) — Julie to read and approve the wording, or edit it
- Expansion beyond Agadir: **other Moroccan cities? Mauritania? a center in the United States?** — placeholders on about and investors; not stated anywhere else
- Julie's title: signature says "CEO & Educational Director"; another draft used "Director of Global Operations" — which is correct?
- American Group USA LLC: where is it registered (Maryland?) and may we name it on the investors page?
- "Exclusive" Anglia franchise for Morocco — can we say exclusive? (currently "franchise holder")
- Homework: K–12 page says "limited homework – time for family bonding"; the homework policy goes up to 2–3 hours a night in grades 11–12 — which applies?
- C.I.T.E. specializations (General English, Young Learners, Very Young Learners) and internship weeks 2–3 content (teachers)
- Partner universities to list on pathways (RB College, Britts Imperial, UCAM, University of London, SIST, Geneva Business School) — still active?
- Investors page: no financial claims are made; add figures only if Julie wants and can document them
- Testimonials on the parents page are the same samples as home — replace with real ones
- Julie's dual citizenship: say **"American-Moroccan"**? (about)
- Founder's letter includes the expansion sentence (other Moroccan cities, Mauritania, United States) — keep only if confirmed (founder-letter)
- "AGI has placed **hundreds of students** into the American educational system" — Julie's wording on angliamorocco.org; still accurate? (investors)
- **Our story page** (our-story.html): Julie approves the two quotes in "In her words" (taken from the draft founder's letter) and the timeline wording
- Story photos: hero, 2013 / early years, Hay Nahda building, students together, Anglia exam day, Julie today, three pillar photos, popup photo
- Home popup: keep the 6-second / 25%-scroll timing and once-a-week frequency?
- Parents page FAQ – answers needed: sibling discount, school day hours, transport and lunch, uniform (parents)
- Popup: phones = bottom bar after half the page; desktop = dialog after half the page or when leaving; once a week – OK?

**12. From the old home page — AGI**
- The old home page calls AGI "a private **correspondence school**" – should the new site use this legal description? (k12, about)
- Old home page says "**45+** nationalities", the rest of the site "46+" – which number?
- Memorial to partner **Professor Abdelfatah** (Essaouira center, passed away 2024) – include on the partnerships page?
- Mathematics in English: course format, prices and certification workshops – confirm details (english-anglia, teachers)
- Saturday classes: BAC, TOEFL, IELTS, SAT and Mathematics-in-English preparation – still offered?

**13. Languages — AGI**
- French pages (fr/index, parents, fees, contact) reviewed by a native French speaker
- Arabic pages (ar/index, parents, fees, contact) reviewed by a native Arabic speaker (Modern Standard Arabic; Darija for social media only)
- Which further pages to translate next (recommended: admissions, calendar, our-story, faq, anglia)
- Forms in French and Arabic (forms.html is English only today)
- angliamorocco.org Arabic pages: move here (ar/) and redirect, or keep on angliamorocco.org?

**14. From the page review — AGI**
- Special education: a parent's letter (2024) names their child (Ismail) – hidden until the family gives written consent; publish or keep hidden?
- C.I.T.E. page: keep the 2019 teacher reference letter?
- Handbook and parent letter call AGI a "Correspondence" school/institution (highlighted gold) – confirm the legal description (claim #4)
- Old Anglia texts called Julie "Director of Operations" / "Country Manager" – replaced by her confirmed title; OK?
- McGuffey resource page (21,000 words): split into lessons?

**15. Privacy and archive — AGI**
- Review docs/privacy-review.csv: 32 journal posts have photos hidden until written parental consent for every child shown; approve by adding the page to "approved" in v2/_build/privacy.json
- Check the 14 "possible names" in docs/privacy-review.csv (no child's name may appear without consent)
- Old journal posts now show an "Archived post" banner (older than 12 months) – OK, or hide some posts entirely?

**16. Media and external links — Tech**
- 3 videos (64 MB) were copied from the old site into v2/assets/journal/files/ (not in git): upload them to the CMS media library or YouTube when migrating
- Anglia First Step practice packs no longer exist on angliaexams.com – ask Anglia for current links
- Run python _build/ext_linkcheck.py before launch (all 98 external links OK on Oct 3, 2026)

### 3.5 Editorial suggestions (29) – AGI's own texts, Julie decides

Long paragraphs, repetitions and wording in imported texts are listed in `docs/editorial-review.md`. Offer rewrites; apply only what Julie approves.

### 3.6 Material to collect
- Photos for every grey "Photo" frame (landscape, good light; only children with photo consent).
- 3–6 real testimonials with written permission (`docs/parent-stories-guide.md`); the current ones are samples and must be replaced.
- 2026–27 Saturday class schedule; current team list with roles and portraits.
- A qualified person to review Privacy, Terms, Cookies and the consent forms.
- Native speakers to review the French (`fr/`) and Arabic (`ar/`) pages.

## 4. Where each answer goes

| Answer | File | How |
|---|---|---|
| Fee, date, contact, number | `v2/_build/facts.json` | set `value`, `status: "confirmed"` |
| Claim decided | `v2/_build/claims.json` | `status: "confirmed"` / `"rejected"` + note; then update the page text |
| Gold text on a page | the generator in `v2/_build/` that writes it (search the key, e.g. `PH_TXT("faq-hours"`) | replace `PH_TXT(...)` by the final text |
| Photo consent | `v2/_build/privacy.json` | add the page to `approved` |
| Checklist item | `v2/LAUNCH-CHECKLIST.md` | `- [x]` |
| Real testimonial | `TESTIMONIALS` in `v2/_build/pages.py` | replace the sample, remove the sample marker |
| Photo | `v2/assets/web/` + `python _build/webp.py` | replace the slot (`data-placeholder="photo:…"`) |

## 5. Map of the documents
- `docs/julie-questions.md` – the same questions, as a printable list
- `docs/rebuild-plan-v3.md` – how the content was rebuilt from both old sites
- `docs/content-map.csv` – every old page → new page (181 sources)
- `docs/privacy-review.csv`, `docs/editorial-review.md`, `docs/page-review.csv`, `docs/content-quality.csv`, `docs/fact-conflicts.csv` – audits
- `docs/website-content-spec.md` – the whole site as plain content (useful for the CMS import)
- `README.md` – how everything is built

## 6. Checks to run after every change (from `v2/`)
```
python _build/pages.py ; python _build/journal.py ; python _build/launch_assets.py ; python _build/build.py
python _build/coverage_gate.py        # every fact from the old sites still present
python _build/linkcheck.py            # 0 broken links
python _build/privacy_scan.py         # children's names/photos
python _build/content_quality.py      # language, leftovers, formatting
python _build/prelaunch.py            # must say READY FOR LAUNCH before going live
python _build/assistant_brief.py      # regenerate this brief
```

## 7. Moving to the CMS (Sitewright) – what must survive
- **Every page and URL** (146 pages incl. `fr/` and `ar/`), and the **147 redirects** from the old WordPress addresses (`v2/_build/redirects.csv`, `.htaccess`).
- **The markers:** `data-placeholder="photo|fact|testimonial|team:…"` and `data-verify="…"` – they are how unfinished items are found. Keep them until each item is resolved.
- **Global settings:** the fact register (fees, dates, contacts) should become CMS global fields used by every page.
- **Privacy holds:** hidden photos stay hidden until approved; the "Archived post" banner on journal posts older than 12 months.
- **Languages:** `lang`/`dir` attributes, the EN · FR · ع switch, `hreflang` links, right-to-left layout for Arabic.
- **SEO:** titles, descriptions, canonical URLs, School and FAQ structured data, sitemap, `noindex` on previews only.
- **Forms:** 10 forms + contact; the payment form never collects card numbers.
- **Performance and accessibility:** WebP images, non-blocking fonts, WCAG AA contrast – re-test with Lighthouse after migration.

## 8. When everything is answered
1. All gold text, grey frames and privacy holds resolved; `prelaunch.py` → **READY FOR LAUNCH**.
2. Final domain set (`SITE_URL`), redirects tested, forms connected to a backend, sitemap submitted to Google Search Console.
3. Julie gives the final go-ahead. Only then publish.

