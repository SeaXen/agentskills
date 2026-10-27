#!/usr/bin/env python3
"""Materialise a sample app used to exercise the QA scripts.

Two variants:
  --variant good    a project that should pass the checks
  --variant broken  a project that must fail them (secrets, eval, weak
                    headers, oversized bundle, boilerplate README)

Usage:
  python make_sample_app.py --out /tmp/sample [--variant broken]

The generated app is intentionally small but structurally realistic:
package.json, an Express server with a /healthz route, a built dist/ with
a Vite manifest, platform configs, CI, docs and real PNG screenshots.
"""
from __future__ import annotations

import argparse
import base64
import random
import string
import struct
import sys
import zlib
from pathlib import Path

# A 4x4 PNG, generated so the fixture has REAL image files (not placeholders).
def tiny_png(rgb=(32, 96, 200)) -> bytes:
    w = h = 4
    raw = b"".join(b"\x00" + bytes(rgb) * w for _ in range(h))

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw))
            + chunk(b"IEND", b""))


PACKAGE_JSON = """{
  "name": "sample-app",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite --port 5173",
    "build": "vite build",
    "start": "node server.js",
    "test": "node --test"
  },
  "dependencies": {},
  "devDependencies": {
    "vite": "^5.4.0"
  }
}
"""

# Dependency-free server (node:http only) so the fixture can be served
# live during QA without an npm install step.
SERVER_JS = """import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { randomUUID } from "node:crypto";
import { extname, join, normalize } from "node:path";
import { log } from "./src/logger.js";

const PORT = Number(process.env.PORT) || 3000;
const API_KEY = process.env.API_KEY;
const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".png": "image/png",
  ".xml": "application/xml; charset=utf-8",
  ".txt": "text/plain; charset=utf-8",
};

async function send(req, res, status, body, type = "text/plain; charset=utf-8") {
  const headers = {
    "content-type": type,
    "x-content-type-options": "nosniff",
    "referrer-policy": "strict-origin-when-cross-origin",
    "content-security-policy": "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; base-uri 'self'",
    "x-frame-options": "SAMEORIGIN",
    "cache-control": "public, max-age=0, must-revalidate",
  };
  let payload = Buffer.isBuffer(body) ? body : Buffer.from(body);
  const accept = String(req.headers["accept-encoding"] || "");
  if (payload.length > 200 && /gzip/.test(accept) && !type.startsWith("image/")) {
    const { gzipSync } = await import("node:zlib");
    payload = gzipSync(payload);
    headers["content-encoding"] = "gzip";
    headers["vary"] = "accept-encoding";
  }
  headers["content-length"] = String(payload.length);
  res.writeHead(status, headers);
  res.end(payload);
}

async function serveStatic(req, res, relPath) {
  const safe = normalize(relPath).replace(/^(\\.\\.[/\\\\])+/, "");
  const file = join("dist", safe);
  try {
    const body = await readFile(file);
    const type = TYPES[extname(file)] || "application/octet-stream";
    await send(req, res, 200, body, type);
  } catch {
    await send(req, res, 404, "Not found");
  }
}

const server = createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || "localhost"}`);
  const path = url.pathname;
  const requestId = req.headers["x-request-id"] || randomUUID();
  res.setHeader("x-request-id", requestId);
  log("info", "request", { method: req.method, path, requestId });

  try {
    if (path === "/healthz") {
      await send(req, res, 200, JSON.stringify({ ok: true, apiKeyPresent: Boolean(API_KEY) }),
        "application/json; charset=utf-8");
      return;
    }
    if (path === "/api/items") {
      await send(req, res, 200, JSON.stringify([{ id: 1, name: "widget" }]),
        "application/json; charset=utf-8");
      return;
    }
    if (path === "/api/account/export") {
      await send(req, res, 200, JSON.stringify({ account: "demo", items: [] }),
        "application/json; charset=utf-8");
      return;
    }
    if (path === "/privacy") {
      await send(req, res, 200, await readFile("privacy.md"), TYPES[".txt"]);
      return;
    }
    if (path === "/robots.txt") {
      await send(req, res, 200, "User-agent: *\\nAllow: /\\n", TYPES[".txt"]);
      return;
    }
    if (path === "/favicon.ico") {
      await send(req, res, 200, await readFile("dist/assets/og.png"), "image/png");
      return;
    }
    if (path === "/sitemap.xml") {
      await send(req, res, 200,
        "<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?><urlset xmlns=\\"http://www.sitemaps.org/schemas/sitemap/0.9\\">" +
        "<url><loc>http://localhost:3000/</loc></url><url><loc>http://localhost:3000/pricing</loc></url></urlset>",
        TYPES[".xml"]);
      return;
    }
    if (path === "/") return serveStatic(req, res, "index.html");
    if (path === "/pricing") return serveStatic(req, res, "pricing.html");
    if (path.startsWith("/assets/")) return serveStatic(req, res, path.slice(1));
    await send(req, res, 404, "Not found");
  } catch (err) {
    log("error", "request failed", { message: err.message, path, requestId });
    await send(req, res, 500, "Internal error");
  }
});

server.listen(PORT, () => console.log(`listening on ${PORT}`));
"""

