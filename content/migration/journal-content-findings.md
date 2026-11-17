# Journal content reconciliation — index, WordPress export and crawl inventory

**Scope:** `v2/journal.html`, `v2/journal/`, `v2/journal-ccgi-partnership.html`, `data/export/AGI_Website_Content_Export.json`, and `docs/content-map.csv`.  
**Status:** preliminary content reconciliation; no article has been deleted, redirected or published as part of this review.

## Reconciled counts

| Source or destination | Count | Interpretation |
|---|---:|---|
| WordPress export `news` records | 60 | Historical source records from 9 January 2018 to 16 June 2026 |
| Cards in `v2/journal.html` | 66 | Actual entries presented by the journal index |
| HTML files in `v2/journal/` | 66 | One file for each current journal card |
| Export records matching a journal card by slug/title | 59 | 59 of the 60 exported records appear in the 66-card journal index |
| Crawl-inventory items added to the journal index | 7 | Six post-like records plus one gallery page; not in the 60-record WordPress export |
| Export record routed to a separate designed page | 1 | The CCGi partnership announcement is routed to `v2/journal-ccgi-partnership.html`, outside `v2/journal/` and absent from the 66 journal cards |
| Total distinct source items represented across these routes | 67 | 60 exported records + 7 crawl-inventory items |

**Conclusion:** the figures 60 and 66 are not a simple duplicate-count discrepancy. The 66-card journal index consists of 59 exported WordPress posts plus seven crawl-inventory additions. The remaining exported post about the CCGi partnership has a separate designed page but is not linked from the journal index. The folder count of 66 therefore does not include that standalone designed page.

## Crawl-only records requiring editorial decisions

| Current article file | Source title | Source words | Proposed treatment |
|---|---|---:|---|
| `anglia-mastery-qualification-awarded-ucas-tariff-points.html` | Anglia Mastery Qualification Awarded UCAS Tariff points | 385 | Consolidate with the second Mastery page as one canonical story with independently reviewed language versions |
| `anglia-mastery-qualification-awarded-ucas-tariff-points-2.html` | Anglia Mastery Qualification Awarded UCAS Tariff Points | 380 | Same story/claim in a second source-language URL; do not retain as a separate duplicate article without a clear editorial reason |
| `chichester-college-group-selected-for-queens-anniversary-prize.html` | Chichester College Group Selected For Queen’s Anniversary Prize | 119 | Retain as dated partner news only after source attribution and partner wording are checked |
| `educational-workshop-english-castle.html` | Educational Workshop English Castle | 211 | It is mapped as a page, not a post; classify as an event archive or resource after confirming date and organiser |
| `julie-our-newest-franchisee-from-morocco-an-article-published-in-the-anglia-november-newsletter-2021.html` | “Julie Our newest franchisee from Morocco” | 512 | Retain as an externally sourced historical profile only with attribution, permission and verified historical role/title |
| `proud-that-everyone-can-take-an-anglia-exam.html` | Proud that EVERYONE can take an Anglia exam! | 59 | Expand from verified special-arrangements information or merge into the current examination support page; do not present as proof of universal access |
| `student-life.html` | student life | 56 | This is a gallery landing page, not an article; move to the Student Life media collection after image-consent and rights review |

## High-priority article findings

1. **Spelling Bee date/content conflict.** The journal index dates the article 16 June 2026, while the body says the event took place in May 2023. Establish whether 2026 is the publication date and 2023 the event date; show both explicitly if correct.
2. **Therapeutic-coach announcement.** The April 2026 article uses accreditation and clinical-adjacent language and lists support for spectrum disorders, ADHD, play therapy and family services. Verify the exact credential, accrediting body's status, legal scope, practitioner role, service provider and safeguarding boundaries before reusing any claim outside the historical news context.
3. **ASCA announcement.** The article title says “Member” while the body describes recognition or partnership through the founder. Confirm whether the member is the individual or the institution and use the exact approved relationship.
4. **Bridge Education Group.** The November 2025 announcement describes an official partnership and accredited TEFL/TESOL programmes. Verify the agreement, scope, current availability and awarding/certifying provider before using this as a current offer.
5. **CCGi announcement.** The exported August 2025 post has a standalone designed page but no journal-index card. Add it to the journal index only after deciding whether it is still a current partnership announcement or should remain a dated archive.
6. **Mastery/UCAS claim.** The two crawl-only pages appear to be language/source variants of one historical claim. Verify the exact qualification title, level, awarding body and UCAS tariff statement against current official records before creating one canonical article.
7. **Old event and admission notices.** Back-to-school, testing-session, summer-school, registration and class-schedule posts must remain visibly historical. Do not reuse old dates or prices as current offers.

## Content quality and reuse rules

- Preserve historical publication dates; add event dates separately when they differ.
- Store article title, original source URL, publication date, event date, author, language, category, image rights, source attribution and review state as separate fields.
- Keep journal stories distinct from evergreen programme descriptions. A news article can link to a current programme module, but it should not be silently rewritten into evergreen marketing copy.
- Do not delete or redirect the crawl-only pages as part of editorial triage. Decide their destination and URL treatment individually.
- Keep partner, accreditation, qualification, clinical, student identity and image-rights claims behind evidence/consent gates.
- The machine-readable review rows are in `journal-reconciliation.csv`.

## Related count discrepancy still open

The content specification describes a 151-page sitemap, while the current `v2/sitemap.xml` contains 150 `<loc>` entries. This is separate from the journal article count. Reconcile the page inventory and sitemap URL-by-URL before treating either number as authoritative.
