"""Phase 0 – builds the initial fact register (v2/_build/facts.json) and claims register (v2/_build/claims.json).
facts.json is then maintained by hand: it is the single source of truth for fees, dates, contacts and numbers.
status: "source" = taken from the old sites, not yet confirmed · "confirmed" = confirmed by AGI · "to-confirm" = conflicting or missing."""
import os, json, re
ROOT = r"C:\Users\belko\AGI"; B = os.path.join(ROOT, "v2", "_build")
inv = json.load(open(os.path.join(ROOT, "data", "crawl", "inventory.json"), encoding="utf-8"))
def src(part): return next((p["url"] for p in inv if part in p["url"]), "")
def text(part): return next((p["text"] for p in inv if part in p["url"]), "")
A = "https://www.americangroup-international.com/"
F = lambda v, s, st="source", note="": {"value": v, "source": s, "status": st, **({"note": note} if note else {})}

facts = {
 "contact": {
  "address": F("Number 20, Rue Baalabek, Hay Nahda, Agadir 80000, Morocco", "julie-signature", "confirmed"),
  "phone_main": F("+212 528 843 349", "julie-signature", "confirmed"),
  "phone_arabic": F("+212 618 639 911", "julie-signature", "confirmed"),
  "whatsapp_english": F("+212 688 739 393", "julie-signature", "confirmed"),
  "email_official": F("americanecoleagadir@gmail.com", "julie-signature", "confirmed"),
  "email_admin_old": F("groupinternationala@gmail.com", A, "to-confirm", "Shown as 'Admin' on the old site header – still used?"),
  "email_anglia_julie": F("j.wilburn@angliamorocco.org", "https://angliamorocco.org/", "source"),
  "email_anglia_abdelhak": F("a.lam@angliamorocco.org", "https://angliamorocco.org/", "source"),
  "office_hours": F(None, "", "to-confirm", "Not on either site"),
 },
 "school": {
  "founded": F(2013, src("about-us"), "source", "angliamorocco.org says AGI is a brand since 2012"),
  "first_students": F(5, src("about-us"), "source"),
  "classrooms": F(8, src("for-a-better-education"), "source"),
  "nationalities": F("46+", src("for-a-better-education"), "to-confirm", "Old front page says 45+"),
  "status_wording": F("private correspondence school", src("front-page"), "to-confirm", "Legal description on old front page"),
  "eligibility": F("Aged 5 by September 1; under 21 on the first day", src("/enrollment"), "source"),
  "attendance_minimum": F("90%", src("attendance-policy"), "source"),
  "pass_mark": F("64% (D)", src("promotion-and-retention"), "source"),
  "service_hours": F("40 (10 per year)", src("volunteer-hours"), "source"),
  "school_hours": F(None, "", "to-confirm", "Not on either site"),
  "transport": F(None, "", "to-confirm"), "lunch": F(None, "", "to-confirm"), "sibling_discount": F(None, "", "to-confirm"),
  "uniform": F("No uniform mentioned; dress code in the handbook", src("handbook"), "to-confirm"),
 },
 "fees": {
  "tuition_monthly": F("2,600 MAD × 10 months", src("admission-fee"), "source"),
  "inscription": F({"K–Grade 1": "6,500 MAD", "Grades 2–6": "7,500 MAD", "Grades 7–8": "7,800 MAD", "Grades 9–11": "10,000 MAD", "Grade 12": "11,000 MAD"}, src("admission-fee"), "source", "Grade bands to verify against the page text in Phase 1"),
  "american_high_school_online": F("US$2,500 per year", src("admission-fee"), "source"),
  "summer_school_high_school": F("3,000 MAD for one month", src("admission-fee"), "source"),
  "included": F("Books, mathematics and Anglia exams, insurance (all-inclusive package)", src("admission-fee"), "source"),
  "anglia_saturday_classes": F("500 MAD a month, yearly exam included", src("pricing-and-details"), "source"),
  "anglia_one_to_one": F("200 MAD per session", src("pricing-and-details"), "source"),
  "anglia_small_group": F("150 MAD per person per session (2–3 students)", src("pricing-and-details"), "source"),
  "anglia_group_course": F("100 MAD a week, 1,200 MAD for 12 weeks (4–10 students)", src("pricing-and-details"), "source"),
  "anglia_level_test": F("Free", src("pricing-and-details"), "source"),
  "online_tutoring_usd": F("US$10 – US$50 per session (by length/package)", src("online-tutoring-session-prices"), "to-confirm", "Exact grid to transcribe in Phase 3; prices may be outdated"),
  "independent_modules": F("US$49.95 / US$79.95 per module; 20% discount mentioned", src("independent-course"), "to-confirm"),
  "proctoring": F("200 MAD (15 EUR) admin + 200 MAD (15 EUR) per exam hour", src("proctoring"), "source"),
  "usa_sponsorship": F("US$60", src("sponsorship"), "source"),
  "play_therapy": F("150 MAD per session", src("play-therapy"), "to-confirm"),
  "handbook_fees_mentions": F("150 DH, 20 DH (see handbook text)", src("handbook"), "to-confirm", "Identify what these fees are in Phase 1"),
 },
 "anglia": {
  "since": F(1993, "https://angliamorocco.org/exams/", "source"),
  "franchise_since": F(2021, src("about-us"), "source"),
  "regions": F(12, src("12-regions"), "source"),
  "open_representatives": F(["Oujda-Angad", "Fès", "Agadir-Ida Ou Tanane", "Taroudant"], src("12-regions"), "to-confirm"),
  "ucas": F("Mastery (C2) qualification carries UCAS tariff points", src("ucas"), "source"),
  "exam_durations": F("Reading & writing 1–3 h; listening 10–30 min; speaking 5–20 min", "https://angliamorocco.org/faq/", "source"),
  "min_age": F("About 4; no upper age limit", "https://angliamorocco.org/faq/", "source"),
 },
 "calendars": {
  "school_2026_27_source_text": F(text("school-calandar"), src("school-calandar"), "source", "Structure into dated events in Phase 1"),
  "saturday_classes_2025_26_source_text": F(text("saturday-classes-yearly-schedule"), src("saturday-classes-yearly-schedule"), "to-confirm", "2026–27 schedule needed"),
  "anglia_exam_dates_2026_source_text": F(text("anglia-exam-dates"), src("anglia-exam-dates"), "source"),
 },
 "people": {
  "julie_title": F("CEO & Educational Director · Anglia Examinations Morocco, American Group International of Agadir", "julie-signature", "confirmed"),
  "julie_other_titles": F(["Founder (ASCA 2026 post)", "Country Manager (angliamorocco.org)", "Director of Operations of AngliaMaroc (2022 post)", "Director of Global Operations (marketing draft)"], "various", "to-confirm"),
  "team_old_front_page": F(["Prof. Abdelhak Lam", "Prof. Latifa Amhari", "Prof. Mohamed Saih", "Mr. Rachid Oussalh"], src("front-page"), "to-confirm", "Julie asked to remove Rachid Oussalh"),
 },
}
claims = [
 {"id": 1, "claim": "Anglia is dependent on the UK Ministry of Education; recognised by the British Council; QCA accreditation; ASCENTIS support", "source": "https://angliamorocco.org/faq/", "decision": "Do not publish until Anglia confirms current wording", "status": "open"},
 {"id": 2, "claim": "Proficiency listed by UCAS", "source": "v2 english-anglia", "decision": "Replace with: Mastery (C2) carries UCAS tariff points", "status": "fix-now"},
 {"id": 3, "claim": "45+ vs 46+ nationalities", "source": "old front page vs school page", "decision": "Julie", "status": "open"},
 {"id": 4, "claim": "AGI is a private correspondence school", "source": "old front page", "decision": "Julie (legal status)", "status": "open"},
 {"id": 5, "claim": "Julie's titles (CEO, Country Manager, Director of Operations, Director of Global Operations, Founder)", "source": "various", "decision": "Julie", "status": "open"},
 {"id": 6, "claim": "Team: Latifa Amhari, Mohamed Saih, Rachid Oussalh", "source": "old front page", "decision": "Julie: current team and roles", "status": "open"},
 {"id": 7, "claim": "Three emails in use (official, admin, agiangliama)", "source": "old site header/menus", "decision": "Julie: one email per purpose", "status": "open"},
 {"id": 8, "claim": "Saturday schedule is for 2025–26", "source": "schedule page", "decision": "Get 2026–27 dates", "status": "open"},
 {"id": 9, "claim": "Limited homework vs homework policy minutes", "source": "K-12 vs policy", "decision": "Julie", "status": "open"},
 {"id": 10, "claim": "American Group USA LLC address in Grantsville (Maryland)", "source": "AGI USA page", "decision": "Confirm and publish", "status": "open"},
 {"id": 11, "claim": "Western Sahara political text on the Anglia network page", "source": "angliamorocco.org network", "decision": "Do not reproduce; list regions and provinces only", "status": "decided"},
 {"id": 12, "claim": "Old prices (online tutoring, modules, proctoring, play therapy) may be outdated", "source": "various", "decision": "Julie", "status": "open"},
]
fp = os.path.join(B, "facts.json")
if os.path.exists(fp): print("facts.json exists – not overwritten (edit by hand)")
else: json.dump(facts, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print("facts.json written")
json.dump(claims, open(os.path.join(B, "claims.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1); print("claims.json written")
n = sum(len(v) for v in facts.values()); tc = sum(1 for g in facts.values() for f in g.values() if f["status"] == "to-confirm")
print(f"facts: {n} in {len(facts)} groups · to confirm: {tc} · claims: {len(claims)} ({sum(c['status']=='open' for c in claims)} open)")
