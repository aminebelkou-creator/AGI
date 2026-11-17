# AGI content and CMS integration review

**Review date:** 17 November 2026  
**Repository:** `aminebelkou-creator/AGI`  
**Reviewed branch:** `cms-test-smartsite`  
**Scope:** Read-only review of the current branch's editorial data, service catalogue, application content runtime, forms API, CMS evaluation and SmartSite test record.  
**Change boundary:** This review does not authorize a merge to `main`, production deployment, live CMS import, route retirement, redirect activation or changes to customer-facing forms.

## Executive decision

The branch contains a substantial editorial foundation and a useful first service knowledge base. It is **not yet ready for a live CMS import or an AI agent to execute customer requests**.

Proceed additively. Keep the existing application and all legacy content intact. First reconcile the content contracts and evidence, then build a non-destructive content adapter and a separate request-management workflow. Do not connect a CMS to the application's operational database, and do not publish any content solely because a structural validator passes.

## 1. Verified repository baseline

| Area | Current branch evidence |
|---|---|
| Page content export | 51 records: 17 page groups × 3 locales (en-US, fr-MA, ar-MA) |
| Editorial states | 17 English records in `editorial-review`; 34 French/Arabic records in `translation-review` |
| SEO metadata | 51 rows: 17 page groups × 3 locales |
| Reusable content | 43 modules × 3 locales = 129 locale variants |
| Page compositions | 12 composition maps; all 12 contain gaps; 51 missing-content entries in total |
| Governed facts | 38 facts: 19 unverified, 5 owner-confirmation-required, 11 partner-approval-required, 2 legal-review-required, 1 specialist-review-required |
| Claims | 23 claims: 7 open, 9 hold, 3 review, 2 explicitly not publishable, and 2 with approved wording/scope |
| Legacy migration | 68 legacy page routes plus 60 WordPress posts are inventoried; 68 route decisions are present |
| Service catalogue | 25 records: 8 form workflows marked for end-to-end testing, 1 general-contact workflow needing a test, and 16 support intents needing workflow confirmation |
| Current app content | Legacy route index and 128 page JSON files (68 route pages + 60 news files) remain separate from the new editorial export |

These are repository counts, not proof of current operational availability or editorial approval.

## 2. Findings and required corrections

### F-01 — Stale documentation counts

The current data contains 51 page records and 51 SEO metadata rows, but `content/entries/README.md` still states 36 records / 12 page groups. `content/README.md` also states 36 SEO rows and refers to a 12-page core set. These statements are inconsistent with the current files and should be corrected.

### F-02 — Evidence linkage is incomplete

All 51 records in `content/entries.json` currently have empty `sources` arrays. The entries reference 22 distinct claim IDs, and the claims register contains 23 claims. The current validator checks that referenced claim IDs exist, but it does not require a source reference for every material assertion or prove that a claim is approved.

**Required:** create page-level source mappings to primary evidence; retain claim status and publication gates; keep unsupported copy in review/hold. Do not mark the export approved until evidence and owner review are complete.

### F-03 — No facts are currently verified in the fact register

The 38 fact rows are distributed across unverified, owner, partner, legal and specialist review states; none is currently marked `verified`. The register is valuable because it identifies owners and evidence requirements, but fees, dates, hours, response promises, qualification status, partner roles and service availability must remain blocked from current customer-facing claims until confirmed.

### F-04 — Reusable library is not yet a complete page assembly

The reusable library has 43 modules, while the 12 page-composition maps collectively identify 51 missing-content entries. Every composition has at least three missing items. This is a clear work queue, not a reason to duplicate text or silently treat missing modules as complete.

**Required:** resolve the missing-content list page by page; add modules only where a real content gap exists; retain stable module IDs and fact references.

### F-05 — Service catalogue and forms specification do not yet align

The knowledge base describes 11 named form workflows, but the machine-readable service catalogue currently has only 8 `FORM-xx` rows. The catalogue does not currently include the tutor request, tutor scheduling and document-request entries as distinct form records. The remaining 16 `SUP-xx` records are support intents marked `needs_workflow_confirmation` and `hold`.

