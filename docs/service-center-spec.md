# AGI Unified Service & Request Center
*Implementation specification · English master · 17 November 2026*

## 1. Decision and scope

American Group International (AGI) is one organization and will operate **one unified website on one canonical domain**. Anglia Morocco is a first-class section of that website, not a separate website or an external destination. The existing AGI and Anglia content, programs, forms, resources, news, and legacy URLs must be consolidated without silently dropping services.

The website is the shared digital front door for all AGI divisions and programs. The Service & Request Center is the single intake layer for all online requests.

This document supplements:
- `docs/website-content-spec.md` — page-level copy and requirements.
- `docs/rebuild-plan-v3.md` — source coverage and merged sitemap.
- `docs/content-inventory.csv` and the v3 content map — source-by-source migration.
- `docs/AI-ASSISTANT-BRIEF.md` — factual, privacy, and editorial guardrails.

## 2. One-site information architecture

The divisions below are represented as sections/program areas under the AGI brand. They are not separate sites or separate top-level domains.

1. AGI School — K–12, admissions, curriculum, student life, family resources, and school policies.
2. Anglia Examinations Morocco — exams and levels, CEFR, dates, placement, special arrangements, practice/audio, Step To books, classes, network/centres, and C.I.T.E.
3. AGI Learning Pods — learning pods and Fast Track High School.
4. AWA High School for Adults — adult diploma pathway; describe the relationship and delivery model only as supported by approved source material.
5. i-Heart / Wellbeing — ADHD coaching, play therapy, therapeutic services and counselling; retain appropriate privacy and safeguarding boundaries.
6. AGI Education Consultancy / University Pathways — education guidance, university applications, partner institutions and related enquiries.
7. American Group USA LLC — online tutoring and US-linked programs; legal/entity details remain subject to confirmation.
8. Professional and educator services — C.I.T.E./TESOL, teacher training, professional/business/medical English, proctoring, document editing, independent studies, careers and sponsorship information.

The navigation should expose audience-friendly destinations, not overwhelm visitors with a list of legal entities. Each division/program page must show its relationship to AGI and provide a relevant action.

## 3. Service Center user experience

Create one discoverable entry point labelled **Forms & Requests** / **Service Center** in the global navigation and footer. It must be reachable from every service page. The center groups actions by visitor need:

- Prospective families: apply/enroll, book a school visit, admissions enquiry.
- Current families: report absence, activity consent, feedback, payment notice, request a school document/attestation.
- Students and English learners: free level test, Anglia exam registration/enquiry, class enquiry, exam special arrangements, practice resources.
- Teachers: C.I.T.E./TESOL registration, internship and careers enquiry.
- Schools and centres: Step To book order, become an Anglia centre/representative, partnership/franchise enquiry, group training request.
- Adults and professionals: adult diploma enquiry, tutoring request/schedule, professional English/team course, proctoring, document editing and university pathways.
- General visitors: contact/general enquiry and complaint/feedback route.

Every action must have a stable deep link, a plain-language description, estimated completion time where known, required information/documents, what happens next, and a clear contact fallback.

## 4. Form registry and migration status

The current repository README documents **10 native forms plus a separate contact form** in `v2/forms.html` and `v2/contact.html`. The generated content specification refers to 11 forms, while the v3 migration plan identifies additional legacy actions including attestation and Anglia book ordering. These counts describe different scopes and must not be conflated.

### Existing native forms documented in the current site
1. Enrollment / application.
2. Book a visit / appointment.
3. Absence notice.
4. Park and outdoor activity consent.
5. Parent feedback.
6. Payment notice (never collect card details).
7. Tutor request.
8. Tutoring schedule / schedule change.
9. Academic document request.
10. General enquiry.

### Existing separate contact form
11. Contact form (name, email, phone, topic, message).

### Legacy and Anglia workflows to reconcile into the same center
12. Attestation for AGI clients.
13. Anglia Step To book order.
14. Anglia exam registration / exam-session enquiry (preserve the actual supported registration route; do not invent an online registration capability).
15. Anglia special arrangements request.
16. Anglia placement/level test.
17. Anglia centre/representative and franchise enquiry.
18. C.I.T.E./TESOL and teacher-training registration/enquiry.
19. Corporate/team training request.
20. Proctoring request.
21. Document editing request.
22. University consultancy/pathways enquiry.
23. Online tutoring and other program enquiries.

Items 12–23 are a migration/reconciliation list, **not a claim that all have an implemented native form today**. For each, inspect the source page and linked destination, capture the actual fields and destination, and decide whether to create a native form or preserve a verified external portal. No form may be declared complete based on a page title alone.

## 5. Unified email intake — required behavior

**All successfully submitted forms must generate an email to the AGI-designated central receiving mailbox.** The currently documented general contact mailbox is `americanecoleagadir@gmail.com`; confirm that it is the approved central intake address before production activation. Existing Anglia mailboxes remain valid contacts where the business owner requires them, but the website must not scatter or lose submissions.

Each submission email must include:
- Unique request reference (e.g. `AGI-2026-000123`).
- Form type and service/division.
- Source page URL and language.
- Submission timestamp (with timezone).
- Submitter's name and reply email; phone if supplied.
- All submitted fields in a readable, labelled format.
- Attachment names and safe links or attachments where supported.
- Consent/privacy acknowledgement version where relevant.
- Reply-to set to the submitter's email (never spoof the sender address).

Subject convention:
`[AGI][<DIVISION>][<FORM-TYPE>][<REFERENCE>] <short topic>`

The submitter receives an acknowledgement email containing the reference, a concise summary, expected next step, and the official contact channel. Do not promise a response time unless the relevant service page has an approved service-level statement.

