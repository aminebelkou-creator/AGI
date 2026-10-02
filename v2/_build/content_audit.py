import os, re, html, json
from collections import defaultdict
V2 = r"C:\Users\belko\AGI\v2"; os.chdir(V2)
pages = sorted(f for f in os.listdir(".") if f.endswith(".html"))
arts = sorted(os.path.join("journal", f) for f in os.listdir("journal"))
def text(f):
    s = open(f, encoding="utf-8").read()
    s = re.sub(r"<!--site:header-->.*?<!--/site:header-->|<!--site:footer-->.*?<!--/site:footer-->", " ", s, flags=re.S)
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()
T = {f: text(f) for f in pages}
A = {f: text(f) for f in arts}
def ctx(t, m, w=70): return "…" + t[max(0, m.start()-w):m.end()+w] + "…"

print("== 1. Leftovers / placeholders / stale wording")
for pat in [r"design preview", r"\bpreview\b", r"sample", r"lorem", r"placeholder", r"\bTBA\b", r"image:", r"\{\{", r"coming soon",
            r"Rachid", r"regional representative", r"Five (academic )?divisions", r"\bLive\b", r"2024[–-]2025|2025[–-]2026|2025[–-]26", r"September 8", r"mid-August",
            r"Country Manager", r"twenty-six", r"three multi-grade", r"18 years of age and older"]:
    for f, t in T.items():
        for m in re.finditer(pat, t, re.I):
            print(f"  [{pat}] {f}: {ctx(t, m)}")

print("\n== 2. Fact consistency across pages")
checks = {
 "monthly fee": r"\d[\d,]* MAD (?:a|per) month|\d[\d,]* MAD per month",
 "inscription": r"inscription[^.]{0,80}?\d[\d,]* MAD|\d[\d,]* MAD[^.]{0,40}inscription",
 "nationalities": r"\d+\+? nationalities",
 "years": r"(?:eleven|11|twelve|12|five|5|ten|10|thirteen|13) years",
 "classrooms": r"\w+ multi-grade classrooms",
 "regions": r"\w+ regions",
 "registration": r"(?:August|Aug) 28[^.]{0,20}31",
 "first day": r"(?:first day|classes begin)[^.]{0,40}September \d+|September \d+[^.]{0,30}first day",
 "graduation": r"(?:graduation|last day)[^.]{0,40}June \d+|June \d+[^.]{0,20}(?:graduation)",
 "phones": r"\+212[\d ]{9,14}",
 "emails": r"[\w.]+@[\w.]+\.\w+",
 "anglia since": r"(?:since|in) (?:19|20)\d\d[^.]{0,40}(?:franchise|Anglia)|franchise holder[^.]{0,30}(?:19|20)\d\d",
 "volunteer hours": r"\d+ (?:volunteer|service) hours",
 "attendance": r"\d+ ?% (?:of the (?:school )?year|attendance)",
 "pass mark": r"\d+ ?% \(D\)|\d+ percent|\d+%",
}
for name, pat in checks.items():
    found = defaultdict(set)
    for f, t in T.items():
        for m in re.finditer(pat, t, re.I): found[re.sub(r"\s+", " ", m.group(0)).strip()].add(f)
    print(f"  {name}:")
    for k, v in sorted(found.items()): print(f"     '{k}'  <- {', '.join(sorted(v))}")

print("\n== 3. Journal articles: empty or very short, and missing images")
for f, t in A.items():
    body = t.split("All journal entries")[0]
    words = len(body.split())
    if words < 60: print(f"  short ({words} words): {f}: {body[:110]}")
ext = sum(open(f, encoding='utf-8').read().count("americangroup-international.com/wp-content") for f in arts)
print(f"  images still loaded from the old WordPress site: {ext}")

print("\n== 4. Repeated words / common typos")
for f, t in T.items():
    for m in re.finditer(r"\b(\w{3,})\s+\1\b", t, re.I):
        if m.group(1).lower() not in ("that", "had"): print(f"  doubled '{m.group(0)}' in {f}: {ctx(t, m, 40)}")
    for m in re.finditer(r"\b(recieve|seperate|occured|enrol{1}ment|enrollement|accomodation|untill|wich|teh|definately|langauge|programme)\b", t, re.I):
        print(f"  spelling '{m.group(0)}' in {f}")
print("\n== 5. Spelling variants (US vs UK) used on the site")
for a, b in [("enrollment", "enrolment"), ("behavior", "behaviour"), ("program", "programme"), ("center", "centre"), ("organization", "organisation"), ("recognized", "recognised")]:
    ca = sum(len(re.findall(rf"\b{a}\w*", t, re.I)) for t in T.values()); cb = sum(len(re.findall(rf"\b{b}\w*", t, re.I)) for t in T.values())
    print(f"  {a}: {ca}   {b}: {cb}")
