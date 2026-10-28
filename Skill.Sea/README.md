# 🌊 Skill.Sea — Autonomous Agent Skills Vault & Leaderboard

> **An independent directory, leaderboard, and one-click activation suite for 6,063+ AI Agent Skills across 38 functional categories.**  
> Inspired by [skillleaderboard.com](https://www.skillleaderboard.com/) and powered by the **ExamForge Design System** (neutral warm-gray surfaces, hairline borders, and deep teal accents).

---

## 🌟 Overview

**Skill.Sea** provides an ultra-fast, aesthetically refined web interface and CLI workflow to discover, inspect, and install agent skills.

- **6,063+ Skills Tracked**: Ingested directly from official and community AI agent repositories.
- **38 Functional Categories**: From `Code Quality` and `Architecture` to `Cloudflare Edge`, `Web3`, `DevOps`, and `Multi-Agent Orchestration`.
- **225 Upstream Repositories**: Transparent GitHub attribution, stars estimate, and original licenses.
- **130 Hot-Set Skills**: Curated daily-driver skills pre-linked for instantaneous zero-latency agent execution.
- **Universal Multi-Platform Deployment**: Runs out-of-the-box on **Localhost**, **Docker**, **Vercel**, **Netlify**, **Railway**, **Render**, **Fly.io**, or **Cloudflare Pages/Workers (Free Plan)** with optional **Cloudflare R2 Object Storage**.

---

## 🚀 Quick Start (Localhost)

Skill.Sea has **zero third-party runtime dependencies**. All you need is Node.js (or any static HTTP server).

```bash
# 1. Clone or navigate to Skill.Sea
cd .agents/Skill.Sea

# 2. Build or refresh the catalog from your local .agents vault
node scripts/build-catalog.js

# 3. Launch local server
node server.js
```

Open your browser at **[http://localhost:8080](http://localhost:8080)**.

Alternatively, run with Python:
```bash
python -m http.server 8080
```

---

## 🚢 Multi-Platform Deployment Guides

Skill.Sea includes native, verified deployment configurations for all 8 target platforms:

### 1. Docker & Docker Compose
```bash
# Build and run with Docker
docker build -t skill-sea .
docker run -d -p 8080:8080 --name skill-sea skill-sea

# Or with Docker Compose
docker compose up -d
```
Access at `http://localhost:8080`.

---

### 2. Cloudflare Pages & Workers (100% Free Plan)
Deploy directly to Cloudflare's global edge network:

```bash
# Using Wrangler CLI
npx wrangler pages deploy . --project-name=skill-sea
```
*Note: Configured via `wrangler.toml`, `_headers`, and `_redirects`.*

---

### 3. Vercel
Deploy in seconds using the included `vercel.json`:

```bash
npx vercel deploy --prod
```

---

### 4. Netlify
Deploy using the included `netlify.toml`:

```bash
npx netlify deploy --prod --dir=.
```

---

### 5. Railway
Deploy via Railway CLI or by linking your GitHub repository:
- Railway detects the included `railway.json` and `Dockerfile`.
- Set the environment variable `PORT=8080`.

---

### 6. Render
Deploy using the included `render.yaml` Blueprint:
1. Connect your GitHub repository to Render.
2. Select **New Blueprint Instance** and choose `render.yaml`.
3. Render automatically provisions the free web service.

---

### 7. Fly.io
Deploy to Fly's global MicroVM edge using `fly.toml`:

```bash
fly launch
fly deploy
```

---

## ☁️ Cloudflare R2 Remote Storage Sync

Cloudflare R2 allows storing the complete skill catalog and archives in S3-compatible object storage with **zero egress fees**.

### Setup Instructions:
1. In Cloudflare Dashboard, navigate to **R2** -> **Create Bucket** (e.g., `skill-sea-vault`).
2. Go to **Manage R2 API Tokens** and create a token with **Object Read & Write** permissions.
3. Set your environment variables:
   ```bash
   # Windows PowerShell
   $env:R2_ACCOUNT_ID="your_cloudflare_account_id"
   $env:R2_ACCESS_KEY_ID="your_r2_access_key_id"
   $env:R2_SECRET_ACCESS_KEY="your_r2_secret_access_key"
   $env:R2_BUCKET_NAME="skill-sea-vault"

   # Run Sync
   npm run sync:r2
   ```

---

## 💻 How to Install & Use the Skills

Once you find a skill on Skill.Sea, you can activate it in your workspace using multiple methods:

### Method 1: One-Click CLI Activation (Recommended)
From your repository root:
```bash
python .agents/library/activate_skill.py activate <skill-name>
```
*Example:*
```bash
python .agents/library/activate_skill.py activate clean-code
```

### Method 2: Zero-Disk Symlink / Junction
Link the skill directly from the library without duplicating disk space:
```bash
python .agents/library/activate_skill.py link <skill-name>
```

### Method 3: Remote Workspace One-Liner (Codespaces / Linux / macOS)
```bash
curl -sSL https://raw.githubusercontent.com/SeaXen/agentskills/main/install.sh | bash -s -- activate <skill-name>
```

---

## 📂 Vault Structure & 38 Categories

Skill.Sea indexes 38 functional domains from `.agents/category/`:

| Category | Skills Count | Focus |
|---|---|---|
| **Code Quality & Refactoring** | 546 | Clean code, static analysis, refactoring |
| **Frontend UI Components** | 280 | Accessible UI primitives, headless design |
| **Fullstack Web Frameworks** | 240 | Next.js, React, Astro, Vite |
| **DevOps, Docker & CI/CD** | 215 | Containerization, deployment, pipelines |
| **Testing & Playwright** | 190 | E2E, unit tests, TDD patterns |
| **Multi-Agent Orchestration** | 165 | Subagents, planning, workflows |
| **Security & Vulnerability Audit**| 145 | OWASP 2025, red teaming, hardening |
| **Cloudflare Edge** | 110 | Workers, Pages, D1, R2, Vectorize |
| **Database (SQL & Serverless)**| 135 | PostgreSQL, Prisma, Drizzle, SQLite |
| ...and 29 more | 1,500+ | Mobile, 3D/ThreeJS, AI Prompting, etc. |

---

## 🎨 Design Reference & Tokens

Skill.Sea strictly adopts the tokens from `design/reference/design-tokens.css`:
- **Light Surface**: Warm-gray `#f9f9f7`, cards `#ffffff`, hairline dividers `rgba(11,11,11,0.10)`
- **Dark Surface**: Deep neutral `#0b0b0b`, cards `#1a1a19`, hairline dividers `rgba(255,255,255,0.10)`
- **Primary Teal**: `#1d9e75`, Brand `#0f6e56`, Active Pill `rgba(29, 158, 117, 0.16)`
- **Typography**: Clean sans-serif with tabular numbers; weights 400 & 500 exclusively.

---

## 🧪 Verification & Automated Testing

Run the automated verification suite to ensure all links, data files, tokens, and server ports are functioning:

```bash
npm test
```

---

## 📄 License & Attribution

- Built for the **SeaXen AgentSkills Vault** ecosystem ([github.com/SeaXen/agentskills](https://github.com/SeaXen/agentskills)).
- Code and documentation released under the **MIT License**.
- Upstream skill licenses remain with their respective original authors.
