/* RSA site — small progressive enhancements. The site works without JS. */
(function () {
  var doc = document.documentElement;
  doc.classList.add('js');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Mobile menu */
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.querySelector('.menu-btn__label').textContent = open ? btn.dataset.close : btn.dataset.open;
    });
  }

  /* Reveal on scroll */
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* Tabs (environment viewer) — WAI-ARIA tabs pattern */
  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(t, false); });
      t.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = tabs[(i + 1) % tabs.length];
        if (e.key === 'ArrowLeft') n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (e.key === 'Home') n = tabs[0];
        if (e.key === 'End') n = tabs[tabs.length - 1];
        if (n) { e.preventDefault(); select(n, true); }
      });
    });
  });

  /* Work filters */
  var filterBar = document.querySelector('[data-filters]');
  if (filterBar) {
    var buttons = filterBar.querySelectorAll('button');
    var cards = document.querySelectorAll('[data-kind]');
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.dataset.filter;
        buttons.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        cards.forEach(function (c) { c.classList.toggle('is-hidden', f !== 'all' && c.dataset.kind !== f); });
      });
    });
  }

  /* Cover sun: page scroll mapped to 06:00 → 18:00. Decorative, not data. */
  var sun = document.querySelector('[data-sun]');
  if (sun) {
    var path = sun.querySelector('.sun-path');
    var dot = sun.querySelector('.sun-dot');
    var ray = sun.querySelector('.sun-ray');
    var read = document.querySelector('[data-sun-time]');
    var len = path.getTotalLength();
    var ticking = false;
    function place() {
      ticking = false;
      var max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      var p = reduce ? 0.35 : Math.min(1, Math.max(0, window.scrollY / max));
      p = 0.06 + p * 0.88;
      var pt = path.getPointAtLength(len * p);
      dot.setAttribute('cx', pt.x); dot.setAttribute('cy', pt.y);
      if (ray) { ray.setAttribute('x2', pt.x); ray.setAttribute('y2', pt.y); }
      if (read) {
        var mins = Math.round(360 + p * 720);
        var h = Math.floor(mins / 60), m = mins % 60;
        read.textContent = (h < 10 ? '0' : '') + h + ':' + (m < 10 ? '0' : '') + m;
      }
    }
    place();
    if (!reduce) {
      window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(place); } }, { passive: true });
      window.addEventListener('resize', place);
    }
  }
})();

/* Copy-to-clipboard buttons (contact page) */
(function () {
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    var label = b.textContent;
    b.addEventListener('click', function () {
      var done = function () { b.textContent = b.dataset.done || 'Copied'; setTimeout(function () { b.textContent = label; }, 1800); };
      var select = function () {
        var el = document.querySelector('.contact__mail');
        if (!el || !window.getSelection) return;
        var r = document.createRange(); r.selectNodeContents(el);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(b.dataset.copy).then(done, select);
      } else { select(); }
    });
  });
})();
