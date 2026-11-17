# Legacy content reconciliation — first structural pass

**Branch:** `cms-test-smartsite`  
**Audit date:** 17 November 2026  
**Scope:** the current React application's static route and news indexes, plus the referenced page JSON files.

## Verified structural baseline

The current repository tree and indexes were inspected directly. The following counts reconcile:

| Check | Result |
|---|---:|
| Route records in `app/public/content/index.json` | 68 |
| News records in `app/public/content/news.json` | 60 |
| Referenced page JSON files | 128 |
| JSON files present under `app/public/content/pages/` | 128 |
| Missing referenced files | 0 |
| Unreferenced JSON files | 0 |
| Duplicate route keys | 0 |
| Duplicate file references | 0 |
| Duplicate news slugs | 0 |

The 68 routes are distributed across nine sections:

- Admissions: 15
- Anglia: 11
- Academics: 6
- EFL: 7
- USA: 7
- Resources: 7
- About: 4
- Special education: 4
- Programs: 7

The 60 news records span **9 January 2018 to 16 June 2026**. Historical news dates are not defects by themselves; they must remain historical and should not be silently rewritten as current announcements.

## What this proves

- Every route and news record currently listed by the app points to a file that exists.
- Every JSON file in the legacy pages directory is referenced by one of those two indexes.
- There are no structural duplicates in the route keys, content-file references or news slugs in this baseline.
- The legacy content store is internally complete at the index-to-file level.

## What this does not prove

This is a structural integrity audit, **not** a complete editorial, legal, factual, SEO, accessibility or translation approval. It does not establish that claims, prices, dates, partner relationships, qualifications, policies, images or forms are still accurate. It also does not prove that every page is linked from navigation or indexed by search engines.

## Priority editorial review queue

The next review should focus first on content that can create operational, legal, reputational or customer-expectation risk:

1. **Admissions and school policies:** fees, refunds, complaints, enrolment, attendance, academic calendar, important dates, placement, parent responsibilities and handbook.
2. **Anglia and partner claims:** exam availability, accreditation wording, C.I.T.E. training descriptions, centre network, current schedules, pricing and partner relationships.
3. **Inclusive-learning and wellbeing:** descriptions of counselling, coaching, therapy, practitioner credentials, scope of service and safeguarding boundaries.
4. **Programmes and qualifications:** adult diploma pathways, teacher sponsorship, proctoring, tutoring and any claimed awarding-body or recognition status.
5. **Conversion paths:** contact, appointment booking, document requests, forms and privacy/terms notices.

Time-sensitive titles found in the route inventory include the **2025–2026 Anglia Saturday schedule**, **Anglia class pricing**, and **2026–2027 school calendar**. These require owner confirmation before being presented as current. Do not infer that they are still valid simply because the files exist.

## Migration decisions

- Keep all 68 legacy routes and all 60 news items in the existing app until reviewed.
- Keep news as a separate content type; do not fold news posts into the 12-page core marketing bundle.
- Map legacy routes to new editorial page groups only after comparing the actual body content and intended audience.
- Treat machine-translated French and Arabic drafts as review material, not publishable translations.
- Export only explicitly approved content into a future public runtime payload.
- Preserve old URLs or prepare tested redirects only after route-by-route review.

## Reproducible check

Run:

```bash
python scripts/audit_legacy_content.py
```

The script uses only the Python standard library, reads the existing indexes and JSON files, and makes no changes. It reports missing files, duplicate references, malformed JSON, empty page bodies and unreferenced files. Unreferenced files are warnings, never automatic deletion candidates.

## Next implementation unit

Build a detailed route-by-route editorial reconciliation table that captures: audience, purpose, currentness risk, evidence required, owner, target content group, proposed action (retain, consolidate, rewrite, archive candidate) and approval status. The existing 12-page model is only the initial core; it is not a substitute for the full 68-route review.
