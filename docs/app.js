/* ============================================================
   State
   ============================================================ */
let appData = { summary: null, scans: {}, notes: [] };

/* ============================================================
   Constants & Helpers
   ============================================================ */
const SEVERITY_ORDER = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO', 'SAFE'];

const SEVERITY_COLORS = {
  CRITICAL: 'var(--critical)',
  HIGH: 'var(--high)',
  MEDIUM: 'var(--medium)',
  LOW: 'var(--low)',
  INFO: 'var(--muted)',
  SAFE: 'var(--safe)'
};

function severityClass(severity) {
  return `badge-${severity.toLowerCase()}`;
}

function formatCategory(cat) {
  return cat.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

const SAFE_TAGS = new Set([
  'P','A','STRONG','EM','B','I','CODE','PRE','H1','H2','H3','H4','H5','H6',
  'UL','OL','LI','BLOCKQUOTE','TABLE','THEAD','TBODY','TR','TH','TD',
  'BR','HR','SPAN','DIV','SUP','SUB','DL','DT','DD'
]);
const SAFE_ATTRS = new Set(['href','target','rel']);

function sanitizeHtml(html) {
  const doc = new DOMParser().parseFromString(html, 'text/html');
  (function clean(node) {
    for (const child of [...node.childNodes]) {
      if (child.nodeType === 3) continue;
      if (child.nodeType !== 1) { child.remove(); continue; }
      if (!SAFE_TAGS.has(child.tagName)) {
        while (child.firstChild) node.insertBefore(child.firstChild, child);
        child.remove();
        continue;
      }
      for (const attr of [...child.attributes]) {
        if (!SAFE_ATTRS.has(attr.name)) child.removeAttribute(attr.name);
      }
      if (child.hasAttribute('href')) {
        const href = child.getAttribute('href').trim().toLowerCase();
        if (href.startsWith('javascript:') || href.startsWith('data:')) {
          child.removeAttribute('href');
        }
      }
      if (child.tagName === 'A' && !child.hasAttribute('rel')) {
        child.setAttribute('rel', 'noopener');
      }
      clean(child);
    }
  })(doc.body);
  return doc.body.innerHTML;
}

/* ============================================================
   Router
   ============================================================ */
function router() {
  const hash = location.hash || '#/';
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));

  if (hash.startsWith('#/skill/')) {
    const name = decodeURIComponent(hash.replace('#/skill/', ''));
    document.getElementById('skill-detail').classList.add('active');
    renderSkillDetail(name);
  } else if (hash.startsWith('#/note/')) {
    const id = decodeURIComponent(hash.replace('#/note/', ''));
    document.getElementById('note-detail').classList.add('active');
    renderNoteDetail(id);
  } else if (hash === '#/notes') {
    document.getElementById('notes-list').classList.add('active');
    renderNotesList();
  } else if (hash === '#/dashboard') {
    document.getElementById('dashboard').classList.add('active');
    renderDashboard();
  } else {
    document.getElementById('skills-table').classList.add('active');
    renderSkillsTable();
  }

  document.querySelectorAll('nav a').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === hash);
  });
}

/* ============================================================
   Data Loading
   ============================================================ */
async function loadData() {
  try {
    const summaryRes = await fetch('data/summary.json');
    appData.summary = await summaryRes.json();

    // Load individual scan files listed in summary
    if (appData.summary.skills) {
      const loads = appData.summary.skills.map(async (skill) => {
        // Derive slug from scan_file to handle names with spaces or odd casing
        const slug = skill.scan_file.replace('-scan.md', '');
        skill.slug = slug;
        try {
          const res = await fetch(`data/scans/${slug}-scan.json`);
          if (res.ok) {
            appData.scans[slug] = await res.json();
          } else {
            console.warn(`Failed to load scan for ${slug}: ${res.status}`);
          }
        } catch (e) {
          console.warn(`Failed to load scan for ${slug}`, e);
        }
      });
      await Promise.all(loads);
    }
    // Load notes
    try {
      const notesRes = await fetch('notes.json');
      if (notesRes.ok) {
        appData.notes = await notesRes.json();
      }
    } catch (e) {
      console.warn('Failed to load notes:', e);
    }
  } catch (e) {
    console.error('Failed to load data:', e);
  }
}

/* ============================================================
   Render: Dashboard
   ============================================================ */
