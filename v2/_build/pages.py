"""Generates the static content pages of AGI v2. Run once; then build.py stamps header/footer."""
import os, html
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300;1,6..72,400'
         '&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')
PAGES = {}

def page(name, title, desc, body, extra_css=""):
    PAGES[name] = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" type="image/png" href="assets/favicon.png">
{FONTS}
<link rel="stylesheet" href="site.css">
<script src="site.js" defer></script>{('<style>' + extra_css + '</style>') if extra_css else ''}
</head>
<body>
<!--site:header-->
<!--/site:header-->
<main id="main" class="np">
{body.strip()}
</main>
<!--site:footer-->
<!--/site:footer-->
</body>
</html>
"""

def hero(crumb, h1, lede, buttons=""):
    c = f'<p class="crumb"><a href="index.html">Home</a> / {crumb}</p>' if crumb else ""
    b = f'<div class="btn-row">{buttons}</div>' if buttons else ""
    return f'<section class="page-hero wrap">{c}<h1>{h1}</h1><p class="lede">{lede}</p>{b}</section>'

def cta(title, text, buttons):
    return (f'<section class="section tight bg-navy"><div class="wrap cta-band"><div><h2>{title}</h2><p>{text}</p></div>'
            f'<div class="btn-row">{buttons}</div></div></section>')

APPLY = '<a class="btn btn-primary" href="forms.html#enrollment">Apply</a>'
VISIT = '<a class="btn btn-ghost" href="forms.html#visit">Book a visit</a>'
GOLD_APPLY = '<a class="btn btn-gold" href="forms.html#enrollment">Apply</a>'
LIGHT_VISIT = '<a class="btn btn-light" href="forms.html#visit">Book a visit</a>'

PROGRAM_CARDS = [
 ("k12.html", "Ages 5–18", "K–12 school", "An American-curriculum micro-school from kindergarten to grade 12, with English support through the Anglia system for children who don't speak English at home."),
 ("special-education.html", "Inclusive", "Special education (SEN)", "Individualized Education Plans, small-group classes and support from occupational therapy to speech-language and behavioral care."),
 ("adult-diploma.html", "Age 16+", "Adult high school diploma", "A self-paced U.S. high school completion program with American Worldwide Academy, with every test proctored on site in Agadir."),
 ("english-anglia.html", "All ages", "English & Anglia exams", "AGI is the Anglia Examinations headquarters for Morocco: ten CEFR-mapped levels, Saturday classes for children and courses for adults."),
 ("teachers.html", "Educators", "For teachers (C.I.T.E.)", "The lifelong Anglia C.I.T.E. teaching certificate, teacher training, a 30-day internship and U.S. private-school sponsorship."),
 ("professional.html", "Professionals", "Professional & medical English", "Business and medical English for working adults and teams, exam proctoring and ADHD holistic coaching."),
 ("pathways.html", "Next steps", "University pathways", "An authorized admissions agent for universities and colleges in the UK, the United States and beyond."),
]
def program_cards(cols=3, current=None):
    items = "".join(f'<a class="card" href="{h}"><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p><span class="more">Learn more</span></a>'
                    for h, t, n, d in PROGRAM_CARDS if h != current)
    return f'<div class="cards" style="--cols:{cols}">{items}</div>'


# ---------------- placeholders (tracked by _build/prelaunch.py) ----------------
def ph(pid, label, ratio="4/3", cls=""):
    """A photo slot. Replace with <figure class="photo"><img ...></figure> when the real photo arrives."""
    c = f' class="photo {cls}"' if cls else ' class="photo"'
    return f'<figure{c} data-placeholder="photo:{pid}" style="--ratio:{ratio}"><figcaption><b>Photo</b>{label}</figcaption></figure>'

MAP = ('<div class="map" data-verify="map-location"><iframe title="Map: AGI, Number 20, Rue Baalabek, Hay Nahda, Agadir" loading="lazy" referrerpolicy="no-referrer-when-downgrade" '
       'src="https://www.google.com/maps?q=20%20Rue%20Baalabek%2C%20Hay%20Nahda%2C%20Agadir%2C%20Morocco&amp;output=embed"></iframe></div>')

TESTIMONIALS = [  # SAMPLE quotes – replace with real, permission-cleared testimonials before launch
 ("parent-1", "Our daughter arrived speaking almost no English. Two years later she reads chapter books and corrects my pronunciation.", "Parent of a grade 3 student", "Sample testimonial"),
 ("parent-2", "The teachers know every child. When our son needed extra support, the plan was in place within weeks, and we were part of it.", "Parent of a grade 7 student", "Sample testimonial"),
 ("alumni-1", "AGI gave me an American diploma and the English to use it. I'm now studying at university abroad.", "AGI graduate", "Sample testimonial"),
]
def testimonials(items=TESTIMONIALS, cols=3):
    cards = "".join(f'<figure class="testimonial" data-placeholder="testimonial:{i}"><blockquote>{q}</blockquote><figcaption><b>{w}</b>{n}</figcaption></figure>' for i, q, w, n in items)
    return f'<div class="testimonials" style="--cols:{cols}">{cards}</div>'

PH_TXT = lambda key, text: f'<span class="ph-text" data-placeholder="fact:{key}">{text}</span>'
# ------------------------------------------------------------------ HOME
HOME_CSS = """
.home-hero{background:radial-gradient(120% 90% at 78% 40%,#0f3a72 0%,#061529 62%);color:#fff;overflow:hidden}
.home-hero .wrap{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(24px,4vw,72px);align-items:center;padding-block:clamp(64px,8vw,120px) clamp(40px,5vw,72px)}
.home-hero .kicker{color:var(--gold)}
.home-hero h1{font-family:var(--serif);font-weight:300;font-size:clamp(46px,6vw,92px);line-height:1;letter-spacing:-.015em;margin:0 0 26px;max-width:12ch}
.home-hero h1 em{font-style:italic;color:var(--gold)}
.home-hero .lede{color:rgba(255,255,255,.78);font-style:normal;font-family:var(--sans);font-size:clamp(16px,1.25vw,18.5px);line-height:1.65;max-width:52ch}
.home-hero .btn-row{margin-top:36px;align-items:center}
.home-hero .btn-row .link{color:#fff;margin-left:10px}
.seal{position:relative;justify-self:center;width:min(440px,80vw);aspect-ratio:1}
.seal img{position:absolute;inset:12%;width:76%;height:76%;object-fit:contain;filter:drop-shadow(0 30px 50px rgba(0,0,0,.45))}
.seal::before,.seal::after{content:"";position:absolute;inset:0;border-radius:50%;border:1px solid rgba(201,162,39,.35)}
.seal::after{inset:-9%;border-color:rgba(255,255,255,.1)}
.enroll{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:8px 24px;align-items:baseline;border-top:1px solid var(--line-dark);padding-top:22px;font-size:14px;color:rgba(255,255,255,.75)}
.enroll b{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);font-weight:500}
.home-facts{background:var(--navy-deep);padding-bottom:clamp(48px,6vw,80px)}
.dates{border-top:1px solid var(--line-dark);margin:0}
.dates div{display:flex;justify-content:space-between;gap:16px;padding:14px 0;border-bottom:1px solid var(--line-dark);font-size:14.5px}
.dates dd{margin:0;font-family:var(--serif);font-style:italic;color:var(--gold);text-align:right}
.adm{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:clamp(32px,4vw,72px);align-items:start}
.fee{font-family:var(--serif);font-weight:300;font-size:48px;line-height:1;color:#fff;margin:26px 0 4px}
.visit{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(32px,4vw,72px);align-items:start}
.visit address{font-style:normal;font-family:var(--serif);font-size:24px;line-height:1.45;color:#fff;margin:0 0 18px}
@media (max-width:1000px){.home-hero .wrap,.adm,.visit{grid-template-columns:minmax(0,1fr)}.seal{width:min(240px,56vw);order:-1}}
"""
NEWS3 = [("4356-2", "Announcement", "April 6, 2026", "Julie Wilburn officially accredited as a Holistic Therapeutic Coach"),
         ("american-school-counselor-association-member", "Membership", "March 4, 2026", "AGI joins the American School Counselor Association"),
         ("leverage-edu-x-agi-join-forces-in-the-south-of-morocco", "Partnership", "March 4, 2026", "Leverage Edu and AGI join forces in the south of Morocco")]

news_cards = "".join(f'<a class="card" href="journal/{s}.html"><span class="tag">{k} · {d}</span><h3>{t}</h3><span class="more">Read</span></a>' for s, k, d, t in NEWS3)
page("index.html", "American Group International – American school in Agadir, Morocco",
 "The first American school in Agadir: K–12, special education, adult diploma, English and Anglia exams. Established 2013. Now enrolling for 2026–27.",
 f"""
<section class="home-hero">
  <div class="wrap">
    <div>
      <p class="kicker">Affordable · Creative · Inclusive — since 2013</p>
      <h1>An American education, <em>close to home.</em></h1>
      <p class="lede">American Group International is the first American school in Agadir – a K–12 micro-school with programs for adults, English learners and educators, and the headquarters of Anglia Examinations in Morocco.</p>
      <div class="btn-row">{GOLD_APPLY}{LIGHT_VISIT}<a class="link" href="programs.html">Explore programs</a></div>
    </div>
    <div class="seal"><img src="assets/web/agi-seal-520.png" alt="The AGI seal: American and Moroccan flags, Agadir, established 2013" width="520" height="520" fetchpriority="high"></div>
    <p class="enroll"><b>Now enrolling</b> Academic year 2026–27, all programs. Registration days are August 28 and 31.</p>
  </div>
</section>
<section class="home-facts" aria-label="AGI in numbers"><div class="wrap facts">
  <div><b>2013</b><span>Founded in Agadir, starting with five children</span></div>
  <div><b>46+</b><span>Nationalities hosted over eleven years</span></div>
  <div><b>4</b><span>U.S. state departments of education recognize AGI</span></div>
  <div><b>12</b><span>Regions served by Anglia Morocco from Agadir</span></div>
</div></section>

<section class="section tight bg-white" aria-label="Find your path"><div class="wrap">
  <div class="section-head" style="margin-bottom:28px"><h2>Find your path</h2><p>Information for each of the people AGI serves.</p></div>
  <div class="cards" style="--cols:5">
    <a class="card" href="parents.html"><span class="tag">Parents</span><h3>For your child</h3><p>Admissions, support and what makes AGI different.</p><span class="more">For parents</span></a>
    <a class="card" href="english-anglia.html"><span class="tag">Students</span><h3>Learn &amp; certify English</h3><p>Anglia levels, classes and free level tests.</p><span class="more">English &amp; Anglia</span></a>
    <a class="card" href="teachers.html"><span class="tag">Teachers</span><h3>C.I.T.E. &amp; training</h3><p>A lifelong credential and a 30-day internship.</p><span class="more">For teachers</span></a>
    <a class="card" href="professional.html"><span class="tag">Professionals</span><h3>Business &amp; medical English</h3><p>English for work, for you or your team.</p><span class="more">For professionals</span></a>
    <a class="card" href="investors.html"><span class="tag">Partners</span><h3>Grow with AGI</h3><p>Franchise, representation and partnership.</p><span class="more">Partners &amp; investors</span></a>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>One American standard, for every stage.</h2><p>From a child's first day of kindergarten to an adult's diploma or teaching certificate.</p></div>
  {program_cards()}
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Affordable, creative and inclusive.</h2><p>Our promise to every family since 2013. School + Home + Community = Student Success.</p></div>
  <div class="gallery" style="margin-bottom:28px">{ph("home-classroom", "A multi-grade classroom during a lesson", "4/3", "wide")}{ph("home-reading", "A student reading or presenting", "4/3")}</div>
  <div class="cards" style="--cols:4">
    <div><span class="tag">Affordable</span><h3>Within reach</h3><p>An international standard for working families, with books, mathematics and Anglia exams included.</p></div>
    <div><span class="tag">Creative</span><h3>Learning with imagination</h3><p>American pedagogy in small multi-grade classes, enriched by Montessori and Waldorf ideas.</p></div>
    <div><span class="tag">Inclusive</span><h3>No one held back</h3><p>Grade placement is never lowered for missing documents, language gaps or academic gaps.</p></div>
    <div><span class="tag">English for life</span><h3>Certified progress</h3><p>Every grade is benchmarked on the CEFR and assessed with Anglia Examinations of England.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap director">
  <img src="assets/web/director-julie-wilburn.jpg" alt="Julie A. Wilburn, CEO and Educational Director" width="576" height="720" loading="lazy">
  <div>
    <p class="kicker">From the director</p>
    <p class="quote">“AGI is a child-centered school where students take responsibility for their learning.”</p>
    <p class="prose">We prepare children to be independent, critical thinkers and caring, contributing members of society. We hold high the value of respect – of oneself, of others and of the environment – and we believe the family is an integral part of the program.</p>
    <p class="cite"><b>Julie A. Wilburn</b>CEO &amp; Educational Director · Anglia Examinations Morocco, American Group International of Agadir</p>
    <p style="margin-top:22px"><a class="link" href="about.html">About AGI</a></p>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>What families say</h2><p>Parents, students and graduates in their own words.</p></div>
  {testimonials()}
</div></section>

<section class="section bg-navy"><div class="wrap">
  <div class="section-head"><h2>Joining AGI</h2><p>Students are welcome at any stage. Every new student sits a free placement test.</p></div>
  <div class="adm">
    <div class="cards" style="--cols:2">
      <div><span class="num">01</span><h3>Enquire &amp; visit</h3><p>Tours are arranged individually, so you can meet the team and see the classrooms.</p></div>
      <div><span class="num">02</span><h3>Placement test</h3><p>A free assessment, including the Anglia level test for language learners.</p></div>
      <div><span class="num">03</span><h3>Documents</h3><p>Previous school records, a behavior report, and proof of age, residency and immunization.</p></div>
      <div><span class="num">04</span><h3>Enroll</h3><p>Pay the annual inscription and confirm the monthly plan on registration days.</p></div>
    </div>
    <div>
      <p class="kicker">Key dates 2026–27</p>
      <dl class="dates">
        <div><dt>Registration days</dt><dd>August 28 &amp; 31</dd></div>
        <div><dt>First day of classes</dt><dd>September 7</dd></div>
        <div><dt>Winter break</dt><dd>Dec 18 – Jan 3</dd></div>
        <div><dt>Last day &amp; graduation</dt><dd>June 17, 2027</dd></div>
      </dl>
      <p class="fee">2,600 MAD</p><p style="color:rgba(255,255,255,.7);font-size:14px">a month over ten months, plus an annual inscription. Books, exams and insurance included.</p>
      <div class="btn-row" style="margin-top:24px">{GOLD_APPLY}<a class="btn btn-light" href="admissions.html">Admissions &amp; fees</a></div>
    </div>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Recognized in the United States</h2><p>Accredited by the American Council of Training and Development, recognized by four state departments of education, and in compliance with NCAA, NAIA, College Board and Meridian Learning standards.</p></div>
  <div class="marks">
    <figure><img src="assets/web/seal-tennessee-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Tennessee</b>Department of Education</figcaption></figure>
    <figure><img src="assets/web/seal-florida-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Florida</b>Department of Education</figcaption></figure>
    <figure><img src="assets/web/seal-colorado-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Colorado</b>Department of Education</figcaption></figure>
    <figure><img src="assets/web/seal-alabama-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Alabama</b>Department of Education</figcaption></figure>
  </div>
  <h3 style="margin:44px 0 16px">Our programs are in compliance with</h3>
  <div class="marks">
    <figure><img src="assets/web/mark-ncaa-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>NCAA</b>Eligibility Center</figcaption></figure>
    <figure><img src="assets/web/mark-naia-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>NAIA</b>Eligibility Center</figcaption></figure>
    <figure><img src="assets/web/mark-collegeboard-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>College Board</b>AP &amp; SAT programs</figcaption></figure>
    <figure><img src="assets/web/mark-meridian-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>Meridian Learning</b>Curriculum standards</figcaption></figure>
  </div>
  <div class="note" style="margin:36px 0 0;background:#fff;border-left-color:var(--navy)"><strong style="color:var(--navy)">Official partner in Morocco of Chichester College Group, UK.</strong> AGI is the Anglia franchise holder for Morocco and home of Anglia Morocco. Anglia Examinations is a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding. <a href="english-anglia.html">English &amp; Anglia exams</a></div>
  <p style="margin-top:24px"><a class="link" href="about.html#accreditation">All accreditation and memberships</a></p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>From the journal</h2><p><a class="link" href="journal.html">All journal entries</a></p></div>
  <div class="cards">{news_cards}</div>
</div></section>

<section class="section bg-navy"><div class="wrap visit">
  <div><h2>Come and see the school.</h2><p style="color:rgba(255,255,255,.75);max-width:48ch;margin-top:16px">Tours are arranged individually, Monday to Friday. Tell us when suits you and the office will confirm a time.</p>
    <div class="btn-row" style="margin-top:28px">{GOLD_APPLY}<a class="btn btn-light" href="forms.html#visit">Book a visit</a></div></div>
  <div><address>Number 20, Rue Baalabek<br>Hay Nahda, Agadir 80000, Morocco</address>
    <p style="color:rgba(255,255,255,.75);font-size:15px;line-height:1.9;margin:0"><a style="color:#fff" href="tel:+212528843349">+212 528 843 349</a> · <a style="color:#fff" href="https://wa.me/212688739393">WhatsApp</a> · <a style="color:#fff" href="mailto:americanecoleagadir@gmail.com">Email</a><br>The office is closed on Sundays.</p>
    <p style="margin-top:16px"><a class="link" style="color:#fff" href="https://www.google.com/maps/search/?api=1&amp;query=20+Rue+Baalabek+Hay+Nahda+Agadir">Open in Google Maps</a></p>
    <div style="margin-top:24px">{MAP}</div></div>
</div></section>
""", HOME_CSS)

NETWORK = [("net-agi-seal", "K–12 division", "American Group International School", "The American school of Agadir: a micro-school and K–12 campus, established 2013."),
 ("net-awa", "U.S. registered", "AWA High School for Adults", "Our U.S.-registered company, offering support programs to clients worldwide."),
 ("net-anglia", "Examinations", "Anglia Examinations England", "AGI is the Anglia franchise holder and headquarters for Morocco."),
 ("net-pods", "Learning pods", "AGI Learning Pods & Fast Track", "Small-group programs led by teacherpreneurs."),
 ("net-ahs", "Online partner", "American High School Online", "A Cognia-accredited online high school for grades 9–12."),
 ("net-iheart", "Wellbeing", "I-Heart Women & Family Institute", "Emotional and behavioral support, accredited by IPHM and ICAHP."),
 ("net-ccg", "UK partner", "Chichester College Group", "Seven colleges in the south of England, with UK progression routes."),
 ("net-leverage", "University pathways", "Leverage Edu", "University placement with housing assistance.")]
net = "".join(f'<figure><img src="assets/web/{i}.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>{n}</b>{d}</figcaption></figure>' for i, k, n, d in NETWORK)
ACC = [("American Council of Training and Development", "Accreditation", "AGI's institutional accreditor for the American-curriculum school and its programs."),
 ("U.S. state departments of education", "Recognition", "Recognized by the departments of education of Tennessee, Florida, Colorado and Alabama."),
 ("Cognia", "Accreditation", "The American High School Online program for grades 9–12 is Cognia accredited; the high school books program is Florida accredited."),
 ("QAHE", "Accreditation", "Quality Assurance in Higher Education covers AGI's independent course studies and professional programs."),
 ("American Canadian Board", "Certification", "Professional training certificates, including the Early Childhood Education and Care diploma, are approved by the American Canadian Board."),
 ("Chichester College Group, UK", "Official partner", "AGI is proud to be the official partner in Morocco of Chichester College Group, UK – award winning and Ofsted Outstanding – which owns Anglia Examinations. AGI became the Anglia franchise holder for Morocco in 2021."),
 ("AIM Qualifications · Ofqual", "Regulation", "Anglia's four highest levels of exam are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual in England."),
 ("UCAS", "Recognition", "The Anglia Proficiency examination is listed by UCAS as evidence of English competence for British universities."),
 ("Global Schools Program", "Membership", "An initiative of the UN Sustainable Development Solutions Network, supporting education for sustainable development. Member since 2023."),
 ("American School Counselor Association", "Membership", "AGI joined ASCA in 2026, bringing U.S. school-counseling standards to student guidance.")]
acc = "".join(f'<div><dt>{n}<small style="display:block;font-family:var(--sans);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--red);margin-top:6px">{k}</small></dt><dd>{d}</dd></div>' for n, k, d in ACC)

page("about.html", "About AGI – American Group International, Agadir",
 "The story, mission and people of American Group International, the first American school in Agadir, and its accreditation.",
 hero("<span>About</span>", "The first American school in Agadir.",
      "AGI began in 2013 with five children in one room. Today it is a K–12 micro-school, a center for adult and English education, and the home of Anglia Examinations in Morocco.") + f"""
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Our story</h2>{ph("about-campus", "The school building in Hay Nahda", "4/3")}</div>
  <div class="prose">
    <p>American Group International School is a small private school in the Berber community of the Souss, in Agadir. The first classes started in 2013 with five children. The school soon outgrew its one-room beginnings and moved to Hay Nahda, where kindergarten to grade 12 is now taught in eight multi-grade classrooms.</p>
    <p>Over eleven years, AGI has welcomed students of more than 46 nationalities. Its enrollment is open: the school was created for students who need a program the Moroccan system may not offer – an American curriculum, English immersion, or support for learning differences.</p>
    <p>In 2021 AGI became the Anglia Examinations franchise holder for Morocco, and it now runs the Anglia network across the Kingdom's twelve regions from its Agadir headquarters. Its mission remains the same: an international education that working families in Morocco can afford.</p>
    <p>{PH_TXT('expansion-about', 'Today AGI also works beyond Agadir [to confirm with AGI: other Moroccan cities, Mauritania, and the United States through American Group USA LLC].')}</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Mission, philosophy and vision</h2><p>Affordable, creative and inclusive. “Global Minds with a Global Perspective.” School + Home + Community = Student Success.</p></div>
  <div class="cards">
    <div><span class="tag">Mission</span><p>To serve the Agadir region by giving children a strong educational foundation following American philosophy and practice, so that they become independent, critical thinkers and caring, contributing members of society.</p></div>
    <div><span class="tag">Philosophy</span><p>Academic excellence, discipline, ethical standards and respect for others. We develop the whole child – intellectual, social, emotional, character and physical – and foster a general respect for all humanity.</p></div>
    <div><span class="tag">Vision</span><p>Lifelong learners who pursue excellence, model integrity and honor cultural diversity, equipped to serve their community in Morocco and the wider world with wisdom and compassion.</p></div>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap director">
  <img src="assets/web/director-julie-wilburn.jpg" alt="Julie A. Wilburn" width="576" height="720" loading="lazy">
  <div>
    <p class="kicker">Founder &amp; leadership</p>
    <h2 style="margin-bottom:20px">Julie A. Wilburn</h2>
    <p class="cite" style="margin-bottom:24px">CEO &amp; Educational Director · Anglia Examinations Morocco, American Group International of Agadir</p>
    <div class="prose">
      <p>Julie Wilburn founded AGI and leads all of its educational programs: the primary and high school, curriculum, testing and assessment, staff training and the social-skills program. She also teaches in the classroom.</p>
      <p>She has lived in Morocco for many years and holds dual citizenship. In 2026 she was accredited as a Holistic Therapeutic Coach by IPHM and ICAHP, and she offers ADHD holistic coaching for children and adults.</p>
      <p><em>“We believe in equality, and that an international education empowers students to open global opportunities for their personal growth and success.”</em></p>
      <p><a class="link" href="founder-letter.html">Read Julie's letter to parents</a></p>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>The team</h2><p>A small team, so families always know who to call.</p></div>
  <div class="people">
    <div class="person"><figure class="photo" style="--ratio:4/5"><img src="assets/web/director-julie-wilburn.jpg" alt="" loading="lazy"></figure><h3>Julie A. Wilburn</h3><p>CEO &amp; Educational Director</p></div>
    <div class="person">{ph("team-abdelhak-lam", "Portrait", "4/5")}<h3>Abdelhak Lam</h3><p>Sales Coordinator, main headquarters</p></div>
    <div class="person">{ph("team-teacher-1", "Portrait", "4/5")}<h3 class="ph-text" data-placeholder="team:teacher-1">Teacher name</h3><p>Lower school · grades K–5</p></div>
    <div class="person">{ph("team-teacher-2", "Portrait", "4/5")}<h3 class="ph-text" data-placeholder="team:teacher-2">Teacher name</h3><p>Middle &amp; upper school · English</p></div>
    <div class="person">{ph("team-teacher-3", "Portrait", "4/5")}<h3 class="ph-text" data-placeholder="team:teacher-3">Teacher name</h3><p>Mathematics &amp; science</p></div>
    <div class="person">{ph("team-teacher-4", "Portrait", "4/5")}<h3 class="ph-text" data-placeholder="team:teacher-4">Teacher name</h3><p>Special education support</p></div>
    <div class="person">{ph("team-anglia", "Portrait", "4/5")}<h3 class="ph-text" data-placeholder="team:anglia-coordinator">Name</h3><p>Anglia Morocco coordinator</p></div>
    <div class="person">{ph("team-admissions", "Portrait", "4/5")}<h3 class="ph-text" data-placeholder="team:admissions">Name</h3><p>Admissions office · <a class="link" href="forms.html">Forms &amp; requests</a></p></div>
  </div>
</div></section>

<section class="section bg-white" id="accreditation"><div class="wrap">
  <div class="section-head"><h2>Accreditation &amp; memberships</h2><p>Where AGI's standards come from, and who holds us to them.</p></div>
  <div class="marks" style="margin-bottom:40px">
    <figure><img src="assets/web/seal-tennessee-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Tennessee</b>Department of Education</figcaption></figure>
    <figure><img src="assets/web/seal-florida-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Florida</b>Department of Education</figcaption></figure>
    <figure><img src="assets/web/seal-colorado-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Colorado</b>Department of Education</figcaption></figure>
    <figure><img src="assets/web/seal-alabama-clean.png" alt="" width="120" height="120" loading="lazy"><figcaption><b>Alabama</b>Department of Education</figcaption></figure>
  </div>
  <dl class="rows">{acc}</dl>
  <h3 style="margin-top:48px">Our programs are in compliance with</h3>
  <div class="marks" style="margin-top:16px">
    <figure><img src="assets/web/mark-ncaa-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>NCAA</b>Eligibility Center</figcaption></figure>
    <figure><img src="assets/web/mark-naia-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>NAIA</b>Eligibility Center</figcaption></figure>
    <figure><img src="assets/web/mark-meridian-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>Meridian Learning</b>Curriculum standards</figcaption></figure>
    <figure><img src="assets/web/mark-collegeboard-clean.png" alt="" width="160" height="84" loading="lazy"><figcaption><b>College Board</b>AP &amp; SAT programs</figcaption></figure>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>The AGI network</h2><p>Divisions, partners and the institutions we work with.</p></div>
  <div class="marks">{net}</div>
</div></section>
""" + cta("Meet us in Agadir.", "Visits are arranged individually, Monday to Friday.", GOLD_APPLY + LIGHT_VISIT))

page("programs.html", "Programs – American Group International, Agadir",
 "AGI programs: K–12 school, special education, adult high school diploma, English and Anglia exams, teacher training and university pathways.",
 hero("<span>Programs</span>", "Programs for every stage.",
      "Every AGI program shares one American academic standard. Each has its own curriculum, calendar and admission requirements – and every learner starts with a free placement test.") + f"""
<section class="section bg-white"><div class="wrap">{program_cards(cols=2)}</div></section>
""" + cta("Not sure which program fits?", "Book a visit or send a question – the office will help you choose and arrange a free placement test.",
           GOLD_APPLY + '<a class="btn btn-light" href="forms.html#enquiry/programs">Ask a question</a>'))

def program_page(name, crumb, title, desc, h1, lede, body, cta_title, cta_text, cta_buttons):
    others = f'<section class="section"><div class="wrap"><div class="section-head"><h2>Other programs</h2><p><a class="link" href="programs.html">All programs</a></p></div>{program_cards(current=name)}</div></section>'
    page(name, f"{title} – American Group International, Agadir", desc,
         hero(f'<a href="programs.html">Programs</a> / <span>{crumb}</span>', h1, lede, APPLY + VISIT)
         + f'<div class="wrap" style="padding-bottom:clamp(40px,5vw,72px)">{ph("program-" + name.replace(".html", ""), crumb + " – students in class or activity", "21/8")}</div>' + body + cta(cta_title, cta_text, cta_buttons) + others)

program_page("special-education.html", "Special education", "Special education (SEN)",
 "Special education at AGI Agadir: Individualized Education Plans, small groups, therapy support and a special-needs high school program.",
 "Every child, supported.",
 "AGI welcomes students with learning differences, mental health challenges, physical or developmental disabilities, and gifted learners – in small classes, with a plan built for each child.", """
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Our approach</h2><p>Mainstream and special-needs students learn in the same community. Support is planned with parents and, where needed, with the child's doctors and therapists.</p></div>
  <dl class="rows">
    <div><dt>Individualized Education Plans</dt><dd>Each student's plan sets goals and accommodations for their needs and abilities, and is reviewed with parents through the year.</dd></div>
    <div><dt>Small-group classrooms</dt><dd>Small classes mean personal attention and a calm, supportive place to learn.</dd></div>
    <div><dt>Therapy and behavioral support</dt><dd>From occupational therapy to speech-language pathology and behavioral care, working with professional caregivers.</dd></div>
    <div><dt>An inclusive community</dt><dd>Every student is valued, respected and given the chance to thrive alongside their classmates.</dd></div>
  </dl>
</div></section>
<section class="section"><div class="wrap split">
  <div class="intro"><h2>Special-needs high school</h2><p>A program designed around the academic, social and emotional needs of teenagers with special needs.</p></div>
  <div class="prose">
    <p>The high school program focuses on life skills, vocational training and preparing for independence, so students leave with the tools to succeed after graduation.</p>
    <p>Subjects follow the AGI spine with individual accommodations: English, mathematics, science, history, reading, spelling, Arabic, physical education, fine arts and ESL.</p>
    <h3>Before you apply</h3>
    <p>To provide an IEP or special-needs support, AGI needs documentation from a licensed practitioner, together with the student's previous school records and a behavior report. A parent's description alone isn't enough to put the right support in place.</p>
    <p>Related services: <a href="professional.html#adhd">ADHD holistic coaching</a> for children and adults, and emotional and behavioral support through our partner, the I-Heart Women &amp; Family Institute.</p>
  </div>
</div></section>
""", "Talk to us about your child.", "Book a visit to meet the team, or send a question first – everything you share is handled in confidence.",
 GOLD_APPLY + '<a class="btn btn-light" href="forms.html#visit">Book a visit</a>')

program_page("adult-diploma.html", "Adult high school diploma", "Adult high school diploma",
 "Earn an American high school diploma in Agadir: a self-paced program for learners aged 16 and over, with American Worldwide Academy and tests proctored on site.",
 "Finish high school, on your schedule.",
 "For learners aged 16 and over who left school before graduating: a low-cost, self-directed American high school completion program, studied by correspondence or online.", """
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>How it works</h2><p>Offered in partnership with American Worldwide Academy. AGI's first adult graduate received their diploma in 2019.</p></div>
  <dl class="rows">
    <div><dt>Study at your own pace</dt><dd>Work through each course independently, online or by correspondence, with tutorial help when you need it.</dd></div>
    <div><dt>Tests in Agadir</dt><dd>Every test is proctored on site at the AGI center. Graduation requires a passing score of 80 percent.</dd></div>
    <div><dt>English included</dt><dd>All students learn English and sit an English exam as part of the program.</dd></div>
    <div><dt>Support after graduation</dt><dd>Enrollment and graduation verification, letters of recommendation and official transcripts for further study.</dd></div>
  </dl>
</div></section>
<section class="section"><div class="wrap split">
  <div class="intro"><h2>Courses</h2><p>A nationally accredited program. Course examples:</p></div>
  <div class="table-wrap"><table>
    <thead><tr><th>Course</th><th>Credits</th><th>Covers</th></tr></thead>
    <tbody>
      <tr><td><b>English language writing skills</b></td><td>2</td><td>Usage, grammar, sentence structure, mechanics, punctuation and spelling</td></tr>
      <tr><td><b>English literature</b></td><td>2</td><td>Classical and contemporary fiction, poetry, prose and non-fiction</td></tr>
      <tr><td><b>General mathematics</b></td><td>3</td><td>Arithmetic, consumer mathematics, data analysis, algebra and geometry</td></tr>
      <tr><td><b>Social science I – American history</b></td><td>2</td><td>From the colonial period to the Second World War</td></tr>
    </tbody></table></div>
</div></section>
""", "Ready to finish your diploma?", "Apply online and the office will explain the next steps, fees and test dates.",
 GOLD_APPLY + '<a class="btn btn-light" href="forms.html#enquiry/programs">Ask a question</a>')

CEFR = [("Kindergarten", "5–6", "Pre-A1 / A1", "Understands simple classroom instructions and basic vocabulary."),
 ("Grades 1–2", "6–8", "A1 – A2", "Speaks in simple sentences; reads short stories and writes simple sentences."),
 ("Grades 3–4", "8–10", "A2 – A2+", "Follows lessons, writes short paragraphs and explains ideas in discussion."),
 ("Grade 5", "10–11", "B1", "Reads chapter books and writes organized paragraphs. Elementary graduation benchmark."),
 ("Grades 6–8", "11–14", "B1+ – B2", "Understands academic vocabulary and lectures; writes essays and analyses texts."),
 ("Grades 9–11", "14–17", "B2 – C1", "Handles academic reading, research, debate and complex presentations."),
 ("Grade 12", "17–18", "C1", "University-level reading and academic writing.")]
cefr = "".join(f"<tr><td><b>{g}</b></td><td>{a}</td><td>{l}</td><td>{s}</td></tr>" for g, a, l, s in CEFR)
program_page("english-anglia.html", "English & Anglia exams", "English & Anglia exams",
 "Anglia Examinations Morocco headquarters in Agadir: ten CEFR levels, Saturday English classes for children, adult courses and free level testing.",
 "English, measured step by step.",
 "AGI is the headquarters of Anglia Examinations in Morocco. Children and adults learn English in small groups and certify their level with exams from England – starting with a free level test.", f"""
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Anglia Examinations</h2><p>Based in Chichester, England, since 1993. AGI has used the Anglia system in its language programs since 2013, and in 2021 became the Anglia franchise holder for Morocco. AGI is proud to be the official partner in Morocco of Chichester College Group, UK.</p></div>
  <dl class="rows">
    <div><dt>Ten levels</dt><dd>From young learner to expert user, mapped to the Common European Framework (CEFR). There is no minimum age; young learners start at about four.</dd></div>
    <div><dt>All four skills</dt><dd>Every level tests listening, reading, writing and speaking.</dd></div>
    <div><dt>Business English</dt><dd>Anglia International Business English, at four levels from A2+ to C1.</dd></div>
    <div><dt>Recognized in the UK</dt><dd>Anglia Examinations is a wholly owned subsidiary of the Chichester College Group, award winning and Ofsted Outstanding. The four highest levels are awarded by AIM Qualifications and Assessment Group, regulated by Ofqual. The Proficiency level is listed by UCAS as evidence of English for British universities.</dd></div>
  </dl>
</div></section>
<section class="section" id="classes"><div class="wrap">
  <div class="section-head"><h2>Classes &amp; prices</h2><p>Groups never exceed ten students. Level testing is free; class times are agreed after the test.</p></div>
  <div class="table-wrap"><table>
    <thead><tr><th>Option</th><th>Who</th><th>Price</th></tr></thead>
    <tbody>
      <tr><td><b>Saturday classes for children</b></td><td>Ages 5–18, Saturdays 2:00–4:00 p.m., October to June</td><td>500 MAD a month, yearly Anglia exam included</td></tr>
      <tr><td><b>One-to-one</b></td><td>English or mathematics</td><td>200 MAD per session</td></tr>
      <tr><td><b>Small group</b></td><td>2–3 students</td><td>150 MAD per person, per session</td></tr>
      <tr><td><b>Group course</b></td><td>4–10 students, 12 weeks</td><td>100 MAD a week per student (1,200 MAD)</td></tr>
    </tbody></table></div>
  <p class="muted" style="font-size:13px;margin-top:12px">Prices effective November 2024. Books and insurance are not included.</p>
</div></section>
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Courses for teenagers and adults</h2></div>
  <dl class="rows">
    <div><dt>Exam preparation</dt><dd>Practice for Moroccan school graduation and British exams.</dd></div>
    <div><dt>Conversation</dt><dd>Speaking practice and new vocabulary.</dd></div>
    <div><dt>ESL 100 – 300</dt><dd>From beginner to advanced (B2): academic reading, essays and research writing.</dd></div>
    <div><dt>English writing</dt><dd>Narrative and descriptive writing, job applications and CVs.</dd></div>
    <div><dt>Business &amp; medical English</dt><dd>For organizations and clinicians – see <a class="link" href="professional.html">professional programs</a>.</dd></div>
  </dl>
</div></section>
<section class="section" id="anglia-morocco"><div class="wrap">
  <div class="section-head"><h2>Anglia Morocco online</h2><p>Exam dates, books and practice material are published on the official Anglia Morocco website.</p></div>
  <div class="cards">
    <a class="card" href="https://angliamorocco.org/anglia-exam-dates-2/" target="_blank" rel="noopener"><span class="tag">angliamorocco.org</span><h3>Exam dates</h3><p>The year's exam sessions for every level, from First Step to Masters.</p><span class="more">See the dates</span></a>
    <a class="card" href="https://angliamorocco.org/step-to-books-2/" target="_blank" rel="noopener"><span class="tag">angliamorocco.org</span><h3>Step To books &amp; audio</h3><p>Preparation books for each level, the book order form and the audio files.</p><span class="more">Order books</span></a>
    <a class="card" href="https://angliamorocco.org/practice-resources/" target="_blank" rel="noopener"><span class="tag">angliamorocco.org</span><h3>Practice resources</h3><p>Sample papers and practice material to prepare for the exams.</p><span class="more">Practice</span></a>
    <a class="card" href="https://angliamorocco.org/citem/" target="_blank" rel="noopener"><span class="tag">angliamorocco.org</span><h3>C.I.T.E. for teachers</h3><p>Register for the Certificate for International Teachers of English.</p><span class="more">Register</span></a>
    <a class="card" href="https://angliamorocco.org/angliamorocco-networks-and-centers-12-regions/" target="_blank" rel="noopener"><span class="tag">angliamorocco.org</span><h3>Network &amp; centers</h3><p>The Anglia Morocco network across the twelve regions, and open representative positions.</p><span class="more">See the network</span></a>
    <a class="card" href="https://angliamorocco.org/faq/" target="_blank" rel="noopener"><span class="tag">angliamorocco.org</span><h3>Questions about the exams</h3><p>How long each exam lasts, what it assesses and how levels are grouped.</p><span class="more">Read the FAQ</span></a>
  </div>
</div></section>
<section class="section" id="cefr"><div class="wrap">
  <div class="section-head"><h2>English benchmarks at AGI</h2><p>How English develops through the K–12 school. Students who don't speak English at home often start half a level lower and catch up by middle school.</p></div>
  <div class="table-wrap"><table><thead><tr><th>Grade</th><th>Age</th><th>CEFR level</th><th>What students can do</th></tr></thead><tbody>{cefr}</tbody></table></div>
</div></section>
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Anglia across Morocco</h2></div>
  <div class="prose"><p>From its Agadir headquarters, Anglia Morocco works with schools, language centers and teachers in the Kingdom's twelve regions. Schools can become Anglia exam centers, and franchise opportunities are open in several regions.</p>
  <p>Anglia Morocco contacts: <a href="mailto:j.wilburn@angliamorocco.org">j.wilburn@angliamorocco.org</a> · <a href="mailto:a.lam@angliamorocco.org">a.lam@angliamorocco.org</a></p>
  <p><a class="link" href="partnerships.html">Partnerships &amp; franchise</a> &nbsp; <a class="link" href="https://angliamorocco.org/" target="_blank" rel="noopener">angliamorocco.org</a></p></div>
</div></section>
""", "Find your level.", "Book a free Anglia level test – the office will suggest the right class afterwards.",
 '<a class="btn btn-gold" href="forms.html#enquiry/anglia">Book a level test</a><a class="btn btn-light" href="forms.html#tutor-request">Request a tutor</a>')

PRO = [("cite", "C.I.T.E. / TESOL", "For English teachers", "Anglia's Certificate for International Teachers of English: no entry qualifications required, mapped to the CEFR, and a lifelong recognition of teaching competence. AGI also partners with Bridge Education Group for accredited TEFL/TESOL courses."),
 ("training", "Teacher training program", "For classroom practice", "English teachers test and train in AGI classrooms to strengthen their language and their teaching."),
 ("sponsorship", "USA teacher sponsorship", "For aspiring educators", "Certification sponsorship for private-school teaching in the United States. Requires a bachelor's degree, a clear background check and a sponsoring school. Fee: $60. Not valid for U.S. public schools."),
 ("courses", "Independent course studies", "Self-paced", "Graduate-level, self-taught modules using books and journals; certificates approved by the American Canadian Board."),
 ("proctoring", "Proctoring services", "Exam invigilation", "Paper and online exams invigilated at AGI for distance learners of North American and British universities, companies and certification bodies. Monday to Thursday, 9:00–17:00. A 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour."),
 ("business", "Corporate & business English", "For organizations", "Anglia Business English in four steps from A2+ to C1, on site at your company or at AGI."),
 ("medical", "Medical English", "For clinicians", "English for medical professionals: patient communication, handovers, seminars and medical papers."),
 ("adhd", "ADHD holistic coaching", "In Agadir and online", "One-to-one coaching for children and adults on focus, organization and time management, with Julie Wilburn, an accredited Holistic Therapeutic Coach (IPHM, ICAHP).")]
pro = "".join(f'<div id="{i}"><dt>{n}<small style="display:block;font-family:var(--sans);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--red);margin-top:6px">{w}</small></dt><dd>{d}</dd></div>' for i, n, w, d in PRO)
program_page("professional.html", "Teacher training & professional", "Teacher training & professional programs",
 "Teacher training and professional services at AGI Agadir: C.I.T.E./TESOL, exam proctoring, U.S. teacher sponsorship, business and medical English, ADHD coaching.",
 "For teachers, clinicians and professionals.",
 "AGI's work goes beyond the school day: certification for teachers, English for professional practice, exam invigilation for distance learners, and coaching.",
 f'<section class="section bg-white"><div class="wrap"><dl class="rows">{pro}</dl></div></section>',
 "Ask about a program.", "Tell us what you need – a certificate, a course for your team or an exam session – and the office will reply within one working day.",
 '<a class="btn btn-gold" href="forms.html#enquiry/programs">Send an enquiry</a><a class="btn btn-light" href="contact.html">Contact</a>')

program_page("pathways.html", "University pathways", "University pathways",
 "AGI Education Consultancy: an authorized admissions agent helping students in Morocco reach universities and colleges in the UK, the USA and beyond.",
 "From Agadir to university.",
 "AGI Education Consultancy is an authorized admissions agent. We help students choose a university, apply, and arrive ready – whether on campus abroad or studying online.", """
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>What we help with</h2><p>Each case is studied individually, with a plan built around the student's goals.</p></div>
  <dl class="rows">
    <div><dt>Choosing and applying</dt><dd>Matching programs to your goals and handling applications to partner universities, locally, abroad or online.</dd></div>
    <div><dt>Moving abroad</dt><dd>Accommodation, visa applications, health insurance and support for families.</dd></div>
    <div><dt>Funding</dt><dd>Help with scholarship and financial-aid applications.</dd></div>
    <div><dt>More than one diploma</dt><dd>Double-diploma programs and language training alongside your studies.</dd></div>
    <div><dt>Career guidance</dt><dd>Career counseling and cultural orientation before you leave.</dd></div>
  </dl>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Partners</h2><p>Part of a wider network of universities and colleges in the United States, Europe and Asia.</p></div>
  <div class="cards">
    <div><span class="tag">United Kingdom</span><h3>Chichester College Group</h3><p>Seven colleges in the south of England – Chichester, Crawley, Worthing, Brinsbury, Brighton MET, Northbrook and Haywards Heath – with UK progression routes for AGI learners.</p><a class="more" href="journal-ccgi-partnership.html">Read about the partnership</a></div>
    <div><span class="tag">Placement</span><h3>Leverage Edu</h3><p>Our regional partner for the Souss and southern Morocco: private and public university placement, with housing assistance.</p></div>
    <div><span class="tag">English requirement</span><h3>Anglia Proficiency</h3><p>Listed by UCAS as evidence of English for British universities – and taken right here in Agadir.</p><a class="more" href="english-anglia.html">English &amp; Anglia exams</a></div>
  </div>
</div></section>
""", "Plan your next step.", "Tell us where you'd like to study. The office will reply within one working day.",
 '<a class="btn btn-gold" href="forms.html#enquiry/programs">Start a conversation</a><a class="btn btn-light" href="forms.html#visit">Book a visit</a>')

page("student-life.html", "Student life – American Group International, Agadir",
 "Life at AGI: a small international community in Agadir, service hours, homework, Saturday classes and events through the year.",
 hero("<span>Student life</span>", "A small school with a big world inside.",
      "Students from more than 46 nationalities learn together in small multi-grade classes, where teachers know every child and every family.") + f"""
<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Life at AGI</h2><p>A school day in Hay Nahda.</p></div>
  <div class="gallery">{ph("life-1", "Morning circle or classroom discussion", "4/3", "wide")}{ph("life-2", "Science or art project", "4/3")}{ph("life-3", "Saturday Anglia class", "4/3")}{ph("life-4", "Students at a park outing", "4/3")}{ph("life-5", "Graduation day", "4/3")}{ph("life-6", "Spelling bee or school event", "4/3", "wide")}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Voices of AGI</h2><p>Parents, students and graduates.</p></div>
  {testimonials()}
</div></section>
<section class="section"><div class="wrap split">
  <div class="intro"><h2>The school year</h2><p>Highlights from the AGI calendar.</p></div>
  <dl class="rows">
    <div><dt>Moroccan &amp; American holidays</dt><dd>The calendar marks both: Green March and Independence Day, Thanksgiving, Amazigh New Year and the Eids.</dd></div>
    <div><dt>Global Play Day</dt><dd>A day each February given over to unstructured play, joined by schools around the world.</dd></div>
    <div><dt>Anglia exams</dt><dd>Every spring, students certify their English level with Anglia Examinations of England.</dd></div>
    <div><dt>Spelling bee</dt><dd>AGI students compete in the American National Spelling Bee of Morocco, held at the American Legation in Tangier. <a class="link" href="journal/american-national-spelling-bee-in-morocco.html">Read the story</a></dd></div>
    <div><dt>Graduation</dt><dd>The year ends in June with graduation for the senior class. <a class="link" href="journal.html">Journal</a></dd></div>
  </dl>
</div></section>
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Service to the community</h2><p>A graduation requirement for every high school student.</p></div>
  <div class="prose">
    <p>High school students complete <strong>40 volunteer hours</strong> – ten each year – documented and approved by the school. Activities must benefit the community, be unpaid, and not be part of a regular job or family obligation.</p>
    <p>Examples include community clean-ups, helping at local libraries and non-profits, tutoring younger students and helping at school events outside school hours.</p>
  </div>
</div></section>
<section class="section"><div class="wrap split">
  <div class="intro"><h2>Homework</h2><p>A guide to nightly homework by grade, so learning at home stays balanced.</p></div>
  <div class="table-wrap"><table><thead><tr><th>Grades</th><th>Per night</th><th>Typical work</th></tr></thead><tbody>
    <tr><td><b>K – 1</b></td><td>10–20 min</td><td>Reading with parents, simple math, basic writing</td></tr>
    <tr><td><b>2 – 3</b></td><td>20–30 min</td><td>Reading, spelling, math problems, short writing</td></tr>
    <tr><td><b>4 – 5</b></td><td>30–60 min</td><td>Reading, vocabulary, math, small projects</td></tr>
    <tr><td><b>6 – 8</b></td><td>60–90 min</td><td>All core subjects, foreign language, project work</td></tr>
    <tr><td><b>9 – 10</b></td><td>90–120 min</td><td>Core subjects, foreign language, electives</td></tr>
    <tr><td><b>11 – 12</b></td><td>120–180 min</td><td>Core subjects, AP courses, college preparation</td></tr>
  </tbody></table></div>
</div></section>
<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>For parents</h2><p>The forms families use most.</p></div>
  <div class="cards">
    <a class="card" href="forms.html#absence"><h3>Report an absence</h3><p>Before 9:00 on the day, for absences, late arrivals and early pick-ups.</p><span class="more">Open form</span></a>
    <a class="card" href="forms.html#consent"><h3>Park &amp; outing consent</h3><p>Permission for park visits and outdoor activities.</p><span class="more">Open form</span></a>
    <a class="card" href="forms.html#feedback"><h3>Parent feedback</h3><p>Suggestions, praise or a concern, reviewed every week.</p><span class="more">Open form</span></a>
  </div>
</div></section>
""" + cta("See it for yourself.", "The best way to know AGI is to visit during the school day.", GOLD_APPLY + LIGHT_VISIT))

POL = [("attendance", "Attendance", "K–12 students must attend 90% of the school year to be promoted. Parents give a dated, signed excuse for any absence within two days of the student's return. Arriving after 9:00 is a late arrival; after 10:00 it counts as a full-day absence. Five unexcused late arrivals equal one unexcused absence."),
 ("promotion", "Promotion & retention", "Promotion follows the grade-level criteria: at least 64% (D) in each core subject – mathematics, science, language arts and social studies – 90% attendance, maturity shown through the year and the English assessment. Students who are not promoted may attend summer remediation and be retested."),
 ("placement", "Provisional placement", "Every new student sits English/ESL and academic assessments before admission, whatever system they come from, so placement holds even when previous records are incomplete."),
 ("parents", "Parent responsibility", "Enrollment begins with a 90-day adjustment period and shared expectations on attendance, participation, safeguarding and following up on learning at home."),
 ("refunds", "Refunds & complaints", "One procedure across all divisions – the school, AGI Learning Pods, iHeart therapeutic services and Anglia Morocco – covering enrollment, refunds, complaints and counseling. The annual inscription is non-refundable."),
 ("counseling", "School counseling", "Guidance from the school counselor is advisory: it supports academic success and personal growth but is not medical diagnosis or therapy."),
 ("media", "Media", "How photos, video and live streams of school events may be used on the website, social media and print – always with consent and safeguarding first."),
 ("service", "Service hours", "High school graduation requires 40 documented volunteer hours, ten each year, approved by the school."),
 ("homework", "Homework", "Nightly homework grows from 10–20 minutes in kindergarten to 2–3 hours in the last years of high school.")]
pol = "".join(f'<div id="{i}"><dt>{n}</dt><dd>{d}</dd></div>' for i, n, d in POL)
page("policies.html", "Policies – American Group International, Agadir",
 "AGI school policies: attendance, promotion and retention, placement, parent responsibility, refunds and complaints, media and service hours.",
 hero('<a href="admissions.html">Admissions</a> / <span>Policies</span>', "Policies for families.",
      "The rules we hold ourselves and our families to, in brief. The full texts are part of the AGI Academic Handbook and are available from the office.",
      '<a class="btn btn-primary" href="forms.html#enquiry/programs">Request the full texts</a><a class="btn btn-ghost" href="forms.html#absence">Report an absence</a>') + f"""
<section class="section bg-white"><div class="wrap"><dl class="rows">{pol}</dl></div></section>
""")

CONTACT_JS = """
(function () {
  var CONFIG = { endpoint: null, email: "americanecoleagadir@gmail.com" };  // endpoint: "/api/trpc/forms.submit" once the API is live
  var form = document.getElementById("contact-form"), done = document.getElementById("contact-done");
  if (!form) return;
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;
    var d = Object.fromEntries(new FormData(form).entries());
    var btn = form.querySelector("button[type=submit]"); btn.disabled = true; btn.textContent = "Sending…";
    function finish(html) { form.hidden = true; done.innerHTML = html; done.hidden = false; done.focus(); btn.disabled = false; btn.textContent = "Send message"; }
    function viaEmail() {
      var subject = "Website message – " + d.topic + " – " + d.name;
      var body = ["Name: " + d.name, "Email: " + d.email, "Phone: " + (d.phone || "–"), "Topic: " + d.topic, "", d.message].join("\\n");
      var href = "mailto:" + CONFIG.email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
      location.href = href;
      finish("<h3>Check your email app</h3><p>Your email app has opened with your message filled in. Press Send to deliver it to " + CONFIG.email + ".</p>" +
             "<p>No email app? Write to us on WhatsApp at +212 688 739 393.</p><p><a class='btn btn-primary' href='" + href.replace(/'/g, '%27') + "'>Open email again</a></p>");
    }
    if (!CONFIG.endpoint) return viaEmail();
    fetch(CONFIG.endpoint, { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ json: { type: "contact", name: d.name, email: d.email, phone: d.phone || undefined, payload: { topic: d.topic, message: d.message } } }) })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function () { finish("<h3>Message sent</h3><p>Thank you. The office replies within one working day, Monday to Friday.</p>"); })
      .catch(viaEmail);
  });
})();
"""
CONTACT_CSS = """
.contact-grid{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:clamp(32px,5vw,88px);align-items:start}
.cform{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px 24px}
.cform .full{grid-column:1/-1}
.cform label{display:block;font-size:14px;font-weight:500;margin:0 0 6px}
.cform .opt{font-weight:400;font-size:12.5px;color:var(--muted);margin-left:6px}
.cform input,.cform select,.cform textarea{width:100%;font:inherit;font-size:15px;color:var(--ink);background:#fff;border:1px solid rgba(10,49,97,.28);border-radius:0;padding:11px 13px;min-height:48px}
.cform textarea{min-height:150px;resize:vertical}
.cform select{appearance:none;-webkit-appearance:none;padding-right:40px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1.5l5 5 5-5' fill='none' stroke='%230A3161' stroke-width='1.6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center}
.cform :focus{outline:2px solid var(--navy);outline-offset:1px;border-color:var(--navy)}
.cform :user-invalid{border-color:var(--red);background:#FBEDEE}
.cform .err{display:none;font-size:12.5px;color:var(--red);margin:6px 0 0}
.cform div:has(:user-invalid)>.err{display:block}
.cform .actions{display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px}
.cform small{font-size:12.5px;color:var(--grey);max-width:44ch}
#contact-done{border:1px solid var(--line);border-top:3px solid var(--navy);background:var(--paper);padding:28px 32px}
#contact-done:focus{outline:none}
.details dt{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--red);margin:0 0 6px}
.details dd{margin:0 0 24px;font-family:var(--serif);font-size:21px;line-height:1.45;color:var(--navy)}
.details dd small{display:block;font-family:var(--sans);font-size:13.5px;color:var(--grey)}
@media (max-width:900px){.contact-grid,.cform{grid-template-columns:minmax(0,1fr)}}
"""
TOPICS = ["Programs & admissions", "Anglia examinations", "Fees & payments", "Documents & records", "Partnership or franchise", "Other"]
topics = "".join(f"<option>{t}</option>" for t in TOPICS)
page("contact.html", "Contact – American Group International, Agadir",
 "Contact AGI in Agadir: 20 Rue Baalabek, Hay Nahda. Phone +212 528 843 349, WhatsApp +212 688 739 393, americanecoleagadir@gmail.com.",
 hero("<span>Contact</span>", "Contact AGI.", "Send a message, call or visit. The office replies within one working day and is closed on Sundays.") + f"""
<section class="section bg-white"><div class="wrap contact-grid">
  <div>
    <h2 style="margin-bottom:28px">Send us a message</h2>
    <form id="contact-form" class="cform" autocomplete="on">
      <div><label for="c-name">Full name</label><input id="c-name" name="name" required autocomplete="name" maxlength="255" aria-describedby="c-name-e"><p class="err" id="c-name-e">Enter your name</p></div>
      <div><label for="c-email">Email</label><input id="c-email" name="email" type="email" required autocomplete="email" maxlength="255" aria-describedby="c-email-e"><p class="err" id="c-email-e">Enter an email address, for example name@example.com</p></div>
      <div><label for="c-phone">Phone or WhatsApp<span class="opt">optional</span></label><input id="c-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" pattern="\\+?[0-9 \\-]{{8,20}}" aria-describedby="c-phone-e"><p class="err" id="c-phone-e">Enter a phone number with the country code, for example +212 6 12 34 56 78</p></div>
      <div><label for="c-topic">Topic</label><select id="c-topic" name="topic" required aria-describedby="c-topic-e"><option value="">Choose…</option>{topics}</select><p class="err" id="c-topic-e">Choose a topic</p></div>
      <div class="full"><label for="c-message">Message</label><textarea id="c-message" name="message" required maxlength="3000" aria-describedby="c-message-e"></textarea><p class="err" id="c-message-e">Write your message</p></div>
      <div class="full actions"><button class="btn btn-primary" type="submit">Send message</button><small>Your message goes only to the AGI office in Agadir. See our <a href="privacy.html">privacy policy</a>.</small></div>
    </form>
    <div id="contact-done" hidden role="status" tabindex="-1"></div>
  </div>
  <dl class="details">
    <dt>Visit</dt><dd>Number 20, Rue Baalabek<br>Hay Nahda, Agadir 80000<small><a href="https://www.google.com/maps/search/?api=1&amp;query=20+Rue+Baalabek+Hay+Nahda+Agadir">Open in Google Maps</a></small></dd>
    <dt>Call</dt><dd><a href="tel:+212528843349">+212 528 843 349</a><small>Administration · in Arabic: <a href="tel:+212618639911">+212 618 639 911</a></small></dd>
    <dt>WhatsApp</dt><dd><a href="https://wa.me/212688739393">+212 688 739 393</a></dd>
    <dt>Email</dt><dd style="word-break:break-all"><a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a></dd>
    <dt>Opening hours</dt><dd><span class="ph-text" data-placeholder="fact:office-hours">Monday to Friday, 9:00–17:00</span><small>Closed on Sundays</small></dd>
  </dl>
</div></section>
<section class="section tight"><div class="wrap">{MAP}</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>Looking for a specific request?</h2><p>These forms go straight to the right person.</p></div>
  <div class="cards">
    <a class="card" href="forms.html#visit"><h3>Book a visit</h3><p>Tours are arranged individually, Monday to Friday.</p><span class="more">Open form</span></a>
    <a class="card" href="forms.html#enrollment"><h3>Apply</h3><p>Apply for a place in any AGI program.</p><span class="more">Open form</span></a>
    <a class="card" href="forms.html#documents"><h3>Request a document</h3><p>Transcripts, certificates and attestations.</p><span class="more">Open form</span></a>
  </div>
</div></section>
<script>{CONTACT_JS}</script>
""", CONTACT_CSS)

LEGAL_CSS = ".prose h2{font-size:clamp(24px,2.2vw,30px);margin:1.8em 0 .5em;color:var(--navy)}"
page("privacy.html", "Privacy policy – American Group International, Agadir", "How American Group International and Anglia Morocco handle personal information on this website.",
 hero("<span>Privacy</span>", "Privacy policy.", "How American Group International and Anglia Morocco handle the information you share on this website. Last updated October 2026.") + """
<section class="section bg-white"><div class="wrap"><div class="prose">
<h2>What we collect</h2><p>When you send a form, write to us or call, we receive the details you give us – usually your name, contact details and information about the student or request. This website does not use advertising or tracking cookies. Fonts are loaded from Google Fonts, which receives your browser's standard technical information.</p>
<h2>How we use it</h2><p>Only to handle your request and to provide the programs and services you ask about – for example to answer an enquiry, process an application or prepare a document. We do not sell your information.</p>
<h2>How forms are sent</h2><p>Website forms are delivered to the AGI office by email. Information sent over the internet can never be guaranteed to be completely secure; please don't include more than the form asks for.</p>
<h2>Payments</h2><p>We never ask for card numbers in our forms and do not store card details. Online card payments are made on a separate, secure payment provider's page, under that provider's privacy policy.</p>
<h2>Sharing</h2><p>We share personal information only when the law requires it, to prevent fraud, or when you ask us to – for example sending your documents to a university.</p>
<h2>Links to other sites</h2><p>Links to other websites are provided for convenience. We are not responsible for their privacy practices.</p>
<h2>Your questions</h2><p>To ask about, correct or remove information you have given us, write to <a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a>.</p>
</div></div></section>""", LEGAL_CSS)

page("terms.html", "Terms of use – American Group International, Agadir", "Terms of use for the American Group International and Anglia Morocco website.",
 hero("<span>Terms</span>", "Terms of use.", "The terms that apply to using this website. Last updated October 2026.") + """
<section class="section bg-white"><div class="wrap"><div class="prose">
<h2>About this website</h2><p>This website is published by American Group International and Anglia Morocco, Number 20, Rue Baalabek, Hay Nahda, Agadir, Morocco.</p>
<h2>Information on the site</h2><p>We work to keep program details, dates and fees accurate, but they can change. The office confirms fees, dates and availability before enrollment. Enrollment in any program is governed by the enrollment agreement and the AGI policies provided by the office.</p>
<h2>Using the forms</h2><p>Please provide accurate information in our forms. Sending a form is a request; it does not by itself confirm a place, a booking or a payment.</p>
<h2>Content and marks</h2><p>Text and images on this site belong to AGI or are used with permission. Partner names, seals and logos belong to their respective institutions.</p>
<h2>Links</h2><p>Links to other websites are provided for convenience; we are not responsible for their content.</p>
<h2>Contact</h2><p>Questions about these terms: <a href="mailto:americanecoleagadir@gmail.com">americanecoleagadir@gmail.com</a>.</p>
</div></div></section>""", LEGAL_CSS)

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "audiences.py"), encoding="utf-8").read())

if __name__ == "__main__":
    for name, doc in PAGES.items():
        open(os.path.join(V2, name), "w", encoding="utf-8", newline="").write(doc)
    print("written:", ", ".join(PAGES))
