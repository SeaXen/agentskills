# index.html Pattern (Annotated)

Working template from `hermes-telemetry` dashboard. Copy and adapt.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My Plugin Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
  /* ... dark theme styles ... */
  
  /* Budget item layout — label, amount, edit button on ONE line */
  .budget-item { display: flex; flex-direction: column; gap: 8px; }
  .budget-item .info { 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
    gap: 12px; 
  }
  .budget-item .info span:first-child { text-align: left; }
  .budget-item .info span:last-of-type { flex: 0 0 auto; text-align: right; }
  .budget-edit-btn { 
    background: #21262d; 
    color: #58a6ff; 
    border: 1px solid #30363d; 
    border-radius: 4px; 
    padding: 2px 8px; 
    font-size: 11px; 
    cursor: pointer; 
    margin-left: 12px; 
    white-space: nowrap; 
  }
  .budget-edit-btn:hover { background: #30363d; }

  /* Modal overlay */
  .modal-overlay { 
    position: fixed; top: 0; left: 0; right: 0; bottom: 0; 
    background: rgba(0,0,0,0.7); 
    display: none; align-items: center; justify-content: center; 
    z-index: 1000; 
  }
  .modal-overlay.open { display: flex; }
  .modal { 
    background: #161b22; 
    border: 1px solid #30363d; 
    border-radius: 8px; 
    padding: 24px; 
    width: 100%; 
    max-width: 400px; 
    margin: 16px; 
  }
  .modal .form-group { margin-bottom: 16px; }
  .modal label { display: block; color: #8b949e; font-size: 12px; margin-bottom: 4px; }
  .modal select, .modal input { 
    width: 100%; 
    background: #21262d; 
    color: #c9d1d9; 
    border: 1px solid #30363d; 
    border-radius: 6px; 
    padding: 8px 12px; 
    font-size: 13px; 
    box-sizing: border-box; 
  }
  .modal .form-row { display: flex; gap: 8px; }
  .modal .form-row .form-group { flex: 1; }
  .modal-actions { display: flex; justify-content: flex-end; gap: 8px; margin-top: 24px; }
  .modal-btn { padding: 8px 16px; border-radius: 6px; font-size: 13px; cursor: pointer; border: 1px solid #30363d; }
  .modal-btn.cancel { background: #21262d; color: #c9d1d9; }
  .modal-btn.save { background: #238636; color: #fff; }
</style>
</head>
<body>

<div class="header">
  <h1>My Plugin</h1>
  <div class="actions">
    <select id="windowSelect" onchange="loadAll()">
      <option value="24">Last 24h</option>
      <option value="168">Last 7 days</option>
      <option value="720">Last 30 days</option>
      <option value="2160">Last 90 days</option>
      <option value="0" selected>All time</option>
    </select>
    <button class="refresh-btn" onclick="loadAll()">&#x21bb; Refresh</button>
  </div>
</div>

<div class="container" id="app">
  <div class="loading">Loading...</div>
</div>

<!-- Budget Modal -->
<div class="modal-overlay" id="budgetModal" onclick="if(event.target===this) closeBudgetModal()">
  <div class="modal" onclick="event.stopPropagation()">
    <h3>Edit Budget</h3>
    <div class="form-group">
      <label>Scope</label>
      <select id="budgetScope">
        <option value="global">Global</option>
        <option value="per_cron_job">Per Cron Job</option>
        <option value="per_sender">Per Sender</option>
      </select>
    </div>
    <div class="form-group">
      <label>Window</label>
      <select id="budgetWindow">
        <option value="daily">Daily</option>
        <option value="monthly">Monthly</option>
      </select>
    </div>
    <div class="form-group">
      <label>Limit (USD)</label>
      <input type="number" id="budgetLimit" step="0.01" min="0" placeholder="e.g. 5.00">
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>Soft threshold (%)</label>
        <input type="number" id="budgetSoftPct" step="0.01" min="0" max="1" placeholder="0.80">
      </div>
      <div class="form-group">
        <label>Hard threshold (%)</label>
        <input type="number" id="budgetHardPct" step="0.01" min="0" max="1" placeholder="1.00">
      </div>
    </div>
    <div class="form-group">
      <label>On estimated data</label>
      <select id="budgetOnEstimated">
        <option value="warn_only">Warn only (degrade hard to soft)</option>
        <option value="enforce">Enforce hard limits</option>
      </select>
    </div>
    <div class="modal-error" id="budgetModalError"></div>
    <div class="modal-actions">
      <button class="modal-btn cancel" onclick="closeBudgetModal()">Cancel</button>
      <button class="modal-btn save" onclick="saveBudget()">Save</button>
    </div>
  </div>
</div>

<script>
const API = '';
let charts = {};

function $(sel) { return document.querySelector(sel); }
function nf(n) { return n == null ? '—' : Number(n).toLocaleString(); }
function fmtCost(v) { return v == null ? '$0.00' : '$' + Number(v).toFixed(4); }

async function fetchJSON(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
}

function destroyChart(id) { if (charts[id]) { charts[id].destroy(); delete charts[id]; } }
// Budget modal functions
let currentBudgetScope = 'global';
let currentBudgetWindow = 'daily';

async function openBudgetModal(scope) {
  currentBudgetScope = scope;
  $('#budgetScope').value = scope;
  $('#budgetModalError').classList.remove('show');
  $('#budgetModalError').textContent = '';

  // Fetch current budget details for pre-fill
  try {
    const res = await fetch(`/api/budget/detail?scope=${encodeURIComponent(scope)}&window=${encodeURIComponent($('#budgetWindow').value)}`);
    const data = await res.json();
    if (!data.error) {
      $('#budgetLimit').value = data.limit_usd !== null && data.limit_usd !== undefined ? data.limit_usd : '';
      $('#budgetSoftPct').value = data.soft_pct !== undefined ? data.soft_pct : '';
      $('#budgetHardPct').value = data.hard_pct !== undefined ? data.hard_pct : '';
      $('#budgetOnEstimated').value = data.on_estimated_mode || 'warn_only';
    } else {
      // Fallback to defaults on error
      $('#budgetWindow').value = 'daily';
      $('#budgetLimit').value = '';
      $('#budgetSoftPct').value = '';
      $('#budgetHardPct').value = '';
      $('#budgetOnEstimated').value = 'warn_only';
    }
  } catch {
    // Fallback to defaults on network error
    $('#budgetWindow').value = 'daily';
    $('#budgetLimit').value = '';
    $('#budgetSoftPct').value = '';
    $('#budgetHardPct').value = '';
    $('#budgetOnEstimated').value = 'warn_only';
  }

  $('#budgetModal').classList.add('open');
}

function closeBudgetModal() {
  $('#budgetModal').classList.remove('open');
}

async function saveBudget() {
  // Helper: parse float, return undefined if empty/whitespace
  const parseOptFloat = (v) => {
    const s = v.trim();
    return s === '' ? undefined : parseFloat(s);
  };

  const payload = {
    scope: $('#budgetScope').value,
    window: $('#budgetWindow').value,
    limit_usd: parseOptFloat($('#budgetLimit').value),
    soft_pct: parseOptFloat($('#budgetSoftPct').value),
    hard_pct: parseOptFloat($('#budgetHardPct').value),
    on_estimated_mode: $('#budgetOnEstimated').value
  };

  if (payload.limit_usd === undefined || isNaN(payload.limit_usd)) {
    showModalError('Limit (USD) is required');
    return;
  }

  $('#budgetModalError').classList.remove('show');

  try {
    const response = await fetch('/api/budget', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (result.error) {
      showModalError(result.error);
      return;
    }
    closeBudgetModal();
    loadAll(); // refresh dashboard
  } catch (err) {
    showModalError('Request failed: ' + err.message);
  }
}

function showModalError(msg) {
  const el = $('#budgetModalError');
  el.textContent = msg;
  el.classList.add('show');
}

// ─── Main load ─────────────────────────────────────────────────
async function loadAll() {
  const hours = $('#windowSelect').value;
  const app = $('#app');
  app.innerHTML = '<div class="loading">Loading...</div>';

  try {
    const [summary, cron, providers, runs, budget, tokenBreakdown] = await Promise.all([
      fetchJSON(`/api/summary?hours=${hours}`),
      fetchJSON(`/api/cron?hours=${hours}`),
      fetchJSON(`/api/providers?hours=${hours}`),
      fetchJSON('/api/runs?limit=30'),
      fetchJSON('/api/budget'),
      fetchJSON(`/api/token-breakdown?hours=${hours}`),
    ]);

    const r = summary.runs || {};
    const l = summary.llm || {};

    // Stat cards
    let html = '<div class="stat-grid">';
    html += renderStatCard('sessions', nf(r.total_runs), 'Sessions', 'blue');
    html += renderStatCard('ok', nf(r.ok_runs), 'OK', 'green');
    html += renderStatCard('failed', nf(r.failed_runs), 'Failed', 'red');
    html += renderStatCard('api', nf(l.api_calls), 'API Calls', 'purple');
    html += renderStatCard('tokens', nf(r.tokens_in), 'Tokens In', '');
    html += renderStatCard('cost', fmtCost(r.cost_usd), 'Cost', 'yellow');
    html += '</div>';

    // Token breakdown
    if (tokenBreakdown && tokenBreakdown.total_tokens > 0) {
      html += renderTokenBreakdown(tokenBreakdown);
    }

    // Budget
    html += renderBudget(budget);

    // Charts...
    html += renderCharts();

    // Tables...
    html += renderTables(cron, runs);

    app.innerHTML = html;
    drawAllCharts(summary, cron, providers);

  } catch (err) {
    app.innerHTML = `<div class="error-box">Error: ${err.message}</div>`;
  }
}

function renderBudget(data) {
  if (!data.enabled) return '<div class="budget-bar"><h3>Budgets</h3><div class="budget-disabled">No budget.yaml</div></div>';
  const items = data.budgets || [];
  if (!items.length) return '<div class="budget-bar"><h3>Budgets</h3><div class="budget-disabled">No limits</div></div>';
  let html = '<div class="budget-bar"><h3>Budgets</h3>';
  for (const s of items) {
    const cls = s.level;
    // Escape scope for safe JS string context in onclick attribute
    const safeScope = JSON.stringify(s.scope);
    html += `<div class="budget-item">
      <div class="info"><span>${s.scope}</span><span>${fmtCost(s.spent)} / ${fmtCost(s.limit)} (${s.pct}%)</span><button class="budget-edit-btn" onclick="openBudgetModal(${safeScope})">Edit</button></div>
      <div class="bar-bg"><div class="bar-fill ${cls}" style="width:${Math.min(s.pct, 100)}%"></div></div>
    </div>`;
  }
  html += `<div class="budget-disabled" style="margin-top:8px">on_estimated: ${data.on_estimated}</div></div>`;
  return html;
}

function renderTokenBreakdown(data) {
  const tb = data;
  let html = '<div class="table-card"><h3>Token Breakdown</h3>';
  html += '<table><thead><tr><th>Type</th><th class="text-right">Count</th><th class="text-right">%</th></tr></thead><tbody>';
  const types = [
    { key: 'tokens_in', label: 'Input', color: '#58a6ff' },
    { key: 'tokens_out', label: 'Output', color: '#3fb950' },
    { key: 'cache_read_tokens', label: 'Cache', color: '#d29922' },
    { key: 'reasoning_tokens', label: 'Reasoning', color: '#f85149' },
  ];
  for (const t of types) {
    const val = tb[t.key] || 0;
    const pct = tb.total_tokens > 0 ? ((val / tb.total_tokens) * 100).toFixed(1) : '0.0';
    html += `<tr><td><span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:${t.color};margin-right:8px;vertical-align:middle"></span>${t.label}</td><td class="text-right">${nf(val)}</td><td class="text-right">${pct}%</td></tr>`;
  }
  html += `<tr style="border-top:1px solid #30363d"><td><b>Total</b></td><td class="text-right"><b>${nf(tb.total_tokens)}</b></td><td class="text-right"><b>100%</b></td></tr>`;
  html += '</tbody></table></div>';
  return html;
}

// Chart rendering, table rendering, etc.
function drawAllCharts(summary, cron, providers) { /* ... */ }
function renderCharts() { /* returns chart row HTML */ }
function renderTables(cron, runs) { /* returns table HTML */ }
function renderStatCard(id, value, label, cls) { /* ... */ }

loadAll();
setInterval(loadAll, 30000);
</script>
</body>
</html>
```

## Key patterns to copy

1. **Time window selector** — includes "All time" (value=0) as default(selected)
2. **Modal form** — hidden overlay, `openBudgetModal(scope)` pre-fills scope, `saveBudget()` POSTs to `/api/budget`
3. **Budget row layout** — `.info` flex container holds label + amount + edit button on ONE line
4. **Token breakdown table** — colored indicators, percentages, total row
5. **All fetchJSON calls include `?hours=${hours}`** — every endpoint respects time window
6. **Auto-refresh** — `setInterval(loadAll, 30000)`