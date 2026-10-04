# Proof of concept — importing three AGI pages into the Northwind demo project

**Date:** 2026-10-04 · **Project:** `cSl4fD6lQjuc` ("Example Project", Northwind demo) · **Role:** owner
**Result: the import did not happen. 0 pages were created. The attempt replaced the Northwind
settings entity, which is awaiting restore.**

---

## 1. Outcome in one line

`import_website` cannot take the three AGI pages. It rejects the task's URLs outright, and when
given a reachable HTTPS equivalent it fetched the page, self-hosted 30 of its assets, then **skipped
the page itself** and overwrote the demo project's site-wide settings with AGI values. No AGI page
object exists in the project, so no fidelity measurement was possible.

## 2. Sitewright page ids / paths of the three imported drafts

**None — there is nothing to delete later.**

| Requested source | Page id | Path | Status |
|---|---|---|---|
| `http://host.docker.internal:8080/index.html` | — | — | not imported (URL rejected) |
| `http://host.docker.internal:8080/fees.html` | — | — | not attempted (same rejection) |
| `http://host.docker.internal:8080/ar/index.html` | — | — | not attempted (same rejection) |

`list_pages({q:"agi"})` → `[]`. `list_content({kind:"page"})` returns only the pre-existing Northwind
pages. The cleanup that *is* needed is on media and settings, not pages — see §6.

## 3. The two blockers

### 3.1 The importer accepts only public HTTPS origins

```
import_website({ url: "http://host.docker.internal:8080/index.html",
                 maxDepth: 0, maxPages: 1, foundation: false })
→ Error 400: only public https URLs can be invalid/imported
```

Verbatim: `only public https URLs can be imported`. The server fetches the page itself, so a
`localhost` / `host.docker.internal` / private-IP origin is unreachable to it by design. This is a
hard validation error, before any crawl. **A local static build can never be imported directly** —
it has to be served from a public HTTPS host first.

I could not stand up the `:8080` server in any case: the PowerShell tool is unusable in this
environment (`pwsh exited with code 1: La ligne de commande est trop longue` on every command,
including `pwd`), and Bash process/network commands (`python -m http.server`, `curl`) were denied.

### 3.2 `rel="canonical"` to another host makes the importer skip the page

Retried against the public HTTPS copy of the same `v2/` build — the EdgeOne PoC deployment, which
is byte-identical to `v2/` apart from an injected `<meta name="robots" content="noindex, nofollow">`
(`prepare_edgeone.py`, preview mode):

```
import_website({ url: "https://agi-website-poc.edgeone.dev/index.html",
                 maxDepth: 0, maxPages: 1, foundation: false })
→ job imp_mut8mk9s1
→ WEBSITE IMPORTED ✓ — 0 page(s) imported (30 media asset(s) self-hosted)
```

Importer notes, verbatim:

- `page-skipped: page is not an internal URL: https://agi-website-poc.edgeone.dev/index.html`
- `locales-detected: detected 3 locales (en, ar, fr); default en`
- `webfonts-hosted: self-hosted Google Fonts: Newsreader, Inter`
- `image-host-failed: could not self-host https://www.americangroup-international.com/assets/web/agi-seal-520.png`

The page it was told to import was classed as *external to itself*. Cause: every AGI page pins its
canonical to the production domain —

```
v2/index.html:39  <link rel="canonical" href="https://www.americangroup-international.com/">
v2/index.html:44  <meta property="og:url" content="https://www.americangroup-international.com/">
v2/index.html:48  <link rel="alternate" hreflang="en" href="https://www.americangroup-international.com/index.html"> …
```

The importer takes the canonical host as the site origin, so the host it actually fetched from
(`agi-website-poc.edgeone.dev`) is "not internal" and every page is skipped. The fourth note is the
same fact from the other side: it tried to pull an image from
`www.americangroup-international.com` and failed, so that domain is not currently serving the build
either — importing from the canonical host itself is not an available workaround today.

Net effect: the crawler walked the page far enough to harvest 30 images and two webfonts and to
sniff the locales, but produced no page object — the one thing the PoC needed.

## 4. Per-page fidelity tables

`fidelity_check`, `compare_to_source`, `compare_regions` and `preview_page` all require a page id,
and all three require `page.data.swImport` (an import source). With 0 pages imported there is
nothing to measure. The ground truth below was read off the local source files so the comparison can
be run the moment a page object exists.

### 4.1 `index.html` → *not imported*

| Check | Result |
|---|---|
| `fidelity_check` | **N/A — no page id** |
| `compare_to_source` | N/A — no page id |
| `preview_page` screenshot | N/A — no page id |
| Visible text | 100% absent (nothing imported) |
| Facts | all absent |
| Links / buttons | all absent |
| Markers | all 7 absent: `photo:home-classroom`, `photo:home-reading`, `testimonial:parent-1`, `testimonial:parent-2`, `testimonial:alumni-1`, `photo:popup-story`, `data-verify="map-location"` |
| `lang` / `dir` | source `<html lang="en" dir="ltr">` — nothing imported to compare |
| Northwind chrome / theme interference | no page to wrap; **the interference ran the other way** — see §5 |

