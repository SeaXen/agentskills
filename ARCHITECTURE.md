# Antigravity Kit Architecture

> Comprehensive AI Agent Capability Expansion Toolkit

---

## 📋 Overview

Antigravity Kit is a modular system consisting of:

- **20 Specialist Agents** - Role-based AI personas
- **87 Active Hot-Set Skills** - Curated daily-driver engineering skills - Domain-specific knowledge modules
- **2,031 Library Reserve Skills** - Offline capability archive across 36 repositories (`.agent/library/`)
- **17 Workflows** - Slash command procedures

---

## 🏗️ Directory Structure

```plaintext
.agent/
├── ARCHITECTURE.md          # This file
├── agents/                  # 20 Specialist Agents
├── skills/                  # 87 Active Hot-Set Skills
├── category/                # 16 Functional Category Directories & Navigation Indexes
├── library/                 # 2,031 Offline Reserve Skills (36 repositories) & Activator
├── workflows/               # 17 Slash Commands
├── rules/                   # Global Rules
└── scripts/                 # Master Validation Scripts
```

---

## 🤖 Agents (20)

Specialist AI personas for different domains.

| Agent                    | Focus                      | Skills Used                                                                          |
| ------------------------ | -------------------------- | ------------------------------------------------------------------------------------ |
| `orchestrator`           | Multi-agent coordination   | parallel-agents, behavioral-modes, antigravity-expert                                 |
| `project-planner`        | Discovery, task planning   | brainstorming, plan-writing, grill-me, codebase-design, architecture, antigravity-expert|
| `frontend-specialist`    | Web UI/UX                  | frontend-design, react-best-practices, tailwind-patterns, ui-taste, shadcn, emil-design-eng, animate, impeccable |
| `backend-specialist`     | API, business logic        | api-patterns, nodejs-best-practices, database-design, nestjs-expert, prisma-expert, typescript-expert |
| `database-architect`     | Schema, SQL                | database-design, prisma-expert                                                       |
| `mobile-developer`       | iOS, Android, RN           | mobile-design, ios-design, design-mobile-apps, mobile-native                          |
| `game-developer`         | Game logic, mechanics      | game-development                                                                     |
| `devops-engineer`        | CI/CD, Docker, Cloudflare  | deployment-procedures, docker-expert, cloudflare, wrangler, nextjs-on-cloudflare      |
| `security-auditor`       | Security compliance        | vulnerability-scanner, red-team-tactics                  |
| `penetration-tester`     | Offensive security         | red-team-tactics                                         |
| `test-engineer`          | Testing strategies         | testing-patterns, tdd-workflow, webapp-testing           |
| `debugger`               | Root cause analysis        | systematic-debugging                                     |
| `performance-optimizer`  | Speed, Web Vitals          | performance-profiling                                    |
| `seo-specialist`         | Ranking, visibility        | seo-fundamentals, geo-fundamentals                       |
| `documentation-writer`   | Manuals, docs, research    | documentation-templates, academic-paper, deep-research   |
| `product-manager`        | Requirements, user stories | plan-writing, brainstorming                              |
| `product-owner`          | Strategy, backlog, MVP     | plan-writing, brainstorming                              |
| `qa-automation-engineer` | E2E testing, CI pipelines  | webapp-testing, testing-patterns                         |
| `code-archaeologist`     | Legacy code, refactoring   | clean-code, code-review-checklist                        |
| `explorer-agent`         | Codebase analysis          | -                                                        |

---

## 🧩 Skills (104)

Modular knowledge domains that agents can load on-demand based on task context.

### Frontend & UI

| Skill                    | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| `react-best-practices`   | React & Next.js performance optimization (Vercel - 57 rules)          |
| `web-design-guidelines`  | Web UI audit - 100+ rules for accessibility, UX, performance (Vercel) |
| `tailwind-patterns`      | Tailwind CSS v4 utilities                                             |
| `frontend-design`        | UI/UX patterns, design systems                                        |
| `ui-ux-pro-max`          | 50 styles, 21 palettes, 50 fonts                                      |
| `ui-taste`               | Anti-UI-slop playbooks, visual hierarchy, polish & references (Uizze) |
| `impeccable`             | Anti-cliché UI design system, bold typography, layout rhythm          |
| `design-taste-frontend`  | Anti-slop frontend taste, typography, bold layout                     |
| `shadcn`                 | Official shadcn/ui components, presets, registries & composition      |
| `radix-ui-design-system` | Accessible design systems with Radix UI primitives & tokens           |
| `figma`                  | Figma design context, component implementation & code connect         |

