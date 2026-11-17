# AGI Knowledge Base

This folder is the editorial and operational knowledge layer for the AGI website and future AI/customer-service assistant.

## Current assets

- [Forms and Customer Service Knowledge Base](forms-and-customer-service.md) — detailed service catalogue, 11 website-specified forms, field requirements, customer journeys, routing, AI permissions, privacy and implementation checks.
- [Structured Service Catalogue](service-catalogue.csv) — machine-readable catalogue for the 11 core forms plus additional support intents that need workflow confirmation.

## Scope to complete

The knowledge base must cover all AGI and Anglia Morocco services, not just website pages:
1. Service descriptions, audiences, eligibility and exclusions.
2. Step-by-step customer journeys and decision trees.
3. Forms, required information, documents, consent and submission channels.
4. Fees, dates, schedules, availability and their authoritative owners.
5. FAQs and approved answers in English, French and Arabic.
6. Customer-service procedures, handoffs, escalation and complaint handling.
7. Policies, privacy, safeguarding, accessibility and data retention.
8. Status messages, acknowledgement templates and follow-up procedures.
9. Knowledge ownership, evidence, approval and freshness metadata.
10. Integrations with the future CRM/helpdesk, forms, calendars, email, WhatsApp and payment provider.

## Status policy

- `APPROVED`: verified and authorized for customer-facing answers.
- `SOURCE_ONLY`: present in repository/source material, but current approval or implementation is not verified.
- `TO_CONFIRM`: requires an authorized answer or current evidence.
- `HOLD`: not safe to publish or automate.
- `RETIRED`: preserve for history, do not present as current.

The assistant must retrieve only approved answers for high-impact facts and procedures. It must clearly qualify source-only material and hand off unresolved matters to a human.

## Governance

Every knowledge item should have a stable ID, language variants, source references, owner, approver, status, last verified date and next review date. English is the master language; Arabic and French versions must preserve the same meaning and approval status.

No customer-facing system should claim that a form is live, a payment is verified, a visit is booked, a document is issued, an application is accepted or a complaint is resolved without a trusted system response.
