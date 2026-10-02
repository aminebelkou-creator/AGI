"""Convert the site's web images to WebP (smaller, same look). Run after images.ps1."""
import os
from PIL import Image
V2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
web = os.path.join(V2, "assets", "web"); before = after = 0
for f in sorted(os.listdir(web)):
    if not f.lower().endswith((".png", ".jpg", ".jpeg")): continue
    src = os.path.join(web, f); dst = os.path.splitext(src)[0] + ".webp"
    im = Image.open(src)
    im = im.convert("RGBA") if im.mode in ("P", "LA", "RGBA") else im.convert("RGB")
    if f.startswith("agi-seal"): im.thumbnail((440, 440), Image.LANCZOS)          # displayed at most ~380px
    im.save(dst, "WEBP", quality=82, method=6)
    before += os.path.getsize(src); after += os.path.getsize(dst)
    print(f"{f:34} {os.path.getsize(src)//1024:5} KB -> {os.path.getsize(dst)//1024:4} KB")
print(f"total {before//1024} KB -> {after//1024} KB")
