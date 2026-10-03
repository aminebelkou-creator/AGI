import json, re, os
inv = json.load(open(r"C:\Users\belko\AGI\data\crawl\inventory.json", encoding="utf-8"))
t = next(p for p in inv if "english-practice-test" in p["url"])["text"]
print("PLACEMENT TEST (first 2200 chars):\n", t[:2200])
print("\n... last 600 chars:\n", t[-600:])
raw = open(os.path.join(r"C:\Users\belko\AGI\data\crawl\agi", "english-practice-test.html"), encoding="utf-8", errors="ignore").read()
print("\nform elements:", len(re.findall(r"<input", raw)), "radios:", len(re.findall(r'type="radio"', raw)), "plugin hints:", set(re.findall(r'(wpforms|quiz|hdq|ays|watu|chained|forminator|qsm)', raw, re.I)))
e = next(p for p in inv if p["url"].rstrip("/").endswith("angliamorocco.org/exams"))["text"]
print("\nEXAMS PAGE:\n", e[:3000])
