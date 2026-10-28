# 🌐 LobeHub Agent Skills Suite

> **Category**: `lobehub-ecosystem`  
> **Total Curated Skills**: 54 skills  
> **Taxonomy Standard**: 38-Domain Granular AI Skills Vault

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate
```powershell
python .agents/library/activate_skill.py activate <skill-name>
```

---

## 🗂️ Curated Skill Inventory

| Skill Name | Status | Origin Repository | Description |
| :--- | :---: | :--- | :--- |
| [`acceptance`](skills/acceptance) | ⚪ Reserve | `lobehub-skills` | > |
| [`add-model-provider`](skills/add-model-provider) | ⚪ Reserve | `lobehub-skills` | Add an AI model provider to LobeHub, including runtime integration, model cards, configuration,... |
| [`add-setting-env`](skills/add-setting-env) | ⚪ Reserve | `lobehub-skills` | Add server-side environment variables that control default values for user settings. |
| [`agent-runtime-hooks`](skills/agent-runtime-hooks) | ⚪ Reserve | `lobehub-skills` | 'Use for agent lifecycle hooks, tool mocks, intervention, sub-agent calls and context compressi... |
| [`agent-signal`](skills/agent-signal) | ⚪ Reserve | `lobehub-skills` | 'Use for Agent Signal sources, actions, policies, middleware, workflow handoff and deduplicatio... |
| [`agent-testing-bot`](skills/agent-testing-bot) | ⚪ Reserve | `lobehub-skills` | 'Use for real bot-channel acceptance in Discord, Slack, Telegram, WeChat/Weixin, Lark/Feishu, Q... |
| [`agent-tracing`](skills/agent-tracing) | ⚪ Reserve | `lobehub-skills` | 'Use for agent traces by operation ID (拉线上 tracing): failed tools, arguments/results, available... |
| [`agent-work`](skills/agent-work) | ⚪ Reserve | `lobehub-skills` | 'Use for the Agent Work output registry: registration, deduplication, cards, skill providers, C... |
| [`alint-ruleset`](skills/alint-ruleset) | ⚪ Reserve | `lobehub-skills` | "Maintain LobeHub's model-backed alint rule set in packages/alint: author a rule, calibrate its... |
| [`builtin-tool`](skills/builtin-tool) | ⚪ Reserve | `lobehub-skills` | 'Use for LobeHub builtin agent tools: manifests, executors, runtimes, inspectors, renders, stre... |
| [`chat-sdk`](skills/chat-sdk) | ⚪ Reserve | `lobehub-skills` | 'Use for multi-platform bots built with chat SDK: webhooks, mentions, slash commands, cards, mo... |
| [`cleanup-git-worktrees`](skills/cleanup-git-worktrees) | ⚪ Reserve | `lobehub-skills` | 'Use for stale-worktree, Git registration and branch audits. Managed removal uses the repo life... |
| [`cli`](skills/cli) | ⚪ Reserve | `lobehub-skills` | LobeHub CLI (@lobehub/cli) development guide — commands, subcommands, architecture. |
| [`compose-atoms`](skills/compose-atoms) | ⚪ Reserve | `lobehub-skills` | 'Use for splitting heavy domains into capabilities (原子组件) across page, portal, share or micro-a... |
| [`data-fetching-architecture`](skills/data-fetching-architecture) | ⚪ Reserve | `lobehub-skills` | 'Use for client APIs, SWR hooks, cache invalidation, async errors, useEffect migration, home fi... |
| [`db-migrations`](skills/db-migrations) | ⚪ Reserve | `lobehub-skills` | 'Use for Drizzle migration rollout, online indexes, backfills, idempotent SQL and migration reg... |
| [`debug-frontend-with-browser`](skills/debug-frontend-with-browser) | ⚪ Reserve | `lobehub-skills` | 'Use for intermittent UI, stale state, ordering, navigation or browser-only bugs. Extends accep... |
| [`debug-package`](skills/debug-package) | ⚪ Reserve | `lobehub-skills` | 'Use for debug() logging, lobe-* namespaces, DEBUG/localStorage.debug configuration and log for... |
| [`deep-review`](skills/deep-review) | ⚪ Reserve | `lobehub-skills` | 'Use for independent PR, diff or branch review; not explanations. Full multi-agent review requi... |
| [`design-prototype`](skills/design-prototype) | ⚪ Reserve | `lobehub-skills` | 'Use for interactive HTML prototypes (交互原型) with the real LobeHub UI stack. Excludes production... |
| [`desktop`](skills/desktop) | ⚪ Reserve | `lobehub-skills` | Electron desktop development guide — IPC handlers, controllers, preload scripts, window/menu ma... |
| [`desktop-security-update`](skills/desktop-security-update) | ⚪ Reserve | `lobehub-skills` | 'Inspect, mark, or revoke vulnerable LobeHub Desktop versions through the existing release work... |
| [`docs-changelog`](skills/docs-changelog) | ⚪ Reserve | `lobehub-skills` | 'Use for EN/ZH website product changelogs in docs/changelog/*.mdx. Excludes GitHub Release note... |
| [`drizzle`](skills/drizzle) | ⚪ Reserve | `lobehub-skills` | 'Use for Drizzle schemas and queries: tables, indexes, relations, joins and inferred types. Rol... |
| [`full-text-search`](skills/full-text-search) | ⚪ Reserve | `lobehub-skills` | 'Use for product search: FtsSearchRepo, pg_search/pg_like/Elasticsearch, mapping migrations, pr... |
| [`heterogeneous-agent`](skills/heterogeneous-agent) | ⚪ Reserve | `lobehub-skills` | 'Use for external-agent launchers and execution identity, Claude Code/Codex adapters, IPC, even... |
| [`hotkey`](skills/hotkey) | ⚪ Reserve | `lobehub-skills` | 'Use for keyboard shortcuts, registration, key combinations, scope, conflicts and shortcut tool... |
| [`i18n`](skills/i18n) | ⚪ Reserve | `lobehub-skills` | 'Use for user-facing strings and react-i18next locale keys, namespaces, interpolation, translat... |
| [`llm-generation`](skills/llm-generation) | ⚪ Reserve | `lobehub-skills` | 'Use for application prompts, generateObject/generateText, model selection and generation traci... |
| [`lobe-design`](skills/lobe-design) | ⚪ Reserve | `lobehub-skills` | > |
| [`lobe-task`](skills/lobe-task) | ⚪ Reserve | `lobehub-skills` |  |
| [`lobehub-platform`](skills/lobehub-platform) | ⚪ Reserve | `lobehub-skills` | Comprehensive LobeHub AI Platform architecture reference: agent groups, bot connectors (Discord... |
| [`model-bank-metadata`](skills/model-bank-metadata) | ⚪ Reserve | `lobehub-skills` | 'Use for model knowledgeCutoff, family and generation metadata: onboarding, corrections, resear... |
| [`product-design`](skills/product-design) | ⚪ Reserve | `lobehub-skills` | 'Use for new surfaces, redesigns and vague product asks: establish user tasks and business mean... |
| [`project-overview`](skills/project-overview) | ⚪ Reserve | `lobehub-skills` | 'Use for the OSS repository map, code-layer lookup, apps/packages/src ownership and business st... |
| [`react`](skills/react) | ⚪ Reserve | `lobehub-skills` | 'Use for TSX components, UI libraries, styling, state locality, layout, render performance and ... |
| [`response-compliance`](skills/response-compliance) | ⚪ Reserve | `lobehub-skills` | 'Use for OpenResponses/Response API compliance tests, endpoint schema failures and test runs.' |
| [`run-eval-harbor`](skills/run-eval-harbor) | ⚪ Reserve | `lobehub-skills` | 'Run and diagnose existing Harbor or FrontierHarness evaluations against local production LobeH... |
| [`skills-audit`](skills/skills-audit) | ⚪ Reserve | `lobehub-skills` | 'Audit .agents/skills SKILL.md files. Use for recurring checks of duplicate, overlapping, stale... |
| [`source-layout`](skills/source-layout) | ⚪ Reserve | `lobehub-skills` | 'Use for where a file lives, how it is named, where its tests go, and how to split a source or ... |
| [`spa-routes`](skills/spa-routes) | ⚪ Reserve | `lobehub-skills` | 'Use for SPA routes and page segments: Web/desktop/mobile/popup routers, redirects and src/rout... |
| [`split-large-file`](skills/split-large-file) | ⚪ Reserve | `lobehub-skills` | 'Refactor a source file over 1200 lines into a directory of cohesive modules without changing b... |
| [`split-micro-app`](skills/split-micro-app) | ⚪ Reserve | `lobehub-skills` | 'Use for standalone micro apps: React Router SSR/SSG, Cloud overlays, Workers, CDN/R2, SEO/OG, ... |
| [`store-data-structures`](skills/store-data-structures) | ⚪ Reserve | `lobehub-skills` | 'Explicit compatibility entry for Zustand data-shape guidance.' |
| [`testing`](skills/testing) | ⚪ Reserve | `lobehub-skills` | 'Use for Vitest tests, mocks, coverage and failing-test diagnosis.' |
| [`testing-heterogeneous-agents`](skills/testing-heterogeneous-agents) | ⚪ Reserve | `lobehub-skills` | 'Manually runs the live LobeHub official-provider compatibility matrix across Claude Code, Code... |
| [`trpc-router`](skills/trpc-router) | ⚪ Reserve | `lobehub-skills` | 'Use for server TRPC routers, procedures and API endpoints in apps/server/src/routers.' |
| [`typescript`](skills/typescript) | ⚪ Reserve | `lobehub-skills` | 'Use for TypeScript style and type safety when editing TS/TSX/MTS, including imports, async cod... |
| [`upstash-workflow`](skills/upstash-workflow) | ⚪ Reserve | `lobehub-skills` | 'Use for Upstash Workflow/QStash handlers, triggers, durable steps and async fan-out.' |
| [`ux`](skills/ux) | ⚪ Reserve | `lobehub-skills` | 'Use for product design principles and UX checks when designing or implementing user-facing flo... |
| [`ux-audit`](skills/ux-audit) | ⚪ Reserve | `lobehub-skills` | 'Audit a page / surface against the Designing Interfaces pattern language + the ux skill checkl... |
| [`version-release`](skills/version-release) | ⚪ Reserve | `lobehub-skills` | 'Version release workflow — release process and GitHub Release notes (not docs/changelog pages)... |
| [`write-landing-docs`](skills/write-landing-docs) | ⚪ Reserve | `lobehub-skills` | 'Use for public LobeHub website documentation under docs/**, including self-hosting, deployment... |
| [`zustand`](skills/zustand) | ⚪ Reserve | `lobehub-skills` | 'Use for Zustand stores: state shapes and type sources, state-only stores with xActions classes... |
