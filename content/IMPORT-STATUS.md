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
- A first reusable multilingual content library at `content/library/reusable-content-library.json`: 15 semantic content modules × 3 locales (45 locale variants).
- Reusable content schema at `content/schemas/reusable-content-library.schema.json`, authoring/composition guide at `content/library/README.md`, and validator at `scripts/validate_reusable_content.py`.
- Seven machine-readable page composition maps at `content/library/page-compositions.json`, connecting page-level drafts to reusable modules by stable ID and listing content gaps.
- Governed fact register at `content/facts/fact-register.csv`: 23 material or volatile claims from v2, each with a source pointer, owner, evidence requirement and publication rule. Reusable modules link to relevant fact IDs, and the module validator checks reference integrity. A validator at `scripts/validate_fact_register.py` checks register completeness and verification-date requirements.
- CI workflow extended to validate the reusable content library alongside the existing page export, legacy inventory and migration plan.
- Import architecture assessment at `content/architecture/current-site-integration.md`.
- Legacy route inventory at `content/migration/legacy-route-inventory.csv`: 68 existing page routes and 60 news items (128 referenced JSON files), all flagged for review rather than automatic replacement.
- Human review matrix at `content/migration/page-review-matrix.csv`, assigning required reviewer roles and publication gates across the 12 core page groups.
- Detailed content review and disposition plan for all 68 legacy routes at `content/migration/route-content-review.csv`, based on inspection of the legacy page bodies and metadata.
- Proposed target navigation, site tree, CMS content types, localisation and editorial workflow at `content/strategy/proposed-information-architecture-v2.md`.
- Automated migration-plan validator at `scripts/validate_migration_plan.py`; it confirms all 68 indexed routes have a unique review decision.

## Structured page content

The page-oriented export contains 36 locale records: 12 page groups × 3 locales (en-US, fr-MA, ar-MA). English remains in editorial review; French and Arabic remain in translation review. No record is approved or published.

The 12 page groups are: homepage, school, inclusive learning, Anglia Morocco, C.I.T.E., Step To books, adult learning, professional English, teacher development, proctoring, wellbeing and FAQ.

## Reusable content coverage

The modular library is a complementary layer, not a replacement for the 12 page narratives. Its first batch covers brand positioning and pillars, K–12, inclusive learning, Anglia examinations, C.I.T.E., Step To resources, adult learning, professional English, proctoring, education consultancy, teacher development, wellbeing and a general contact CTA.

Page templates should compose modules by stable IDs instead of copying the same programme/service description into several pages. Volatile facts (fees, dates, hours, staff roles, availability and partner status) still need a separately governed fact register with source, owner, verification date and review/expiry date before being embedded or reused.

## Important distinction: core set vs full site

This is the first structured content set, not a complete migration of every v2 page, every legacy route or every news item. The existing app currently contains 128 page JSON files, including 60 news article files. The current v2 static site and the old WordPress export remain source material for subsequent content reconciliation.

The new content export and reusable library are deliberately separate from the legacy app content. Do not replace the legacy JSON store or route index with these first content batches. The 68-route review is a preliminary content audit and proposed disposition; it is not factual/legal approval or permission to rewrite/publish.

## Deliberately not done

- No changes to `app/`, its current content loader, routes, navigation, or page JSON files.
- No WordPress/headless CMS connection or import.
- No deployment, publication, merge to main, or change to the live website.
- No claim that legal, regulatory, partner, clinical, qualification or fee statements have been approved.
- No automatic publication based on schema or CI validation.

## Next content work

1. Reconcile the complete v2 page copy against the legacy WordPress export and the new reusable modules, identifying keep/merge/rewrite/archive decisions.
2. Verify and date-stamp the 22 existing fact-register entries; add primary evidence and review/expiry dates. Expand the register as new material claims are discovered.
3. Expand the reusable library with institutional story, mission/vision, admissions, parent policies, student life, approved testimonials, detailed Anglia levels and news/article records; extend page composition maps as those modules are reviewed.
4. Create page compositions that reference modules, then compare them against v2 page narratives to avoid losing useful detail.
5. Assign content owners and complete subject-matter, legal, partner, safeguarding, rights and translation reviews.
6. Only then prepare CMS import and staging-only previews.

**Boundary:** this branch is an editorial and content-architecture workspace. The live site and main branch remain untouched.
