# Session handoff – AGI website & agent-first CMS

*Written at the end of an incognito Claude conversation (October 2026). Give this file to a new chat or to Claude Code: "Read docs/SESSION-HANDOFF.md and continue."*

## Where everything is
- Project: `C:\Users\belko\AGI` · GitHub `aminebelkou-creator/AGI` (private) · built site `v2/` (151 pages, all checks pass).
- Read first: `README.md` (section 16 = v3 pipeline), `docs/skills/agi-website/SKILL.md` (rules), `docs/AI-ASSISTANT-BRIEF.md` (open questions for Julie).
- Rebuild prompts: `docs/agent-prompt.md` (with AGI design), `docs/rebuild-prompt-neutral.md` (no tech/design, every section described).
- Content: `docs/website-content-spec.md`, `v2/_build/facts.json`, `claims.json`, `privacy.json`, `redirects.csv`, `docs/angliamorocco-redirects.htaccess`.
- Checks: `python v2/_build/check_all.py` · `compare_published.py <folder>` · `test_deploy.py <url>`.

## Decisions made
- ONE website: angliamorocco.org redirects into the Anglia section (33 redirects ready). Anglia logo/colors approved.
- Hosting: EdgeOne Makers works – preview https://agi-website-poc.edgeone.dev (account hotelhersedorparis@gmail.com, international site, ALWAYS `-a overseas`, max 25 MB/file, redirects via `middleware.js`). Build: `python v2/_build/prepare_edgeone.py`, deploy: `edgeone makers deploy "%USERPROFILE%\agi-edgeone-deploy" -n agi-website-poc -a overseas`.
- Direction now: choose the best **agent-first CMS**, then rebuild the site natively on it (operate it mainly via agents).

## CMS evaluation so far
- **Sitewright** (local Docker `agi-sitewright-poc`, http://localhost:8090, projects "Example Project" = demo, "AGI POC" = `GbW8RQ7sK2jx`):
  raw import FAILS (0.35–0.47: design/chrome/links/RTL lost; public-HTTPS only; canonical; imports land on Home; overwrote demo settings – restored).
  Native rebuild pilot (stopped mid-run) reproduced AGI design + Arabic RTL well; defects: menu labels glued to descriptions, `&amp;amp;`, header menu missing.
  Reports: `docs/poc-sitewright-agi-import.md`, `docs/poc-sitewright-import.md`. Strengths: 55-tool remote MCP, fidelity/visual audits, locales, static output. Risks: tiny community, History gaps, OAuth expiry (use a project-scoped API key for unattended agents).
- **Instatic**: strongest agent-first product on paper (OAuth + PAT MCP, typed components, branches, roles, audit, Super Import keeps CSS) – but NO i18n, pre-1.0. Not yet tested.
- **Git-native** option (content files + schemas + CI checks + EdgeOne, Pages CMS for humans): simplest for agents; not yet tested.
- Others reviewed and set aside: EmDash (backup), Primo, Webstudio, Craft, Keystone, BaseHub, AICMS, Tinykit, markdown.fast.

## Next step proposed
Run the **8-task agent test** on Sitewright (AGI POC): new page from description · fee change everywhere (dataset) · Arabic RTL page · journal post with image · fix a broken link · rollback incl. site settings · publish to EdgeOne · Julie's visual edit (are texts `data-sw-*` editable?). Then decide (Sitewright vs Instatic vs Git-native).
Blocker: Sitewright MCP in Claude Code shows "Needs authentication" → `/mcp` → sitewright → Authenticate (AGI POC), or a project-scoped API key added with `--header "Authorization: Bearer …"` (user enters the key).

## How agents were driven
From a chat via Desktop Commander → `claude -p "<task file>" --allowedTools "<only needed tools>"` headless on the PC. Task files in `docs/poc-task-*.md`. Always: project-id guard, list_revisions first, no delete tools unless intended, verify with our scripts.

## Pending cleanup (only with the owner's OK)
Demo project: 28 leftover files from the failed import (incl. Julie's portrait) + check its logo was restored. AGI POC: partial pilot pages.
