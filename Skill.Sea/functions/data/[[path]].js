/**
 * functions/data/[[path]].js
 * Cloudflare Pages Function with R2 Binding & Resilient Static Fallback
 * 
 * Intercepts requests to /data/*
 * 1. Checks Cloudflare R2 bucket binding 'SKILLS_BUCKET' (bucket: skill-sea-vault)
 * 2. If present in R2, streams the object with HTTP ETags (304 support) and edge caching
 * 3. If R2 object is missing or R2 binding is absent, gracefully calls context.next()
 *    to serve the static asset from Cloudflare Pages CDN.
 */

export async function onRequest(context) {
  const { request, env, params } = context;
  const pathParts = params.path;
  const fileName = Array.isArray(pathParts) ? pathParts.join('/') : (pathParts || '');

  // Only GET and HEAD requests
  if (request.method !== 'GET' && request.method !== 'HEAD') {
    return new Response('Method Not Allowed', { status: 405 });
  }

  // 1. Try Cloudflare R2 Storage (SKILLS_BUCKET)
  if (env && env.SKILLS_BUCKET && fileName) {
    try {
      // Look up under data/{fileName} or {fileName}
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

        // Fine-tuned Cache-Control
        if (fileName === 'stats.json') {
          headers.set('Cache-Control', 'public, max-age=60, stale-while-revalidate=300');
        } else if (fileName === 'catalog.json') {
          headers.set('Cache-Control', 'public, max-age=3600, stale-while-revalidate=86400');
        } else {
          headers.set('Cache-Control', 'public, max-age=86400, stale-while-revalidate=604800');
        }

        // Conditional Request (ETag 304 Not Modified)
        const clientEtag = request.headers.get('if-none-match');
        if (clientEtag && clientEtag === object.httpEtag) {
          return new Response(null, { headers, status: 304 });
        }

        return new Response(object.body, { headers });
      }
    } catch (err) {
      // Non-blocking log: fall back smoothly to static asset
      console.warn(`[R2 Fetch Warning] Failed to stream ${fileName} from R2:`, err.message);
    }
  }

  // 2. Resilient Fallback: pass to Cloudflare Pages static CDN asset pipeline
  return context.next();
}