INDEX_HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Sample App - production dashboard</title>
    <meta name="description" content="Sample App is a small production-ready dashboard used to verify the app-production-readiness skill." />
    <meta property="og:title" content="Sample App" />
    <meta property="og:description" content="A small app used to verify the review pipeline." />
    <meta property="og:image" content="/assets/og.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <link rel="canonical" href="http://localhost:3000/" />
    <link rel="stylesheet" href="/assets/app.css" />
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
    <header><nav aria-label="Primary"><a href="/" data-i18n="nav.home">Home</a> <a href="/pricing" data-i18n="nav.pricing">Pricing</a></nav></header>
    <main id="main">
      <h1 data-i18n="hero.title">Sample App</h1>
      <p data-i18n="hero.subtitle">A deliberately small app that satisfies the review gates.</p>
      <img src="/assets/og.png" alt="Sample App dashboard preview" />
    </main>
    <footer><p>MIT licensed</p><a href="/privacy" data-i18n="footer.privacy">Privacy</a></footer>
    <script src="/assets/app.js"></script>
  </body>
</html>
"""

PRICING_HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Pricing - Sample App</title>
    <meta name="description" content="Pricing for Sample App: a free tier and a paid tier, with limits documented for each." />
    <meta property="og:title" content="Pricing - Sample App" />
    <meta property="og:image" content="/assets/og.png" />
    <link rel="canonical" href="http://localhost:3000/pricing" />
    <link rel="stylesheet" href="/assets/app.css" />
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>
    <header><nav aria-label="Primary"><a href="/">Home</a> <a href="/pricing">Pricing</a></nav></header>
    <main id="main">
      <h1>Pricing</h1>
      <p>Free tier: 100 requests per day. When the limit is hit, the fallback is a cached response.</p>
      <img src="/assets/og.png" alt="Pricing table preview" />
    </main>
    <footer><p>MIT licensed</p><a href="/privacy">Privacy</a></footer>
  </body>
</html>
"""

README_GOOD = """# Sample App

A small app used to verify the app-production-readiness review pipeline.

## Screenshots

![Sample App dashboard](docs/screenshots/home.png)

![Pricing page](docs/screenshots/pricing.png)

![Mobile view](docs/screenshots/mobile.png)

## Features

- Runs locally, in Docker and on any free-tier host
- Health endpoint for orchestrators
- Free tier with a documented fallback

## Quick start

```bash
npm install
npm run dev
```

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | HTTP port | `3000` |
| `API_KEY` | Upstream API key | - |

## Deploy

### Docker

```bash
docker build -t sample-app .
docker run -p 3000:3000 sample-app
```

### Vercel

Zero-config: `vercel deploy`.

### Netlify

Zero-config: `netlify deploy --prod`.

### Railway

`railway up` - the start script honours `$PORT`.

### Render

Blueprint in `render.yaml`.

### Fly.io

`fly launch` - `fly.toml` declares the internal port.

### Cloudflare

`wrangler deploy` - the worker entrypoint is behind a flag.

## Free tier and limits

| Service | Free limit | When it breaks | Fallback |
|---------|-----------|----------------|----------|
| Cloudflare Workers | 100k requests/day | Daily cap reached | Static export on a CDN |
| GitHub Actions | 2000 minutes/month | Minutes exhausted | Run the checks locally |

## Testing

```bash
npm test
```

## License

MIT
"""

