"""Mobile overflow check, one page at a time (headless Chrome at 520px – its minimum – with a probe that measures overflow).
python _build/mobile_probe.py -> data/mobile-probe.json"""
import os, json, subprocess, re, html as H
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
pages = [f for f in sorted(os.listdir(V2)) if f.endswith(".html") and not f.startswith("_")] + [f"{d}/{f}" for d in ("fr", "ar", "journal") if os.path.isdir(os.path.join(V2, d)) for f in sorted(os.listdir(os.path.join(V2, d))) if f.endswith(".html")]
PROBE = """<script>addEventListener("load",()=>setTimeout(()=>{const W=document.documentElement.clientWidth,S=document.documentElement.scrollWidth,b=[];
if(S>W+1)document.querySelectorAll("body *").forEach(e=>{const r=e.getBoundingClientRect();if((r.right>W+1||r.left<-1)&&r.width>0&&b.length<4&&getComputedStyle(e).position!=="fixed")b.push(e.tagName.toLowerCase()+(typeof e.className==="string"&&e.className?"."+e.className.split(" ")[0]:"")+" w="+Math.round(r.width))});
const p=document.createElement("pre");p.id="probe";p.textContent=JSON.stringify({W,S,b});document.body.appendChild(p)},300))</script></body>"""
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"; res = []
for pg in pages:
    src = os.path.join(V2, pg); tmp = os.path.join(os.path.dirname(src), "_probe_" + os.path.basename(pg))
    open(tmp, "w", encoding="utf-8").write(open(src, encoding="utf-8").read().replace("</body>", PROBE, 1))
    url = "http://127.0.0.1:8080/" + (os.path.dirname(pg) + "/" if "/" in pg else "") + "_probe_" + os.path.basename(pg)
    try:
        out = subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={os.environ['TEMP']}\\agi_probe_profile", "--window-size=520,900",
                              "--virtual-time-budget=2500", "--dump-dom", url], capture_output=True, text=True, encoding="utf-8", timeout=60).stdout
        m = re.search(r'<pre id="probe">(.*?)</pre>', out, re.S)
        r = json.loads(H.unescape(m.group(1))) if m else {"err": "no probe"}
    except Exception as e: r = {"err": str(e)}
    finally: os.remove(tmp)
    r["p"] = pg; res.append(r)
json.dump(res, open(os.path.join(ROOT, "data", "mobile-probe.json"), "w"), indent=1)
bad = [r for r in res if r.get("S", 0) > r.get("W", 0) + 1]; err = [r for r in res if "err" in r]
print(f"pages measured at phone width: {len(res) - len(err)} / {len(pages)} · horizontal overflow on {len(bad)} · errors {len(err)}")
for r in bad[:30]: print(f"   {r['p']:55} {r['S']}px > {r['W']}px  {r['b']}")
