const fs = require('fs');
const path = require('path');

const SKILL_SEA_DIR = path.resolve(__dirname, '..');
const AGENTS_DIR = path.resolve(SKILL_SEA_DIR, '..');
const WORKSPACE_DIR = path.resolve(AGENTS_DIR, '..');

const CATEGORIES_INDEX_PATH = path.join(AGENTS_DIR, 'category', 'categories_index.json');
const SKILLS_INDEX_PATH = path.join(AGENTS_DIR, 'library', 'skills_index.json');
const UPSTREAMS_PATH = path.join(AGENTS_DIR, 'library', 'upstreams.json');
const AGENTS_SKILLS_DIR = path.join(AGENTS_DIR, 'skills');
const HOT_SKILLS_DIR = path.join(WORKSPACE_DIR, '.agent', 'skills');

console.log('🔄 Building Skill.Sea Catalog & Repositories from .agents vault...');

// 1. Read Upstreams
let upstreams = {};
if (fs.existsSync(UPSTREAMS_PATH)) {
  try {
    upstreams = JSON.parse(fs.readFileSync(UPSTREAMS_PATH, 'utf8'));
    console.log(`Loaded ${Object.keys(upstreams).length} upstreams`);
  } catch (err) {
    console.error('Error reading upstreams.json:', err.message);
  }
}

// 2. Read Active Hot-Set Skills
const hotSkills = new Set();
function checkSkillsDir(dir) {
  if (fs.existsSync(dir)) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
      if (fs.statSync(path.join(dir, item)).isDirectory()) {
        hotSkills.add(item.toLowerCase());
      }
    }
  }
}
checkSkillsDir(AGENTS_SKILLS_DIR);
checkSkillsDir(HOT_SKILLS_DIR);
console.log(`Identified ${hotSkills.size} active hot-set skills`);

// 3. Read Skills Index
let librarySkills = new Map();
if (fs.existsSync(SKILLS_INDEX_PATH)) {
  try {
    const rawSkills = JSON.parse(fs.readFileSync(SKILLS_INDEX_PATH, 'utf8'));
    for (const s of rawSkills) {
      const key = (s.id || s.name || '').toLowerCase();
      if (key) {
        librarySkills.set(key, s);
      }
    }
    console.log(`Loaded ${librarySkills.size} skills from library/skills_index.json`);
  } catch (err) {
    console.error('Error reading skills_index.json:', err.message);
  }
}

// 4. Read Categories Index
let categoriesData = {};
let categoryMeta = [];
if (fs.existsSync(CATEGORIES_INDEX_PATH)) {
  try {
    const rawCategories = JSON.parse(fs.readFileSync(CATEGORIES_INDEX_PATH, 'utf8'));
    categoriesData = rawCategories.categories || {};
    console.log(`Loaded ${Object.keys(categoriesData).length} categories from categories_index.json`);
  } catch (err) {
    console.error('Error reading categories_index.json:', err.message);
  }
}

// Category emoji/icon map
const categoryIcons = {
  '3d-web-threejs': 'cube',
  'academic-writing-publishing': 'book',
  'algorithms-logic': 'binary',
  'architecture-system-design': 'building',
  'audio-voice-sound': 'volume',
  'autonomous-agents-hermes': 'robot',
  'backend-api-design': 'server',
  'business-finance-accounting': 'coin',
  'business-sales-crm': 'briefcase',
  'business-strategy-legal': 'scale',
  'cloudflare-edge': 'cloud',
  'code-quality-refactoring': 'sparkles',
  'core-antigravity-protocols': 'flame',
  'data-engineering-ml': 'database',
  'database-nosql-serverless': 'bolt',
  'database-sql-relational': 'table',
  'devops-docker-cicd': 'brand-docker',
  'diagrams-technical-visuals': 'chart-dots',
  'frontend-motion-animation': 'movie',
  'frontend-ui-components': 'layout-grid',
  'frontend-visual-taste': 'palette',
  'fullstack-web-frameworks': 'browser',
  'git-version-control': 'brand-git',
  'graphics-branding-design': 'brush',
  'lobehub-ecosystem': 'circles-relation',
  'mobile-ios-android': 'device-mobile',
  'multi-agent-orchestration': 'network',
  'productivity-workspace-tools': 'checkbox',
  'programming-languages-core': 'code',
  'prompt-llm-engineering': 'message-code',
  'scientific-bio-data': 'dna',
  'security-compliance-auth': 'shield-check',
  'security-vulnerability-audit': 'bug',
  'terminal-system-tools': 'terminal-2',
  'testing-playwright-e2e': 'browser-check',
  'testing-unit-tdd': 'checklist',
  'video-motion-production': 'video',
  'web3-smart-contracts': 'brand-ethereum'
};

