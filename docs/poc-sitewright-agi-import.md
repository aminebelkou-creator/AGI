# Sitewright proof of concept — faithful import of three AGI pages into “AGI POC”

Date: 4 October 2026 · Project: **GbW8RQ7sK2jx** (“AGI POC”) · role: owner · MCP `http://localhost:8090/mcp`

**Safety guard.** `get_scope` was called before anything else and returned
`{"authenticated": true, "projectId": "GbW8RQ7sK2jx", "role": "owner"}`. It is the new AGI POC project, **not**
`cSl4fD6lQjuc` (Example Project / Northwind), so the task continued. Nothing outside this project was touched.

**Method.** `get_guide("import")` was read first. Every import used the smallest possible scope —
`maxDepth: 0, maxPages: 1`, one URL at a time. The site was never crawled. **Faithful import only**: no content was
improved, translated, re-worded or restyled, and the imported scaffolds were deliberately *not* nativized
(the import guide’s “now rebuild each page with native primitives” step was skipped on purpose, because this
proof of concept measures what the importer alone preserves).

---

## 1. Two structural findings that shaped the run

**(a) A URL ending in `index.html` is refused.** Both `…/index.html` and `…/ar/index.html` came back with
`0 page(s) imported` and the note *“page is not an internal URL”*. The same pages import correctly when the
**directory form** of the URL is used (`https://agi-website-poc.edgeone.dev/` and `…/ar/`). The importer appears to
normalise `index.html` away and then reject the requested address as not matching its own canonical form.
Nothing is wrong with the published pages — only with the address given to the importer.

**(b) A single-URL import always lands on the one page `home` (path `""`), replacing what was there.**
`fees.html` was imported, landed on `home`, and was then silently replaced by the next import. The project can
therefore hold **only one of the three pages at a time**. `put_page` and `list_revisions` are not granted to this
agent, so imported pages could not be copied aside either. Each page was consequently imported, measured in full
(fidelity, compare, screenshot, content audit) while it occupied `home`, and then gave way to the next.
**Final state of the project: `home` = the English index page** (re-imported at the end of the run).

---

## 2. Import jobs and importer notes (verbatim)

| # | Job id | URL | Result |
|---|---|---|---|
| 1 | `imp_mut9sb7u2` | `https://agi-website-poc.edgeone.dev/index.html` | **0 pages**, 31 media |
| 2 | `imp_mut9u4353` | `…/fees.html` | 1 page, 21 media (later overwritten) |
| 3 | `imp_mut9uhns4` | `…/` | 1 page, 31 media |
| 4 | `imp_mut9v64p5` | `…/ar/index.html` | **0 pages**, 30 media |
| 5 | `imp_muta168g6` | `…/fees.html` (re-run, measured) | 1 page, 21 media |
| 6 | `imp_muta2k8c7` | `…/ar/` | 1 page, 30 media |
| 7 | `imp_muta64gs8` | `…/` (restore final state) | 1 page, 31 media |

Importer notes, copied exactly as returned:

**Job 1 — `/index.html` (5 notes)**
> page-skipped: page is not an internal URL: https://agi-website-poc.edgeone.dev/index.html | locales-detected: detected 3 locales (en, ar, fr); default en | webfonts-hosted: self-hosted Google Fonts: Newsreader, Inter | effects-mapped: mapped source behaviours to native website.effects: stickyHeader=pinned — verify/adjust in Settings › Effects | foundation-applied: native foundation: colors=base-content, fonts+6named, noise-texture, data-driven nav + footer, foreign js discarded; foreign css kept for the nativize capture (stripped at finalize — publish/author it away if you skip nativize)

