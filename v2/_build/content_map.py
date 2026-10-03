"""Phase 0 – content map: every source page of both sites -> v3 destination page, section, action, reason, phase.
Writes docs/content-map.csv. Rules are ordered; first match wins. Review the CSV by hand; edits there are authoritative."""
import os, re, json, csv
from collections import Counter
ROOT = r"C:\Users\belko\AGI"
pages = json.load(open(os.path.join(ROOT, "data", "crawl", "inventory.json"), encoding="utf-8"))

# (regex on url path + title, destination, section, action, phase, reason)
R = [
 # ---- decisions for pages no general rule covered (reviewed by hand)
 (r"/blog/?\s|/lates?t?-news/?\s|angliamorocco\.org/news/?\s|/programs(-2)?/?\s|/services-2/?\s|sch-dashboard", "-", "-", "drop", 0, "Menu, archive or internal page without content of its own"),
 (r"/lerninpods/", "programs/learning-pods.html", "Learning pods & fast track", "merge", 3, "Duplicate learning-pods page"),
 (r"for-a-better-education", "k12.html", "K–12 school", "merge", 1, "School presentation page"),
 (r"location-physical", "special-education.html", "Special education", "expand", 1, "Special education services page"),
 (r"importance-of-school-attendance", "policies/attendance.html", "Why attendance matters", "merge", 1, "Attendance explainer"),
 (r"rb-college", "pathways.html", "Partner universities", "merge", 3, "Partner institution"),
 (r"schedule-an-appointment", "forms.html", "Book a visit", "merge", 5, "Native visit form"),
 (r"educational-workshop-english-castle", "journal/educational-workshop-english-castle.html", "Journal · Event", "keep", 4, "Event page kept in the journal"),
 (r"new-online-examinations", "anglia/exams.html", "Online exams", "merge", 2, "Online exam option"),
 (r"club-anglia", "anglia/index.html", "Club Anglia (coming soon)", "merge", 2, "Planned club – confirm with Julie"),
 # fragments / archives / duplicates
 (r"floating|elementor|/recent-posts|/blog/?$|/news/?$|/category/|/author/|front-page-copy", "-", "-", "drop", 0, "Fragment, archive or duplicate of another page"),
 # legal
 (r"cookie", "cookies.html", "Cookies", "merge", 5, "One cookies notice for the whole site"),
 (r"privacy", "privacy.html", "Privacy", "merge", 5, "One privacy policy for both sites (legal review)"),
 (r"terms", "terms.html", "Terms", "merge", 5, "One terms page; old goods-sales terms not reused"),
 # Arabic pages of angliamorocco.org
 (r"/ar/", "ar/", "Arabic version", "translate", 7, "Basis for the Arabic version"),
 # fees & calendar
 (r"admission-fee|tuition", "fees.html", "Tuition & fees", "expand", 1, "Full fee table and inclusions"),
 (r"class-pricing|pricing-and-details", "fees.html", "Anglia class prices", "merge", 1, "Prices in one place, also shown on class pages"),
 (r"online-tutoring-session-prices", "online-tutoring.html", "Prices", "expand", 3, "American Group USA online tutoring"),
 (r"school-calandar|calendar|last-day-for-students", "calendar.html", "School year 2026–27", "expand", 1, "Every date and holiday"),
 (r"saturday-classes-yearly-schedule", "calendar.html", "Saturday classes", "expand", 1, "Week-by-week schedule"),
 (r"anglia-exam-dates", "calendar.html", "Anglia exam sessions", "expand", 1, "Exam sessions by month and level (also on exam pages)"),
 # admissions & policies
 (r"admissions-procedure|admission-prossess", "admissions.html", "How to apply", "expand", 1, "Full procedure"),
 (r"/enrollment", "admissions.html", "Enrollment documents", "expand", 1, "Age, residency, health documents"),
 (r"applyform|/apply", "forms.html", "Enrollment application", "merge", 1, "Native application form"),
 (r"provisional-placement", "policies/placement.html", "Provisional placement & assessment", "expand", 1, "Full policy"),
 (r"academic-school-handbook|handbook", "policies/handbook.html", "Academic handbook", "expand", 1, "Full handbook by chapter"),
 (r"attendance-policy", "policies/attendance.html", "Attendance", "expand", 1, "Full policy"),
 (r"promotion-and-retention", "policies/promotion-retention.html", "Promotion & retention", "expand", 1, "Full policy"),
 (r"parent-policy", "policies/parent-responsibility.html", "Parent responsibility", "expand", 1, "Full policy"),
 (r"refunds-and-complaints|policies-procedures", "policies/refunds-complaints.html", "Refunds & complaints", "expand", 1, "Full policy"),
 (r"media-policy", "policies/media.html", "Media", "expand", 1, "Full policy"),
 (r"homework-guidelines", "policies/homework.html", "Homework", "expand", 1, "Full guidelines"),
 (r"volunteer-hours", "policies/volunteer-hours.html", "Volunteer hours", "expand", 1, "Full rules"),
 (r"supplies-list", "school/supplies.html", "Supplies list", "expand", 1, "Full list"),
 (r"benchmarks-for-natives|cerf|/cefr", "anglia/cefr.html", "CEFR levels & AGI benchmarks", "expand", 2, "CEFR explained + K–12 benchmarks"),
 # Anglia Morocco
 (r"special-arrangements", "anglia/special-arrangements.html", "Special arrangements", "expand", 2, "Accessibility for candidates"),
 (r"practice-resources|audio", "anglia/practice.html", "Practice papers & audio", "expand", 2, "Packs per level"),
 (r"step-to-books|book-order|order-form", "anglia/books.html", "Step To books & order", "expand", 2, "Books and order form"),
 (r"english-practice-test|placement-test", "anglia/placement-test.html", "Free placement test", "expand", 2, "Interactive online test"),
 (r"business-examinations|business-english", "anglia/exams.html", "Business English exams", "merge", 2, "Exam suite page"),
 (r"accreditation-with-aim|ucas|mastery|30-years|online-exams", "anglia/about.html", "About Anglia Examinations", "merge", 2, "Recognition and history"),
 (r"angliamorocco\.org/exams|/anglia/?\s|anglia-examinations-of-england", "anglia/exams.html", "Levels & exams", "expand", 2, "All levels with descriptions"),
 (r"networks?-and-centers|12-regions|franchise|headquarters-of-angliamaroc", "anglia/network.html", "Network & centres", "expand", 2, "Regions, provinces, representatives"),
 (r"angliamorocco\.org/faq", "anglia/faq.html", "Anglia FAQ", "expand", 2, "Verified answers only (claims register)"),
 (r"angliamorocco\.org/?\s", "anglia/index.html", "Anglia Morocco home", "merge", 2, "Hub page of the Anglia Morocco section"),
 (r"angliamorocco\.org/.*(about|who)", "anglia/about.html", "About Anglia Morocco", "merge", 2, "History, team"),
 (r"cite|c-i-t-e|teacher-assistant-trainings|teachers-training", "teachers/cite.html", "C.I.T.E. / TESOL", "expand", 3, "Full teacher certification page"),
 (r"saturday|children-and-teens", "anglia/classes.html", "Saturday classes", "expand", 2, "Program and prep"),
 (r"one-on-one|efl-classes|library-facilities|conversation", "anglia/classes.html", "EFL classes", "expand", 2, "Class formats"),
 (r"math", "anglia/classes.html", "Mathematics in English", "expand", 2, "Math in English"),
 (r"learning-pod", "programs/learning-pods.html", "Learning pods & fast track", "expand", 3, "Pods of ten, teacherpreneurs"),
 # teachers
 (r"sponsorship", "teachers/usa-sponsorship.html", "USA private-school sponsorship", "expand", 3, "Process and fee"),
 (r"early-childhood", "teachers/ecec-diploma.html", "Early childhood education & care diploma", "expand", 3, "American Canadian Board diploma"),
 (r"teachers-database|stem-educators|4084-2", "teachers/careers.html", "Teach with AGI", "expand", 3, "Teachers database, workshops"),
 # adults & professionals
 (r"adult-high-school|etudes-secondaires", "adult-diploma.html", "Adult high school diploma", "expand", 3, "Full course list"),
 (r"independent-course", "programs/independent-studies.html", "Independent course studies", "expand", 3, "Modules and prices"),
 (r"medical", "professional.html", "Medical English", "expand", 3, "Medical EFL"),
 (r"corporate|business", "professional.html", "Business English", "expand", 3, "Corporate training"),
 (r"document-editing", "services/document-editing.html", "Document editing", "expand", 3, "Service and process"),
 (r"proctoring", "services/proctoring.html", "Proctoring", "expand", 3, "Exams, fees, conditions"),
 (r"attestation|document-request", "forms.html", "Document & attestation request", "merge", 5, "Native form"),
 (r"book-an-appointment", "forms.html", "Book a visit", "merge", 5, "Native form"),
 (r"/forms", "forms.html", "Forms", "merge", 5, "Native forms"),
 # wellbeing
 (r"adhd", "wellbeing/adhd-coaching.html", "ADHD holistic coaching", "expand", 3, "Service page"),
 (r"play-therapy", "wellbeing/play-therapy.html", "Holistic play therapy", "expand", 3, "Service page"),
 (r"i-heart|counsel", "wellbeing/index.html", "i-Heart therapeutic services", "expand", 3, "Wellbeing hub"),
 (r"special-education", "special-education.html", "Special education", "expand", 1, "Program page"),
 # online / AGI USA
 (r"how-long-should", "online-tutoring.html", "How long should a session last", "expand", 3, "Guide"),
 (r"zoom|teams-instructions|online-applications", "online-tutoring.html", "Joining online classes", "expand", 3, "Zoom/Teams instructions"),
 (r"american-group-international-usa|american-group-usa", "about/agi-usa.html", "American Group USA LLC", "expand", 3, "US entity"),
 # pathways
 (r"network-of-partners", "pathways.html", "Partner universities", "expand", 3, "Ten institutions"),
 (r"consultancy|university-agent|lane-community|leverage|chichester|ccgi", "pathways.html", "University pathways", "expand", 3, "Services and partners"),
 # resources
 (r"nursery-rhymes", "resources/nursery-rhymes.html", "Nursery rhymes for Pre-K", "expand", 4, "Resource"),
 (r"mcguffey|sight-words", "resources/mcguffey.html", "McGuffey readers & sight words", "expand", 4, "Resource (public domain)"),
 (r"self-help|helps|english-math-resources|dyslexia", "resources/index.html", "Resources", "expand", 4, "Resource hub"),
 # school & about
 (r"academic-english|american-group-international-school|micro-school|/school", "k12.html", "K–12 school", "expand", 1, "School overview & curriculum"),
 (r"student-life", "student-life.html", "Student life", "expand", 4, "Life at AGI"),
 (r"about-us|our-vision|mission", "about.html", "About", "expand", 5, "Story, mission, vision"),
 (r"partnerships", "partnerships.html", "Partnerships & franchise", "expand", 2, "Partnership routes"),
 (r"/contact", "contact.html", "Contact", "merge", 5, "Contact details"),
 (r"americangroup-international\.com/?\s", "index.html", "Home", "merge", 5, "Home page programs and team"),
]
def route(p):
    key = p["url"].lower() + " " + p["title"].lower()
    if p["kind"] in ("fragment", "archive"): return ("-", "-", "drop", 0, "Fragment or archive page")
    if p["kind"] == "post":
        slug = p["url"].rstrip("/").rsplit("/", 1)[-1]
        ev = re.search(r"graduat|congrat|celebrat|party|birthday|seamstress|award|spelling|workshop|castle|summer-school|holiday|fun-times|back-to-school|work-experience", key)
        return (f"journal/{slug}.html", "Journal" + (" · Event" if ev else ""), "keep", 4, "News post kept in the journal" + (" (event)" if ev else ""))
    for rx, dest, sec, act, ph, why in R:
        if re.search(rx, key): return (dest, sec, act, ph, why)
    return ("REVIEW", "-", "review", 0, "No rule matched – decide by hand")