### Backend & API

| Skill                   | Description                    |
| ----------------------- | ------------------------------ |
| `api-patterns`          | REST, GraphQL, tRPC            |
| `nestjs-expert`         | NestJS modules, DI, decorators |
| `nodejs-best-practices` | Node.js async, modules         |
| `python-patterns`       | Python standards, FastAPI      |

### Database

| Skill                            | Description                                                     |
| -------------------------------- | --------------------------------------------------------------- |
| `database-design`                | Schema design, indexing, optimization                           |
| `prisma-expert`                  | Prisma ORM, migrations, relations                               |
| `supabase`                       | Official Supabase Auth, RLS security, Edge functions, Storage   |
| `supabase-postgres-best-practices` | Postgres indexing, connection pooling, RLS query optimization |
| `neon`                           | Serverless Postgres branching, pooling & migrations             |

### TypeScript/JavaScript

| Skill               | Description                         |
| ------------------- | ----------------------------------- |
| `typescript-expert` | Type-level programming, performance |

### Cloud & Infrastructure

| Skill                   | Description               |
| ----------------------- | ------------------------- |
| `docker-expert`         | Containerization, Compose |
| `deployment-procedures` | CI/CD, deploy workflows   |
| `server-management`     | Infrastructure management |

### Testing & Quality

| Skill                   | Description                                                |
| ----------------------- | ---------------------------------------------------------- |
| `testing-patterns`      | Jest, Vitest, strategies                                   |
| `webapp-testing`        | E2E, Playwright                                            |
| `playwright-cli`        | Microsoft Playwright CLI execution & browser automation     |
| `break-ui`              | Stress-test UI components with edge-case and worst-case data|
| `tdd-workflow`          | Test-driven development                                    |
| `code-review-checklist` | Code review standards                                      |
| `lint-and-validate`     | Linting, validation                                        |

### Security

| Skill                   | Description              |
| ----------------------- | ------------------------ |
| `vulnerability-scanner` | Security auditing, OWASP |
| `red-team-tactics`      | Offensive security       |

### Architecture & Planning

| Skill                | Description                                                            |
| -------------------- | ---------------------------------------------------------------------- |
| `app-builder`        | Full-stack app scaffolding                                             |
| `architecture`       | System design patterns                                                 |
| `plan-writing`       | Task planning, breakdown                                               |
| `brainstorming`      | Socratic questioning protocol                                          |
| `grill-me`           | Relentless Socratic interview to sharpen plans & unearth edge cases    |
| `grill-with-docs`    | Discovery interview that auto-generates ADRs and glossary documentation|
| `grilling`           | Stress-test user decisions and architectural trade-offs                |
| `codebase-design`    | Shared vocabulary for designing deep modules and AI-navigable seams    |
| `domain-modeling`    | Domain models, ubiquitous language, and ADR records                    |
| `antigravity-expert` | Antigravity platform, customizations, skills, rules, hooks, subagents   |

### Mobile

| Skill                | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| `mobile-design`      | Mobile UI/UX patterns                                           |
| `ios-design`         | Native iOS UI/UX, SwiftUI/UIKit/RN, Apple HIG & audits (Uizze)   |
| `design-mobile-apps` | Sleek mobile app screen workflows and visual patterns           |
| `mobile-native`      | Touch feedback, safe area, notch, and native mobile web craft   |

### Game Development

| Skill              | Description           |
| ------------------ | --------------------- |
| `game-development` | Game logic, mechanics |

### SEO & Growth

| Skill              | Description                   |
| ------------------ | ----------------------------- |
| `seo-fundamentals` | SEO, E-E-A-T, Core Web Vitals |
| `geo-fundamentals` | GenAI optimization            |