README_BROKEN = """# sample-app

This is a [Next.js](https://nextjs.org) project bootstrapped with create-next-app.

## Getting Started

Run `npm run dev`.
"""

ENV_EXAMPLE = """# HTTP port
PORT=3000
# Upstream API key
API_KEY=
"""

DOCKERFILE = """FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
ENV PORT=3000
COPY --from=build /app/dist ./dist
COPY package*.json ./
RUN npm ci --omit=dev
COPY server.js ./
USER node
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://127.0.0.1:${PORT}/healthz || exit 1
CMD ["node", "server.js"]
"""

DOCKERIGNORE = """node_modules
dist
.git
.env
"""

VERCEL_JSON = """{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "framework": null
}
"""

NETLIFY_TOML = """[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "DENY"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Content-Security-Policy = "default-src 'self'"
"""

FLY_TOML = """app = "sample-app"
primary_region = "iad"

[build]
  dockerfile = "Dockerfile"

[env]
  PORT = "3000"

[http_service]
  internal_port = 3000
  force_https = true
  auto_stop_machines = "stop"

  [http_service.http_checks]
    interval = "30s"
    timeout = "3s"
    path = "/healthz"
"""

RENDER_YAML = """services:
  - type: web
    name: sample-app
    runtime: node
    plan: free
    buildCommand: npm ci && npm run build
    startCommand: npm start
    healthCheckPath: /healthz
    envVars:
      - key: PORT
        value: 3000
"""

WRANGLER_TOML = """name = "sample-app"
main = "src/worker.js"
compatibility_date = "2024-11-01"

[vars]
ENVIRONMENT = "production"
"""

WORKER_JS = """export default {
  async fetch(request, env) {
    return new Response("ok", { status: 200 });
  },
};
"""

CI_YML = """name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run build
      - run: npm test
"""

TEST_JS = """import test from "node:test";
import assert from "node:assert/strict";

test("pricing page exists", () => {
  assert.ok(true);
});
"""

LICENSE = """MIT License

Copyright (c) 2026 Sample App

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
"""

CONTRIBUTING = """# Contributing

1. Fork the repository
2. Create a branch
3. Run `npm test`
4. Open a pull request
"""

BROKEN_SECRET = """const apiKey = "sk_live_51H8xQ2eZvKYlo2Cabcdefghijklmnop";

export function run() {
  return eval("1 + 1");
}
"""


LOGGER_JS = """/** Minimal structured logger - one JSON object per line. */
export function log(level, message, fields) {
  const extra = fields || {};
  const line = JSON.stringify({
    ts: new Date().toISOString(),
    level,
    message,
    ...extra,
  });
  if (level === "error") console.error(line);
  else console.log(line);
}
"""


APP_CSS = """:root {
  --color-bg: #0f172a;
  --color-surface: #111c33;
  --color-text: #e2e8f0;
  --color-muted: #94a3b8;
  --color-accent: #38bdf8;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --font-sans: system-ui, -apple-system, "Segoe UI", sans-serif;
  --radius: 10px;
}
body {
  font-family: var(--font-sans);
  font-size: 16px;
  line-height: 1.55;
  background: var(--color-bg);
  color: var(--color-text);
  margin: 0;
  padding: 0;
}
h1 { font-size: 2rem; line-height: 1.2; margin-block-end: var(--space-4); }
h2 { font-size: 1.5rem; line-height: 1.3; }
p { font-size: 1rem; max-width: 70ch; }
a { color: var(--color-accent); transition: color 150ms ease-in-out; }
a:hover { color: var(--color-text); }
.skip-link {
  position: absolute;
  inset-inline-start: -9999px;
  top: 0;
  padding: var(--space-3) var(--space-4);
  background: var(--color-surface);
  color: var(--color-text);
}
.skip-link:focus { inset-inline-start: var(--space-2); }
header nav { display: flex; gap: var(--space-2); align-items: center; }
nav a { display: inline-block; padding: var(--space-2) var(--space-3); min-height: 44px; }
main { max-width: 72rem; margin-inline: auto; padding: var(--space-6) var(--space-4); }
footer { padding: var(--space-6) var(--space-4); color: var(--color-muted); }
img { max-width: 100%; height: auto; border-radius: var(--radius); }
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; animation: none !important; }
}
@media (max-width: 40rem) {
  main { padding: var(--space-4) var(--space-3); }
}
"""

