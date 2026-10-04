"""Smoke test of a deployed preview: pages, redirects, 404, noindex.  python test_deploy.py https://agi-website-poc.edgeone.dev"""
import sys, urllib.request, urllib.error, ssl, csv, random, os
BASE = sys.argv[1].rstrip("/"); CTX = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 AGI-deploy-check"}
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
op = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=CTX))
def get(path, follow=False):
    req = urllib.request.Request(BASE + path, headers=UA)
    try:
        r = (urllib.request.urlopen(req, timeout=25, context=CTX) if follow else op.open(req, timeout=25))
        return r.status, dict(r.headers), r.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as e: return e.code, dict(e.headers), e.read().decode("utf-8", "ignore")
    except Exception as e: return "ERR " + type(e).__name__, {}, str(e)
ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    ok += cond; fail += (not cond); print(f"  {'PASS' if cond else 'FAIL'}  {name}  {detail}")
print("== pages")
for p, must in [("/", "American Group International"), ("/index.html", "Agadir"), ("/fees.html", "2,600"), ("/anglia.html", "Anglia"), ("/anglia-exams.html", "Masters"),
                ("/fr/index.html", "lang=\"fr\""), ("/ar/index.html", "dir=\"rtl\""), ("/journal.html", "Journal"), ("/forms.html", "forms"), ("/sitemap.xml", "<urlset")]:
    s, h, b = get(p, follow=True); check(p, s == 200 and must in b, f"status {s}")
print("== redirects (old WordPress addresses, via middleware)")
rows = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "redirects.csv"), encoding="utf-8-sig")))
sample = [r for r in rows if r["old_address"] in ("/cite/", "/admission-fee/", "/school-calandar/")] + random.Random(7).sample(rows, 7)
for r in sample:
    s, h, b = get(r["old_address"]); loc = h.get("Location") or h.get("location") or ""
    check(r["old_address"], s in (301, 308) and loc.endswith(r["new_page"]), f"{s} -> {loc[-45:]}")
print("== 404 page")
s, h, b = get("/this-page-does-not-exist-" + str(random.randint(1000, 9999)))
check("unknown address returns 404", s == 404, f"status {s}")
check("custom 404 page shown", "This page has moved" in b)
print("== preview protection")
s, h, b = get("/", follow=True)
xr = h.get("X-Robots-Tag") or h.get("x-robots-tag") or ""
check("X-Robots-Tag noindex header", "noindex" in xr.lower(), xr)
check("noindex meta in page", 'name="robots" content="noindex' in b)
s, h, b = get("/robots.txt", follow=True); check("robots.txt blocks crawlers", "Disallow: /" in b)
print(f"\n{ok} passed, {fail} failed")
