---
name: third-party-integration-audit
description: "Audit an external repo or tool for practical adoption: inspect claims, map integration surfaces, install in isolation, run a real smoke test, and judge production readiness from observed behavior."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [audit, integration, repo, evaluation, smoke-test, hermes, plugins]
    related_skills: [codebase-inspection, systematic-debugging, hermes-agent]
---

# Third-Party Integration Audit

Evaluate whether an external repository or tool is worth using in practice, not just in theory.

## When to use

Use this when the user asks some version of:
- "Check this repo and tell me what it does"
- "Is this worth using with Hermes?"
- "Install it and see if it actually works"
- "Audit this plugin/provider/integration before I trust it"

Especially useful for:
- Hermes plugins and memory providers
- CLIs, agents, dashboards, and MCP servers
- repos that claim local/private operation
- tools where docs may be ahead of code

## Core rule

Do not stop at README summary if the user cares about adoption. Convert claims into verified facts.

Separate:
- **repo claims** — what docs say
- **code facts** — what source actually implements
- **runtime facts** — what works under a real install
- **judgment** — whether the tool is worth using for this user's workflow

## Output shape

Give the user four things:
1. **What it is**
2. **How it integrates**
3. **What actually worked / broke in testing**
4. **Recommendation for this workflow**

## Workflow

### 1. Inspect the repository before touching local state

Read, in roughly this order:
- root README
- packaging/manifest files (`pyproject.toml`, `package.json`, `plugin.yaml`, Docker files)
- integration docs
- actual integration code paths
- tests
- open issues if the repo is young or ambitious

Look for:
- claimed features
- supported runtimes
- persistence layer
- auth/secrets model
- extension points
- install path
- operational assumptions
- skipped contexts, special cases, or fallbacks

### 2. Map the integration surface explicitly

For Hermes-related audits, identify:
- plugin entrypoints
- memory/provider hooks
- MCP/tool surfaces
- CLI commands
- config keys written or expected
- storage paths / DB locations
- background jobs, consolidation, or async behavior

Do not rely only on docs. Read the code that wires the integration.

### 3. Use isolated installation by default

If the user wants a real test, do **not** modify the main profile first.

Preferred pattern:
- create a throwaway Hermes profile
- clone enough config to reproduce reality
- install into the runtime Hermes actually uses
- point installer/config at the throwaway profile

For Hermes specifically:
- verify which Python interpreter the `hermes` launcher uses
- install the package into that venv, not whichever `python3` happens to be on PATH
- verify active profile and resulting config after installation

### 3b. Prefer the lightest install that proves the user's actual need

Do not default to cloning a repo just because the user linked GitHub.

Use this decision order:
- compare the repo's claimed value against tools/workflows the user already has
- identify the exact missing capability in the user's stack
- if normal use only needs the published package/CLI, install the package in an isolated venv instead of cloning source
- only clone the repo when you need source inspection beyond hosted files, local modification, or an unreleased fix

This matters for document/conversion tools in particular: often the real question is not "is the repo good?" but "does it cover a gap that existing OCR/web/PDF tooling does not?"

A good audit answer can therefore be:
- current stack already covers URLs/remote PDFs well
- this tool is only worth adding for recurring local DOCX/PPTX/XLSX/PDF→Markdown ingestion
- package install is enough; repo clone is unnecessary for routine use

### 4. Treat installer success messages as claims, not proof

After any installer or setup command, verify:
- config file values are actually correct
- plugin/provider is visible in status commands
- expected files/symlinks/directories exist
- the feature is active in the intended profile
- the config still parses cleanly if the installer touched YAML/JSON/TOML

If the installer says success but status disagrees, inspect the resulting config directly and correct with the official CLI/config tool if possible.

### 4b. When an installer edits config files, verify syntax before trusting runtime status

Some third-party installers append the right semantic content but break indentation or structure while doing it. That can make the host app ignore the entire config and fall back to defaults.

Practical check pattern right after install:
- parse the touched config with the native parser (`yaml.safe_load`, `jq`, TOML parser, etc.)
- run the app's own config/status command to catch silent fallback-to-default behavior
- re-check the feature surface you expected (for Hermes, `hermes mcp list`)
- if parsing failed, fix the file structure first, then re-run status verification

Reference examples:
- `references/codegraph-hermes-installer-yaml-bug.md` — CodeGraph v0.9.4 on Hermes wrote the right MCP block but mis-indented `platform_toolsets.cli`, causing Hermes to ignore the config until manual repair.
- `references/hermes-dashboard-telemetry-vs-analytics.md` — how to distinguish operator telemetry from real analytics in Hermes dashboard/plugin repos, plus DOM/text verification when route snapshots are too shallow.
- `references/deployment-ci-release-audit.md` — end-to-end checks for fresh-install auth, Compose env/healthcheck parity, hardened-runtime CI, installer exposure ordering, persisted-state upgrades, docs, secrets, and release pinning.

### 4c. When deployment files are in scope, trace install and upgrade paths across files

Do not review the Dockerfile, Compose, installer, CI, tests, and README as independent documents. Follow values and behavior across all of them:

- start with no `.env` and no persisted data; prove the documented first-account flow works through the real network boundary
- compare `.env.example` and README variables against the Compose `environment:` block
- render Compose with sentinel overrides to catch hardcoded healthcheck ports or silently dropped settings
- compare installer credential detection with runtime persisted-state precedence
- verify helper scripts use the same host/container data paths described by the docs
- require CI to exercise the actual hardened runtime and a real product capability, not merely a weak `docker run` health probe

Treat an impossible fresh install or an insecure-by-default remote shell bind as a release blocker even when unit tests and syntax checks pass.

