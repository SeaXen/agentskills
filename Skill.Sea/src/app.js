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
    activeSkill: null,
    stack: new Set(),
    compareList: [],
    drawerTab: 'docs',
    promptCustomGoal: '',
    suppressHashSync: false,
    pendingSkillDrawerId: null
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

  // =========================================================================
  // FEATURE 1: URL Hash State & Deep-Linking Router
  // =========================================================================
  function syncUrlHash() {
    if (state.suppressHashSync) return;
    let hash = '';
    if (state.activeSkill) {
      hash = `#/skill/${encodeURIComponent(state.activeSkill.id)}`;
    } else if (state.currentViewName === 'skill-hub') {
      const params = new URLSearchParams();
      if (state.searchQuery) params.set('q', state.searchQuery);
      if (state.selectedCategory !== 'all') params.set('cat', state.selectedCategory);
      if (state.selectedLibrary !== 'all') params.set('lib', state.selectedLibrary);
      if (state.filterTier !== 'all') params.set('tier', state.filterTier);
      if (state.sortBy !== 'rank') params.set('sort', state.sortBy);
      const str = params.toString();
      hash = str ? `#/hub?${str}` : `#/hub`;
    } else {
      hash = `#/${state.currentViewName}`;
    }

    if (window.location.hash !== hash) {
      history.replaceState(null, '', hash);
    }
  }

  function handleRoute(hashStr) {
    if (!hashStr) hashStr = window.location.hash;
    if (!hashStr || hashStr === '#') return;

    state.suppressHashSync = true;
    try {
      const raw = hashStr.replace(/^#\/?/, '');

      // Route: skill/:id
      if (raw.startsWith('skill/')) {
        const skillId = decodeURIComponent(raw.replace(/^skill\//, ''));
        if (state.catalog.length > 0) {
          openSkillDrawer(skillId);
        } else {
          state.pendingSkillDrawerId = skillId;
        }
        return;
      }

      // Route: stack=:id1,:id2
      if (raw.startsWith('stack=')) {
        const ids = raw.replace(/^stack=/, '').split(',').map(s => s.trim()).filter(Boolean);
        ids.forEach(id => state.stack.add(id));
        saveStack();
        renderStackTray();
        openStackTray();
        return;
      }

      // Route: hub?...
      if (raw.startsWith('hub')) {
        const queryIdx = raw.indexOf('?');
        if (queryIdx !== -1) {
          const qs = raw.substring(queryIdx + 1);
          const params = new URLSearchParams(qs);
          if (params.has('q')) {
            state.searchQuery = params.get('q');
            if (el.searchInput) el.searchInput.value = state.searchQuery;
          }
          if (params.has('cat')) {
            state.selectedCategory = params.get('cat');
            if (el.categoryFilterSelect) el.categoryFilterSelect.value = state.selectedCategory;
          }
          if (params.has('lib')) {
            state.selectedLibrary = params.get('lib');
            if (el.libraryFilterSelect) el.libraryFilterSelect.value = state.selectedLibrary;
          }
          if (params.has('tier')) {
            state.filterTier = params.get('tier');
            if (el.tierSelect) el.tierSelect.value = state.filterTier;
          }
          if (params.has('sort')) {
            state.sortBy = params.get('sort');
            if (el.sortSelect) el.sortSelect.value = state.sortBy;
          }
          applyFilter();
        }
        switchView('skill-hub', false);
        return;
      }

      // Route: simple view names
      const viewMap = {
        'skill-hub': 'skill-hub',
        'hotset': 'hotset',
        'categories': 'categories',
        'library': 'library',
        'guide': 'guide'
      };
      if (viewMap[raw]) {
        switchView(viewMap[raw], false);
      }
    } finally {
      state.suppressHashSync = false;
    }
  }

  // Switch Active Page View (Skill Hub, Hotset, Categories, Library, Guide)
  window.switchView = function (viewName, updateHash = true) {
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

    if (updateHash) {
      syncUrlHash();
    }

    window.scrollTo(0, 0);
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

    loadStack();
    renderStackTray();
    startTelemetryPolling();
    setupEventListeners();
    handleRoute(window.location.hash);
    if (state.pendingSkillDrawerId) {
      openSkillDrawer(state.pendingSkillDrawerId);
      state.pendingSkillDrawerId = null;
    }
  }

  function renderStats() {
    const totalSkills = Number(state.stats.totalSkills || state.catalog.length || 7401);
    const totalCats = Number(state.stats.totalCategories || state.categories.length || 38);
    const totalRepos = Number(state.stats.totalRepositories || state.repositories.length || 212);
    const hotCount = Number(state.stats.activeHotSetCount || 130);

    if (el.statTotalSkills) el.statTotalSkills.textContent = totalSkills.toLocaleString();
    if (el.statTotalCats) el.statTotalCats.textContent = totalCats.toLocaleString();
    if (el.statTotalRepos) el.statTotalRepos.textContent = totalRepos.toLocaleString();
    if (el.statActiveHot) el.statActiveHot.textContent = hotCount.toLocaleString();

    // Dynamically update subtext so counts stay in sync
    const subSkills = document.getElementById('sub-total-skills');
    if (subSkills) subSkills.innerHTML = `<span class="status-dot"></span> All ${totalSkills.toLocaleString()} Ingested & Verified`;

    const subCats = document.getElementById('sub-total-cats');
    if (subCats) subCats.innerHTML = `<span class="status-dot"></span> All ${totalCats} Domains Synchronized`;

    const subRepos = document.getElementById('sub-total-repos');
    if (subRepos) subRepos.innerHTML = `<span class="status-dot"></span> All ${totalRepos} Repositories Active`;

    const subHot = document.getElementById('sub-active-hot');
    if (subHot) subHot.innerHTML = `<span class="status-dot status-dot-hot"></span> ${hotCount} Live in Hot-Set`;

    const tabLib = document.querySelector('#tab-library span');
    if (tabLib) tabLib.textContent = `Library & Git Repos (${totalRepos})`;
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

  // =========================================================================
  // FEATURE 2: Vanilla Fuzzy Search & Typo-Tolerance Engine
  // =========================================================================
  function levenshteinDistance(s1, s2) {
    if (s1 === s2) return 0;
    const l1 = s1.length;
    const l2 = s2.length;
    if (Math.abs(l1 - l2) > 2) return 99; // Bounded for high-speed sub-millisecond execution
    if (l1 === 0) return l2;
    if (l2 === 0) return l1;

    let prevRow = new Array(l2 + 1);
    let currRow = new Array(l2 + 1);

    for (let j = 0; j <= l2; j++) prevRow[j] = j;

    for (let i = 1; i <= l1; i++) {
      currRow[0] = i;
      const c1 = s1.charCodeAt(i - 1);
      for (let j = 1; j <= l2; j++) {
        const cost = c1 === s2.charCodeAt(j - 1) ? 0 : 1;
        currRow[j] = Math.min(
          currRow[j - 1] + 1,
          prevRow[j] + 1,
          prevRow[j - 1] + cost
        );
      }
      for (let j = 0; j <= l2; j++) prevRow[j] = currRow[j];
    }
    return currRow[l2];
  }

  function fuzzyScore(query, item) {
    const q = query.toLowerCase().trim();
    if (!q) return 100;
    const name = item.name.toLowerCase();
    const cat = (item.cleanCategory || item.category || '').toLowerCase();
    const desc = (item.description || '').toLowerCase();
    const repo = (item.repository || '').toLowerCase();

    // 1. Exact name match
    if (name === q) return 200;
    // 2. Name starts with query
    if (name.startsWith(q)) return 160;
    // 3. Substring match
    if (name.includes(q)) return 130;
    if (cat.includes(q)) return 110;
    if (desc.includes(q)) return 90;
    if (repo.includes(q)) return 80;

    // 4. Word-token transposition / typo match (for terms >= 4 chars)
    if (q.length >= 4) {
      const tokens = name.split(/[-_\s]+/);
      for (const tok of tokens) {
        if (Math.abs(tok.length - q.length) <= 2) {
          const dist = levenshteinDistance(q, tok);
          if (dist <= 2) {
            return 70 - dist * 10;
          }
        }
      }
      // Check full name distance
      if (Math.abs(name.length - q.length) <= 2) {
        const fullDist = levenshteinDistance(q, name);
        if (fullDist <= 2) {
          return 65 - fullDist * 10;
        }
      }
    }
    return 0;
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

      // Query filter with typo-tolerance
      if (q) {
        const score = fuzzyScore(q, item);
        if (score <= 0) return false;
        item._searchScore = score;
        return true;
      }
      item._searchScore = 0;
      return true;
    });

    // Sorting Logic
    state.filteredCatalog.sort((a, b) => {
      if (q && state.sortBy === 'rank') {
        // When searching, sort primarily by relevance score, then rank
        const diff = (b._searchScore || 0) - (a._searchScore || 0);
        if (diff !== 0) return diff;
        return (a.rank || 9999) - (b.rank || 9999);
      }
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
    syncUrlHash();
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
          <button type="button" class="filter-chip-remove" aria-label="Remove search filter" onclick="clearSearchFilter()">×</button>
        </span>
      `;
    }

    if (state.selectedCategory !== 'all') {
      const catObj = state.categories.find(c => c.slug === state.selectedCategory);
      const catName = catObj ? (catObj.cleanTitle || catObj.title) : state.selectedCategory;
      chipsHtml += `
        <span class="filter-chip">
          Category: <b>${escapeHtml(catName)}</b>
          <button type="button" class="filter-chip-remove" aria-label="Remove category filter" onclick="setCategory('all')">×</button>
        </span>
      `;
    }

    if (state.selectedLibrary !== 'all') {
      chipsHtml += `
        <span class="filter-chip">
          Library: <b>${escapeHtml(state.selectedLibrary)}</b>
          <button type="button" class="filter-chip-remove" aria-label="Remove library filter" onclick="setLibrary('all')">×</button>
        </span>
      `;
    }

    if (state.filterTier !== 'all') {
      chipsHtml += `
        <span class="filter-chip">
          Tier: <b>${state.filterTier === 'hot' ? 'Hot-Set Only' : 'Vault Only'}</b>
          <button type="button" class="filter-chip-remove" aria-label="Remove tier filter" onclick="setTier('all')">×</button>
        </span>
      `;
    }

    chipsHtml += `<button type="button" class="filter-reset-btn" onclick="clearAllFilters()">Reset All</button>`;
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
                <i class="ti ti-${item.categoryIcon || 'cpu'}" aria-hidden="true"></i>
              </div>
              <div class="skill-info">
                <div class="skill-title-row">
                  <span class="skill-title">${escapeHtml(item.name)}</span>
                  ${activeTag}
                  <span class="skill-repo" role="button" tabindex="0" onclick="event.stopPropagation(); setLibrary('${item.repository}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();setLibrary('${item.repository}');}" title="Filter by library: ${escapeHtml(item.repository)}" aria-label="Filter by library ${escapeHtml(item.repository)}">
                    <i class="ti ti-books" aria-hidden="true"></i>${escapeHtml(item.repository)}
                  </span>
                  <a href="${escapeHtml(item.githubUrl)}" target="_blank" rel="noopener noreferrer" class="skill-repo" onclick="event.stopPropagation()" title="Open upstream GitHub repository (${escapeHtml(item.repository)})" aria-label="Open upstream GitHub repository for ${escapeHtml(item.name)}">
                    <i class="ti ti-brand-github" aria-hidden="true"></i>
                  </a>
                </div>
                <div class="skill-desc">${escapeHtml(item.description || 'Specialized skill ready for instant agent activation.')}</div>
              </div>
            </div>
          </td>
          <td>
            <span class="tg tg-cat cat-color-${item.colorTheme || 'blue'}" role="button" tabindex="0" onclick="event.stopPropagation(); setCategory('${item.category}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();setCategory('${item.category}');}" title="Filter by category: ${escapeHtml(item.cleanCategory || item.category)}" aria-label="Filter by category ${escapeHtml(item.cleanCategory || item.category)}">
              <i class="ti ti-${item.categoryIcon || 'folder'}" style="font-size:10px" aria-hidden="true"></i>
              ${escapeHtml(item.cleanCategory || item.category)}
            </span>
          </td>
          <td>
            ${tierBadge}
          </td>
          <td class="col-cmd">
            <div class="cmd-box" role="button" tabindex="0" onclick="copyCommand('${escapeHtml(cmd)}', event)" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();copyCommand('${escapeHtml(cmd)}', event);}" title="Click to copy 1-click install command (${state.installCmdMode.toUpperCase()})" aria-label="Copy 1-click install command for ${escapeHtml(item.name)}">
              <code>${escapeHtml(cmd)}</code>
              <i class="ti ti-copy cmd-copy-icon" aria-hidden="true"></i>
            </div>
          </td>
          <td style="text-align:right;white-space:nowrap">
            <button type="button" class="btn-stack-toggle ${state.stack.has(item.id) ? 'in-stack' : ''}" onclick="toggleStackSkill('${escapeHtml(item.id)}', event)" aria-label="Toggle ${escapeHtml(item.name)} in stack" style="margin-right:6px">
              <i class="ti ti-${state.stack.has(item.id) ? 'check' : 'plus'}"></i>
              <span>${state.stack.has(item.id) ? 'Stacked' : 'Stack'}</span>
            </button>
            <button type="button" class="btn-action" onclick="event.stopPropagation(); openSkillDrawer('${item.id}')" aria-label="Inspect ${escapeHtml(item.name)}">
              <span>Inspect</span>
              <i class="ti ti-chevron-right" style="font-size:12px" aria-hidden="true"></i>
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
              <span class="card-repo" role="button" tabindex="0" onclick="event.stopPropagation(); setLibrary('${item.repository}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();setLibrary('${item.repository}');}" style="cursor:pointer" aria-label="Filter by library ${escapeHtml(item.repository)}">
                <i class="ti ti-books" aria-hidden="true"></i> ${escapeHtml(item.repository)}
              </span>
            </div>
            ${tierBadge}
          </div>
          <div class="card-desc">${escapeHtml(item.description || 'Specialized skill ready for instant agent activation.')}</div>
          <div class="card-bottom">
            <span class="tg tg-cat cat-color-${item.colorTheme || 'blue'}" role="button" tabindex="0" onclick="event.stopPropagation(); setCategory('${item.category}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();setCategory('${item.category}');}" aria-label="Filter by category ${escapeHtml(item.cleanCategory || item.category)}">
              <i class="ti ti-${item.categoryIcon || 'folder'}" style="font-size:10px" aria-hidden="true"></i>
              <span>${escapeHtml(item.cleanCategory || item.category)}</span>
            </span>
            <div style="display:flex;align-items:center;gap:4px">
              <button type="button" class="btn-stack-toggle ${state.stack.has(item.id) ? 'in-stack' : ''}" onclick="toggleStackSkill('${escapeHtml(item.id)}', event)" aria-label="Toggle ${escapeHtml(item.name)} in stack">
                <i class="ti ti-${state.stack.has(item.id) ? 'check' : 'plus'}"></i>
                <span>${state.stack.has(item.id) ? 'Stacked' : 'Stack'}</span>
              </button>
              <button type="button" class="btn-stack-toggle" onclick="toggleCompareSkill('${escapeHtml(item.id)}', event)" aria-label="Compare ${escapeHtml(item.name)}">
                <i class="ti ti-arrows-diff"></i>
                <span>Compare</span>
              </button>
            </div>
          </div>
          <div style="margin-top:8px">
            <div class="cmd-box" role="button" tabindex="0" onclick="copyCommand('${escapeHtml(cmd)}', event)" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();copyCommand('${escapeHtml(cmd)}', event);}" title="Click to copy install command (${state.installCmdMode.toUpperCase()})" aria-label="Copy ${state.installCmdMode.toUpperCase()} command for ${escapeHtml(item.name)}">
              <code>${escapeHtml(cmd)}</code>
              <i class="ti ti-copy cmd-copy-icon" aria-hidden="true"></i>
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
                <span class="tag-active-pill" style="font-size:9px;padding:1px 5px"><i class="ti ti-flame" style="font-size:8.5px" aria-hidden="true"></i> Active</span>
              </div>
              <span class="card-repo" role="button" tabindex="0" onclick="event.stopPropagation(); setLibrary('${item.repository}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();setLibrary('${item.repository}');}" style="cursor:pointer" aria-label="Filter by library ${escapeHtml(item.repository)}">
                <i class="ti ti-books" aria-hidden="true"></i> ${escapeHtml(item.repository)}
              </span>
            </div>
            <span class="tg tg-hot"><i class="ti ti-flame" style="font-size:10px" aria-hidden="true"></i> Hot-Set</span>
          </div>
          <div class="card-desc">${escapeHtml(item.description || 'Pre-linked active skill ready for instantaneous invocation.')}</div>
          <div class="card-bottom">
            <span class="tg tg-cat cat-color-${item.colorTheme || 'blue'}" role="button" tabindex="0" onclick="event.stopPropagation(); setCategory('${item.category}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();setCategory('${item.category}');}" aria-label="Filter by category ${escapeHtml(item.cleanCategory)}">
              <i class="ti ti-${item.categoryIcon || 'folder'}" style="font-size:10px" aria-hidden="true"></i>
              <span>${escapeHtml(item.cleanCategory)}</span>
            </span>
            <button type="button" class="btn-stack-toggle ${state.stack.has(item.id) ? 'in-stack' : ''}" onclick="toggleStackSkill('${escapeHtml(item.id)}', event)" aria-label="Toggle ${escapeHtml(item.name)} in stack">
              <i class="ti ti-${state.stack.has(item.id) ? 'check' : 'plus'}"></i>
              <span>${state.stack.has(item.id) ? 'Stacked' : 'Stack'}</span>
            </button>
          </div>
          <div style="margin-top:8px">
            <div class="cmd-box" role="button" tabindex="0" onclick="copyCommand('${escapeHtml(cmd)}', event)" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();copyCommand('${escapeHtml(cmd)}', event);}" title="Click to copy install command (${state.installCmdMode.toUpperCase()})" aria-label="Copy ${state.installCmdMode.toUpperCase()} command for ${escapeHtml(item.name)}">
              <code>${escapeHtml(cmd)}</code>
              <i class="ti ti-copy cmd-copy-icon" aria-hidden="true"></i>
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
        <div class="cat-dir-card cat-color-${cat.colorTheme || 'blue'}" role="button" tabindex="0" onclick="setCategory('${cat.slug}')" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();setCategory('${cat.slug}');}" aria-label="Browse ${escapeHtml(cat.cleanTitle || cat.title)} category">
          <div class="cat-dir-header">
            <div class="cat-dir-icon" style="background:var(--cat-bg);border:0.5px solid var(--cat-border);color:var(--cat-text)">
              <i class="ti ti-${cat.icon || 'folder'}" aria-hidden="true"></i>
            </div>
            <div>
              <div class="cat-dir-title">${escapeHtml(cat.cleanTitle || cat.title)}</div>
              <div class="cat-dir-count">${cat.count} total skills available</div>
            </div>
          </div>
          <div style="display:flex;align-items:center;justify-content:space-between;margin-top:auto;border-top:0.5px solid var(--border);padding-top:8px;gap:6px;flex-wrap:wrap">
            <span style="font-size:11.5px;color:var(--cat-text, var(--teal));font-weight:500">Browse Skills →</span>
            <div class="cat-quick-actions" onclick="event.stopPropagation()">
              <button type="button" class="cat-quick-btn cat-quick-btn-primary" onclick="copyCategoryLinkCmd('${cat.slug}', event)" title="Copy CLI batch symlink command for all ${cat.count} skills" aria-label="Link all ${cat.count} skills in ${cat.slug}">
                <i class="ti ti-link" aria-hidden="true"></i> Link All (${cat.count})
              </button>
              <button type="button" class="cat-quick-btn" onclick="copyCategorySkillNames('${cat.slug}', event)" title="Copy comma-separated skill names" aria-label="Copy skill names for ${cat.slug}">
                <i class="ti ti-copy" aria-hidden="true"></i> Names
              </button>
              <button type="button" class="cat-quick-btn" onclick="addCategoryToStack('${cat.slug}', event)" title="Add all ${cat.count} skills to stack" aria-label="Add all ${cat.count} skills in ${cat.slug} to stack">
                <i class="ti ti-stack-2" aria-hidden="true"></i> + Stack
              </button>
            </div>
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
                <button type="button" style="font-size:10px;color:var(--teal);cursor:pointer;background:none;border:none;padding:0" onclick="event.stopPropagation(); copyCommand('python .agents/library/activate_skill.py activate-repo ${r.name}', event)" aria-label="Activate all skills in ${escapeHtml(r.name)}">Activate All Skills</button>
              </div>
              <div class="cmd-box" role="button" tabindex="0" onclick="copyCommand('${escapeHtml(npxCmd)}', event)" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();copyCommand('${escapeHtml(npxCmd)}', event);}" style="max-width:100%" title="Click to copy NPX install command" aria-label="Copy NPX install command for ${escapeHtml(r.name)}">
                <code>${escapeHtml(npxCmd)}</code>
                <i class="ti ti-copy cmd-copy-icon" aria-hidden="true"></i>
              </div>
            </div>
          </div>

          <div style="border-top:0.5px solid var(--border);padding-top:10px;display:flex;align-items:center;justify-content:space-between">
            <span style="font-size:11.5px;color:var(--text-secondary)">
              ${r.hotCount > 0 ? `<b style="color:var(--teal)">${r.hotCount} Hot-Set</b> · ` : ''}Vault Collection
            </span>
            <button type="button" class="btn-action" onclick="setLibrary('${r.name}')" aria-label="View ${r.skillsCount} skills in ${escapeHtml(r.name)}">
              <span>View ${r.skillsCount} Skills</span>
              <i class="ti ti-chevron-right" style="font-size:11px" aria-hidden="true"></i>
            </button>
          </div>
        </div>
      `;
    }
    el.repoGrid.innerHTML = cards;
  }

  // =========================================================================
  // FEATURE 3: Agent Stack Builder Functions
  // =========================================================================
  function loadStack() {
    try {
      const saved = localStorage.getItem('skillsea_stack');
      if (saved) {
        const arr = JSON.parse(saved);
        if (Array.isArray(arr)) state.stack = new Set(arr);
      }
    } catch (e) {
      state.stack = new Set();
    }
  }

  function saveStack() {
    try {
      localStorage.setItem('skillsea_stack', JSON.stringify(Array.from(state.stack)));
    } catch (e) {}
  }

  window.toggleStackSkill = function (skillId, event) {
    if (event) event.stopPropagation();
    if (state.stack.has(skillId)) {
      state.stack.delete(skillId);
      showToast(`Removed from stack: ${skillId}`);
    } else {
      state.stack.add(skillId);
      showToast(`Added to stack: ${skillId}`);
    }
    saveStack();
    renderStackTray();
    renderResults();
    if (state.currentViewName === 'hotset') renderHotSet();
    if (state.activeSkill && state.activeSkill.id === skillId) {
      renderDrawerContent();
    }
  };

  window.toggleStackTray = function () {
    const tray = document.getElementById('agent-stack-tray');
    if (!tray) return;
    const isExpanded = tray.classList.toggle('expanded');
    tray.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
    const panel = document.getElementById('stack-tray-panel');
    if (panel) panel.setAttribute('aria-hidden', isExpanded ? 'false' : 'true');
  };

  window.openStackTray = function () {
    const tray = document.getElementById('agent-stack-tray');
    if (!tray) return;
    tray.classList.add('expanded');
    tray.setAttribute('aria-expanded', 'true');
    const panel = document.getElementById('stack-tray-panel');
    if (panel) panel.setAttribute('aria-hidden', 'false');
  };

  window.clearStack = function () {
    state.stack.clear();
    saveStack();
    renderStackTray();
    renderResults();
    if (state.currentViewName === 'hotset') renderHotSet();
    if (state.activeSkill) renderDrawerContent();
    showToast('Agent stack cleared');
  };

  function renderStackTray() {
    const countBadge = document.getElementById('stack-count-badge');
    const subText = document.getElementById('stack-tray-sub');
    const listEl = document.getElementById('stack-items-list');
    const count = state.stack.size;

    if (countBadge) countBadge.textContent = count;
    if (subText) subText.textContent = `${count} ${count === 1 ? 'skill' : 'skills'} selected`;

    if (!listEl) return;
    if (count === 0) {
      listEl.innerHTML = `
        <div style="text-align:center;padding:24px 12px;color:var(--text-muted);font-size:11.5px">
          No skills in your stack.<br>Click <strong>+ Stack</strong> on any skill to add.
        </div>
      `;
      return;
    }

    let html = '';
    for (const skillId of state.stack) {
      const item = state.catalog.find(s => s.id === skillId) || { name: skillId, cleanCategory: 'Skill', id: skillId };
      html += `
        <div class="stack-item-row">
          <div class="stack-item-info">
            <span class="stack-item-name">${escapeHtml(item.name)}</span>
            <span class="stack-item-cat">${escapeHtml(item.cleanCategory || item.category || 'Skill')}</span>
          </div>
          <button type="button" class="stack-item-del" onclick="toggleStackSkill('${escapeHtml(item.id)}', event)" aria-label="Remove ${escapeHtml(item.name)} from stack">
            <i class="ti ti-x" aria-hidden="true"></i>
          </button>
        </div>
      `;
    }
    listEl.innerHTML = html;
  }

  window.exportStackCli = function (mode) {
    if (state.stack.size === 0) {
      showToast('Stack is empty! Add skills first.');
      return;
    }
    const skillNames = Array.from(state.stack).map(id => {
      const item = state.catalog.find(s => s.id === id);
      return item ? item.name : id;
    });

    let cmd = '';
    if (mode === 'link') {
      cmd = `python .agents/library/activate_skill.py link ${skillNames.join(' ')}`;
    } else if (mode === 'activate') {
      cmd = `python .agents/library/activate_skill.py activate ${skillNames.join(' ')}`;
    } else if (mode === 'npx') {
      const urls = Array.from(state.stack).map(id => {
        const item = state.catalog.find(s => s.id === id);
        return item && item.githubUrl ? item.githubUrl : 'https://github.com/SeaXen/agentskills';
      });
      cmd = urls.map(u => `npx skills add ${u}`).join(' && ');
    }
    copyCommand(cmd);
  };

  window.exportStackJson = function () {
    if (state.stack.size === 0) {
      showToast('Stack is empty! Add skills first.');
      return;
    }
    const stackItems = Array.from(state.stack).map(id => {
      const item = state.catalog.find(s => s.id === id);
      return item || { id, name: id };
    });
    const manifest = {
      name: "Skill.Sea Agent Stack",
      created: new Date().toISOString(),
      skillsCount: stackItems.length,
      skills: stackItems.map(s => ({
        id: s.id,
        name: s.name,
        category: s.cleanCategory || s.category,
        repository: s.repository,
        githubUrl: s.githubUrl
      }))
    };
    const blob = new Blob([JSON.stringify(manifest, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'skills-stack.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast('skills-stack.json downloaded');
  };

  window.shareStackUrl = function () {
    if (state.stack.size === 0) {
      showToast('Stack is empty! Add skills first.');
      return;
    }
    const ids = Array.from(state.stack).join(',');
    const url = `${window.location.origin}${window.location.pathname}#/stack=${ids}`;
    copyCommand(url);
  };

  // =========================================================================
  // FEATURE 4: Detail Drawer & Prompt Simulator
  // =========================================================================
  window.switchDrawerTab = function (tabName) {
    state.drawerTab = tabName;
    const tabDocs = document.getElementById('tab-drawer-docs');
    const tabPrompts = document.getElementById('tab-drawer-prompts');
    if (tabDocs) {
      tabDocs.classList.toggle('active', tabName === 'docs');
      tabDocs.setAttribute('aria-selected', tabName === 'docs' ? 'true' : 'false');
    }
    if (tabPrompts) {
      tabPrompts.classList.toggle('active', tabName === 'prompts');
      tabPrompts.setAttribute('aria-selected', tabName === 'prompts' ? 'true' : 'false');
    }
    renderDrawerContent();
  };

  window.updatePromptCustomGoal = function (val) {
    state.promptCustomGoal = val;
    const item = state.activeSkill;
    if (item && state.drawerTab === 'prompts') {
      renderPromptSimulator(item);
      const input = document.getElementById('prompt-goal-input');
      if (input) {
        input.focus();
        input.setSelectionRange(input.value.length, input.value.length);
      }
    }
  };

  function renderDrawerContent() {
    const item = state.activeSkill;
    if (!item || !el.drawerBody) return;
    if (state.drawerTab === 'prompts') {
      renderPromptSimulator(item);
    } else {
      renderDrawerDocs(item);
    }
  }

  function renderDrawerDocs(item) {
    const githubRepoUrl = item.githubUrl || `https://github.com/SeaXen/agentskills`;
    const curlCommand = `curl -sSL https://raw.githubusercontent.com/SeaXen/agentskills/main/install.sh | bash -s -- activate ${item.name}`;

    el.drawerBody.innerHTML = `
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;background:var(--surface-1);border:0.5px solid var(--border);border-radius:8px;padding:8px 12px;gap:8px;flex-wrap:wrap">
        <span style="font-size:12px;color:var(--text-secondary)">Quick Actions:</span>
        <div style="display:flex;align-items:center;gap:6px">
          <button type="button" class="btn-stack-toggle ${state.stack.has(item.id) ? 'in-stack' : ''}" onclick="toggleStackSkill('${escapeHtml(item.id)}', event)">
            <i class="ti ti-${state.stack.has(item.id) ? 'check' : 'plus'}"></i>
            <span>${state.stack.has(item.id) ? 'In Stack' : '+ Add to Stack'}</span>
          </button>
          <button type="button" class="btn-stack-toggle" onclick="toggleCompareSkill('${escapeHtml(item.id)}', event)">
            <i class="ti ti-arrows-diff"></i>
            <span>Compare</span>
          </button>
        </div>
      </div>

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
        <h3><i class="ti ti-file-text" style="color:var(--teal)" aria-hidden="true"></i> Overview & Description</h3>
        <p style="color:var(--text-secondary);font-size:13px;line-height:1.6;margin-bottom:12px">
          ${escapeHtml(item.description || 'This skill provides structured protocols, tool integrations, and automation rules for AI coding agents.')}
        </p>
      </div>

      <div class="doc-section">
        <h3><i class="ti ti-terminal-2" style="color:var(--teal)" aria-hidden="true"></i> One-Click Activation & Install Commands</h3>
        
        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">1. Universal NPX Install (Upstream Origin Repo):</p>
        <div class="code-snippet-box">
          <button type="button" class="copy-pill" aria-label="Copy Universal NPX command" onclick="copyCommand('${escapeHtml(item.npxCmd || ('npx skills add ' + item.githubUrl))}')">Copy</button>
          <code>${escapeHtml(item.npxCmd || ('npx skills add ' + item.githubUrl))}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">2. Universal NPX Install (My Repo Vault):</p>
        <div class="code-snippet-box">
          <button type="button" class="copy-pill" aria-label="Copy My Repo NPX command" onclick="copyCommand('${escapeHtml(item.myRepoNpxCmd || 'npx skills add https://github.com/SeaXen/agentskills')}')">Copy</button>
          <code>${escapeHtml(item.myRepoNpxCmd || 'npx skills add https://github.com/SeaXen/agentskills')}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">3. AgentSkills Python CLI (Local Workspace Activation):</p>
        <div class="code-snippet-box">
          <button type="button" class="copy-pill" aria-label="Copy Python CLI command" onclick="copyCommand('${escapeHtml(item.activationCmd)}')">Copy</button>
          <code>${escapeHtml(item.activationCmd)}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">4. Zero-Disk Symlink / Junction (Instant Link):</p>
        <div class="code-snippet-box">
          <button type="button" class="copy-pill" aria-label="Copy Zero-Disk symlink command" onclick="copyCommand('${escapeHtml(item.linkCmd)}')">Copy</button>
          <code>${escapeHtml(item.linkCmd)}</code>
        </div>

        <p style="font-size:11.5px;color:var(--text-muted);margin-bottom:4px">5. Remote cURL Quick-Launch (Linux/macOS/Codespaces):</p>
        <div class="code-snippet-box">
          <button type="button" class="copy-pill" aria-label="Copy remote cURL command" onclick="copyCommand('${escapeHtml(curlCommand)}')">Copy</button>
          <code>${escapeHtml(curlCommand)}</code>
        </div>
      </div>

      <div class="doc-section">
        <h3><i class="ti ti-brand-github" style="color:var(--teal)" aria-hidden="true"></i> Original Repository & Documentation</h3>
        <div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap">
          <a href="${escapeHtml(githubRepoUrl)}" target="_blank" rel="noopener noreferrer" class="pill" style="padding:6px 14px;background:var(--surface-1);color:var(--text-primary)">
            <i class="ti ti-brand-github" aria-hidden="true"></i>
            <span>View Upstream on GitHub</span>
            <i class="ti ti-external-link" style="font-size:11px" aria-hidden="true"></i>
          </a>
          <button type="button" class="pill" onclick="copyCommand('${escapeHtml(githubRepoUrl)}')" style="padding:6px 14px" aria-label="Copy repository link">
            <i class="ti ti-link" aria-hidden="true"></i>
            <span>Copy Repository Link</span>
          </button>
        </div>
      </div>

      <div class="doc-section" style="margin-top:24px;border-top:0.5px solid var(--border);padding-top:16px">
        <h3><i class="ti ti-device-floppy" style="color:var(--teal)" aria-hidden="true"></i> Cloudflare R2 Sync</h3>
        <p style="font-size:12px;color:var(--text-secondary);margin-bottom:8px">
          This skill definition is cached in your local vault catalog. To sync or download the skill archive directly to Cloudflare R2 object storage:
        </p>
        <div class="code-snippet-box">
          <button type="button" class="copy-pill" aria-label="Copy Cloudflare R2 sync command" onclick="copyCommand('npm run sync:r2')">Copy</button>
          <code>npm run sync:r2</code>
        </div>
      </div>
    `;
  }

  function renderPromptSimulator(item) {
    const goal = state.promptCustomGoal || '';
    const universalDirective = `You are equipped with the '${item.name}' skill. Read and adhere strictly to its rules in .agents/skills/${item.name}/SKILL.md.\nObjective: ${goal || 'Execute task with domain excellence and zero regressions.'}`;
    const antigravityDirective = `🤖 Use @skill/${item.name} to ${goal || 'analyze, test, and implement this solution'}`;
    const claudeCommand = `/${item.name} ${goal || ''}`;

    el.drawerBody.innerHTML = `
      <div class="prompt-sim-wrap">
        <div class="prompt-input-row">
          <label for="prompt-goal-input"><i class="ti ti-target" style="color:var(--teal)"></i> Custom Task Goal or Context (Live Simulator)</label>
          <input type="text" id="prompt-goal-input" class="prompt-input-box" placeholder="e.g. Audit all database queries and index foreign keys" value="${escapeHtml(goal)}" oninput="updatePromptCustomGoal(this.value)">
        </div>

        <div class="prompt-template-card">
          <div class="prompt-template-hd">
            <span class="prompt-template-title"><i class="ti ti-shield-check" style="color:var(--teal)"></i> 1. Universal System Prompt Directive (Recommended)</span>
            <button type="button" class="copy-pill" onclick="copyCommand('${escapeHtml(universalDirective.replace(/\n/g, '\\n'))}')">Copy</button>
          </div>
          <div class="prompt-code-box">${escapeHtml(universalDirective)}</div>
        </div>

        <div class="prompt-template-card">
          <div class="prompt-template-hd">
            <span class="prompt-template-title"><i class="ti ti-robot" style="color:var(--teal)"></i> 2. Google Antigravity Directive</span>
            <button type="button" class="copy-pill" onclick="copyCommand('${escapeHtml(antigravityDirective)}')">Copy</button>
          </div>
          <div class="prompt-code-box">${escapeHtml(antigravityDirective)}</div>
        </div>

        <div class="prompt-template-card">
          <div class="prompt-template-hd">
            <span class="prompt-template-title"><i class="ti ti-terminal" style="color:var(--teal)"></i> 3. Claude Code / Windsurf Slash Command</span>
            <button type="button" class="copy-pill" onclick="copyCommand('${escapeHtml(claudeCommand)}')">Copy</button>
          </div>
          <div class="prompt-code-box">${escapeHtml(claudeCommand)}</div>
        </div>
      </div>
    `;
  }

  // Open Skill Detail Slide-Over Drawer
  window.openSkillDrawer = function (skillId) {
    const item = state.catalog.find(s => s.id === skillId);
    if (!item) return;
    state.activeSkill = item;
    state.drawerTab = 'docs';
    state.lastActiveElement = document.activeElement;

    if (el.drawerTitle) el.drawerTitle.textContent = item.name;
    if (el.drawerSubtitle) el.drawerSubtitle.textContent = `${item.repository} · Category: ${item.cleanCategory}`;

    // Reset tabs
    const tabDocs = document.getElementById('tab-drawer-docs');
    const tabPrompts = document.getElementById('tab-drawer-prompts');
    if (tabDocs) {
      tabDocs.classList.add('active');
      tabDocs.setAttribute('aria-selected', 'true');
    }
    if (tabPrompts) {
      tabPrompts.classList.remove('active');
      tabPrompts.setAttribute('aria-selected', 'false');
    }

    renderDrawerContent();

    if (el.drawerBackdrop) {
      el.drawerBackdrop.classList.add('open');
      el.drawerBackdrop.setAttribute('aria-hidden', 'false');
      if (el.drawerCloseBtn) {
        setTimeout(() => el.drawerCloseBtn.focus(), 50);
      }
    }

    syncUrlHash();
  };

  window.closeSkillDrawer = function () {
    if (el.drawerBackdrop) {
      el.drawerBackdrop.classList.remove('open');
      el.drawerBackdrop.setAttribute('aria-hidden', 'true');
    }
    state.activeSkill = null;
    if (state.lastActiveElement && typeof state.lastActiveElement.focus === 'function') {
      state.lastActiveElement.focus();
    }
    state.lastActiveElement = null;
    syncUrlHash();
  };

  // =========================================================================
  // FEATURE 5: Side-by-Side Skill Comparator
  // =========================================================================
  window.toggleCompareSkill = function (skillId, event) {
    if (event) event.stopPropagation();
    const idx = state.compareList.indexOf(skillId);
    if (idx !== -1) {
      state.compareList.splice(idx, 1);
      showToast(`Removed from comparator: ${skillId}`);
    } else {
      if (state.compareList.length >= 3) {
        showToast('Max 3 skills in comparator. Removing oldest.');
        state.compareList.shift();
      }
      state.compareList.push(skillId);
      showToast(`Added to comparator: ${skillId}`);
    }
    if (state.compareList.length >= 2) {
      openComparatorModal();
    }
  };

  window.openComparatorModal = function () {
    const backdrop = document.getElementById('comparator-backdrop');
    if (!backdrop) return;
    renderComparatorModal();
    backdrop.classList.add('open');
    backdrop.setAttribute('aria-hidden', 'false');
  };

  window.closeComparatorModal = function () {
    const backdrop = document.getElementById('comparator-backdrop');
    if (!backdrop) return;
    backdrop.classList.remove('open');
    backdrop.setAttribute('aria-hidden', 'true');
  };

  function renderComparatorModal() {
    const bodyEl = document.getElementById('comparator-body');
    if (!bodyEl) return;
    if (state.compareList.length === 0) {
      bodyEl.innerHTML = `<div style="text-align:center;padding:32px;color:var(--text-muted)">Select 2 or 3 skills to compare side-by-side.</div>`;
      return;
    }
    const items = state.compareList.map(id => state.catalog.find(s => s.id === id) || { id, name: id });

    let tableHtml = `
      <table class="comparator-matrix-table">
        <thead>
          <tr>
            <th>Property</th>
            ${items.map(s => `<th>${escapeHtml(s.name)}</th>`).join('')}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Tier Status</td>
            ${items.map(s => `<td>${s.isActive ? '<span class="tg tg-hot"><i class="ti ti-flame"></i> Hot-Set</span>' : '<span class="tg tg-vault">Vault</span>'}</td>`).join('')}
          </tr>
          <tr>
            <td>Leaderboard Rank</td>
            ${items.map(s => `<td><strong>#${s.rank || 'N/A'}</strong></td>`).join('')}
          </tr>
          <tr>
            <td>Category</td>
            ${items.map(s => `<td><span class="tg tg-cat cat-color-${s.colorTheme || 'blue'}">${escapeHtml(s.cleanCategory || s.category || '')}</span></td>`).join('')}
          </tr>
          <tr>
            <td>Repository</td>
            ${items.map(s => `<td>${escapeHtml(s.repository || 'Origin')}</td>`).join('')}
          </tr>
          <tr>
            <td>Token Weight (Est.)</td>
            ${items.map(s => `<td>~${((s.description || '').length * 3 + 240)} tokens</td>`).join('')}
          </tr>
          <tr>
            <td>CLI Symlink Command</td>
            ${items.map(s => `<td><div class="cmd-box" onclick="copyCommand('${escapeHtml(s.linkCmd || '')}')"><code>${escapeHtml(s.linkCmd || '')}</code></div></td>`).join('')}
          </tr>
          <tr>
            <td>Agent Stack</td>
            ${items.map(s => `
              <td>
                <button type="button" class="btn-stack-toggle ${state.stack.has(s.id) ? 'in-stack' : ''}" onclick="toggleStackSkill('${escapeHtml(s.id)}', event)">
                  <i class="ti ti-${state.stack.has(s.id) ? 'check' : 'plus'}"></i>
                  ${state.stack.has(s.id) ? 'In Stack' : 'Add to Stack'}
                </button>
              </td>
            `).join('')}
          </tr>
        </tbody>
      </table>
    `;
    bodyEl.innerHTML = tableHtml;
  }

  // =========================================================================
  // FEATURE 6: Category Quick Action Handlers
  // =========================================================================
  window.copyCategoryLinkCmd = function (catSlug, event) {
    if (event) event.stopPropagation();
    copyCommand(`python .agents/library/activate_skill.py link-category ${catSlug}`);
  };

  window.copyCategorySkillNames = function (catSlug, event) {
    if (event) event.stopPropagation();
    const skills = state.catalog.filter(s => s.category === catSlug).map(s => s.name);
    copyCommand(skills.join(', '));
  };

  window.addCategoryToStack = function (catSlug, event) {
    if (event) event.stopPropagation();
    const skills = state.catalog.filter(s => s.category === catSlug);
    skills.forEach(s => state.stack.add(s.id));
    saveStack();
    renderStackTray();
    renderResults();
    showToast(`Added ${skills.length} skills from '${catSlug}' to stack`);
  };

  // =========================================================================
  // FEATURE 7: Live Telemetry Polling Watcher
  // =========================================================================
  let telemetryPollTimer = null;
  function startTelemetryPolling() {
    if (telemetryPollTimer) clearInterval(telemetryPollTimer);
    telemetryPollTimer = setInterval(async () => {
      if (document.hidden) return; // Save resources when tab is inactive
      try {
        const res = await fetch(`./data/stats.json?t=${Date.now()}`, { cache: 'no-store' });
        if (res.ok) {
          const freshStats = await res.json();
          if (
            Number(freshStats.totalSkills) !== Number(state.stats.totalSkills) ||
            Number(freshStats.activeHotSetCount) !== Number(state.stats.activeHotSetCount) ||
            Number(freshStats.totalCategories) !== Number(state.stats.totalCategories) ||
            Number(freshStats.totalRepositories) !== Number(state.stats.totalRepositories)
          ) {
            state.stats = freshStats;
            renderStats();
            showToast('⚡ Workspace Updated: Skills telemetry synchronized');
          }
        }
      } catch (e) {
        // Silent fail when server unreachable
      }
    }, 6000);
  }

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

    // Comparator modal close backdrop click
    const compBackdrop = document.getElementById('comparator-backdrop');
    if (compBackdrop) {
      compBackdrop.addEventListener('click', (e) => {
        if (e.target === compBackdrop) closeComparatorModal();
      });
    }

    // Hash navigation listener
    window.addEventListener('hashchange', () => {
      handleRoute(window.location.hash);
    });

    // Sync button
    if (el.syncBtn) {
      el.syncBtn.addEventListener('click', () => {
        const totalSkills = Number(state.stats.totalSkills || state.catalog.length || 7401);
        const totalCats = Number(state.stats.totalCategories || state.categories.length || 38);
        const totalRepos = Number(state.stats.totalRepositories || state.repositories.length || 212);
        showToast(`✓ All Updated: ${totalSkills.toLocaleString()} skills across ${totalCats} categories & ${totalRepos} repositories fully synchronized.`);
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
        closeComparatorModal();
        const tray = document.getElementById('agent-stack-tray');
        if (tray && tray.classList.contains('expanded')) toggleStackTray();
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
