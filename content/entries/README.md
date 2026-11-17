# Structured AGI content export

`entries.json` is the CMS-neutral structured export: 36 records covering 12 page groups in English (en-US), French for Morocco (fr-MA), and Modern Standard Arabic (ar-MA).

Each record contains a stable translation-group ID, slug, locale, source locale, workflow status, title, summary, Markdown body, SEO title/description, evidence placeholders, owner, review date, text direction and publication gates.

## Workflow state
English records remain in editorial review. French and Arabic remain in translation review. None is approved or published. The empty `claims` and `sources` arrays are intentional; evidence mapping must be completed against primary documentation rather than guessed.

## Validation
Run `python scripts/validate_content_export.py` from the repository root. It uses only the Python standard library and checks record count, uniqueness, locale coverage, RTL/LTR direction and review states.

The Markdown bundles remain the human-readable editorial source. This JSON export is a portable interchange format for a future React, WordPress or headless-CMS importer. No live CMS is connected and nothing has been published.
