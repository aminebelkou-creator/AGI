# Phase 7 – translated pages (fr/, ar/). Loaded by pages.py after content_pages.py.
# Links: "./x.html" = page in the same language; "x.html" = English page (made "../x.html" below).
os.makedirs(os.path.join(V2, "fr"), exist_ok=True); os.makedirs(os.path.join(V2, "ar"), exist_ok=True)
AR_FONT = '<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;500;600&display=swap" rel="stylesheet">'
def tr_page(lang, name, title, desc, body, css=""):
    key = f"{lang}/{name}"
    page(key, title, desc, body, css)
    h = PAGES[key]
    h = _re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/|\.\./|\./)', r'\1="../', h)
    h = h.replace('<main id="main" class="np">', f'<main id="main" class="np" data-verify="translation-review:{lang}">', 1)
    if lang == "ar": h = h.replace("</head>", AR_FONT + "\n</head>", 1)
    PAGES[key] = h
def tr_hero(crumb_home, crumb, h1, lede, buttons=""):
    c = f'<p class="crumb"><a href="./index.html">{crumb_home}</a> / <span>{crumb}</span></p>' if crumb else ""
    b = f'<div class="btn-row">{buttons}</div>' if buttons else ""
    return f'<section class="page-hero wrap">{c}<h1>{h1}</h1><p class="lede">{lede}</p>{b}</section>'
def tr_cta(title, text, buttons):
    return f'<section class="section tight bg-navy"><div class="wrap cta-band"><div><h2>{title}</h2><p>{text}</p></div><div class="btn-row">{buttons}</div></div></section>'
WA_TR = lambda label: f'<a class="btn btn-ghost" href="https://wa.me/212688739393?text=Bonjour%20AGI%2C%20" target="_blank" rel="noopener">{label}</a>'

