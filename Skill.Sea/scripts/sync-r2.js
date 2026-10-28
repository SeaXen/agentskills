/**
 * scripts/sync-r2.js
 * Automated sync utility to upload Skill.Sea master datasets to Cloudflare R2
 * Bucket: skill-sea-vault
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const BUCKET_NAME = process.env.R2_BUCKET || 'skill-sea-vault';
const DATA_DIR = path.resolve(__dirname, '..', 'data');

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

let successCount = 0;

for (const item of FILES_TO_SYNC) {
  const filePath = path.join(DATA_DIR, item.name);
  if (!fs.existsSync(filePath)) {
    console.warn(`⚠️ Warning: Missing ${item.name}, skipping.`);
    continue;
  }

  const stat = fs.statSync(filePath);
  const sizeMB = (stat.size / (1024 * 1024)).toFixed(2);
  console.log(`📦 Uploading ${item.name} (${sizeMB} MB)...`);

  try {
    // 1. Upload to data/{name}
    const cmdData = `npx wrangler r2 object put "${BUCKET_NAME}/data/${item.name}" --file="${filePath}" --content-type="application/json" --cache-control="${item.cache}" --remote`;
    execSync(cmdData, { stdio: 'inherit', cwd: path.resolve(__dirname, '..') });

    // 2. Also upload to root {name} for direct bucket lookups
    const cmdRoot = `npx wrangler r2 object put "${BUCKET_NAME}/${item.name}" --file="${filePath}" --content-type="application/json" --cache-control="${item.cache}" --remote`;
    execSync(cmdRoot, { stdio: 'inherit', cwd: path.resolve(__dirname, '..') });

    console.log(`  ✓ Synced ${item.name} successfully.\n`);
    successCount++;
  } catch (err) {
    console.error(`  ✗ Failed to upload ${item.name}:`, err.message);
    process.exit(1);
  }
}

console.log(`🎉 Sync Complete! ${successCount}/${FILES_TO_SYNC.length} datasets uploaded to R2 '${BUCKET_NAME}'.\n`);
