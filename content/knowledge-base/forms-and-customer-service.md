# AGI Knowledge Base — Forms, Requests and Customer Service

**Project:** American Group International (AGI), Agadir, Morocco  
**Branch:** `cms-test-smartsite`  
**Status:** Research-derived service knowledge base. It is not an approved operational policy and must not be treated as proof that every form, integration, SLA or workflow is currently live.  
**Primary source:** `docs/website-content-spec.md`, section 5; cross-checked against `v2/forms.html`, `app/public/content/pages/forms.json`, `app/src/pages/FormPage.tsx`, `app/api/forms-router.ts` and relevant policy/content records.  
**Purpose:** Provide a reliable operational knowledge layer for the AGI website, AI assistant, digital receptionist and human customer-service team.

---

## 1. Operating principle

The assistant must do more than describe services. It must help a person identify the correct service, understand eligibility and requirements, prepare the right information, open the correct form, explain what happens next, and route exceptions to the responsible human team.

A form is a **service workflow** with:
- a defined customer intent;
- an audience and eligibility boundary;
- a canonical form ID and URL;
- required and optional data;
- supporting documents or information;
- consent/privacy considerations;
- a receiving team or role;
- a confirmation and next-step process;
- an escalation path;
- a source, owner, approval status and review date.

The assistant must never claim a form was submitted, a payment was received, a visit was booked, a document was issued, or a request was approved unless the connected system returns a verifiable success result.

## 2. What the repository currently tells us

### 2.1 The intended forms catalogue

The website content specification describes **11 named form workflows** on one forms page:
1. Enrollment application
2. Visit the school
3. Report an absence
4. Park and outdoor activity consent
5. Parent feedback
6. Payment notice
7. Order Step To books
8. Request a tutor
9. Schedule tutoring sessions
10. Request a document
11. General enquiry

The specification says each form should have a deep link, a short explanation, preparation guidance, fields, and a clear explanation of what happens after submission.

### 2.2 Other form surfaces found

The legacy/current content surfaces also mention:
- a general contact/message form;
- an external Omella enrollment link;
- absence request;
- payment request;
- enrollment application;
- microschool park consent;
- tutor request;
- tutor scheduling;
- parent feedback;
- document request / Forminator shortcode in a legacy content record;
- admissions placement assessment and supporting admissions documents;
- partnership/franchise enquiry as a topic within general enquiry;
- careers enquiry as a topic within general enquiry.

These are not necessarily 1:1 implementations of the 11 workflows. Keep the catalogue IDs stable and reconcile implementation before publishing final links.

### 2.3 Technical implementation mismatch — critical

The repository contains several different descriptions of the forms system:
- `docs/website-content-spec.md` specifies 11 detailed workflows and says forms are selected and submitted on `forms.html`.
- `v2/forms.html` contains a large static HTML forms page. Its copy and links must be tested against the actual working destination and submission behavior.
- `app/public/content/pages/forms.json` advertises seven cards with external Omella links (absence, payment, enrollment, park consent, tutor request, tutor schedule, parent feedback) and uses strong security/availability claims that need technical verification.
- `app/src/pages/FormPage.tsx` currently models only four generic form types: `contact`, `appointment`, `enrollment`, `consultation`. It collects name, email, optional phone, and a limited payload. It does not by itself implement all 11 detailed workflows.
- `app/api/forms-router.ts` accepts those same four types and writes submissions to a database. The code shown does not establish email notification, staff assignment, status tracking, customer confirmation, file upload, consent records, payment verification, or document generation.
- `app/public/content/pages/admissions__document-request.json` contains a legacy Forminator shortcode, not a verified working document-request implementation.
- The admissions content includes policies and supporting material, but a policy page is not itself a request workflow.

**Conclusion:** the intended service catalogue is broader than the currently inspected generic application form/API. Do not tell customers all 11 forms are live or that every submission is securely routed/emailed until each route and backend behavior is tested end-to-end.

## 3. Customer-service journey

Use this common journey for every request:

1. **Welcome and identify intent** — ask what the person wants to accomplish; detect language (English, French, Arabic) and preferred contact channel.
2. **Classify the request** — select one canonical service/form ID. If unclear, ask one focused clarification.
3. **Explain the service** — give a short plain-language description, audience, prerequisites and any known limitations.
4. **Prepare the customer** — list only the information and documents needed for that specific workflow. Avoid collecting sensitive data in chat if the official form or secure channel is the right place.
5. **Provide the official action** — open the verified form URL or offer the correct human contact. Never invent a URL.
6. **Explain next steps** — state the documented receiving team/process and expected response only if currently confirmed.
7. **Confirm status** — use an integrated submission/CRM record if available. Otherwise say the customer must wait for the office's confirmation; do not imply that the assistant can see the submission.
8. **Escalate** — send exceptions, urgent safeguarding matters, payment disputes, complaints, sensitive records, eligibility decisions and policy interpretations to an authorized human.
9. **Close the loop** — provide the reference number or next action only when returned by the system.

## 4. Canonical service catalogue

### FORM-01 — Enrollment application

**Customer intent:** Apply for a place for a learner in an AGI programme.  
**Audiences:** Parent/guardian applying for a child; adult learner applying for themselves.  
**Programs named in the specification:** K–12 school; adult high-school diploma (16+); English and Anglia examinations; special education (SEN); teacher training and C.I.T.E.; education consultancy. Availability and current eligibility must be reconfirmed for each intake.  
**Canonical deep link:** `forms.html#enrollment` (verify in production before use).  
**Preparation:** Previous school records and behavior report; proof of age and residency; immunization and physical examination records; documentation from a licensed practitioner if requesting IEP/special-needs support. Do not request medical documents in an open chat.  
**Fields described:** Student full name, date of birth, nationality (optional), programme, grade (where relevant), preferred start, current/previous school, home languages, learning support/health needs; parent/guardian name, relationship, email, phone/WhatsApp; accuracy and non-refundable annual inscription acknowledgement.  
**Next step in specification:** Admissions contacts the applicant to arrange a placement test and visit.  
**Human owner:** Admissions office — named role in content specification; current assignee/contact to confirm.  
**Agent can:** explain application stages, list documents, identify programme category, link to the form, help prepare a checklist.  
**Agent cannot:** decide admission, grade placement, eligibility exceptions, diagnose a learning need, or guarantee a place.

### FORM-02 — Visit the school

**Customer intent:** Request a guided visit to the Agadir campus.  
**Canonical deep link:** `forms.html#visit`.  
**Preparation:** Two or three suitable dates and the programme of interest.  
**Fields described:** Preferred date, preferred time (morning/afternoon), number of visitors, programme of interest, optional notes; visitor name, email and phone/WhatsApp.  
**Next step in specification:** Office confirms a time by phone or email. Visits are described as Monday–Friday at 20 Rue Baalabek, Hay Nahda, Agadir. Opening hours and available slots require current confirmation.  
**Human owner:** Front office / admissions — confirm assignment.  
**Agent can:** collect preferred date/time, explain location, provide directions and submit a visit request only if a live booking integration is connected.  
**Agent cannot:** invent available slots or say a visit is booked without confirmation from a calendar/booking system.

### FORM-03 — Report an absence, late arrival or early pick-up

**Customer intent:** Notify AGI about a student's absence or change to arrival/pick-up.  
**Canonical deep link:** `forms.html#absence`.  
**Preparation:** Student name and grade, date(s), reason.  
**Fields described:** Student name and grade; notice type (full-day absence, late arrival, early pick-up); date and optional last day/time; reason and details; parent/guardian name, relationship, email and phone.  
**Policy references in the specification:** Notify the office before 9:00 on the day; dated, signed excuse within two days of return; arrival after 10:00 counts as a full-day absence; promotion requires 90% attendance. These are policy claims and must be checked against the currently approved attendance policy before the assistant repeats them as current rules.  
**Next step:** Office records the notice.  
**Human owner:** School administration / attendance office — confirm.  
**Agent can:** help identify the right absence type, list required details, link to the form.  
**Agent must escalate:** same-day safety concern, unexplained missing child, emergency, dispute about attendance or an exception request. A form is not an emergency channel.

