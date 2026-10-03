"""Screenshot sheet of every page (desktop + phone) for a quick human review.
python _build/shots_all.py  -> data/review/shots/*.png + data/review/index.html (open in a browser). Needs the local server on :8080."""
import os, subprocess, html, json, re, time
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(V2)
OUT = os.path.join(ROOT, "data", "review"); SH = os.path.join(OUT, "shots"); os.makedirs(SH, exist_ok=True)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE = os.path.join(os.environ["TEMP"], "agi_review_profile")
pages = [f for f in sorted(os.listdir(V2)) if f.endswith(".html")]
for d in ("fr", "ar", "journal"):
    if os.path.isdir(os.path.join(V2, d)): pages += [f"{d}/{f}" for f in sorted(os.listdir(os.path.join(V2, d))) if f.endswith(".html")]
def shot(url, out, size, scale):
    if os.path.exists(out): return
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run", f"--user-data-dir={PROFILE}",
                    f"--force-device-scale-factor={scale}", f"--window-size={size}", "--virtual-time-budget=3000", f"--screenshot={out}", url],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
t0 = time.time(); rows = []
for i, p in enumerate(pages, 1):
    key = p.replace("/", "__").replace(".html", "")
    title = (re.search(r"<title>(.*?)</title>", open(os.path.join(V2, p), encoding="utf-8").read(), re.S) or [None, p])[1]
    shot(f"http://127.0.0.1:8080/{p}", os.path.join(SH, f"{key}_desktop.png"), "1440,3200", "0.4")
    shot(f"http://127.0.0.1:8080/{p}", os.path.join(SH, f"{key}_phone.png"), "520,2000", "0.6")
    rows.append((p, html.unescape(title), key))
    if i % 20 == 0: print(f"{i}/{len(pages)} pages · {int(time.time() - t0)}s", flush=True)
groups = {}
for p, t, k in rows: groups.setdefault(p.split("/")[0] if "/" in p else "main", []).append((p, t, k))
cards = []
for g, L in groups.items():
    cards.append(f'<h2 id="{g}">{ {"main": "Main pages", "journal": "Journal", "fr": "Français", "ar": "العربية"}.get(g, g)} ({len(L)})</h2><div class="grid">')
    for p, t, k in L:
        cards.append(f'''<figure id="{k}"><figcaption><b>{html.escape(p)}</b><span>{html.escape(t)}</span>
<a href="https://agi-preview.vercel.app/{p}" target="_blank">live</a> · <label><input type="checkbox" data-k="{k}"> OK</label> · <input class="note" data-k="{k}" placeholder="note…"></figcaption>
<div class="pair"><a href="shots/{k}_desktop.png" target="_blank"><img loading="lazy" src="shots/{k}_desktop.png" alt="desktop"></a><a href="shots/{k}_phone.png" target="_blank"><img loading="lazy" src="shots/{k}_phone.png" alt="phone"></a></div></figure>''')
    cards.append("</div>")
doc = f"""<!doctype html><html lang="en"><meta charset="utf-8"><title>AGI – page review sheet</title>
<style>body{{font:14px/1.5 system-ui,sans-serif;margin:24px;background:#f6f5f1;color:#0a3161}}h1{{margin:0 0 4px}}h2{{margin:32px 0 12px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(520px,1fr));gap:18px}}figure{{margin:0;background:#fff;border:1px solid #ddd;padding:10px}}
figcaption{{font-size:12px;margin-bottom:8px}}figcaption span{{display:block;color:#5b6472}}.pair{{display:grid;grid-template-columns:2fr 1fr;gap:8px;align-items:start}}
.pair img{{width:100%;height:420px;object-fit:cover;object-position:top;border:1px solid #eee}}.note{{width:180px;font-size:12px}}figure.ok{{opacity:.45}}
#bar{{position:sticky;top:0;background:#f6f5f1;padding:8px 0;z-index:2}}</style>
<h1>AGI – page review sheet</h1><div id="bar">{len(rows)} pages · desktop + phone · tick OK or write a note (saved in this browser) · <button onclick="exportNotes()">Export notes</button> · {" · ".join(f'<a href="#{g}">{g}</a>' for g in groups)}</div>
{''.join(cards)}
<script>
const S=JSON.parse(localStorage.getItem("agi-review")||"{{}}");
document.querySelectorAll("[data-k]").forEach(el=>{{const k=el.dataset.k,s=S[k]||{{}};if(el.type==="checkbox"){{el.checked=!!s.ok;el.closest("figure").classList.toggle("ok",el.checked)}}else el.value=s.note||"";
el.addEventListener("input",()=>{{S[k]=S[k]||{{}};if(el.type==="checkbox"){{S[k].ok=el.checked;el.closest("figure").classList.toggle("ok",el.checked)}}else S[k].note=el.value;localStorage.setItem("agi-review",JSON.stringify(S))}})}});
function exportNotes(){{const t=Object.entries(S).filter(([k,v])=>v.note).map(([k,v])=>k.replace("__","/")+".html: "+v.note).join("\\n");navigator.clipboard.writeText(t);alert("Notes copied ("+t.split("\\n").filter(Boolean).length+")")}}
</script></html>"""
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(doc)
print(f"done: {len(rows)} pages, sheet at {os.path.join(OUT, 'index.html')} ({int(time.time() - t0)}s)")
