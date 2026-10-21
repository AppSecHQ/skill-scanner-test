// Progressive enhancement for pre-rendered skill tables: sort, filter, search.
(function () {
  'use strict';

  function cellValue(row, idx, type) {
    var text = row.children[idx].textContent.trim();
    return type === 'num' ? (parseFloat(text) || 0) : text.toLowerCase();
  }

  document.querySelectorAll('table.sortable').forEach(function (table) {
    var headers = table.querySelectorAll('th[data-sort]');
    headers.forEach(function (th, idx) {
      th.addEventListener('click', function () {
        var type = th.dataset.type || 'str';
        var dir = th.classList.contains('sorted-asc') ? 'desc' : 'asc';
        headers.forEach(function (h) { h.classList.remove('sorted-asc', 'sorted-desc'); });
        th.classList.add('sorted-' + dir);
        var tbody = table.tBodies[0];
        var rows = Array.prototype.slice.call(tbody.rows);
        rows.sort(function (a, b) {
          var va = cellValue(a, idx, type), vb = cellValue(b, idx, type);
          if (va < vb) return dir === 'asc' ? -1 : 1;
          if (va > vb) return dir === 'asc' ? 1 : -1;
          return 0;
        });
        rows.forEach(function (r) { tbody.appendChild(r); });
      });
    });
  });

  var search = document.getElementById('skill-search');
  var sourceFilter = document.getElementById('source-filter');
  var verdictFilter = document.getElementById('verdict-filter');
  var rows = document.querySelectorAll('table.sortable tbody tr[data-name]');
  if (!rows.length) return;

  function applyFilters() {
    var q = search ? search.value.trim().toLowerCase() : '';
    var src = sourceFilter ? sourceFilter.value : '';
    var verdict = verdictFilter ? verdictFilter.value : '';
    rows.forEach(function (row) {
      var ok = true;
      if (q && row.dataset.name.indexOf(q) === -1) ok = false;
      if (src && row.dataset.source !== src) ok = false;
      if (verdict) {
        var isSafe = row.querySelector('.badge-safe') !== null;
        if (verdict === 'safe' && !isSafe) ok = false;
        if (verdict === 'issues' && isSafe) ok = false;
      }
      row.hidden = !ok;
    });
  }

  if (search) {
    var params = new URLSearchParams(location.search);
    if (params.get('q')) search.value = params.get('q');
    search.addEventListener('input', applyFilters);
  }
  if (sourceFilter) sourceFilter.addEventListener('change', applyFilters);
  if (verdictFilter) verdictFilter.addEventListener('change', applyFilters);
  applyFilters();
})();