# ================================================================== FRANÇAIS
FR = dict(home="Accueil")
tr_page("fr", "index.html", "American Group International – école américaine à Agadir",
 "La première école américaine d'Agadir : de la maternelle à la terminale, éducation spécialisée, diplôme pour adultes, anglais et examens Anglia. Depuis 2013.",
 f"""
<section class="home-hero"><div class="wrap">
  <div>
    <p class="kicker">Abordable · Créative · Inclusive — depuis 2013</p>
    <h1>Une éducation américaine, <em>près de chez vous.</em></h1>
    <p class="lede">American Group International est la première école américaine d'Agadir : une micro-école de la maternelle à la 12e année, des programmes pour adultes, apprenants d'anglais et enseignants, et le siège d'Anglia Examinations au Maroc.</p>
    <div class="btn-row"><a class="btn btn-gold" href="forms.html#enrollment">S'inscrire</a><a class="btn btn-light" href="forms.html#visit">Réserver une visite</a><a class="link" href="./parents.html">Pour les parents</a></div>
  </div>
  <div class="seal"><img src="assets/web/agi-seal-520.webp" alt="Le sceau d'AGI" width="520" height="520" fetchpriority="high"></div>
  <p class="enrol"><b>Inscriptions ouvertes</b> Année scolaire 2026–27, tous les programmes. Journées d'inscription : 28 et 31 août.</p>
</div></section>
<section class="home-facts" aria-label="AGI en chiffres"><div class="wrap facts">
  <div><b>2013</b><span>Fondée à Agadir avec cinq enfants</span></div>
  <div><b>46+</b><span>Nationalités accueillies en onze ans</span></div>
  <div><b>4</b><span>Départements de l'éducation américains reconnaissent AGI</span></div>
  <div><b>12</b><span>Régions desservies par Anglia Maroc depuis Agadir</span></div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Abordable, créative et inclusive.</h2><p>Notre promesse à chaque famille depuis 2013. École + Famille + Communauté = Réussite de l'élève.</p></div>
  <div class="cards" style="--cols:4">
    <div><span class="tag">Abordable</span><h3>À la portée des familles</h3><p>Un niveau international pour les familles qui travaillent : livres, examens de mathématiques et examens Anglia inclus.</p></div>
    <div><span class="tag">Créative</span><h3>Apprendre avec imagination</h3><p>La pédagogie américaine en petites classes multi-niveaux, enrichie par les idées Montessori et Waldorf.</p></div>
    <div><span class="tag">Inclusive</span><h3>Aucun enfant retenu</h3><p>Le niveau de classe n'est jamais abaissé pour des documents manquants, des lacunes linguistiques ou scolaires.</p></div>
    <div><span class="tag">Anglais</span><h3>Des progrès certifiés</h3><p>Chaque niveau est évalué selon le CECR et certifié par Anglia Examinations (Angleterre).</p></div>
  </div>
</div></section>
<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Nos programmes</h2><p><a class="link" href="programs.html">Tous les programmes (en anglais)</a></p></div>
  <div class="cards">
    <a class="card" href="k12.html"><span class="tag">5–18 ans</span><h3>École K–12</h3><p>Une micro-école au programme américain, de la maternelle à la 12e année.</p></a>
    <a class="card" href="special-education.html"><span class="tag">Inclusif</span><h3>Éducation spécialisée</h3><p>Plans éducatifs individualisés, petits groupes et accompagnement thérapeutique.</p></a>
    <a class="card" href="adult-diploma.html"><span class="tag">16 ans et plus</span><h3>Diplôme d'études secondaires pour adultes</h3><p>Un diplôme américain à votre rythme, avec examens surveillés à Agadir.</p></a>
    <a class="card" href="anglia.html"><span class="tag">Tous âges</span><h3>Anglais et examens Anglia</h3><p>Le siège d'Anglia au Maroc : dix niveaux, cours du samedi, test de niveau gratuit.</p></a>
    <a class="card" href="teachers.html"><span class="tag">Enseignants</span><h3>Certificat C.I.T.E.</h3><p>Une certification à vie pour les enseignants d'anglais, et un stage de 30 jours.</p></a>
    <a class="card" href="pathways.html"><span class="tag">Études supérieures</span><h3>Parcours universitaires</h3><p>Un agent d'admission agréé pour les universités au Royaume-Uni et ailleurs.</p></a>
  </div>
</div></section>
<section class="section bg-navy"><div class="wrap">
  <div class="section-head"><h2>Rejoindre AGI</h2><p>Les élèves sont accueillis à tout moment de l'année. Chaque nouvel élève passe un test de placement gratuit.</p></div>
  <div class="cards" style="--cols:4">
    <div><span class="num">01</span><h3>Prendre contact et visiter</h3><p>Les visites sont organisées individuellement.</p></div>
    <div><span class="num">02</span><h3>Test de placement</h3><p>Gratuit, y compris le test de niveau Anglia.</p></div>
    <div><span class="num">03</span><h3>Documents</h3><p>Dossier scolaire, rapport de comportement, justificatifs d'âge, de domicile et de vaccination.</p></div>
    <div><span class="num">04</span><h3>Inscription</h3><p>Frais d'inscription annuels et plan mensuel, les 28 et 31 août.</p></div>
  </div>
  <p style="margin-top:28px;color:rgba(255,255,255,.8)">Scolarité : <b>2 600 MAD par mois sur dix mois</b>, plus des frais d'inscription annuels. <a class="link" style="color:#fff" href="./fees.html">Frais de scolarité</a></p>
</div></section>
""" + tr_cta("Venez visiter l'école.", "Les visites ont lieu du lundi au vendredi, sur rendez-vous.", '<a class="btn btn-gold" href="forms.html#visit">Réserver une visite</a><a class="btn btn-light" href="./contact.html">Contact</a>'), HOME_CSS)

