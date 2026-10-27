# 🌐 LobeHub Agent Skills Suite

> **Category**: `lobehub-ecosystem`  
> **Total Skills in Category**: 55 real modular skills  
> **Directory**: [`.agents/category/lobehub-ecosystem`](./)  
> **Format**: **100% Real standalone skill folders** (no symlinks, fully portable, offline ready).

---

## ⚡ Quick Activation Command

To link any skill from this category into your active hot-set (`.agents/skills/`):
```bash
python .agents/library/activate_skill.py link <skill-name>
```

---

## 📑 Complete Skill Catalog (55 Skills)

| Skill Folder | Status | Upstream Source | Description |
| :--- | :---: | :--- | :--- |
| **[`acceptance`](./acceptance/SKILL.md)** | 📦 Library | `lobehub-skills` | End-to-end verification and self-evidence for a delivery in any repository, |
| **[`add-model-provider`](./add-model-provider/SKILL.md)** | 📦 Library | `lobehub-skills` | Add an AI model provider to LobeHub, including runtime integration, model cards, configuration, branding, documentation, |
| **[`add-setting-env`](./add-setting-env/SKILL.md)** | 📦 Library | `lobehub-skills` | Add server-side environment variables that control default values for user settings. |
| **[`agent-runtime-hooks`](./agent-runtime-hooks/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for agent lifecycle hooks, tool mocks, intervention, sub-agent calls and context compression. |
| **[`agent-signal`](./agent-signal/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for Agent Signal sources, actions, policies, middleware, workflow handoff and deduplication. |
| **[`agent-testing-bot`](./agent-testing-bot/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for real bot-channel acceptance in Discord, Slack, Telegram, WeChat/Weixin, Lark/Feishu, QQ or iMessage on macOS. Ex |
| **[`agent-tracing`](./agent-tracing/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for agent traces by operation ID (拉线上 tracing): failed tools, arguments/results, available tools, execution location |
| **[`agent-work`](./agent-work/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for the Agent Work output registry: registration, deduplication, cards, skill providers, CLI scanners and Work types |
| **[`alint-ruleset`](./alint-ruleset/SKILL.md)** | 📦 Library | `lobehub-skills` | Maintain LobeHub's model-backed alint rule set in packages/alint: author a rule, calibrate its false positives against r |
| **[`builtin-tool`](./builtin-tool/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for LobeHub builtin agent tools: manifests, executors, runtimes, inspectors, renders, streaming and intervention. |
| **[`chat-sdk`](./chat-sdk/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for multi-platform bots built with chat SDK: webhooks, mentions, slash commands, cards, modals and streaming. |
| **[`cleanup-git-worktrees`](./cleanup-git-worktrees/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for stale-worktree, Git registration and branch audits. Managed removal uses the repo lifecycle. |
| **[`cli`](./cli/SKILL.md)** | 📦 Library | `lobehub-skills` | LobeHub CLI (@lobehub/cli) development guide — commands, subcommands, architecture. |
| **[`compose-atoms`](./compose-atoms/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for splitting heavy domains into capabilities (原子组件) across page, portal, share or micro-app hosts, sinking state (状 |
| **[`data-fetching-architecture`](./data-fetching-architecture/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for client APIs, SWR hooks, cache invalidation, async errors, useEffect migration, home first paint and persistent c |
| **[`db-migrations`](./db-migrations/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for Drizzle migration rollout, online indexes, backfills, idempotent SQL and migration regeneration or rebase confli |
| **[`debug-frontend-with-browser`](./debug-frontend-with-browser/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for intermittent UI, stale state, ordering, navigation or browser-only bugs. Extends acceptance with boundary tracin |
| **[`debug-package`](./debug-package/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for debug() logging, lobe-* namespaces, DEBUG/localStorage.debug configuration and log formatting. |
| **[`deep-review`](./deep-review/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for independent PR, diff or branch review; not explanations. Full multi-agent review requires an explicit deep-revie |
| **[`design-prototype`](./design-prototype/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for interactive HTML prototypes (交互原型) with the real LobeHub UI stack. Excludes production UI implementation. |
| **[`desktop`](./desktop/SKILL.md)** | 📦 Library | `lobehub-skills` | Electron desktop development guide — IPC handlers, controllers, preload scripts, window/menu management. |
| **[`desktop-security-update`](./desktop-security-update/SKILL.md)** | 📦 Library | `lobehub-skills` | Inspect, mark, or revoke vulnerable LobeHub Desktop versions through the existing release workflow and signed R2 securit |
| **[`docs-changelog`](./docs-changelog/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for EN/ZH website product changelogs in docs/changelog/*.mdx. Excludes GitHub Release notes. |
| **[`drizzle`](./drizzle/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for Drizzle schemas and queries: tables, indexes, relations, joins and inferred types. Rollout belongs to db-migrati |
| **[`full-text-search`](./full-text-search/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for product search: FtsSearchRepo, pg_search/pg_like/Elasticsearch, mapping migrations, projections, Outbox sync, re |
| **[`heterogeneous-agent`](./heterogeneous-agent/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for external-agent launchers and execution identity, Claude Code/Codex adapters, IPC, event mapping, sessions, persi |
| **[`hotkey`](./hotkey/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for keyboard shortcuts, registration, key combinations, scope, conflicts and shortcut tooltips. |
| **[`i18n`](./i18n/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for user-facing strings and react-i18next locale keys, namespaces, interpolation, translations or bun run i18n. |
| **[`llm-generation`](./llm-generation/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for application prompts, generateObject/generateText, model selection and generation tracing. Excludes provider adap |
| **[`lobe-design`](./lobe-design/SKILL.md)** | 📦 Library | `lobehub-skills` | Single entry for LobeHub UI design work. Routes any instruction — macro ("重做这个后台", "整体打磨一下"), |
| **[`lobe-task`](./lobe-task/SKILL.md)** | 📦 Library | `lobehub-skills` | Modular agent skill module |
| **[`lobehub-platform`](./lobehub-platform/SKILL.md)** | 📦 Library | `lobehub-skills` | Comprehensive LobeHub AI Platform architecture reference: agent groups, bot connectors (Discord, Slack, Telegram, WeChat |
| **[`model-bank-metadata`](./model-bank-metadata/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for model knowledgeCutoff, family and generation metadata: onboarding, corrections, research and bulk backfills. |
| **[`pr`](./pr/SKILL.md)** | 📦 Library | `lobehub-skills` | Create a PR for the current branch (targets `canary` by default), including splitting one cross-layer branch into ordere |
| **[`product-design`](./product-design/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for new surfaces, redesigns and vague product asks: establish user tasks and business meaning. Built-screen audits a |
| **[`project-overview`](./project-overview/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for the OSS repository map, code-layer lookup, apps/packages/src ownership and business stubs. |
| **[`react`](./react/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for TSX components, UI libraries, styling, state locality, layout, render performance and memoization. |
| **[`response-compliance`](./response-compliance/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for OpenResponses/Response API compliance tests, endpoint schema failures and test runs. |
| **[`run-eval-harbor`](./run-eval-harbor/SKILL.md)** | 📦 Library | `lobehub-skills` | Run and diagnose existing Harbor or FrontierHarness evaluations against local production LobeHub or LobeHub Cloud, on a  |
| **[`skills-audit`](./skills-audit/SKILL.md)** | 📦 Library | `lobehub-skills` | Audit .agents/skills SKILL.md files. Use for recurring checks of duplicate, overlapping, stale, inconsistent, or broken  |
| **[`source-layout`](./source-layout/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for where a file lives, how it is named, where its tests go, and how to split a source or test file over 1200 lines  |
| **[`spa-routes`](./spa-routes/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for SPA routes and page segments: Web/desktop/mobile/popup routers, redirects and src/routes-to-features boundaries. |
| **[`split-large-file`](./split-large-file/SKILL.md)** | 📦 Library | `lobehub-skills` | Refactor a source file over 1200 lines into a directory of cohesive modules without changing behavior, test-first. Use w |
| **[`split-micro-app`](./split-micro-app/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for standalone micro apps: React Router SSR/SSG, Cloud overlays, Workers, CDN/R2, SEO/OG, gateway routes, previews,  |
| **[`store-data-structures`](./store-data-structures/SKILL.md)** | 📦 Library | `lobehub-skills` | Explicit compatibility entry for Zustand data-shape guidance. |
| **[`testing`](./testing/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for Vitest tests, mocks, coverage and failing-test diagnosis. |
| **[`testing-heterogeneous-agents`](./testing-heterogeneous-agents/SKILL.md)** | 📦 Library | `lobehub-skills` | Manually runs the live LobeHub official-provider compatibility matrix across Claude Code, Codex, Grok Build, Kimi Code,  |
| **[`trpc-router`](./trpc-router/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for server TRPC routers, procedures and API endpoints in apps/server/src/routers. |
| **[`typescript`](./typescript/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for TypeScript style and type safety when editing TS/TSX/MTS, including imports, async code and error suppression. |
| **[`upstash-workflow`](./upstash-workflow/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for Upstash Workflow/QStash handlers, triggers, durable steps and async fan-out. |
| **[`ux`](./ux/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for product design principles and UX checks when designing or implementing user-facing flows. |
| **[`ux-audit`](./ux-audit/SKILL.md)** | 📦 Library | `lobehub-skills` | Audit a page / surface against the Designing Interfaces pattern language + the ux skill checklists, then land findings.  |
| **[`version-release`](./version-release/SKILL.md)** | 📦 Library | `lobehub-skills` | Version release workflow — release process and GitHub Release notes (not docs/changelog pages). |
| **[`write-landing-docs`](./write-landing-docs/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for public LobeHub website documentation under docs/**, including self-hosting, deployment, migration, and configura |
| **[`zustand`](./zustand/SKILL.md)** | 📦 Library | `lobehub-skills` | Use for Zustand stores: state shapes and type sources, state-only stores with xActions classes, replica-backed list/deta |

---

*Part of the [AgentSkills Vault](https://github.com/SeaXen/agentskills). Master directory in [category/README.md](../README.md).*