**Job 3 — `/` → page `home` (8 notes)**
> locales-detected: detected 3 locales (en, ar, fr); default en | webfonts-hosted: self-hosted Google Fonts: Newsreader, Inter | style-removed: &lt;style&gt; block removed (CSS hoisted separately) | script-dropped: inline/external &lt;script&gt; removed | form-inerted: &lt;form&gt; converted to an inert &lt;div&gt; | form-inerted: &lt;form&gt; converted to an inert &lt;div&gt; | effects-mapped: mapped source behaviours to native website.effects: stickyHeader=pinned — verify/adjust in Settings › Effects | foundation-applied: native foundation: colors=base-content, fonts+6named, noise-texture, data-driven nav + footer, foreign js discarded; foreign css kept for the nativize capture (stripped at finalize — publish/author it away if you skip nativize)

**Job 5 — `/fees.html` → page `home` (4 notes)**
> locales-detected: detected 3 locales (en, ar, fr); default en | webfonts-hosted: self-hosted Google Fonts: Newsreader, Inter | effects-mapped: mapped source behaviours to native website.effects: stickyHeader=pinned — verify/adjust in Settings › Effects | foundation-applied: native foundation: colors=base-content, fonts+6named, noise-texture, data-driven nav + footer, foreign js discarded; foreign css kept for the nativize capture (stripped at finalize — publish/author it away if you skip nativize)

**Job 6 — `/ar/` → page `home` (4 notes)**
> locales-detected: detected 3 locales (en, ar, fr); default en | webfonts-hosted: self-hosted Google Fonts: Newsreader, Inter, Noto Naskh Arabic | effects-mapped: mapped source behaviours to native website.effects: stickyHeader=pinned — verify/adjust in Settings › Effects | foundation-applied: native foundation: colors=base-content, fonts+6named, noise-texture, data-driven nav + footer, foreign js discarded; foreign css kept for the nativize capture (stripped at finalize — publish/author it away if you skip nativize)

**Job 4 — `/ar/index.html` (5 notes)** — identical to job 6 plus:
> page-skipped: page is not an internal URL: https://agi-website-poc.edgeone.dev/ar/index.html

---

## 3. Page ids and paths

All three pages occupied the **same** id and path in turn, because of finding (b):

| Source URL | Page id | Path | Title stored | Canonical stored | noindex | locale |
|---|---|---|---|---|---|---|
| `…/` (index.html) | `home` | `""` | American Group International – American school in Agadir, Morocco | `https://agi-website-poc.edgeone.dev/` | true | — (default `en`) |
| `…/fees.html` | `home` | `""` | Tuition & fees – American Group International, Agadir | `https://agi-website-poc.edgeone.dev/fees.html` | true | — (default `en`) |
| `…/ar/` | `home` | `""` | المجموعة الأمريكية الدولية – مدرسة أمريكية في أكادير | `https://agi-website-poc.edgeone.dev/ar/index.html` | true | **— (default `en`, not `ar`)** |

Each page carried `data.swImport = { sourceUrl, rewritten: false, importedAt }`, status `published`, the correct
`description`, and the AGI seal as `image`. Title, description, canonical and noindex were carried over correctly.

---

## 4. Per-page results

### 4.1 `index.html` → page `home`

| Check | Result |
|---|---|
| **fidelity_check** | **FAIL** — BODY coverage 78 % (85/109), fontMiss 2, gradFail 0, **score 0.47**; CHROME coverage **1 % (1/114)** |
| Visible text (body) | **kept, verbatim** — all 13 sections present (hero, facts, Find your path, One American standard, Affordable/creative/inclusive, director, testimonials, Joining AGI, Recognized in the United States, journal, visit, story popup, CTA band); one `<h1>` |
| Facts | **all kept in body**: 2,600 MAD · August 28 & 31 · September 7 · Dec 18 – Jan 3 · June 17, 2027 · +212 528 843 349 · wa.me/212688739393 · americanecoleagadir@gmail.com · 2013 / 46+ / 4 / 12. **Lost with the footer:** the second number **+212 618 639 911** and the street address |
| Links | 25 body links kept, but **every `#fragment` dropped** (7); **all 65 header/footer links deleted** |
| Markers | **7 / 7 kept** — `photo:home-classroom`, `photo:home-reading`, `testimonial:parent-1`, `testimonial:parent-2`, `testimonial:alumni-1`, `data-verify="map-location"`, `photo:popup-story` |
| lang / dir | `<html lang="en">`, no `dir` attribute, computed `direction: ltr` — **correct for English** |
| Verdict | **FAIL** (body text faithful, page not faithful) |

