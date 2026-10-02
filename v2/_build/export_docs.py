import os, re, html, subprocess
ROOT = r"C:\Users\belko\AGI"; DOCS = os.path.join(ROOT, "docs"); os.makedirs(DOCS, exist_ok=True)

# 1) founder's letter as editable Markdown (taken from the published page so they stay identical)
s = open(os.path.join(ROOT, "v2", "founder-letter.html"), encoding="utf-8").read()
art = re.search(r'<article class="letter"[^>]*>(.*?)</article>', s, re.S).group(1)
paras = []
for p in re.findall(r"<p[^>]*>(.*?)</p>", art, re.S):
    p = re.sub(r'<span class="ph-text"[^>]*>(.*?)</span>', r"[TO CONFIRM: \1]", p)
    p = re.sub(r"</?strong>", "**", p); p = re.sub(r"</?em>", "*", p)
    p = re.sub(r"<b>(.*?)</b>", r"**\1**  \n", p)
    paras.append(html.unescape(re.sub(r"<[^>]+>", "", p)).strip())
open(os.path.join(DOCS, "founder-letter.md"), "w", encoding="utf-8").write(
    "# A letter from our founder\n\n> Draft for Julie's approval. Published on the site at `v2/founder-letter.html` "
    "(text generated from `v2/_build/audiences.py`). Items marked [TO CONFIRM] are highlighted on the site until approved.\n\n"
    + "\n\n".join(paras) + "\n")
print("docs/founder-letter.md")
