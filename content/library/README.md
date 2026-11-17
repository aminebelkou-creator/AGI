# AGI reusable content library

This directory contains reusable editorial modules, not page-specific copies. It is designed to feed multiple page templates, channels and language versions without duplicating the underlying content.

## Current content coverage

`reusable-content-library.json` currently contains 43 reusable modules and 129 locale variants (43 × English, French and Arabic):

- Brand positioning, promise, mission, philosophy, vision, founding story and school–home–community message.
- Founder/leadership profile, admissions journey, application records, placement assessment and fee guidance.
- Curriculum overview, grade pathways, student life, community service, parent FAQs and policy summaries.
- K–12 school, inclusive learning and Anglia examinations.
- Anglia General English levels, Business English, exam formats, CEFR, special arrangements, class formats, placement assessment, qualification recognition, C.I.T.E. and Step To resources.
- Adult learning pathway and professional/medical English.
- Examination proctoring, education consultancy, teacher development and wellbeing.
- A general contact call to action.

This is an expanded reusable core, not a complete rewrite of every v2 page, the 66 journal-index entries or the 68 legacy routes. Existing page-level drafts in `content/entries.json` remain intact and are not replaced by these modules.

## Data model

Each item has:

- `id`: stable semantic identifier, unchanged across locales and channels.
- `type`: editorial module type (brand message, programme, service, resource, CTA, etc.).
- `audiences` and `channels`: intended reuse contexts.
- `status`: editorial state of the module.
- `locales`: independently reviewable `en-US`, `fr-MA` and `ar-MA` copy.
- `fact_refs`: stable IDs in `../facts/fact-register.csv` for material claims used by the module.
- `evidence_gates`: approvals or specialist checks required before publication.

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
9. No module in the current library is approved or published. Do not treat structural validation as editorial, legal or partner approval.

## Recommended future page assembly

Example only:

- Home: `agi.brand.positioning` + `agi.brand.promise` + selected programme summaries + `agi.cta.contact`.
- School: `agi.program.school-k12` + approved admissions, curriculum, student-life and policy modules.
- Anglia: `agi.program.anglia-examinations` + `agi.program.cite` + `agi.program.step-to`.
- Professional: `agi.service.professional-english` + `agi.service.proctoring`.
- Teacher development: `agi.service.teacher-development` + the separate C.I.T.E. examination module.

This is a content-composition guide, not a route or navigation approval.

The Anglia-specific editorial findings and content decisions are documented in `../research/anglia-content-audit.md`.

## Next expansion batches

1. Grade-by-grade curriculum and subject descriptions, checked against the current academic programme.
2. Detailed Anglia exam levels, formats, exam sessions, active centres and Step To catalogue.
3. Adult diploma disclosures, current awarding-provider information and programme-specific FAQs.
4. Student-life stories, outcomes and testimonials only where evidence, consent and media rights are documented.
5. Journal/news records with source URL, publication date, event date, author, image rights, category and canonical URL; follow the reconciliation report before consolidation.

The public repository must contain only publishable editorial material and non-confidential governance metadata. Keep contracts, private correspondence, personal data, safeguarding records and internal legal opinions in access-controlled storage.
