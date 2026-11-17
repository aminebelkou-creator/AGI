# AGI multilingual content library

This directory is the CMS-independent editorial source for the future AGI website. It is additive to the existing site and does not replace v2/, docs/ or the historical WordPress export.

## Editorial languages
- en/pages.md — English master (US English).
- fr/pages.md — French localisation for Morocco.
- ar/pages.md — Modern Standard Arabic, adapted to Moroccan educational terminology; right-to-left.
- Page boundaries use stable markers such as <!-- page: homepage -->. The marker value is the slug and is consistent across locales.

## Current coverage
The initial core library contains 12 page groups in three locales (36 locale-page entries): homepage, school, inclusive learning, Anglia Morocco, C.I.T.E., Step To books, adult learning, professional English, teacher development, proctoring, wellbeing and FAQ.

See manifest.csv for the page/locale inventory and current editorial state. The seo/metadata.csv file contains draft title and meta-description suggestions for all 36 locale-page entries.

## Publication workflow
- editorial-review: English master awaiting AGI subject-owner review.
- translation-review: translated copy awaiting native-speaker review against the approved English master.
- legal-review: legal, regulatory, qualification or consumer-facing claim awaiting appropriate review.
- partner-approval: partner-controlled names, logos, credentials or claims awaiting written approval.
- approved: all relevant reviews complete; ready for CMS import.
- published: deployed and checked on the live website.
- archived: superseded content retained for history.

Never mark a page approved or published based only on this initial migration.

## Content safety
- Do not invent fees, dates, staff biographies, outcomes, authorisations, accreditation or testimonials.
- Keep AGI's role distinct from awarding bodies and partners.
- Do not state that all Anglia examinations are Ofqual-regulated. The wording in the Anglia page is deliberately limited to the four highest General English qualifications as described by Anglia.
- C.I.T.E. is an Anglia examination; do not describe it as a teaching licence or standalone teaching qualification.
- Adult diploma, clinical/wellbeing, inclusive-support and proctoring claims require provider, role, qualification, availability and safeguarding checks.
- Treat school authorisation, approved grades, foreign-education permissions, fee schedules and contracts as mandatory publication gates.
- Obtain written consent for identifiable student images, stories and testimonials.

## CMS portability
The Markdown bundles are the human-readable master. The JSON Schema in schemas/ defines the target structured entry shape. A future importer can split each bundle on page markers and create one content entity per slug and locale. Keep content IDs stable across translations.

## Public repository boundary
Only website copy and non-confidential editorial rules belong here. Internal legal opinions, contracts, personal data, safeguarding records, credentials, private partner correspondence and unredacted audit evidence must be stored in an access-controlled private location, not this public repository.

## Source and limitations
This first migration batch is based on the AGI Multilingual Content Foundation v3 editorial package and public-facing source research. It is a content draft, not a legal opinion, regulatory approval, accreditation audit or proof that every described service is currently available.

## Structured export and website integration

- `entries.json` is the CMS-neutral structured export (36 records, 12 page groups × 3 locales).
- `entries/README.md` documents the record model and review-state boundaries.
- `schemas/content-entry.schema.json` describes the portable entry shape.
- `../scripts/validate_content_export.py` checks the structured export using Python's standard library.
- `architecture/current-site-integration.md` explains why the export is not a drop-in replacement for the current React app content store and defines a non-destructive migration path.
- `migration/legacy-route-inventory.csv` inventories all 68 current page routes and 60 news items for reconciliation.
- `migration/page-review-matrix.csv` identifies the subject-owner roles and evidence gates for each core page group.
- `IMPORT-STATUS.md` records scope, completed work and remaining gates.

The current app has its own legacy route index and 128 page JSON files (including 60 news items). The new 12-page core set does not replace those files. Production export must include only approved records; none of the current records is approved or published.

## Architecture evaluation

- [Headless CMS evaluation](architecture/cms-evaluation.md): recommends an isolated Strapi 5 Community proof of concept, with Payload as the alternative. No CMS has been deployed or selected for production.
- [Current-site integration assessment](architecture/current-site-integration.md): documents the non-destructive migration approach.

## Route review and target site structure

- [68-route content review](migration/route-content-review.csv)
- [Proposed information architecture v2](strategy/proposed-information-architecture-v2.md)
- [Migration review validator](../scripts/validate_migration_plan.py)

## Reusable content layer

The page-oriented export above remains intact. A complementary modular library has now been added for content that should be reused across multiple pages and channels:

- [Reusable content library](library/README.md): content IDs, composition rules, localisation and expansion plan.
- `library/reusable-content-library.json`: 15 semantic modules × 3 locales (45 locale variants) covering brand messages, programme/service descriptions, resources and CTAs.
- `library/page-compositions.json`: seven initial page composition maps that reference reusable module IDs and expose missing content.
- `schemas/reusable-content-library.schema.json`: portable data contract for the modular library.
- `../scripts/validate_reusable_content.py`: standard-library validator for IDs, locale completeness and editorial states.
- `facts/fact-register.csv`: 22 volatile or material claims with source pointers, owners, verification requirements and publication rules.
- `../scripts/validate_fact_register.py`: checks fact IDs, required evidence/ownership fields and verification dates.

Use the page entries for page-level narrative drafts; use the reusable library for shared semantic modules. Do not copy the same programme description into multiple pages. Compose pages by referencing stable module IDs. Volatile facts such as fees, dates, opening hours, staff roles and availability are tracked in `facts/fact-register.csv`; they must be verified and date-stamped before reuse. The register validator is `../scripts/validate_fact_register.py`.

All new modules remain in editorial/translation review. Validation checks structure only; it does not approve the content.
