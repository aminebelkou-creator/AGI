Use the agi-website skill (C:\Users\belko\.claude\skills\agi-website\SKILL.md).

SAFETY GUARD: call get_scope first. Continue ONLY if projectId is GbW8RQ7sK2jx ("AGI POC"). Otherwise STOP. Call list_revisions before your first write.
A previous run may have left partial work in AGI POC – inspect it (list_pages, get_content settings) and reuse or overwrite it; do not delete anything.

SMALL PILOT – TWO PAGES ONLY. Keep it short: at most 2 build attempts per page.
Sources (public preview, identical to the AGI build):
  EN home: https://agi-website-poc.edgeone.dev/
  AR home: https://agi-website-poc.edgeone.dev/ar/
Previous raw-import measurements: C:\Users\belko\AGI\docs\poc-sitewright-agi-import.md (read the summary only).

1. Read get_guide("import") (nativize section), get_guide("i18n"), get_guide("nav"). Be brief – only what you need.
2. Corporate identity: AGI colors (navy #0A3161, deep #061529, red #B22234, gold #C9A227, paper #F6F5F1), fonts Newsreader (titles) / Inter (text) / Noto Naskh Arabic (ar).
3. Native header (AGI seal + "AGI / American Group International School · Agadir", main menu, EN/FR/AR switch, Forms, Apply → /forms.html#enrollment)
   and native footer (brand sentence, link columns, Number 20, Rue Baalabek, Hay Nahda, Agadir 80000 · +212 528 843 349 · +212 618 639 911 (Arabic)
   · WhatsApp +212 688 739 393 · americanecoleagadir@gmail.com, legal row). Take labels and targets from the source (inspect_source html:true).
4. EN home → page "home", rebuilt natively. AR home → add_language("ar") if needed, Arabic locale variant of home, content wrapped in
   <div dir="rtl" lang="ar">, Noto Naskh Arabic, Arabic links to /ar/... pages.
   Keep EXACT text, every fact, every link target incl. #fragments, every data-placeholder / data-verify attribute. No rewording, no translation, no invented facts.
5. After each attempt: fidelity_check, compare_to_source, compare_regions (header/footer), preview_page desktop + mobile. Fix and retry once if needed.

REPORT (NEW file C:\Users\belko\AGI\docs\poc-sitewright-nativize.md): per page the scores of attempt 1 and 2 (body coverage, chrome coverage, score, fontMiss),
PASS/FAIL, text/facts/links/markers/lang-dir, what could not be done natively, how long it took, and an honest verdict on migrating the full AGI site this way.
Print the summary at the end.
