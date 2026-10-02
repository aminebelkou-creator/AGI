// <world-dots> — dotted world map drawn from real Natural Earth geometry (d3 + topojson).
// Expects d3 and topojson to be loaded by the host page (pinned tags in <helmet>).
(() => {
  const TOPO_URL = "https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json";
  let landPromise = null;

  function waitForLibs() {
    return new Promise((resolve) => {
      const tick = () => {
        if (window.d3 && window.topojson) resolve();
        else setTimeout(tick, 60);
      };
      tick();
    });
  }

  async function getLand() {
    if (!landPromise) {
      landPromise = (async () => {
        await waitForLibs();
        const topo = await window.d3.json(TOPO_URL);
        return window.topojson.merge(topo, topo.objects.countries.geometries);
      })();
    }
    return landPromise;
  }

  class WorldDots extends HTMLElement {
    connectedCallback() {
      if (this._init) return;
      this._init = true;
      Object.assign(this.style, { display: "block", position: "absolute", inset: "0", width: "100%", height: "100%" });
      this.canvas = document.createElement("canvas");
      Object.assign(this.canvas.style, { width: "100%", height: "100%", display: "block" });
      this.appendChild(this.canvas);
      this._ro = new ResizeObserver(() => this.schedule());
      this._ro.observe(this);
      this.render();
    }

    disconnectedCallback() {
      if (this._ro) this._ro.disconnect();
      clearTimeout(this._t);
    }

    schedule() {
      clearTimeout(this._t);
      this._t = setTimeout(() => this.render(), 120);
    }

    async render() {
      const land = await getLand();
      const d3 = window.d3;
      const rect = this.getBoundingClientRect();
      const w = Math.max(1, Math.round(rect.width));
      const h = Math.max(1, Math.round(rect.height));
      if (!w || !h) return;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      this.canvas.width = w * dpr;
      this.canvas.height = h * dpr;
      const ctx = this.canvas.getContext("2d");
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, w, h);

      const step = Number(this.getAttribute("step")) || 9;
      const radius = Number(this.getAttribute("dot-radius")) || 1.4;
      const color = this.getAttribute("color") || "91,155,224";
      const projection = d3.geoNaturalEarth1().fitSize([w, h], land);

      ctx.fillStyle = "rgba(" + color + ",1)";
      for (let y = step / 2; y < h; y += step) {
        for (let x = step / 2; x < w; x += step) {
          const inv = projection.invert([x, y]);
          if (!inv) continue;
          if (!d3.geoContains(land, inv)) continue;
          ctx.globalAlpha = 0.35 + Math.random() * 0.5;
          ctx.beginPath();
          ctx.arc(x, y, radius, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      ctx.globalAlpha = 1;
      this.dispatchEvent(new CustomEvent("worlddots:ready"));
    }
  }

  if (!customElements.get("world-dots")) customElements.define("world-dots", WorldDots);
})();
