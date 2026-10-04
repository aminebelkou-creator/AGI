Use the agi-website skill (C:\Users\belko\.claude\skills\agi-website\SKILL.md). Read it fully first.

SAFETY GUARD: call get_scope first. Continue ONLY if projectId is GbW8RQ7sK2jx ("AGI POC"). Otherwise STOP and report.
Never touch any other project. Call list_revisions before your first write so the starting point is known.

GOAL: Pilot Sitewright's native rebuild ("nativize") of three AGI pages, then measure how faithful it gets.
Sources (public preview, identical to the AGI build; use the directory form for index pages):
  EN home:  https://agi-website-poc.edgeone.dev/
  Fees:     https://agi-website-poc.edgeone.dev/fees.html
  AR home:  https://agi-website-poc.edgeone.dev/ar/
Previous measurements of the raw import are in C:\Users\belko\AGI\docs\poc-sitewright-agi-import.md – read them.

STEPS
1. Read get_guide("import") (the nativize workflow), get_guide("i18n"), get_guide("nav"), get_components and get_capabilities. Follow them.
2. Brand + chrome (site-wide, in AGI POC): set the corporate identity colors and fonts to the AGI design system from the skill
   (navy #0A3161, deep #061529, red #B22234, gold #C9A227, paper #F6F5F1; Newsreader titles, Inter text; Noto Naskh Arabic for ar).
   Build a NATIVE header (AGI seal + "AGI / American Group International School · Agadir", the 7 menu items with the Programs submenu,
   EN/FR/AR language switch, "Forms" link, "Apply" button → /forms.html#enrollment) and a NATIVE footer (brand sentence, the Programs /
   School / Services columns, Contact: Number 20, Rue Baalabek, Hay Nahda, Agadir 80000 · +212 528 843 349 · +212 618 639 911 (Arabic)
   · WhatsApp +212 688 739 393 · americanecoleagadir@gmail.com, legal row: Privacy · Terms · Cookies · Accessibility · Safeguarding · Contact).
   Copy link labels/targets from the source pages (inspect_source html:true).
3. Pages – rebuild each with native primitives, keeping EXACT text, every fact, every link target (keep the original relative targets,
   e.g. /forms.html#enrollment, /fees.html, /calendar.html – including #fragments), and every data-placeholder / data-verify attribute:
   - EN home → page "home" (path "").
   - Fees → its OWN page at path "fees" (import it, then put the nativized page at path "fees" – do not leave it on home).
   - AR home → add_language("ar") if not present, then the Arabic home as the ar locale variant; wrap its content in
     <div dir="rtl" lang="ar">, use Noto Naskh Arabic, keep Arabic link targets pointing to the Arabic pages (/ar/…) where they exist.
   Re-create the popup/map/mobile-menu behaviours with native components where they exist; if impossible, note it.
4. After each page: fidelity_check + compare_to_source (+ compare_regions for header/footer) + preview_page (desktop and mobile).
   Iterate up to 3 times per page to fix what the checks report. Record every score (body coverage, chrome coverage, score, fontMiss).
5. Do NOT improve, translate or re-word content. Do not invent facts. Do not delete anything.

REPORT: write a NEW file C:\Users\belko\AGI\docs\poc-sitewright-nativize.md with: what was built, per page the score progression
(attempt 1/2/3), final PASS/FAIL, text/facts/links/markers/lang-dir results, what could not be reproduced natively, time and effort
observations, and an honest verdict: can a full 151-page AGI migration to Sitewright reach acceptable fidelity this way, and what would it take?
Print the summary at the end.
