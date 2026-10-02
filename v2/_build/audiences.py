# Audience pages (parents, teachers, professionals, investors) and the founder's letter.
# Loaded by pages.py; uses its helpers: page, hero, cta, ph, testimonials, program_cards, program_page, buttons.
WA = '<a class="btn btn-ghost" href="https://wa.me/212688739393?text=Hello%20AGI%2C%20" target="_blank" rel="noopener">WhatsApp us</a>'
WA_LIGHT = '<a class="btn btn-light" href="https://wa.me/212688739393?text=Hello%20AGI%2C%20" target="_blank" rel="noopener">WhatsApp us</a>'
PH_TXT = lambda key, text: f'<span class="ph-text" data-placeholder="fact:{key}">{text}</span>'
FAQ_CSS = """
.faq details{border-bottom:1px solid var(--line);padding:4px 0}
.faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:20px;padding:18px 0;font-family:var(--serif);font-size:21px;color:var(--navy)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-family:var(--sans);font-size:22px;color:var(--red);line-height:1}
.faq details[open] summary::after{content:"–"}
.faq details p{margin:0 0 20px;color:var(--text);font-size:15.5px;line-height:1.75;max-width:70ch}
.promise{font-family:var(--serif);font-weight:300;font-size:clamp(28px,3.4vw,48px);line-height:1.2;margin:0 0 18px;max-width:22ch}
.letter{max-width:68ch;margin:0 auto;font-family:var(--serif);font-size:clamp(18px,1.4vw,21px);line-height:1.75;color:var(--text)}
.letter p{margin:0 0 1.2em}.letter .sign{margin-top:2em;font-family:var(--sans);font-size:14px;color:var(--grey)}.letter .sign b{display:block;font-family:var(--serif);font-size:24px;font-weight:400;color:var(--navy)}
"""