function renderDashboard() {
  if (!appData.summary) return;

  const summary = appData.summary;

  // --- Stat cards (update text only, don't replace HTML) ---
  document.getElementById('stat-total-skills').textContent = summary.total_skills;
  document.getElementById('stat-total-findings').textContent = summary.total_findings;
  document.getElementById('stat-critical').textContent = summary.severity_counts.CRITICAL;
  document.getElementById('stat-high').textContent = summary.severity_counts.HIGH;
  document.getElementById('stat-medium').textContent = summary.severity_counts.MEDIUM;
  document.getElementById('stat-low').textContent = summary.severity_counts.LOW;

  // --- Scan metadata (tool + model) ---
  const existingMeta = document.querySelector('#dashboard .scan-meta');
  if (existingMeta) existingMeta.remove();

  // Extract LLM model from any scan that has LLM findings
  let llmModel = 'N/A';
  for (const slug in appData.scans) {
    const scan = appData.scans[slug];
    if (scan && scan.findings) {
      const f = scan.findings.find(f => f.analyzer === 'llm' && f.metadata && f.metadata.model);
      if (f) { llmModel = f.metadata.model; break; }
    }
  }

  const analyzers = summary.analyzers_used || [];
  const metaDiv = document.createElement('div');
  metaDiv.className = 'scan-meta';
  metaDiv.innerHTML = `<span>Scanner: <strong>cisco-ai-skill-scanner</strong></span>` +
    `<span>LLM Model: <strong style="font-family:var(--font-mono);font-size:0.8125rem;">${escapeHtml(llmModel)}</strong></span>` +
    `<span>Analyzers: ${analyzers.map(a => `<span class="analyzer-pill" style="font-size:0.7rem;padding:0.1rem 0.4rem;border-radius:9999px;background-color:rgba(99,102,241,0.08);color:var(--muted);border:1px solid var(--border);">${escapeHtml(a)}</span>`).join(' ')}</span>`;

  // Insert after first stats-bar
  const firstStatsBar = document.querySelector('#dashboard .stats-bar');
  if (firstStatsBar) {
    firstStatsBar.parentNode.insertBefore(metaDiv, firstStatsBar.nextSibling);
  }

  // --- Severity Breakdown (stacked bar) ---
  const severityPanel = document.getElementById('severity-breakdown');
  const total = summary.total_findings || 1; // avoid division by zero
  const sevEntries = SEVERITY_ORDER.filter(s => (summary.severity_counts[s] || 0) > 0);

  let barHtml = '<div class="severity-bar" style="display:flex;height:2rem;border-radius:6px;overflow:hidden;margin-bottom:1rem;">';
  sevEntries.forEach(sev => {
    const count = summary.severity_counts[sev] || 0;
    const pct = ((count / total) * 100).toFixed(1);
    barHtml += `<div class="severity-bar-segment" style="width:${pct}%;background-color:${SEVERITY_COLORS[sev]};min-width:${count > 0 ? '2px' : '0'};transition:width 0.3s ease;" title="${sev}: ${count}"></div>`;
  });
  barHtml += '</div>';

  barHtml += '<div class="bar-legend" style="display:flex;flex-wrap:wrap;gap:1rem;">';
  SEVERITY_ORDER.forEach(sev => {
    const count = summary.severity_counts[sev] || 0;
    barHtml += `<span style="display:flex;align-items:center;gap:0.375rem;font-size:0.8125rem;">
      <span style="width:10px;height:10px;border-radius:50%;background-color:${SEVERITY_COLORS[sev]};display:inline-block;"></span>
      ${sev} <strong>${count}</strong>
    </span>`;
  });
  barHtml += '</div>';

  severityPanel.innerHTML = barHtml;

  // --- Findings by Category (horizontal bar chart) ---
  const catPanel = document.getElementById('findings-by-category');
  const cats = summary.findings_by_category;
  const catEntries = Object.entries(cats).sort((a, b) => b[1] - a[1]);
  const maxCat = catEntries.length > 0 ? catEntries[0][1] : 1;

  let catHtml = '';
  catEntries.forEach(([cat, count]) => {
    const pct = ((count / maxCat) * 100).toFixed(1);
    catHtml += `<div class="category-bar-row" style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.625rem;">
      <span style="min-width:10rem;font-size:0.8125rem;text-align:right;color:var(--muted);">${formatCategory(cat)}</span>
      <div style="flex:1;background-color:var(--border);border-radius:4px;height:1.25rem;overflow:hidden;">
        <div class="category-bar-fill" style="width:${pct}%;height:100%;background-color:var(--accent);border-radius:4px;transition:width 0.3s ease;"></div>
      </div>
      <span style="min-width:2rem;font-size:0.8125rem;font-weight:600;">${count}</span>
    </div>`;
  });

  catPanel.innerHTML = catHtml;

  // --- Top Risks (append after dashboard-grid) ---
  const dashboard = document.getElementById('dashboard');

  // Remove any previously rendered top-risks section to avoid duplicates
  const existingRisks = dashboard.querySelector('.top-risks');
  if (existingRisks) existingRisks.remove();

  if (summary.top_risks && summary.top_risks.length > 0) {
    const risksSection = document.createElement('div');
    risksSection.className = 'top-risks';
    risksSection.style.marginTop = '1.5rem';

    let risksHtml = '<h2>Top Risks</h2>';
    summary.top_risks.forEach(risk => {
      const sev = risk.severity;
      risksHtml += `<div class="risk-card" style="background-color:var(--surface);border:1px solid var(--border);border-left:4px solid;border-left-color:${SEVERITY_COLORS[sev] || 'var(--muted)'};border-radius:8px;padding:1rem 1.25rem;margin-bottom:0.75rem;">
        <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;margin-bottom:0.5rem;">
          <span class="badge ${severityClass(sev)}">${sev}</span>
          <strong style="font-size:0.875rem;">${escapeHtml(risk.skill)}</strong>
          <span class="badge badge-category" style="background-color:rgba(99,102,241,0.12);color:var(--accent);border:1px solid rgba(99,102,241,0.25);">${formatCategory(risk.category)}</span>
        </div>
        <p style="font-size:0.8125rem;color:var(--muted);line-height:1.5;margin:0;">${escapeHtml(risk.description)}</p>
      </div>`;
    });

    risksSection.innerHTML = risksHtml;
    dashboard.appendChild(risksSection);
  }
}

