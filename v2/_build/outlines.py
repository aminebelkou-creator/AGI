import json, re, os
items = json.load(open(r"C:\Users\belko\AGI\data\crawl\inventory.json", encoding="utf-8"))
KEY = ["Admission Fees", "Academic School Calendar 2026-2027", "Last Day for Students", "Saturday Classes Yearly Schedule", "AGI Mission Statement and Academic Handbook",
       "Attendance Policy", "Media Policy", "Policies & Procedures", "Admissions Procedure", "Promotion and Retention", "Parent Policy", "Enrollment",
       "INDEPENDENT Course", "Adult High School Diploma Program", "Online Tutoring Session Prices", "Anglia Language Class Pricing", "Teacher Training Program for English",
       "AngliaMorocco English Test", "Network of Partners", "Holistic Play Therapy", "Early Childhood Education", "Anglia Learning Pods", "Learning Pod", "Front Page",
       "Exams", "CEFR", "ANGLIA EXAM DATES", "Special Arrangements", "FAQ", "AngliaMorocco Networks", "Practice Resources", "USA Private School Teacher", "Proctoring",
       "Document Editing", "Business Examinations", "EFL Classes", "STEM Educators", "Educational Workshop English Castle", "School Supplies", "Volunteer", "Homework"]
out = []
for k in KEY:
    for it in items:
        if k.lower() in it["title"].lower() and it["kind"] != "archive":
            heads = [l for l in it["text"].split("\n") if l.startswith("#")][:30]
            money = it["facts"].get("money", [])[:25]; dates = it["facts"].get("date", [])[:30]; nums = it["facts"].get("number", [])[:15]
            out.append(f"\n######## [{it['site']}/{it['lang']}] {it['title']} ({it['words']}w) {it['url']}\nHEADINGS: " + " || ".join(h.lstrip('# ').strip()[:70] for h in heads)
                       + (f"\nMONEY: {money}" if money else "") + (f"\nDATES: {dates}" if dates else "") + (f"\nNUMBERS: {nums}" if nums else ""))
            break
open(r"C:\Users\belko\AGI\data\crawl\key-outlines.txt", "w", encoding="utf-8").write("\n".join(out))
print(len(out), "outlines,", sum(len(x) for x in out), "chars")
