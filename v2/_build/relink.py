import os, re, glob
os.chdir(r"C:\Users\belko\AGI\v2")
def rd(f): return open(f, encoding="utf-8", newline="").read()
def wr(f, s): open(f, "w", encoding="utf-8", newline="").write(s)

# forms.html: shared header/footer
s = rd("forms.html")
s, a = re.subn(r'<header class="top">.*?</header>', "<!--site:header-->\n<!--/site:header-->", s, count=1, flags=re.S)
s, b = re.subn(r"<footer>.*?</footer>", "<!--site:footer-->\n<!--/site:footer-->", s, count=1, flags=re.S)
s, c = re.subn(r"<main>", '<main id="main">', s, count=1)
assert (a, b, c) == (1, 1, 1), (a, b, c)
wr("forms.html", s)

# old file names and old home anchors -> new pages
HOME_ANCHORS = {"": "index.html", "#top": "index.html", "#programs": "programs.html", "#admissions": "admissions.html",
  "#services": "forms.html", "#connect": "connect.html", "#experience": "student-life.html", "#stories": "journal.html",
  "#fees": "admissions.html#fees", "#policies": "policies.html", "#curriculum": "k12.html", "#accreditation": "about.html#accreditation",
  "#english": "english-anglia.html", "#professional": "professional.html", "#partners": "partnerships.html"}
FILES = {"AGI Admissions.dc.html": "admissions.html", "AGI Program K12.dc.html": "k12.html", "AGI Partnerships.dc.html": "partnerships.html",
  "AGI Connect.dc.html": "connect.html", "AGI Journal.dc.html": "journal.html", "AGI Journal Article.dc.html": "journal-ccgi-partnership.html",
  "AGI Forms.html": "forms.html"}
def fix(m):
    url = m.group(2).replace("%20", " ")
    for old in ("AGI Preview.dc.html",):
        if url.startswith(old):
            anchor = url[len(old):]
            return m.group(1) + HOME_ANCHORS.get(anchor, "index.html") + m.group(3)
    for old, new in FILES.items():
        if url.startswith(old):
            return m.group(1) + new + url[len(old):] + m.group(3)
    return m.group(0)
total = 0
for f in sorted(glob.glob("*.html")):
    s = rd(f)
    t, n = re.subn(r'(href=")([^"]+)(")', lambda m: fix(m), s)
    changed = sum(1 for x, y in zip(re.findall(r'href="([^"]+)"', s), re.findall(r'href="([^"]+)"', t)) if x != y)
    if t != s: wr(f, t)
    total += changed; print(f"{f:34} links rewritten: {changed}")
left = [(f, u) for f in glob.glob("*.html") for u in re.findall(r'href="([^"]*(?:AGI%20|AGI |\.dc\.html)[^"]*)"', rd(f))]
print("old-style links left:", left[:10])
