# Structured AGI content export

`entries.json` is the CMS-neutral structured export: **51 records covering 17 page groups** in English (en-US), French for Morocco (fr-MA), and Modern Standard Arabic (ar-MA).

Each record contains a stable translation-group ID, slug, locale, source locale, workflow status, title, summary, Markdown body, SEO metadata, claim references, source references, owner, review date, text direction and publication gates.

## Workflow state
English records remain in editorial review. French and Arabic remain in translation review. None is approved or published. The current export contains claim references, but all 51 `sources` arrays are empty. Source mapping to primary evidence is therefore an outstanding publication gate; do not treat a valid claim ID as proof that the claim is approved.

## Validation
Run `python scripts/validate_content_export.py` from the repository root. It uses only the Python standard library and checks record count, uniqueness, locale coverage, RTL/LTR direction, review states and claim-reference integrity. Structural validation does not verify factual accuracy, source quality or human approval.

The Markdown bundles remain the human-readable editorial source. This JSON export is a portable interchange format for a future React, WordPress or headless-CMS importer. No live CMS is connected and nothing has been published.

See [the integration review](../architecture/integration-review-2026-11-17.md) for the current branch baseline, source-evidence gaps and safe integration sequence.