I18N_JS = """/** Tiny message catalogue loader - keys are resolved at runtime. */
import en from "../locales/en.json" with { type: "json" };

const catalogues = { en };

export function t(key, locale = "en") {
  const catalogue = catalogues[locale] || catalogues.en;
  return catalogue[key] || key;
}

export function setLocale(locale) {
  document.documentElement.lang = locale;
  document.documentElement.dir = locale === "ar" ? "rtl" : "ltr";
}
"""

APP_JS = """/** Front-end bootstrap: localised copy and explicit UI states. */
import { t } from "./i18n.js";

export const states = { loading: "Loading", empty: "No data yet", error: "Something went wrong" };

export function render(root) {
  root.querySelectorAll("[data-i18n]").forEach((node) => {
    node.textContent = t(node.dataset.i18n);
  });
  if (!root.querySelector("[data-state]")) {
    root.setAttribute("data-state", states.loading);
  }
}
"""

LOCALES_EN = """{
  "hero.title": "Sample App",
  "hero.subtitle": "A deliberately small app that satisfies the review gates.",
  "nav.home": "Home",
  "nav.pricing": "Pricing",
  "footer.privacy": "Privacy"
}
"""

LOCALES_FR = """{
  "hero.title": "Sample App",
  "hero.subtitle": "Une petite application qui respecte les portes de qualite.",
  "nav.home": "Accueil",
  "nav.pricing": "Tarifs",
  "footer.privacy": "Confidentialite"
}
"""

PAYMENTS_JS = """/** Stripe checkout - amounts are integer minor units, webhooks are verified. */
import Stripe from "stripe";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

export async function createCheckoutSession(priceCents, currency, customerId) {
  return stripe.checkout.sessions.create({
    mode: "payment",
    line_items: [{ price_data: { currency, unit_amount: priceCents }, quantity: 1 }],
    customer: customerId,
    success_url: process.env.APP_URL + "/thanks",
    cancel_url: process.env.APP_URL + "/pricing",
  }, { idempotencyKey: `checkout-${customerId}-${priceCents}` });
}

export function verifyWebhook(payload, signature) {
  return stripe.webhooks.constructEvent(payload, signature, process.env.STRIPE_WEBHOOK_SECRET);
}
"""

MAILER_JS = """/** Transactional email through Resend - failures are surfaced, never swallowed. */
import { Resend } from "resend";
import { readFile } from "node:fs/promises";

const resend = new Resend(process.env.RESEND_API_KEY);

export async function sendWelcome(to, name) {
  try {
    const template = await readFile("src/mail-templates/welcome.html", "utf8");
    const response = await resend.emails.send({
      from: process.env.MAIL_FROM,
      to,
      subject: "Welcome to Sample App",
      html: template.replace("{{name}}", name),
    });
    return response;
  } catch (error) {
    console.error("mail send failed", { message: error.message });
    throw error;
  }
}
"""

MAIL_TEMPLATE = """<!doctype html>
<html lang="en">
  <body>
    <h1>Welcome, {{name}}</h1>
    <p>Your workspace is ready.</p>
  </body>
</html>
"""

PRIVACY_MD = """# Privacy Policy

## What we collect
We collect the account e-mail address and the product usage events needed to run the service.

## Why we collect it
To authenticate you, to answer support requests and to keep the service reliable.

## How long we keep it
Account data is retained for the lifetime of the account. You can request deletion at any time and the
data is removed within 30 days.

## Your rights
You have the right to access your data, the right to erasure (delete your data), the right to data
portability and the right to withdraw consent at any time.

## Sharing
We do not sell personal data. Data is processed by our infrastructure providers under a data
processing agreement.

## Contact
privacy@example.com
"""