### Shell/CLI

| Skill                | Description               |
| -------------------- | ------------------------- |
| `bash-linux`         | Linux commands, scripting |
| `powershell-windows` | Windows PowerShell        |

### Other

| Skill                     | Description               |
| ------------------------- | ------------------------- |
| `clean-code`              | Coding standards (Global) |
| `behavioral-modes`        | Agent personas            |
| `parallel-agents`         | Multi-agent patterns      |
| `mcp-builder`             | Model Context Protocol    |
| `documentation-templates` | Doc formats               |
| `i18n-localization`       | Internationalization      |
| `performance-profiling`   | Web Vitals, optimization  |
| `systematic-debugging`    | Troubleshooting           |

### Community & Advanced Engineering (Vercel, Chrome / Addy Osmani, Wshobson)

| Skill | Description | Sourced From |
| --- | --- | --- |
| `git-workflow-and-versioning` | Atomic commits, branching, PRs, semantic versioning | `addyosmani/agent-skills` |
| `doubt-driven-development` | Adversarial cross-examination of non-trivial assumptions | `addyosmani/agent-skills` |
| `incremental-implementation` | Thin, verifiable slices of multi-file changes | `addyosmani/agent-skills` |
| `observability-and-instrumentation` | Production logging, OpenTelemetry, metrics, alerting | `addyosmani/agent-skills` |
| `ai-debt-detector` | Catches orphaned resources, brittle code, thin error handling | `wshobson/agents` |
| `session-guard` | Prevents context compaction amnesia and rule drift in long sessions | `wshobson/agents` |
| `parallel-feature-development` | Coordinates multi-agent work streams and conflict avoidance rules | `wshobson/agents` |
| `parallel-debugging`           | Competing hypotheses with parallel evidence collection            | `wshobson/agents` |
| `task-coordination-strategies` | Decomposing complex tasks & dependency graphs                     | `wshobson/agents` |
| `vercel-composition-patterns` | React composition patterns that scale, compound components | `vercel-labs/agent-skills` |
| `vercel-react-view-transitions` | React View Transitions API for fluid native animations | `vercel-labs/agent-skills` |

### Cloud Native & DevOps Infrastructure

| Skill | Description |
| --- | --- |
| `kubernetes-operator` | Helm charts, k8s manifests, resource quotas, pod diagnostics |
| `terraform-architect` | Infrastructure as Code, remote state locking, modular cloud |
| `aws-cloud-patterns`  | Serverless, Lambda, S3 security, DynamoDB, least-privilege IAM |

### Advanced Quality & Contract Testing

| Skill | Description |
| --- | --- |
| `mutation-testing`       | Stryker/Mutmut mutation testing, assertion strength, mutant elimination |
| `property-based-testing` | Generative invariant testing (fast-check), automatic shrinking |
| `api-contract-testing`   | Consumer-Driven Contracts (Pact), OpenAPI schema validation |

### Git Mastery & SRE Operations

| Skill | Description |
| --- | --- |
| `git-workflow-pro`     | Conventional commits, interactive rebase, bisect, worktrees |
| `pr-review-specialist` | Severity-calibrated code reviews, security and performance flagging |
| `caveman-review`       | Ultra-dense, zero-fluff code reviews (one-line format: L<line>: <problem>. <fix>.) |
| `incident-postmortem`  | Blameless SRE postmortems, 5 Whys root cause analysis, action items |

### API Security & Resilience

| Skill | Description |
| --- | --- |
| `security-hardened-api`    | OWASP API Security Top 10, BOLA defense, defensive rate limiting |
| `database-query-optimizer` | EXPLAIN ANALYZE, composite indexes, deadlock mitigation |
| `microservices-resilience` | Circuit breakers, bulkheads, exponential backoff with jitter |

### Design Engineering & Motion Suite (Emil Kowalski)