/* ============================================================
   Render: Skills Table
   ============================================================ */
let currentSort = { column: null, asc: true };

function renderSkillsTable() {
  if (!appData.summary) return;

  const skills = appData.summary.skills;

  // --- Populate source filter dropdown ---
  const sourceFilter = document.getElementById('source-filter');
  const sources = [...new Set(skills.map(s => s.source))].sort();
  // Keep the first "All Sources" option, clear any previously added options
  sourceFilter.innerHTML = '<option value="">All Sources</option>';
  sources.forEach(src => {
    sourceFilter.innerHTML += `<option value="${escapeHtml(src)}">${escapeHtml(src)}</option>`;
  });

  // --- Build table body ---
  const tbody = document.querySelector('#skills-list tbody');
  renderTableRows(skills, tbody);

  // --- Event listeners (remove old ones by cloning) ---
  const searchInput = document.getElementById('skill-search');
  const newSearch = searchInput.cloneNode(true);
  searchInput.parentNode.replaceChild(newSearch, searchInput);
  newSearch.addEventListener('input', filterTable);

  const newFilter = sourceFilter.cloneNode(true);
  sourceFilter.parentNode.replaceChild(newFilter, sourceFilter);
  newFilter.addEventListener('change', filterTable);

  // --- Sorting on table headers ---
  document.querySelectorAll('#skills-list thead th[data-sort]').forEach(th => {
    const newTh = th.cloneNode(true);
    th.parentNode.replaceChild(newTh, th);
    newTh.addEventListener('click', () => {
      const col = newTh.getAttribute('data-sort');
      if (currentSort.column === col) {
        currentSort.asc = !currentSort.asc;
      } else {
        currentSort.column = col;
        currentSort.asc = true;
      }

      // Update header classes
      document.querySelectorAll('#skills-list thead th').forEach(h => {
        h.classList.remove('sort-asc', 'sort-desc');
      });
      newTh.classList.add(currentSort.asc ? 'sort-asc' : 'sort-desc');

      sortTable();
    });
  });
}

