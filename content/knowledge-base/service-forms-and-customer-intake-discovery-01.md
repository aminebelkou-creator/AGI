# AGI Service, Forms & Customer-Request Knowledge Base — Discovery 01

**Repository:** `aminebelkou-creator/AGI`  
**Working branch:** `cms-test-smartsite`  
**Evidence snapshot:** `data/export/AGI_Website_Content_Export.json` (generated 2026-08-21)  
**Status:** Discovery inventory; not operationally verified; not approved for public publication.

## 1. Purpose

This inventory treats every form, application, appointment request, payment request, consent, feedback channel and document submission as an operational service entry point. It is a foundation for the AGI website, a structured knowledge base, and a future AI customer-service assistant.

A form is not merely a URL. The knowledge base must describe:
- the user intent and service requested;
- who may submit it and on whose behalf;
- required and optional information;
- required attachments and consent;
- the receiving team and responsible owner;
- what happens after submission;
- expected acknowledgement and processing time (only when verified);
- status tracking, correction, cancellation and escalation;
- privacy classification, retention and access controls;
- fallback channel if the form fails.

## 2. Forms discovered in the AGI export

The records below are extracted from the WordPress content export. External URLs and embedded shortcodes have **not** been tested. Availability, ownership, current fields, recipient inbox, integrations and response times remain to be confirmed.

| ID | Legacy page / form | Purpose stated in source | Form technology / destination | Status |
|---|---|---|---|---|
| F-001 | `/forms` — Register for a Program / Enrollment Application | Register for an academic programme, extracurricular activity or workshop | Omella: https://omella.com/shzpk | Found in export; verify live form, scope and duplicate listing |
| F-002 | `/forms` — Absence Request | Notify administration of student absence or late arrival; page says submit before 9 AM on the day | Omella: https://omella.com/29e5p | Found in export; confirm current attendance process and cut-off |
| F-003 | `/forms` — Payment Request Form | Submit tuition, service fees or programme costs | Omella: https://omella.com/ti26c | Found in export; confirm payment purpose, methods, reconciliation and finance owner |
| F-004 | `/forms` — Microschool Park Consent | Parent/guardian consent for park visits and outdoor microschool activities | Omella: https://omella.com/eivv0 | Found in export; confirm whether activity is current and consent wording |
| F-005 | `/forms` — Tutor Request | Request one-to-one academic tutoring | Omella: https://omella.com/zcy7u | Found in export; source claims matching within 48 hours — verify before reuse |
| F-006 | `/forms` — Tutor Scheduling Form | Choose preferred times, subjects and session frequency for tutoring | Omella: https://omella.com/x6trk | Found in export; confirm whether new requests or existing-client scheduling |
| F-007 | `/forms` — Parent Feedback Form | Submit parent experience, suggestions or concerns | Omella: https://omella.com/e8x0m | Found in export; source says reviewed weekly — verify owner and SLA |
| F-008 | `/apply` — Schedule Your Free Consultation | Request an education consultancy consultation | WordPress Ninja Forms shortcode `ninja_form id='1'` | Embedded form identified; verify fields, routing and whether “free” still applies |
| F-009 | `/admissions/document-request` — Document Request Form | Request documents; exact request types not visible in export | WordPress Forminator shortcode `forminator_form id="2977"` | Embedded form identified; inspect live form and document fulfilment workflow |
| F-010 | `/book-appointment` — Book an Appointment | Request an appointment; page asks user to fill information and says AGI will confirm | Embedded form not preserved in export | Incomplete extraction; inspect live page and form provider |
| F-011 | `/admissions` — Admission application / supporting documents | Apply for school admission; source refers to application, interview, supporting records and PDF documents | Images / downloadable or offline forms referenced; no stable form endpoint captured | Legacy process described; current workflow and forms must be confirmed |
| F-012 | `/usa` — Online Teacher Registration / Information Form | Collect teacher contact details, ID, degree information, subject areas and PDF documents | Static form content in export; asks applicant to email `AgiAngliama@gmail.com` | Do not treat as live US operation; confirm entity, programme and recipient before use |
| F-013 | `/partnerships` — Employee Application AGI Agadir | Employment application; source form includes identity, contact, work history and education | Static legacy form content; no live form endpoint captured | Sensitive-data risk; requires HR/legal/privacy review and replacement |
| F-014 | `/partnerships` — Teacher / Learning Pods / partnership interest | Express interest in teaching, educational assistant, administrative work, Learning Pods or partnerships | Page describes email applications to `americanecoleagadir@gmail.com`; no dedicated structured form URL captured | Several intents are conflated; split into separate verified request types |
| F-015 | `/cite` and `/anglia/cite-teacher-training` — C.I.T.E. enquiry / registration | Ask about C.I.T.E. and examination registration | Legacy copy references Anglia online enquiry form; local registration link is a placeholder | Do not imply AGI issues the qualification; verify official current registration path |
| F-016 | `/about/partners-network` and `/usa/education-consultancy` — Apply / consultation links | Apply or schedule a consultation | Links point to legacy `/applyform` | Resolve destination and intent; avoid dead or ambiguous links |
| F-017 | `/admissions/handbook` — Absence form / student and family information | Parent/student administration and attendance | Handbook refers to an absence form and annual updates; no live endpoint captured | Verify current parent portal/form and data governance |