| Skill                | Description                                                                    | Sourced From |
| -------------------- | ------------------------------------------------------------------------------ | ------------ |
| `emil-design-eng`    | UI polish, component feeling, and micro-interaction philosophy                 | `emilkowalski/skills` |
| `apple-design`       | Tactile feedback, optical sizing, fluid springs, Apple HIG craft               | `emilkowalski/skills` |
| `animate`            | Building 60fps animations with curve physics and interruptibility              | `emilkowalski/skills` |
| `review-animations`  | Auditing motion code, spring curves, and framerate budgets                     | `emilkowalski/skills` |
| `improve-animations` | Prioritized motion roadmaps and codebase animation audit                       | `emilkowalski/skills` |
| `prototype`          | Building multiple visual variations of UI components                           | `emilkowalski/skills` |
| `pick-ui-library`    | Curated selection of premier frontend libraries for specific tasks            | `emilkowalski/skills` |

### Cloudflare Edge & Serverless Infrastructure

| Skill                    | Description                                                            | Sourced From |
| ------------------------ | ---------------------------------------------------------------------- | ------------ |
| `cloudflare`             | Official architecture guide for Workers, D1, R2, KV, and Pages         | `cloudflare/skills` |
| `workers-best-practices` | Production Workers patterns, cache APIs, bindings, low latency         | `cloudflare/skills` |
| `wrangler`               | Official Wrangler CLI configuration, previews, migrations, deployments | `cloudflare/skills` |
| `nextjs-on-cloudflare`   | Deploying Next.js apps onto Cloudflare Workers / OpenNext (`ruleforge`)| `cloudflare/skills` |

### Developer Productivity & Deployment

| Skill              | Description                                                                | Sourced From |
| ------------------ | -------------------------------------------------------------------------- | ------------ |
| `deploy-to-vercel` | Vercel zero-friction preview and production deployments                    | `vercel-labs` |
| `find-skills`      | Interactive skill discovery utility across open agent ecosystem            | `vercel-labs` |

### Academic Research & Synthesis

| Skill                     | Description                                                                    | Sourced From |
| ------------------------- | ------------------------------------------------------------------------------ | ------------ |
| `academic-pipeline`       | Orchestrator for full academic research pipeline (research → write → review)  | `imbad0202/academic-research-skills` |
| `academic-paper`          | 12-agent academic paper writing pipeline with 11 operational modes             | `imbad0202/academic-research-skills` |
| `academic-paper-reviewer` | Multi-perspective academic paper review with dynamic reviewer personas         | `imbad0202/academic-research-skills` |
| `deep-research`           | Universal deep research agent team; 13-agent pipeline for literature synthesis  | `imbad0202/academic-research-skills` |
| `sr-screener`             | Protocol-driven study screening for systematic, scoping & rapid reviews (PRISMA)| `imbad0202/academic-research-skills` |

---

## 🔄 Workflows (17)

Slash command procedures. Invoke with `/command`.

| Command          | Description                                                                 |
| ---------------- | --------------------------------------------------------------------------- |
| `/battle`        | Colosseum Battle Mode — adversarial dual-agent stress test & arbitration   |
| `/benchmark`     | Empirical hardware telemetry & ad-hoc performance stress harnesses          |
| `/brainstorm`    | Socratic discovery & structured options exploration                         |
| `/compaction`    | Context compaction, durable artifact flushing & turn history hygiene        |
| `/create`        | Application & feature scaffolding dialog                                    |
| `/debug`         | Systematic problem investigation mode                                       |
| `/deploy`        | Safe production deployment procedures & pre-flight checks                   |
| `/enhance`       | Iterative feature updates on existing codebases                             |
| `/impeccable`    | Anti-cliché UI polish, typography, and frontend design review                |
| `/library`       | Search, inspect, and activate from the 2,031 offline reserve skills across 36 repositories          |
| `/orchestrate`   | Multi-agent perspective coordination & workload balancing                   |
| `/owl`           | Decoupled deep investigator & verified coder pipeline                       |
| `/plan`          | Structured roadmap & task dependency planning (no code)                     |
| `/preview`       | Development preview server management                                       |
| `/status`        | Project progress tracking & status board                                    |
| `/test`          | Test suite generation & verification execution                              |
| `/ui-ux-pro-max` | Comprehensive UI design planning (50 styles, 21 palettes, 50 fonts)        |

---

## 🎯 Skill Loading Protocol

