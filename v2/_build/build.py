"""AGI v2 build: stamps the shared header and footer into every page.

Each page contains the markers
  <!--site:header-->...<!--/site:header-->   and   <!--site:footer-->...<!--/site:footer-->
Run:  python _build/build.py      (from the v2 folder or anywhere)
Edit the menu here, once, and every page updates.
"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROGRAMS = [
    ("k12.html", "K–12 school", "American curriculum, kindergarten to grade 12"),
    ("special-education.html", "Special education (SEN)", "IEPs, small groups, therapy support"),
    ("adult-diploma.html", "Adult high school diploma", "U.S. diploma for learners 16 and over"),
    ("english-anglia.html", "English & Anglia exams", "Anglia Morocco headquarters, classes and exams"),
    ("professional.html", "Teacher training & professional", "C.I.T.E., proctoring, business and medical English"),
    ("pathways.html", "University pathways", "Admissions agent for universities abroad"),
]
NAV = [("about.html", "About"), ("PROGRAMS", "Programs"), ("admissions.html", "Admissions"),
       ("student-life.html", "Student life"), ("journal.html", "Journal"),
       ("partnerships.html", "Partnerships"), ("contact.html", "Contact")]
# which menu item each page belongs to
SECTION = {p: "PROGRAMS" for p, _, _ in PROGRAMS}
SECTION.update({"programs.html": "PROGRAMS", "policies.html": "admissions.html", "journal-ccgi-partnership.html": "journal.html",
                "connect.html": "contact.html", "privacy.html": None, "terms.html": None, "forms.html": "FORMS", "index.html": None})

def cur(page, href):
    return ' aria-current="page"' if page == href else ""

def header(page):
    sec = SECTION.get(page, page)
    items = []
    for href, label in NAV:
        if href == "PROGRAMS":
            sub = "".join(f'<li><a href="{h}"{cur(page, h)}>{t}<small>{d}</small></a></li>' for h, t, d in PROGRAMS)
            sub += f'<li><a class="all" href="programs.html"{cur(page, "programs.html")}>All programs</a></li>'
            mark = " data-current" if sec == "PROGRAMS" else ""
            items.append(f'<li class="has-menu"><button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu-programs"{mark}>Programs</button>'
                         f'<ul class="submenu" id="menu-programs" hidden>{sub}</ul></li>')
        else:
            on = ' aria-current="page"' if (page == href or sec == href) else ""
            items.append(f'<li><a href="{href}"{on}>{label}</a></li>')
    mob = []
    for href, label in NAV:
        if href == "PROGRAMS":
            mob.append(f'<li><a href="programs.html"{cur(page, "programs.html")}>Programs</a></li>')
            mob += [f'<li class="sub"><a href="{h}"{cur(page, h)}>{t}</a></li>' for h, t, _ in PROGRAMS]
        else:
            mob.append(f'<li><a href="{href}"{cur(page, href)}>{label}</a></li>')
    mob.append(f'<li><a href="forms.html"{cur(page, "forms.html")}>Forms &amp; requests</a></li>')
    fcur = ' aria-current="page"' if page == "forms.html" else ""
    return f"""<!--site:header-->
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="AGI – American Group International School, home"><img src="assets/favicon.png" alt="" width="44" height="44"><span class="brand-name">AGI</span><span class="brand-sub">American Group International School · Agadir</span></a>
    <nav class="primary" aria-label="Main"><ul>{"".join(items)}</ul></nav>
    <div class="head-actions">
      <a class="util" href="forms.html"{fcur}>Forms</a>
      <a class="btn btn-primary" href="forms.html#enrollment">Apply</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu"><span></span></button>
    </div>
  </div>
  <nav class="mobile-menu" id="mobile-menu" aria-label="Mobile" hidden><ul>{"".join(mob)}</ul>
    <div class="wrap" style="padding-bottom:28px"><a class="btn btn-primary" href="forms.html#enrollment">Apply</a></div></nav>
</header>
<!--/site:header-->"""

def footer(page):
    progs = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t, _ in PROGRAMS)
    return f"""<!--site:footer-->
<footer class="site-footer">
  <div class="wrap cols">
    <div class="about">
      <a class="brand" href="index.html"><img src="assets/favicon.png" alt="" width="44" height="44"><span class="brand-name">AGI</span></a>
      <p>American Group International – the first American school in Agadir, since 2013, and headquarters of Anglia Examinations in Morocco.</p>
    </div>
    <div><h2>Programs</h2><ul>{progs}</ul></div>
    <div><h2>School</h2><ul><li><a href="about.html">About AGI</a></li><li><a href="admissions.html">Admissions</a></li><li><a href="admissions.html#fees">Tuition &amp; fees</a></li><li><a href="policies.html">Policies</a></li><li><a href="student-life.html">Student life</a></li><li><a href="journal.html">Journal</a></li></ul></div>
    <div><h2>Services</h2><ul><li><a href="forms.html">Forms &amp; requests</a></li><li><a href="forms.html#absence">Report an absence</a></li><li><a href="forms.html#documents">Request a document</a></li><li><a href="forms.html#visit">Book a visit</a></li><li><a href="partnerships.html">Partnerships &amp; franchise</a></li><li><a href="connect.html">AGI Connect (preview)</a></li><li><a href="https://angliamorocco.org/" target="_blank" rel="noopener">Anglia Morocco ↗</a></li></ul></div>
    <div><h2>Contact</h2><address>Number 20, Rue Baalabek<br>Hay Nahda, Agadir 80000<br>Morocco</address>
      <ul style="margin-top:14px"><li><a href="tel:+212528843349">+212 528 843 349</a></li><li><a href="tel:+212618639911">+212 618 639 911</a> <span style="color:rgba(255,255,255,.45);font-size:13px">Arabic</span></li><li><a href="https://wa.me/212688739393">WhatsApp +212 688 739 393</a></li><li><a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a></li></ul></div>
  </div>
  <div class="wrap bottom"><span>© 2026 American Group International · Agadir, Morocco</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="contact.html">Contact</a></span></div>
