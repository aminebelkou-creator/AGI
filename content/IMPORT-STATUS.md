# Content foundation import status

**Target branch:** `cms-test-smartsite`  
**Last updated:** 17 November 2026  
**Website deployment:** none  
**Merge to main:** none

## Completed in this branch

- Editorial foundation: positioning, information architecture, editorial policy, source register, research backlog, claims register, correction backlog, Law 59.21 operational checklist and public-facing website audit.
- Human-readable English, French and Arabic content bundles covering 12 core page groups.
- Manifest and SEO metadata for all 36 page/locale combinations.
- Portable JSON Schema and a CMS-neutral structured export at `content/entries.json`.
- A lightweight validation script at `scripts/validate_content_export.py`.
- Import architecture assessment at `content/architecture/current-site-integration.md`.

## Structured content coverage

The structured export contains 36 locale records: 12 page groups × 3 locales (en-US, fr-MA, ar-MA). English remains in editorial review; French and Arabic remain in translation review. No record is approved or published.

The 12 page groups are: homepage, school, inclusive learning, Anglia Morocco, C.I.T.E., Step To books, adult learning, professional English, teacher development, proctoring, wellbeing and FAQ.

## Important distinction: core set vs full site

This is the first structured core content set, not a complete migration of every legacy website page or news item. The existing app currently contains 128 page JSON files, including 60 news article files. Its content loader reads a single English `/content/index.json` and `/content/pages/*.json` store; the en/fr/ar i18n files currently translate interface strings, not the full page corpus.

The new content export is deliberately kept separate from the legacy app content. Do not replace the legacy JSON store or route index with this 12-page core set. The integration assessment describes a safe phased approach.

## Deliberately not done

- No changes to `app/`, its current content loader, routes, navigation, or page JSON files.
- No WordPress/headless CMS connection or import.
- No deployment, publication, merge to main, or change to the live website.
- No claim that legal, regulatory, partner, clinical, qualification or fee statements have been approved.

## Next gates

1. Complete page-by-page reconciliation of the 128 legacy pages and 60 news records against the new content model.
2. Build a route/slug/locale mapping and identify duplicates, redirects, obsolete pages and content that must remain.
3. Complete claim-to-source mapping from primary evidence and assign human owners/review dates.
4. Obtain native-speaker and subject-owner review; obtain legal and partner approval where required.
5. Implement a non-destructive locale-aware adapter and tests in a separate implementation phase.
6. Run accessibility, SEO, internal-link, route, locale and build checks before any release proposal.

**Boundary:** this branch is an editorial and integration-preparation workspace. The live site and main branch remain untouched.
