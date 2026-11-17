# Current-site integration assessment

## Executive finding

The AGI repository already contains a substantial website implementation. The new structured content export must be integrated additively; it must not replace the existing content store or be treated as a ready-to-deploy CMS import.

## Observed architecture on `cms-test-smartsite`

- The React/Vite application lives in `app/`.
- The current static content index is `app/public/content/index.json`.
- Page bodies are individual JSON files under `app/public/content/pages/`, using a `{ title, markdown }` shape.
- The current loader in `app/src/lib/content.ts` fetches one `/content/index.json`, then loads `/content/pages/<file>`.
- The content index and route navigation are English-first. `app/src/i18n/locales/en.json`, `fr.json` and `ar.json` currently provide interface translations; they do not provide translated versions of every page body.
- `app/src/pages/ContentPage.tsx` renders page body content with `dir="ltr"`.
- The current index contains many route entries. The repository tree has 128 page JSON files under `app/public/content/pages/`: 68 route pages and 60 news article JSON files. The route/news inventory is recorded in `content/migration/legacy-route-inventory.csv`.

## Compatibility gap

The new `content/entries.json` is an editorial interchange format, not a drop-in replacement for the current app format:
- It groups locale variants under stable content IDs.
- It stores SEO metadata, editorial status, direction, and publication gates.
- The app expects a route-keyed index with a section and filename, then a separate `{title, markdown}` page payload.
- The app currently does not select page bodies by locale or set page-level RTL direction.

A direct copy into `app/public/content/` would risk losing route coverage, navigation metadata, legacy redirects, news content, and locale behaviour.

## Recommended target architecture

1. Keep `content/en/pages.md`, `content/fr/pages.md`, `content/ar/pages.md` and `content/entries.json` as the editorial source of truth.
2. Preserve the existing app content files during the transition.
3. Add a deterministic build/export adapter that generates a separate versioned runtime payload, for example `app/public/content/v2/{locale}/index.json` and `pages/{slug}.json`.
4. Extend routing and content loading to resolve a locale explicitly, with safe fallback to the approved English master only where policy permits.
5. Set document language and direction from the resolved locale; Arabic pages must use RTL layout, not merely RTL navigation labels.
6. Add redirects/aliases from the existing route inventory and keep all legacy pages until an owner approves retirement or consolidation.
7. Migrate the 60 news items as a separate content type with dates, media, authorship, rights and status. Do not force them into the static page model.
8. Add tests for schema validation, locale fallback, missing translations, route resolution, legacy redirects, SEO metadata, and RTL rendering.

## Proposed runtime contract

- `/content/v2/{locale}/index.json`: locale-specific route index.
- `/content/v2/{locale}/pages/{slug}.json`: `{ id, slug, locale, title, summary, markdown, seo, direction }`.
- Editorial-only fields such as `status`, `claims`, `sources`, `owner` and `publication_gates` stay in the editorial source and are not exposed publicly unless a deliberate product requirement exists.
- Only `approved` content may be exported to the public runtime payload. Current records are review-stage and therefore must not be exported for production.

## Safe implementation sequence

**Phase A — inventory:** reconcile every current route, JSON page and news item with the content manifest; identify duplicates, orphan files, outdated dates/prices, missing locale variants and high-risk claims.

**Phase B — editorial approval:** confirm owners, facts, evidence, translation quality, partner wording, school authorisations and publication gates.

**Phase C — adapter and tests:** implement a non-destructive exporter and locale-aware reader in a separate feature branch. Keep the old loader as a fallback during testing.

**Phase D — staging:** generate a preview-only build and compare route coverage, page content, links, metadata, language switching, accessibility and RTL rendering.

**Phase E — release decision:** provide a diff, test report and rollback plan for human review. Do not deploy or merge automatically.

## Current decision

No app source, routes, runtime content files, WordPress settings or production systems were changed as part of the content foundation import. The next safe unit of work is the route and legacy-content reconciliation, not a live integration.
