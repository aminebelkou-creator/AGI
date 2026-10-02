# Prompt – rebuild the AGI website with an AI agent

Copy the prompt below into the agent (Claude, Cursor, v0, Lovable, Bolt, a developer brief…).
**Attach:** `docs/website-content-spec.md` (required) and, to rebuild the journal articles, `data/export/AGI_Website_Content_Export.json`.
Optional: photos from AGI, `v2/_build/redirects.csv` (old → new addresses).

Before using it: regenerate the spec so it matches the current site – `python v2/_build/export_spec.py`.

---

## Full prompt

```
You are building the new website of American Group International (AGI), an American-curriculum
school in Agadir, Morocco, and headquarters of Anglia Examinations Morocco.

The attached file "website-content-spec.md" is the single source of truth. It defines the
structure, every page and section in order, the exact copy, all forms, the requirements and the
content rules. It deliberately contains NO design decisions: you choose the visual design.

## What to build
1. Every page in section 4 of the spec, with its sections in the given order and its exact copy,
   browser title and meta description. Do not invent, remove or reword content, figures, prices,
   dates, names or claims.
2. The header navigation, footer, WhatsApp contact and breadcrumbs from section 3, identical on
   every page.
3. All 10 forms from section 5 (fields, types, required/optional rules, hints, options, conditional
   rules, introductions, "Have ready", "What happens next", submit labels), on one forms page where
   each form can be opened directly by its address (e.g. forms.html#absence,
   forms.html#documents/transcript preselects "Academic transcript"). Plus the contact form on the
   contact page.
4. The journal: a list of all 60 posts grouped by year with category labels, and one page per post
   (date, category, full text, images, links to newer/older posts) from the attached export JSON.

## The parent journey (most important)
- parents.html is THE landing page for parents. Its goal is a booked visit, a WhatsApp message or
  an application. Keep its section order from the spec.
- The home page shows a parents popup leading to parents.html, with the SAME headline
  ("Your child, known by name."). Behavior (spec 3.4): never on the first screen; open after the
  visitor has scrolled past half the page, or on desktop on exit intent; once every 7 days;
  on phones a small non-blocking bar at the bottom (no backdrop); on desktop an accessible modal
  dialog (focus trapped and returned; closes with the close button, "Not now", Escape or a click
  outside).
- our-story.html is the longer brand story; it links to parents.html.

## Requirements (spec 3.5) – non-negotiable
- Accessibility: WCAG 2.1 AA. One H1 per page, semantic headings, keyboard-operable menus and
  dialogs, visible focus, contrast ≥ 4.5:1, labelled form fields with error messages shown after a
  field is left (not while typing), alt text, reduced motion respected.
- Performance: mobile-first, modern image formats, lazy loading below the first screen,
  non-blocking fonts. Target Lighthouse ≥ 95 in all four categories on mobile.
- SEO: the titles and descriptions from the spec, canonical URLs, Open Graph tags, "School"
  structured data on the home page, sitemap.xml, robots.txt, 301 redirects from the old WordPress
  addresses (news posts: /<slug>/ → /journal/<slug>.html).
- Forms: until a backend exists, a submitted form opens the visitor's email app pre-filled to
  americanecoleagadir@gmail.com, with "Copy details" and WhatsApp as fallbacks. Structure the code
  so one setting switches to a backend endpoint receiving {type, name, email, phone, payload}.
  NEVER collect card numbers – the payment form is a notice only.
- No cookies or tracking.
- Ready for French and Arabic (right-to-left) later: no text inside images, layouts that can mirror.

## Content rules (spec 3.6) – non-negotiable
- Use only the facts in the spec. Keep every placeholder visible and easy to find:
  [PHOTO NEEDED – …] → a clearly labelled image slot with the caption as a brief for the photographer;
  [TO CONFIRM: …] → the text, visibly marked as awaiting confirmation;
  [SAMPLE …] → the testimonial, marked as a sample.
  Give every placeholder a machine-readable marker (e.g. data-placeholder="photo:<id>") so all of
  them can be listed before launch.
- Do not add: expansion to other cities, Mauritania or the USA; "exclusive" franchise;
  "Director of Global Operations"; any claim that Anglia depends on the UK Ministry of Education;
  invented testimonials; financial figures on the investors page.
- Quote exactly: "Grade placement is not lowered due to missing documents, language gaps, or
  academic gaps." – AGI Provisional Placement Policy.
- Tone: warm, direct, parent-first. US English.
- Slogan "Affordable · Creative · Inclusive" and motto "School + Home + Community = Student Success"
  are the brand line.

## Design
Choose the visual design yourself. It should feel trustworthy, warm and international –
a small school that knows every child – and must work equally well on phones. Keep it consistent
across all pages.

## Deliverables
1. The complete site (static HTML/CSS/JS or a framework that outputs static pages – explain your
   choice).
2. A list of every placeholder (photos, samples, facts to confirm) with page and id.
3. A short README: how to run, build, edit content, replace a photo, confirm a fact, and switch
   the forms to a backend.
4. A self-check against the requirements: Lighthouse scores for home and parents pages, and a
   link check showing no broken internal links.

Ask before deviating from the spec. If something in the spec seems contradictory, flag it rather
than guessing.
```

---

## Short prompt (quick prototypes)

```
Build this website from the attached specification. Follow sections 3.5 (requirements) and 3.6
(content rules) strictly, use the exact copy in sections 4–5, make parents.html the parent landing
page with the home popup described in 3.4, keep every [PHOTO NEEDED], [TO CONFIRM] and [SAMPLE]
marker visible and easy to find, and choose your own visual design.
```

---

## Follow-up prompts

- **Single page or section:** *"Build only parents.html from section 4 of the spec, with the popup from 3.4 on a sample home page."*
- **French version:** *"Translate pages index, parents, our-story, admissions, contact and forms into French (Morocco), keeping structure, placeholders and facts identical; mark the translation for native-speaker review."*
- **Arabic version:** *"Create the Arabic (right-to-left) version of the same pages; mirror the layout; mark the translation for native-speaker review."*
- **Forms backend:** *"Implement the forms backend: one endpoint accepting {type, name, email, phone, payload} for the 11 form types, store submissions, email the office, and switch the site's forms to it."*