function renderTableRows(skills, tbody) {
  let html = '';
  skills.forEach(skill => {
    const slug = skill.slug;
    const scan = appData.scans[slug];

    // Count findings by severity from scan data
    const sevCounts = {};
    SEVERITY_ORDER.forEach(s => { sevCounts[s] = 0; });
    if (scan && scan.findings) {
      scan.findings.forEach(f => {
        if (sevCounts[f.severity] !== undefined) {
          sevCounts[f.severity]++;
        }
      });
    }

    const hasScan = !!scan;
    const maxSev = skill.max_severity || 'SAFE';

    html += `<tr data-name="${escapeHtml(skill.name.toLowerCase())}" data-source="${escapeHtml(skill.source)}">
      <td>
        <a href="#/skill/${encodeURIComponent(slug)}" style="color:var(--accent-light);text-decoration:none;font-weight:500;">${escapeHtml(skill.name)}</a>
        <span class="badge ${severityClass(maxSev)}">${maxSev === 'SAFE' ? 'SAFE' : maxSev}</span>
      </td>
      <td style="color:var(--muted);">${escapeHtml(skill.source)}</td>
      <td style="font-weight:${skill.findings_count > 0 ? '700' : '400'};">${skill.findings_count}</td>
      <td${hasScan && sevCounts.CRITICAL > 0 ? ` style="color:var(--critical);font-weight:600;"` : ''}>${hasScan ? sevCounts.CRITICAL : '--'}</td>
      <td${hasScan && sevCounts.HIGH > 0 ? ` style="color:var(--high);font-weight:600;"` : ''}>${hasScan ? sevCounts.HIGH : '--'}</td>
      <td${hasScan && sevCounts.MEDIUM > 0 ? ` style="color:var(--medium);font-weight:600;"` : ''}>${hasScan ? sevCounts.MEDIUM : '--'}</td>
      <td${hasScan && sevCounts.LOW > 0 ? ` style="color:var(--low);font-weight:600;"` : ''}>${hasScan ? sevCounts.LOW : '--'}</td>
    </tr>`;
  });

  tbody.innerHTML = html;
}

function filterTable() {
  const searchTerm = document.getElementById('skill-search').value.toLowerCase();
  const sourceValue = document.getElementById('source-filter').value;

  document.querySelectorAll('#skills-list tbody tr').forEach(row => {
    const name = row.getAttribute('data-name') || '';
    const source = row.getAttribute('data-source') || '';
    const matchesSearch = name.includes(searchTerm);
    const matchesSource = !sourceValue || source === sourceValue;
    row.style.display = (matchesSearch && matchesSource) ? '' : 'none';
  });
}

