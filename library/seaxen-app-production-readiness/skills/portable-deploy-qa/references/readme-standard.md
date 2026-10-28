# Production README Standard

Every app README must be a **standalone product document** — a new user should understand what the app is, run it, see it, and deploy it without asking anyone.

## Required structure (in order)

```markdown
# <App Name>

<One-line pitch. What it does and who it is for.>

![App Logo](docs/screenshots/logo.png)          <- optional

> **Status**: Production | Beta | WIP   |  **Stack**: Next.js 15 + TS + Tailwind

## 📸 Screenshots          <- REQUIRED, see rules below

## ✨ Features
- ...

## 🧪 Quick Start
## ⚙️ Configuration (env table)
## 🏗️ Architecture
## 🚀 Deploy
## 📜 Scripts
## 🧭 Troubleshooting
## 🤝 Contributing
## 📄 License
```

## Screenshot rules (MANDATORY)

1. **Real screenshots of the running app.** Never placeholders, never stock images, never a "coming soon" box.
2. **Location**: `docs/screenshots/<slug>.png` (canonical). If the repo already uses another folder, keep it and be consistent within that repo.
3. **Width 1440px**, `deviceScaleFactor=2` → crisp on retina. Full-page for long views.
4. **Minimum 3** shots: hero/home, one key feature in action, one secondary view.
5. **Add a contact sheet** `contact-sheet.png` at the top of the gallery so the reader sees everything at a glance.
6. **Alt text describes the screen**, not the file: `![Dashboard with portfolio chart and holdings table](docs/screenshots/dashboard.png)`.
7. **Captions** under each image: `> Dashboard — live portfolio with PnL chart.`
8. **Keep them small**: target < 500 KB each. If larger, re-capture with `--no-full-page` or compress.
9. **Dark/light**: if the app has themes, capture both and label them.
10. **No secrets/PII** in captured screens. Blur or use a seeded demo account.

### Screenshot block template

```markdown
## 📸 Screenshots

| Home | Dashboard |
|:----:|:---------:|
| ![Home page](docs/screenshots/home.png) | ![Dashboard view](docs/screenshots/dashboard.png) |

> Live views captured from the production build (1440px, 2x).
```

## Env table (REQUIRED)

```markdown
| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PORT` | No | `3000` | HTTP port |
| `DATABASE_URL` | Yes | — | Postgres connection string |
```

Every var in code must appear here; every var here must exist in code.

## Deploy section (REQUIRED — copy from deploy-matrix.md)

Per platform: Docker, Vercel, Netlify, Railway, Render, Fly.io, Cloudflare. Each with copy-paste commands and a link to the free-tier limits.

## Anti-patterns

- ❌ `create-next-app` boilerplate README left in place
- ❌ No screenshots, or a broken image link
- ❌ "Coming soon" for the docs section
- ❌ Env vars documented but not in a table
- ❌ Screenshots of a different app / old UI
- ❌ Missing license or contribution guide
- ✅ One command to run locally
- ✅ A reader can go repo → run → see → deploy with zero questions