// 5. Build Unified Skills Catalog
const catalogMap = new Map();
const repoMap = new Map();

function ensureRepo(repoSlug) {
  if (!repoMap.has(repoSlug)) {
    const upstreamInfo = upstreams[repoSlug] || {};
    let url = upstreamInfo.url || null;
    let upstream = upstreamInfo.upstream || repoSlug;

    if (!url && repoSlug.includes('/')) {
      url = `https://github.com/${repoSlug}`;
    } else if (!url && !repoSlug.startsWith('#')) {
      url = `https://github.com/SeaXen/agentskills/tree/main/library/${repoSlug}`;
    }

    let cloneCmd = url && url.startsWith('https://github.com/') ? `git clone ${url}.git` : `python .agents/library/activate_skill.py activate <skill>`;

    repoMap.set(repoSlug, {
      id: repoSlug,
      name: repoSlug,
      type: upstreamInfo.type || (repoSlug.startsWith('#') ? 'local-collection' : 'github-repo'),
      upstream: upstream,
      url: url,
      cloneCmd: cloneCmd,
      skillsCount: 0,
      skills: [],
      hotCount: 0,
      categories: new Set()
    });
  }
  return repoMap.get(repoSlug);
}

// Ensure all upstreams are seeded into repoMap
for (const [rSlug, rData] of Object.entries(upstreams)) {
  ensureRepo(rSlug);
}

// Process category index skills
for (const [catSlug, catObj] of Object.entries(categoriesData)) {
  const catTitle = catObj.title || catSlug;
  const cleanTitle = catTitle.replace(/^[^\w\s]+/, '').trim();

  categoryMeta.push({
    slug: catSlug,
    title: catTitle,
    cleanTitle: cleanTitle,
    icon: categoryIcons[catSlug] || 'folder',
    count: (catObj.skills || []).length
  });

  for (const s of (catObj.skills || [])) {
    const skillName = s.name;
    const lowerName = skillName.toLowerCase();
    const repoSlug = s.repo || 'community';
    const upstreamInfo = upstreams[repoSlug] || {};
    const githubUrl = upstreamInfo.url || (repoSlug.includes('/') ? `https://github.com/${repoSlug}` : `https://github.com/SeaXen/agentskills/tree/main/library/${repoSlug}/skills/${skillName}`);

    const libMatch = librarySkills.get(lowerName) || {};

    const description = s.description || libMatch.description || `Specialized skill for ${cleanTitle}.`;
    const isActive = hotSkills.has(lowerName);

    const activationCmd = libMatch.activation_cmd || `python .agents/library/activate_skill.py activate ${skillName}`;
    const linkCmd = libMatch.link_cmd || `python .agents/library/activate_skill.py link ${skillName}`;
    const relativePath = libMatch.path || `category/${catSlug}/${skillName}`;

    // Update repo stats
    const repoEntry = ensureRepo(repoSlug);
    repoEntry.skillsCount++;
    repoEntry.skills.push({ name: skillName, isActive });
    if (isActive) repoEntry.hotCount++;
    repoEntry.categories.add(cleanTitle);

    if (!catalogMap.has(lowerName)) {
      catalogMap.set(lowerName, {
        id: lowerName,
        name: skillName,
        category: catSlug,
        categoryTitle: catTitle,
        cleanCategory: cleanTitle,
        categoryIcon: categoryIcons[catSlug] || 'folder',
        repository: repoSlug || 'community',
        githubUrl: githubUrl,
        description: description.trim(),
        isActive: isActive,
        activationCmd: activationCmd,
        linkCmd: linkCmd,
        path: relativePath,
        starsEstimate: calculateStarScore(repoSlug, isActive)
      });
    }
  }
}