The email must be sent server-side through a configured SMTP or transactional email provider. Never expose SMTP credentials, API keys, or secrets in browser JavaScript or the repository. Email delivery must be logged; transient failures must be retried, and the request must remain stored so that a failed email does not lose the submission.

## 6. Data and backend contract

The current `app/api/forms-router.ts` accepts only `contact | appointment | enrollment | consultation`, stores submissions in the database, and does not send email. The static site currently falls back to opening the visitor's email application with a prefilled message. Therefore **the promised central email workflow is not yet implemented**.

Before connecting the website forms to the API:
- Expand the form-type registry to cover all approved form types.
- Validate each form with a typed schema; do not reduce every field to unvalidated arbitrary strings.
- Persist the full payload, form version, source URL, locale, timestamp, request reference, consent metadata and attachment metadata.
- Add server-side email notification to the central mailbox.
- Add acknowledgement email to the submitter.
- Add idempotency / duplicate-submission protection.
- Add rate limiting, spam protection, input length limits, safe file-type/size validation, and malware scanning for uploads.
- Escape all user content in email templates and staff views.
- Keep payment notices separate from payment processing. Never request or store card numbers, CVV, passwords or other payment credentials. Card payments must remain on AGI's verified secure payment provider.
- Do not put sensitive health, disability, child, or safeguarding details in broad email distribution lists. For special arrangements and i-Heart enquiries, collect only the minimum necessary data, route to an authorized recipient, and use a secure restricted-access record or link rather than distributing sensitive attachments widely.
- Keep a submission record and delivery state: received, queued, sent, failed/retrying, acknowledged, assigned, resolved.
- Provide an administrative export and deletion/retention process consistent with Moroccan Law 09-08 and applicable CNDP obligations; obtain legal review before launch.

Suggested normalized request envelope:
```json
{
  "reference": "AGI-2026-000123",
  "type": "anglia-book-order",
  "division": "anglia-morocco",
  "locale": "en",
  "sourceUrl": "/anglia-books.html",
  "submittedAt": "ISO-8601 timestamp",
  "name": "Submitter name",
  "email": "submitter@example.com",
  "phone": "+212...",
  "payload": {},
  "consentVersion": "privacy-2026-01",
  "attachments": []
}
```

## 7. AI assistant integration

The assistant must use the same approved service catalogue and form registry as the website. It should:
1. Identify the visitor's goal and the correct AGI division.
2. Answer from approved service facts and the source page.
3. Ask only for fields required by the selected form.
4. Explain documents, fees, eligibility and next steps only when verified.
5. Create a structured draft/request and ask the visitor to review it before submission.
6. Submit through the same backend endpoint as the website, producing the same request reference and email workflow.
7. Never claim a request was sent unless the backend confirms success.
8. Escalate complaints, safeguarding matters, sensitive health/disability disclosures, ambiguous eligibility, and unverified claims to an authorized human.
9. Never invent prices, schedules, accreditation, legal status, outcomes, or partner relationships.

## 8. Editorial, privacy and migration safeguards

- English is the master content language; French and Modern Standard Arabic versions must be planned and linked to the same service identifiers.
- Preserve Anglia Morocco's identity within its section, including approved logo and page-specific brand accents, while retaining the unified AGI site header, footer and URL domain.
- Keep source-to-destination mapping for every crawled page. No source URL may be left unmapped; every exclusion must have a documented reason.
- Preserve journal history and approved article content; archive old announcements instead of presenting expired dates as current.
- Keep all `[TO CONFIRM]`, `[PHOTO NEEDED]`, `[SAMPLE]` and privacy holds visible to editors and blocking for launch where required.
- Never publish a child's name/photo without verified written parental consent.
- Use approved Anglia wording only. Do not claim UK Ministry of Education dependence, British Council recognition, or unsupported accreditation.
- Do not invent testimonials, team roles, office hours, prices, exam dates or legal claims.
- Preserve 301 redirects from both old domains/URL sets to the corresponding page or section on the one canonical AGI domain. Avoid blanket redirects where a specific destination exists.

## 9. Acceptance criteria

The unified Service Center is ready only when:
- Every source form/action from both sites appears in the registry with a verified destination and status.
- All implemented forms share one submission backend and request-reference format.
- Every successful submission is persisted and sends an email to the approved central mailbox.
- The submitter receives an acknowledgement with the same reference.
- Email failure does not lose a submission and is visible to administrators.
- Attachments are validated and protected.
- Sensitive requests have restricted handling.
- All forms work on mobile, support keyboard and screen readers, and display clear validation.
- All pages and forms have English/French/Arabic language behavior defined.
- The source coverage gate, link checks, content audit, privacy checks, and prelaunch checklist pass.
- No production email is enabled until the central mailbox and provider credentials are configured and tested by an authorized owner.

## 10. Immediate implementation sequence

1. Reconcile the 10 native forms + contact form against the 11-form generated spec and the legacy/Anglia workflow list above.
2. Complete the source-to-destination and form-field inventory for both crawled sites.
3. Confirm the central mailbox and routing policy with AGI; keep `americanecoleagadir@gmail.com` as the documented candidate, not a silently assumed production endpoint.
4. Extend the backend schema and `forms-router.ts` with typed form schemas and persistent request references.
5. Implement server-side email delivery, acknowledgement, retries and audit logs.
6. Convert verified legacy forms/actions into native forms or preserve verified external portals.
7. Connect all website and assistant submissions to the same endpoint.
8. Run automated tests and the complete prelaunch gates; retain the existing branch review workflow and do not deploy or merge without approval.
