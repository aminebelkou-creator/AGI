# Prompt – rebuild or migrate the AGI website with an AI agent

*Version 2 · updated October 2026 (one website with Anglia Morocco, Anglia branding, French/Arabic, privacy holds, 151 pages).*

Use this prompt with an agent or developer (Claude, Cursor, a Sitewright/MCP agent, a developer brief).
**Before using it, regenerate the spec** so it matches the site exactly: `python v2/_build/export_spec.py`.

## What to attach

| File | Why |
|---|---|
| `docs/website-content-spec.md` | **Required.** Every page, section, copy, link and form (generated from the built site) |
| `v2/_build/facts.json` | Fees, dates, contacts, numbers – the single source of truth |
| `v2/_build/claims.json` | Claims that must not be published until confirmed |
| `v2/_build/privacy.json` | Journal posts whose photos stay hidden until parental consent |
| `v2/_build/redirects.csv`, `v2/.htaccess`, `docs/angliamorocco-redirects.htaccess` | 147 + 33 redirects that must keep working |
| `v2/assets/` | Images (WebP), logos (AGI seal, Anglia Morocco), journal images, files |
| `data/export/AGI_Website_Content_Export.json` + `data/crawl/inventory.json` | Full text of old journal posts and source pages, if articles must be rebuilt |
| `docs/AI-ASSISTANT-BRIEF.md` | What is still waiting for Julie (do not resolve those items yourself) |

---

## Full prompt

```
You are rebuilding (or migrating into a CMS) the website of American Group International (AGI),
an American-curriculum school in Agadir, Morocco, which is also the headquarters of Anglia
Examinations Morocco. It is ONE website: angliamorocco.org redirects into its Anglia Morocco section.

The attached "website-content-spec.md" is the single source of truth for structure and copy.
"facts.json" is the single source of truth for fees, dates, contacts and numbers.

## 1. What to build
- All pages in section 4 of the spec (151 pages: 69 main English pages, 66 journal articles,
  4 French pages in /fr/, 12 Arabic pages in /ar/), with their sections in the given order,
  their exact copy, browser titles and meta descriptions, and the same URLs.
- The header, footer, language switch (EN · FR · ع), breadcrumbs and WhatsApp contact from spec 3.2–3.4.
- The 11 forms of spec section 5 on forms.html (enrollment, visit, absence, consent, feedback, payment
  notice, tutor request, tutor schedule, documents/attestation, enquiry, Step To books order), each
  addressable (forms.html#books, forms.html#enquiry/anglia, forms.html#documents/transcript …),
  plus the contact form. Never collect card numbers.
- The journal list generated from the articles (grouped by year, category labels).
- A 404 page with absolute links (noindex).

## 2. Design system (keep it – do not redesign)
- Colors: navy #0A3161 (primary), deep #061529, red #B22234 (accents), gold #C9A227 (on dark),
  paper #F6F5F1 (background), grey #5B6472 / muted #646A75 (secondary text).
- Fonts: Newsreader (titles, serif) and Inter (text); Arabic: Noto Naskh Arabic, right-to-left, no italics.
- Components: page hero with breadcrumb, sections alternating paper/white/navy, card grids, definition
  rows, tables in scrollable wrappers, quote blocks, closing call-to-action band on every page,
  collapsible "Full text as published by AGI" sections, photo slots.
- Anglia Morocco section (approved by Anglia): same layout, but accents in Anglia blues
  (#03379F headings/buttons/dark sections, #0082D0 labels, #000F23 deep) and the Anglia Morocco logo
  in the hub hero, the "Why Anglia" strip and as a badge on every Anglia page.
- Mobile-first: no page may scroll sideways at 390px; tables scroll inside their wrapper.

## 3. Behaviors
- Parents popup on the home page only (spec 3.4): leads to parents.html with the same headline;
  never on the first screen; after half the page or exit intent; once every 7 days; bottom bar on
  phones, accessible dialog on desktop.
- Exam dates page: filter "Upcoming / All of 2026". Anglia hub shows the next exam session by date.
- Privacy holds: posts listed in privacy.json "hide_photos" (and not in "approved") show
  "Photo hidden until parental consent is confirmed" instead of photos.
- Journal posts older than 12 months open with the "Archived post" banner linking to fees and calendar.
- Languages: lang/dir attributes, hreflang links between language versions, sitemap with all languages.
- Redirects: all 147 old AGI addresses and all 33 angliamorocco.org addresses must 301 to their new pages.

## 4. Non-negotiable rules
- Use only facts from the spec and facts.json. Keep every placeholder visible AND machine-readable:
  data-placeholder="photo|fact|testimonial|team:<id>" and data-verify="<id>" (gold text, grey photo
  frames). They are resolved by Julie, not by you.
- Never publish: claims in claims.json with status "open" (e.g. "exclusive" franchise, expansion to
  other cities/Mauritania/USA, "Director of Global Operations", Anglia "dependent on the UK Ministry
  of Education", British Council or QCA recognition); any child's name or photo without consent;
  third-party personal contacts; copyrighted tests or texts (the old Pearson placement test is excluded).
- Anglia wording exactly: "official partner in Morocco of Chichester College Group, UK"; "the four
  highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual";
  "the Mastery (C2) qualification carries UCAS tariff points".
- Quote exactly: "Grade placement is not lowered due to missing documents, language gaps, or academic gaps."
- One website: never link to angliamorocco.org; the Anglia mailboxes (j.wilburn@ / a.lam@angliamorocco.org)
  remain in use. One official school email: americanecoleagadir@gmail.com.
- US English; warm, parent-first tone; keep AGI's own wording in policies and the handbook.

## 5. Quality bar (acceptance)
- WCAG 2.1 AA (one H1 per page, keyboard-operable menus and dialogs, contrast ≥ 4.5:1, labelled fields).
- Lighthouse ≥ 95 in all four categories on mobile for home, parents, fees, calendar, anglia-exams.
- 0 broken internal links, 0 broken external links, 0 pages with horizontal overflow on phones.
- Every fact of every source page present (or excluded with a reason) – compare with the original
  site by running the project's checks: python _build/check_all.py

## 6. Deliverables
1. The complete site (or the CMS content), with the same URLs.
2. A list of every remaining placeholder (photos, facts, testimonials, team, translation reviews).
3. A short README: how to edit content, change a fee in one place, replace a photo, approve a privacy
   hold, add a language page, and run the checks.
4. The check results (Lighthouse, links, mobile, coverage).

Ask before deviating from the spec. If two sources disagree, flag it – do not guess.
```