**Screenshot (preview_page, fullhd + mobile).** The build is **unstyled**: no navy hero, no gold, no cards, no
grid. Everything is a single top-to-bottom column of browser-default HTML — the H1 renders at 32 px instead of
92 px, section headings at 24 px instead of 52 px, card titles at 18.7 px instead of 26 px. Header: a thin white
bar with the AGI seal favicon on the left and a single link “Home” on the right. Footer: a near-black band with
“American Group International”, one phone, one email, and an **indigo** `© 2026` sub-band (Sitewright’s default
accent, not AGI navy #0A3161). The WhatsApp floating button renders as a **full-width black SVG** roughly 800 px
tall, because the `.wa-float` CSS is gone. Photos/seals load at natural size. Fonts: Inter/Newsreader are
self-hosted but applied to the wrong elements (body text that should be Newsreader renders Inter and vice versa).
`compare_to_source` side-by-side shows the original with its navy hero, gold numerals, five-card “Find your path”
row, open “Your child, known by name.” popup and four-column navy footer — none of which the build has.

### 4.2 `fees.html` → page `home`

| Check | Result |
|---|---|
| **fidelity_check** | **FAIL** — BODY coverage 98 % (43/44), fontMiss 5, gradFail 0, **score 0.35**; CHROME coverage **1 % (1/114)** |
| Visible text (body) | **kept, verbatim** — hero + breadcrumb, K–12 school, the three fee tables, all four `<h3>`, Good to know, Requirements at enrollment, English & Anglia classes, Other programs and services, CTA band; section ids `#school #high-school #good-to-know #requirements #english #services` preserved; one `<h1>` |
| Facts | **all kept, exact**: 6,500 / 7,500 / 7,800 / 10,000 / 11,000 MAD · US$2,500 · 2,600 MAD a month · 26,000 MAD · 3,000 MAD · 500 / 200 / 150 / 100 MAD · 1,200 MAD · Free · 200 MAD (15 EUR) · US$60 · 150 MAD · US$10 – US$50 · US$49.95 / US$79.95 · “Prices effective November 2024” |
| Links | **12 of 13 body links destroyed** — all rewritten to `href="/"`; only the breadcrumb “Home” is coincidentally right. All 65 header/footer links deleted |
| Markers | **3 / 3 kept** — `fact:price-play-therapy`, `fact:price-online-tutoring`, `fact:price-modules` |
| lang / dir | `<html lang="en">`, no `dir`, `direction: ltr` — correct |
| Verdict | **FAIL** (text and every price faithful; links and design lost) |

**Screenshot.** All text and all three price tables are present and readable, but the tables have no
`fee-table` styling (no header band, rules, right-aligned prices), the H1 is 32 px not 82 px, the lede renders in
Inter instead of Newsreader italic, the “Apply” button is **indigo #4F46E5 instead of AGI navy #0A3161**, the
“Questions about fees?” band is grey-white instead of navy with a gold APPLY, and the sidebar (`<aside>`) has
collapsed into the text flow. Same generic header/footer and oversized WhatsApp SVG as above.

### 4.3 `ar/index.html` (imported as `…/ar/`) → page `home`

| Check | Result |
|---|---|
| **fidelity_check** | **FAIL** — BODY coverage 87 % (45/52), **fontMiss 18**, gradFail 0, **score 0.47**; CHROME coverage **1 % (1/114)** |
| Visible text (body) | **kept, verbatim** — hero, four figures, “في المتناول، مبدعة وشاملة.”, برامجنا (6 cards), الالتحاق بالمدرسة (01–04), fees line, CTA band; one `<h1>` |
| Facts | **kept**: 2013 · +46 · 4 · 12 · 2600 درهم شهرياً على مدى عشرة أشهر · 28 و31 غشت · 2026–2027 · wa.me/212688739393. **Lost with the footer:** +212 528 843 349, +212 618 639 911, the email and the address |
| Links | **13 of 13 body links wrong** — 10 collapsed to `href="/"`; 3 Arabic links (`./parents.html`, `./fees.html`, `./contact.html`) silently **re-pointed at the English pages** `/parents.html`, `/fees.html`, `/contact.html`. All header/footer links deleted |
| Markers | **1 / 1 kept** — `data-verify="translation-review:ar"` |
| **lang / dir** | **BROKEN** — rendered as `<html lang="en">`; `html[lang='ar']` matches 0 nodes; **no `dir` attribute anywhere** (`[dir]` → 0 matches); computed `direction: ltr` on `html`, `body`, `#main`, `h1` and `footer`. Source measures `direction: rtl` on all five. The page has **no `locale` field** — it replaced the default-language home |
| Verdict | **FAIL — the Arabic page does not read right-to-left** |

**Screenshot.** The Arabic page is rendered **left-to-right**. The buttons row (سجّل الآن · احجزوا زيارة ·
للآباء والأمهات) starts at the left edge instead of the right; the 01–04 enrolment steps run left-to-right;
trailing Arabic full stops land on the wrong side of the headings; the seal sits top-left instead of beside the
hero. The H1 is 32 px (source: 86.4 px measured at 1440 px) and is rendered in **Newsreader**, a Latin serif,
instead of Noto Naskh Arabic — `fidelity_check` counts **18 font misses**, all Arabic headings. Body text does
use the self-hosted Noto Naskh Arabic. No navy hero, no gold figures, no card grid; header is the generic
“Home” bar and the footer the generic English three-line block. `compare_to_source` shows the original as a full
RTL design — navy hero with the gold-accented headline on the right, right-to-left nav with the EN/FR/ع switch,
right-to-left card grid and a four-column RTL Arabic footer.

---

## 5. Exactly what was lost or changed

**Lost on all three pages (site-wide, caused by the import):**

1. **The whole page design.** The foreign CSS is “kept for the nativize capture” but is not applied to the stored
   page, so every page renders as unstyled HTML. Brand colours are replaced by Sitewright defaults
   (buttons/`© ` band **indigo #4F46E5** instead of navy **#0A3161**, no gold **#C9A227**, no navy sections).
   Heading sizes collapse to browser defaults (92 px → 32 px, 52 px → 24 px, 26 px → 18.7 px).
2. **The header.** AGI logo lockup + “AMERICAN GROUP INTERNATIONAL SCHOOL · AGADIR”, the 7-item nav with the
   11-entry “Programs” dropdown and its descriptions, the **EN / FR / ع language switch**, the “Forms” link and
   the **APPLY** button → replaced by a seal favicon and one link, “Home”. Chrome fidelity: **1 %**.
3. **The footer.** The four-column navy footer (Programs 12 links, School 12, Services 12, Contact) with the
   brand sentence, the postal address, **both** phone numbers (+212 528 843 349 and the Arabic line
   **+212 618 639 911**), WhatsApp, the email, and the legal row (Privacy · Terms · Cookies · Accessibility ·
   Safeguarding · Contact) → replaced by a generic block with one phone and the email only.
   (The address and phone were harvested into site settings/JSON-LD, but they are no longer visible on the page.)
4. **All JavaScript and therefore all behaviour**: the story-popup dialog never opens (and its two
   `<form method="dialog">` elements were converted to inert `<div method="dialog">`, so its close and
   “Not now” buttons are dead), the Google map `<iframe>` keeps its `data-src` and never loads, the mobile menu
   and the sticky-header script are gone (sticky header was remapped to a native effect).
5. **Semantic structure**: `<main>` → `<div id="main">`, `<aside>` → `<div>`, `<form>` → `<div>` — landmarks and
   the form elements are gone, which is an accessibility regression against the WCAG 2.1 AA rule in the AGI skill.
6. **Link targets** (the most dangerous loss, because it is invisible in a screenshot):
   - index: all 7 in-page fragments dropped — `forms.html#enrollment` ×3, `forms.html#visit` ×3,
     `about.html#accreditation` → now `/forms.html` and `/about.html`;
   - fees: 12 of 13 body links collapsed to `/` (Apply, Calendar 2026–27, Admissions breadcrumb, Refunds &
     complaints, Attendance, How to apply, Policies, Payment notice, Apply, Ask a question …);
   - Arabic: 10 of 13 collapsed to `/`, and `./parents.html` `./fees.html` `./contact.html` now point to the
     **English** pages — a wrong-language link, not just a broken one.
7. **hreflang alternates** (en / fr / ar / x-default) and the per-page `<style>` block.

**Lost on the Arabic page only — the serious one:** `lang="ar"` and `dir="rtl"`. The imported page has no
`locale`, renders inside `<html lang="en">` with no `dir` attribute at all, computes `direction: ltr`, and its
headings fall back to a Latin serif. This is exactly the behaviour the AGI skill warns about (“Sitewright sets no
page-level direction”), and it confirms the skill’s prescription: Arabic pages must be **fork variants whose
source wraps the content in `<div dir="rtl" lang="ar">`**, or be created with `add_language("ar")` so they get a
real locale.

**NOT lost — what the importer got right:**

- **Every word of body text, verbatim**, on all three pages, including the Arabic, with no re-wording, no
  translation and no “improvement”.
- **Every fact inside the body**: all MAD/US$ prices, the 2026–27 dates, the phone/WhatsApp/email in the page body.
- **All `data-placeholder` / `data-verify` markers — 11 of 11** (7 + 3 + 1). The importer does **not** strip
  `data-*` attributes, so the placeholder/verification system survives an import intact.
- Title, meta description, canonical, `noindex`, OG image, heading hierarchy (one `<h1>` per page), section ids,
  tables, lists, image `alt` text, `width`/`height`, and the self-hosting of images and the three Google fonts
  (Newsreader, Inter, Noto Naskh Arabic).

**One thing to watch before any publication:** the import wrote site-level JSON-LD using the project name —
`"@type":"Organization","name":"AGI POC"` — together with AGI’s real phone, email and address. That must be
corrected to “American Group International” before anything is published.

---

## 6. Verdict

**The import is faithful to the content and unfaithful to the page.** On all three pages the body text, the
facts and all eleven placeholder/verify markers survived verbatim — nothing was invented, translated or
re-worded, which is the hardest requirement in the AGI rules and the importer meets it. Everything else did not
survive: `fidelity_check` fails on all three pages (body scores 0.47 / 0.35 / 0.47, chrome coverage **1 %**),
the design system is absent, header and footer are replaced by generic chrome that loses ~65 links per page and
one of AGI’s two phone numbers, all behaviour is dead, and link targets are silently wrong on fees (12 of 13)
and on the Arabic page (13 of 13, three of them re-pointed at the wrong language).

The Arabic page is the blocking failure: it renders **left-to-right in `<html lang="en">` with no `dir`
attribute**, so it is not publishable in any form. The remedy is the one already written in the AGI skill —
create Arabic pages through `add_language("ar")` / as fork variants wrapping the content in
`<div dir="rtl" lang="ar">`, and verify with `preview_page` every time.

Operationally, two importer behaviours must be planned around for a 151-page site: `index.html` URLs are
rejected (use the directory form), and a single-URL import always overwrites the one `home` page — so a real
migration needs either a single crawl that covers the whole site or per-page writes with `put_page`
(not available to this agent), followed in both cases by the nativize pass the import guide describes.
A faithful import alone is a content transfer, not a site.
