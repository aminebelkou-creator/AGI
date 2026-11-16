# AGI Content Foundation

This directory is the CMS-independent editorial source for the future AGI website. It is deliberately separate from the current website implementation in `v2/`, the earlier application in `app/`, and the source exports in `data/`.

## Principles
- English (`en-US`) is the master language; French (`fr-MA`) and Modern Standard Arabic (`ar-MA`) are linked localisations.
- Stable content IDs connect translations, claims, media, programmes and related pages.
- Content status is explicit. A draft is not publication-ready merely because it exists in Git.
- Legal, accreditation, partner, safeguarding, fee and qualification claims require evidence and named approval.
- Dynamic information (fees, dates, contacts, availability, staff roles) must have an owner and review/expiry date.
- This repository is the source of truth for authored content; the future CMS or website consumes it.

## Structure
- `en/`, `fr/`, `ar/`: locale-specific page content.
- `strategy/`: positioning and information architecture.
- `governance/`: editorial policy, claims and publication controls.
- `schemas/`: portable content data contracts.
- `sources/`: source register and evidence references.
- `research/`: internal research and audit material; not website copy.
- `media/`: media register and rights/consent metadata (assets are added only when rights are confirmed).

## Current import
The first import establishes the three homepage language variants and the core editorial architecture. The wider page drafts and v3 research supplement remain in the separately supplied `AGI_Multilingual_Content_Foundation_v3.zip` and should be migrated into this structure in subsequent content batches. Existing comprehensive website content remains in `v2/`, `docs/` and `data/`; do not overwrite it.

## Status vocabulary
`draft`, `subject_review`, `legal_review`, `partner_approval`, `approved`, `scheduled`, `published`, `expired`, `withdrawn`.

## Before publication
1. Resolve P0 items in the website correction backlog.
2. Confirm school authorisation, approved designation and foreign-curriculum permissions with AREF and Moroccan counsel.
3. Reconcile fees, dates, contracts and refund terms against current approved documents.
4. Verify partner/awarder roles and all accreditation wording.
5. Confirm wellbeing scope, provider credentials and safeguarding/referral procedures.
6. Review EN master, then FR and AR; verify Arabic RTL rendering.
7. Publish only content whose page status and every referenced claim are approved.

See the repository root README for the current site/build workflow. This directory does not change or deploy the website.