```plaintext
User Request → Skill Description Match → Load SKILL.md
                                            ↓
                                    Read references/
                                            ↓
                                    Read scripts/
```

### Skill Structure

```plaintext
skill-name/
├── SKILL.md           # (Required) Metadata & instructions
├── scripts/           # (Optional) Python/Bash scripts
├── references/        # (Optional) Templates, docs
└── assets/            # (Optional) Images, logos
```

### Enhanced Skills (with scripts/references)

| Skill               | Files | Coverage                            |
| ------------------- | ----- | ----------------------------------- |
| `ui-ux-pro-max`     | 27    | 50 styles, 21 palettes, 50 fonts    |
| `app-builder`       | 20    | Full-stack scaffolding              |

---

## � Scripts (2)

Master validation scripts that orchestrate skill-level scripts.

### Master Scripts

| Script          | Purpose                                 | When to Use              |
| --------------- | --------------------------------------- | ------------------------ |
| `checklist.py`  | Priority-based validation (Core checks) | Development, pre-commit  |
| `verify_all.py` | Comprehensive verification (All checks) | Pre-deployment, releases |

### Usage

```bash
# Quick validation during development
python .agent/scripts/checklist.py .

# Full verification before deployment
python .agent/scripts/verify_all.py . --url http://localhost:3000
```

### What They Check

**checklist.py** (Core checks):

- Security (vulnerabilities, secrets)
- Code Quality (lint, types)
- Schema Validation
- Test Suite
- UX Audit
- SEO Check

**verify_all.py** (Full suite):

- Everything in checklist.py PLUS:
- Lighthouse (Core Web Vitals)
- Playwright E2E
- Bundle Analysis
- Mobile Audit
- i18n Check

For details, see [scripts/README.md](scripts/README.md)

---

## 📊 Statistics

| Metric              | Value                         |
| ------------------- | ----------------------------- |
| **Total Agents**    | 20                            |
| **Total Skills**    | 36                            |
| **Total Workflows** | 11                            |
| **Total Scripts**   | 2 (master) + 18 (skill-level) |
| **Coverage**        | ~90% web/mobile development   |

---

## 🔗 Quick Reference

| Need     | Agent                 | Skills                                |
| -------- | --------------------- | ------------------------------------- |
| Web App  | `frontend-specialist` | react-best-practices, frontend-design |
| API      | `backend-specialist`  | api-patterns, nodejs-best-practices   |
| Mobile   | `mobile-developer`    | mobile-design                         |
| Database | `database-architect`  | database-design, prisma-expert        |
| Security | `security-auditor`    | vulnerability-scanner                 |
| Testing  | `test-engineer`       | testing-patterns, webapp-testing      |
| Debug    | `debugger`            | systematic-debugging                  |
| Plan     | `project-planner`     | brainstorming, plan-writing           |


## 🎯 Active Curated Skills vs Full Library

To maintain optimal context performance and adhere strictly to AI system context budgets without prompt bloat or skill exclusion:
- **Active Hot Set (`D:\Repo\.agent\skills`)**: **89 curated high-signal skills** (Core standards, Next.js, Cloudflare, testing, UI craft, databases, security, academic research).
- **Full Offline Store (`D:\Repo\.agents\skills`)**: **594 total skills** preserved permanently on disk.
- **Skill Activation on Demand**: Any skill from the 594 library can be activated into `.agent/skills` anytime via `python .agents/library/activate_skill.py <skill-name>` or `/library`.


### 📚 Skills Provenance & Upstream Registry

All 594 installed skills and their upstream origins, source repositories, and update commands are systematically cataloged in:
- **Registry Document**: [`SKILLS_PROVENANCE.md`](file:///D:/Repo/.agents/SKILLS_PROVENANCE.md)
- **JSON Lockfiles**: [`skills-lock.json`](file:///D:/Repo/.agents/skills-lock.json)
- Covers 32 distinct source repositories (e.g. `anthropics/knowledge-work-plugins`, `magentosh/superpowers`, `emilkowalski/skills`, `vercel-labs/agent-skills`, `cloudflare/skills`, `addyosmani/agent-skills`, etc.).