tr_page("fr", "parents.html", "Pour les parents – American Group International, Agadir",
 "Votre enfant, connu par son prénom : une école américaine abordable, créative et inclusive à Agadir depuis 2013.",
 tr_hero("Accueil", "Pour les parents", "Votre enfant, connu par son prénom.",
  "Une école américaine abordable, créative et inclusive à Agadir – où chaque enseignant connaît votre enfant, où il est soutenu là où il en a besoin, et jamais retenu à cause de la langue.",
  '<a class="btn btn-primary" href="forms.html#visit">Réserver une visite</a>' + WA_TR("WhatsApp"))
 + """
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Votre enfant s'épanouit-il vraiment ?</h2></div>
  <div class="prose"><p>Beaucoup de familles connaissent ce sentiment : des classes trop chargées, des notes qui pénalisent un enfant qui apprend encore une langue, et des écoles internationales hors de prix.</p>
  <p>AGI a été créée pour ces familles. L'école a ouvert en 2013 avec cinq enfants dans une seule salle à Agadir, avec une conviction : une éducation américaine ne devrait pas être réservée à quelques-uns.</p></div>
</div></section>
<section class="section"><div class="wrap split">
  <div class="intro"><p class="kicker">Notre engagement</p><h2>Aucun enfant n'est retenu à cause de la langue.</h2></div>
  <div><p class="quote" style="max-width:none">« Le niveau de classe n'est pas abaissé en raison de documents manquants, de lacunes linguistiques ou scolaires. »</p>
  <p class="cite"><b>Politique de placement provisoire d'AGI</b>Chaque nouvel élève passe une évaluation de placement gratuite</p></div>
</div></section>
<section class="section bg-navy"><div class="wrap"><p class="kicker">Notre devise</p><p class="promise" style="font-family:var(--serif);font-weight:300;font-size:clamp(28px,3.4vw,48px);line-height:1.2">École + Famille + Communauté = Réussite de l'élève</p>
<p style="color:rgba(255,255,255,.8);max-width:60ch">Vous connaîtrez les enseignants de votre enfant et participerez à son plan. Les nouveaux élèves commencent par une période d'adaptation de 90 jours.</p></div></section>
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Questions fréquentes</h2></div>
  <dl class="rows">
    <div><dt>Mon enfant ne parle pas encore anglais.</dt><dd>Il rejoint sa classe d'âge avec un soutien en anglais langue seconde et des évaluations Anglia.</dd></div>
    <div><dt>Peut-il commencer en cours d'année ?</dt><dd>Oui, nous accueillons les élèves à tout moment.</dd></div>
    <div><dt>Mon enfant a des besoins particuliers.</dt><dd>Nous établissons avec vous un plan éducatif individualisé ; un document d'un praticien agréé est nécessaire.</dd></div>
    <div><dt>Combien cela coûte-t-il ?</dt><dd>2 600 MAD par mois sur dix mois, plus des frais d'inscription annuels. <a class="link" href="./fees.html">Frais</a></dd></div>
  </dl>
</div></section>
""" + tr_cta("Venez visiter l'école.", "La meilleure façon de connaître AGI est de la visiter pendant une journée de classe.", '<a class="btn btn-gold" href="forms.html#visit">Réserver une visite</a>'), PARENTS_CSS)

