# Anglia Morocco content audit — programme copy and evidence gates

**Scope:** `v2/anglia.html`, `anglia-exams.html`, `anglia-cefr.html`, `anglia-classes.html`, `anglia-books.html`, `anglia-special-arrangements.html`, `anglia-placement-test.html` and `anglia-faq.html`.  
**Status:** content audit and reusable copy preparation; not partner approval or qualification verification.

## Editorial structure

Anglia Morocco should be presented as a distinct examination and English-learning activity associated with AGI, with a clear explanation of AGI’s local role. It should not be mixed into the K–12 school curriculum or presented as if AGI itself awards every qualification.

The current content library now provides separate reusable modules for:

- General English levels and the exam pathway.
- Exam components and duration.
- CEFR explanation.
- Business English examinations.
- Special arrangements.
- Class formats.
- Placement assessment.
- Step To learning resources.
- Qualification recognition and progression.

The Anglia page composition references these modules by stable ID. Existing v2 copy remains source material and is not automatically replaced.

## Critical copy conflicts

### 1. C.I.T.E. is incorrectly described as a TESOL qualification

The Anglia hub currently describes C.I.T.E. as a “prestigious TESOL qualification” and a lifelong qualification recognised worldwide. This conflicts with the explicit qualification boundary already recorded in claim C-013 and in the C.I.T.E. content: C.I.T.E. is an Anglia examination and must not be presented as a professional teaching qualification or teaching licence.

**Decision:** remove the TESOL qualification/licence language from the Anglia hub and C.I.T.E. promotional copy. Use the approved-boundary draft in `agi.program.cite`, subject to current official Anglia wording.

### 2. General English, Business English and qualification regulation must remain separate

The source pages describe a ten-step General English pathway, young-learner/intermediate/higher groupings, and a separate Business English pathway. They also describe the four highest General English qualifications as AIM/Ofqual regulated. These are different facts and must not be collapsed into a statement that all Anglia exams are regulated or carry the same recognition.

**Decision:** keep General English and Business English as separate modules. Use the exact level and qualification names from current official specifications. Retain the scope limit in claim C-010 and the prohibition in C-011.

### 3. UCAS statement applies to a specific qualification

The current pages state that Anglia Mastery (C2) carries UCAS tariff points. The journal also contains two language/source variants of the same historical story.

**Decision:** use a qualification-specific statement only after checking the current UCAS listing, exact title and awarding body. Do not imply that all Anglia certificates carry tariff points. Consolidate the two historical language variants into one canonical story with separate language copy.

### 4. Class prices and placement-test offer are stale or unverified

The classes page labels its prices as effective November 2024 and says books and insurance are not included. The current placement page calls the assessment free. These statements require present-day operational confirmation.

**Decision:** remove old figures from evergreen programme copy. Ask the Anglia Morocco office for the current fee schedule, schedule, materials/inclusions and whether the placement assessment remains free. Record approved offers as dated facts.

### 5. CEFR school benchmarks are not the same as Anglia examination specifications

The CEFR page combines school-grade benchmarks with the general explanation of CEFR levels and Anglia examination information.

**Decision:** separate:
- the CEFR framework as a general language reference;
- Anglia’s official exam-to-CEFR mapping;
- AGI’s internal school grade benchmarks.

Do not imply an external awarding body has approved AGI’s internal grade benchmarks unless documentary evidence supports that exact claim.

### 6. Special arrangements must not be promised automatically

The current page describes accommodations for sensory, learning and physical needs, including temporary injuries, and says the organisation will try to meet other needs.

**Decision:** explain the request process, evidence and deadline, individual decision, and centre capability. Do not guarantee an accommodation before the examination provider and centre confirm it.

### 7. Step To catalogue needs rights and product-level metadata

The current page describes ten books with 10–12 topic-based units, QR-linked audio and sample tests, and 110–128 pages. These specifications, editions and digital assets need a verified catalogue.

**Decision:** create one record per book with official title, level, edition, ISBN, rights holder, included resources, audio access, teacher guide, price, stock and ordering terms. Do not reproduce protected book content or audio without permission.

## Source and claim controls

| Topic | Existing claim reference | Required gate |
|---|---|---|
| Morocco franchise relationship | C-008 | Current franchise confirmation and approved territory wording |
| Anglia / Chichester relationship | C-009, C-014 | Keep legal entities distinct; current partner wording |
| AIM / Ofqual status | C-010, C-011 | Exact four qualification titles and current regulator register |
| Mastery / UCAS | C-012 | Current UCAS listing and qualification title |
| C.I.T.E. | C-013 | Examination only; not a teaching licence or standalone teaching qualification |
| Bridge / TEFL / TESOL | C-015 | Current agreement, issuer, scope and AGI role |
| Current classes, prices and dates | C-020 | Current approved operational schedule and tariff |

The detailed evidence register is `content/facts/fact-register.csv` (facts F-AGI-031 through F-AGI-038).

## Page-by-page disposition

| Page | Content action |
|---|---|
| `anglia.html` | Rewrite the hub around the examination pathway, local role, class options, centres and verified CTAs; remove the C.I.T.E./TESOL contradiction |
| `anglia-exams.html` | Preserve the ten-step concept only after level-name verification; split General and Business English |
| `anglia-cefr.html` | Separate CEFR explanation, official Anglia mapping and AGI internal school benchmarks |
| `anglia-classes.html` | Remove November 2024 prices from current offer copy; rebuild from an approved current tariff |
| `anglia-books.html` | Use a verified Step To catalogue; check rights and audio/digital access |
| `anglia-special-arrangements.html` | Rewrite as a request and review process, not a guaranteed accommodation promise |
| `anglia-placement-test.html` | Retain placement-assessment purpose; verify whether the offer is free and currently bookable |
| `anglia-faq.html` | Rebuild answers from the reusable modules and current official specifications |

## Publication rule

All new Anglia modules remain in editorial or partner review. The presence of a module, fact reference or successful structural validator does not constitute Anglia approval, awarding-body approval or proof of current availability.
