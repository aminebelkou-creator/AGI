# AGI content reconciliation and editorial audit

**Review date:** 17 November 2026  
**Branch:** `cms-test-smartsite`  
**Scope:** WordPress export, v2 journal and sitemap, crawl content map, structured multilingual content, claims/facts registers and legacy route review.  
**Status:** Editorial working document. No content in this report is approved for publication.

## Executive findings

The repository contains several overlapping but distinct generations of AGI content. They must be reconciled by provenance and editorial purpose, not by page count alone.

| Source | Observed count | What the count means |
|---|---:|---|
| WordPress content export | 68 pages + 60 posts | Legacy source records in `data/export/AGI_Website_Content_Export.json` |
| v2 journal directory | 66 HTML files | 66 rendered article destinations in `v2/journal/` |
| Crawl content map | 66 journal destinations | 59 titles match WordPress export posts; 7 are additional crawl-only destinations |
| Dedicated Chichester feature | 1 page | The 60th WordPress post is represented by `v2/journal-ccgi-partnership.html`, outside the journal directory |
| v2 sitemap | 150 `<loc>` entries | Current XML count; the website content specification says 151 pages |
| Structured core entries | 51 records | 17 content groups × 3 locales in the current structured bundle |
| Reusable content library | 15 modules / 45 locale variants | First reusable copy batch, not the full site |

**Reconciled journal interpretation:** 59 WordPress posts have matching journal-map titles; one WordPress post about the Chichester College Group partnership is handled by a separately designed feature page; seven additional journal destinations originate from the wider crawl (including Anglia Morocco material). The 66 journal HTML files therefore are not 66 WordPress posts. Preserve all 60 source posts and all 66 mapped journal destinations until individual editorial decisions are approved.

The 150-versus-151 sitemap/specification difference remains open. It is a count difference, not proof of a missing page. Compare canonical URLs and page types before changing either source.

## 1. Reconciliation decisions

### WordPress and journal

- Retain the original 60 WordPress news records as the historical source set.
- Keep the dedicated Chichester partnership feature separate from the 66-file journal directory unless an editor explicitly decides to integrate it.
- Retain the seven crawl-only destinations in the reconciliation register as independent source material. Do not assume they are duplicates or WordPress posts.
- Compare the two Anglia Mastery / UCAS crawl articles. They appear to be parallel language/source versions and should not both be treated as separate English news events without a content comparison.
- The short items `Proud that EVERYONE can take an Anglia exam!` and `student life` are not strong standalone articles in their current form. Consider turning them into resource/gallery records or archiving them after checking source media and rights.
- The `Educational Workshop English Castle` record is classified as a page in the source map but routed to the journal. Decide whether it is an event archive or programme page.
- The Julie Wilburn franchisee newsletter extract is a historical profile. Do not reuse its 2021 role description as a current title.
- Historical dates and announcements must remain historical. Expired enrolment, examination, class and calendar announcements must never be presented as current offers.

The row-level decisions are in `content/migration/journal-reconciliation.csv`.

### Legacy pages

The route review covers all 68 legacy routes. High-risk content should be resolved before low-risk editorial polish:

1. Admissions, fees, calendar, eligibility, attendance, academic progress and handbook.
2. School legal designation, curriculum scope, grade authorisation and recognition claims.
3. Anglia examinations, current franchise scope, C.I.T.E., awarding-body wording, exam dates and centre directory.
4. Adult diploma provider and issuer, university pathway agency status, teacher sponsorship and proctoring.
5. Inclusive-learning, counselling, coaching and therapy descriptions, provider credentials and safeguarding.
6. Contact, forms, privacy, consent and handling of student information.

The route matrix is a triage instrument, not a declaration that every body has been legally or academically approved.

## 2. Specific content defects and editorial opportunities

| Area | Finding | Recommended treatment |
|---|---|---|
| Institutional story | History, legal identity, school status and AGI/Anglia relationships are blended | Create one approved institutional narrative and a separate school profile |
| Vision | Legacy `/about/vision` contains Lorem ipsum | Do not migrate the placeholder; write a fresh vision statement for leadership approval |
| Admissions calendar | 2026–27 page contains 2025 dates in its body | Replace only from an approved academic calendar; archive the superseded version |
| Important dates | Legacy material includes 2022 dates | Historical archive only |
| Anglia Saturday schedule | 2025–26 schedule has expired | Replace with a dated current schedule or remove current promotion |
| C.I.T.E. | Duplicate legacy pages and risk of calling it a TESOL/teaching qualification | One canonical page; state clearly that C.I.T.E. is an examination and not itself a teaching qualification |
| Learning Pods | Multiple pages overlap | Compare programme scope and consolidate only after owner confirmation |
| Special education / wellbeing | Public copy includes clinical/therapeutic language | Separate educational support from clinical services; verify provider, scope, credentials and safeguarding |
| Adult diploma | Provider, issuer, recognition and AGI's role are material | Identify provider and diploma issuer explicitly; disclose recognition limitations |
| University pathways | “Authorised admissions agent” is a material agency claim | Hold until a current agreement defines territory, role and permitted wording |
| Student stories | Real names, photos and testimonials may appear | Require purpose-specific written consent and rights record before promotion |
| Educational resources | McGuffey and other third-party content may be extensive | Rights review; preserve attribution and licensing; do not republish uncertain material |
| Forms | Some legacy pages contain only shortcodes or form references | Describe the user task clearly and confirm secure working form before presenting as operational |
| Privacy/legal pages | Generic or legacy text is not proof of legal compliance | Qualified review against actual data flows and applicable Moroccan law |

## 3. Claims and fact governance

The current registers contain important unresolved items. The claims register has 23 entries; the v2 claims file has 13 entries, with 11 marked open. These are overlapping registers and should be cross-mapped by stable claim ID rather than maintained as independent, contradictory truth sources.