</footer>
<a class="wa-float" href="https://wa.me/212688739393?text=Hello%20AGI%2C%20" target="_blank" rel="noopener" aria-label="Message AGI on WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg><span>WhatsApp</span></a>
<!--/site:footer-->"""


SITE_URL = "https://www.americangroup-international.com"   # VERIFY: final domain for the new site
OG_IMAGE = "assets/web/agi-seal-520.png"                      # VERIFY: replace with a real campus photo (1200x630)
SCHOOL_JSONLD = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"School","name":"American Group International School","alternateName":"AGI","url":"%s/","logo":"%s/assets/web/agi-seal-520.png","foundingDate":"2013","telephone":"+212528843349","email":"americanecoleagadir@gmail.com","address":{"@type":"PostalAddress","streetAddress":"Number 20, Rue Baalabek, Hay Nahda","addressLocality":"Agadir","postalCode":"80000","addressCountry":"MA"},"sameAs":[]}</script>""" % (SITE_URL, SITE_URL)

def seo_block(rel, s):
    title = re.search(r"<title>(.*?)</title>", s, re.S); desc = re.search(r'<meta name="description" content="([^"]*)"', s)
    t = title.group(1).strip() if title else "American Group International"; d = desc.group(1) if desc else ""
    url = SITE_URL + "/" + ("" if rel == "index.html" else rel)
    tags = [f'<link rel="canonical" href="{url}">', '<meta property="og:site_name" content="American Group International">',
            f'<meta property="og:type" content="{"article" if rel.startswith("journal/") else "website"}">',
            f'<meta property="og:title" content="{t}">', f'<meta property="og:description" content="{d}">',
            f'<meta property="og:url" content="{url}">', f'<meta property="og:image" content="{SITE_URL}/{OG_IMAGE}">',
            '<meta name="twitter:card" content="summary_large_image">']
    if rel == "index.html": tags.append(SCHOOL_JSONLD)
    return "<!--site:seo-->\n" + "\n".join(tags) + "\n<!--/site:seo-->"

HEAD_LINKS = '<link rel="stylesheet" href="site.css">\n<script src="site.js" defer></script>'

def prefixed(block, prefix):
    if not prefix: return block
    return re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/|\.\./)', lambda m: f'{m.group(1)}="{prefix}', block)

def stamp(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    depth = rel.count("/"); prefix = "../" * depth
    page = rel if depth == 0 else rel  # e.g. "journal/x.html"
    key = page if depth == 0 else "journal.html"   # menu section for sub-folder pages
    s = open(path, encoding="utf-8", newline="").read()
    for name, fn in (("header", header), ("footer", footer)):
        pat = re.compile(r"<!--site:%s-->.*?<!--/site:%s-->" % (name, name), re.S)
        if not pat.search(s):
            raise SystemExit(f"{page}: missing <!--site:{name}--> markers")
        block = fn(key)
        if depth:  # in sub-folders nothing is the current page itself, only its section
            block = block.replace(' aria-current="page"', "") if name == "footer" else block
        s = pat.sub(lambda m: prefixed(block, prefix), s, count=1)
    block = seo_block(rel, s)
    if "<!--site:seo-->" in s:
        s = re.sub(r"<!--site:seo-->.*?<!--/site:seo-->", lambda m: block, s, count=1, flags=re.S)
    else:
        s = s.replace("</head>", block + "\n</head>", 1)
    if 'site.css"' not in s:
        s = s.replace("</head>", HEAD_LINKS.replace('href="site', f'href="{prefix}site').replace('src="site', f'src="{prefix}site') + "\n</head>", 1)
    open(path, "w", encoding="utf-8", newline="").write(s)
    return page

def pages():
    for d in ("", "journal"):
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base): continue
        for f in sorted(os.listdir(base)):
            fp = os.path.join(base, f)
            if f.endswith(".html") and not f.startswith("_") and "<!--site:header-->" in open(fp, encoding="utf-8").read():
                yield fp

if __name__ == "__main__":
    done = [stamp(fp) for fp in pages()]
    top = [d for d in done if "/" not in d]
    print(f"stamped {len(done)} pages:", ", ".join(top), f"+ {len(done) - len(top)} journal articles")
