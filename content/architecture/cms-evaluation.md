# CMS evaluation and pilot decision

**Status:** architecture recommendation for a reversible proof of concept; not a production selection or deployment approval.  
**Date:** 17 November 2026

## Recommendation

Run a small, isolated **Strapi 5 Community Edition** proof of concept as the leading CMS candidate. Keep Payload CMS as the principal alternative. Do not connect either candidate to the existing application's production database, and do not migrate or publish legacy content during the proof of concept.

The choice is driven by AGI's current application shape: a React/Vite front end, a separate content API boundary, and a repository that already uses MySQL in its application stack. Strapi is independently deployable and documents support for MySQL, MariaDB, PostgreSQL and SQLite. Its official self-hosting page states that the Community Edition is MIT-licensed and can run on infrastructure controlled by the operator.

## Candidate comparison

| Candidate | Strengths for AGI | Constraints / risks | Current position |
|---|---|---|---|
| Strapi 5 Community | Standalone headless CMS; generated REST API; MySQL/MariaDB/PostgreSQL/SQLite support; built-in i18n; draft/publish; MIT Community Edition; admin UI | Separate application and dedicated database required; confirm exact locale codes; advanced review workflow and AI translation may require paid plans; must configure roles, permissions and editorial gates carefully | **Preferred isolated pilot** |
| Payload CMS | MIT; self-hostable; strong TypeScript model; generated REST API; native field-level localization, locale fallback and RTL locale configuration | Official getting-started requirements list MongoDB, PostgreSQL or SQLite, not MySQL; closer coupling to a Next.js application architecture; database choice would be an additional decision | Strong alternative if AGI chooses PostgreSQL and/or a Next.js application |
| KeystoneJS | MIT; code-first schema; GraphQL-oriented; flexible for bespoke data models | More engineering required for a polished editorial experience and multilingual workflows; less turnkey for the editorial team | Not first choice for this website migration |
| Directus | Strong data/API interface and flexible data modelling | Licensing model and feature entitlements require a separate legal/commercial review; avoid assuming the whole product is OSI-open-source or that every feature is free | Defer pending licensing review |

## Evidence from official documentation

- Strapi describes itself as self-hostable and its Community Edition as MIT-licensed: https://strapi.io/hosting
- Strapi database support and minimum versions are documented here: https://docs.strapi.io/cms/configurations/database
- Strapi internationalization is available as a free feature, but must be enabled on each relevant content type and field: https://docs.strapi.io/cms/features/internationalization
- Strapi Draft & Publish is a free feature for managing draft and published versions: https://docs.strapi.io/cms/features/draft-and-publish
- Strapi REST API endpoints are generated from content types: https://docs.strapi.io/cms/api/rest
- Payload's localization supports field-level locales, locale fallback and RTL configuration: https://payloadcms.com/docs/configuration/localization
- Payload's REST API is generated from collection and global configuration: https://payloadcms.com/docs/rest-api/overview
- Payload's official self-hosting page describes the open-source MIT option and lists PostgreSQL, MongoDB or SQLite requirements: https://payloadcms.com/get-started
- Payload's repository license: https://github.com/payloadcms/payload/blob/main/LICENSE.md
- Keystone's repository license: https://github.com/keystonejs/keystone/blob/main/LICENSE

## Important database boundary

Strapi's documentation explicitly warns that a Strapi application is not intended to be connected to an existing database that was not created by Strapi. Therefore:

1. Create a separate, empty database for the pilot.
2. Never point Strapi at the existing AGI application's database.
3. Do not reuse production credentials.
4. Keep the pilot isolated from the public website and all live forms.
5. Take normal backups and keep test content synthetic or already approved for this purpose.

This is a deliberate boundary, not an obstacle. The CMS can expose content through REST APIs to the existing Vite front end without sharing the application's operational database.

## Pilot scope

The pilot should prove the following before a final CMS decision:

- Content types: Page, News Article, Service, Partner, FAQ, Resource and reusable SEO metadata.
- Locales: English, French and Arabic, including a verified Arabic RTL editor experience.
- Translation relationships: stable identity across locale variants; no silent fallback that presents English as if it were Arabic or French.
- Editorial state: draft, editorial review, translation review, legal/partner review, approved and published.
- Permissions: author, translator, reviewer, publisher and administrator roles; only a restricted publisher role can publish.
- API: read-only public endpoints for approved/published content; authenticated editorial write operations.
- Media: image alt text, ownership/rights notes, captions, focal points and safe asset handling.
- Migration: import a small sample only; preserve original legacy IDs and slugs.
- Export: deterministic export back to the neutral `content/entries.json` contract.
- Backup/restore: demonstrate a complete backup and restore before any real content import.

## Acceptance gates

The pilot is successful only if all of these are demonstrated:

1. A content editor can create and edit an English page without developer assistance.
2. A translator can create French and Arabic variants while preserving the stable content identity.
3. Arabic content displays and edits correctly in RTL.
4. An unapproved draft cannot appear in the public API.
5. A reviewer can see the source language and evidence/claim notes.
6. The system supports the required SEO fields and canonical/alternate language metadata.
7. The existing React/Vite site can read approved content through a versioned API adapter.
8. Backups, restore, authentication, roles, auditability and security updates are documented.
9. The CMS can be operated and updated without a vendor-hosted dependency.
10. No live website route or content is changed during the test.

## Decision rule

If Strapi passes the pilot with the required locale and editorial controls, use it as the CMS behind the existing React/Vite front end. If it fails a critical requirement, test Payload with a dedicated PostgreSQL database. Do not select a platform based only on feature marketing or popularity.

## Explicit non-goals

This recommendation does not authorize a production CMS installation, a database migration, a live-site content import, a domain/DNS change, or publication. Those remain separate release decisions after a tested staging deployment and rollback plan.
