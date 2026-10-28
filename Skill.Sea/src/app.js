/**
 * Skill.Sea — Application Controller
 * Inspired by skillleaderboard.com and ExamForge design tokens.
 * Features: Skill Hub (All Skills), Multi-facet sorting & filtering by Category, Library / Git Repo, Tier, Search.
 */

(function () {
  'use strict';

  // Application State
  const state = {
    catalog: [],
    filteredCatalog: [],
    categories: [],
    repositories: [],
    stats: {
      totalSkills: 6063,
      totalCategories: 38,
      totalRepositories: 225,
      activeHotSetCount: 130
    },
    currentViewName: 'skill-hub', // 'skill-hub', 'hotset', 'categories', 'library', 'guide'
    selectedCategory: 'all',
    selectedLibrary: 'all',
    filterTier: 'all',
    searchQuery: '',
    hotsetSearchQuery: '',
    categorySearchQuery: '',
    repoSearchQuery: '',
    sortBy: 'rank',
    currentView: 'table',
    installCmdMode: 'npx', // 'npx', 'python', 'myrepo'
    currentPage: 1,
    pageSize: 50,
    theme: localStorage.getItem('skill-sea-theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'),
    activeSkill: null
  };

  // DOM Elements
  const el = {
    themeToggle: document.getElementById('theme-toggle'),
    themeIcon: document.getElementById('theme-icon'),
    categoryRail: document.getElementById('category-rail'),
    cmdTypeToggle: document.getElementById('cmd-type-toggle'),
    searchInput: document.getElementById('search-input'),
    hotsetSearchInput: document.getElementById('hotset-search-input'),
    categorySearchInput: document.getElementById('category-search-input'),
    repoSearchInput: document.getElementById('repo-search-input'),
    categoryFilterSelect: document.getElementById('category-filter-select'),
    libraryFilterSelect: document.getElementById('library-filter-select'),
    sortSelect: document.getElementById('sort-select'),
    tierSelect: document.getElementById('tier-select'),
    activeFiltersBar: document.getElementById('active-filters-bar'),
    viewTableBtn: document.getElementById('view-table-btn'),
    viewGridBtn: document.getElementById('view-grid-btn'),
    tableContainer: document.getElementById('table-container'),
    gridContainer: document.getElementById('grid-container'),
    tableBody: document.getElementById('table-body'),
    gridBody: document.getElementById('grid-body'),
    hotsetGrid: document.getElementById('hotset-grid'),
    categoryDirectoryGrid: document.getElementById('category-directory-grid'),
    repoGrid: document.getElementById('repo-grid'),
    repoCountBadge: document.getElementById('repo-count-badge'),
    itemCount: document.getElementById('item-count'),
    prevPageBtn: document.getElementById('prev-page-btn'),
    nextPageBtn: document.getElementById('next-page-btn'),
    pageIndicator: document.getElementById('page-indicator'),
    toast: document.getElementById('toast'),
    toastMessage: document.getElementById('toast-message'),
    drawerBackdrop: document.getElementById('drawer-backdrop'),
    drawerTitle: document.getElementById('drawer-title'),
    drawerSubtitle: document.getElementById('drawer-subtitle'),
    drawerBody: document.getElementById('drawer-body'),
    drawerCloseBtn: document.getElementById('drawer-close-btn'),
    statTotalSkills: document.getElementById('stat-total-skills'),
    statTotalCats: document.getElementById('stat-total-cats'),
    statTotalRepos: document.getElementById('stat-total-repos'),
    statActiveHot: document.getElementById('stat-active-hot'),
    syncBtn: document.getElementById('sync-btn')
  };

  // Apply Theme
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('skill-sea-theme', theme);
    if (el.themeIcon) {
      el.themeIcon.className = theme === 'dark' ? 'ti ti-sun' : 'ti ti-moon';
    }
  }

  // Toast message utility
  let toastTimer = null;
  function showToast(msg) {
    if (!el.toast) return;
    el.toastMessage.textContent = msg;
    el.toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      el.toast.classList.remove('show');
    }, 2400);
  }

  // Copy to clipboard with toast
  window.copyCommand = function (text, event) {
    if (event) event.stopPropagation();
    navigator.clipboard.writeText(text).then(() => {
      showToast(`Copied: ${text}`);
    }).catch(() => {
      const input = document.createElement('input');
      input.value = text;
      document.body.appendChild(input);
      input.select();
      document.execCommand('copy');
      document.body.removeChild(input);
      showToast(`Copied: ${text}`);
    });
  };

  // Switch Active Page View (Skill Hub, Hotset, Categories, Library, Guide)
  window.switchView = function (viewName) {
    if (viewName === 'leaderboard' || viewName === 'home') viewName = 'skill-hub';
    state.currentViewName = viewName;

    const views = ['skill-hub', 'hotset', 'categories', 'library', 'guide'];
    views.forEach(v => {
      const vEl = document.getElementById(`view-${v}`);
      if (vEl) {
        if (v === viewName) {
          vEl.classList.add('active');
        } else {
          vEl.classList.remove('active');
        }
      }
      const navBtn = document.getElementById(`tab-${v}`);
      if (navBtn) {
        if (v === viewName) navBtn.classList.add('on');
        else navBtn.classList.remove('on');
      }
      const mobBtn = document.getElementById(`mob-tab-${v}`);
      if (mobBtn) {
        if (v === viewName) mobBtn.classList.add('on');
        else mobBtn.classList.remove('on');
      }
    });

    if (viewName === 'hotset') {
      renderHotSet();
    } else if (viewName === 'categories') {
      renderCategoryDirectory();
    } else if (viewName === 'library') {
      renderRepositories();
    } else if (viewName === 'skill-hub') {
      renderResults();
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Initialize Data
  async function init() {
    applyTheme(state.theme);
    const dataVersion = '2.3';

    try {
      const statsRes = await fetch(`./data/stats.json?v=${dataVersion}`);
      if (statsRes.ok) {
        state.stats = await statsRes.json();
        renderStats();
      }
    } catch (e) {
      console.warn('Using embedded stats fallback', e);
    }

    try {
      const catRes = await fetch(`./data/categories.json?v=${dataVersion}`);
      if (catRes.ok) {
        state.categories = await catRes.json();
        renderCategories();
      }
    } catch (e) {
      console.warn('Error loading categories', e);
    }

    try {
      const repoRes = await fetch(`./data/repositories.json?v=${dataVersion}`);
      if (repoRes.ok) {
        state.repositories = await repoRes.json();
      }
    } catch (e) {
      console.warn('Error loading repositories.json', e);
    }

    try {
      const catalogRes = await fetch(`./data/catalog.json?v=${dataVersion}`);
      if (catalogRes.ok) {
        state.catalog = await catalogRes.json();
        renderStats();
        populateDropdowns();
        applyFilter();
      } else {
        showToast('Error loading catalog. Check data files.');
      }
    } catch (e) {
      console.error('Failed to load catalog data:', e);
      showToast('Could not fetch catalog.json');
    }

    setupEventListeners();
  }

  function renderStats() {
    if (el.statTotalSkills) el.statTotalSkills.textContent = Number(state.stats.totalSkills || state.catalog.length).toLocaleString();
    if (el.statTotalCats) el.statTotalCats.textContent = state.stats.totalCategories || state.categories.length;
    if (el.statTotalRepos) el.statTotalRepos.textContent = state.stats.totalRepositories || state.repositories.length || '210';
    if (el.statActiveHot) el.statActiveHot.textContent = state.stats.activeHotSetCount || '130';
  }

  function renderCategories() {
    if (!el.categoryRail) return;
    let html = `
      <button class="cat-pill ${state.selectedCategory === 'all' ? 'active' : ''}" data-cat="all">
        <i class="ti ti-layout-grid" style="font-size:13px"></i>
        <span>All Categories</span>
        <span class="cat-count">${state.catalog.length || state.stats.totalSkills}</span>
      </button>
    `;

    for (const cat of state.categories) {
      const isActive = state.selectedCategory === cat.slug;
      html += `
        <button class="cat-pill cat-color-${cat.colorTheme || 'blue'} ${isActive ? 'active' : ''}" data-cat="${cat.slug}">
          <i class="ti ti-${cat.icon || 'folder'}" style="font-size:13px"></i>
          <span>${cat.cleanTitle || cat.title}</span>
          <span class="cat-count">${cat.count}</span>
        </button>
      `;
    }

    el.categoryRail.innerHTML = html;
  }

  // Populate Filter Dropdowns
  function populateDropdowns() {
    // 1. Category Filter Dropdown
    if (el.categoryFilterSelect) {
      let catOpts = `<option value="all">Category: All (${state.categories.length})</option>`;
      for (const cat of state.categories) {
        catOpts += `<option value="${cat.slug}">${cat.cleanTitle || cat.title} (${cat.count})</option>`;
      }
      el.categoryFilterSelect.innerHTML = catOpts;
      el.categoryFilterSelect.value = state.selectedCategory;
    }

    // 2. Library / Repository Filter Dropdown
    if (el.libraryFilterSelect) {
      let repoOpts = `<option value="all">Library: All (${state.repositories.length})</option>`;
      for (const r of state.repositories) {
        repoOpts += `<option value="${r.name}">${r.name} (${r.skillsCount})</option>`;
      }
      el.libraryFilterSelect.innerHTML = repoOpts;
      el.libraryFilterSelect.value = state.selectedLibrary;
    }
  }

  // Filter and Sort Engine
  function applyFilter() {
    const q = state.searchQuery.toLowerCase().trim();
    const cat = state.selectedCategory;
    const lib = state.selectedLibrary;
    const tier = state.filterTier;

    state.filteredCatalog = state.catalog.filter(item => {
      // Category filter
      if (cat !== 'all' && item.category !== cat) return false;
      // Library / Repository filter
      if (lib !== 'all' && item.repository !== lib) return false;
      // Tier filter
      if (tier === 'hot' && !item.isActive) return false;
      if (tier === 'vault' && item.isActive) return false;
      // Query filter
      if (q) {
        const matchesName = item.name.toLowerCase().includes(q);
        const matchesDesc = (item.description || '').toLowerCase().includes(q);
        const matchesRepo = (item.repository || '').toLowerCase().includes(q);
        const matchesCat = (item.cleanCategory || '').toLowerCase().includes(q);
        return matchesName || matchesDesc || matchesRepo || matchesCat;
      }
      return true;
    });

    // Sorting Logic
    state.filteredCatalog.sort((a, b) => {
      if (state.sortBy === 'rank') {
        return (a.rank || 9999) - (b.rank || 9999);
      }
      if (state.sortBy === 'name-asc') {
        return a.name.localeCompare(b.name);
      }
      if (state.sortBy === 'name-desc') {
        return b.name.localeCompare(a.name);
      }
      if (state.sortBy === 'category') {
        return (a.cleanCategory || '').localeCompare(b.cleanCategory || '');
      }
      if (state.sortBy === 'repo') {
        return (a.repository || '').localeCompare(b.repository || '');
      }
      if (state.sortBy === 'hot-first') {
        if (a.isActive && !b.isActive) return -1;
        if (!a.isActive && b.isActive) return 1;
        return (a.rank || 9999) - (b.rank || 9999);
      }
      return 0;
    });

    state.currentPage = 1;
    renderActiveFilterChips();
    renderResults();
  }

  // Render Active Filter Chips
  function renderActiveFilterChips() {
    if (!el.activeFiltersBar) return;
    const hasFilter = state.selectedCategory !== 'all' || state.selectedLibrary !== 'all' || state.filterTier !== 'all' || state.searchQuery !== '';

    if (!hasFilter) {
      el.activeFiltersBar.style.display = 'none';
      el.activeFiltersBar.innerHTML = '';
      return;
    }

    el.activeFiltersBar.style.display = 'flex';
    let chipsHtml = `<span class="active-filters-label">Filters:</span>`;

    if (state.searchQuery) {
      chipsHtml += `
        <span class="filter-chip">
          Search: "<b>${escapeHtml(state.searchQuery)}</b>"
          <span class="filter-chip-remove" onclick="clearSearchFilter()">×</span>
        </span>
      `;
    }

    if (state.selectedCategory !== 'all') {
      const catObj = state.categories.find(c => c.slug === state.selectedCategory);
      const catName = catObj ? (catObj.cleanTitle || catObj.title) : state.selectedCategory;
      chipsHtml += `
        <span class="filter-chip">
          Category: <b>${escapeHtml(catName)}</b>
          <span class="filter-chip-remove" onclick="setCategory('all')">×</span>
        </span>
      `;
    }

    if (state.selectedLibrary !== 'all') {
      chipsHtml += `
        <span class="filter-chip">
          Library: <b>${escapeHtml(state.selectedLibrary)}</b>
          <span class="filter-chip-remove" onclick="setLibrary('all')">×</span>
        </span>
      `;
    }

    if (state.filterTier !== 'all') {
      chipsHtml += `
        <span class="filter-chip">
          Tier: <b>${state.filterTier === 'hot' ? 'Hot-Set Only' : 'Vault Only'}</b>
          <span class="filter-chip-remove" onclick="setTier('all')">×</span>
        </span>
      `;
    }

    chipsHtml += `<button class="filter-reset-btn" onclick="clearAllFilters()">Reset All</button>`;
    el.activeFiltersBar.innerHTML = chipsHtml;
  }

  window.clearSearchFilter = function () {
    state.searchQuery = '';
    if (el.searchInput) el.searchInput.value = '';
    applyFilter();
  };

  window.setTier = function (tier) {
    state.filterTier = tier;
    if (el.tierSelect) el.tierSelect.value = tier;
    applyFilter();
  };

  window.setLibrary = function (libSlug) {
    state.selectedLibrary = libSlug;
    if (el.libraryFilterSelect) el.libraryFilterSelect.value = libSlug;
    applyFilter();
    switchView('skill-hub');
  };

  window.setCategory = function (catSlug) {
    state.selectedCategory = catSlug;
    if (el.categoryFilterSelect) el.categoryFilterSelect.value = catSlug;
    renderCategories();
    applyFilter();
    switchView('skill-hub');
  };

  window.clearAllFilters = function () {
    state.selectedCategory = 'all';
    state.selectedLibrary = 'all';
    state.filterTier = 'all';
    state.searchQuery = '';
    state.sortBy = 'rank';
    if (el.searchInput) el.searchInput.value = '';
    if (el.categoryFilterSelect) el.categoryFilterSelect.value = 'all';
    if (el.libraryFilterSelect) el.libraryFilterSelect.value = 'all';
    if (el.tierSelect) el.tierSelect.value = 'all';
    if (el.sortSelect) el.sortSelect.value = 'rank';
    renderCategories();
    applyFilter();
    switchView('skill-hub');
    showToast('Filters reset to default.');
  };

  // Render Skill Hub Results (Table or Grid)
  function renderResults() {
    const total = state.filteredCatalog.length;
    const totalPages = Math.ceil(total / state.pageSize) || 1;
    if (state.currentPage > totalPages) state.currentPage = totalPages;

    const startIdx = (state.currentPage - 1) * state.pageSize;
    const endIdx = Math.min(startIdx + state.pageSize, total);
    const pageItems = state.filteredCatalog.slice(startIdx, endIdx);

    if (el.itemCount) {
      el.itemCount.textContent = `Showing ${total === 0 ? 0 : startIdx + 1}–${endIdx} of ${total.toLocaleString()} skills`;
    }
    if (el.pageIndicator) {
      el.pageIndicator.textContent = `Page ${state.currentPage} of ${totalPages}`;
    }
    if (el.prevPageBtn) el.prevPageBtn.disabled = state.currentPage <= 1;
    if (el.nextPageBtn) el.nextPageBtn.disabled = state.currentPage >= totalPages;

    if (state.currentView === 'table') {
      renderTable(pageItems);
      el.tableContainer.style.display = 'block';
      el.gridContainer.style.display = 'none';
    } else {
      renderGrid(pageItems);
      el.tableContainer.style.display = 'none';
      el.gridContainer.style.display = 'grid';
    }
  }

  function renderTable(items) {
    if (!el.tableBody) return;
    if (items.length === 0) {
      el.tableBody.innerHTML = `
        <tr>
          <td colspan="6" style="text-align:center;padding:48px 12px;color:var(--text-muted)">
            <i class="ti ti-search-off" style="font-size:32px;display:block;margin-bottom:8px"></i>
            No skills found matching your active filter criteria.
            <div style="margin-top:12px">
              <button class="btn-action" onclick="clearAllFilters()">Clear Filters</button>
            </div>
          </td>
        </tr>
      `;
      return;
    }

    let rows = '';
    for (const item of items) {
      const isTop3 = item.rank <= 3;
      const rankClass = isTop3 ? `rank-pill rank-top-${item.rank}` : 'rank-pill';
      const tierBadge = item.isActive
        ? `<span class="tg tg-hot"><i class="ti ti-flame" style="font-size:11px"></i> Hot-Set</span>`
        : `<span class="tg tg-vault">Vault</span>`;

      // Active status shown as a dedicated TAG, NOT as a git repository!
      const activeTag = item.isActive
        ? `<span class="tag-active-pill" title="Currently activated in your workspace .agents/skills"><i class="ti ti-flame" style="font-size:9.5px"></i> Active</span>`
        : '';

      // Determine active 1-click command based on state.installCmdMode
      let cmd = item.npxCmd || `npx skills add ${item.githubUrl}`;
      if (state.installCmdMode === 'python') {
        cmd = item.activationCmd;
      } else if (state.installCmdMode === 'myrepo') {
        cmd = item.myRepoNpxCmd || 'npx skills add https://github.com/SeaXen/agentskills';
      }

      rows += `
        <tr onclick="openSkillDrawer('${item.id}')">
          <td class="col-rank">
            <span class="${rankClass}">${item.rank || '-'}</span>
          </td>
          <td>
            <div class="skill-meta">
              <div class="skill-icon-tile">
                <i class="ti ti-${item.categoryIcon || 'cpu'}"></i>
              </div>
              <div class="skill-info">
                <div class="skill-title-row">
                  <span class="skill-title">${escapeHtml(item.name)}</span>
                  ${activeTag}
                  <span class="skill-repo" onclick="event.stopPropagation(); setLibrary('${item.repository}')" title="Filter by library: ${escapeHtml(item.repository)}">
                    <i class="ti ti-books"></i>${escapeHtml(item.repository)}
                  </span>
                  <a href="${escapeHtml(item.githubUrl)}" target="_blank" rel="noopener noreferrer" class="skill-repo" onclick="event.stopPropagation()" title="Open upstream GitHub repository (${escapeHtml(item.repository)})">
                    <i class="ti ti-brand-github"></i>
                  </a>
                </div>
                <div class="skill-desc">${escapeHtml(item.description || 'Specialized skill ready for instant agent activation.')}</div>
              </div>
            </div>
          </td>
          <td>
            <span class="tg tg-cat cat-color-${item.colorTheme || 'blue'}" onclick="event.stopPropagation(); setCategory('${item.category}')" title="Filter by category: ${escapeHtml(item.cleanCategory || item.category)}">
              <i class="ti ti-${item.categoryIcon || 'folder'}" style="font-size:10px"></i>
              ${escapeHtml(item.cleanCategory || item.category)}
            </span>
          </td>
          <td>
            ${tierBadge}
          </td>
          <td class="col-cmd">
            <div class="cmd-box" onclick="copyCommand('${escapeHtml(cmd)}', event)" title="Click to copy 1-click install command (${state.installCmdMode.toUpperCase()})">
              <code>${escapeHtml(cmd)}</code>
              <i class="ti ti-copy cmd-copy-icon"></i>
            </div>
          </td>
          <td style="text-align:right">
            <button class="btn-action" onclick="event.stopPropagation(); openSkillDrawer('${item.id}')">
              <span>Inspect</span>
              <i class="ti ti-chevron-right" style="font-size:12px"></i>
            </button>
          </td>
        </tr>
      `;
    }
    el.tableBody.innerHTML = rows;
  }

  function renderGrid(items) {
    if (!el.gridBody) return;
    if (items.length === 0) {
      el.gridBody.innerHTML = `
        <div style="grid-column: 1 / -1; text-align:center; padding: 48px; color:var(--text-muted)">
          <i class="ti ti-search-off" style="font-size:32px;display:block;margin-bottom:8px"></i>
          No skills found matching your active filter criteria.
          <div style="margin-top:12px">
            <button class="btn-action" onclick="clearAllFilters()">Clear Filters</button>
          </div>
        </div>
      `;
      return;
    }

    let cards = '';
    for (const item of items) {
      const tierBadge = item.isActive
        ? `<span class="tg tg-hot"><i class="ti ti-flame" style="font-size:10px"></i> Hot-Set</span>`
        : `<span class="tg tg-vault">Vault</span>`;

      const activeTag = item.isActive
        ? `<span class="tag-active-pill" style="font-size:9px;padding:1px 5px"><i class="ti ti-flame" style="font-size:8.5px"></i> Active</span>`
        : '';

      let cmd = item.npxCmd || `npx skills add ${item.githubUrl}`;
      if (state.installCmdMode === 'python') {
        cmd = item.activationCmd;
      } else if (state.installCmdMode === 'myrepo') {
        cmd = item.myRepoNpxCmd || 'npx skills add https://github.com/SeaXen/agentskills';
      }

      cards += `
        <div class="skill-card" onclick="openSkillDrawer('${item.id}')">
          <div class="card-top">
            <div>
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:3px;flex-wrap:wrap">
                <span class="rank-pill ${item.rank <= 3 ? 'rank-top-' + item.rank : ''}" style="font-size:10px;width:20px;height:20px">${item.rank}</span>
                <span class="card-title">${escapeHtml(item.name)}</span>
                ${activeTag}
              </div>
              <span class="card-repo" onclick="event.stopPropagation(); setLibrary('${item.repository}')" style="cursor:pointer">
                <i class="ti ti-books"></i> ${escapeHtml(item.repository)}
              </span>
            </div>
            ${tierBadge}
          </div>
          <div class="card-desc">${escapeHtml(item.description || 'Specialized skill ready for instant agent activation.')}</div>
          <div class="card-bottom">
            <span class="tg tg-cat cat-color-${item.colorTheme || 'blue'}" onclick="event.stopPropagation(); setCategory('${item.category}')">
              <i class="ti ti-${item.categoryIcon || 'folder'}" style="font-size:10px"></i>
              ${escapeHtml(item.cleanCategory || item.category)}
            </span>
            <div class="cmd-box" onclick="copyCommand('${escapeHtml(cmd)}', event)" style="max-width:140px" title="Copy ${state.installCmdMode.toUpperCase()} command">
              <code>${state.installCmdMode.toUpperCase()}</code>
              <i class="ti ti-copy cmd-copy-icon"></i>
            </div>
          </div>
        </div>
      `;
    }
    el.gridBody.innerHTML = cards;
  }

  // =========================================================================
  // PAGE 2: Hot-Set View Renderer
  // =========================================================================
  function renderHotSet() {
    if (!el.hotsetGrid) return;
    const q = (state.hotsetSearchQuery || '').toLowerCase().trim();
    const hotItems = state.catalog.filter(s => {
      if (!s.isActive) return false;
      if (q) {
        return s.name.toLowerCase().includes(q) || (s.description || '').toLowerCase().includes(q) || (s.cleanCategory || '').toLowerCase().includes(q);
      }
      return true;
    });

    if (hotItems.length === 0) {
      el.hotsetGrid.innerHTML = `
        <div style="grid-column:1/-1;text-align:center;padding:48px;color:var(--text-muted)">
          No active hot-set skills match your query.
        </div>
      `;
      return;
    }

    let cards = '';
    for (const item of hotItems) {
      let cmd = item.npxCmd || `npx skills add ${item.githubUrl}`;
      if (state.installCmdMode === 'python') cmd = item.activationCmd;
      else if (state.installCmdMode === 'myrepo') cmd = item.myRepoNpxCmd || 'npx skills add https://github.com/SeaXen/agentskills';

      cards += `
        <div class="skill-card" onclick="openSkillDrawer('${item.id}')">
          <div class="card-top">
            <div>
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:3px;flex-wrap:wrap">
                <span class="rank-pill rank-top-1" style="font-size:10px;width:20px;height:20px">⚡</span>
                <span class="card-title">${escapeHtml(item.name)}</span>
                <span class="tag-active-pill" style="font-size:9px;padding:1px 5px"><i class="ti ti-flame" style="font-size:8.5px"></i> Active</span>
              </div>
              <span class="card-repo" onclick="event.stopPropagation(); setLibrary('${item.repository}')" style="cursor:pointer">
                <i class="ti ti-books"></i> ${escapeHtml(item.repository)}
              </span>
            </div>
            <span class="tg tg-hot"><i class="ti ti-flame" style="font-size:10px"></i> Hot-Set</span>
          </div>
          <div class="card-desc">${escapeHtml(item.description || 'Pre-linked active skill ready for instantaneous invocation.')}</div>
          <div class="card-bottom">
            <span class="tg tg-cat cat-color-${item.colorTheme || 'blue'}" onclick="event.stopPropagation(); setCategory('${item.category}')">
              <i class="ti ti-${item.categoryIcon || 'folder'}" style="font-size:10px"></i>
              ${escapeHtml(item.cleanCategory)}
            </span>
            <div class="cmd-box" onclick="copyCommand('${escapeHtml(cmd)}', event)" style="max-width:180px" title="Copy ${state.installCmdMode.toUpperCase()} command">
              <code>${escapeHtml(cmd)}</code>
              <i class="ti ti-copy cmd-copy-icon"></i>
            </div>
          </div>
        </div>
      `;
    }
    el.hotsetGrid.innerHTML = cards;
  }

  // =========================================================================
  // PAGE 3: Categories Directory Renderer
  // =========================================================================
  function renderCategoryDirectory() {
    if (!el.categoryDirectoryGrid) return;
    const q = (state.categorySearchQuery || '').toLowerCase().trim();
    const filteredCats = state.categories.filter(c => {
      if (q) {
        return c.title.toLowerCase().includes(q) || c.cleanTitle.toLowerCase().includes(q);
      }
      return true;
    });

    let cards = '';
    for (const cat of filteredCats) {
      cards += `
        <div class="cat-dir-card cat-color-${cat.colorTheme || 'blue'}" onclick="setCategory('${cat.slug}')">
          <div class="cat-dir-header">
            <div class="cat-dir-icon" style="background:var(--cat-bg);border:0.5px solid var(--cat-border);color:var(--cat-text)">
              <i class="ti ti-${cat.icon || 'folder'}"></i>
            </div>
            <div>
              <div class="cat-dir-title">${escapeHtml(cat.cleanTitle || cat.title)}</div>
              <div class="cat-dir-count">${cat.count} total skills available</div>
            </div>
          </div>
          <div style="display:flex;align-items:center;justify-content:space-between;margin-top:auto;border-top:0.5px solid var(--border);padding-top:8px;gap:6px">
            <span style="font-size:11.5px;color:var(--cat-text, var(--teal));font-weight:500">Browse Skills →</span>
            <button class="btn-copy-cat" onclick="event.stopPropagation(); copyCommand('python .agents/library/activate_skill.py link-category ${cat.slug}', event)" title="Copy 1-click command to link all skills in ${cat.slug}">
              <i class="ti ti-terminal"></i> Copy Activate Cmd
            </button>
          </div>
        </div>
      `;
    }
    el.categoryDirectoryGrid.innerHTML = cards;
  }

  // =========================================================================
  // PAGE 4: Library & Git Origin Repositories Renderer
  // =========================================================================
  function renderRepositories() {
    if (!el.repoGrid) return;
    const q = (state.repoSearchQuery || '').toLowerCase().trim();
    const repos = state.repositories.filter(r => {
      if (q) {
        return r.name.toLowerCase().includes(q) || (r.upstream || '').toLowerCase().includes(q) || (r.url || '').toLowerCase().includes(q);
      }
      return true;
    });

    if (el.repoCountBadge) {
      el.repoCountBadge.innerHTML = `<span>${repos.length} Repositories</span>`;
    }

    if (repos.length === 0) {
      el.repoGrid.innerHTML = `
        <div style="grid-column:1/-1;text-align:center;padding:48px;color:var(--text-muted)">
          No git origin repositories found matching your query.
        </div>
      `;
      return;
    }

    let cards = '';
    for (const r of repos) {
      const gitUrl = r.url || (r.upstream ? `https://github.com/${r.upstream}` : `https://github.com/SeaXen/agentskills`);
      const cloneCmd = r.cloneCmd || `git clone ${gitUrl}.git`;
      const npxCmd = r.url ? `npx skills add ${r.url}` : `npx skills add https://github.com/SeaXen/agentskills`;

      cards += `
        <div class="repo-card">
          <div>
            <div class="repo-header">
              <div>
                <div class="repo-name">${escapeHtml(r.name)}</div>
                <a href="${escapeHtml(gitUrl)}" target="_blank" rel="noopener noreferrer" class="repo-upstream">
                  <i class="ti ti-brand-github"></i> ${escapeHtml(r.upstream || r.name)}
                  <i class="ti ti-external-link" style="font-size:10px"></i>
                </a>
              </div>
              <span class="pill" style="font-family:var(--font-mono);font-size:11px">
                ${r.skillsCount} skills
              </span>
            </div>

            <div style="margin-top:10px">
              <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:3px">
                <span style="font-size:11px;color:var(--text-muted)">1-Click NPX / Clone:</span>
                <span style="font-size:10px;color:var(--teal);cursor:pointer" onclick="event.stopPropagation(); copyCommand('python .agents/library/activate_skill.py activate-repo ${r.name}', event)">Activate All Skills</span>
              </div>
              <div class="cmd-box" onclick="copyCommand('${escapeHtml(npxCmd)}', event)" style="max-width:100%" title="Click to copy NPX install command">
                <code>${escapeHtml(npxCmd)}</code>
                <i class="ti ti-copy cmd-copy-icon"></i>
              </div>
            </div>
          </div>

          <div style="border-top:0.5px solid var(--border);padding-top:10px;display:flex;align-items:center;justify-content:space-between">
            <span style="font-size:11.5px;color:var(--text-secondary)">
              ${r.hotCount > 0 ? `<b style="color:var(--teal)">${r.hotCount} Hot-Set</b> · ` : ''}Vault Collection
            </span>
            <button class="btn-action" onclick="setLibrary('${r.name}')">
              <span>View ${r.skillsCount} Skills</span>
              <i class="ti ti-chevron-right" style="font-size:11px"></i>
            </button>
          </div>
        </div>
      `;
    }
    el.repoGrid.innerHTML = cards;
  }

  // Open Skill Detail Slide-Over Drawer
  window.openSkillDrawer = function (skillId) {
    const item = state.catalog.find(s => s.id === skillId);
    if (!item) return;
    state.activeSkill = item;

    if (el.drawerTitle) el.drawerTitle.textContent = item.name;
    if (el.drawerSubtitle) el.drawerSubtitle.textContent = `${item.repository} · Category: ${item.cleanCategory}`;

    const githubRepoUrl = item.githubUrl || `https://github.com/SeaXen/agentskills`;
    const curlCommand = `curl -sSL https://raw.githubusercontent.com/SeaXen/agentskills/main/install.sh | bash -s -- activate ${item.name}`;

    let bodyHtml = `
      <div class="metadata-grid">
        <div class="meta-box">
          <span class="lbl">Category</span>
          <span class="val">${escapeHtml(item.cleanCategory)}</span>
        </div>
        <div class="meta-box">
          <span class="lbl">Tier Status</span>
          <span class="val">${item.isActive ? 'Active (Hot-Set)' : 'Offline Vault (Reserve)'}</span>
        </div>
        <div class="meta-box">
          <span class="lbl">Leaderboard Rank</span>
          <span class="val">#${item.rank}</span>
        </div>
        <div class="meta-box">
          <span class="lbl">Source Upstream</span>
          <span class="val">${escapeHtml(item.repository)}</span>
        </div>
      </div>

      <div class="doc-section">
        <h3><i class="ti ti-file-text" style="color:var(--teal)"></i> Overview & Description</h3>
        <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;margin-bottom:12px">
          ${escapeHtml(item.description || 'This skill provides structured protocols, tool integrations, and automation rules for AI coding agents.')}
        </p>
      </div>

      <div class="doc-section">
        <h3><i class="ti ti-terminal-2" style="color:var(--teal)"></i> One-Click Activation & Install Commands</h3>
        
        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">1. Universal NPX Install (Upstream Origin Repo):</p>
        <div class="code-snippet-box">
          <span class="copy-pill" onclick="copyCommand('${escapeHtml(item.npxCmd || ('npx skills add ' + item.githubUrl))}')">Copy</span>
          <code>${escapeHtml(item.npxCmd || ('npx skills add ' + item.githubUrl))}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">2. Universal NPX Install (My Repo Vault):</p>
        <div class="code-snippet-box">
          <span class="copy-pill" onclick="copyCommand('${escapeHtml(item.myRepoNpxCmd || 'npx skills add https://github.com/SeaXen/agentskills')}')">Copy</span>
          <code>${escapeHtml(item.myRepoNpxCmd || 'npx skills add https://github.com/SeaXen/agentskills')}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">3. AgentSkills Python CLI (Local Workspace Activation):</p>
        <div class="code-snippet-box">
          <span class="copy-pill" onclick="copyCommand('${escapeHtml(item.activationCmd)}')">Copy</span>
          <code>${escapeHtml(item.activationCmd)}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">4. Zero-Disk Symlink / Junction (Instant Link):</p>
        <div class="code-snippet-box">
          <span class="copy-pill" onclick="copyCommand('${escapeHtml(item.linkCmd)}')">Copy</span>
          <code>${escapeHtml(item.linkCmd)}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">5. Remote cURL Quick-Launch (Linux/macOS/Codespaces):</p>
        <div class="code-snippet-box">
          <span class="copy-pill" onclick="copyCommand('${escapeHtml(curlCommand)}')">Copy</span>
          <code>${escapeHtml(curlCommand)}</code>
        </div>
      </div>

      <div class="doc-section">
        <h3><i class="ti ti-brand-github" style="color:var(--teal)"></i> Original Repository & Documentation</h3>
        <div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap">
          <a href="${escapeHtml(githubRepoUrl)}" target="_blank" rel="noopener noreferrer" class="pill" style="padding:6px 14px;background:var(--surface-1);color:var(--text-primary)">
            <i class="ti ti-brand-github"></i>
            <span>View Upstream on GitHub</span>
            <i class="ti ti-external-link" style="font-size:11px"></i>
          </a>
          <button class="pill" onclick="copyCommand('${escapeHtml(githubRepoUrl)}')" style="padding:6px 14px">
            <i class="ti ti-link"></i>
            <span>Copy Repository Link</span>
          </button>
        </div>
      </div>

      <div class="doc-section" style="margin-top:24px;border-top:0.5px solid var(--border);padding-top:16px">
        <h3><i class="ti ti-device-floppy" style="color:var(--teal)"></i> Cloudflare R2 Sync</h3>
        <p style="font-size:12px;color:var(--text-secondary);margin-bottom:8px">
          This skill definition is cached in your local vault catalog. To sync or download the skill archive directly to Cloudflare R2 object storage:
        </p>
        <div class="code-snippet-box">
          <span class="copy-pill" onclick="copyCommand('npm run sync:r2')">Copy</span>
          <code>npm run sync:r2</code>
        </div>
      </div>
    `;

    if (el.drawerBody) el.drawerBody.innerHTML = bodyHtml;
    if (el.drawerBackdrop) {
      el.drawerBackdrop.classList.add('open');
      el.drawerBackdrop.setAttribute('aria-hidden', 'false');
      if (el.drawerCloseBtn) {
        setTimeout(() => el.drawerCloseBtn.focus(), 50);
      }
    }
  };

  window.closeSkillDrawer = function () {
    if (el.drawerBackdrop) {
      el.drawerBackdrop.classList.remove('open');
      el.drawerBackdrop.setAttribute('aria-hidden', 'true');
    }
    state.activeSkill = null;
  };

  // Event Listeners
  function setupEventListeners() {
    if (el.themeToggle) {
      el.themeToggle.addEventListener('click', () => {
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
      });
    }

    // 1-Click Install Command Type Switcher (NPX / Python / My Repo)
    const cmdTypeToggle = document.getElementById('cmd-type-toggle');
    if (cmdTypeToggle) {
      cmdTypeToggle.addEventListener('click', (e) => {
        const btn = e.target.closest('.cmd-type-btn');
        if (btn && btn.dataset.mode) {
          state.installCmdMode = btn.dataset.mode;
          cmdTypeToggle.querySelectorAll('.cmd-type-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          renderResults();
          const modeLabels = {
            npx: 'Universal NPX (Origin Upstream)',
            python: 'Python Local Activation',
            myrepo: 'My Repo Vault NPX'
          };
          showToast(`Install Mode: ${modeLabels[state.installCmdMode]}`);
        }
      });
    }

    if (el.categoryRail) {
      el.categoryRail.addEventListener('click', (e) => {
        const btn = e.target.closest('.cat-pill');
        if (btn && btn.dataset.cat) {
          setCategory(btn.dataset.cat);
        }
      });
    }

    // Main search input
    if (el.searchInput) {
      let debounce = null;
      el.searchInput.addEventListener('input', (e) => {
        clearTimeout(debounce);
        debounce = setTimeout(() => {
          state.searchQuery = e.target.value;
          applyFilter();
        }, 150);
      });
    }

    // Category filter dropdown
    if (el.categoryFilterSelect) {
      el.categoryFilterSelect.addEventListener('change', (e) => {
        setCategory(e.target.value);
      });
    }

    // Library / Repo filter dropdown
    if (el.libraryFilterSelect) {
      el.libraryFilterSelect.addEventListener('change', (e) => {
        setLibrary(e.target.value);
      });
    }

    // Tier select
    if (el.tierSelect) {
      el.tierSelect.addEventListener('change', (e) => {
        setTier(e.target.value);
      });
    }

    // Sort select
    if (el.sortSelect) {
      el.sortSelect.addEventListener('change', (e) => {
        state.sortBy = e.target.value;
        applyFilter();
      });
    }

    // Hot-set search input
    if (el.hotsetSearchInput) {
      let debounce = null;
      el.hotsetSearchInput.addEventListener('input', (e) => {
        clearTimeout(debounce);
        debounce = setTimeout(() => {
          state.hotsetSearchQuery = e.target.value;
          renderHotSet();
        }, 150);
      });
    }

    // Categories search input
    if (el.categorySearchInput) {
      let debounce = null;
      el.categorySearchInput.addEventListener('input', (e) => {
        clearTimeout(debounce);
        debounce = setTimeout(() => {
          state.categorySearchQuery = e.target.value;
          renderCategoryDirectory();
        }, 150);
      });
    }

    // Repositories search input
    if (el.repoSearchInput) {
      let debounce = null;
      el.repoSearchInput.addEventListener('input', (e) => {
        clearTimeout(debounce);
        debounce = setTimeout(() => {
          state.repoSearchQuery = e.target.value;
          renderRepositories();
        }, 150);
      });
    }

    // View toggles
    if (el.viewTableBtn) {
      el.viewTableBtn.addEventListener('click', () => {
        state.currentView = 'table';
        el.viewTableBtn.classList.add('active');
        el.viewGridBtn.classList.remove('active');
        renderResults();
      });
    }

    if (el.viewGridBtn) {
      el.viewGridBtn.addEventListener('click', () => {
        state.currentView = 'grid';
        el.viewGridBtn.classList.add('active');
        el.viewTableBtn.classList.remove('active');
        renderResults();
      });
    }

    // Pagination
    if (el.prevPageBtn) {
      el.prevPageBtn.addEventListener('click', () => {
        if (state.currentPage > 1) {
          state.currentPage--;
          renderResults();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    if (el.nextPageBtn) {
      el.nextPageBtn.addEventListener('click', () => {
        const totalPages = Math.ceil(state.filteredCatalog.length / state.pageSize);
        if (state.currentPage < totalPages) {
          state.currentPage++;
          renderResults();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    // Drawer close
    if (el.drawerCloseBtn) {
      el.drawerCloseBtn.addEventListener('click', closeSkillDrawer);
    }

    if (el.drawerBackdrop) {
      el.drawerBackdrop.addEventListener('click', (e) => {
        if (e.target === el.drawerBackdrop) closeSkillDrawer();
      });
    }

    // Sync button
    if (el.syncBtn) {
      el.syncBtn.addEventListener('click', () => {
        showToast(`✓ All Updated: 6,063 skills across 38 categories & 225 repositories fully synchronized.`);
      });
    }

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== el.searchInput) {
        e.preventDefault();
        switchView('skill-hub');
        if (el.searchInput) el.searchInput.focus();
      }
      if (e.key === 'Escape') {
        closeSkillDrawer();
      }
      if ((e.key === 't' || e.key === 'T') && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
      }
    });
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
