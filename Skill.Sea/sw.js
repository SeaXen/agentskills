// Skill.Sea Lightweight Offline-First Service Worker
const CACHE_NAME = 'skill-sea-v2.3';
const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/styles/design-tokens.css',
  '/styles/main.css',
  '/src/app.js',
  '/data/stats.json',
  '/data/categories.json',
  '/manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_ASSETS).catch(() => {});
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  // Stale-while-revalidate for local app shell and data
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);

  // Network first for catalog if online, fallback to cache
  if (url.pathname.includes('/data/catalog.json')) {
    event.respondWith(
      fetch(event.request).then((res) => {
        if (res.ok) {
          const clone = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return res;
      }).catch(() => caches.match(event.request))
    );
    return;
  }

  // Cache first with network update for static assets
  event.respondWith(
    caches.match(event.request).then((cached) => {
      const fetchPromise = fetch(event.request).then((networkRes) => {
        if (networkRes.ok && url.origin === location.origin) {
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, networkRes.clone()));
        }
        return networkRes;
      }).catch(() => cached);
      return cached || fetchPromise;
    })
  );
});
