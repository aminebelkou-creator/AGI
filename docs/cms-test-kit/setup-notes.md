# Setup notes per candidate (what we already know – verify against each project's current docs)

General: run each CMS in its own Docker container/volume, on its own port, so tests never interfere. Create owner accounts yourself.
Connect Claude Code to an MCP: `claude mcp add --transport http --scope user <name> <url>` (OAuth: then `/mcp` → Authenticate),
or with a key: `claude mcp add --transport http --scope user <name> <url> --header "Authorization: Bearer <KEY>"` (you paste the key).

## 1. Sitewright – github.com/sitewright-cms/sitewright (Apache-2.0)
- Docker: `ghcr.io/sitewright-cms/sitewright:latest`, port 80 in container, volume `/app/data`. Already running here: `agi-sitewright-poc` on http://localhost:8090.
- First boot admin: `admin@sitewright.example` / `123456` (change immediately; production: set SW_ADMIN_EMAIL / SW_ADMIN_PASSWORD).
- MCP: `http://localhost:8090/mcp` (OAuth; or a project-scoped key via "Connect an agent"). 55 tools incl. get_guide, put_page, put_content, add_language, fidelity_check, preview_page, publish_project.
- Known: OAuth sign-in expires (headless agents then fail) → use a scoped key. One MCP connection = one project; no create_project tool (create the test project in the UI first).
  Importer: public HTTPS only and it can overwrite project settings – for this test, build natively, do not import.
- Use a NEW project "CMS Test – Atlas" for this kit.

## 2. Instatic – github.com/CoreBunch/Instatic (MIT, v0.0.x pre-1.0)
- Self-hosted, one Bun server (Docker image or Railway template). Check the README for the current Docker command and port.
- MCP: hosted OAuth (PKCE + dynamic client registration) for remote clients, or personal access tokens for Claude Code/Codex/Cursor (docs/features/mcp-connectors.md).
- Built-in AI agent (bring your own OpenAI/Claude key). Visual Components with typed params and slots, templates, loops, forms, branches, roles, audit log, static output.
- Known gap: no multilingual/i18n support (task 3 will show how RTL can be done manually).

## 3. EmDash – github.com/emdash-cms/emdash (MIT, beta)
- Astro-based; runs on Node + SQLite or Cloudflare (D1/R2/Workers). Check the README for the quick start.
- Built-in MCP server (Claude and ChatGPT), CLI, agent skills; WordPress-like admin with inline editing, roles, revisions, forms plugin.
- Unknown: content localisation + RTL – task 3 will tell.

## 4. Primo – primo.build (MIT, v3.2)
- Local files (Svelte blocks + YAML content) + server (PocketBase) for visual editing. No MCP: agents (Claude Code/Codex) edit the files, then `primo push`.
- For this kit: score "Setup & MCP" on how well a CLI agent can operate it; note that ChatGPT-style assistants cannot connect.

## 5. Git-native baseline (no CMS product)
- A small static generator (any: plain HTML + a JSON data file, or Astro/Eleventy) in a Git repo; global data in `data/site.json`; content in Markdown/JSON.
- Agents edit files; checks run in CI; human editor = Pages CMS (pagescms.org) on the GitHub repo.
- Use it as the reference: if a CMS cannot beat this baseline on agent simplicity, it is not worth the extra server.

## Optional
- Webstudio (local MCP via CLI, strong design; needs a separate CMS for content) – only if design freedom becomes the priority.
