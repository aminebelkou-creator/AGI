"""Page review: repetition, duplicate pages, claims that came back, stale dates, leftovers, length.
python _build/page_review.py -> ranked list + docs/page-review.csv"""
import os, re, html, csv, json
from collections import defaultdict
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
CLAIMS = {r"Ministry of Education": "Claim #1 (UK Ministry)", r"British Council": "Claim #1 (British Council)", r"\bQCA\b|Qualifications and Curriculum Authority": "Claim #1 (QCA)",
          r"ASCENTIS": "Claim #1 (ASCENTIS)", r"Director of (?:Global )?Operations": "Claim #5 (title)", r"\bexclusive\b": "Claim (exclusive)", r"Rachid Oussalh": "Person removed by Julie",
          r"Country Manager": "Claim #5 (title)", r"\b45\+? nationalities|45 different nationalities": "Claim #3 (45 vs 46)", r"correspondence (?:school|institution)|Correspondence as your": "Claim #4 (correspondence)",
          r"Mauritania": "Expansion claim", r"Lorem ipsum": "Placeholder Latin"}
LEFTOVER = r"^(?:Read more|Read More|Apply Now!?|Enroll Now|Learn More|Contact Us|Register Now|Book Now|Download|Submit|Share|Previous|Next)$"
def blocks(s):
    s = re.sub(r"<!--site:(header|footer|seo)-->.*?<!--/site:\1-->", " ", s, flags=re.S)
    m = re.search(r"<main\b.*?</main>", s, re.S); s = m.group(0) if m else s
    s = re.sub(r"<(script|style|nav|aside)\b.*?</\1>", " ", s, flags=re.S)
    return [(t, re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b))).strip()) for t, a, b in re.findall(r"<(p|li|h[1-6]|td|dd|dt|blockquote)\b([^>]*)>(.*?)</\1>", s, re.S) if "lang=" not in a]
def sents(txt): return {re.sub(r"\W+", " ", x.lower()).strip() for x in re.split(r"(?<=[.!?])\s+", txt) if len(x) > 50}
pages = [f for f in sorted(os.listdir(V2)) if f.endswith(".html")]
data, rows = {}, []
for f in pages:
    raw = open(os.path.join(V2, f), encoding="utf-8").read(); B = blocks(raw)
    text = " ".join(t for _, t in B); words = len(text.split()); flags = []
    # 1. top summary repeated by the appended full text (sections injected or "In detail")
    cut = max(raw.find("<!--p1:"), raw.find('id="details"'), raw.find(">In detail<"), raw.find("in full</h2>"))
    if cut > 0:
        top = sents(re.sub(r"<[^>]+>", " ", raw[:cut])); bottom = sents(re.sub(r"<[^>]+>", " ", raw[cut:]))
        dup = len(top & bottom)
        if dup >= 2: flags.append(("Summary repeated in the full text below", f"{dup} sentences appear twice"))
    # 2. claims that came back
    for rx, lab in CLAIMS.items():
        m = re.search(rx, text, re.I)
        if m and "TO CONFIRM" not in text[max(0, m.start() - 40):m.end() + 40]: flags.append((lab, text[max(0, m.start() - 60):m.end() + 60]))
    # 3. stale dates on permanent pages
    if not f.startswith("journal"):
        for m in re.finditer(r"\b20(?:1[5-9]|2[0-4])\b|2025[-–]2026|2025-26", text):
            ctx = text[max(0, m.start() - 50):m.end() + 50]
            if not re.search(r"since|founded|established|in 20|archive|2013|copyright|©|effective|published|2021, AGI|franchise", ctx, re.I):
                flags.append(("Date that may be outdated", ctx)); break
    # 4. leftovers + orphan headings
    for i, (t, x) in enumerate(B):
        if re.match(LEFTOVER, x): flags.append(("Old-site button text", x))
        if t in ("h2", "h3") and (i + 1 == len(B) or B[i + 1][0] in ("h2", "h3") and B[i + 1][0] <= t): flags.append(("Heading with nothing under it", x))
    # 5. length
    if words > 3500: flags.append(("Very long page", f"{words} words"))
    data[f] = sents(text)
    for k, v in flags: rows.append((f, k, v[:150]))
# duplicate pages (shared sentences)
names = list(data)
for i, a in enumerate(names):
    for b in names[i + 1:]:
        sh = len(data[a] & data[b])
        if sh >= 6 and sh >= 0.25 * min(len(data[a]), len(data[b])): rows.append((a, "Overlaps another page", f"{sh} sentences shared with {b}"))
with open(os.path.join(ROOT, "docs", "page-review.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["page", "flag", "detail"]); w.writerows(rows)
by_page = defaultdict(list)
for f, k, v in rows: by_page[f].append((k, v))
kinds = defaultdict(int)
for f, k, v in rows: kinds[k] += 1
print(f"pages reviewed: {len(pages)} · flagged: {len(by_page)} · findings: {len(rows)}\n")
for k, n in sorted(kinds.items(), key=lambda x: -x[1]): print(f"  {n:3}  {k}")
print()
for f, L in sorted(by_page.items(), key=lambda x: -len(x[1])):
    print(f"{f}  ({len(L)})")
    seen = set()
    for k, v in L:
        if k in seen: continue
        seen.add(k); print(f"    - {k}: {v[:120]}")
