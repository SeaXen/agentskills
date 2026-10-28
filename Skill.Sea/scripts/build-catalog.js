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
const LIB_DIR = path.join(AGENTS_DIR, 'library');

console.log('🔄 Building Skill.Sea Catalog, Categories & Repositories from .agents vault...');

// 1. Read Upstreams
let upstreams = {};
if (fs.existsSync(UPSTREAMS_PATH)) {
  try {
    upstreams = JSON.parse(fs.readFileSync(UPSTREAMS_PATH, 'utf8'));
    console.log(`Loaded ${Object.keys(upstreams).length} upstreams from upstreams.json`);
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

// 3. Helper to Parse SKILL.md Frontmatter & Content Descriptions
function parseSkillDescription(content) {
  if (!content) return '';
  let description = '';

  // 1. Check YAML frontmatter
  const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (fmMatch) {
    const fm = fmMatch[1];
    
    // Multiline folded scalar description: description: [|>"-]*\n  ...
    const multiMatch = fm.match(/description:\s*(?:[\|\>][\-\+]?|["'][\|\>][\-\+]?["'])\r?\n((?:[ \t]+[^\r\n]+(?:\r?\n|$))+)/i);
    if (multiMatch) {
      const lines = multiMatch[1].split(/\r?\n/).map(l => l.trim()).filter(Boolean);
      const combined = lines.join(' ').trim();
      if (combined && !['.', '>', '>-', '|', '|-', '""', "''"].includes(combined)) {
        description = combined;
      }
    }

    // Single line description if multiline didn't match
    if (!description) {
      const singleMatch = fm.match(/description:\s*([^\r\n]+)/i);
      if (singleMatch) {
        let line = singleMatch[1].trim();
        line = line.replace(/^["']|["']$/g, '').trim();
        if (line && !['.', '>', '>-', '|', '|-', '""', "''"].includes(line)) {
          description = line;
        }
      }
    }
  }

  // 2. Fall back to first markdown paragraph after frontmatter/header
  if (!description || ['.', '>', '>-', '|', '|-'].includes(description)) {
    const body = content.replace(/^---\r?\n[\s\S]*?\r?\n---/, '').trim();
    const paragraphs = body.split(/\r?\n\r?\n/).map(p => p.trim()).filter(Boolean);
    for (const p of paragraphs) {
      const clean = p
        .replace(/^#+.*$/gm, '')
        .replace(/^[-*+]\s+/gm, '')
        .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
        .replace(/[`*]/g, '')
        .replace(/[\r\n]+/g, ' ')
        .trim();
      if (clean.length > 20 && !clean.startsWith('```')) {
        description = clean.slice(0, 320);
        break;
      }
    }
  }

  return description.trim();
}

// 4. Pre-Index all SKILL.md files from filesystem to accurately resolve real repos and descriptions
console.log('🔍 Indexing filesystem SKILL.md definitions across library and skills...');
const fsSkillMap = new Map();

if (fs.existsSync(LIB_DIR)) {
  const libRepos = fs.readdirSync(LIB_DIR).filter(r => {
    try {
      return fs.statSync(path.join(LIB_DIR, r)).isDirectory();
    } catch { return false; }
  });

  for (const r of libRepos) {
    const rPath = path.join(LIB_DIR, r);
    // Case A: library/<repo>/skills/<skill>/SKILL.md
    const skillsSub = path.join(rPath, 'skills');
    if (fs.existsSync(skillsSub) && fs.statSync(skillsSub).isDirectory()) {
      const sItems = fs.readdirSync(skillsSub);
      for (const s of sItems) {
        const mdPath = path.join(skillsSub, s, 'SKILL.md');
        if (fs.existsSync(mdPath)) {
          const content = fs.readFileSync(mdPath, 'utf8');
          const desc = parseSkillDescription(content);
          fsSkillMap.set(s.toLowerCase(), {
            name: s,
            repo: r,
            relPath: `library/${r}/skills/${s}`,
            description: desc
          });
        }
      }
    }
    // Case B: library/<repo>/<skill>/SKILL.md
    const directItems = fs.readdirSync(rPath);
    for (const s of directItems) {
      if (s !== 'skills') {
        const mdPath = path.join(rPath, s, 'SKILL.md');
        if (fs.existsSync(mdPath)) {
          const content = fs.readFileSync(mdPath, 'utf8');
          const desc = parseSkillDescription(content);
          if (!fsSkillMap.has(s.toLowerCase())) {
            fsSkillMap.set(s.toLowerCase(), {
              name: s,
              repo: r,
              relPath: `library/${r}/${s}`,
              description: desc
            });
          }
        }
      }
    }
  }
}

// Also check .agents/skills (hot-set files)
if (fs.existsSync(AGENTS_SKILLS_DIR)) {
  const activeItems = fs.readdirSync(AGENTS_SKILLS_DIR);
  for (const s of activeItems) {
    const mdPath = path.join(AGENTS_SKILLS_DIR, s, 'SKILL.md');
    if (fs.existsSync(mdPath)) {
      const content = fs.readFileSync(mdPath, 'utf8');
      const desc = parseSkillDescription(content);
      const lower = s.toLowerCase();
      if (fsSkillMap.has(lower)) {
        // keep library repo, but update description if better
        const existing = fsSkillMap.get(lower);
        if (!existing.description && desc) existing.description = desc;
      } else {
        fsSkillMap.set(lower, {
          name: s,
          repo: 'core-antigravity-kit',
          relPath: `skills/${s}`,
          description: desc
        });
      }
    }
  }
}
console.log(`Indexed ${fsSkillMap.size} skills directly from filesystem SKILL.md files`);

// 5. Read Skills Index from file
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

// 6. Category Icons & Color Palette System
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

const categoryColors = {
  '3d-web-threejs': 'emerald',
  'academic-writing-publishing': 'slate',
  'algorithms-logic': 'teal',
  'architecture-system-design': 'blue',
  'audio-voice-sound': 'rose',
  'autonomous-agents-hermes': 'blue',
  'backend-api-design': 'sky',
  'business-finance-accounting': 'emerald',
  'business-sales-crm': 'amber',
  'business-strategy-legal': 'slate',
  'cloudflare-edge': 'orange',
  'code-quality-refactoring': 'emerald',
  'core-antigravity-protocols': 'amber',
  'data-engineering-ml': 'cyan',
  'database-nosql-serverless': 'amber',
  'database-sql-relational': 'indigo',
  'devops-docker-cicd': 'teal',
  'diagrams-technical-visuals': 'cyan',
  'frontend-motion-animation': 'indigo',
  'frontend-ui-components': 'sky',
  'frontend-visual-taste': 'rose',
  'fullstack-web-frameworks': 'blue',
  'git-version-control': 'orange',
  'graphics-branding-design': 'pink',
  'lobehub-ecosystem': 'teal',
  'mobile-ios-android': 'sky',
  'multi-agent-orchestration': 'indigo',
  'productivity-workspace-tools': 'emerald',
  'programming-languages-core': 'blue',
  'prompt-llm-engineering': 'cyan',
  'scientific-bio-data': 'teal',
  'security-compliance-auth': 'rose',
  'security-vulnerability-audit': 'crimson',
  'terminal-system-tools': 'slate',
  'testing-playwright-e2e': 'emerald',
  'testing-unit-tdd': 'lime',
  'video-motion-production': 'orange',
  'web3-smart-contracts': 'teal'
};

// 7. Read Categories Index
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

// 8. Build Unified Skills Catalog
const catalogMap = new Map();
const repoMap = new Map();

function ensureRepo(repoSlug) {
  // Never create a repo named 'active'
  if (repoSlug === 'active') repoSlug = 'antigravity-awesome-skills';

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
  if (rSlug !== 'active') ensureRepo(rSlug);
}

// Helper to clean descriptions
function cleanDescription(desc) {
  if (!desc) return '';
  desc = desc.trim();
  if (['.', '>', '>-', '|', '|-', '""', "''"].includes(desc)) return '';
  if (desc.startsWith('>-') || desc.startsWith('|-')) {
    desc = desc.slice(2).trim();
  } else if (desc.startsWith('>') || desc.startsWith('|')) {
    desc = desc.slice(1).trim();
  }
  return desc.replace(/^["']|["']$/g, '').trim();
}

// Process category index skills
for (const [catSlug, catObj] of Object.entries(categoriesData)) {
  const catTitle = catObj.title || catSlug;
  const cleanTitle = catTitle.replace(/^[^\w\s]+/, '').trim();
  const colorTheme = categoryColors[catSlug] || 'blue';

  categoryMeta.push({
    slug: catSlug,
    title: catTitle,
    cleanTitle: cleanTitle,
    icon: categoryIcons[catSlug] || 'folder',
    colorTheme: colorTheme,
    count: (catObj.skills || []).length
  });

  for (const s of (catObj.skills || [])) {
    const skillName = s.name;
    const lowerName = skillName.toLowerCase();
    const isActive = hotSkills.has(lowerName);

    // Resolve actual repository (CRITICAL: never allow repo = 'active')
    let repoSlug = s.repo;
    const fsInfo = fsSkillMap.get(lowerName);
    const libMatch = librarySkills.get(lowerName) || {};

    if (!repoSlug || repoSlug === 'active') {
      if (fsInfo && fsInfo.repo && fsInfo.repo !== 'active') {
        repoSlug = fsInfo.repo;
      } else if (libMatch.repository && libMatch.repository !== 'active') {
        repoSlug = libMatch.repository;
      } else {
        repoSlug = 'antigravity-awesome-skills';
      }
    }

    const upstreamInfo = upstreams[repoSlug] || {};
    const upstreamUrl = upstreamInfo.url || (repoSlug.includes('/') ? `https://github.com/${repoSlug}` : null);
    
    // Valid GitHub URL that will NEVER 404
    const githubUrl = upstreamUrl || `https://github.com/SeaXen/agentskills/tree/main/library/${repoSlug}/skills/${skillName}`;

    // Universal 1-Click Install commands
    const npxCmd = upstreamUrl ? `npx skills add ${upstreamUrl}` : `npx skills add https://github.com/SeaXen/agentskills`;
    const myRepoNpxCmd = `npx skills add https://github.com/SeaXen/agentskills`;
    const activationCmd = libMatch.activation_cmd || `python .agents/library/activate_skill.py activate ${skillName}`;
    const linkCmd = libMatch.link_cmd || `python .agents/library/activate_skill.py link ${skillName}`;
    const relativePath = fsInfo?.relPath || libMatch.path || `category/${catSlug}/${skillName}`;

    // Resolve description without any '.' or '>' artifacts
    let description = cleanDescription(fsInfo?.description);
    if (!description) description = cleanDescription(s.description);
    if (!description) description = cleanDescription(libMatch.description);
    if (!description) description = `Specialized skill for ${cleanTitle} automation.`;

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
        colorTheme: colorTheme,
        repository: repoSlug,
        upstreamUrl: upstreamUrl,
        githubUrl: githubUrl,
        description: description,
        isActive: isActive,
        npxCmd: npxCmd,
        myRepoNpxCmd: myRepoNpxCmd,
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
    const colorTheme = categoryColors[catSlug] || 'blue';
    const isActive = hotSkills.has(lowerName);

    let repoSlug = s.repository;
    const fsInfo = fsSkillMap.get(lowerName);
    if (!repoSlug || repoSlug === 'active') {
      if (fsInfo && fsInfo.repo && fsInfo.repo !== 'active') {
        repoSlug = fsInfo.repo;
      } else {
        repoSlug = 'antigravity-awesome-skills';
      }
    }

    const upstreamInfo = upstreams[repoSlug] || {};
    const upstreamUrl = upstreamInfo.url || (repoSlug.includes('/') ? `https://github.com/${repoSlug}` : null);
    const githubUrl = upstreamUrl || `https://github.com/SeaXen/agentskills/tree/main/library/${repoSlug}/skills/${s.name}`;

    const npxCmd = upstreamUrl ? `npx skills add ${upstreamUrl}` : `npx skills add https://github.com/SeaXen/agentskills`;
    const myRepoNpxCmd = `npx skills add https://github.com/SeaXen/agentskills`;
    const activationCmd = s.activation_cmd || `python .agents/library/activate_skill.py activate ${s.name}`;
    const linkCmd = s.link_cmd || `python .agents/library/activate_skill.py link ${s.name}`;
    const relativePath = fsInfo?.relPath || s.path || `library/${repoSlug}/skills/${s.name}`;

    let description = cleanDescription(fsInfo?.description);
    if (!description) description = cleanDescription(s.description);
    if (!description) description = `Specialized skill for ${catSlug.replace(/-/g, ' ')} automation.`;

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
      colorTheme: colorTheme,
      repository: repoSlug,
      upstreamUrl: upstreamUrl,
      githubUrl: githubUrl,
      description: description,
      isActive: isActive,
      npxCmd: npxCmd,
      myRepoNpxCmd: myRepoNpxCmd,
      activationCmd: activationCmd,
      linkCmd: linkCmd,
      path: relativePath,
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
  if (repo.includes('addyosmani')) score += 600;
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

// Convert repoMap to array (clean up, removing empty/invalid repos)
const repositories = Array.from(repoMap.values())
  .filter(r => r.name !== 'active' && r.skillsCount > 0)
  .map(r => ({
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
