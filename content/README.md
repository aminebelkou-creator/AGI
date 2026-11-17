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
