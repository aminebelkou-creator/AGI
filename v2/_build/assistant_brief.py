"""Writes docs/AI-ASSISTANT-BRIEF.md: the instructions for Julie's AI assistant (verification before launch + CMS migration).
Generated from facts.json, claims.json, privacy.json, LAUNCH-CHECKLIST.md and the audit CSVs – re-run after every change:
python _build/assistant_brief.py"""
import os, json, csv, re, datetime
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2); B = os.path.join(V2, "_build"); D = os.path.join(ROOT, "docs")
facts = json.load(open(os.path.join(B, "facts.json"), encoding="utf-8")); claims = json.load(open(os.path.join(B, "claims.json"), encoding="utf-8"))
priv = json.load(open(os.path.join(B, "privacy.json"), encoding="utf-8")) if os.path.exists(os.path.join(B, "privacy.json")) else {"hide_photos": [], "approved": []}
def rows(name):
    p = os.path.join(D, name)
    return list(csv.DictReader(open(p, encoding="utf-8-sig"))) if os.path.exists(p) else []
chk, sec = [], ""
for l in open(os.path.join(V2, "LAUNCH-CHECKLIST.md"), encoding="utf-8").read().split("\n"):
    if l.startswith("## "): sec = l[3:].strip()
    elif l.strip().startswith("- [ ]"): chk.append((sec, l.strip()[6:]))
pending_photos = [p for p in priv.get("hide_photos", []) if p not in priv.get("approved", []) and p.startswith("journal/")]
names = [r for r in rows("privacy-review.csv") if r["issue"] == "Possible child's name"]
edit = rows("content-quality.csv")
L = []
A = L.append
A(f"# Brief for Julie's AI assistant – American Group International website")
A(f"*Generated {datetime.date.today():%B %d, %Y} by `v2/_build/assistant_brief.py` from the project's registers. Re-generate after every change; do not edit by hand.*\n")
A("""## 1. Who you are working for and what the job is

You are helping **Julie A. Wilburn** (Founder · CEO & Educational Director, American Group International of Agadir · Anglia Examinations Morocco) verify the new website of her school before it launches. The site is built and every page exists. Your job is to **ask Julie the questions below, one topic at a time, record her answers in the right file, and never publish anything she has not confirmed.**

- Preview: https://agi-preview.vercel.app (not indexed by search engines). French: `/fr/`, Arabic: `/ar/`.
- Text in **gold** on a page = a fact waiting for confirmation. A grey **"Photo"** frame = a photo to supply. "Photo hidden until parental consent is confirmed" = privacy hold.
- The site will move to a CMS (Sitewright) where you will edit it through MCP. Section 7 explains what must survive the move.

## 2. Rules you must follow

1. **Ask, never guess.** If Julie does not know or is unsure, leave the item open. A placeholder is better than a wrong fact.
2. **Children's privacy (Moroccan law 09-08).** Never show a child's name or photo unless Julie confirms *written parental consent* is on file for that child. When in doubt, keep it hidden.
3. **Third-party data.** No personal email, phone or address of anyone outside AGI without their agreement.
4. **Anglia wording.** Use only: "official partner in Morocco of Chichester College Group, UK"; "the four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual"; "the Mastery (C2) qualification carries UCAS tariff points". Do **not** write that Anglia depends on the UK Ministry of Education, is recognized by the British Council, or is accredited by QCA, unless Anglia confirms it in writing.
5. **Copyright.** Do not paste text, tests or images from other organizations (the old Pearson "Total English" placement test was removed for this reason).
6. **Fees and dates live in one place** (`v2/_build/facts.json`). Change them there, never on a single page.
7. **One email per purpose.** Official contact: americanecoleagadir@gmail.com; Anglia Morocco: j.wilburn@ / a.lam@angliamorocco.org.
8. **Tone:** warm, direct, parent-first, US English. Keep AGI's own wording in policies and the handbook; suggest edits, don't impose them.
9. **Keep the safety nets:** after any change run the checks in section 6; the launch is allowed only when `prelaunch.py` says **READY FOR LAUNCH**.
""")
A("## 3. Questions to ask Julie\n")
A("### 3.1 Claims to confirm or correct\n")
for c in claims:
    if c["status"] == "open": A(f"- **[{c['id']}]** {c['claim']} — *needed:* {c['decision']}")
A("\n### 3.2 Facts to confirm (each appears in gold on the site)\n")
for g, items in facts.items():
    for k, f in items.items():
        if f.get("status") == "to-confirm":
            v = f.get("value"); v = "not known yet" if v in (None, "") else (", ".join(v) if isinstance(v, list) else (json.dumps(v, ensure_ascii=False) if isinstance(v, dict) else str(v)))
            if len(v) > 140: v = v[:140] + "…"
            A(f"- **{g} › {k}:** {v}" + (f" — {f['note']}" if f.get("note") else ""))