RULES_MD = """# Business Rules

These are the rules the product owner states. They are the subject of the
domain sign-off: the executable scenarios in `qa/scenarios.json` prove the
code implements them, and a named human confirms they are the intended ones.

## R1 - Health
`GET /healthz` returns 200 with a JSON body. It is used by the deploy
smoke test and by the platform health checks.

## R2 - Items
`GET /api/items` returns a JSON array of items. An empty catalogue is a
valid answer and is not an error.

## R3 - Pricing
`GET /pricing` is a public page. It never requires authentication and it
never renders user data.

## R4 - Privacy
`GET /privacy` serves the privacy policy from `privacy.md`.
"""

MIGRATION_UP = """-- 001 initial schema
CREATE TABLE IF NOT EXISTS items (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

MIGRATION_DOWN = """-- 001 initial schema (rollback)
DROP TABLE IF EXISTS items;
"""

SCHEMA_SQL = """CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

SCENARIOS = """{
  "scenarios": [
    {
      "name": "health endpoint answers",
      "method": "GET",
      "path": "/healthz",
      "expect_status": 200,
      "expect_body_contains": ["ok"]
    },
    {
      "name": "items api returns the seeded widget",
      "method": "GET",
      "path": "/api/items",
      "expect_status": 200,
      "expect_json": { "0.name": "widget" }
    },
    {
      "name": "unknown route is a hard 404",
      "method": "GET",
      "path": "/api/does-not-exist",
      "expect_status": 404
    }
  ]
}
"""

BROKEN_MIGRATION = """-- 002 clean up the old table
DROP TABLE items;
DELETE FROM users;
"""

BROKEN_JS = """/** Legacy module - the old checkout path that never got removed. */
const apiKey = "sk_live_51H8xQ2eZvKYlo2Cabcdefghijklmnop";

export function charge(cardNumber, email) {
  console.log("charging", email, cardNumber);
  fetch("/api/charge", { method: "POST", body: JSON.stringify({ cardNumber }) });
}

export function loadProfile(user) {
  try {
    return fetchUser(user.id);
  } catch (err) {
  }
}

export function verifyWebhook(payload) {
  return JSON.parse(payload);
}
"""

BROKEN_HTML = """<!doctype html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Welcome to our amazing new platform</title>
  </head>
  <body>
    <div>
      <h1>Welcome to our amazing new platform</h1>
      <p>Sign up today and start shipping faster than ever before.</p>
      <input type="email" name="email" />
      <input type="text" name="company" />
      <button>Submit</button>
      <img src="/assets/og.png" />
    </div>
    <script>
      fetch("/api/profile").then(function (r) { return r.json(); });
    </script>
  </body>
</html>
"""


def write(path: Path, content) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content, encoding="utf-8")


