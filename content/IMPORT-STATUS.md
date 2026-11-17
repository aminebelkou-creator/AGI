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
- Legacy route inventory at `content/migration/legacy-route-inventory.csv`: 68 existing page routes and 60 news items (128 referenced JSON files), all flagged for review rather than automatic replacement.
- Human review matrix at `content/migration/page-review-matrix.csv`, assigning required reviewer roles and publication gates across the 12 core page groups.
- Detailed content review and disposition plan for all 68 legacy routes at `content/migration/route-content-review.csv`, based on inspection of the legacy page bodies and metadata.
- Proposed target navigation, site tree, CMS content types, localisation and editorial workflow at `content/strategy/proposed-information-architecture-v2.md`.
- Automated migration-plan validator at `scripts/validate_migration_plan.py`; it confirms all 68 indexed routes have a unique review decision.

## Structured content coverage

The structured export contains 36 locale records: 12 page groups × 3 locales (en-US, fr-MA, ar-MA). English remains in editorial review; French and Arabic remain in translation review. No record is approved or published.

The 12 page groups are: homepage, school, inclusive learning, Anglia Morocco, C.I.T.E., Step To books, adult learning, professional English, teacher development, proctoring, wellbeing and FAQ.

## Important distinction: core set vs full site

This is the first structured core content set, not a complete migration of every legacy website page or news item. The existing app currently contains 128 page JSON files, including 60 news article files. Its content loader reads a single English `/content/index.json` and `/content/pages/*.json` store; the en/fr/ar i18n files currently translate interface strings, not the full page corpus.

The new content export is deliberately kept separate from the legacy app content. Do not replace the legacy JSON store or route index with this 12-page core set. The integration assessment describes a safe phased approach. The 68-route review is now complete as a preliminary content audit and proposed disposition; it is not a factual/legal approval or permission to rewrite/publish.

## Deliberately not done

- No changes to `app/`, its current content loader, routes, navigation, or page JSON files.
- No WordPress/headless CMS connection or import.
- No deployment, publication, merge to main, or change to the live website.
- No claim that legal, regulatory, partner, clinical, qualification or fee statements have been approved.

## Next gates

1. Review and approve the proposed information architecture and brand boundaries.
2. Assign named content owners and subject-matter reviewers to each route and service.
3. Complete source/evidence, pricing, date, qualification, partner, safeguarding, legal and media-rights checks flagged in the route review matrix.
4. Decide the canonical routes and approve each redirect individually; no redirects have been installed.
5. Build the isolated CMS pilot and import only a small set of approved sample content.
6. Prepare a versioned locale-aware adapter and staging-only tests after content and CMS gates are met.

**Boundary:** this branch is an editorial and integration-preparation workspace. The live site and main branch remain untouched.