### Important observations

1. The `/forms` page lists seven operational forms, but the enrolment form is also repeated as the “Register for a Program” CTA. It should be represented once in the canonical catalogue, with multiple page placements if needed.
2. The `/forms` page makes strong claims such as “Encrypted Submission Environment”, “100% Protected Submission Portal”, “7+ Active Forms”, “24/7 Secure Access” and “<3m Average Completion Time”. These are **unverified marketing claims**, not evidence of technical controls or measured performance. Do not expose them as facts until the platform, security controls and metrics are verified.
3. The legacy export contains at least three different form mechanisms: Omella external forms, Ninja Forms, and Forminator, plus static/email-based application instructions. The future knowledge base must not assume one common submission pipeline.
4. Some pages refer to an appointment or consultation without exposing the actual embedded form in the export. A live-site inspection is needed.
5. The source says the tutor request is matched within 48 hours and parent feedback is reviewed weekly. These are service-level commitments and must be confirmed before the assistant repeats them.
6. The absence form's “before 9 AM” instruction may be a time-sensitive operational rule. Confirm whether it still applies and how late/urgent notices are handled.
7. The old employee form includes highly sensitive and potentially unnecessary fields (including social security number and driver's licence details). Do not reproduce these fields in a new Moroccan recruitment form without a documented lawful purpose, data-minimisation review and legal approval.
8. The USA page contains an announcement of an upcoming extension and a teacher form. This export does not establish that AGI USA is currently operational. Keep the route and any US service claims on HOLD until verified.
9. Anglia/C.I.T.E. links must be aligned with current official Anglia registration and assessment processes. C.I.T.E. must not be described as a standalone teaching licence or TEFL/TESOL qualification.

## 3. Service catalogue: user intents to support

The public website and knowledge base should provide one canonical service record for each of the following. A listed intent is a discovery target, not proof that the service is currently active.

### A. School and family services
- Request information about the school and available grade levels.
- Ask about admission eligibility and placement.
- Book a school visit or admissions meeting.
- Start an admission application.
- Ask which documents are required.
- Submit or correct supporting documents.
- Request a document from the school.
- Notify absence or late arrival.
- Ask about attendance, homework, school calendar and student life.
- Request tutoring or academic support.
- Schedule or change tutoring.
- Submit parent feedback, a concern or a complaint.
- Ask about payment, fees, invoices or payment allocation.
- Submit activity-specific consent.
- Ask about media/photo consent or request removal of an image.

### B. Anglia Morocco and English assessment
- Ask which Anglia examination or level may be suitable.
- Understand the General English step structure.
- Ask about Business English examinations.
- Ask about C.I.T.E. for teachers, without overstating its status.
- Ask about CEFR levels and how they relate to Anglia examinations.
- Ask about exam format, registration, candidate requirements and results.
- Ask about examination dates, fees, venues and availability.
- Ask about learning materials / Step To books.
- Ask about becoming a partner, centre or local representative.
- Ask about Learning Pods, teacher participation or educational partnerships.

For exam dates, fees, availability, local centres, registration and recognition, the assistant must use current approved source records or hand off to the Anglia team. Historical web copy is not sufficient.

### C. Professional learning and education services
- Enquire about professional English or business English.
- Enquire about English for healthcare / professional contexts.
- Enquire about teacher development or training.
- Enquire about proctoring / examination administration.
- Enquire about adult learning or diploma pathways.
- Enquire about education consultancy or university pathways.
- Enquire about Learning Pods.
- Enquire about inclusive learning support.

Every pathway needs a clear issuer/provider statement, eligibility, delivery mode, current availability, costs, outcome, and limitations. Do not imply AGI awards an external provider's qualification.

### D. Partnerships, recruitment and institutional enquiries
- Apply for an advertised job.
- Register interest as a teacher or educational assistant.
- Propose a school, centre or institutional partnership.
- Enquire about Anglia partnership / franchise arrangements.
- Offer a Learning Pod or local delivery proposal.
- Submit a media, event or community collaboration request.
- Submit a supplier or general business enquiry.

Employment, partnership and franchise requests should be separate flows, with different data requirements and responsible owners.

## 4. Required canonical form record (knowledge-base schema)

Every form should be represented as a structured record with these fields:

| Field | Meaning |
|---|---|
| `form_id` | Stable internal identifier (e.g. F-001) |
| `service_id` | Canonical service the form supports |
| `display_name` | Approved name in EN / AR / FR |
| `purpose` | What the form is for, in plain language |
| `audience` | Parent, student, adult learner, candidate, teacher, partner, staff |
| `eligibility` | Who can submit; any restrictions |
| `required_fields` | Minimum necessary data |
| `optional_fields` | Optional data, clearly labelled |
| `attachments` | Required file types, size limits and alternatives |
| `consents` | Specific consent and acknowledgement text |
| `submission_channel` | Omella, embedded form, portal, email, in person |
| `canonical_url` | Current verified destination |
| `receiving_team` | Responsible department / mailbox |
| `workflow` | Triage, acknowledgement, review, decision, completion |
| `status_values` | Received, incomplete, in review, awaiting user, accepted, declined, completed, cancelled |
| `service_level` | Verified acknowledgement / processing target; otherwise null |
| `follow_up_method` | How the applicant receives updates |
| `correction_or_cancel` | How to amend or withdraw a submission |
| `escalation_rule` | When a human employee must take over |
| `data_classification` | Public, internal, confidential, sensitive |
| `retention_rule` | Approved retention period and deletion owner |
| `source_evidence` | Source URL, document or owner confirmation |
| `last_verified_at` | Date of last operational verification |
| `status` | Draft, evidence-needed, tested, approved, retired |

## 5. Customer-service workflows the AI must understand

The assistant should classify a message into an intent, ask only for the minimum missing information, then either provide a grounded answer, direct the user to the correct form, or create a human handoff.

### Example: school admission
1. Identify whether the request concerns school admission, adult learning, Anglia examinations or another service.
2. Ask the learner's age / target grade only if necessary and appropriate.
3. Explain the currently approved admission process.
4. Offer a visit or consultation request.
5. Direct the family to the verified admission form.
6. Explain which documents are required using the current checklist.
7. Never promise admission, placement, price or start date.
8. Record the request and hand off any eligibility, safeguarding, special educational needs or fee exception.

### Example: absence notification
1. Identify the student and date through a secure channel; do not request sensitive information in public chat.
2. Direct the parent to the current absence form.
3. If the form is unavailable or the absence is urgent, provide the verified school-office fallback.
4. Do not expose student records or confirm receipt unless the form system provides that status.

### Example: payment request
1. Distinguish fee enquiry, invoice request, payment link, proof of payment and payment dispute.
2. Do not collect full card details, banking passwords or payment credentials in chat.
3. Send only a verified payment link.
4. Route reconciliation, refund and disputed transactions to finance.
5. The assistant must not claim that payment has been received unless a trusted payment integration confirms it.

### Example: Anglia examination enquiry
1. Identify exam family / purpose and candidate level if known.
2. Explain only facts supported by current official Anglia sources and approved local operating details.
3. Treat dates, fees, seats, venues and candidate registration as live operational data, not static FAQ text.
4. Link to the correct official or authorised registration route.
5. Escalate uncertain eligibility, special arrangements, complaints and result disputes to the Anglia team.

### Example: tutor request
1. Distinguish a new tutoring enquiry from scheduling an existing tutor.
2. Ask subject, learner level, preferred format and availability only when needed.
3. Send to the verified request form.
4. Do not promise tutor matching or a 48-hour response until the service level is confirmed.

### Example: recruitment / partnership
1. Classify job application, teacher interest, Learning Pod proposal, Anglia centre partnership or general institutional partnership.
2. Use a dedicated form for each path.
3. Do not ask for national identity, criminal-record documents, social security numbers or degree scans in a general first-contact form.
4. Provide a secure, restricted upload channel only after HR / partnership review.
5. Human review is mandatory; AI must not make recruitment or partnership decisions.

## 6. AI customer-service operating rules

- **Grounded answers only:** answer from approved knowledge records, not unreviewed legacy pages.
- **Source traceability:** every operational answer should carry an internal source ID and last-verified date.
- **Freshness:** fees, dates, availability, exam sessions, office hours and response times require expiry dates and periodic review.
- **No false completion:** never say a form was submitted, a payment received, a booking confirmed or a request accepted unless an integrated system confirms it.
- **No sensitive data in chat:** route identity documents, student records, health information, payment proofs and recruitment attachments to approved secure forms.
- **Human handoff:** safeguarding, student welfare, complaints, refunds, payment disputes, disability accommodations, legal matters, privacy requests, exam appeals and uncertain eligibility must go to a human.
- **Language:** support English, Arabic and French; preserve the original request and avoid changing names, IDs or document details during translation.
- **Minors:** use parent/guardian workflows for children; minimise personal data and never expose one student's information to another family.
- **Consent:** distinguish consent to process an enquiry from consent to marketing, photography, video or publication.
- **No unsupported promises:** do not invent response times, acceptance, results, qualifications, accreditation, availability or guarantees.

## 7. Priority verification checklist

### P0 — before public use or AI routing
- [ ] Open and test all seven Omella URLs; record owner, fields, confirmation page, notifications and current availability.
- [ ] Confirm whether `/forms` is the current production page or a draft/new portal.
- [ ] Test Ninja Forms ID 1 and Forminator ID 2977 on the live/staging environment.
- [ ] Identify the actual embedded form on `/book-appointment`.
- [ ] Confirm the current school admission application and document checklist.
- [ ] Confirm who receives each form and who is the accountable service owner.
- [ ] Confirm the absence deadline and fallback process.
- [ ] Confirm the payment workflow, payment provider and finance reconciliation process.
- [ ] Confirm privacy notice, consent wording, retention, access permissions and data processors for Omella / WordPress plugins.
- [ ] Remove or substantiate claims about encryption, 100% protection, 24/7 access, active form count and average completion time.
- [ ] Review legacy recruitment fields and remove unnecessary sensitive data.
- [ ] Confirm current Anglia / C.I.T.E. registration routes with official sources and the authorised local team.

### P1 — operational readiness
- [ ] Define acknowledgement and completion targets for each request type.
- [ ] Define status tracking and applicant reference numbers.
- [ ] Create secure attachment upload and document correction workflows.
- [ ] Define escalation ownership, office hours and out-of-hours response.
- [ ] Provide a fallback for inaccessible forms, failed uploads and duplicate submissions.
- [ ] Create a form catalogue in EN / AR / FR.
- [ ] Test accessibility, mobile usability, validation, error messages and confirmation emails.
- [ ] Test spam prevention and abuse controls without blocking legitimate applicants.

### P2 — AI and automation integration
- [ ] Assign stable service IDs and form IDs.
- [ ] Publish approved form metadata to the knowledge API / retrieval index.
- [ ] Connect submission events to CRM or case management only after privacy and access review.
- [ ] Provide read-only status lookup with verified identity checks.
- [ ] Add human handoff queue and conversation summary.
- [ ] Log source IDs, answer confidence, escalation reason and outcome.
- [ ] Build regression tests from real, anonymised customer questions.

## 8. Evidence sources inspected

- `data/export/AGI_Website_Content_Export.json` — WordPress export, generated 2026-08-21; 68 pages and 60 news posts.
- `docs/content-map.csv` — source content map.
- `content/migration/legacy-route-inventory.csv` — legacy route inventory.
- `content/migration/route-content-review.csv` — editorial route review.
- `content/migration/anglia-source-to-content-map.csv` — Anglia-related source mapping.
- Legacy form destinations recorded in the export: Omella URLs, Ninja Forms shortcode, Forminator shortcode, and static/email instructions.

## 9. Explicit non-goals of this discovery

This file does not certify that any form is live, secure, legally compliant or connected to the correct team. It does not authorise publishing, changing production forms, collecting new personal data, changing payment routes, or activating AI submission / payment / booking actions. Those require operational testing and owner approval.