### 4.2 `fees.html` → *not imported*

| Check | Result |
|---|---|
| `fidelity_check` | **N/A — no page id** |
| `compare_to_source` | N/A — no page id |
| `preview_page` screenshot | N/A — no page id |
| Visible text | 100% absent |
| Facts | all absent. Source carries the fee schedule in MAD: 6,500 / 7,500 / 7,800 / 10,000 / 11,000 MAD tuition tiers, 2,600 MAD, 26,000 MAD, 3,000 MAD, 500 / 200 / 150 / 100 / 1,200 MAD line items |
| Contacts | `+212528843349`, `+212 618 639 911`, `+212 688 739 393`, `americanecoleagadir@gmail.com` — none imported |
| Links / buttons | all absent |
| Markers | all 3 absent: `fact:price-play-therapy`, `fact:price-online-tutoring`, `fact:price-modules` |
| `lang` / `dir` | source `<html lang="en" dir="ltr">` — nothing imported to compare |
| Northwind chrome / theme interference | no page to wrap |

### 4.3 `ar/index.html` → *not imported*

| Check | Result |
|---|---|
| `fidelity_check` | **N/A — no page id** |
| `compare_to_source` | N/A — no page id |
| `preview_page` screenshot | N/A — no page id |
| Visible text | 100% absent |
| Facts | all absent |
| Links / buttons | all absent |
| Markers | absent: `data-verify="translation-review:ar"` |
| `lang` / `dir` | source `<html lang="ar" dir="rtl">` plus 3 inner `lang="ar"` scopes. **Untestable, and the known risk stands:** Sitewright sets no page-level direction, so an Arabic page has to be a fork whose source wraps the body in `<div dir="rtl" lang="ar">`. A raw import would have had to be checked for this; it never got that far. |
| Northwind chrome / theme interference | no page to wrap. The Northwind chrome is LTR-only and its locale set did not include `ar` before this run |

## 5. What was actually changed — the import's side effects on the demo project

The task required the run to be non-destructive. It was not. The importer wrote site-wide state
**before** deciding to skip the page, so the damage happened with nothing to show for it.

### 5.1 The settings entity was replaced wholesale

`get_content({kind:"settings", id:"settings"})` after the import returns an AGI-flavoured object.
A full pre-import snapshot was captured and is intact (94,583 bytes, 1,524 lines) at:

```
C:\Users\belko\.claude\projects\C--Users-belko-AGI\dd5ef6ac-fec9-40ee-94e5-a86710445c40\tool-results\mcp-sitewright-list_content-1791082984617.txt
```

| Settings key | Before (Northwind) | After (importer) |
|---|---|---|
| `identity.name` | `Northwind Web Studio` | `American Group International` |
| `identity.legalName` | `Northwind Web Studio Ltd.` | **deleted** |
| `identity.shortName` | `Northwind` | **deleted** |
| `identity.slogan` | `Websites that mean business.` | **deleted** |
| `identity.businessType` | `ProfessionalService` | **deleted** |
| `identity.description` | boutique-web-studio blurb | AGI meta description |
| `identity.logo` / `.icon` | `BzufXH-brand-logo.png` / `l5o6Jm-brand-icon.png` | both → `8NQcCi-favicon.png` |
| `identity.image` | `9mNKIK-brand-og.png` | `https://www.americangroup-international.com/assets/web/agi-seal-520.png` (off-site, un-hosted) |
| `identity.email` | `hello@northwindstudio.com` | `americanecoleagadir@gmail.com` |
| `identity.telephone` | `+1 (415) 555-0142` | `+212528843349` |
| `identity.address` | Northwind address | `Number 20, Rue BaalabekHay Nahda, Agadir 80000` / `Morocco` |
| `identity.social` | Northwind set | single WhatsApp entry `https://wa.me/212688739393` |
| `identity.colors` | 6 tokens | **unchanged** (identical values — no AGI palette extracted) |
| `identity.typography` | `heading: Space Grotesk 700, assetId Yv4gSg` | **deleted** |
| `website.criticalCss` | 7,268 chars of site-wide CSS | **deleted** |
| `website.mainNav` | the header chrome slot (desktop bar + mobile drawer) | **deleted** |
| `website.footer` | the footer chrome slot | **deleted** |
| `website.data` | project data store | **deleted** |
| `website.translations` | ~1,384 lines of de/es strings | **deleted** |
| `website.shop` | shop config incl. `https://paypal.me/northwind/{total}` | **deleted** |
| `website.consent` | `enabled: true` | **deleted** |
| `website.effects` | `navEffect box-solid`, `buttonEffect lift`, `preloaderEffect logo-pulse`, `stickyHeader pinned` | **deleted** |
| `website.enableThemes` / `.defaultTheme` | `true` / `light` | **deleted** |
| `website.siteUrl` | `https://example.com` | `https://agi-website-poc.edgeone.dev/index.html` |
| `website.head` | *(absent)* | **added** — `<link rel="stylesheet" href="/media/example/gX5Xya-styles.css">` |
| `website.scripts` | *(absent)* | **added** — two AGI `<script>` tags |
| `settings.locales` | `["en","de","es"]` | `["en","ar","fr"]` |
| `settings.defaultLocale` | `en` | `en` (unchanged) |

