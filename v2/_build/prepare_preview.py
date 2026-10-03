"""Prepare a clean review copy of v2 for a Vercel preview: no build files, noindex, redirects, caching."""
import os, re, csv, json, shutil
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
OUT = os.path.join(ROOT, "deploy", "agi-preview")
EXCLUDE = {"_build", "_legacy", "LAUNCH-CHECKLIST.md", ".thumbnail", "support.js", "world-dots.js", "journal-posts.json", ".htaccess", "__pycache__"}
if os.path.exists(OUT): shutil.rmtree(OUT)
shutil.copytree(V2, OUT, ignore=lambda d, names: [n for n in names if n in EXCLUDE or n.startswith("_test")])

# preview must stay out of search engines
open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8", newline="\n").write("User-agent: *\nDisallow: /\n")

# redirects from the old WordPress addresses (only paths Vercel can match safely)
redirects, skipped, seen = [], 0, set()
with open(os.path.join(V2, "_build", "redirects.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        src = row["old_address"].strip().rstrip("/") or "/"
        dst = row["new_page"].strip()
        if src in ("", "/") or src in seen: continue
        if not re.fullmatch(r"/[A-Za-z0-9/_.\-]+", src): skipped += 1; continue
        seen.add(src); redirects.append({"source": src, "destination": dst, "permanent": True})

config = {
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "trailingSlash": False,
  "redirects": redirects,
  "headers": [
    {"source": "/(.*)", "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]},
    {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/(site\\.css|site\\.js)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]}
  ]
}
json.dump(config, open(os.path.join(OUT, "vercel.json"), "w", encoding="utf-8"), indent=2)
files = sum(len(fs) for _, _, fs in os.walk(OUT)); size = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(OUT) for f in fs)
print(f"review copy: {OUT}\nfiles: {files}  size: {size // 1024 // 1024} MB  redirects: {len(redirects)} (skipped {skipped} with special characters)")
