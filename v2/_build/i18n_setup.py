"""Phase 7 – language support in build.py (fr/, ar/)."""
p = r"C:\Users\belko\AGI\v2\_build\build.py"
s = open(p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
I18N = r'''
# ---------------- languages ----------------
LANGS = {"en": {"name": "English", "short": "EN", "dir": "ltr"}, "fr": {"name": "Français", "short": "FR", "dir": "ltr"}, "ar": {"name": "العربية", "short": "ع", "dir": "rtl"}}
T = {
 "fr": {"About": "À propos", "Programs": "Programmes", "Admissions": "Admissions", "Student life": "Vie scolaire", "Journal": "Journal", "Anglia Morocco": "Anglia Maroc",
        "Contact": "Contact", "Forms": "Formulaires", "Apply": "S'inscrire", "All programs": "Tous les programmes", "Skip to content": "Aller au contenu",
        "Open menu": "Ouvrir le menu", "Forms &amp; requests": "Formulaires et demandes",
        "footer_about": "American Group International – la première école américaine d'Agadir, depuis 2013, et siège d'Anglia Examinations au Maroc.",
        "School": "École", "Services": "Services", "Privacy": "Confidentialité", "Terms": "Conditions", "Cookies": "Cookies", "English version": "Version anglaise"},
 "ar": {"About": "من نحن", "Programs": "البرامج", "Admissions": "التسجيل", "Student life": "الحياة المدرسية", "Journal": "الأخبار", "Anglia Morocco": "أنجليا المغرب",
        "Contact": "اتصل بنا", "Forms": "الاستمارات", "Apply": "سجّل الآن", "All programs": "جميع البرامج", "Skip to content": "انتقل إلى المحتوى",
        "Open menu": "فتح القائمة", "Forms &amp; requests": "الاستمارات والطلبات",
        "footer_about": "المجموعة الأمريكية الدولية – أول مدرسة أمريكية في أكادير منذ 2013، والمقر الرئيسي لامتحانات أنجليا في المغرب.",
        "School": "المدرسة", "Services": "الخدمات", "Privacy": "الخصوصية", "Terms": "الشروط", "Cookies": "ملفات تعريف الارتباط", "English version": "النسخة الإنجليزية"},
}
def translated(lang):
    d = os.path.join(ROOT, lang)
    return {f for f in os.listdir(d) if f.endswith(".html")} if os.path.isdir(d) else set()
def localize(block, lang, page):
    """Translate labels and point links to the translated page when it exists ("./x.html"), else to English."""
    if lang == "en": return block
    have = translated(lang)
    for en, tr in T[lang].items():
        if en.islower() or "_" in en: continue
        block = block.replace(f">{en}<", f">{tr}<").replace(f'aria-label="{en}"', f'aria-label="{tr}"')
    block = block.replace(T["fr"]["footer_about"] if False else "American Group International – the first American school in Agadir, since 2013, and headquarters of Anglia Examinations in Morocco.", T[lang]["footer_about"])
    block = re.sub(r'href="([a-z0-9-]+\.html)(#[^"]*)?"', lambda m: f'href="./{m.group(1)}{m.group(2) or ""}"' if m.group(1) in have else m.group(0), block)
    return block
def lang_switch(rel):
    lang = rel.split("/")[0] if rel.split("/")[0] in ("fr", "ar") else "en"
    name = rel.split("/")[-1]
    out = []
    for L, meta in LANGS.items():
        if L == "en": href = name if lang == "en" else f"../{name}"
        else:
            tgt = name if name in translated(L) else "index.html"
            href = f"{L}/{tgt}" if lang == "en" else (f"./{tgt}" if L == lang else f"../{L}/{tgt}")
        cur = ' aria-current="true"' if L == lang else ""
        out.append(f'<a href="{href}" hreflang="{L}" lang="{L}"{cur}>{meta["short"]}</a>')
    return '<nav class="lang-switch" aria-label="Language">' + "".join(out) + "</nav>"
'''
s = s.replace("HEAD_LINKS = ", I18N + "\nHEAD_LINKS = ", 1)
# prefixing must leave "./" links alone
s = s.replace("""return re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/|\\.\\./)', lambda m: f'{m.group(1)}="{prefix}', block)""",
              """return re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/|\\.\\./|\\./)', lambda m: f'{m.group(1)}="{prefix}', block)""")
# stamp(): language-aware header/footer, lang/dir, switcher, hreflang
s = s.replace('''    key = page if depth == 0 else "journal.html"   # menu section for sub-folder pages''',
'''    lang = rel.split("/")[0] if rel.split("/")[0] in ("fr", "ar") else "en"
    key = page if depth == 0 else ("journal.html" if rel.startswith("journal/") else rel.split("/")[-1])   # menu section''')
s = s.replace('''        block = fn(key)''', '''        block = localize(fn(key), lang, rel)
        if name == "header": block = block.replace('<div class="head-actions">', '<div class="head-actions">' + lang_switch(rel), 1)''')
s = s.replace('''    block = seo_block(rel, s)''', '''    s = re.sub(r'<html lang="[^"]*"( dir="[^"]*")?>', f'<html lang="{lang}" dir="{LANGS[lang]["dir"]}">', s, count=1)
    block = seo_block(rel, s)
    name_ = rel.split("/")[-1]; alts = [("en", name_ if lang == "en" else name_)] + [(L, f"{L}/{name_}") for L in ("fr", "ar") if name_ in translated(L)]
    if len(alts) > 1: block = block.replace("<!--/site:seo-->", "".join(f'<link rel="alternate" hreflang="{L}" href="{SITE_URL}/{u}">' for L, u in alts) + f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{name_}">\\n<!--/site:seo-->')''')
s = s.replace('''    for d in ("", "journal"):''', '''    for d in ("", "journal", "fr", "ar"):''')
open(p, "w", encoding="utf-8", newline="").write(s); print("build.py: languages")

# CSS: language switch + RTL
c = r"C:\Users\belko\AGI\v2\site.css"
css = open(c, encoding="utf-8").read()
if ".lang-switch" not in css:
    css += """
/* ---------- languages ---------- */
.lang-switch{display:flex;gap:2px;align-items:center}
.lang-switch a{font:600 12px/1 var(--sans);color:var(--grey);padding:8px 7px;letter-spacing:.04em}
.lang-switch a[aria-current]{color:var(--navy);box-shadow:inset 0 -2px 0 var(--red)}
.lang-switch a:hover{color:var(--red)}
[dir="rtl"] body{font-family:'Noto Naskh Arabic','IBM Plex Sans Arabic',var(--sans)}
[dir="rtl"] h1,[dir="rtl"] h2,[dir="rtl"] h3,[dir="rtl"] .h1,[dir="rtl"] .h2,[dir="rtl"] .quote,[dir="rtl"] .lede,[dir="rtl"] .brand-name{font-family:'Noto Naskh Arabic',var(--serif);letter-spacing:0}
[dir="rtl"] .kicker,[dir="rtl"] .crumb,[dir="rtl"] .cards .tag,[dir="rtl"] .btn{letter-spacing:0;text-transform:none}
[dir="rtl"] .wa-float{right:auto;left:clamp(14px,2vw,24px)}
[dir="rtl"] .submenu{left:auto;right:-24px}
[dir="rtl"] .note{border-left:0;border-right:3px solid var(--gold)}
[dir="rtl"] .prose ul,[dir="rtl"] .doc ul,[dir="rtl"] .doc ol{padding-left:0;padding-right:22px}
[dir="rtl"] .steps li{padding:22px 76px 22px 24px}[dir="rtl"] .steps li::before{left:auto;right:24px}
[dir="rtl"] .menu-btn::after{transform:rotate(45deg) translate(2px,-2px)}
@media (max-width:1060px){.lang-switch a{padding:8px 5px}}
"""
    open(c, "w", encoding="utf-8").write(css); print("site.css: language switch + RTL")