### FORM-04 — Park and outdoor activity consent

**Customer intent:** Give parental/guardian permission for a named child to attend a specified outdoor activity.  
**Canonical deep link:** `forms.html#consent`.  
**Preparation:** Activity name/date, emergency phone number, relevant allergy/medication/health notes.  
**Fields described:** Student name and grade; activity and date; emergency contact name/phone; optional health notes; parent/guardian identity/contact; explicit consent checkbox, typed signature and date.  
**Next step in specification:** Teachers receive consent before the activity; parent should call the office if anything changes on the day.  
**Human owner:** School administration / activity lead — confirm.  
**Privacy:** Child and health-related data. Do not collect these details in ordinary assistant chat; route to the approved secure form. Do not infer or create consent.  
**Agent can:** explain the form and remind the parent to submit one per child and activity.  
**Agent cannot:** give consent on behalf of a parent, alter consent, or confirm a child is cleared to attend without verified receipt.

### FORM-05 — Parent feedback

**Customer intent:** Share a suggestion, positive feedback or concern with AGI administration.  
**Canonical deep link:** `forms.html#feedback`.  
**Preparation:** A specific example if possible.  
**Fields described:** Topic (teaching/learning, communication, safety/wellbeing, facilities, fees/administration, other); grade (optional); feedback text; whether a reply is requested; name and email optional/conditional. The specification says anonymous feedback is possible.  
**Next step in specification:** Administration reviews feedback weekly; contact is made if a reply is requested. This cadence must be confirmed before presenting as an SLA.  
**Human owner:** Administration / relevant department.  
**Agent can:** explain anonymous vs reply-requested options and route the form.  
**Agent must escalate:** safeguarding, abuse, threats, immediate safety, discrimination or serious complaints; do not leave these in a routine weekly-feedback queue.

### FORM-06 — Payment notice

**Customer intent:** Tell the office that a payment was made so it can be matched to the correct learner/account.  
**Canonical deep link:** `forms.html#payment`.  
**Preparation:** Student name, amount, payment date, payment method and transfer/cheque/receipt reference.  
**Fields described:** Student name; payment category; months covered where relevant; amount in MAD; date; method (bank transfer, cash at office, cheque, card via online payment page); reference/receipt number; optional note; payer name/email/phone.  
**Critical security rule:** Never ask for or accept card number, CVV, PIN, banking password or one-time passcode. The specification directs card payments to AGI's secure payment page, followed by a payment notice using the receipt number.  
**Next step in specification:** Office checks the payment and confirms by email.  
**Human owner:** Finance / administration — confirm.  
**Agent can:** explain how to report a payment and what reference is useful.  
**Agent cannot:** verify payment, issue a receipt, promise a refund, change balances or accept card credentials unless a trusted finance integration explicitly supports the action.

### FORM-07 — Order Anglia Step To books

**Customer intent:** Ask to purchase/order Anglia Step To books or teachers' guides.  
**Canonical deep link:** `forms.html#books`.  
**Preparation:** Levels, quantities, whether teachers' guides are needed, delivery/collection preference.  
**Fields described:** Book levels (First Step through Masters/C2 as listed in the specification); guide requirement; quantities; buyer type (parent/student, teacher, school/Anglia centre); organization name if relevant; collection at AGI or delivery; delivery address if needed; customer name/email/phone.  
**Next step in specification:** Office confirms availability, price, delivery/collection date, then payment details.  
**Human owner:** Anglia Morocco / book orders — confirm.  
**Agent can:** explain how to submit an order request and help prepare quantities/levels.  
**Agent cannot:** guarantee stock, current price, delivery date or exam eligibility without live inventory/pricing confirmation.

### FORM-08 — Request a tutor