**Required:** reconcile the 11 specified forms against the 25-row catalogue and the actual live form destinations. Preserve canonical IDs; do not invent URLs or claim that an external form works until it has been tested end to end.

### F-06 — Current application form API is a storage endpoint, not a request-management system

The inspected `FormPage.tsx`, `forms-router.ts` and `db/schema.ts` show four generic submission types: `contact`, `appointment`, `enrollment` and `consultation`. The API inserts a record and returns an ID. The inspected implementation does not establish email delivery, customer acknowledgement, staff assignment, workflow status, attachment handling, payment reconciliation, document issuance, or a customer-facing status lookup.

**Required:** design a dedicated request domain before expanding the form UI. At minimum it needs canonical service/form IDs, validated per-form schemas, consent and data-minimisation rules, request references, immutable event/audit history, idempotent submission, spam/rate protection, controlled attachment handling, notification retries, human assignment/escalation and status transitions. A submission must not be described as completed unless the backend confirms it.

### F-07 — Runtime content and localisation gap

The inspected application loader reads `/content/index.json` and `/content/pages/{file}`; it does not select the new structured content by locale. The inspected `ContentPage.tsx` renders the article body with `dir="ltr"`. Existing interface translations do not prove that all page bodies have language variants or correct RTL rendering.

**Required:** build a separate, deterministic, versioned export adapter. Generate locale-specific runtime indexes and page payloads only from approved records. Resolve locale, document `lang`, `dir`, SEO canonical/hreflang and safe translation fallback together. Keep the current loader as fallback until route, language and visual regression tests pass.

### F-08 — CMS test evidence and CMS recommendation need reconciliation

The SmartSite result records a score of 29/45 for SmartSite 4.0.2 as tested, with weak multilingual/RTL and publish/export scores. It separately describes later code customisations and a large import after the scored test. Those later interventions were not part of the scored result and should not be treated as independently accepted product capabilities.

The architecture evaluation recommends an isolated Strapi 5 Community pilot, with Payload as the alternative. The SmartSite report describes a Payload-based deployment. These are not necessarily contradictory: one is a candidate recommendation and one is a customised pilot. But there is no documented, apples-to-apples retest showing which implementation now meets AGI's requirements.

**Required:** preserve the original score; run a fresh, controlled retest of the customised SmartSite/Payload build and compare it with the isolated Strapi pilot using the same test kit. Verify backup/restore, Arabic RTL, EN/FR/AR language trees, editorial roles, revision-safe writes, media rights, static/export strategy, accessibility, security updates and operational cost. Do not select a production CMS until the comparison is recorded and approved.

## 3. Target integration architecture

Keep four layers separate:

1. **Editorial source:** Markdown bundles, `entries.json`, reusable content library, facts, claims, sources, privacy and approval metadata.
2. **CMS/editorial interface:** selected only after the controlled pilot; stores editorial workflow and media metadata. Use a dedicated database and least-privilege credentials.
3. **Public content delivery:** a versioned read-only API or generated static payload. Export approved records only; do not expose internal evidence notes, personal data or editorial-only fields.
4. **Request and customer-service system:** separate from the CMS. It owns submissions, reference IDs, status, consent, routing, notifications, attachments, audit trail and human handoff. The AI assistant reads approved knowledge and may create a request only through an authorized, validated endpoint.

The CMS must not become the system of record for payments, student records, safeguarding cases or operational request status unless a separately approved architecture explicitly assigns that responsibility.

## 4. Implementation sequence

### Phase 0 — Content baseline and governance
- Correct stale documentation counts.
- Reconcile page manifest, SEO rows, 51 structured records and 43 reusable modules.
- Map sources and claim IDs to each material statement.
- Confirm fact owners and review dates; do not fabricate verification.
- Resolve all 51 page-composition gaps or explicitly defer them with reasons.
- Preserve the legacy 68 routes and 60 news records.

