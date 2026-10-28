---
name: portable-deploy-qa
description: (Legacy alias for app-production-readiness) Build portable apps (any stack - TypeScript, Python, Go, Rust) for localhost, Docker, Vercel, Netlify, Railway, Render, Fly.io, Cloudflare Free plan, then run an adaptive 21-gate production-readiness review. Automatically forwards to the full 21-gate app-production-readiness skill.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash
category: devops-docker-cicd
---

# Portable Deploy + QA (Upgraded to app-production-readiness)

> ⚠️ **UPGRADE NOTICE**: This skill has been superseded by the full 21-gate production-readiness engine located at:
> `@[d:\Repo\.agents\skills\app-production-readiness]`

## Forwarding Instructions

When this skill is triggered, immediately forward execution to **`app-production-readiness`**:

1. Refer to the canonical skill definition in [.agents/skills/app-production-readiness/SKILL.md](file:///d:/Repo/.agents/skills/app-production-readiness/SKILL.md).
2. Run the one-command orchestrator:
   ```bash
   python .agents/skills/app-production-readiness/scripts/review.py --root <app_root> --serve [--fix]
   ```
3. To bootstrap and check local browser/Lighthouse dependencies:
   ```bash
   python .agents/skills/app-production-readiness/scripts/bootstrap_env.py
   ```
4. All 21 quality gates, adversarial claim verification, framework profiles, and auto-fixes are maintained in `.agents/skills/app-production-readiness/`.