**Customer intent:** Request one-to-one tutoring in a subject, in Agadir or online.  
**Canonical deep link:** `forms.html#tutor-request`.  
**Preparation:** Subject, learner's current grade/level, learning goal and availability.  
**Fields described:** Learner name, grade/level, subject(s), learning goal, location mode (in person Agadir, online, either), availability; requester name/email/phone.  
**Next step in specification:** Office matches the learner with a tutor and confirms price/schedule; a legacy forms page claims 48 hours, but that turnaround is unverified and must not be promised until reconfirmed.  
**Human owner:** Tutoring coordinator / programme administration — confirm.  
**Agent can:** help identify the subject and learning goal, gather preferences and link to the form.  
**Agent cannot:** guarantee tutor qualifications, availability, a match or price without approved roster and schedule data.

### FORM-09 — Schedule or change tutoring sessions

**Customer intent:** Arrange a new tutoring schedule or change an existing one.  
**Canonical deep link:** `forms.html#tutor-schedule`.  
**Preparation:** Learner name, tutor name if known, subject, start date, preferred days/times, frequency and session length.  
**Fields described:** Learner and tutor; new schedule vs change; subject; start date; days; preferred time; frequency; duration (45/60/90 minutes); notes; requester name/email/phone.  
**Next step in specification:** Tutor confirms or proposes an alternative if the preferred slot is unavailable.  
**Human owner:** Tutor / tutoring coordinator — confirm.  
**Agent can:** format preferences and route a scheduling request.  
**Agent cannot:** assert a slot is reserved until a calendar or responsible tutor confirms it.

### FORM-10 — Request a document

**Customer intent:** Request a transcript, enrollment certificate, attendance attestation, AGI-client attestation, diploma copy, apostille-legalised copy or another school record.  
**Canonical deep link:** `forms.html#documents`.  
**Preparation:** Student's full name as on school records, date of birth, years attended, last grade completed, document type, number of copies, language, purpose and delivery method.  
**Fields described:** Student identity and attendance period; document type; number of copies; language (English/French/Arabic); purpose; collection/email PDF/courier; courier address if applicable; requester identity/relationship/contact.  
**Next step in specification:** Office confirms processing time and any fee before preparing the document.  
**Human owner:** Student records / administration — confirm.  
**Privacy/security:** Identity and education records. Do not disclose or send records until identity and authority (former student, current student, parent/guardian, other authorized representative) are verified through approved procedure. Do not put sensitive records into the assistant transcript.  
**Agent can:** explain the request process and collect non-sensitive routing details.  
**Agent cannot:** release a transcript, certify a document, promise apostille/legalisation or waive a fee.

### FORM-11 — General enquiry

**Customer intent:** Ask a question not covered by a dedicated workflow.  
**Canonical deep link:** `forms.html#enquiry`; partnership deep link is described as `forms.html#enquiry/partnership` and must be tested.  
**Topics described:** Programs and admissions; Anglia examinations; partnership or franchise; careers at AGI; other.  
**Fields described:** Topic, organization (optional, especially for partnership/franchise), message; requester name/email/phone.  
**Next step in specification:** Office routes message to the right person and replies by email or phone within one working day. Confirm this response target before using it as a public promise.  
**Human owner:** Front office triages to admissions, Anglia, partnerships, HR/careers or another team. Exact routing table is pending confirmation.  
**Agent can:** answer grounded FAQs, choose a topic, help compose an enquiry and link to the correct form.  
**Agent must escalate:** legal, financial, safeguarding, formal complaints, media, partnership commitments and requests for exceptions.

---

## 5. Additional customer-service intents that need their own workflow records

The website and legacy content mention these actions, but they are not all defined as separate live forms in the 11-form specification:
- General contact/message (contact page).
- Careers / employment application.
- Anglia exam registration and candidate entry.
- Anglia exam special arrangements / access arrangements.
- Anglia placement or level assessment booking.
- Anglia centre / representative / franchise application.
- C.I.T.E. and teacher-development enquiries.
- Adult diploma eligibility and enrolment enquiry.
- Proctoring service enquiry and booking.
- Document editing service enquiry.
- University/pathway consultation.
- Learning Pods / independent studies enquiry.
- Wellbeing / student support enquiry.
- Refund request (must be distinct from a complaint where appropriate).
- Formal complaint and complaint escalation.
- Privacy/data access, correction or deletion request.
- Safeguarding concern / urgent student welfare report.
- Media/photo consent withdrawal or update.
- Accessibility accommodation request.
- Payment reconciliation, receipt request and payment dispute.

