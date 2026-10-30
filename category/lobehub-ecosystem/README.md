# 🌐 LobeHub Agent Skills Suite

> **Category**: `lobehub-ecosystem`  
> **Total Curated Skills**: 52 skills  
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
| [`acceptance`](../../library/lobehub-skills/skills/acceptance) | ⚪ Reserve | `lobehub-skills` | End-to-end verification and self-evidence for a delivery in any repository, with or without a p... |
| [`add-model-provider`](../../library/lobehub-skills/skills/add-model-provider) | ⚪ Reserve | `lobehub-skills` | Add an AI model provider to LobeHub, including runtime integration, model cards, configuration,... |
| [`add-setting-env`](../../library/lobehub-skills/skills/add-setting-env) | ⚪ Reserve | `lobehub-skills` | Add server-side environment variables that control default values for user settings. |
| [`agent-runtime-hooks`](../../library/lobehub-skills/skills/agent-runtime-hooks) | ⚪ Reserve | `lobehub-skills` | Use for agent lifecycle hooks, tool mocks, intervention, sub-agent calls and context compressio... |
| [`agent-signal`](../../library/lobehub-skills/skills/agent-signal) | ⚪ Reserve | `lobehub-skills` | Use for Agent Signal sources, actions, policies, middleware, workflow handoff and deduplication... |
| [`agent-testing-bot`](../../library/lobehub-skills/skills/agent-testing-bot) | ⚪ Reserve | `lobehub-skills` | Use for real bot-channel acceptance in Discord, Slack, Telegram, WeChat/Weixin, Lark/Feishu, QQ... |
| [`agent-tracing`](../../library/lobehub-skills/skills/agent-tracing) | ⚪ Reserve | `lobehub-skills` | Use for agent traces by operation ID (拉线上 tracing): failed tools, arguments/results, available ... |
| [`agent-work`](../../library/lobehub-skills/skills/agent-work) | ⚪ Reserve | `lobehub-skills` | Use for the Agent Work output registry: registration, deduplication, cards, skill providers, CL... |
| [`alint-ruleset`](../../library/lobehub-skills/skills/alint-ruleset) | ⚪ Reserve | `lobehub-skills` | Maintain LobeHub's model-backed alint rule set in packages/alint: author a rule, calibrate its ... |
| [`builtin-tool`](../../library/lobehub-skills/skills/builtin-tool) | ⚪ Reserve | `lobehub-skills` | Use for LobeHub builtin agent tools: manifests, executors, runtimes, inspectors, renders, strea... |
| [`chat-sdk`](../../library/lobehub-skills/skills/chat-sdk) | ⚪ Reserve | `lobehub-skills` | Use for multi-platform bots built with chat SDK: webhooks, mentions, slash commands, cards, mod... |
| [`cleanup-git-worktrees`](../../library/lobehub-skills/skills/cleanup-git-worktrees) | ⚪ Reserve | `lobehub-skills` | Use for stale-worktree, Git registration and branch audits. Managed removal uses the repo lifec... |
| [`cli`](../../library/lobehub-skills/skills/cli) | ⚪ Reserve | `lobehub-skills` | LobeHub CLI (@lobehub/cli) development guide — commands, subcommands, architecture. |
| [`compose-atoms`](../../library/lobehub-skills/skills/compose-atoms) | ⚪ Reserve | `lobehub-skills` | Use for splitting heavy domains into capabilities (原子组件) across page, portal, share or micro-ap... |
| [`data-fetching-architecture`](../../library/lobehub-skills/skills/data-fetching-architecture) | ⚪ Reserve | `lobehub-skills` | Use for client APIs, SWR hooks, cache invalidation, async errors, useEffect migration, home fir... |
| [`db-migrations`](../../library/lobehub-skills/skills/db-migrations) | ⚪ Reserve | `lobehub-skills` | Use for Drizzle migration rollout, online indexes, backfills, idempotent SQL and migration rege... |
| [`debug-frontend-with-browser`](../../library/lobehub-skills/skills/debug-frontend-with-browser) | ⚪ Reserve | `lobehub-skills` | Use for intermittent UI, stale state, ordering, navigation or browser-only bugs. Extends accept... |
| [`debug-package`](../../library/lobehub-skills/skills/debug-package) | ⚪ Reserve | `lobehub-skills` | Use for debug() logging, lobe-* namespaces, DEBUG/localStorage.debug configuration and log form... |
| [`deep-review`](../../library/lobehub-skills/skills/deep-review) | ⚪ Reserve | `lobehub-skills` | Use for independent PR, diff or branch review; not explanations. Full multi-agent review requir... |
| [`design-prototype`](../../library/lobehub-skills/skills/design-prototype) | ⚪ Reserve | `lobehub-skills` | Use for interactive HTML prototypes (交互原型) with the real LobeHub UI stack. Excludes production ... |
| [`desktop`](../../library/lobehub-skills/skills/desktop) | ⚪ Reserve | `lobehub-skills` | Electron desktop development guide — IPC handlers, controllers, preload scripts, window/menu ma... |
| [`desktop-security-update`](../../library/lobehub-skills/skills/desktop-security-update) | ⚪ Reserve | `lobehub-skills` | Inspect, mark, or revoke vulnerable LobeHub Desktop versions through the existing release workf... |
| [`docs-changelog`](../../library/lobehub-skills/skills/docs-changelog) | ⚪ Reserve | `lobehub-skills` | Use for EN/ZH website product changelogs in docs/changelog/*.mdx. Excludes GitHub Release notes... |
| [`drizzle`](../../library/lobehub-skills/skills/drizzle) | ⚪ Reserve | `lobehub-skills` | Use for Drizzle schemas and queries: tables, indexes, relations, joins and inferred types. Roll... |
| [`full-text-search`](../../library/lobehub-skills/skills/full-text-search) | ⚪ Reserve | `lobehub-skills` | Use for product search: FtsSearchRepo, pg_search/pg_like/Elasticsearch, mapping migrations, pro... |
| [`heterogeneous-agent`](../../library/lobehub-skills/skills/heterogeneous-agent) | ⚪ Reserve | `lobehub-skills` | Use for external-agent launchers and execution identity, Claude Code/Codex adapters, IPC, event... |
| [`hotkey`](../../library/lobehub-skills/skills/hotkey) | ⚪ Reserve | `lobehub-skills` | Use for keyboard shortcuts, registration, key combinations, scope, conflicts and shortcut toolt... |
| [`i18n`](../../library/lobehub-skills/skills/i18n) | ⚪ Reserve | `lobehub-skills` | Use for user-facing strings and react-i18next locale keys, namespaces, interpolation, translati... |
| [`llm-generation`](../../library/lobehub-skills/skills/llm-generation) | ⚪ Reserve | `lobehub-skills` | Use for application prompts, generateObject/generateText, model selection and generation tracin... |
| [`lobe-design`](../../library/lobehub-skills/skills/lobe-design) | ⚪ Reserve | `lobehub-skills` | Single entry for LobeHub UI design work. Routes any instruction — macro ("重做这个后台", "整体打磨一下"), m... |
| [`lobe-task`](../../library/lobehub-skills/skills/lobe-task) | ⚪ Reserve | `lobehub-skills` | category: lobehub-ecosystem |
| [`lobehub-platform`](../../library/lobehub-skills/skills/lobehub-platform) | ⚪ Reserve | `lobehub-skills` | Comprehensive LobeHub AI Platform architecture reference: agent groups, bot connectors (Discord... |
| [`model-bank-metadata`](../../library/lobehub-skills/skills/model-bank-metadata) | ⚪ Reserve | `lobehub-skills` | Use for model knowledgeCutoff, family and generation metadata: onboarding, corrections, researc... |
| [`product-design`](../../library/lobehub-skills/skills/product-design) | ⚪ Reserve | `lobehub-skills` | Use for new surfaces, redesigns and vague product asks: establish user tasks and business meani... |
| [`project-overview`](../../library/lobehub-skills/skills/project-overview) | ⚪ Reserve | `lobehub-skills` | Use for the OSS repository map, code-layer lookup, apps/packages/src ownership and business stu... |
| [`react`](../../library/lobehub-skills/skills/react) | ⚪ Reserve | `lobehub-skills` | Use for TSX components, UI libraries, styling, state locality, layout, render performance and m... |
| [`response-compliance`](../../library/lobehub-skills/skills/response-compliance) | ⚪ Reserve | `lobehub-skills` | Use for OpenResponses/Response API compliance tests, endpoint schema failures and test runs. |
| [`run-eval-harbor`](../../library/lobehub-skills/skills/run-eval-harbor) | ⚪ Reserve | `lobehub-skills` | Run and diagnose existing Harbor or FrontierHarness evaluations against local production LobeHu... |
| [`skills-audit`](../../library/lobehub-skills/skills/skills-audit) | ⚪ Reserve | `lobehub-skills` | Audit .agents/skills SKILL.md files. Use for recurring checks of duplicate, overlapping, stale,... |
| [`source-layout`](../../library/lobehub-skills/skills/source-layout) | ⚪ Reserve | `lobehub-skills` | Use for where a file lives, how it is named, where its tests go, and how to split a source or t... |
| [`spa-routes`](../../library/lobehub-skills/skills/spa-routes) | ⚪ Reserve | `lobehub-skills` | Use for SPA routes and page segments: Web/desktop/mobile/popup routers, redirects and src/route... |
| [`split-large-file`](../../library/lobehub-skills/skills/split-large-file) | ⚪ Reserve | `lobehub-skills` | Refactor a source file over 1200 lines into a directory of cohesive modules without changing be... |
| [`split-micro-app`](../../library/lobehub-skills/skills/split-micro-app) | ⚪ Reserve | `lobehub-skills` | Use for standalone micro apps: React Router SSR/SSG, Cloud overlays, Workers, CDN/R2, SEO/OG, g... |
| [`store-data-structures`](../../library/lobehub-skills/skills/store-data-structures) | ⚪ Reserve | `lobehub-skills` | Explicit compatibility entry for Zustand data-shape guidance. |
| [`testing-heterogeneous-agents`](../../library/lobehub-skills/skills/testing-heterogeneous-agents) | ⚪ Reserve | `lobehub-skills` | Manually runs the live LobeHub official-provider compatibility matrix across Claude Code, Codex... |
| [`trpc-router`](../../library/lobehub-skills/skills/trpc-router) | ⚪ Reserve | `lobehub-skills` | Use for server TRPC routers, procedures and API endpoints in apps/server/src/routers. |
| [`typescript`](../../library/lobehub-skills/skills/typescript) | ⚪ Reserve | `lobehub-skills` | Use for TypeScript style and type safety when editing TS/TSX/MTS, including imports, async code... |
| [`upstash-workflow`](../../library/lobehub-skills/skills/upstash-workflow) | ⚪ Reserve | `lobehub-skills` | Use for Upstash Workflow/QStash handlers, triggers, durable steps and async fan-out. |
| [`ux`](../../library/lobehub-skills/skills/ux) | ⚪ Reserve | `lobehub-skills` | Use for product design principles and UX checks when designing or implementing user-facing flow... |
| [`version-release`](../../library/lobehub-skills/skills/version-release) | ⚪ Reserve | `lobehub-skills` | Version release workflow — release process and GitHub Release notes (not docs/changelog pages). |
| [`write-landing-docs`](../../library/lobehub-skills/skills/write-landing-docs) | ⚪ Reserve | `lobehub-skills` | Use for public LobeHub website documentation under docs/**, including self-hosting, deployment,... |
| [`zustand`](../../library/lobehub-skills/skills/zustand) | ⚪ Reserve | `lobehub-skills` | Use for Zustand stores: state shapes and type sources, state-only stores with xActions classes,... |
