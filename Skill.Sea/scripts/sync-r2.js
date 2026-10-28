/**
 * Skill.Sea — Cloudflare R2 Synchronization Utility
 * Syncs the local catalog and skill manifests to Cloudflare R2 Object Storage.
 *
 * Requirements:
 * Cloudflare R2 provides an S3-compatible API.
 * Set the following environment variables (or in .env):
 *   R2_ACCOUNT_ID
 *   R2_ACCESS_KEY_ID
 *   R2_SECRET_ACCESS_KEY
 *   R2_BUCKET_NAME (default: 'skill-sea')
 *   R2_PUBLIC_URL (optional, e.g. https://skills.yourdomain.com)
 */

const fs = require('fs');
const path = require('path');
const https = require('https');
const crypto = require('crypto');

const SKILL_SEA_DIR = path.resolve(__dirname, '..');
const DATA_DIR = path.join(SKILL_SEA_DIR, 'data');

const ACCOUNT_ID = process.env.R2_ACCOUNT_ID;
const ACCESS_KEY_ID = process.env.R2_ACCESS_KEY_ID;
const SECRET_ACCESS_KEY = process.env.R2_SECRET_ACCESS_KEY;
const BUCKET_NAME = process.env.R2_BUCKET_NAME || 'skill-sea-vault';
const ENDPOINT = ACCOUNT_ID ? `${ACCOUNT_ID}.r2.cloudflarestorage.com` : null;

console.log('☁️  Skill.Sea — Cloudflare R2 Sync Tool');
console.log('==================================================');

if (!ACCOUNT_ID || !ACCESS_KEY_ID || !SECRET_ACCESS_KEY) {
  console.log('ℹ️  No Cloudflare R2 credentials detected in environment variables.');
  console.log('');
  console.log('To sync your catalog and skills to Cloudflare R2:');
  console.log('1. Go to Cloudflare Dashboard -> R2 -> Manage R2 API Tokens');
  console.log('2. Create an API token with Object Read & Write permissions');
  console.log('3. Run with environment variables:');
  console.log('   $env:R2_ACCOUNT_ID="your_account_id"');
  console.log('   $env:R2_ACCESS_KEY_ID="your_access_key"');
  console.log('   $env:R2_SECRET_ACCESS_KEY="your_secret_key"');
  console.log('   $env:R2_BUCKET_NAME="skill-sea-vault"');
  console.log('   node scripts/sync-r2.js');
  console.log('');
  console.log('✅ Local catalog is currently fully bundled and operating offline.');
  console.log('   Files ready for R2 upload:');
  ['catalog.json', 'categories.json', 'stats.json'].forEach(f => {
    const p = path.join(DATA_DIR, f);
    if (fs.existsSync(p)) {
      console.log(`   - ${f}: ${(fs.statSync(p).size / 1024).toFixed(1)} KB`);
    }
  });
  console.log('==================================================');
  process.exit(0);
}

// Upload using AWS S3 Signature V4 implementation
async function uploadFile(fileName) {
  const filePath = path.join(DATA_DIR, fileName);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return;
  }

  const fileData = fs.readFileSync(filePath);
  console.log(`📤 Uploading ${fileName} to R2 bucket "${BUCKET_NAME}"...`);

  // AWS SigV4 Auth Headers for S3-compatible R2 upload
  const dateStr = new Date().toISOString().replace(/[:-]|\.\d{3}/g, '');
  const dateStamp = dateStr.slice(0, 8);
  const region = 'auto';
  const service = 's3';
  const host = `${BUCKET_NAME}.${ENDPOINT}`;
  const uriPath = `/${fileName}`;

  const payloadHash = crypto.createHash('sha256').update(fileData).digest('hex');

  const canonicalHeaders = `host:${host}\nx-amz-content-sha256:${payloadHash}\nx-amz-date:${dateStr}\n`;
  const signedHeaders = 'host;x-amz-content-sha256;x-amz-date';

  const canonicalRequest = `PUT\n${uriPath}\n\n${canonicalHeaders}\n${signedHeaders}\n${payloadHash}`;
  const canonicalRequestHash = crypto.createHash('sha256').update(canonicalRequest).digest('hex');

  const credentialScope = `${dateStamp}/${region}/${service}/aws4_request`;
  const stringToSign = `AWS4-HMAC-SHA256\n${dateStr}\n${credentialScope}\n${canonicalRequestHash}`;

  const kDate = crypto.createHmac('sha256', `AWS4${SECRET_ACCESS_KEY}`).update(dateStamp).digest();
  const kRegion = crypto.createHmac('sha256', kDate).update(region).digest();
  const kService = crypto.createHmac('sha256', kRegion).update(service).digest();
  const kSigning = crypto.createHmac('sha256', kService).update('aws4_request').digest();
  const signature = crypto.createHmac('sha256', kSigning).update(stringToSign).digest('hex');

  const authHeader = `AWS4-HMAC-SHA256 Credential=${ACCESS_KEY_ID}/${credentialScope}, SignedHeaders=${signedHeaders}, Signature=${signature}`;

  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: host,
      path: uriPath,
      method: 'PUT',
      headers: {
        'Host': host,
        'Content-Type': 'application/json',
        'Content-Length': fileData.length,
        'x-amz-date': dateStr,
        'x-amz-content-sha256': payloadHash,
        'Authorization': authHeader
      }
    }, (res) => {
      let respData = '';
      res.on('data', chunk => respData += chunk);
      res.on('end', () => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          console.log(`✅ ${fileName} uploaded successfully! (HTTP ${res.statusCode})`);
          resolve();
        } else {
          console.error(`❌ Upload failed for ${fileName}: HTTP ${res.statusCode} — ${respData}`);
          reject(new Error(respData));
        }
      });
    });

    req.on('error', (err) => {
      console.error(`Network error uploading ${fileName}:`, err.message);
      reject(err);
    });

    req.write(fileData);
    req.end();
  });
}

(async () => {
  try {
    await uploadFile('stats.json');
    await uploadFile('categories.json');
    await uploadFile('catalog.json');
    console.log('🎉 All files synced to Cloudflare R2 successfully!');
  } catch (err) {
    console.error('Sync failed:', err.message);
    process.exit(1);
  }
})();