# ------------------------------------------------------------------ PARENTS
page("parents.html", "For parents – American Group International, Agadir",
 "An affordable, creative and inclusive American school in Agadir: small classes, support for every learner, and a placement policy that never lowers a grade because of language gaps.",
 hero("<span>For parents</span>", "An education built around your child.",
      "Affordable, creative and inclusive: a K–12 micro-school in Agadir where your child is known by name, supported where they need it, and prepared for a world without borders.",
      '<a class="btn btn-primary" href="forms.html#visit">Book a visit</a>' + WA)
 + f"""
<div class="wrap" style="padding-bottom:clamp(40px,5vw,72px)">{ph("parents-hero", "Parents and children arriving at school in the morning", "21/8")}</div>

<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>Is your child thriving – or just fitting in?</h2></div>
  <div class="prose">
    <p>Many families know the feeling: classrooms too crowded for a teacher to notice your child, grades that punish a child for still learning a language, and international schools with fees that are simply out of reach.</p>
    <p>AGI was created to change that. The school opened in 2013 with five children in a single room in Agadir. The idea was simple then and it is the same today: an American education should not be a privilege for a few families.</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>Affordable, creative and inclusive.</h2><p>Three words that guide every decision we make for your child.</p></div>
  <div class="cards">
    <div><span class="tag">Affordable</span><h3>Within reach of working families</h3><p>Tuition of 2,600 MAD a month over ten months, with books, mathematics and Anglia exams included. No hidden extras for the essentials.</p></div>
    <div><span class="tag">Creative</span><h3>Learning with imagination</h3><p>Small multi-grade classes, American pedagogy enriched by Montessori and Waldorf ideas, and room for critical thinking and independent research.</p></div>
    <div><span class="tag">Inclusive</span><h3>Every learner belongs</h3><p>Students of more than 46 nationalities, mainstream and special-needs learners side by side, with individual plans where they need them.</p></div>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap split">
  <div class="intro"><p class="kicker">Our placement promise</p><h2>No child is held back for a language gap.</h2></div>
  <div>
    <p class="quote" style="max-width:none">“Grade placement is not lowered due to missing documents, language gaps, or academic gaps.”</p>
    <p class="cite"><b>AGI Provisional Placement Policy</b>Every new student sits a free placement assessment</p>
    <p class="prose" style="margin-top:24px">Instead of moving your child down a year, we keep them with their age group and give targeted support: English as a second language, extra help in the subjects where they are behind, and regular reviews with you.</p>
  </div>
</div></section>

<section class="section bg-navy"><div class="wrap">
  <p class="kicker">Our motto</p>
  <p class="promise">School + Home + Community = Student Success</p>
  <p style="color:rgba(255,255,255,.75);max-width:60ch;margin:0">Children do best when the adults around them work together. You'll know your child's teachers, take part in their plan, and have an open door to the office. New students begin with a 90-day adjustment period so that you, your child and the school can settle in together.</p>
</div></section>

<section class="section"><div class="wrap split">
  <div class="intro"><h2>Caring for the whole child</h2><p>Academic progress depends on feeling safe and understood.</p></div>
  <dl class="rows">
    <div><dt>Individual plans</dt><dd>Individualized Education Plans for students who need them, built with you and, where needed, with your child's doctors and therapists. <a class="link" href="special-education.html">Special education</a></dd></div>
    <div><dt>Emotional wellbeing</dt><dd>AGI's founder, Julie Wilburn, is an accredited Holistic Therapeutic Coach, and the school is a member of the American School Counselor Association.</dd></div>
    <div><dt>Time for family</dt><dd>{PH_TXT('limited-homework', 'Limited homework, so children have time to bond with their families.')} Homework is planned by grade so that learning at home stays balanced. <a class="link" href="student-life.html">Homework guide</a></dd></div>
    <div><dt>English for life</dt><dd>Every grade is benchmarked on the CEFR and certified with Anglia Examinations of England. <a class="link" href="english-anglia.html">English &amp; Anglia</a></dd></div>
  </dl>
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Programs for your child</h2><p><a class="link" href="programs.html">All programs</a></p></div>
  <div class="cards">{"".join(f'<a class="card" href="{h}"><span class="tag">{t}</span><h3>{n}</h3><p>{d}</p><span class="more">Learn more</span></a>' for h, t, n, d in PROGRAM_CARDS if h in ("k12.html", "special-education.html", "english-anglia.html"))}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><h2>What parents say</h2></div>
  {testimonials()}
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Three steps to joining AGI</h2><p>Students are welcome at any stage of the year.</p></div>
  <div class="cards">
    <div><span class="num">01</span><h3>Reach out</h3><p>Send a message, call or WhatsApp us. We'll answer your questions and arrange a visit.</p></div>
    <div><span class="num">02</span><h3>Visit &amp; placement test</h3><p>Meet the team, see the classrooms, and let your child sit a free, friendly placement assessment.</p></div>
    <div><span class="num">03</span><h3>Enroll</h3><p>Pay the annual inscription and confirm the monthly plan. Registration days for 2026–27 are August 28 and 31.</p></div>
  </div>
  <p style="margin-top:22px"><a class="link" href="admissions.html">Admissions, fees &amp; calendar</a></p>
</div></section>

<section class="section"><div class="wrap split">
  <div class="intro"><h2>Questions parents ask</h2></div>
  <div class="faq">
    <details><summary>My child doesn't speak English yet. Can they join?</summary><p>Yes. Many of our students start with little English. They join their age group, receive ESL support, and are benchmarked with the Anglia levels as they progress.</p></details>
    <details><summary>Can my child join in the middle of the year?</summary><p>Yes. We welcome students at any stage. Your child sits the placement assessment and starts with the right support.</p></details>
    <details><summary>My child has special needs. How do you support them?</summary><p>We build an Individualized Education Plan with you. To put the right support in place we need documentation from a licensed practitioner, along with previous school records.</p></details>
    <details><summary>What does it cost?</summary><p>Tuition is 2,600 MAD a month over ten months, plus an annual inscription paid at enrollment. Books, mathematics and Anglia exams are included. <a href="admissions.html#fees">See tuition &amp; fees</a>.</p></details>
    <details><summary>What do we need to bring?</summary><p>Previous school records and a behavior report, proof of age and residency, and immunization and physical examination records.</p></details>
  </div>
</div></section>
""" + cta("Come and see the school.", "The best way to know AGI is to visit during the school day. Tours are arranged individually, Monday to Friday.",
           '<a class="btn btn-gold" href="forms.html#visit">Book a visit</a>' + WA_LIGHT), FAQ_CSS)