### Phase 1 — CMS decision gate
- Retest the customised SmartSite/Payload build with a fresh agent session.
- Run the same test kit against an isolated Strapi 5 Community pilot.
- Record licensing, database, backup/restore, localisation, editor usability, agent/MCP reliability, accessibility, export and operational requirements.
- Make a documented human decision; no production database connection during the pilot.

### Phase 2 — Non-destructive content adapter
- Define a versioned runtime contract for locale-specific page indexes and page bodies.
- Export approved records only.
- Preserve legacy URLs, route metadata, news, media provenance and redirects.
- Add automated checks for missing translations, invalid claim/source refs, unsafe fallback, route coverage, SEO and RTL.
- Keep the existing application content loader available as rollback.

### Phase 3 — Unified Service & Request Center
- Reconcile the 11 form specifications with the service catalogue and actual form endpoints.
- Assign a canonical service ID, owner, privacy class, required fields and next-step policy to each workflow.
- Implement secure submissions, acknowledgement, reference ID, status history, staff routing, notification retries and human handoff.
- Add attachments only for approved workflows and storage controls.
- Confirm the central receiving mailbox and operational owners before enabling production notifications.
- Keep payment, student records, health and safeguarding workflows behind appropriate human/security controls.

### Phase 4 — AI customer-service integration
- Retrieve approved knowledge by service ID, language and publication state.
- Let the assistant explain, prepare and route; require explicit customer confirmation before creating a request.
- Do not accept passwords, payment-card data, one-time codes or unnecessary sensitive student/health information in chat.
- Do not claim a booking, payment, admission, document issue or submission succeeded without a trusted system response.
- Provide a human escalation route for complaints, safeguarding, privacy, payments and exceptions.

### Phase 5 — Staging acceptance
- Compare all 68 legacy routes and 60 articles with the proposed destinations.
- Test EN/FR/AR, Arabic RTL, mobile layouts, accessibility, metadata, internal/external links and redirects.
- Test each form end to end in a non-production environment.
- Verify email delivery, retries, duplicate prevention, reference IDs, status transitions, attachment access and audit logs.
- Obtain editorial, legal, partner, safeguarding, translation and operational approvals before any release decision.

## 5. Release gates

No CMS import or public release until all are true:

- [ ] Every published page has an owner, approver, source and current review date.
- [ ] All material facts and claims have evidence and the required approval state.
- [ ] All translations have been reviewed against the approved English master.
- [ ] Arabic page body, navigation, forms and document metadata render RTL correctly.
- [ ] Only approved content is present in the public runtime payload.
- [ ] Legacy route coverage and redirect decisions are reviewed and tested.
- [ ] Every public form is verified end to end, with correct privacy notice and consent.
- [ ] Customer acknowledgement, reference ID, notification and human-routing paths work.
- [ ] Backup/restore, security, access control, logging and rollback are tested.
- [ ] Human release approval is recorded.

## 6. Immediate branch actions completed by this review

- This review document is added as an additive architecture/governance artifact.
- Stale record counts in the two content README files are corrected to match the current repository data.
- No application source, live form, database, CMS deployment, DNS, production site or `main` branch is changed.

## Source files reviewed

- `content/entries.json`
- `content/manifest.csv`
- `content/seo/metadata.csv`
- `content/library/reusable-content-library.json`
- `content/library/page-compositions.json`
- `content/facts/fact-register.csv`
- `content/governance/claims-register.csv`
- `content/knowledge-base/service-catalogue.csv`
- `content/knowledge-base/forms-and-customer-service.md`
- `content/architecture/cms-evaluation.md`
- `content/architecture/current-site-integration.md`
- `docs/cms-test-kit/results/smartsite.md`
- `app/src/lib/content.ts`
- `app/src/pages/ContentPage.tsx`
- `app/src/pages/FormPage.tsx`
- `app/api/forms-router.ts`
- `app/db/schema.ts`
- `.github/workflows/content-validation.yml`

**Validation note:** the workflow definition and validator scripts were inspected, but this review did not claim that a new CI run or production end-to-end test had passed.