Both chrome slots and the whole visual theme of the demo site are gone from the live entity. The
Northwind pages still reference them, so the demo project currently renders unthemed and
un-navigable.

### 5.2 30 media assets were added

`30 media asset(s) self-hosted` — AGI images plus self-hosted Newsreader and Inter webfonts, written
into the project's media library. One asset failed (`agi-seal-520.png`). The exact id list could not
be read: `list_media` is not granted in this session. No evidence any pre-existing Northwind asset
was replaced; the new ids seen in settings (`8NQcCi`, `gX5Xya`, `828ZKL`, `XgfDqB`) are all new.

### 5.3 Untouched

Pages, datasets, entries, forms and templates: **no change**. All Northwind pages are present with
their original ids, paths, locales, `translationGroup`s and nav slots. Nothing was published or
republished.

### 5.4 Restore status — OPEN

Restoring needs one of `restore_revision`, `list_revisions` or `put_content`; all three are
ungranted in this session, so the overwrite is still live. Both repair routes are ready:

1. **Preferred** — `list_revisions({kind:"settings", id:"settings"})` then
   `restore_revision(…, revisionId:<the revision immediately before job imp_mut8mk9s1>)`. Exact, and
   non-destructive (the current version stays in history).
2. **Fallback** — `put_content({kind:"settings", id:"settings", data:<the snapshot above>})`. The
   snapshot is complete, but it would have to be re-serialised by hand through a 7,268-char
   `criticalCss` line, which risks a subtle escaping error. Use route 1.

## 6. Exact list of losses

**AGI content lost in the import: everything.** 0 of 3 pages, 0 of 3 `<html lang/dir>` declarations,
0 of 11 `data-placeholder` / `data-verify` markers, 0 facts, 0 links, 0 buttons. There is no partial
result to grade — the loss is total and it is a *skip*, not a degradation.

**Northwind state lost (recoverable):** the 20 settings keys marked *deleted* / overwritten in §5.1,
chiefly `criticalCss`, `mainNav`, `footer`, `translations`, `shop`, `effects`, `typography`, and the
`de`/`es` locales.

**Pollution added:** 30 media assets, `website.head`, `website.scripts`, locale `ar` + `fr`.

## 7. Did the demo project's settings distort the result?

**No — the causation is inverted, and that is the finding.** The Northwind project's own settings,
theme and chrome played no part in the failure: nothing was wrapped, re-themed or restyled, because
no page object was ever created. The two things that stopped the import are both properties of the
*source* and of the importer, not of the demo project:

1. the importer's URL policy (public HTTPS only), and
2. the AGI build's cross-host `rel="canonical"`.

What the demo project *did* suffer is the reverse distortion: a single-page import with
`maxDepth:0, maxPages:1, foundation:false` treated the target project's site-wide settings as its
own to replace. **`import_website` is not safe to point at a project you want to keep.** It is a
project-level operation dressed as a page-level one, and the "import one page as a draft, change
nothing else" shape the task asked for is not available from this tool.

A second, quieter distortion is worth recording: the importer sniffed `en, ar, fr` from the AGI
hreflang tags and rewrote the locale set. Had the pages actually landed, the Arabic page would have
arrived into a project whose chrome is LTR-only and whose slots had just been emptied — so the
Arabic `dir="rtl"` question (§4.3) would have been untestable in this project regardless.

## 8. What a real run of this PoC needs

1. **Restore Northwind settings first** (§5.4), and prune the 30 added media assets.
2. **Do not use the shared demo project.** Use a scratch project — `import_website` overwrites
   site-wide settings, so sharing a project with content you care about is not viable.
3. **Serve the pages from a public HTTPS host whose origin matches their canonical.** Either deploy
   with `prepare_edgeone.py --production` and import from the canonical domain once it serves the
   build, or temporarily rewrite `rel="canonical"` / `og:url` / `hreflang` to the preview host in the
   deploy copy. Without that the importer skips every page, silently, after harvesting assets.
4. Only then are `fidelity_check` / `compare_to_source` / `compare_regions` meaningful, and only then
   can the real questions — do `data-placeholder` / `data-verify` survive, does `dir="rtl"` survive,
   does the host project's chrome wrap the page — actually be answered.

## 9. Environment notes

- PowerShell tool: unusable. Every invocation, including `pwd`, fails with
  `pwsh exited with code 1: La ligne de commande est trop longue`.
- Bash tool: file reads work; process-spawning and network commands (`python -m http.server`,
  `curl`) were denied, as were shell `for` loops and `$(…)` substitution.
- Sitewright tools granted this session: `get_scope`, `get_guide`, `get_capabilities`, `list_pages`,
  `list_content`, `get_content`, `import_website`, `import_status`.
  Not granted: `list_revisions`, `restore_revision`, `put_content`, `list_media`.
- `get_guide("import")` and its `chrome` section were read before importing, as required.
