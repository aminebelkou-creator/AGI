"""One-time conversion of the DC-runtime pages to plain static HTML."""
import os, re, json, subprocess, html
V2 = r"C:\Users\belko\AGI\v2"; os.chdir(V2)
PAGES = {  # old file -> (new file, <title>, meta description)
 "AGI Admissions.dc.html": ("admissions.html", "Admissions", "How to apply to American Group International in Agadir: steps, calendar, tuition and documents."),
 "AGI Program K12.dc.html": ("k12.html", "K–12 school", "An American-curriculum micro-school in Agadir, from kindergarten to grade 12, with English support through Anglia."),
 "AGI Partnerships.dc.html": ("partnerships.html", "Partnerships & franchise", "Franchise and institutional partnerships with AGI and Anglia Morocco across the Kingdom's twelve regions."),
 "AGI Connect.dc.html": ("connect.html", "AGI Connect (preview)", "A preview of AGI Connect, the school's planned digital front desk."),
 "AGI Journal.dc.html": ("journal.html", "Journal", "News, announcements and stories from American Group International and Anglia Morocco."),
 "AGI Journal Article.dc.html": ("journal-ccgi-partnership.html", "AGI and Anglia Morocco join forces with Chichester College Group International", "AGI and Anglia Morocco partner with Chichester College Group International, opening UK progression routes."),
}
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
def kind_of(t):
    s = t.lower()
    if re.search(r"partner|join forces|forces|member|leverage|bridge|chichester|ccgi|counselor", s): return "Partnership"
    if re.search(r"graduat|congrat|award|spelling bee|celebrat|honor", s): return "Achievement"
    if re.search(r"inscription|admission|back to school|school starts|first day|semester|summer school|calendar", s): return "Admissions"
    if re.search(r"course|program|training|diploma|class|testing|exam|proctor|resource|psychology", s): return "Programs"
    return "News"
def journal_ctx():
    posts = json.load(open("journal-posts.json", encoding="utf-8")); by = {}
    for p in posts:
        y, m, d = p["date"].split("-")
        by.setdefault(y, []).append({"date": f"{MONTHS[int(m)-1]} {int(d)}", "title": re.sub(r'^[“"]|[”"]$', "", p["title"]).replace("\u00a0", " "), "kind": kind_of(p["title"])})
    return {"years": [{"year": y, "count": f'{len(by[y])} {"entry" if len(by[y]) == 1 else "entries"}', "items": by[y]} for y in sorted(by, reverse=True)]}

def resolve(ctx, path):
    v = ctx
    for k in path.strip().split("."): v = v[k]
    return v
def render(tpl, ctx):
    out, i = [], 0
    open_re = re.compile(r'<sc-for\s+list="\{\{\s*([\w.]+)\s*\}\}"\s+as="(\w+)"[^>]*>')
    while True:
        m = open_re.search(tpl, i)
        if not m: out.append(tpl[i:]); break
        out.append(tpl[i:m.start()])
        depth, j = 1, m.end()
        while depth:
            a = tpl.find("<sc-for", j); b = tpl.find("</sc-for>", j)
            if a != -1 and a < b: depth += 1; j = a + 7
            else: depth -= 1; j = b + 9
        inner = tpl[m.end():j - 9]
        for item in resolve(ctx, m.group(1)):
            out.append(render(inner, {**ctx, m.group(2): item}))
        i = j
    s = "".join(out)
    return re.sub(r"\{\{\s*([\w.]+)\s*\}\}", lambda mm: html.escape(str(resolve(ctx, mm.group(1)))), s)

for old, (new, title, desc) in PAGES.items():
    s = open(old, encoding="utf-8").read()
    helmet = re.search(r"<helmet>(.*?)</helmet>", s, re.S).group(1)
    body = re.search(r"<x-dc>(.*?)</x-dc>", s, re.S).group(1)
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
    if "{{" in body: body = render(body, journal_ctx())
    assert "{{" not in body and "<sc-" not in body, old
    # hover styles -> CSS classes
    rules, n = [], 0
    def hov(m):
        global n
        tag = m.group(0); val = re.search(r'style-hover="([^"]*)"', tag).group(1)
        n += 1; cls = f"hv{n}"
        decl = ";".join(d.strip() + " !important" for d in val.split(";") if d.strip())
        rules.append(f".{cls}:hover{{{decl}}}")
        tag = re.sub(r'\s*style-hover="[^"]*"', "", tag)
        if re.search(r'\sclass="', tag): tag = re.sub(r'\sclass="', f' class="{cls} ', tag, count=1)
        else: tag = tag.replace(">", f' class="{cls}">', 1) if tag.endswith(">") else tag
        return tag
    body = re.sub(r"<[a-zA-Z][^>]*\sstyle-hover=\"[^\"]*\"[^>]*>", hov, body)
    # shared header/footer + main landmark
    body, h = re.subn(r"<header\b.*?</header>", "<!--site:header-->\n<!--/site:header-->\n<main id=\"main\">", body, count=1, flags=re.S)
    body, f = re.subn(r"<footer\b.*?</footer>", "</main>\n<!--site:footer-->\n<!--/site:footer-->", body, count=1, flags=re.S)
    assert h == 1 and f == 1, (old, h, f)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} – American Group International, Agadir</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" type="image/png" href="assets/favicon.png">
{helmet.strip()}
<style>{chr(10).join(rules)}</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""
    subprocess.run(["git", "mv", old, new], check=True)
    open(new, "w", encoding="utf-8", newline="").write(doc)
    print(f"{old} -> {new}  ({n} hover rules)")