_fr_ins = {"K–Grade 1": "Maternelle – 1re année", "Grades 2–6": "2e – 6e année", "Grades 7–8": "7e – 8e année", "Grades 9–11": "9e – 11e année", "Grade 12": "12e année"}
tr_page("fr", "fees.html", "Frais de scolarité – American Group International, Agadir",
 "Frais AGI 2026–27 : inscription annuelle par niveau (6 500 – 11 000 MAD), scolarité 2 600 MAD par mois, forfait tout compris, cours d'anglais.",
 tr_hero("Accueil", "Frais de scolarité", "Frais de scolarité.", "Simple et clair : des frais d'inscription annuels, dix mensualités, et l'essentiel inclus. Les frais sont les mêmes pour toutes les familles.",
  '<a class="btn btn-primary" href="forms.html#enrollment">S\'inscrire</a>')
 + '<section class="section bg-white"><div class="wrap"><div class="doc">'
 + "<h2 style=\"margin-top:0\">Frais d'inscription annuels (non remboursables)</h2><div class=\"table-wrap\"><table class=\"fee-table\"><thead><tr><th>Niveau</th><th>Inscription</th></tr></thead><tbody>"
 + "".join(f"<tr><td>{_fr_ins.get(g, g)}</td><td><b>{v.replace(',', ' ')}</b></td></tr>" for g, v in _ins.items())
 + "<tr><td>Lycée en ligne – American High School Online</td><td><b>2 500 US$</b></td></tr></tbody></table></div>"
 + "<h2>Scolarité mensuelle</h2><p><b>2 600 MAD par mois, sur dix mois</b> – soit 26 000 MAD par année scolaire.</p>"
 + "<h2>Forfait tout compris</h2><ul><li>Livres et supports pédagogiques</li><li>Examens de mathématiques</li><li>Examens d'anglais Anglia</li><li>Inscription aux États-Unis et au Maroc</li><li>Assurance scolaire</li></ul>"
 + "<h2>École d'été (lycée)</h2><p>Pour rattraper ou s'inscrire tardivement : <b>3 000 MAD</b> pour un programme d'un mois.</p>"
 + "<h2>Cours d'anglais Anglia</h2><div class=\"table-wrap\"><table class=\"fee-table\"><tbody><tr><td>Cours du samedi, 5–18 ans (14h–16h, octobre–juin, examen annuel inclus)</td><td><b>500 MAD par mois</b></td></tr><tr><td>Cours particulier</td><td><b>200 MAD la séance</b></td></tr><tr><td>Petit groupe (2–3 élèves)</td><td><b>150 MAD par personne</b></td></tr><tr><td>Cours de 12 semaines (4–10 élèves)</td><td><b>1 200 MAD</b></td></tr><tr><td>Test de niveau</td><td><b>Gratuit</b></td></tr></tbody></table></div>"
 + '<p>Les frais ne sont pas négociables : ils sont déjà fixés au plus bas pour garder AGI accessible. <a class="link" href="fees.html">Version complète (en anglais)</a></p></div></div></section>', DOC_CSS)

tr_page("fr", "contact.html", "Contact – American Group International, Agadir",
 "Contacter AGI à Agadir : 20 rue Baalabek, Hay Nahda. Téléphone +212 528 843 349, WhatsApp +212 688 739 393.",
 tr_hero("Accueil", "Contact", "Contacter AGI.", "Appelez, écrivez ou venez nous voir. Le bureau répond sous un jour ouvrable et il est fermé le dimanche.")
 + f"""<section class="section bg-white"><div class="wrap"><div class="cards" style="--cols:4">
  <div><span class="tag">Adresse</span><h3>N° 20, rue Baalabek</h3><p>Hay Nahda, Agadir 80000, Maroc</p></div>
  <div><span class="tag">Téléphone</span><h3><a href="tel:+212528843349">+212 528 843 349</a></h3><p>En arabe : <a href="tel:+212618639911">+212 618 639 911</a></p></div>
  <div><span class="tag">WhatsApp</span><h3><a href="https://wa.me/212688739393">+212 688 739 393</a></h3><p>Pour les questions rapides.</p></div>
  <div><span class="tag">E-mail</span><h3 style="font-size:19px;word-break:break-all"><a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a></h3><p>Adresse officielle d'AGI.</p></div>
</div></div></section>
<section class="section tight"><div class="wrap">{MAP}</div></section>
<section class="section"><div class="wrap"><div class="section-head"><h2>Formulaires</h2><p>Les formulaires sont pour l'instant en anglais.</p></div>
<div class="cards"><a class="card" href="forms.html#visit"><h3>Réserver une visite</h3></a><a class="card" href="forms.html#enrollment"><h3>S'inscrire</h3></a><a class="card" href="forms.html#enquiry"><h3>Poser une question</h3></a></div></div></section>""")