function sortTable() {
  const tbody = document.querySelector('#skills-list tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  const col = currentSort.column;

  const colIndex = {
    name: 0,
    source: 1,
    findings: 2,
    critical: 3,
    high: 4,
    medium: 5,
    low: 6
  };
  const idx = colIndex[col];
  if (idx === undefined) return;

  rows.sort((a, b) => {
    let aVal = a.cells[idx].textContent.trim();
    let bVal = b.cells[idx].textContent.trim();

    // Numeric sort for findings/severity columns
    if (idx >= 2) {
      aVal = aVal === '--' ? -1 : parseInt(aVal, 10);
      bVal = bVal === '--' ? -1 : parseInt(bVal, 10);
      return currentSort.asc ? aVal - bVal : bVal - aVal;
    }

    // String sort for name/source
    aVal = aVal.toLowerCase();
    bVal = bVal.toLowerCase();
    if (aVal < bVal) return currentSort.asc ? -1 : 1;
    if (aVal > bVal) return currentSort.asc ? 1 : -1;
    return 0;
  });

  rows.forEach(row => tbody.appendChild(row));
}

/* ============================================================
   Render: Skill Detail
   ============================================================ */
function renderSkillDetail(name) {
  const scan = appData.scans[name];
  const skillSummary = appData.summary
    ? appData.summary.skills.find(s => s.slug === name)
    : null;

  // --- Breadcrumb ---
  const breadcrumbEl = document.getElementById('detail-breadcrumb-name');
  breadcrumbEl.textContent = scan ? scan.skill_name : (skillSummary ? skillSummary.name : name);

  // --- No data guard ---
  if (!scan && !skillSummary) {
    document.getElementById('detail-metadata').innerHTML =
      `<p class="muted">No scan data found for "${escapeHtml(name)}"</p>`;
    document.getElementById('detail-findings-list').innerHTML =
      '<li class="muted">No data available.</li>';
    return;
  }

  // --- Metadata ---
  const metaEl = document.getElementById('detail-metadata');
  const displayName = scan ? scan.skill_name : skillSummary.name;
  const source = skillSummary ? skillSummary.source : '--';
  const isSafe = scan ? scan.is_safe : (skillSummary ? skillSummary.is_safe : true);
  const maxSev = scan ? scan.max_severity : (skillSummary ? skillSummary.max_severity : 'SAFE');
  const analyzers = scan ? (scan.analyzers_used || []) : (skillSummary ? (skillSummary.analyzers || []) : []);
  const duration = scan && scan.scan_duration_seconds != null ? scan.scan_duration_seconds.toFixed(1) + 's' : '--';
  const timestamp = scan && scan.timestamp ? new Date(scan.timestamp).toLocaleString() : '--';

  // Extract LLM model: check this skill's findings first, then fall back to any scan globally
  const hasLlmAnalyzer = analyzers.some(a => a === 'llm_analyzer');
  let llmModel = 'N/A (static only)';
  if (hasLlmAnalyzer) {
    const llmFinding = scan && scan.findings ? scan.findings.find(f => f.analyzer === 'llm' && f.metadata && f.metadata.model) : null;
    if (llmFinding) {
      llmModel = llmFinding.metadata.model;
    } else {
      // LLM analyzer ran but produced no findings with model -- check other scans
      for (const slug in appData.scans) {
        const s = appData.scans[slug];
        if (s && s.findings) {
          const f = s.findings.find(f => f.analyzer === 'llm' && f.metadata && f.metadata.model);
          if (f) { llmModel = f.metadata.model; break; }
        }
      }
    }
  }

  metaEl.innerHTML = `<div class="metadata-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(14rem,1fr));gap:1rem;">
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Skill Name</div>
      <div style="font-weight:600;">${skillSummary && skillSummary.repo_url ? `<a href="${escapeHtml(skillSummary.repo_url)}" target="_blank" rel="noopener" style="color:var(--accent);text-decoration:none;">${escapeHtml(displayName)} &#x2197;</a>` : escapeHtml(displayName)}</div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Source</div>
      <div>${escapeHtml(source)}</div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Status</div>
      <div><span class="badge ${isSafe ? 'badge-safe' : 'badge-critical'}">${isSafe ? 'Safe' : 'Unsafe'}</span></div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Max Severity</div>
      <div><span class="badge ${severityClass(maxSev)}">${maxSev}</span></div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Analyzers</div>
      <div style="display:flex;flex-wrap:wrap;gap:0.375rem;">${analyzers.map(a =>
        `<span class="analyzer-pill" style="font-size:0.75rem;padding:0.125rem 0.5rem;border-radius:9999px;background-color:rgba(99,102,241,0.12);color:var(--accent);border:1px solid rgba(99,102,241,0.25);">${escapeHtml(a)}</span>`
      ).join('')}</div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Scan Duration</div>
      <div>${duration}</div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Timestamp</div>
      <div>${timestamp}</div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">Scanner</div>
      <div>cisco-ai-skill-scanner</div>
    </div>
    <div>
      <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.04em;color:var(--muted);margin-bottom:0.25rem;">LLM Model</div>
      <div style="font-family:var(--font-mono);font-size:0.8125rem;">${escapeHtml(llmModel)}</div>
    </div>
  </div>`;

  // --- Findings ---
  const findingsList = document.getElementById('detail-findings-list');

  if (!scan || !scan.findings || scan.findings.length === 0) {
    findingsList.innerHTML = `<li style="text-align:center;padding:2rem;">
      <span class="badge badge-safe">SAFE</span>
      <p style="margin-top:0.75rem;color:var(--muted);">No findings -- this skill passed all security checks.</p>
    </li>`;
    return;
  }

  // Sort findings by severity (CRITICAL first)
  const sortedFindings = [...scan.findings].sort((a, b) => {
    return SEVERITY_ORDER.indexOf(a.severity) - SEVERITY_ORDER.indexOf(b.severity);
  });

  let findingsHtml = '';
  sortedFindings.forEach(f => {
    const sev = f.severity;
    const fileLine = f.file_path
      ? `<p class="finding-file" style="font-size:0.8125rem;color:var(--muted);margin:0.5rem 0;">&#x1f4c4; ${escapeHtml(f.file_path)}${f.line_number ? ':' + f.line_number : ''}</p>`
      : '';
    const snippet = f.snippet
      ? `<div class="finding-snippet" style="margin:0.75rem 0;"><pre style="background-color:var(--bg);border:1px solid var(--border);border-radius:6px;padding:0.75rem;overflow-x:auto;font-family:var(--font-mono);font-size:0.8125rem;line-height:1.5;"><code>${escapeHtml(f.snippet)}</code></pre></div>`
      : '';
    const remediation = f.remediation
      ? `<div class="finding-remediation" style="font-size:0.8125rem;margin-top:0.75rem;padding:0.75rem;background-color:rgba(34,197,94,0.06);border-radius:6px;border:1px solid rgba(34,197,94,0.15);"><strong>Remediation:</strong> ${escapeHtml(f.remediation)}</div>`
      : '';

    findingsHtml += `<li style="padding:0;">
      <details class="finding-card" style="border-left:4px solid ${SEVERITY_COLORS[sev] || 'var(--muted)'};border-radius:8px;padding:0;">
        <summary class="finding-header" style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;padding:1rem 1.25rem;cursor:pointer;list-style:none;">
          <span class="badge ${severityClass(sev)}">${sev}</span>
          <span class="finding-title" style="font-weight:600;font-size:0.875rem;">${escapeHtml(f.title)}</span>
          <span class="badge badge-category" style="background-color:rgba(99,102,241,0.12);color:var(--accent);border:1px solid rgba(99,102,241,0.25);">${formatCategory(f.category)}</span>
          <span class="analyzer-pill" style="font-size:0.7rem;padding:0.1rem 0.4rem;border-radius:9999px;background-color:rgba(99,102,241,0.08);color:var(--muted);border:1px solid var(--border);">${escapeHtml(f.analyzer)}</span>
        </summary>
        <div class="finding-body" style="padding:0 1.25rem 1rem;border-top:1px solid var(--border);">
          <p class="finding-description" style="font-size:0.8125rem;color:var(--text);line-height:1.6;margin:0.75rem 0;">${escapeHtml(f.description)}</p>
          ${fileLine}
          ${snippet}
          ${remediation}
        </div>
      </details>
    </li>`;
  });

  findingsList.innerHTML = findingsHtml;
}

