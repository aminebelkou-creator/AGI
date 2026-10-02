"""Pre-launch check: lists everything still marked as a placeholder or unverified.

Run:  python _build/prelaunch.py
It exits with code 1 (NOT READY) while anything remains. Markers it looks for:
  data-placeholder="photo:..."        a photo slot without a real photo
  data-placeholder="testimonial:..."  a sample testimonial
  data-placeholder="team:..." / "fact:..."   assumed names or facts
  data-verify="..."                   content that must be checked (e.g. map location)
  # VERIFY:  comments in the build scripts (domain, share image)
plus the open items in LAUNCH-CHECKLIST.md (lines starting with "- [ ]").
"""
import os, re, sys
from collections import defaultdict
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
found = defaultdict(list)
for dp, _, fs in os.walk(V2):
    if any(x in dp for x in ("_legacy", "assets", ".git")): continue
    for f in fs:
        path = os.path.join(dp, f); rel = os.path.relpath(path, V2).replace(os.sep, "/")
        if f.endswith(".html") and not rel.startswith("_build"):
            s = open(path, encoding="utf-8").read()
            for kind, item in re.findall(r'data-placeholder="(\w+):([^"]+)"', s): found[kind].append((rel, item))
            for item in re.findall(r'data-verify="([^"]+)"', s): found["verify"].append((rel, item))
        elif f.endswith(".py") and rel.startswith("_build") and f != "prelaunch.py":
            for i, line in enumerate(open(path, encoding="utf-8"), 1):
                if "# VERIFY:" in line: found["config"].append((rel + f":{i}", line.split("# VERIFY:")[1].strip()))
check = os.path.join(V2, "LAUNCH-CHECKLIST.md")
open_items = [l.strip()[6:] for l in open(check, encoding="utf-8")] if os.path.exists(check) else []
open_items = [l for l in (x.strip() for x in open(check, encoding="utf-8")) if l.startswith("- [ ]")] if os.path.exists(check) else []

titles = {"photo": "Photos to supply", "testimonial": "Sample testimonials to replace", "team": "Team names to confirm",
          "fact": "Assumed facts on pages", "verify": "Items to verify", "config": "Site settings to confirm"}
total = 0
for kind in ("photo", "testimonial", "team", "fact", "verify", "config"):
    items = found.get(kind, [])
    if not items: continue
    uniq = sorted(set(items)); total += len(uniq)
    print(f"\n{titles[kind]} ({len(uniq)})")
    by = defaultdict(list)
    for where, item in uniq: by[item].append(where)
    for item, wheres in sorted(by.items()): print(f"  - {item}: {', '.join(sorted(set(wheres)))}")
print(f"\nChecklist items still open in LAUNCH-CHECKLIST.md: {len(open_items)}")
total += len(open_items)
print("\n" + ("READY FOR LAUNCH" if total == 0 else f"NOT READY: {total} open items"))
sys.exit(0 if total == 0 else 1)
