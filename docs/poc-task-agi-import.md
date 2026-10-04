Use the agi-website skill.

SAFETY GUARD (do this first): call get_scope. Continue ONLY if the project id is GbW8RQ7sK2jx (the new "AGI POC" project).
If it is cSl4fD6lQjuc (Example Project / Northwind) or anything else, STOP immediately and report – change nothing.

TASK: faithful import of three AGI pages into AGI POC from the public preview (canonical URLs now point to this host):
  https://agi-website-poc.edgeone.dev/index.html
  https://agi-website-poc.edgeone.dev/fees.html
  https://agi-website-poc.edgeone.dev/ar/index.html
- Read get_guide("import") first and follow it. Faithful import only: do NOT improve, translate, re-word or restyle content.
- Import with the smallest scope (one page each, or the three explicitly) – do not crawl the whole site.
- Use import_status until each job finishes; record importer notes verbatim.

Then for EACH imported page:
  1. fidelity_check and compare_to_source (compare_regions where useful);
  2. preview_page screenshot – describe layout, header/footer, fonts, colors, and for the Arabic page whether the content reads right-to-left;
  3. list precisely what was lost or changed: visible text, facts (MAD fees, dates, phones, emails), links/buttons and their targets,
     data-placeholder / data-verify attributes, html lang/dir, dir="rtl".

Write the report to a NEW file C:\Users\belko\AGI\docs\poc-sitewright-agi-import.md containing: page ids and paths, the importer notes,
a table per page (fidelity PASS/FAIL + score, text, facts, links, markers, lang/dir), the exact losses, and your overall verdict.
Print the same summary at the end.
