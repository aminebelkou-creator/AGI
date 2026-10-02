"""Page-level audit: titles, descriptions, headings, images, links, weight."""
import os, re, html
from collections import Counter
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(V2)
pages = sorted(f for f in os.listdir(".") if f.endswith(".html"))
arts = sorted("journal/" + f for f in os.listdir("journal") if f.endswith(".html"))
issues, titles, rows = [], Counter(), []
def size_of(src, base):
    p = os.path.normpath(os.path.join(os.path.dirname(base), src.split("?")[0]))
    return os.path.getsize(p) if os.path.exists(p) else 0
for f in pages + arts:
    s = open(f, encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", s, re.S); t = html.unescape(t.group(1).strip()) if t else ""
    d = re.search(r'<meta name="description" content="([^"]*)"', s); d = html.unescape(d.group(1)) if d else ""
    titles[t] += 1
    body = s.split("<!--/site:header-->")[-1]
    h1 = len(re.findall(r"<h1\b", body))
    imgs = re.findall(r"<img\b[^>]*>", s)
    no_alt = [i for i in imgs if not re.search(r'\salt="', i)]
    big = sum(size_of(m, f) for m in re.findall(r'<img[^>]*\ssrc="([^"]+)"', s) if not m.startswith("http") and 'loading="lazy"' not in m)
    empty_links = len(re.findall(r"<a\b[^>]*>\s*</a>", s))
    blank_no_rel = [a for a in re.findall(r'<a\b[^>]*target="_blank"[^>]*>', s) if "noopener" not in a]
    heads = [int(x) for x in re.findall(r"<h([1-6])\b", body)]
    jumps = sum(1 for a, b in zip(heads, heads[1:]) if b - a > 1)
    weight = len(s.encode()) + sum(size_of(m, f) for m in set(re.findall(r'<img[^>]*\ssrc="([^"]+)"', s)) if not m.startswith("http"))
    rows.append((f, len(t), len(d), h1, len(imgs), len(no_alt), jumps, weight // 1024))
    if not t: issues.append((f, "missing <title>"))
    elif len(t) > 70: issues.append((f, f"title long ({len(t)} chars)"))
    if not d: issues.append((f, "missing meta description"))
    elif len(d) > 165: issues.append((f, f"description long ({len(d)})"))
    elif len(d) < 70: issues.append((f, f"description short ({len(d)})"))
    if h1 != 1: issues.append((f, f"{h1} <h1> elements"))
    if no_alt: issues.append((f, f"{len(no_alt)} images without alt"))
    if empty_links: issues.append((f, f"{empty_links} empty links"))
    if blank_no_rel: issues.append((f, f"{len(blank_no_rel)} target=_blank without rel=noopener"))
    if jumps: issues.append((f, f"{jumps} heading level jumps (e.g. h2 -> h4)"))
    if 'lang="en"' not in s[:300]: issues.append((f, "missing lang attribute"))
    if 'name="viewport"' not in s: issues.append((f, "missing viewport"))
for t, n in titles.items():
    if n > 1: issues.append(("(site)", f"title used {n}x: {t[:60]}"))
print(f"pages checked: {len(pages)} + {len(arts)} articles")
print(f"{'page':38} title desc h1 imgs noalt hjump KB")
for r in rows[:len(pages)]: print(f"{r[0]:38} {r[1]:5} {r[2]:4} {r[3]:2} {r[4]:4} {r[5]:5} {r[6]:5} {r[7]}")
heaviest = sorted(rows, key=lambda r: -r[7])[:5]
print("heaviest pages (HTML + local images, KB):", [(r[0], r[7]) for r in heaviest])
print(f"\nISSUES ({len(issues)}):")
by = Counter(i[1].split(" (")[0] for i in issues)
for k, v in by.most_common(): print(f"  {v:3}x {k}")
print("\nexamples:")
for f, msg in issues[:40]: print(f"  {f}: {msg}")