# ------------------------------------------------------------------ FOUNDER'S LETTER
page("founder-letter.html", "A letter from our founder – American Group International, Agadir",
 "Julie A. Wilburn, founder of American Group International, on why AGI started with five children in one room in Agadir, and what it promises families today.",
 hero('<a href="about.html">About</a> / <span>A letter from our founder</span>', "A letter from our founder.", "Julie A. Wilburn, on how AGI began and what it promises every family.")
 + f"""
<section class="section bg-white"><div class="wrap">
<article class="letter" data-placeholder="fact:founder-letter-approval">
  <p>Dear parents,</p>
  <p>When American Group International opened its doors in 2013, it was one room in Agadir and five children. We had a conviction more than a plan: that every child deserves an excellent education, and that an American education should not be reserved for the few families who can afford an international school.</p>
  <p>Having lived in Morocco for many years, I saw how often good families were shut out – by fees that were out of reach, or by systems that held children back because they learned differently or were still learning a language. So we built something else: a school that is <strong>affordable, creative and inclusive</strong>.</p>
  <p>At AGI, a child is never moved down a grade because of a language gap or a missing document. We welcome them, assess what they can do, and give them the support they need. As a Holistic Therapeutic Coach, I care as much about how our students feel as about what they learn, because children only thrive when they feel safe and valued.</p>
  <p>Since that first room, students of more than 46 nationalities have learned together with us. We outgrew our beginnings, moved to Hay Nahda, and in 2021 AGI became the Anglia Examinations franchise holder for Morocco, bringing internationally recognized English certification to students across the Kingdom.</p>
  <p>{PH_TXT('letter-expansion', 'Today we also serve families beyond Agadir – in other Moroccan cities, in Mauritania and in the United States.')}</p>
  <p>Our motto says what we believe: <em>School + Home + Community = Student Success</em>. Trusting a school with your child is trusting it with what matters most to you. We take that trust seriously, every day.</p>
  <p>I would be delighted to welcome you, show you our classrooms and introduce you to our team.</p>
  <p class="sign"><b>Julie A. Wilburn</b>Founder · CEO &amp; Educational Director, American Group International of Agadir · Anglia Examinations Morocco {PH_TXT('letter-title', '· Director of Global Operations')}</p>
</article>
</div></section>
""" + cta("Visit AGI.", "Meet Julie and the team, and see the school for yourself.", GOLD_APPLY + LIGHT_VISIT), FAQ_CSS)

# ------------------------------------------------------------------ TEACHERS
AM = "https://angliamorocco.org"
program_page("teachers.html", "For teachers", "For teachers – C.I.T.E. & teacher training",
 "Teach English with a lifelong credential: the Anglia C.I.T.E. (TESOL) certificate, teacher training in AGI classrooms, a 30-day internship and U.S. private-school sponsorship.",
 "Teach English with a lifelong credential.",
 "Earn the C.I.T.E. from Anglia Examinations England, practice in AGI classrooms, and open a path to teaching abroad – with support from Morocco's Anglia headquarters.", f"""
<section class="section bg-white" id="cite"><div class="wrap split">
  <div class="intro"><p class="kicker">Anglia Examinations England</p><h2>C.I.T.E. – Certificate for International Teachers of English</h2><p>A TESOL qualification that proves both your English and your ability to teach it.</p>
    <div class="btn-row" style="margin-top:20px"><a class="btn btn-primary" href="{AM}/citem/" target="_blank" rel="noopener">Register on angliamorocco.org</a></div></div>
  <dl class="rows">
    <div><dt>Lifelong</dt><dd>A qualification with no expiration date, recognized worldwide.</dd></div>
    <div><dt>Open to all</dt><dd>No entry qualifications are required. It suits current teachers who want to validate their skills and aspiring teachers starting out.</dd></div>
    <div><dt>Mapped to the CEFR</dt><dd>Your certificate shows your English level on the same European framework schools and employers use.</dd></div>
    <div><dt>Specializations</dt><dd>{PH_TXT("cite-tracks", "General English, Young Learners and Very Young Learners")}</dd></div>
  </dl>
</div></section>

<section class="section" id="internship"><div class="wrap">
  <div class="section-head"><h2>The 30-day teacher internship</h2><p>Learn by doing, in real AGI classrooms in Agadir.</p></div>
  <div class="cards" style="--cols:4">
    <div><span class="num">01</span><h3>Week 1</h3><p>Orientation to the school and its methods, and classroom observation.</p></div>
    <div><span class="num">02</span><h3>Week 2</h3><p>{PH_TXT("internship-week-2", "Co-teaching with a mentor teacher and lesson planning.")}</p></div>
    <div><span class="num">03</span><h3>Week 3</h3><p>{PH_TXT("internship-week-3", "Leading lessons with feedback, and assessment practice.")}</p></div>
    <div><span class="num">04</span><h3>Week 4</h3><p>Professional development workshops, a final survey and wrap-up.</p></div>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>More for educators</h2></div>
  <dl class="rows">
    <div id="sponsorship"><dt>USA teacher sponsorship</dt><dd>Certification sponsorship for teaching in U.S. private schools. Requires a bachelor's degree, a clear background check and a sponsoring school. Fee: US$60. Not valid for U.S. public schools.</dd></div>
    <div id="training"><dt>Teacher training program</dt><dd>English teachers test and train in AGI classrooms to strengthen their language and their teaching.</dd></div>
    <div id="tefl"><dt>TEFL / TESOL with Bridge</dt><dd>Accredited TEFL/TESOL courses through AGI's partnership with Bridge Education Group.</dd></div>
    <div id="courses"><dt>Independent course studies</dt><dd>Graduate-level, self-paced modules using books and journals; certificates approved by the American Canadian Board.</dd></div>
    <div id="pods"><dt>Teach a learning pod</dt><dd>Freelance teachers can lead Anglia learning pods: small groups of about ten students over ten weeks, with materials supplied.</dd></div>
  </dl>
</div></section>
""", "Start your next step as a teacher.", "Register for C.I.T.E. on angliamorocco.org, or ask us about the internship and sponsorship.",
 f'<a class="btn btn-gold" href="{AM}/citem/" target="_blank" rel="noopener">Register for C.I.T.E.</a><a class="btn btn-light" href="forms.html#enquiry/programs">Ask about the internship</a>')

