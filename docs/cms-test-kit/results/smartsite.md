# SmartSite 4.0.2 – CMS test kit result

- **Date:** 2026-11-16 · **Agent:** Claude (claude-opus-5-5) · **Score:** 29 / 45.
- **Install:** self-hosted Docker stack on a Tencent Lighthouse VPS (2 vCPU, 2 GB RAM). Mongo 8 replica set, Next.js 16 / Payload 3.92 app and a Caddy proxy. The image is built on GitHub Actions because the VPS is too small to build it.
- **Test site:** https://43-157-108-87.sslip.io/ (EN) and /ar (AR). The whole site is set to noindex.
- **MCP:** Payload's official plugin at `/api/mcp` with a scoped key. Four tools: `smartsiteRead`, `smartsiteSave`, `smartsiteUploadMedia` and `smartsiteOperationStatus`.

## 5 lines
- **Best thing:** saves are checked against the current revision, can be safely retried (each write has an ID) and confirm when the page cache has refreshed. Version history plus "read one version" gave an exact rollback and redo.
- **Worst thing:** page building is limited to 3 usable blocks (hero, rich-text content, contact form). Cards, pricing, FAQ accordion and testimonials have no native block, and the theme (colours, fonts, logo) is only changeable in code.
- **Surprise:** a `testimonials` collection exists, but no page block can show it. An unknown field (`meta` instead of `seo.meta`) was silently ignored, with no error.
- **Risk for AGI:** there are no language versions in the content model and no static export. Arabic is a separate page, made right-to-left section by section; the HTML keeps `lang="en"`, there's no hreflang and the header stays in English.
- **Verdict:** a solid, agent-safe CMS core with poor fit for AGI as shipped. Language versions, Arabic RTL, the theme and new blocks would all need code work (Payload supports them) before it could beat the static v2 site.

## Discovery (agent summary)
Pages are made of ordered blocks (`hero`, `content` with rich text, `contact-form`, plus post blocks). Header, footer and settings are shared site-wide data, and settings holds the address, phone and email. There are no content languages; rich text only has a left-to-right / right-to-left direction. Pages can be draft or published and keep full version history, while settings, header, footer, forms and media change immediately. Media upload accepts PNG, JPEG or WebP up to 2 MiB, with one alt text per file.

## First build
**Built:**
- Settings: site name, footer sentence, one location with address, phone and email.
- Media: hero image, CC BY 2.0 "English Tutor" (Preply) from Wikimedia Commons.
- Form: name, email, phone, message, consent, plus a confirmation message.
- Page "Atlas Language Studio" (now the homepage) with 6 blocks and anchors `#top #features #courses #prices #faq #contact`.
- Header: 4 anchor links plus a "Book a free level test" button.
- Footer: menu, Privacy and Terms links.
- SEO title and meta description.

**Not possible natively:**
- No brand colours or fonts (Fraunces, Inter); the site keeps the SmartSite theme and logo.
- No phone number in the header.
- No EN | ع switch in the first build.
- The FAQ is not expandable.
- Feature cards and the pricing card are rich text, not real cards.
- `monthly_price` and opening hours have no shared field, so they are typed into the page itself. Phone, email and address are shared settings for the footer, but are typed again in the contact block.

**Verified:** desktop and 375 px mobile, no sideways scrolling, every anchor resolves. About 3 minutes of agent time.

## Tasks
| # | Task | Result | Notes |
|---|---|---|---|
| 1 | Price → 950 MAD | partial | Edited in **2 places** (hero pre-heading and price card) in one save. No single source. |
| 2 | Testimonials before FAQ | yes | Reused the `content` block, same styling, marked SAMPLE. The native testimonials collection can't be placed on a page. |
| 3 | Arabic RTL | partial | Separate `/ar` page with `dir=rtl lang=ar` set on each section. The `<html>` stays `lang=en`, there's no Arabic font, no hreflang and the header is shared English. Switch: "ع" in the header goes to /ar, an "EN" button on /ar goes back to /. |
| 4 | Replace hero image | partial | Media library upload works. One alt per file, so the Arabic alt needed a second re-encoded copy of the image (workaround). |
| 5 | Broken link (#pricess) | yes | No link checker in the CMS. The agent compared every `#` link with the section IDs through MCP reads, found it and fixed it. |
| 6 | Undo 2 changes, then redo | yes | History plus a stored version, restored against the current revision. Exact restore and redo, confirmed on the live page. |
| 7 | Publish / export | partial | Publishing works and pages are server-rendered. There's **no static export**: a saved HTML copy has the text but points to `/_next/static`, so it opens unstyled. |
| 8 | Self-check | partial | No audit tool in the CMS, so I audited in the browser. **Fixed:** the heading jump from h1 to h3, and turned on site-wide noindex (it was `index,follow` although the deployment says indexing is off). **Remaining:** brand fonts and colours, no skip link, footer logo link has no accessible name, the phone field defaults to the UAE flag, `/ar` has `html lang=en` and no hreflang, no Arabic font. **Speed:** first byte 93 ms, largest paint about 1.1 s, about 190 KB over 31 requests. |

## Scores
c1 3 · c2 2 · c3 1 · c4 2 · c5 1 · c6 3 · c7 1 · c8 2 · c9 3 · c10 3 · c11 1 · c12 1 · c13 2 (owner: "alright" – usable) · c14 2 · c15 2 → **29 / 45**

No zero on the deal-breaker criteria (c7, c10, c11), but c7 = 1 and c11 = 1 are weak for AGI.

## Interventions and fairness notes
- **1 intervention:** the owner created the MCP key in the admin. The agent's environment doesn't allow it to create access keys; the CMS itself would allow it.
- **Not a fresh session.** This agent had already deployed SmartSite and had read its source before the test, which may have made discovery easier than for a new agent.
- **Content was written only through MCP.** Browser reads were used only to check the live pages.

## After the test (not scored)
Following the test, SmartSite was customised in code for AGI on the same server: EN/FR/AR language trees (`/fr`, `/ar`) with right-to-left Arabic, Noto Naskh Arabic, per-language menus, an EN | FR | ع switch and hreflang; new blocks (cards, facts, testimonials, FAQ accordion with FAQ structured data); the AGI theme (navy/gold, Newsreader + Inter). The whole v2 site (68 EN + 4 FR + 12 AR pages, 66 journal articles, 144 old-site redirects) was imported. These changes address c3, c4, c7 and c12 but were made by a developer, so the scores above describe SmartSite as shipped.