/* ============================================================
   Render: Notes List
   ============================================================ */
function renderNotesList() {
  const container = document.getElementById('notes-container');
  if (!appData.notes || appData.notes.length === 0) {
    container.innerHTML = '<p class="muted">No notes yet.</p>';
    return;
  }

  // Reverse chronological
  const sorted = [...appData.notes].sort((a, b) => b.date.localeCompare(a.date));

  let html = '';
  sorted.forEach(note => {
    const dateStr = new Date(note.date + 'T00:00:00').toLocaleDateString('en-US', {
      year: 'numeric', month: 'long', day: 'numeric'
    });
    const tags = (note.tags || []).map(t =>
      `<span class="tag-pill">${escapeHtml(t)}</span>`
    ).join('');

    html += `<a href="#/note/${encodeURIComponent(note.id)}" class="note-card">
      <div class="note-card-header">
        <span class="note-date">${dateStr}</span>
        <div class="note-tags">${tags}</div>
      </div>
      <h3 class="note-title">${escapeHtml(note.title)}</h3>
      <p class="note-excerpt">${escapeHtml(note.excerpt || '')}</p>
    </a>`;
  });

  container.innerHTML = html;
}

/* ============================================================
   Render: Note Detail
   ============================================================ */
function renderNoteDetail(id) {
  const note = appData.notes.find(n => n.id === id);
  const breadcrumb = document.getElementById('note-breadcrumb-title');
  const content = document.getElementById('note-content');

  if (!note) {
    breadcrumb.textContent = 'Not Found';
    content.innerHTML = '<p class="muted">Note not found.</p>';
    return;
  }

  breadcrumb.textContent = note.title;

  const dateStr = new Date(note.date + 'T00:00:00').toLocaleDateString('en-US', {
    year: 'numeric', month: 'long', day: 'numeric'
  });
  const tags = (note.tags || []).map(t =>
    `<span class="tag-pill">${escapeHtml(t)}</span>`
  ).join('');

  content.innerHTML = `<div class="note-detail-header">
    <h1>${escapeHtml(note.title)}</h1>
    <div class="note-detail-meta">
      <span class="note-date">${dateStr}</span>
      <div class="note-tags">${tags}</div>
    </div>
  </div>
  <div class="note-body">${sanitizeHtml(note.body)}</div>`;
}

/* ============================================================
   Bootstrap
   ============================================================ */
function renderFooter() {
  if (!appData.summary) return;
  const s = appData.summary;
  const dateEl = document.getElementById('footer-scan-date');
  const countEl = document.getElementById('footer-skill-count');
  if (dateEl && s.scan_date) {
    dateEl.textContent = 'Scanned ' + new Date(s.scan_date).toLocaleDateString('en-US', {
      year: 'numeric', month: 'long', day: 'numeric'
    });
  }
  if (countEl) {
    countEl.textContent = `${s.total_skills} skills \u00b7 ${s.total_findings} findings \u00b7 ${s.analyzers_used ? s.analyzers_used.length : 0} analyzers`;
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  await loadData();
  renderFooter();
  window.addEventListener('hashchange', router);
  router();
});
