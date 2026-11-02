// Skill.Sea Lightweight Offline-First Service Worker
const CACHE_NAME = 'skill-sea-v3.0';
const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/styles/design-tokens.css?v=3.0',
  '/styles/main.css?v=3.0',
  '/src/app.js?v=3.0',
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
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);

  // Network first for all local HTML, CSS, JS, and JSON data
  if (url.origin === location.origin) {
    event.respondWith(
      fetch(event.request).then((networkRes) => {
        if (networkRes.ok) {
          const clone = networkRes.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return networkRes;
      }).catch(() => caches.match(event.request))
    );
    return;
  }

  // Fallback for external assets (CDN fonts/icons)
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});