def build(out: Path, variant: str = "good") -> Path:
    out.mkdir(parents=True, exist_ok=True)

    if variant == "broken":
        write(out / "package.json",
              PACKAGE_JSON.replace('"name": "sample-app"', '"name": "broken-app"'))
        write(out / "server.js", SERVER_JS)
        write(out / "src" / "broken.js", BROKEN_SECRET)
        write(out / "src" / "logger.js", LOGGER_JS)
        write(out / "README.md", README_BROKEN)
        write(out / ".env", "API_KEY=sk_live_51H8xQ2eZvKYlo2Cabcdefghijklmnop\n")
        write(out / "src" / "worker.js", WORKER_JS)
        # the defects the new gates have to catch
        write(out / "src" / "legacy.js", BROKEN_JS)
        write(out / "locales" / "en.json", '{"hero.title": "Broken app"}\n')
        write(out / "docs" / "rules.md", RULES_MD)
        write(out / "db" / "migrate" / "002_cleanup.sql", BROKEN_MIGRATION)
        write(out / "dist" / "index.html", BROKEN_HTML)
        write(out / "src" / "index.html", BROKEN_HTML)
        # an oversized bundle so the budget check has something to catch.
        # The filler is high-entropy on purpose: repetitive text gzips down to
        # almost nothing and would slip past a gzip-based budget.
        rng = random.Random(20260101)
        alphabet = string.ascii_letters + string.digits
        noise = "".join(rng.choice(alphabet) for _ in range(300_000))
        write(out / "dist" / "assets" / "huge.js", "// filler\n" + noise)
        return out

    write(out / "package.json", PACKAGE_JSON)
    write(out / "server.js", SERVER_JS)
    write(out / "src" / "worker.js", WORKER_JS)
    write(out / "src" / "logger.js", LOGGER_JS)
    write(out / "src" / "app.js", APP_JS)
    write(out / "src" / "i18n.js", I18N_JS)
    write(out / "src" / "payments.js", PAYMENTS_JS)
    write(out / "src" / "mailer.js", MAILER_JS)
    write(out / "src" / "mail-templates" / "welcome.html", MAIL_TEMPLATE)
    write(out / "src" / "index.html", INDEX_HTML)
    write(out / "src" / "pricing.html", PRICING_HTML)
    write(out / "src" / "styles.css", APP_CSS)
    write(out / "locales" / "en.json", LOCALES_EN)
    write(out / "locales" / "fr.json", LOCALES_FR)
    write(out / "privacy.md", PRIVACY_MD)
    write(out / "docs" / "rules.md", RULES_MD)
    write(out / "db" / "migrate" / "001_init.sql", MIGRATION_UP)
    write(out / "db" / "migrate" / "001_init.down.sql", MIGRATION_DOWN)
    write(out / "db" / "schema.sql", SCHEMA_SQL)
    write(out / "qa" / "scenarios.json", SCENARIOS)
    write(out / "dist" / "index.html", INDEX_HTML)
    write(out / "dist" / "pricing.html", PRICING_HTML)
    write(out / "dist" / "assets" / "app.js", "window.__APP_VERSION__='1.0.0';\n")
    write(out / "dist" / "assets" / "app.css", APP_CSS)
    write(out / "dist" / "assets" / "og.png", tiny_png())
    write(out / "dist" / "robots.txt", "User-agent: *\nAllow: /\n")
    write(out / "dist" / "sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
          '<url><loc>http://localhost:3000/</loc></url>'
          '<url><loc>http://localhost:3000/pricing</loc></url></urlset>')
    write(out / "dist" / ".vite" / "manifest.json",
          '{"index.html":{"file":"assets/app.js","isEntry":true,"imports":[]}}')
    write(out / "README.md", README_GOOD)
    write(out / ".env.example", ENV_EXAMPLE)
    write(out / ".gitignore", "node_modules\n.env\ndist\n")
    write(out / "Dockerfile", DOCKERFILE)
    write(out / ".dockerignore", DOCKERIGNORE)
    write(out / "vercel.json", VERCEL_JSON)
    write(out / "netlify.toml", NETLIFY_TOML)
    write(out / "fly.toml", FLY_TOML)
    write(out / "render.yaml", RENDER_YAML)
    write(out / "wrangler.toml", WRANGLER_TOML)
    write(out / "LICENSE", LICENSE)
    write(out / "CONTRIBUTING.md", CONTRIBUTING)
    write(out / ".github" / "workflows" / "ci.yml", CI_YML)
    write(out / "tests" / "app.test.js", TEST_JS)
    write(out / "package-lock.json",
          '{"name":"sample-app","version":"1.0.0","lockfileVersion":3,'
          '"requires":true,"packages":{}}')
    # real screenshots so the README check has genuine images to resolve
    shots = out / "docs" / "screenshots"
    for name in ("home.png", "pricing.png", "mobile.png"):
        write(shots / name, tiny_png((20, 120, 200)))
    write(shots / "contact-sheet.png", tiny_png((10, 10, 10)))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--variant", default="good", choices=["good", "broken"])
    args = ap.parse_args()
    out = build(Path(args.out), args.variant)
    print(f"{args.variant} fixture written to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
