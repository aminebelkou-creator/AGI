"""Content quality audit of the English pages: wrong language, unformatted text, leftovers, duplicates.
python _build/content_quality.py  -> summary + docs/content-quality.csv (one row per finding)"""
import os, re, html, csv
from collections import Counter, defaultdict
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
FR = set("le la les des est et pour avec une un du dans sur que qui vous nous sont aux au ce cette ces leur leurs pas plus être été par".split())
EN = set("the and for with is are to of in on that this you we our your be was were by not from".split())
JUNK = [(r"\[(?!to confirm|TO CONFIRM)[a-z_-]+[^\]]*\]", "WordPress shortcode"), (r"Leave a Reply|Cancel reply|Posted in|Share this|Like this:|Related posts?", "WordPress leftover"),
        (r"\bClick here\b|\bclick here\b|cliking here|Show the Way", "'Click here' link text"), (r"u003c|u003e|&lt;|&gt;|\\u00", "Escaped HTML code"),
        (r"Ã.|â€|Â|ï»¿|�", "Broken characters (encoding)"), (r"https?://\S{25,}", "Raw URL in text"), (r"Lorem ipsum", "Placeholder Latin"),
        (r"\b(?:Elementor|elementor|wp-content|WordPress)\b", "Builder/CMS leftover"), (r"#\w+\s+#\w+", "Hashtags"),
        (r"The form has been submitted|There has been some error|No matching forms found", "Old form message")]
def main_text(s):
    s = re.sub(r"<!--site:(header|footer|seo)-->.*?<!--/site:\1-->", " ", s, flags=re.S)
    m = re.search(r"<main\b.*?</main>", s, re.S); s = m.group(0) if m else s
    s = re.sub(r"<(script|style|svg|nav|aside)\b.*?</\1>", " ", s, flags=re.S)
    blocks = [(t, b) for t, a, b in re.findall(r"<(p|li|h[1-6]|td|dd|dt|blockquote|figcaption)\b([^>]*)>(.*?)</\1>", s, re.S) if "lang=" not in a and "ph-text" not in b]
    return [(t, re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b))).strip()) for t, b in blocks]
rows, per_page = [], defaultdict(Counter)
files = [f for f in sorted(os.listdir(V2)) if f.endswith(".html")] + ["journal/" + f for f in sorted(os.listdir(os.path.join(V2, "journal"))) if f.endswith(".html")]
for f in files:
    blocks = main_text(open(os.path.join(V2, f), encoding="utf-8").read())
    def add(kind, txt):
        per_page[f][kind] += 1
        if per_page[f][kind] <= 3: rows.append((f, kind, txt[:160]))
    seen = Counter(); short_run = 0
    for tag, t in blocks:
        if not t: continue
        words = re.findall(r"[A-Za-zÀ-ÿ']+", t.lower())
        if len(re.findall(r"[\u0600-\u06ff]", t)) > 8: add("Arabic text on an English page", t)
        elif len(words) >= 8:
            fr = sum(w in FR for w in words); en = sum(w in EN for w in words)
            if fr >= 4 and fr > en * 1.5 or re.search(r"[éèêàçù].*[éèêàçù].*[éèêàçù]", t) and fr >= 3: add("French text on an English page", t)
        for rx, kind in JUNK:
            if re.search(rx, t): add(kind, t)
        if tag == "p" and len(t.split()) > 160: add("Very long paragraph (>160 words)", t)
        if tag == "p" and (len(re.findall(r"\s[•·▪]\s|\s-\s[A-Z]", t)) >= 3 or len(re.findall(r"(?:^|\s)\d{1,2}[.)]\s+[A-Z]", t)) >= 3): add("List run together in one paragraph", t)
        if tag == "p" and len(t.split()) >= 8 and t.upper() == t and len(re.findall(r"[A-Z]", t)) > 0.5 * len(re.sub(r"\W", "", t)): add("ALL-CAPS paragraph", t)
        if tag == "p" and 0 < len(t.split()) <= 2 and not re.search(r"\d", t): short_run += 1
        else:
            if short_run >= 5: add("Run of one/two-word lines (broken list or table)", f"{short_run} short lines in a row")
            short_run = 0
        if len(t) > 40:
            seen[t] += 1
            if seen[t] == 2: add("Duplicated paragraph", t)
    if short_run >= 5: add("Run of one/two-word lines (broken list or table)", f"{short_run} short lines in a row")
with open(os.path.join(ROOT, "docs", "content-quality.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["page", "issue", "example"]); w.writerows(rows)
tot = Counter(); pages = Counter()
for f, c in per_page.items():
    for k, n in c.items(): tot[k] += n; pages[k] += 1
print(f"pages scanned: {len(files)} (English; fr/ and ar/ excluded) · pages with issues: {len(per_page)}")
print(f"{'issue':52} {'findings':>8} {'pages':>6}")
for k, n in tot.most_common(): print(f"{k:52} {n:8} {pages[k]:6}")
print("\nworst pages:")
for f, c in sorted(per_page.items(), key=lambda x: -sum(x[1].values()))[:15]: print(f"  {sum(c.values()):3}  {f:60} {dict(c)}")
print("\nexamples:")
shown = Counter()
for f, k, t in rows:
    if shown[k] < 2: shown[k] += 1; print(f"  [{k}] {f}: {t[:130]}")