# ------------------------------------------------------------------ PROFESSIONALS (replaces the old professional.html)
program_page("professional.html", "Professional & medical English", "English for professionals & clinicians",
 "Business and medical English in Agadir and online: Anglia Business English, courses for teams, medical English for clinicians, exam proctoring and ADHD coaching.",
 "Speak the language of your profession.",
 "Practical English for the way you work – in business, in medicine and across borders – certified with Anglia Examinations England.", """
<section class="section bg-white"><div class="wrap split">
  <div class="intro"><h2>English for work</h2><p>Start with a free level test; we'll recommend the right course and schedule.</p></div>
  <dl class="rows">
    <div id="business"><dt>Business English</dt><dd>Anglia International Business English, certified in four steps from A2+ to C1: meetings, presentations, emails and negotiation.</dd></div>
    <div id="medical"><dt>Medical English</dt><dd>For doctors, nurses and clinicians: patient communication, handovers, seminars and reading medical papers.</dd></div>
    <div id="teams"><dt>Courses for organizations</dt><dd>Group courses for your team, on site at your company or at AGI, with progress measured on the CEFR.</dd></div>
    <div id="one-to-one"><dt>One-to-one</dt><dd>Private sessions at 200 MAD each, at times that fit a working schedule. <a class="link" href="english-anglia.html#classes">All class prices</a></dd></div>
  </dl>
</div></section>
<section class="section"><div class="wrap split">
  <div class="intro"><h2>Professional services</h2></div>
  <dl class="rows">
    <div id="proctoring"><dt>Exam proctoring</dt><dd>Paper and online exams invigilated at AGI for distance learners of North American and British universities, companies and certification bodies. Monday to Thursday, 9:00–17:00. A 200 MAD (15 EUR) administration fee plus 200 MAD (15 EUR) per exam hour.</dd></div>
    <div id="adhd"><dt>ADHD holistic coaching</dt><dd>One-to-one coaching for children and adults on focus, organization and time management, in Agadir and online, with Julie Wilburn, an accredited Holistic Therapeutic Coach (IPHM, ICAHP).</dd></div>
    <div id="cite"><dt>For teachers</dt><dd>C.I.T.E. certification, teacher training and the 30-day internship have their own page. <a class="link" href="teachers.html">For teachers</a></dd></div>
  </dl>
</div></section>
""", "Find the right course.", "Book a free level test, or tell us what your team needs and we'll reply within one working day.",
 '<a class="btn btn-gold" href="forms.html#enquiry/anglia">Book a level test</a><a class="btn btn-light" href="forms.html#enquiry/programs">Request a team course</a>')

