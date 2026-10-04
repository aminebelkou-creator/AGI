Use the agi-website skill (C:\Users\belko\.claude\skills\agi-website\SKILL.md).

TASK (proof of concept, non-destructive): The Sitewright MCP is bound to the existing project cSl4fD6lQjuc ("Example Project", Northwind demo).
Import ONLY these three AGI pages into it as separate draft pages:
  http://host.docker.internal:8080/index.html
  http://host.docker.internal:8080/fees.html
  http://host.docker.internal:8080/ar/index.html
Rules:
- Do NOT modify, delete or republish any existing (Northwind) page, dataset, media, setting or chrome slot.
- Do NOT "improve", translate, re-word or restyle any AGI content. Faithful import only.
- Before importing, read get_guide("import") and follow it for a faithful import.
After importing, for EACH of the three pages:
  1. run fidelity_check and compare_to_source (and compare_regions if useful);
  2. take a preview_page screenshot and describe what you see (layout, header/footer, fonts, colors);
  3. report precisely what was lost or changed: visible text, facts (fees in MAD, dates, phone numbers, emails),
     links and buttons (targets), data-placeholder / data-verify attributes, the html lang/dir and dir="rtl" on the Arabic page,
     and whether the Northwind project's chrome/theme wrapped or altered the page.
Finally write a concise markdown report to C:\Users\belko\AGI\docs\poc-sitewright-import.md with:
  - the Sitewright page ids/paths of the three imported drafts (needed to delete them later),
  - a table per page (fidelity score / PASS-FAIL, text, facts, links, markers, lang/dir, theme interference),
  - the exact list of losses, and your assessment of whether the demo project's settings distorted the result.
Then print the same summary.