# ================================================================== العربية
tr_page("ar", "index.html", "المجموعة الأمريكية الدولية – مدرسة أمريكية في أكادير",
 "أول مدرسة أمريكية في أكادير منذ 2013: من الروض إلى الصف الثاني عشر، التربية الخاصة، دبلوم الكبار، اللغة الإنجليزية وامتحانات أنجليا.",
 f"""
<section class="home-hero"><div class="wrap">
  <div>
    <p class="kicker">في المتناول · مبدعة · شاملة — منذ 2013</p>
    <h1>تعليم أمريكي، <em>قريب منكم.</em></h1>
    <p class="lede">المجموعة الأمريكية الدولية (AGI) هي أول مدرسة أمريكية في أكادير: مدرسة صغيرة من الروض إلى الصف الثاني عشر، وبرامج للكبار ولمتعلمي الإنجليزية وللأساتذة، والمقر الرئيسي لامتحانات أنجليا في المغرب.</p>
    <div class="btn-row"><a class="btn btn-gold" href="forms.html#enrollment">سجّل الآن</a><a class="btn btn-light" href="forms.html#visit">احجزوا زيارة</a><a class="link" href="./parents.html">للآباء والأمهات</a></div>
  </div>
  <div class="seal"><img src="assets/web/agi-seal-520.webp" alt="شعار المجموعة الأمريكية الدولية" width="520" height="520" fetchpriority="high"></div>
  <p class="enrol"><b>التسجيل مفتوح</b> السنة الدراسية 2026–2027، جميع البرامج. أيام التسجيل: 28 و31 غشت.</p>
</div></section>
<section class="home-facts" aria-label="AGI بالأرقام"><div class="wrap facts">
  <div><b>2013</b><span>تأسست في أكادير بخمسة أطفال</span></div>
  <div><b>+46</b><span>جنسية استقبلتها المدرسة خلال إحدى عشرة سنة</span></div>
  <div><b>4</b><span>وزارات تعليم أمريكية على مستوى الولايات تعترف بالمدرسة</span></div>
  <div><b>12</b><span>جهة تغطيها أنجليا المغرب انطلاقاً من أكادير</span></div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>في المتناول، مبدعة وشاملة.</h2><p>وعدنا لكل أسرة منذ 2013: المدرسة + الأسرة + المجتمع = نجاح التلميذ.</p></div>
  <div class="cards" style="--cols:4">
    <div><span class="tag">في المتناول</span><h3>تعليم في متناول الأسر</h3><p>مستوى دولي للأسر العاملة، مع الكتب وامتحانات الرياضيات وامتحانات أنجليا مشمولة.</p></div>
    <div><span class="tag">مبدعة</span><h3>تعلّم بالإبداع</h3><p>بيداغوجيا أمريكية في أقسام صغيرة متعددة المستويات، مستلهمة من أفكار مونتيسوري ووالدورف.</p></div>
    <div><span class="tag">شاملة</span><h3>لا يُعاد أي طفل إلى الوراء</h3><p>لا يُخفَّض مستوى القسم بسبب وثائق ناقصة أو ضعف في اللغة أو في التحصيل الدراسي.</p></div>
    <div><span class="tag">الإنجليزية</span><h3>تقدّم مُعتمد</h3><p>يُقيَّم كل مستوى وفق الإطار الأوروبي المرجعي ويُعتمد بامتحانات أنجليا البريطانية.</p></div>
  </div>
</div></section>
<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>برامجنا</h2><p><a class="link" href="programs.html">جميع البرامج (بالإنجليزية)</a></p></div>
  <div class="cards">
    <a class="card" href="k12.html"><span class="tag">من 5 إلى 18 سنة</span><h3>مدرسة K–12</h3><p>مدرسة صغيرة بالمنهاج الأمريكي من الروض إلى الصف الثاني عشر.</p></a>
    <a class="card" href="special-education.html"><span class="tag">شاملة</span><h3>التربية الخاصة</h3><p>خطط تربوية فردية، أقسام صغيرة ودعم علاجي.</p></a>
    <a class="card" href="adult-diploma.html"><span class="tag">16 سنة فما فوق</span><h3>دبلوم الثانوية للكبار</h3><p>دبلوم أمريكي حسب إيقاعك، مع امتحانات مراقبة في أكادير.</p></a>
    <a class="card" href="anglia.html"><span class="tag">لجميع الأعمار</span><h3>الإنجليزية وامتحانات أنجليا</h3><p>المقر الرئيسي لأنجليا في المغرب: عشرة مستويات، دروس يوم السبت واختبار مستوى مجاني.</p></a>
    <a class="card" href="teachers.html"><span class="tag">للأساتذة</span><h3>شهادة C.I.T.E.</h3><p>شهادة مدى الحياة لأساتذة الإنجليزية، وتدريب لمدة 30 يوماً.</p></a>
    <a class="card" href="pathways.html"><span class="tag">الدراسات العليا</span><h3>المسارات الجامعية</h3><p>وكيل قبول معتمد للجامعات في المملكة المتحدة وغيرها.</p></a>
  </div>
</div></section>
<section class="section bg-navy"><div class="wrap">
  <div class="section-head"><h2>الالتحاق بالمدرسة</h2><p>نستقبل التلاميذ في أي وقت من السنة، ويجتاز كل تلميذ جديد اختبار تحديد مستوى مجانياً.</p></div>
  <div class="cards" style="--cols:4">
    <div><span class="num">01</span><h3>التواصل والزيارة</h3><p>تُنظَّم الزيارات بشكل فردي.</p></div>
    <div><span class="num">02</span><h3>اختبار تحديد المستوى</h3><p>مجاني، بما في ذلك اختبار مستوى أنجليا.</p></div>
    <div><span class="num">03</span><h3>الوثائق</h3><p>الملف الدراسي، تقرير السلوك، وإثبات السن والسكن والتلقيح.</p></div>
    <div><span class="num">04</span><h3>التسجيل</h3><p>رسوم التسجيل السنوية وخطة الأداء الشهري، يومي 28 و31 غشت.</p></div>
  </div>
  <p style="margin-top:28px;color:rgba(255,255,255,.8)">الرسوم الدراسية: <b>2600 درهم شهرياً على مدى عشرة أشهر</b>، إضافة إلى رسوم التسجيل السنوية. <a class="link" style="color:#fff" href="./fees.html">الرسوم الدراسية</a></p>
</div></section>
""" + tr_cta("تفضّلوا بزيارة المدرسة.", "الزيارات من الاثنين إلى الجمعة، بموعد مسبق.", '<a class="btn btn-gold" href="forms.html#visit">احجزوا زيارة</a><a class="btn btn-light" href="./contact.html">اتصل بنا</a>'), HOME_CSS)

