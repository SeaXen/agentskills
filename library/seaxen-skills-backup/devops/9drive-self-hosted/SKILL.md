---
name: 9drive-self-hosted
description: Deploy 9Drive Google Drive/S3 gateway with Docker, including host-network installs with relocated ports when 80/3306 are already used, and the Dockerfile `tsc: not found` build fix (npm ci --include=dev).
version: 0.1.0
author: Hermes
platforms: [linux]
metadata:
  hermes:
    tags: [Self-Hosted, Docker, Google-Drive, S3, Storage, Gateway, host-network, port-relocation]
---

# 9Drive Self-Hosted

9Drive is a storage gateway web app that connects multiple Google Drive accounts and S3-compatible storage (MinIO, R2, Wasabi, B2, AWS) into one virtual dashboard. Files stream directly through the backend — never stored on the server. Includes quota tracking, virtual folders, file preview, upload routing, and API keys.

This skill covers Docker-based deployment on a Linux host with MySQL, Express/TypeScript backend, and React/Vite frontend.

## When to Use

- Deploy 9Drive on a Linux VPS or homelab with Docker
- Connect multiple Google Drive accounts as a unified storage pool
- Add S3-compatible storage (R2, Wasabi, MinIO, B2) alongside Google Drive
- Route uploads by most-available, round-robin, or priority order
- Need external upload API with API key management

## Prerequisites

- Linux host with Docker and Docker Compose
- Domain or public IP with port 80/443 available
- Google Cloud project with Drive API enabled
- Google OAuth credentials (Client ID, Client Secret)
- MySQL 8+ (included in docker-compose)
- SMTP server for email auth (optional, can use Google-only)

## How to Run

Invoke through the `terminal` tool. Clone the repo, configure `.env`, run `docker compose up -d --build`.

## Quick Reference

| Command | Purpose |
|---------|---------|
| `docker compose up -d --build` | Build and start all services |
| `docker compose logs -f backend` | Follow backend logs |
| `docker compose exec backend npx prisma migrate deploy` | Apply DB migrations |
| `docker compose exec backend npm run seed:google-config` | Seed Google OAuth from env |
| `./update.sh` | Manual update (git pull, rebuild, migrate, PM2 restart) |

## Procedure

### 1. Clone and Prepare

```bash
git clone https://github.com/zenhosta/9drive.git
cd 9drive
cp .env.docker.example .env
```

### 2. Edit `.env` with Required Values

```env
# Database
MYSQL_ROOT_PASSWORD=strong-root-password
MYSQL_DATABASE=9drive

# Frontend/Backend URLs (replace with your domain)
FRONTEND_URL=https://your-domain.com
VITE_API_URL=https://your-domain.com

# Security secrets (generate long random strings)
JWT_ACCESS_SECRET=your-32-char-min-random-secret
TOKEN_ENCRYPTION_KEY=your-32-byte-encryption-key

# Google OAuth (get from Google Cloud Console)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://your-domain.com/connected-accounts/google/callback

# reCAPTCHA (optional, leave empty to disable)
VITE_RECAPTCHA_SITE_KEY=
RECAPTCHA_SECRET_KEY=
```

### 3. Google Cloud Setup

1. Open [Google Cloud Console](https://console.cloud.google.com/)
2. Create/select project
3. **Enable Google Drive API**: APIs & Services → Library → "Google Drive API" → Enable
4. **OAuth Consent Screen**: External → add scopes:
   - `https://www.googleapis.com/auth/drive`
   - `https://www.googleapis.com/auth/userinfo.email`
   - `https://www.googleapis.com/auth/userinfo.profile`
4. Add test users (your Google accounts)
5. **Create OAuth Client**: Web application → authorized origins: `https://your-domain.com` → redirect URI: `https://your-domain.com/connected-accounts/google/callback`
6. Copy Client ID and Secret to `.env`

### 4. Start Containers

```bash
docker compose up -d --build
```

Services:
- Frontend: `https://your-domain.com` (via nginx on port 80/443)
- Backend API: internal port 4000 (proxied by frontend nginx)
- MySQL: internal port 3306

### 5. Seed Google OAuth Config (Optional if Set via UI)

```bash
docker compose exec backend npm run seed:google-config
```

Or configure via Dashboard → Settings → Google Credentials after first login.

### 6. First Login & Drive Connection

1. Open `https://your-domain.com`
2. Register with email/password or **Sign in with Google**
3. Google sign-in auto-connects your first Drive account
4. In Dashboard → Settings → Connect more Drive accounts
5. Add S3 storage in Settings if needed

### 7. Enable HTTPS (Production)

Use a reverse proxy (nginx, Caddy, Traefik) or Cloudflare Tunnel in front of the frontend container on port 80. Update `FRONTEND_URL` and `GOOGLE_REDIRECT_URI` to use `https://`.

## Pitfalls

- **Google Drive API not enabled** → 403 "Google Drive API has not been used"
- **OAuth consent screen not configured** → "access_denied" error 403
- **Test users not added** (while in Testing mode) → blocked sign-in
- **Redirect URI mismatch** → must exactly match `GOOGLE_REDIRECT_URI` in `.env`
- **Prisma migration fails on Windows** → stop dev servers, run `npx prisma generate`
- **Port 3306 conflict** → change MySQL port in `docker-compose.yml` and `DATABASE_URL`
- **Uploads fail >5GB** → increase `MAX_UPLOAD_BYTES` in backend `.env`
- **Google OAuth verification required** for production apps with >100 users
- **`npm run build` fails: `tsc: not found` inside Docker build** → `npm ci` skips devDependencies by default when `NODE_ENV=production` is set by the base image. The backend Dockerfile uses `tsc` (devDep) at build time. Fix: change `npm ci` to `npm ci --include=dev` and use `npx tsc` (not `npm run build`) so devDeps are present. See `references/port-relocation-host-network.md` for the patch.
- **Host network mode + already-used port** → use `references/port-relocation-host-network.md` to find free ports and rewrite compose + frontend nginx + .env URLs consistently.

## Verification

```bash
# Check all containers healthy
docker compose ps

# Verify backend API
curl -s https://your-domain.com/api/health

# Verify frontend loads
curl -s https://your-domain.com | grep -i "9drive"

# Test Google OAuth flow
# Open https://your-domain.com in browser → click "Sign in with Google"
```