### 5. Run a real smoke test with a concrete token

Use a unique test string or token that is easy to search.

For memory systems, verify at least:
- write/store path works
- retrieval works in the same session if relevant
- retrieval works in a fresh session
- persisted data lands where expected on disk

Prefer a direct end-to-end probe over synthetic confidence from status commands.

### 5b. For dashboard/plugin repos, verify the shipped frontend bundle actually runs

Do not assume `dist/index.js` is valid just because the repo has a manifest, screenshots, and a README.

For Hermes dashboard plugins, verify all three layers:
- **discovery** — plugin appears in `/api/dashboard/plugins`
- **route** — the tab route loads (for example `/control-room`)
- **runtime registration** — the page does not fall back to "script did not call register()" or similar plugin-loader errors

Practical checks:
- inspect the actual `dist/index.js`, not just the manifest
- if the bundle looks corrupted or oddly encoded, treat that as a real adoption risk
- use browser console/page text to confirm the plugin registered and rendered real UI, not just the dashboard shell
- if the dashboard route snapshot only shows sidebar/shell text, verify with `document.body.innerText.includes(...)` and DOM counts (`querySelectorAll(...)`) instead of trusting the accessibility snapshot alone
- if the repo's backend API works but the shipped frontend bundle is broken, report the split clearly: backend usable, frontend artifact bad
- when the user explicitly wants a working install anyway, it is acceptable to salvage by pairing the renamed plugin identity/route/API with a known-good compatible frontend bundle, but say plainly that this is a repaired install rather than a pure untouched upstream install
- distinguish operator telemetry from real analytics: confirm whether the shipped code actually calls things like `getAnalytics(...)` / `getModelsAnalytics(...)` or only exposes current status, session counts, health scores, token totals, and recent activity

### 6. If observability tools disagree, inspect the underlying state

When CLI status, stats, or inspect output conflicts with observed behavior:
- inspect storage directly (DB/files)
- compare shared vs profile-isolated paths
- check whether data is in working vs consolidated storage
- verify whether the user-facing behavior still works despite misleading instrumentation

This often separates a real data-loss bug from a reporting bug.

### 7. Judge against the user's actual workflow

Reference notes:
- `references/mnemosyne-hermes-smoke-test.md` — example where installer/config success was misleading and direct DB inspection was needed.
- `references/yantrikdb-hermes-smoke-test.md` — example where the plugin worked end-to-end, but explicit profile-local DB path/namespace and env-driven CLI verification removed ambiguity about storage and observability.
- `references/hermes-dashboard-plugin-broken-dist-recovery.md` — dashboard-plugin-specific runtime check and recovery pattern when a third-party repo ships a broken `dist` bundle but the user still wants a working install.
- `references/markitdown-adoption-pattern.md` — compare existing extraction coverage first, then decide whether an isolated package-only install is enough or the repo itself is unnecessary.
- `references/groktocrawl-firecrawl-stack-eval.md` — Firecrawl v2-compatible Docker stack: Hermes `FIRECRAWL_API_URL` wiring, overlap with web_search/web_extract, hardware/port deferral, Obsidian decision note pattern.

Do not give generic "promising project" praise.

Score it against the user's needs, such as:
- low-noise memory
- cron/subagent compatibility
- local/private storage
- install simplicity
- operational reliability
- debuggability
- profile isolation

## Pitfalls

1. **System Python vs app runtime Python** — many agent tools run from a bundled or dedicated venv. Installing into `/usr/bin/python3` may do nothing for the actual app.
2. **Installer wrote config but not valid effective config** — duplicate keys, trailing overrides, or wrong profile targets can make a claimed install inert.
3. **Status commands can lag reality** — a broken `stats`/`inspect` surface does not automatically mean the core feature failed. Verify with a real end-to-end probe and direct storage inspection.
4. **Fresh-session verification matters** — a memory/plugin test is weak if it only works inside the original session.
5. **Young integrations often skip contexts** — cron, subagents, background workers, and consolidation/sleep paths may differ from normal chat behavior. Check explicitly before recommending broad adoption.
6. **Shared-vs-isolated storage confusion** — when a tool supports profile isolation or multi-bank storage, always identify which DB/path the test actually used.

## Hermes-specific checklist

When auditing a Hermes integration:
- identify Hermes version
- identify Hermes runtime Python / venv
- inspect current `memory status` or equivalent baseline first
- create a throwaway profile unless user explicitly wants in-place change
- run installer with the intended `HERMES_HOME` / profile context
- verify `hermes --profile <name> ... status` after install
- for memory plugins with implicit defaults, set explicit profile-local storage/env config in the throwaway profile after install (for example DB path + namespace) so the smoke test cannot silently hit a shared global store
- run a real chat/tool probe, not just admin/status commands
- if memory-related, test fresh-session recall
- inspect the on-disk store if reporting looks inconsistent
- when the provider ships its own CLI/stats commands, verify them against the same profile-local DB; if the CLI keys off env vars rather than CLI flags, export the exact DB path for the check instead of assuming it will discover the throwaway profile automatically

## Recommendation language

Use concrete verdicts such as:
- **Works in practice, but rough edges remain**
- **Good experimental profile-only tool, not main-profile default yet**
- **Docs overstate maturity**
- **Core path works; observability and installer quality lag**

Avoid vague language like "seems promising" unless you immediately say why and what was or was not verified.

## References

- `references/mnemosyne-hermes-smoke-test.md` — example of a Hermes memory-provider audit where installer success was misleading, fresh-session recall passed, and direct DB inspection was needed to resolve CLI/reporting mismatch.
