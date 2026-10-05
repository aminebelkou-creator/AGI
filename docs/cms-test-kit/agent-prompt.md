# Agent prompt (identical for every CMS)

Paste this into a FRESH agent session that is connected to the CMS's MCP. Attach or paste `test-page-brief.md` after it.

```
You are connected to a CMS through its MCP server. Your job is to build ONE web page in this CMS,
operating it only through its MCP tools (no manual browser work, no editing files outside the CMS
unless the CMS itself is file-based).

1. First, discover the CMS: read its own guides / capabilities / component catalog through the MCP.
   Summarise in 5 lines how this CMS models pages, reusable components, global data, languages and publishing.
2. Build the page described in the brief below, using the CMS's native building blocks
   (components / blocks / sections / collections) – not one large HTML blob.
3. Store the global data ONCE (settings, dataset or equivalent) and reference it where needed.
   monthly_price must appear in two places, phone in header and footer – from the single source.
4. Use the exact texts from the brief. Do not invent content.
5. When finished, verify your own work with the CMS's tools (preview/screenshot/validation) on desktop and mobile,
   fix what is wrong, then report:
   - what you built (pages, components, data entries),
   - anything from the brief you could NOT do natively and why,
   - how many tool calls it took and any errors you hit,
   - a link or path to preview the page.

Brief:
<paste test-page-brief.md here>
```