# ------------------------------------------------------------------ PARTNERS & INVESTORS
page("investors.html", "Partners & investors – American Group International, Agadir",
 "Grow with AGI: a K–12 micro-school, the Anglia Morocco examinations network across twelve regions, teacher certification and professional English programs.",
 hero('<a href="partnerships.html">Partnerships</a> / <span>Partners &amp; investors</span>', "Grow with AGI.",
      "Since 2013, AGI has grown from a single room in Agadir into a K–12 school, an English examinations network across Morocco's twelve regions, and programs for teachers and professionals. We welcome conversations with partners who share our mission.",
      '<a class="btn btn-primary" href="forms.html#enquiry/partnership">Request the partner brief</a><a class="btn btn-ghost" href="partnerships.html">Partnerships &amp; franchise</a>')
 + f"""
<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>One mission, five activities</h2><p>Affordable, creative and inclusive education, delivered through complementary programs.</p></div>
  <div class="cards">
    <div><span class="tag">Since 2013</span><h3>K–12 micro-school</h3><p>An American-curriculum school in Agadir: eight multi-grade classrooms and students of more than 46 nationalities.</p></div>
    <div><span class="tag">Since 2021</span><h3>Anglia Morocco</h3><p>Anglia Examinations franchise holder for Morocco, with a network of centers and representatives across the twelve regions.</p></div>
    <div><span class="tag">Educators</span><h3>Teacher certification</h3><p>C.I.T.E. (TESOL), teacher training, a 30-day internship and U.S. private-school sponsorship.</p></div>
    <div><span class="tag">Professionals</span><h3>Professional English &amp; services</h3><p>Business and medical English, team courses and exam proctoring.</p></div>
    <div><span class="tag">Pathways</span><h3>University placement</h3><p>An authorized admissions agent with partners including Chichester College Group and Leverage Edu.</p></div>
    <div><span class="tag">International</span><h3>American Group USA LLC</h3><p>AGI's U.S.-registered company {PH_TXT('usa-llc-state', '(Maryland)')}, offering programs and coaching to clients worldwide.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <div class="intro"><h2>Why the model works</h2></div>
  <dl class="rows">
    <div><dt>Built for working families</dt><dd>An international standard at an accessible price reaches families that traditional international schools do not. AGI has placed hundreds of students into the American educational system with low-cost programs.</dd></div>
    <div><dt>Recognized standards</dt><dd>Accredited by the American Council of Training and Development, recognized by four U.S. state departments of education, and official partner in Morocco of Chichester College Group, UK. <a class="link" href="about.html#accreditation">Accreditation</a></dd></div>
    <div><dt>A format that travels</dt><dd>Micro-schools and learning pods – small groups of about ten students – can open where demand is, without large campuses.</dd></div>
    <div><dt>Presence today</dt><dd>{PH_TXT("expansion", "Agadir headquarters; Anglia network across Morocco's twelve regions; [to confirm: other Moroccan cities, Mauritania, United States]")}</dd></div>
  </dl>
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="section-head"><h2>Ways to partner</h2></div>
  <div class="cards">
    <a class="card" href="partnerships.html"><h3>Open an AGI school or center</h3><p>Franchise and institutional partnerships for schools and language centers.</p><span class="more">Partnerships &amp; franchise</span></a>
    <a class="card" href="{AM}/angliamorocco-networks-and-centers-12-regions/" target="_blank" rel="noopener"><h3>Represent Anglia in your region</h3><p>Open representative positions in the Anglia Morocco network.</p><span class="more">See the network</span></a>
    <a class="card" href="forms.html#enquiry/partnership"><h3>Strategic partnership or investment</h3><p>Request the partner brief and a conversation with Julie Wilburn.</p><span class="more">Request the brief</span></a>
  </div>
</div></section>
""" + cta("Let's talk.", "Request the partner brief and we'll arrange a conversation.",
           '<a class="btn btn-gold" href="forms.html#enquiry/partnership">Request the partner brief</a><a class="btn btn-light" href="contact.html">Contact</a>'))
