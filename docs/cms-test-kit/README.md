# Agent-first CMS test kit

Goal: compare CMSs on **how simply an AI agent can operate them**, using the same neutral one-page test – independent of the AGI website.
Run one CMS at a time. Same brief, same prompt, same tasks, same scoring. Record results in `results.csv` and a short note per CMS in `results/<cms>.md`.

## Files
- `test-page-brief.md` – the page to build (fictional business, EN + Arabic RTL, all common section types).
- `agent-prompt.md` – the exact prompt to give the agent once it is connected to the CMS's MCP.
- `tasks.md` – the 8 tasks after the first build (change a global value, add Arabic, rollback, …).
- `scoring.md` – how to score (0–3 per criterion) and what counts as an intervention.
- `results.csv` – one row per CMS.
- `setup-notes.md` – how to install and connect each candidate (MCP endpoint, auth, gotchas we already know).

## Protocol (same for every CMS)
1. **Install** the CMS locally (Docker when possible). Create the owner account yourself.
2. **Connect the agent** to its MCP. Prefer a **scoped API key/token** (works unattended) over OAuth sign-in (expires). Note how long setup took.
3. **Fresh agent session** (Claude Code, or your ChatGPT agent). Give it `agent-prompt.md` + `test-page-brief.md`. Do not help unless it is stuck – every help = 1 intervention.
4. **Build**: let it build the page. Stop the clock at "done". Take desktop + mobile screenshots.
5. **Tasks**: run the 8 tasks in `tasks.md`, one prompt each. Record success / interventions / minutes.
6. **Human test**: you (as a non-technical editor) change a sentence, a price and an image in the CMS's visual editor.
7. **Export/publish**: publish or export static output; check it opens without the CMS.
8. **Score** with `scoring.md`; fill `results.csv`; write 5 lines in `results/<cms>.md` (best thing, worst thing, surprise, risk, verdict).

## Rules for a fair test
- Same agent and model for every CMS (e.g. Claude Code with the same model). Note the model.
- The agent may read the CMS's own guides/tools (that is part of "agent-first").
- No manual code fixes by you during build/tasks – only prompts. Manual help = intervention.
- Time-box: build 45 min, each task 10 min. Over time = fail for that step.
- Keep screenshots in `results/<cms>/`.
