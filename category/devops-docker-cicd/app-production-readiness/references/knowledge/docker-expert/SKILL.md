<!-- Absorbed from the sibling skill 'docker-expert' (D:\Repo\.agents\skills\docker-expert\SKILL.md).
     Kept verbatim so this review skill stays self-contained.
     The sibling skill itself was NOT deleted. -->
---
name: docker-expert
description: Docker containerization and Compose architecture. Use when creating Dockerfiles, optimizing multi-stage builds, managing docker-compose stacks, configuring networking, and securing containerized production environments.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
---

# Docker Expert

> **Production Containerization, Compose Stacks & Container Security**

---

## ðŸ—ï¸ Core Principles

| Principle | Rule |
|-----------|------|
| **Multi-Stage Builds** | Separate build-time dependencies from production runtimes to minimize final image size. |
| **Non-Root Execution** | Never run containers as `root` in production. Always define a dedicated system user. |
| **Layer Caching** | Copy dependency manifests (`package.json`, `requirements.txt`, `Cargo.toml`) and install packages before copying application source code. |
| **Minimal Base Images** | Prefer Alpine, Distroless, or slim Debian images over full distributions. |
| **Explicit Tagging** | Pin base image versions (e.g., `node:20.11-alpine3.19`); never use `:latest` in production. |

---

## ðŸ“‹ Production Multi-Stage Dockerfile Pattern (Node.js Example)

```dockerfile
# Stage 1: Dependencies
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

# Stage 2: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Stage 3: Runner
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules
COPY package*.json ./
USER nodejs
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

---

## ðŸ“‹ Docker Compose Best Practices

- Use `.env` files for environment variables; never hardcode credentials.
- Set container resource limits (`cpus`, `memory`).
- Define explicit health checks (`healthcheck:`) for dependent services (`depends_on: { service: { condition: service_healthy } }`).
- Use named volumes for persistent data and bridge networks for container isolation.

---

## âŒ Anti-Patterns

- âŒ Storing secrets or API keys in `ENV` instructions or Dockerfile layers.
- âŒ Running `npm install` without copying lockfiles.
- âŒ Leaving build tools (compilers, git, devDependencies) in production runtime containers.
- âŒ Skipping `.dockerignore` (causing local `node_modules` or `.git` to copy into build contexts).

