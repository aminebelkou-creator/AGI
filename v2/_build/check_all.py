"""Run every check in one go.   python _build/check_all.py          (all checks)
                                 python _build/check_all.py --ci     (no browser / network checks; used by GitHub Actions)
Exit code 1 if a blocking check fails. prelaunch.py is reported but never blocks (the site is NOT READY until Julie's answers are in)."""
import subprocess, sys, os, time, re
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CI = "--ci" in sys.argv
CHECKS = [  # (name, script, blocking, pass-test on output)
 ("Coverage gate (no fact lost)", "coverage_gate.py", True, lambda o: "FAIL" not in o),
 ("Internal links", "linkcheck.py", True, lambda o: int((re.search(r"broken: (\d+)", o) or [0, 99])[1]) <= 3),
 ("Page audit (titles, headings, alt)", "site_audit.py", False, lambda o: True),
 ("Site QA (facts, structure, buttons)", "qa_site.py", False, lambda o: True),
 ("Content quality", "content_quality.py", False, lambda o: True),
 ("Fact conflicts (prices)", "fact_conflicts.py", True, lambda o: "0 on current pages" in o),
 ("Privacy scan", "privacy_scan.py", False, lambda o: True),
 ("Launch readiness", "prelaunch.py", False, lambda o: "READY FOR LAUNCH" in o and "NOT READY" not in o),
]
if not CI:
    CHECKS += [("External links", "ext_linkcheck.py", True, lambda o: "BROKEN" not in o),
               ("Mobile layout (needs local server :8080)", "mobile_probe.py", True, lambda o: "horizontal overflow on 0" in o)]
env = dict(os.environ, PYTHONIOENCODING="utf-8"); fail = False; t0 = time.time()
print(f"{'check':42} {'result':8} summary")
for name, script, blocking, ok in CHECKS:
    r = subprocess.run([sys.executable, os.path.join(V2, "_build", script)], cwd=V2, capture_output=True, text=True, encoding="utf-8", env=env)
    out = (r.stdout or "") + (r.stderr or "")
    passed = ok(out) and (r.returncode == 0 or script in ("coverage_gate.py", "prelaunch.py", "linkcheck.py"))
    first = next((l.strip() for l in out.splitlines() if l.strip()), "")[:90]
    tag = "PASS" if passed else ("FAIL" if blocking else "info")
    if not passed and blocking: fail = True
    print(f"{name:42} {tag:8} {first}")
print(f"\\n{'ALL BLOCKING CHECKS PASS' if not fail else 'BLOCKING CHECK FAILED'} ({int(time.time() - t0)}s)")
sys.exit(1 if fail else 0)