---

## Short prompt

```
Rebuild this website from the attached spec and facts.json: same 151 pages and URLs, exact copy,
the AGI design system (navy/red/gold, Newsreader + Inter) with the Anglia blue theme and logo on
Anglia pages, the 11 forms, EN/FR/AR with right-to-left Arabic, privacy holds and archive banners,
all redirects. Keep every [PHOTO NEEDED]/[TO CONFIRM]/[SAMPLE] marker visible and machine-readable,
never publish open claims, and pass python _build/check_all.py.
```

---

## Follow-up prompts

- **Sitewright migration (CMS + MCP):** *"Import the attached site into Sitewright. Model each page as structured content (sections and fields as in the spec), make facts.json global settings used by every page, keep the data-placeholder / data-verify markers as editable 'to confirm' fields, upload assets and the three videos to the media library, recreate the 11 forms and the 180 redirects, and keep lang/dir/hreflang. Report anything that cannot be represented."*
- **Verification with Julie:** *"Follow docs/AI-ASSISTANT-BRIEF.md: ask Julie the open questions one topic at a time, record each answer where the brief says, and never publish what she has not confirmed."*
- **More French / Arabic:** *"Translate admissions, calendar, our-story, faq, anglia-exams and anglia-classes into French (fr/) and Arabic (ar/, right-to-left), keeping structure, facts and placeholders identical; mark each page data-verify='translation-review:<lang>'."*
- **Forms backend:** *"Connect the 11 forms and the contact form to the CMS or one endpoint receiving {type, name, email, phone, payload}; store submissions; email the office; keep the email fallback."*
