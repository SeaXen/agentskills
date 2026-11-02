/**
 * Skill.Sea Production Cloudflare Worker
 * 
 * Features:
 * - Dynamic Cloudflare R2 streaming for /data/* (catalog.json, categories.json, repositories.json, stats.json)
 * - Zero-latency static asset serving via Cloudflare Worker Static Assets (env.ASSETS)
 * - Automatic SPA fallback to /index.html for client-side hash and path routing
 * - Instant cache-invalidation headers (max-age=0, must-revalidate) for HTML, CSS, and JS
 * - Full ETag (304 Not Modified) and CORS support
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // 1. Dynamic R2 Data Streaming (/data/*)
    if (url.pathname.startsWith('/data/')) {
      const fileName = url.pathname.replace(/^\/data\//, '').trim();

      if (fileName && env.SKILLS_BUCKET) {
        try {
          // Check data/{fileName} or direct {fileName} in R2
          let object = await env.SKILLS_BUCKET.get(`data/${fileName}`);
          if (!object) {
            object = await env.SKILLS_BUCKET.get(fileName);
          }

          if (object) {
            const headers = new Headers();
            object.writeHttpMetadata(headers);
            headers.set('etag', object.httpEtag);
            headers.set('Content-Type', 'application/json; charset=utf-8');
            headers.set('X-Data-Source', 'cloudflare-r2');
            headers.set('Access-Control-Allow-Origin', '*');

            if (fileName === 'stats.json') {
              headers.set('Cache-Control', 'public, max-age=60, stale-while-revalidate=300');
            } else if (fileName === 'catalog.json') {
              headers.set('Cache-Control', 'public, max-age=3600, stale-while-revalidate=86400');
            } else {
              headers.set('Cache-Control', 'public, max-age=86400, stale-while-revalidate=604800');
            }

            // ETag 304 Not Modified
            const clientEtag = request.headers.get('if-none-match');
            if (clientEtag && clientEtag === object.httpEtag) {
              return new Response(null, { headers, status: 304 });
            }

            return new Response(object.body, { headers });
          }
        } catch (err) {
          console.error(`[Worker R2 Error] Failed to stream ${fileName}:`, err);
        }
      }
    }

    // 2. Static Asset Serving via env.ASSETS
    if (env.ASSETS) {
      let response = await env.ASSETS.fetch(request);

      // SPA fallback for clean navigation paths without file extensions
      if (response.status === 404 && request.method === 'GET' && !url.pathname.includes('.')) {
        const indexRequest = new Request(new URL('/', request.url), request);
        response = await env.ASSETS.fetch(indexRequest);
      }

      // Add security & cache headers
      const headers = new Headers(response.headers);
      headers.set('X-Content-Type-Options', 'nosniff');
      headers.set('X-Frame-Options', 'SAMEORIGIN');
      headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');

      // Instant cache revalidation for HTML, CSS, and JS
      const path = url.pathname;
      if (path === '/' || path.endsWith('.html') || path.endsWith('.css') || path.endsWith('.js')) {
        headers.set('Cache-Control', 'public, max-age=0, must-revalidate');
      }

      return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers
      });
    }

    return new Response('Not Found', { status: 404 });
  }
};
