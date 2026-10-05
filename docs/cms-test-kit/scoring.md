# Scoring (0–3 per criterion, max 45)

| # | Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| 1 | **Setup & MCP connection** | could not connect | connected with workarounds | connected, OAuth only (expires) | connected with a scoped key/token, unattended |
| 2 | **Discoverability** (agent learns the CMS through MCP guides/capabilities) | no guidance | sparse | good tools, little guidance | guides + capabilities + component catalog |
| 3 | **First build quality** (matches brief: sections, texts, design, mobile) | broken | major gaps | minor gaps | faithful |
| 4 | **Native structure** (components/blocks, not one HTML blob) | blob | partly | mostly native | fully native, reusable |
| 5 | **Global data** (task 1) | duplicated values | one place, manual sync | single source, 1 miss | single source, everywhere |
| 6 | **Extending** (task 2) | failed | inconsistent | consistent with help | consistent, reused components |
| 7 | **Multilingual + RTL** (task 3) | not possible | separate page, manual RTL | locales, partial RTL | locales + full RTL + linked switch |
| 8 | **Media** (task 4) | failed | outside media library | library, missing alt per language | library + alt per language |
| 9 | **Self-repair** (task 5) | not found | found, not fixed | fixed with help | found and fixed alone |
| 10 | **Rollback** (task 6) | none | partial / manual | revisions, incomplete | exact restore + redo |
| 11 | **Publish/export** (task 7) | locked in | export with losses | static output, minor issues | clean static output, both languages |
| 12 | **Self-check** (task 8) | none | external only | CMS audit, few fixes | CMS audit + fixes + honest list |
| 13 | **Human editor** (your test) | unusable | needs help | usable | obvious for a non-technical person |
| 14 | **Reliability** (errors, crashes, surprises during the whole test) | blocking | many | few | none |
| 15 | **Operations** (install, resources, updates, backups, maturity) | heavy / risky | complex | acceptable | one container, simple backup, mature |

**Interventions:** every time you had to help the agent (explain, fix, retry manually) = 1. Report the total; fewer is better.
**Time:** total agent minutes for build + 8 tasks.
**Decision rule:** highest score wins, unless it scores 0 on criteria 7 (multilingual/RTL), 10 (rollback) or 11 (export) – those are deal-breakers for AGI.