tr_page("ar", "parents.html", "للآباء والأمهات – المجموعة الأمريكية الدولية، أكادير",
 "طفلكم معروف باسمه: مدرسة أمريكية في المتناول، مبدعة وشاملة في أكادير منذ 2013.",
 tr_hero("الرئيسية", "للآباء والأمهات", "طفلكم، معروف باسمه.",
  "مدرسة أمريكية في المتناول، مبدعة وشاملة في أكادير – يعرف فيها كل أستاذ طفلكم، ويحصل على الدعم حيث يحتاجه، ولا يُعاد إلى الوراء بسبب اللغة.",
  '<a class="btn btn-primary" href="forms.html#visit">احجزوا زيارة</a>' + WA_TR("واتساب"))
 + """
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>هل يتألق طفلكم حقاً؟</h2></div>
  <div class="prose"><p>تعرف كثير من الأسر هذا الشعور: أقسام مكتظة، ونقط تعاقب طفلاً ما زال يتعلم لغة جديدة، ومدارس دولية برسوم بعيدة المنال.</p>
  <p>أُنشئت AGI من أجل هذه الأسر. افتتحت المدرسة سنة 2013 بخمسة أطفال في قاعة واحدة بأكادير، بقناعة واحدة: التعليم الأمريكي لا ينبغي أن يكون حكراً على القلة.</p></div>
</div></section>
<section class="section"><div class="wrap split">
  <div class="intro"><p class="kicker">التزامنا</p><h2>لا يُعاد أي طفل إلى الوراء بسبب اللغة.</h2></div>
  <div><p class="quote" style="max-width:none">«لا يُخفَّض مستوى القسم بسبب وثائق ناقصة أو ضعف في اللغة أو في التحصيل الدراسي.»</p>
  <p class="cite"><b>سياسة التسجيل المؤقت والتقييم في AGI</b>يجتاز كل تلميذ جديد تقييماً مجانياً لتحديد المستوى</p></div>
</div></section>
<section class="section bg-navy"><div class="wrap"><p class="kicker">شعارنا</p><p style="font-family:'Noto Naskh Arabic',serif;font-size:clamp(26px,3vw,42px);line-height:1.4;color:#fff">المدرسة + الأسرة + المجتمع = نجاح التلميذ</p>
<p style="color:rgba(255,255,255,.8);max-width:60ch">ستتعرفون على أساتذة طفلكم وتشاركون في خطته. يبدأ التلاميذ الجدد بفترة تكيّف مدتها 90 يوماً.</p></div></section>
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>أسئلة متكررة</h2></div>
  <dl class="rows">
    <div><dt>طفلي لا يتكلم الإنجليزية بعد.</dt><dd>يلتحق بقسم عمره مع دعم في الإنجليزية كلغة ثانية وتقييمات أنجليا.</dd></div>
    <div><dt>هل يمكنه الالتحاق خلال السنة؟</dt><dd>نعم، نستقبل التلاميذ في أي وقت.</dd></div>
    <div><dt>طفلي له احتياجات خاصة.</dt><dd>نضع معكم خطة تربوية فردية، ويلزم تقرير من مختص معتمد.</dd></div>
    <div><dt>كم تبلغ التكلفة؟</dt><dd>2600 درهم شهرياً على مدى عشرة أشهر، إضافة إلى رسوم التسجيل السنوية. <a class="link" href="./fees.html">الرسوم</a></dd></div>
  </dl>
</div></section>
""" + tr_cta("تفضّلوا بزيارة المدرسة.", "أفضل طريقة للتعرف على AGI هي زيارتها خلال يوم دراسي.", '<a class="btn btn-gold" href="forms.html#visit">احجزوا زيارة</a>'), PARENTS_CSS)

