/**
 * Skill.Sea — Verification & Validation Suite
 * Runs automated checks on catalog, tokens, files, and server integrity.
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

// 2. Validate Catalog JSON
console.log('\n2. Validating Catalog Data Integrity');
try {
  const catalog = JSON.parse(fs.readFileSync(path.join(ROOT, 'data/catalog.json'), 'utf8'));
  assert(Array.isArray(catalog) && catalog.length > 3000, `Catalog contains ${catalog.length} items (> 3000)`);
  
  const sample = catalog[0];
  assert(sample.id && sample.name && sample.category && sample.activationCmd, `Sample item has id, name, category, activationCmd`);
  assert(sample.activationCmd.startsWith('python'), `Activation command format valid: ${sample.activationCmd}`);
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

// 4. Test Server Spawn
console.log('\n4. Testing Local HTTP Server');
const serverProc = require('child_process').spawn('node', ['server.js'], {
  cwd: ROOT,
  env: { ...process.env, PORT: '8999' }
});

setTimeout(() => {
  http.get('http://localhost:8999', (res) => {
    assert(res.statusCode === 200, `HTTP server returns status 200 (Got ${res.statusCode})`);
    assert(res.headers['content-type'].includes('text/html'), 'Content-Type is text/html');
    
    // Test data endpoint
    http.get('http://localhost:8999/data/stats.json', (statsRes) => {
      assert(statsRes.statusCode === 200, `Data endpoint returns 200 for stats.json`);
      serverProc.kill();
      report();
    }).on('error', () => {
      assert(false, 'Data endpoint reachable');
      serverProc.kill();
      report();
    });
  }).on('error', (err) => {
    assert(false, `Server reachable: ${err.message}`);
    serverProc.kill();
    report();
  });
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