For each, create a separate service definition only after confirming that the service is currently offered, its owner, intake method, required data and response process. Do not invent a live form URL.

## 6. Routing matrix — proposed, requires leadership confirmation

| Request category | First-line destination | Specialist destination | Escalation |
|---|---|---|---|
| K–12 application / visit | Admissions / front office | Academic leadership for placement questions | Authorized school leadership |
| Attendance / absence | School administration | Class/attendance lead | School leadership for urgent welfare or disputes |
| Outdoor activity consent | School administration | Activity lead / teacher | School leadership |
| Parent feedback | Administration | Relevant programme/department lead | Senior leadership for serious complaint |
| Payment notice / refund | Administration | Finance | Authorized finance/leadership |
| Anglia exams / books / classes | Anglia Morocco desk | Exam/candidate coordinator | Anglia authorized leadership |
| Tutor request/schedule | Programme administration | Tutoring coordinator / tutor | Programme lead |
| Student records/documents | Administration | Records custodian | Authorized school leadership |
| Partnership/franchise | Front office | Partnerships / Anglia Morocco lead | Authorized leadership |
| Careers | Front office | HR / hiring manager | Authorized leadership |
| Safeguarding / urgent safety | Immediate designated safeguarding contact | Safeguarding lead | Emergency/local competent services as appropriate |

This matrix is a proposed operational model, not confirmation of current named roles or staff assignment.

## 7. AI assistant: what it may and may not do

### Allowed when supported by approved knowledge
- Explain programmes, services, eligibility criteria and documented steps.
- Help the user identify the right form.
- Provide the correct verified form link.
- Prepare a checklist of required documents.
- Translate and explain the form fields in English, French or Arabic.
- Ask for only the minimum information needed to route a request.
- Summarize a user's request before handoff, with their permission where required.
- Create a draft enquiry or support ticket if the connected system supports it.
- Check request status only through a connected system that returns an authoritative record.
- Hand off to a human with a concise context summary.

### Not allowed without a verified integration and explicit authorization
- Submit a form on behalf of a customer.
- Book a visit, tutoring session or exam seat.
- Confirm admission, placement, registration, exam entry or special arrangements.
- Verify or reconcile payments, issue receipts or process refunds.
- Release transcripts or other educational records.
- Sign or grant parental consent.
- Make clinical/therapeutic judgments or diagnoses.
- Promise a response time, availability, price, stock, outcome or service level not in a current approved source.
- Accept card details, passwords, one-time codes, national ID scans or sensitive health records in ordinary chat.
- Claim to be a human employee or conceal that the user is interacting with an AI assistant.

## 8. Privacy, data minimization and safeguarding

- Collect only the information required for the specific request.
- Keep child identity, health, disability, educational records, family details and emergency contacts out of ordinary chat whenever an approved secure form exists.
- Do not ask a user to upload medical/psychological reports to an unapproved channel.
- Verify a parent/guardian's authority before sharing a child's records or case details.
- Do not disclose whether a child is enrolled or share student records with an unverified requester.
- Do not expose internal notes, staff personal contacts, other customers' submissions or private student information.
- Route safeguarding concerns to the designated human process immediately; the assistant is not an emergency service.
- The website's privacy policy and Moroccan data-protection requirements must be reviewed by the responsible legal/privacy owner. Do not make unsupported encryption or compliance claims.

## 9. Knowledge record schema for each service/form

Every form should be represented in the future knowledge base with these fields:

```yaml
service_id: FORM-01
canonical_name: Enrollment application
aliases: [apply, admissions application, register my child]
brand: AGI | Anglia Morocco | AGI Programs
audience: [parent, guardian, adult learner]
intent: apply_for_place
canonical_url: /forms.html#enrollment
availability_status: verified_live | needs_test | retired | planned
languages: [en, fr, ar]
description: ""
eligibility: []
required_fields: []
optional_fields: []
required_documents: []
sensitive_data: []
pre_submission_checks: []
submission_method: website_form | external_provider | email | phone | in_person
receiving_team: ""
human_owner: ""
acknowledgement: ""
next_steps: []
response_time: null
exceptions: []
escalation_rules: []
source_refs: []
fact_refs: []
policy_refs: []
approval_status: proposed | source_only | approved | hold
last_verified: null
review_due: null
```

Use stable service IDs across languages and channels. Translate display names and instructions, not the IDs.

## 10. Implementation and validation backlog

### P0 — before the AI assistant is allowed to direct customers to forms
1. Test all 11 deep links in the actual target website and mobile view.
2. Submit test entries for each form using test data; verify where each submission lands.
3. Confirm whether Omella is still the official provider for enrollment, absence, payment, consent, tutoring and feedback forms.
4. Resolve the mismatch between the 11-form specification, seven cards in `forms.json`, four generic app form types, and the static `v2/forms.html`.
5. Confirm the receiving team, owner, notification method, acknowledgement and status tracking for every form.
6. Confirm current fees, dates, availability, schedules and policy references before the assistant repeats them.
7. Remove or substantiate unverified claims such as "100% protected", "encrypted submission environment", "24/7 secure access", "average completion time" and any fixed response time.
8. Verify the privacy notice, retention period, access controls, consent and lawful handling of child/student data.
9. Create human escalation contacts and a tested handoff process for every sensitive request type.
10. Ensure card payments are handled only by the approved payment provider; never collect card data in AGI forms or chat.

### P1 — for a useful digital receptionist
- Connect the form catalogue to a CRM/helpdesk or submissions inbox with a unique request ID.
- Add statuses: received, awaiting information, assigned, in progress, waiting for customer, completed, declined, escalated.
- Send a customer acknowledgement that does not imply approval.
- Give staff an internal routing queue and an auditable change history.
- Add multilingual templates for acknowledgements and missing-information requests.
- Allow customers to check status through a verified reference and appropriate identity checks.
- Measure first response time, resolution time, incomplete submissions, abandoned forms and handoff rate.

### P2 — service automation
- Pre-fill non-sensitive form fields only with user consent.
- Offer guided form completion without bypassing mandatory fields or consent.
- Schedule visits only against a live calendar.
- Schedule tutoring only against approved tutor availability.
- Prepare document requests, but require staff verification before release.
- Integrate payment status read-only first; never infer payment from a user statement alone.
- Keep human approval for admissions, refunds, complaints, safeguarding, exam arrangements and partnership commitments.

---

## 11. Source references and confidence

| Source | What it supports | Limit |
|---|---|---|
| `docs/website-content-spec.md`, section 5 | Detailed intended 11-form catalogue, fields and described next steps | Specification, not proof of production implementation or current policy |
| `v2/forms.html` | Static forms page and customer-facing copy | Must test actual destinations and submission behavior |
| `app/public/content/pages/forms.json` | Seven card links and legacy portal copy | Contains unverified operational/security claims |
| `app/src/pages/FormPage.tsx` | Four generic form types and collected fields | Not a complete implementation of all 11 workflows |
| `app/api/forms-router.ts` | Four accepted submission types and database insert | Does not show full routing, notification or status workflow |
| `app/public/content/pages/admissions__document-request.json` | Legacy Forminator shortcode | Not a verified working form |
| `app/public/content/pages/admissions__placement-assessment.json` | Admissions placement/assessment policy text | Must be checked for current approval and legal suitability |
| `app/public/content/pages/admissions__refunds-complaints.json` | Refund and complaints text | Must be reviewed and confirmed before assistant use |

**Publication rule:** this knowledge base is a discovery and design artifact. Convert an item to customer-facing answerable knowledge only after its current source, owner, approval and operational behavior are verified.
