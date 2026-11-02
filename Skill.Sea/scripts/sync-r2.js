/**
 * scripts/sync-r2.js
 * Automated sync utility to upload Skill.Sea master datasets to Cloudflare R2
 * Bucket: skill-sea-vault
 * Optimized with SHA-256 Hash Caching for instant sub-second verification.
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const BUCKET_NAME = process.env.R2_BUCKET || 'skill-sea-vault';
const DATA_DIR = path.resolve(__dirname, '..', 'data');
const CACHE_FILE = path.join(DATA_DIR, '.r2_sync_cache.json');

const FILES_TO_SYNC = [
  { name: 'catalog.json', cache: 'public, max-age=3600, stale-while-revalidate=86400' },
  { name: 'categories.json', cache: 'public, max-age=86400, stale-while-revalidate=604800' },
  { name: 'repositories.json', cache: 'public, max-age=14400, stale-while-revalidate=86400' },
  { name: 'stats.json', cache: 'public, max-age=60, stale-while-revalidate=300' }
];

console.log(`\n☁️  Skill.Sea Cloudflare R2 Sync Utility`);
console.log(`Target Bucket: ${BUCKET_NAME}`);
console.log(`Source Dir:    ${DATA_DIR}\n`);

if (!fs.existsSync(DATA_DIR)) {
  console.error(`❌ Error: Data directory not found: ${DATA_DIR}`);
  process.exit(1);
}

const ALLOW_OFFLINE = process.argv.includes('--allow-offline') || process.argv.includes('--graceful');
const FORCE_UPLOAD = process.argv.includes('--force');
const npxCmd = process.platform === 'win32' ? 'npx.cmd' : 'npx';

let cache = {};
if (fs.existsSync(CACHE_FILE)) {
  try {
    cache = JSON.parse(fs.readFileSync(CACHE_FILE, 'utf8'));
  } catch {}
}

function getFileHash(filePath) {
  try {
    const data = fs.readFileSync(filePath);
    return crypto.createHash('sha256').update(data).digest('hex');
  } catch {
    return null;
  }
}

let successCount = 0;
let skippedCount = 0;

for (const item of FILES_TO_SYNC) {
  const filePath = path.join(DATA_DIR, item.name);
  if (!fs.existsSync(filePath)) {
    console.warn(`⚠️ Warning: Missing ${item.name}, skipping.`);
    continue;
  }

  const stat = fs.statSync(filePath);
  const sizeMB = (stat.size / (1024 * 1024)).toFixed(2);
  const currentHash = getFileHash(filePath);

  // Check if file is unchanged compared to previous upload
  if (!FORCE_UPLOAD && cache[item.name] && cache[item.name] === currentHash) {
    console.log(`  ✓ ${item.name} (${sizeMB} MB): Unchanged (SHA-256 match), skipping upload.`);
    successCount++;
    skippedCount++;
    continue;
  }

  console.log(`📦 Uploading ${item.name} (${sizeMB} MB)...`);

  try {
    // 1. Upload to data/{name}
    const cmdData = `${npxCmd} wrangler r2 object put "${BUCKET_NAME}/data/${item.name}" --file="${filePath}" --content-type="application/json" --cache-control="${item.cache}" --remote`;
    execSync(cmdData, { stdio: 'inherit', cwd: path.resolve(__dirname, '..') });

    // 2. Also upload to root {name} for direct bucket lookups
    const cmdRoot = `${npxCmd} wrangler r2 object put "${BUCKET_NAME}/${item.name}" --file="${filePath}" --content-type="application/json" --cache-control="${item.cache}" --remote`;
    execSync(cmdRoot, { stdio: 'inherit', cwd: path.resolve(__dirname, '..') });

    cache[item.name] = currentHash;
    console.log(`  ✓ Synced ${item.name} successfully.\n`);
    successCount++;
  } catch (err) {
    console.error(`  ❌ Failed to upload ${item.name}:`, err.message);
    if (ALLOW_OFFLINE) {
      console.warn(`  ⚠️ Graceful offline mode: continuing without crashing.`);
    } else {
      process.exit(1);
    }
  }
}

try {
  fs.writeFileSync(CACHE_FILE, JSON.stringify(cache, null, 2));
} catch {}

if (skippedCount === FILES_TO_SYNC.length) {
  console.log(`⚡ All ${skippedCount} R2 datasets are already fully up to date in bucket '${BUCKET_NAME}'. (0 uploads needed)\n`);
} else if (successCount === FILES_TO_SYNC.length) {
  console.log(`🎉 Sync Complete! ${successCount}/${FILES_TO_SYNC.length} datasets verified/uploaded to R2 '${BUCKET_NAME}'.\n`);
} else {
  console.log(`⚠️ Sync partial: ${successCount}/${FILES_TO_SYNC.length} datasets processed.\n`);
}