_ar_ins = {"K–Grade 1": "الروض – الصف الأول", "Grades 2–6": "الصف الثاني – السادس", "Grades 7–8": "الصف السابع – الثامن", "Grades 9–11": "الصف التاسع – الحادي عشر", "Grade 12": "الصف الثاني عشر"}
tr_page("ar", "fees.html", "الرسوم الدراسية – المجموعة الأمريكية الدولية، أكادير",
 "رسوم AGI 2026–2027: التسجيل السنوي حسب المستوى (6500 – 11000 درهم)، الرسوم الشهرية 2600 درهم، باقة شاملة، دروس الإنجليزية.",
 tr_hero("الرئيسية", "الرسوم الدراسية", "الرسوم الدراسية.", "بسيطة وواضحة: رسوم تسجيل سنوية، عشرة أقساط شهرية، والأساسيات مشمولة. الرسوم نفسها لجميع الأسر.",
  '<a class="btn btn-primary" href="forms.html#enrollment">سجّل الآن</a>')
 + '<section class="section bg-white"><div class="wrap"><div class="doc">'
 + '<h2 style="margin-top:0">رسوم التسجيل السنوية (غير قابلة للاسترجاع)</h2><div class="table-wrap"><table class="fee-table"><thead><tr><th>المستوى</th><th>التسجيل</th></tr></thead><tbody>'
 + "".join(f"<tr><td>{_ar_ins.get(g, g)}</td><td><b>{v.replace(',', '').replace('MAD', 'درهم')}</b></td></tr>" for g, v in _ins.items())
 + "<tr><td>الثانوية عبر الإنترنت – American High School Online</td><td><b>2500 دولار</b></td></tr></tbody></table></div>"
 + "<h2>الرسوم الشهرية</h2><p><b>2600 درهم شهرياً على مدى عشرة أشهر</b> – أي 26000 درهم للسنة الدراسية.</p>"
 + "<h2>باقة شاملة</h2><ul><li>الكتب والمواد التعليمية</li><li>امتحانات الرياضيات</li><li>امتحانات أنجليا للإنجليزية</li><li>التسجيل في الولايات المتحدة والمغرب</li><li>التأمين المدرسي</li></ul>"
 + "<h2>المدرسة الصيفية (الثانوي)</h2><p>للاستدراك أو للتسجيل المتأخر: <b>3000 درهم</b> لبرنامج مدته شهر.</p>"
 + "<h2>دروس الإنجليزية مع أنجليا</h2><div class=\"table-wrap\"><table class=\"fee-table\"><tbody><tr><td>دروس السبت، من 5 إلى 18 سنة (14:00–16:00، من أكتوبر إلى يونيو، الامتحان السنوي مشمول)</td><td><b>500 درهم شهرياً</b></td></tr><tr><td>درس فردي</td><td><b>200 درهم للحصة</b></td></tr><tr><td>مجموعة صغيرة (2–3 تلاميذ)</td><td><b>150 درهم للفرد</b></td></tr><tr><td>دورة من 12 أسبوعاً (4–10 تلاميذ)</td><td><b>1200 درهم</b></td></tr><tr><td>اختبار المستوى</td><td><b>مجاني</b></td></tr></tbody></table></div>"
 + '<p>الرسوم غير قابلة للتفاوض: فهي محددة في أدنى مستوى ممكن لتبقى المدرسة في متناول الجميع. <a class="link" href="fees.html">النسخة الكاملة (بالإنجليزية)</a></p></div></div></section>', DOC_CSS)

