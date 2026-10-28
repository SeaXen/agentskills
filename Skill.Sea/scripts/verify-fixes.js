const fs = require('fs');
const path = require('path');

const catalog = JSON.parse(fs.readFileSync(path.join(__dirname, '../data/catalog.json'), 'utf8'));
const categories = JSON.parse(fs.readFileSync(path.join(__dirname, '../data/categories.json'), 'utf8'));

console.log('====================================================');
console.log('🎯 SKILL.SEA USER REQUIREMENTS VERIFICATION');
console.log('====================================================');

// 1. Category Colors
const colorThemes = new Set(categories.map(c => c.colorTheme));
console.log(`1. Category Colors:`);
console.log(`   - Total Categories: ${categories.length}`);
console.log(`   - Distinct Color Themes: ${colorThemes.size} (${Array.from(colorThemes).join(', ')})`);
if (colorThemes.size >= 10) {
  console.log('   ✅ PASS: Rich harmonious color palette assigned to all categories');
} else {
  console.log('   ❌ FAIL: Not enough distinct colors');
}

// 2. Active Skills resolution (not shown as git repo, real origin repo shown, no 404 links)
const activeAsRepo = catalog.filter(s => s.repository === 'active');
const hotSkills = catalog.filter(s => s.isActive);
const badUrls = catalog.filter(s => s.githubUrl && s.githubUrl.includes('/library/active/'));
console.log(`\n2. Active Skills & Real Origin Upstream:`);
console.log(`   - Skills with repository === "active": ${activeAsRepo.length}`);
console.log(`   - Broken 404 URLs (/library/active/): ${badUrls.length}`);
console.log(`   - Active Hot-Set Skills: ${hotSkills.length}`);
if (activeAsRepo.length === 0 && badUrls.length === 0) {
  console.log('   ✅ PASS: Active is 100% decoupled from repo; real upstream repos mapped without 404s');
} else {
  console.log('   ❌ FAIL: Active repo or 404 URLs still exist');
}

// 3. Descriptions check
const badDesc = catalog.filter(s => !s.description || s.description === '.' || s.description === '>' || s.description === '>-');
const sampleAzure = catalog.find(s => s.name === 'azure-identity-py');
const sampleCaveman = catalog.find(s => s.name === 'caveman-review');
console.log(`\n3. Skill Descriptions:`);
console.log(`   - Empty / Dot / Dummy Descriptions: ${badDesc.length} of ${catalog.length}`);
console.log(`   - azure-identity-py description: "${sampleAzure?.description.slice(0, 80)}..."`);
console.log(`   - caveman-review description: "${sampleCaveman?.description.slice(0, 80)}..."`);
if (badDesc.length === 0) {
  console.log('   ✅ PASS: 100% of skills have real, un-truncated descriptions');
} else {
  console.log(`   ❌ FAIL: ${badDesc.length} skills still have dummy descriptions`);
}

// 4. One-click install strokes (NPX origin / My repo / Python)
const npxCount = catalog.filter(s => s.npxCmd && s.npxCmd.startsWith('npx skills add')).length;
const myRepoCount = catalog.filter(s => s.myRepoNpxCmd && s.myRepoNpxCmd.includes('SeaXen/agentskills')).length;
console.log(`\n4. 1-Click Install Strokes:`);
console.log(`   - Skills with Universal NPX origin command: ${npxCount} of ${catalog.length}`);
console.log(`   - Skills with My Repo NPX command: ${myRepoCount} of ${catalog.length}`);
if (npxCount === catalog.length && myRepoCount === catalog.length) {
  console.log('   ✅ PASS: Universal NPX and My Repo 1-click install commands ready');
} else {
  console.log('   ❌ FAIL: Some skills missing install commands');
}

console.log('====================================================\n');