// Add remaining skills from librarySkills not present in category index
for (const [lowerName, s] of librarySkills.entries()) {
  if (!catalogMap.has(lowerName)) {
    const catSlug = s.category || 'core-antigravity-protocols';
    const repoSlug = s.repository || 'community';
    const upstreamInfo = upstreams[repoSlug] || {};
    const githubUrl = upstreamInfo.url || (repoSlug.includes('/') ? `https://github.com/${repoSlug}` : `https://github.com/SeaXen/agentskills/tree/main/library/${repoSlug}/skills/${s.name}`);
    const isActive = hotSkills.has(lowerName);

    const repoEntry = ensureRepo(repoSlug);
    repoEntry.skillsCount++;
    repoEntry.skills.push({ name: s.name, isActive });
    if (isActive) repoEntry.hotCount++;
    repoEntry.categories.add(catSlug.replace(/-/g, ' '));

    catalogMap.set(lowerName, {
      id: lowerName,
      name: s.name || lowerName,
      category: catSlug,
      categoryTitle: catSlug,
      cleanCategory: catSlug.replace(/-/g, ' '),
      categoryIcon: categoryIcons[catSlug] || 'folder',
      repository: repoSlug || 'community',
      githubUrl: githubUrl,
      description: (s.description || '').trim(),
      isActive: isActive,
      activationCmd: s.activation_cmd || `python .agents/library/activate_skill.py activate ${s.name}`,
      linkCmd: s.link_cmd || `python .agents/library/activate_skill.py link ${s.name}`,
      path: s.path || `library/${repoSlug}/skills/${s.name}`,
      starsEstimate: calculateStarScore(repoSlug, isActive)
    });
  }
}

function calculateStarScore(repo, isActive) {
  let score = 100;
  if (isActive) score += 500;
  if (repo.includes('anthropics')) score += 800;
  if (repo.includes('antigravity')) score += 950;
  if (repo.includes('obra')) score += 750;
  if (repo.includes('addieosmani')) score += 600;
  if (repo.includes('vercel')) score += 700;
  if (repo.includes('cloudflare')) score += 650;
  let hash = 0;
  for (let i = 0; i < repo.length; i++) {
    hash = (hash << 5) - hash + repo.charCodeAt(i);
    hash |= 0;
  }
  return score + (Math.abs(hash) % 400);
}

// Convert map to array and assign rank
const catalog = Array.from(catalogMap.values());
catalog.sort((a, b) => {
  if (a.isActive && !b.isActive) return -1;
  if (!a.isActive && b.isActive) return 1;
  return b.starsEstimate - a.starsEstimate;
});

// Assign ranks
catalog.forEach((item, idx) => {
  item.rank = idx + 1;
});

// Category summary sorting
categoryMeta.sort((a, b) => b.count - a.count);

// Convert repoMap to array
const repositories = Array.from(repoMap.values()).map(r => ({
  ...r,
  categories: Array.from(r.categories)
}));
repositories.sort((a, b) => b.skillsCount - a.skillsCount);

// Ensure output directory exists
const DATA_DIR = path.join(SKILL_SEA_DIR, 'data');
if (!fs.existsSync(DATA_DIR)) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
}

// Write files
fs.writeFileSync(path.join(DATA_DIR, 'catalog.json'), JSON.stringify(catalog, null, 2));
fs.writeFileSync(path.join(DATA_DIR, 'categories.json'), JSON.stringify(categoryMeta, null, 2));
fs.writeFileSync(path.join(DATA_DIR, 'repositories.json'), JSON.stringify(repositories, null, 2));

const stats = {
  totalSkills: catalog.length,
  totalCategories: categoryMeta.length,
  totalRepositories: repositories.length,
  activeHotSetCount: hotSkills.size,
  lastUpdated: new Date().toISOString()
};
fs.writeFileSync(path.join(DATA_DIR, 'stats.json'), JSON.stringify(stats, null, 2));

console.log(`✅ Catalog & Repositories built successfully!`);
console.log(`   - Total skills: ${stats.totalSkills}`);
console.log(`   - Total categories: ${stats.totalCategories}`);
console.log(`   - Total repositories: ${stats.totalRepositories}`);
console.log(`   - Active Hot-Set: ${stats.activeHotSetCount}`);