tr_page("ar", "contact.html", "اتصل بنا – المجموعة الأمريكية الدولية، أكادير",
 "تواصلوا مع AGI في أكادير: رقم 20، شارع بعلبك، حي النهضة. الهاتف ‎+212 528 843 349، واتساب ‎+212 688 739 393.",
 tr_hero("الرئيسية", "اتصل بنا", "تواصلوا معنا.", "اتصلوا بنا أو راسلونا أو زورونا. تجيب الإدارة خلال يوم عمل واحد، وهي مغلقة يوم الأحد.")
 + f"""<section class="section bg-white"><div class="wrap"><div class="cards" style="--cols:4">
  <div><span class="tag">العنوان</span><h3>رقم 20، شارع بعلبك</h3><p>حي النهضة، أكادير 80000، المغرب</p></div>
  <div><span class="tag">الهاتف</span><h3><a href="tel:+212528843349" dir="ltr">+212 528 843 349</a></h3><p>بالعربية: <a href="tel:+212618639911" dir="ltr">+212 618 639 911</a></p></div>
  <div><span class="tag">واتساب</span><h3><a href="https://wa.me/212688739393" dir="ltr">+212 688 739 393</a></h3><p>للأسئلة السريعة.</p></div>
  <div><span class="tag">البريد الإلكتروني</span><h3 style="font-size:18px;word-break:break-all"><a href="mailto:americanecoleagadir@gmail.com" dir="ltr">americanecoleagadir@gmail.com</a></h3><p>العنوان الرسمي للمدرسة.</p></div>
</div></div></section>
<section class="section tight"><div class="wrap">{MAP}</div></section>
<section class="section"><div class="wrap"><div class="section-head"><h2>الاستمارات</h2><p>الاستمارات متوفرة حالياً بالإنجليزية.</p></div>
<div class="cards"><a class="card" href="forms.html#visit"><h3>احجزوا زيارة</h3></a><a class="card" href="forms.html#enrollment"><h3>سجّل الآن</h3></a><a class="card" href="forms.html#enquiry"><h3>اطرحوا سؤالاً</h3></a></div></div></section>""")