rows = []
for p in pages:
    dest, sec, act, ph, why = route(p)
    rows.append({"site": p["site"], "language": p["lang"], "kind": p["kind"], "category": p["category"], "title": p["title"], "url": p["url"],
                 "words": p["words"], "thin": "yes" if p["thin"] else "", "current_status": p["status"], "destination": dest, "section": sec,
                 "action": act, "phase": ph, "reason": why, "facts": sum(len(v) for v in p["facts"].values())})
rows.sort(key=lambda r: (r["phase"], r["destination"], r["site"], r["title"]))
with open(os.path.join(ROOT, "docs", "content-map.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("sources:", len(rows), "| actions:", dict(Counter(r["action"] for r in rows)), "| by phase:", dict(sorted(Counter(r["phase"] for r in rows).items())))
print("destinations:", len({r["destination"] for r in rows if r["destination"] not in ("-", "REVIEW")}))
rev = [r for r in rows if r["action"] == "review"]
print(f"\nNEEDS REVIEW ({len(rev)}):"); [print(f"   {r['site']:6} {r['kind']:5} {r['category']:10} {r['title'][:60]:60} {r['url'][-60:]}") for r in rev]
print("\nDESTINATIONS (sources -> page):")
for d, n in Counter(r["destination"] for r in rows if r["action"] not in ("drop", "keep")).most_common(): print(f"   {n:2}  {d}")