Do not publish the following until the specified evidence exists:

- 45+ versus 46+ nationalities; define population, period and counting method.
- “First American school in Agadir”; comparative evidence and legal review required.
- AGI's legal designation as a correspondence school and the exact operator/entity name.
- Founding date, first cohort and founding story; founder confirmation and historical record.
- Current grade range, curriculum and school authorisations.
- Fees, inclusions, refunds, deadlines, school hours and response-time promises.
- Current Anglia franchise status, centres, schedules, prices and exam availability.
- Qualification-specific AIM / Ofqual / UCAS claims; never generalise one qualification's status to all Anglia exams.
- C.I.T.E. scope; do not describe it as a professional teaching licence or standalone TEFL/TESOL qualification.
- Adult diploma awarding body, provider status, credit transfer and recognition.
- Clinical, therapeutic, occupational-therapy, speech-language and behavioural-service claims.
- Current partner relationships with Chichester, Bridge, Leverage Edu, AWA and other organisations.
- Current staff roles, biographies, credentials and photographs.

The fact register should be the only maintained source for dynamic values. Every dynamic fact needs an owner, source, effective date, last-verified date, next review date and publication rule. Do not copy an old price or date into evergreen marketing prose.

## 4. Canonical content architecture

The editorial library should be organized around these content entities:

1. **Institution:** AGI identity, history, mission, vision, values, leadership, governance and contact.
2. **School:** school profile, curriculum, learning approach, student life, inclusion, admissions and policies.
3. **Programme:** each distinct programme with audience, purpose, eligibility, delivery mode, outcomes, provider and evidence.
4. **Qualification / examination:** awarding organisation, exact title, level, specification, assessment, recognition scope and current availability.
5. **Partner / provider:** legal name, relationship type, territory, term, role, permission and current status.
6. **Policy / document:** owner, version, effective date, review date, audience and authoritative file.
7. **News / story:** original date, author/source, event date, participants, consent, media rights and historical status.
8. **Resource / book:** publisher, edition, ISBN, author, level, rights, format, price and stock.
9. **Event / schedule:** academic year, local time, dates, registration status, owner and expiry.
10. **Form / workflow:** purpose, data collected, controller, recipient, retention, security and confirmation route.

A programme is not a partner; a franchise is not an accreditation; an examination is not a teaching qualification; an educational support service is not automatically a clinical service. Preserve these distinctions in every language.

## 5. Page-by-page editorial sequence

### Priority A — trust and enrolment
- Homepage: explain AGI in one clear sentence, then route visitors by audience.
- About AGI: approved institutional history, mission, vision, leadership and entity relationships.
- School: exact educational offer, authorised grades, curriculum, learning approach and student experience.
- Parents: practical answers to parent concerns, support, communication and visit expectations.
- Admissions: steps, documents, placement, current fees, calendar and realistic response times.
- Policies: plain-language summaries linked to approved full policies.

### Priority B — programme clarity
- Inclusive learning: educational scope and referral boundaries.
- Anglia Morocco: examination levels, local role, centre directory and registration.
- C.I.T.E.: examination scope and explicit qualification boundary.
- Step To: current catalogue and rights.
- Adult learning: provider, issuer and recognition disclosure.
- Professional English, proctoring, teacher development and consultancy: one page per service with distinct provider and offer details.

### Priority C — proof and editorial depth
- Student life: consent-cleared stories, authentic photos and dated events.
- Journal: preserve history; label old news; add context rather than rewriting historical facts.
- Outcomes: only evidenced learner outcomes and approved testimonials.
- Resources: useful learning guides, parent explainers and exam-preparation material.

## 6. Editorial quality standard

Every public page must answer:
- Who is this for?
- What exactly is offered?
- Who delivers it and who awards any credential?
- What does the learner or parent need to know before deciding?
- What is included, excluded and conditional?
- What evidence supports the important claims?
- What is the next useful action?
- When was this information last checked?

Avoid generic promotional phrases that could describe any school. Replace them with verifiable practices, examples, clear process descriptions and actual learner experience. Do not invent testimonials, outcomes, class sizes, facilities, staff qualifications or student stories.

## 7. Localisation standard

English is the meaning master for the current core batch. French and Arabic must be localised as independent editorial versions, not literal machine translations.

- French (Morocco): use natural institutional French and explain foreign qualifications without suggesting automatic equivalence with Moroccan diplomas.
- Arabic: use clear Modern Standard Arabic suited to Moroccan families; maintain right-to-left direction and carefully format dates, numbers, names and qualification titles.
- Preserve official names and qualification titles in their original form, with a short explanation in the local language.
- Review legal, educational and examination terminology with a qualified reviewer in each language.

## 8. Publication gates

No page moves to `approved` or `published` solely because it passes JSON, HTML or link validation. Required gates are:

1. Editorial owner review.
2. Fact and source verification.
3. Specialist, legal or partner review where applicable.
4. Student/media consent and third-party rights review.
5. Native-language localisation review.
6. Final page preview and link/form verification.
7. Effective date, review owner and expiry/review date recorded.

## 9. Next actions

1. Reconcile the 23-claim register with `v2/_build/claims.json` and the fact register.
2. Obtain the Priority 0 evidence listed in `content/governance/research-backlog.md`.
3. Approve the AGI/School/Anglia/AGI USA entity descriptions.
4. Complete Priority A pages in English; localise only after English meaning and claims are cleared.
5. Reconcile the 150 sitemap URLs with the 151-page specification.
6. Review the 66 journal pages and seven crawl-only items; retain historical source and record final disposition individually.

**Safety rule:** This audit proposes content decisions. It does not authorise deletion, public release, URL redirects, publication, or changes to the live website.
