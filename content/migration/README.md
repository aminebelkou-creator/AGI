# Legacy content inventory

This CSV was generated from the current app's `app/public/content/index.json` and `news.json` on branch `cms-test-smartsite`. It inventories existing routes and news items; it does not authorise deletion, rewriting, redirects or publication.

- 68 indexed legacy page routes.
- 60 legacy news items.
- 128 referenced page JSON files in total.
- Every route/news item is marked review-required; candidate core-page mappings are discovery hints only.
- Preserve the existing route and content until a human owner approves consolidation or retirement.

See `content/architecture/current-site-integration.md` for the migration strategy.

## Reconciliation and review

- [Structural reconciliation report](legacy-content-reconciliation.md): verified route/news/file integrity baseline and review priorities.
- [Legacy route review matrix](legacy-route-review-matrix.csv): 68 route-by-route triage rows. Priority flags are automated from route/title text only; they are not a review or approval of the page body.
- Run the read-only integrity audit with `python scripts/audit_legacy_content.py`. GitHub Actions runs it alongside the multilingual export validator.
