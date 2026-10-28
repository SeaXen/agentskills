/**
 * Skill.Sea — Comprehensive Verification & Validation Suite
 * Runs automated checks on catalog schema integrity, design tokens,
 * HTTP server functionality, SPA routing, and security confinement boundaries.
 */

const fs = require('fs');
const path = require('path');
const http = require('http');

const ROOT = path.resolve(__dirname, '..');

let errors = 0;
let passed = 0;

function assert(condition, message) {
  if (condition) {
    console.log(`  ✓ ${message}`);
    passed++;
  } else {
    console.error(`  ✗ FAIL: ${message}`);
    errors++;
  }
}

console.log('🧪 Running Skill.Sea Verification Suite...');
console.log('----------------------------------------------------');

// 1. Check Key Files Exist
console.log('1. Checking Core Files');
const requiredFiles = [
  'index.html',
  'server.js',
  'styles/design-tokens.css',
  'styles/main.css',
  'src/app.js',
  'data/catalog.json',
  'data/categories.json',
  'data/repositories.json',
  'data/stats.json',
  'Dockerfile',
  'docker-compose.yml',
  'vercel.json',
  'netlify.toml',
  'railway.json',
  'render.yaml',
  'fly.toml',
  'wrangler.toml',
  'package.json',
  'README.md'
];

requiredFiles.forEach(f => {
  const p = path.join(ROOT, f);
  assert(fs.existsSync(p), `File exists: ${f}`);
});

// 2. Validate Catalog JSON & Schema Uniformity
console.log('\n2. Validating Catalog Data Integrity & Schema');
try {
  const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/catalog.json'), 'utf8'));
  assert(Array.isArray(catalog) && catalog.length >= 6000, `Catalog contains ${catalog.length} items (>= 6000)`);

  let invalidSchemaCount = 0;
  for (let i = 0; i < catalog.length; i++) {
    const item = catalog[i];
    if (!item.id || !item.name || !item.category || !item.activationCmd || !item.npxCmd || !item.myRepoNpxCmd) {
      invalidSchemaCount++;
    }
  }
  assert(invalidSchemaCount === 0, `All ${catalog.length} items satisfy required schema (id, name, category, activationCmd, npxCmd)`);

  const sample = catalog[0];
  assert(sample.activationCmd.startsWith('python'), `Activation command format valid: ${sample.activationCmd}`);
  assert(sample.npxCmd.startsWith('npx skills add'), `NPX command format valid: ${sample.npxCmd}`);
} catch (e) {
  assert(false, `Catalog JSON is valid and parseable: ${e.message}`);
}

// 3. Validate Design Tokens
console.log('\n3. Validating Design Token Values (ExamForge reference)');
try {
  const tokens = fs.readFileSync(path.join(ROOT, 'styles/design-tokens.css'), 'utf8');
  assert(tokens.includes('--teal: #1d9e75'), 'Teal primary color token #1d9e75 verified');
  assert(tokens.includes('--teal-strong: #0f6e56'), 'Teal strong color token #0f6e56 verified');
  assert(tokens.includes('--surface-0: #f9f9f7'), 'Surface 0 warm-gray #f9f9f7 verified');
  assert(tokens.includes('--surface-0: #0b0b0b'), 'Dark mode surface 0 #0b0b0b verified');
} catch (e) {
  assert(false, `Tokens file valid: ${e.message}`);
}

// 4. Test Server Spawn, Routing, Caching & Security Confinement
console.log('\n4. Testing Local HTTP Server & Security Confinement');
const TEST_PORT = 8998;
const serverProc = require('child_process').spawn('node', ['server.js'], {
  cwd: ROOT,
  env: { ...process.env, PORT: String(TEST_PORT), NODE_ENV: 'production' }
});

function httpGet(reqPath) {
  return new Promise((resolve, reject) => {
    const req = http.request({
      hostname: '127.0.0.1',
      port: TEST_PORT,
      path: reqPath,
      method: 'GET'
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ status: res.statusCode, headers: res.headers, body: data }));
    });
    req.on('error', reject);
    req.end();
  });
}

setTimeout(async () => {
  try {
    // 4.1 Root HTML request
    const rootRes = await httpGet('/');
    assert(rootRes.status === 200, `Root returns status 200 (Got ${rootRes.status})`);
    assert(rootRes.headers['content-type'].includes('text/html'), 'Content-Type is text/html');

    // 4.2 Data JSON request & Cache-Control
    const dataRes = await httpGet('/data/stats.json');
    assert(dataRes.status === 200, `Data endpoint returns 200 for /data/stats.json`);
    assert(dataRes.headers['content-type'].includes('application/json'), 'Stats Content-Type is application/json');
    assert(dataRes.headers['cache-control'].includes('public'), 'Production Cache-Control active for static data');

    // 4.3 SPA Client Route Fallback
    const spaRes = await httpGet('/skill-hub');
    assert(spaRes.status === 200, `Clean SPA route /skill-hub resolves to 200 index.html`);
    assert(spaRes.headers['content-type'].includes('text/html'), 'SPA route serves text/html');

    // 4.4 Missing Asset 404
    const notFoundRes = await httpGet('/data/nonexistent-file.json');
    assert(notFoundRes.status === 404, `Missing asset /data/nonexistent-file.json correctly returns 404`);

    // 4.5 Security: Directory Traversal Confinement
    const traversalRes = await httpGet('/scripts/%2e%2e/%2e%2e/package.json');
    assert(traversalRes.status === 403, `Directory traversal attempt correctly blocked with 403 Forbidden`);

    // 4.6 Security: Hidden Dotfile Confinement
    const dotfileRes = await httpGet('/.env');
    assert(dotfileRes.status === 403, `Hidden dotfile access attempt correctly blocked with 403 Forbidden`);

  } catch (err) {
    assert(false, `Server integration test error: ${err.message}`);
  } finally {
    serverProc.kill();
    report();
  }
}, 800);

function report() {
  console.log('----------------------------------------------------');
  if (errors === 0) {
    console.log(`🎉 ALL ${passed} VERIFICATION CHECKS PASSED!`);
    process.exit(0);
  } else {
    console.error(`⚠️ ${errors} checks failed out of ${passed + errors}`);
    process.exit(1);
  }
}