A(f"\n### 3.3 Privacy – needs Julie's decision\n")
A(f"- **{len(pending_photos)} journal posts** show *\"Photo hidden until parental consent is confirmed\"*. For each post, ask whether written consent exists for every child in its photos. Only then add the page to `approved` in `v2/_build/privacy.json`:")
for p in pending_photos: A(f"  - `{p}`")
if names:
    A(f"- **{len(names)} possible names** were found near words like student/son/daughter/birthday (most are ordinary words). Ask Julie to confirm none is a child's name:")
    for r in names: A(f"  - `{r['page']}`: {r['detail']}")
A("- Special education: a 2024 parent letter naming a child is hidden. Publish only with the family's written consent.")
A(f"\n### 3.4 Launch checklist ({len(chk)} open items)\n")
last = None
for s_, item in chk:
    if s_ != last: A(f"\n**{s_}**"); last = s_
    A(f"- {item}")
A(f"\n### 3.5 Editorial suggestions ({len(edit)}) – AGI's own texts, Julie decides\n")
A("Long paragraphs, repetitions and wording in imported texts are listed in `docs/editorial-review.md`. Offer rewrites; apply only what Julie approves.\n")
A("""### 3.6 Material to collect
- Photos for every grey "Photo" frame (landscape, good light; only children with photo consent).
- 3–6 real testimonials with written permission (`docs/parent-stories-guide.md`); the current ones are samples and must be replaced.
- 2026–27 Saturday class schedule; current team list with roles and portraits.
- A qualified person to review Privacy, Terms, Cookies and the consent forms.
- Native speakers to review the French (`fr/`) and Arabic (`ar/`) pages.

## 4. Where each answer goes

| Answer | File | How |
|---|---|---|
| Fee, date, contact, number | `v2/_build/facts.json` | set `value`, `status: "confirmed"` |
| Claim decided | `v2/_build/claims.json` | `status: "confirmed"` / `"rejected"` + note; then update the page text |
| Gold text on a page | the generator in `v2/_build/` that writes it (search the key, e.g. `PH_TXT("faq-hours"`) | replace `PH_TXT(...)` by the final text |
| Photo consent | `v2/_build/privacy.json` | add the page to `approved` |
| Checklist item | `v2/LAUNCH-CHECKLIST.md` | `- [x]` |
| Real testimonial | `TESTIMONIALS` in `v2/_build/pages.py` | replace the sample, remove the sample marker |
| Photo | `v2/assets/web/` + `python _build/webp.py` | replace the slot (`data-placeholder="photo:…"`) |

## 5. Map of the documents
- `docs/julie-questions.md` – the same questions, as a printable list
- `docs/rebuild-plan-v3.md` – how the content was rebuilt from both old sites
- `docs/content-map.csv` – every old page → new page (181 sources)
- `docs/privacy-review.csv`, `docs/editorial-review.md`, `docs/page-review.csv`, `docs/content-quality.csv`, `docs/fact-conflicts.csv` – audits
- `docs/website-content-spec.md` – the whole site as plain content (useful for the CMS import)
- `README.md` – how everything is built

## 6. Checks to run after every change (from `v2/`)
```
python _build/pages.py ; python _build/journal.py ; python _build/launch_assets.py ; python _build/build.py
python _build/coverage_gate.py        # every fact from the old sites still present
python _build/linkcheck.py            # 0 broken links
python _build/privacy_scan.py         # children's names/photos
python _build/content_quality.py      # language, leftovers, formatting
python _build/prelaunch.py            # must say READY FOR LAUNCH before going live
python _build/assistant_brief.py      # regenerate this brief
```

## 7. Moving to the CMS (Sitewright) – what must survive
- **Every page and URL** (146 pages incl. `fr/` and `ar/`), and the **147 redirects** from the old WordPress addresses (`v2/_build/redirects.csv`, `.htaccess`).
- **The markers:** `data-placeholder="photo|fact|testimonial|team:…"` and `data-verify="…"` – they are how unfinished items are found. Keep them until each item is resolved.
- **Global settings:** the fact register (fees, dates, contacts) should become CMS global fields used by every page.
- **Privacy holds:** hidden photos stay hidden until approved; the "Archived post" banner on journal posts older than 12 months.
- **Languages:** `lang`/`dir` attributes, the EN · FR · ع switch, `hreflang` links, right-to-left layout for Arabic.
- **SEO:** titles, descriptions, canonical URLs, School and FAQ structured data, sitemap, `noindex` on previews only.
- **Forms:** 10 forms + contact; the payment form never collects card numbers.
- **Performance and accessibility:** WebP images, non-blocking fonts, WCAG AA contrast – re-test with Lighthouse after migration.

## 8. When everything is answered
1. All gold text, grey frames and privacy holds resolved; `prelaunch.py` → **READY FOR LAUNCH**.
2. Final domain set (`SITE_URL`), redirects tested, forms connected to a backend, sitemap submitted to Google Search Console.
3. Julie gives the final go-ahead. Only then publish.
""")
open(os.path.join(D, "AI-ASSISTANT-BRIEF.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"docs/AI-ASSISTANT-BRIEF.md: {sum(1 for c in claims if c['status']=='open')} claims · {sum(1 for g in facts.values() for f in g.values() if f.get('status')=='to-confirm')} facts · {len(pending_photos)} photo holds · {len(names)} names · {len(chk)} checklist items")
