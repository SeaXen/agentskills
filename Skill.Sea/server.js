/**
 * Skill.Sea — High-Performance Universal Static Web Server
 * Zero dependencies — Runs natively on Node.js 18+
 * Hardened Security • Intelligent SPA Routing • Adaptive Asset Caching
 * Compatible with Localhost, Docker, Railway, Render, Fly.io
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const PORT = parseInt(process.env.PORT || '8080', 10);
const HOST = process.env.HOST || '0.0.0.0';
const ROOT = path.resolve(__dirname);
const IS_PROD = process.env.NODE_ENV === 'production';

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.txt': 'text/plain; charset=utf-8'
};

const server = http.createServer((req, res) => {
  // CORS Headers for API/asset friendliness
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  if (req.method !== 'GET' && req.method !== 'HEAD') {
    res.writeHead(405, { 'Content-Type': 'text/plain' });
    res.end('405 Method Not Allowed');
    return;
  }

  // Parse path and query
  const [rawUrlPath] = (req.url || '/').split('?');
  let decodedPath = '';
  try {
    decodedPath = decodeURIComponent(rawUrlPath);
  } catch (err) {
    res.writeHead(400, { 'Content-Type': 'text/plain' });
    res.end('400 Bad Request: Malformed URI');
    return;
  }

  // 1. Strict Security Confinement Check: Instantly deny any directory traversal attempts
  if (/(^|[/\\])\.\.([/\\]|$)/.test(decodedPath)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden: Directory traversal denied');
    return;
  }

  // Normalize path and resolve strictly relative to ROOT
  let cleanPath = path.normalize(decodedPath);
  if (cleanPath === '/' || cleanPath === '\\' || cleanPath === '' || cleanPath === '.') {
    cleanPath = '/index.html';
  }

  // Ensure leading slash for uniform resolution
  if (!cleanPath.startsWith('/') && !cleanPath.startsWith('\\')) {
    cleanPath = '/' + cleanPath;
  }

  let filePath = path.resolve(ROOT, '.' + cleanPath);

  // Secondary Confinement Check: Ensure resolved path strictly starts with ROOT
  if (!filePath.startsWith(ROOT) || filePath.includes('\0')) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden: Access Denied');
    return;
  }

  // Block sensitive files / dotfiles (e.g., .env, .git)
  const baseName = path.basename(filePath);
  if (baseName.startsWith('.') && baseName !== '.well-known') {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden: Hidden file access denied');
    return;
  }

  // If path is a directory, serve its index.html
  if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
    filePath = path.join(filePath, 'index.html');
  }

  // 2. Intelligent SPA Routing vs 404 for Static Assets
  if (!fs.existsSync(filePath)) {
    const hasExtension = Boolean(path.extname(cleanPath));
    if (!hasExtension) {
      // Clean SPA client-side route -> Fallback to index.html
      filePath = path.join(ROOT, 'index.html');
    } else {
      // Explicit asset/data request that does not exist -> Return genuine 404
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found');
      return;
    }
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found');
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';
    const acceptEncoding = req.headers['accept-encoding'] || '';

    // 3. Adaptive Caching Strategy
    if (ext === '.html') {
      res.setHeader('Cache-Control', 'no-cache, must-revalidate');
    } else if (IS_PROD) {
      // Production: cache versioned data and static assets
      res.setHeader('Cache-Control', 'public, max-age=3600, stale-while-revalidate=86400');
    } else {
      // Local development: no-cache for instant live reloading
      res.setHeader('Cache-Control', 'no-cache, must-revalidate');
    }

    res.setHeader('Content-Type', contentType);

    if (req.method === 'HEAD') {
      res.setHeader('Content-Length', stats.size);
      res.writeHead(200);
      res.end();
      return;
    }

    // Gzip compression for text & json assets
    const canGzip = /\b(gzip)\b/.test(acceptEncoding) && /^(text\/|application\/javascript|application\/json|image\/svg\+xml)/.test(contentType);

    if (canGzip) {
      res.setHeader('Content-Encoding', 'gzip');
      const rawStream = fs.createReadStream(filePath);
      const gzipStream = zlib.createGzip({ level: 6 });
      res.writeHead(200);
      rawStream.pipe(gzipStream).pipe(res);
    } else {
      res.setHeader('Content-Length', stats.size);
      res.writeHead(200);
      fs.createReadStream(filePath).pipe(res);
    }
  });
});

server.listen(PORT, HOST, () => {
  console.log(`=======================================================`);
  console.log(`🌊 Skill.Sea Server running at http://${HOST}:${PORT}`);
  console.log(`   - Static root: ${ROOT}`);
  console.log(`   - Environment: ${process.env.NODE_ENV || 'production'}`);
  console.log(`   - Security: Path Confinement & SPA Fallback Active`);
  console.log(`=======================================================`);
});

// Graceful termination
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully...');
  server.close(() => process.exit(0));
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully...');
  server.close(() => process.exit(0));
});
