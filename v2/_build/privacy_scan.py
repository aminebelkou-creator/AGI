"""Privacy scan: children's names, personal contact details, photos in posts about children.
python _build/privacy_scan.py -> docs/privacy-review.csv + v2/_build/privacy.json (pages whose photos stay hidden until approved)
Approve a page: add it to "approved" in privacy.json (after written parental consent), then rebuild."""
import os, re, html, csv, json
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
ADULTS = set("""Julie Wilburn Abdelhak Lam Latifa Amhari Mohamed Saih Rachid Oussalh Kamal Sarjdine Said El Ouahbi Suzanne Linsen Brahim Robio Mrs Mr Dr Professor Prof
Director Dear Sincerely Agadir Morocco Moroccan American Group International AGI Anglia English Grade School Class Congratulations Happy Birthday Graduation Graduates Christmas
Halloween Ramadan Eid New Year Saturday Sunday Monday Tuesday Wednesday Thursday Friday January February March April May June July August September October November December
The This Our We They He She His Her Their All Each Every In On At For And With From Students Student Parents Teachers Teacher Kindergarten High Middle Elementary Anglia's
Chichester College Group UK USA United States Spelling Bee Tangier Casablanca Marrakech Fes Rabat Essaouira Ben Bouskoura Castle STEM CITE TESOL Global Schools Program ASCA""".split())
KIDS = r"son|daughter|child|children|kid|kids|student|students|pupil|boy|girl|grandson|granddaughter|birthday|graduate|graduates|graduation|class of|little one"
NAME = r"([A-Z][a-z]{2,}(?:\s[A-Z][a-z]{2,})?)"
PHOTO_TOPICS = r"birthday|party|halloween|christmas|celebration|class|classes|students|kids|children|graduat|park|outing|field trip|spelling bee|fun|seamstress|burger|award|back to school|holiday|new year"
AGI_MAIL = {"name@example.com", "americanecoleagadir@gmail.com", "j.wilburn@angliamorocco.org", "a.lam@angliamorocco.org", "groupinternationala@gmail.com", "agiangliama@gmail.com", "info@anglia.org"}
AGI_TEL = {"612345678", "528843349", "618639911", "688739393"}
def main_html(s):
    m = re.search(r"<main\b.*?</main>", s, re.S); return m.group(0) if m else ""
# words that also appear in lowercase anywhere on the site are ordinary words, not first names
LOWER_VOCAB = set()
for _f in [f for f in os.listdir(V2) if f.endswith(".html")] + ["journal/" + f for f in os.listdir(os.path.join(V2, "journal")) if f.endswith(".html")]:
    LOWER_VOCAB |= set(re.findall(r"\b[a-z]{3,}\b", re.sub(r"<[^>]+>", " ", open(os.path.join(V2, _f), encoding="utf-8").read())))
KNOWN_TERMS = {"Montessori", "Waldorf", "Ofqual", "Cognia", "Anglia", "Pearson", "Zoom", "Teams", "Google", "Microsoft", "Omella", "WhatsApp", "Leverage", "Bridge", "Agadir"}
rows, hide = [], []
files = [f for f in sorted(os.listdir(V2)) if f.endswith(".html")] + ["journal/" + f for f in sorted(os.listdir(os.path.join(V2, "journal"))) if f.endswith(".html")]
for f in files:
    raw = open(os.path.join(V2, f), encoding="utf-8").read(); mh = main_html(raw)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)\b.*?</\1>", " ", mh, flags=re.S))))
    title = html.unescape((re.search(r"<h1[^>]*>(.*?)</h1>", mh, re.S) or [None, ""])[1]); title = re.sub(r"<[^>]+>", "", title)
    names = set()
    for m in re.finditer(rf"(?i:\b(?:{KIDS})\b)\W+(?:[a-z]+\W+){{0,3}}?{NAME}", text):
        n = m.group(1)
        if n.split()[0] not in ADULTS and n not in ADULTS and n.split()[0].lower() not in LOWER_VOCAB and n.split()[0] not in KNOWN_TERMS: names.add(n)
    for m in re.finditer(rf"{NAME}'s (?i:birthday)|(?i:happy birthday|congratulations|congrats|bravo)\W+(?:to\W+)?{NAME}", text):
        n = m.group(1) or m.group(2)
        if n and n.split()[0] not in ADULTS and n.split()[0].lower() not in LOWER_VOCAB and n.split()[0] not in KNOWN_TERMS: names.add(n)
    for n in sorted(names): rows.append((f, "Possible child's name", n, "Check: is this a minor? Publish only with written parental consent, otherwise remove the name"))
    for e in set(re.findall(r"[\w.+-]+@[\w-]+\.[a-z]{2,}", text.lower())) - AGI_MAIL: rows.append((f, "Personal email", e, "Remove unless the person agreed"))
    for t in {re.sub(r"\D", "", x)[-9:] for x in re.findall(r"(?:\+?212|0)[\s.-]?[5-7](?:[\s.-]?\d){8}", text)} - AGI_TEL: rows.append((f, "Personal phone", t, "Remove unless the person agreed"))
    imgs = len(re.findall(r"<img\b", mh)) + len(re.findall(r'class="photo-hidden"', mh))
    if imgs and (f.startswith("journal/") or f == "student-life.html") and re.search(PHOTO_TOPICS, title + " " + text[:600], re.I):
        rows.append((f, "Photos in a post about children/school life", f"{imgs} photo(s) – '{title[:60]}'", "Photos hidden until consent for every child shown is confirmed"))
        hide.append(f)
    elif names and imgs: hide.append(f)
pj = os.path.join(V2, "_build", "privacy.json")
old = json.load(open(pj, encoding="utf-8")) if os.path.exists(pj) else {"approved": []}
json.dump({"hide_photos": sorted(set(hide)), "approved": old.get("approved", []), "note": "Pages in hide_photos show no photos until listed in approved (after written parental consent)."},
          open(pj, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
with open(os.path.join(ROOT, "docs", "privacy-review.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh); w.writerow(["page", "issue", "detail", "action"]); w.writerows(rows)
from collections import Counter
c = Counter(r[1] for r in rows)
print(f"privacy scan: {len(files)} pages · {len({r[0] for r in rows})} pages flagged · {len(rows)} findings")
for k, n in c.most_common(): print(f"  {n:3}  {k}")
print(f"photos hidden on {len(set(hide))} pages (until approved)")
for r in rows[:14]: print("   ", r[0], "|", r[1], "|", r[2][:70])
