/* AGI v2 – shared behaviour: Programs dropdown and mobile menu. */
(function () {
  function closeAll(except) {
    document.querySelectorAll(".menu-btn[aria-expanded='true']").forEach(function (b) {
      if (b === except) return;
      b.setAttribute("aria-expanded", "false");
      var m = document.getElementById(b.getAttribute("aria-controls")); if (m) m.hidden = true;
    });
  }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".menu-btn, .burger");
    if (btn) {
      var open = btn.getAttribute("aria-expanded") === "true";
      if (btn.classList.contains("menu-btn")) closeAll(btn);
      btn.setAttribute("aria-expanded", String(!open));
      var target = document.getElementById(btn.getAttribute("aria-controls"));
      if (target) target.hidden = open;
      if (btn.classList.contains("burger")) btn.setAttribute("aria-label", open ? "Open menu" : "Close menu");
      return;
    }
    if (!e.target.closest(".submenu")) closeAll();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var open = document.querySelector(".menu-btn[aria-expanded='true']");
    closeAll(); if (open) open.focus();
  });
  document.addEventListener("focusin", function (e) {
    if (!e.target.closest(".has-menu")) closeAll();
  });
})();
