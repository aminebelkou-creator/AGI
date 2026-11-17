# AGI reusable content library

This directory contains reusable editorial modules, not page-specific copies. It is designed to feed multiple page templates, channels and language versions without duplicating the underlying content.

## First content batch

`reusable-content-library.json` currently contains 15 reusable modules and 45 locale variants (15 × English, French and Arabic):

- Brand positioning, brand promise and school–home–community message.
- K–12 school, inclusive learning and Anglia examinations.
- C.I.T.E. and Step To learning resources.
- Adult learning pathway and professional/medical English.
- Examination proctoring, education consultancy, teacher development and wellbeing.
- A general contact call to action.

This is a first reusable core, not a complete rewrite of all 25 v2 pages, 59 journal articles or the 68 legacy routes. Existing page-level drafts in `content/entries.json` remain intact and are not replaced by these modules.

## Data model

Each item has:

- `id`: stable semantic identifier, unchanged across locales and channels.
- `type`: editorial module type (brand message, programme, service, resource, CTA, etc.).
- `audiences` and `channels`: intended reuse contexts.
- `status`: editorial state of the module.
- `locales`: independently reviewable `en-US`, `fr-MA` and `ar-MA` copy.
- `evidence_gates`: facts, approvals or specialist checks required before publication.

The JSON contract is in `../schemas/reusable-content-library.schema.json`. Validate with:

```bash
python scripts/validate_reusable_content.py
```

## Composition and reuse rules

1. A page is a composition of content modules; it should reference stable IDs rather than maintain a second copy of the same programme description.
2. A module may be reused on the homepage, programme landing page, audience page, brochure, social post or email, with channel-appropriate excerpts.
3. Reuse does not mean every context must show the full body. A future page assembler may select title, summary, body or CTA fields, but must retain the same source ID.
4. Do not put volatile facts (fees, dates, opening hours, staff roles, availability, partner status) into reusable prose as untracked literals. Use `../facts/fact-register.csv`, which records source pointers, owners, verification requirements, review dates and publication rules. Add a fact to page copy only after its status and evidence are approved; localise its display format separately.
5. Keep qualification, regulatory, partner, clinical, safeguarding and school-authorisation wording subject to the relevant evidence gate.
6. English is the editorial master for this batch. French and Arabic are localised copy, not automatic machine fallbacks; each translation remains in translation review until checked by a qualified reviewer.
7. Arabic is Modern Standard Arabic adapted for the Moroccan audience. Any Arabic presentation must set RTL direction at the rendering layer.
8. Never change an item's ID because its wording changes. Create a new ID only when the meaning or service itself becomes materially different; retain aliases when a migration requires them.
9. No item in this first batch is approved or published. Do not treat structural validation as editorial, legal or partner approval.

## Recommended future page assembly

Example only:

- Home: `agi.brand.positioning` + `agi.brand.promise` + selected programme summaries + `agi.cta.contact`.
- School: `agi.program.school-k12` + approved admissions, curriculum, student-life and policy modules.
- Anglia: `agi.program.anglia-examinations` + `agi.program.cite` + `agi.program.step-to`.
- Professional: `agi.service.professional-english` + `agi.service.proctoring`.
- Teacher development: `agi.service.teacher-development` + the separate C.I.T.E. examination module.

This is a content-composition guide, not a route or navigation approval.

## Next expansion batches

1. Institutional story, mission, vision, leadership and verified history.
2. Admissions, fees, school calendar, policies and parent resources (volatile facts separated).
3. Student life, outcomes, testimonials and media-rights-cleared stories.
4. Anglia exam levels, exam formats, centres, schedules and detailed Step To catalogue.
5. Adult diploma details, provider disclosures, consultancy partner directory and programme-specific FAQs.
6. Journal/news records with source, date, author, image rights, category and canonical URL.

The public repository must contain only publishable editorial material and non-confidential governance metadata. Keep contracts, private correspondence, personal data, safeguarding records and internal legal opinions in access-controlled storage.
