---
name: sagar-hermes-ops
description: Use when working on Hermes, Hermes dashboard/TUI, memory experiments, or SeaDash for Dr. Sagar. Captures his preferred operational workflow and verification standard.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, seadash, dashboard, memory, verification, dr-sagar]
    related_skills: [hermes-agent, hermes-dashboard, seadash, cron-wakeagent-prerun-gates, hermes-gateway-safe-restart]
---

# Sagar Hermes Ops

## Overview
This skill captures durable operational preferences that are too procedural for USER.md or MEMORY.md.

## Dashboard port ownership and proxy topology
When Dr. Sagar reports that the Hermes dashboard is "not opening", do not assume the visible Hermes-branded page on another port is the main dashboard.

Use this order:
2. Verify port ownership and service topology before changing binds or auth. Distinguish:
   - nginx proxy listener
   - raw Hermes dashboard listener
   - unrelated custom dashboards that also happen to be served by a `hermes dashboard` process
3. On current Hermes builds, a dashboard service that binds `0.0.0.0` directly on the public/main port without a registered auth provider will crash-loop. Do not treat `--insecure` as a fix on modern builds; it is deprecated/no-op for non-loopback auth bypass.
4. If `9119` is meant to be the main browser entrypoint, do **not** assume the fix is still the historical `9119 nginx -> 9120 Hermes` split. First ask/verify whether nginx is still intentionally part of the topology. If the user says nginx was removed and they want **direct Hermes on 9119**, restore Hermes' own auth path instead of reintroducing a proxy.
5. For direct `0.0.0.0:9119` binds on modern Hermes, restore `dashboard.basic_auth` via the supported CLI/config path (`hermes config set dashboard.basic_auth.* ...`) rather than trying to patch `~/.hermes/config.yaml` with file-edit tools. On this host, direct patch/write helpers can refuse Hermes security-sensitive config edits.
6. After restoring direct Hermes auth on `9119`, verify in this order:
   - listener exists on `:9119`
   - unauthenticated `GET /` returns `302` to `/login?next=%2F`
   - `GET /api/auth/providers` exposes `basic`
   - `POST /auth/password-login` with the intended credentials returns `{"ok":true,...}`
   - authenticated `GET /api/auth/me` returns the expected `user_id`
   - authenticated `GET /` serves dashboard HTML (for example `<title>Hermes Agent - Dashboard</title>`)
7. If the reverse-proxy auth artifact is missing (for example `.htpasswd` removed), call that out explicitly before changing behavior. The durable lesson is to verify proxy config + auth files together, not to assume the proxy alone is enough.

Reference: `references/dashboard-port-topology-9119-9120.md`

## Session-reset / config-corruption triage
When Hermes appears to have "re-enabled" automatic session reset after the user previously disabled it, do **not** assume the policy actually changed.

Use this order:
1. Check whether `~/.hermes/config.yaml` is still parseable. A YAML parse failure can make Hermes fall back to defaults or partial state, and dashboards/commands may then report misleading behavior.
2. Compare the active config against `config.yaml.bak`, `config.yaml.corrupt.*.bak`, `*.bak-move-*`, and any state-snapshot copy. A suddenly tiny/truncated active config is strong evidence of config corruption, not a real settings change.
3. For session-reset claims, correlate log lines around `Invalidated run generation ... (session_reset)`. That marker is **not** proof of idle/daily auto-reset by itself — it also appears on manual `/reset` flows. Look for nearby slash-command or confirm/cancel log lines before concluding the reset was automatic.
4. Remember the current Hermes upstream default is `session_reset.mode: none`; a missing stanza should not itself re-enable auto reset.
5. If backups show `session_reset.mode: none`, restore a known-good config, validate YAML, then restart the gateway cleanly.

Reference: `references/session-reset-config-corruption-triage.md`

## When to Use
- Working on Hermes itself
- **AceRoute** (`/mnt/tb/1Apps/AceRoute`, `:8866`) — Hermes-only analytics from `state.db` (Search, Tools, Skills, Journey, Home, Costs, Channels, Ops, **Sessions**, **Requests**, **Messages**, **Models**). Operator tier: mirror **Models** depth on other analytics tabs (podium, charts, sort, export, cross-tab). If they say "session page" but mean LLM turns, use **Requests**. **Global duration** lives in header **Settings** only; default **All time** — see `references/aceroute-global-duration-all-time.md` and `dashboard-ui-operations` → `references/aceroute-global-duration-and-all-time.md`. After UI edits: bump `dashboard.js?v=`; `curl` served HTML vs repo. Python changes need **`docker compose build aceroute`** (`./static` is bind-mounted; `app.py` / `aceroute_*.py` are in the image). Page recipes: `hermes-dashboard-development` → `references/aceroute-*-page-v2.md`. Ship features + API smoke + cache-bust before claiming done.
- Debugging Hermes dashboard, TUI, websocket, or gateway issues
- Evaluating memory backends or self-improvement features
- Handling SeaDash UI/fix/improvement requests

## Workflow
1. Prefer direct inspection over guesses.
   - Check the live browser page, websocket endpoints, running processes, logs, and real API responses.
2. Verify before claiming fixed.
   - For dashboard/TUI issues, finish with an actual browser/chat probe, not just a code or log review.
   - **For TradingX (`:8799`, `/mnt/tb/1Apps/Tradingx`):** after pushes, run `npm run test`, `npm run build`, then **`bash scripts/redeploy.sh`** (not bare `docker compose up --build` alone). Verify with curl `/api/...` and browser `/settings`. See `nextjs-dual-deploy` and `medsea-publishing-pipeline` → `references/docker-compose-named-redeploy.md`.
   - **For MedSea (`:8855`):** prefer `curl` on `questions-index.json`, `site-db.js`, and a sample shard before claiming deploy or "10/10". Run `site/scripts/verify_medsea_bank.py` after rebuild. If `docker build` times out, use tar-into-container + `chmod 644` (see `static-site-performance-optimization` recipe Q). Do not claim every clinical answer is correct from JSON gates alone — report mechanical PASS vs clinical unverified separately. For study-app / rationale pushes, load **`medsea-question-bank-audit`** and re-run `rationale_coverage_report.py` before quoting %; honest product matrix is `site/docs/FEATURES.md`.
   - **MedSea exam/flashcards/header:** do not claim "verified" or "done" without a **browser pass** when UX changed — curl alone misses JS fatals. Minimum: `!!window.MedSea`, topic URL params applied, Start reaches runner. If `MedSea` is false, `eval` `exam-engine.js` in console (often `fmtDateTime is not defined`). Use `/exam/index.html?topic=…` when SW serves stale `/exam/` shell; bump `exam-engine.js?v=N` + `CACHE_VERSION`. See `references/medsea-live-browser-verification.md`. Topic-load perf: `static-site-performance-optimization` → `references/topic-scoped-exam-flash-load.md`.
   - **For "is X complete?" follow-up questions, re-run the actual measurement.** A defensive re-statement of the prior claim is not verification. If 33 WebPs are still 300-600 KB after you said "all done", the user has to spend a turn pushing back ("Okk continue check") before you actually look. Build the re-measurement in as the default response shape. See `static-site-performance-optimization/references/web-perf-recipe.md` §"Anti-pattern: claiming 'all done' without re-verification" for the worked example.
3. Prefer external CLI tools directly when they exist.
4. For Mission Control and similar dashboard extensions, fix clutter with **information architecture before feature sprawl**.
   - Prefer **internal sub-tabs / view selectors inside the same route** over adding more top-level pages or turning the tab into one long scroll wall.
   - For Dr. Sagar, default to **one Mission Control route with upper internal tabs** when the page starts feeling haphazard.
   - Treat "same tab, better structure" as the first remedy before adding another dashboard section.
   - Example: use `agy` from shell for inspection tasks instead of recreating its behavior.
5. Keep explanations of self-improvement simple.
   - Avoid mystical or hype-heavy framing.
6. For experimental memory systems or semantic/graph memory, use a throwaway Hermes profile first.
   - Do not test risky memory changes in the main profile.
7. Treat SeaDash UI/fix/improvement requests as SeaDash product work.
   - **Default install path for new self-hosted apps on this server:** `/mnt/tb/1Apps/<appname>` (e.g. Manifest at `/mnt/tb/1Apps/manifest`). Do not use `/mnt/tb/<app>` unless the user overrides.
   - **Filesystem navigation maps:** load skill `hermes-project-context-maps`. For index-only work, **do not modify `AGENTS.md`**. Start at `/mnt/tb/INDEX.md` (disk) and `hermes/INDEX.md` (Hermes home). Weekly cron refreshes via `refresh_mnt_tb_index.py` / `refresh_hermes_indexes.py`; run manually after a new `1Apps/` install if the map must be current immediately. Details: `hermes-project-context-maps` → `references/curated-index-cron-and-layout.md`.
   - **Disk pressure triage:** if Docker is already clean (`docker image prune` → 0B) but SSD/HDD still full, use `references/dietpi-disk-space-audit.md` — usual wins are `hermes-backups/#plain` retention and `.tmp-hermes-backup` staging, not more container prune. Safe cache trims: `uv cache clean --force` (~5G), remove regeneratable dirs under `/root/.cache` (go-build, playwright, puppeteer, camoufox); `pip cache purge` often no-op here (PEP 668 / cache disabled).
   - **Samba `/mnt/tb` from Windows (LAN):** share **`HDD`** → `\\192.168.0.222\HDD`, user **`root`**, Samba password via `sudo smbpasswd root` (not SSH). Sub-shares: `SSD-Apps` → `/mnt/tb/1Apps`, guest **`2dl`**. See `references/dietpi-samba-and-cloudflare-smb.md`.
   - **FreeLLMAPI (`/root/freellmapi`, LAN :3055):** if bridge port-publish fails from the laptop, use **`network_mode: host`**, drop `ports:`, set `PORT`/`HOSTNAME=0.0.0.0` (default **3055**). Verify `ss` shows **node** on `*:3055`, not `docker-proxy`. Recreate with `docker compose up -d --force-recreate`.
8. For third-party Hermes dashboard repos, classify the repo before touching the live system.
   - Determine whether it is theme-only, plugin+theme, or a full dashboard/plugin pack by reading the actual repo tree, manifest files, and shipped assets, not just the README.
9. When a third-party dashboard idea collides with an existing built-in Hermes surface, prefer feature-porting into the working built-in UI over shipping a fake renamed clone.
   - If the upstream frontend bundle is broken, do not substitute a different working frontend and present it as the upstream install. Either disclose it explicitly as a surrogate for diagnosis or stop and pivot to feature-porting.
10. For live Hermes dashboard verification, use the real runtime surface.
    - Confirm the active Hermes home/config path first.
    - Verify plugin/theme behavior on the live dashboard route and, when API probes are auth-gated, use an authenticated browser-session fetch instead of mislabeling the endpoint as broken.
11. For the Obsidian read-only dashboard, treat the systemd user service file as the runtime source of truth.
    - Confirm `ExecStart`, vault path, port, and working directory before editing or restarting.
    - If `/root/.hermes/...` and the service path under `/mnt/...` may be the same file, verify samefile semantics before assuming you need to patch both.
    - For visual overhauls, `agy --print` with `--add-dir` is effective for monolithic single-file dashboards. See `agy-cli` skill for the monolithic dashboard pattern.
12. When adding recall/search to the Obsidian dashboard, prefer lightweight local retrieval over heavy embedding stacks unless the environment clearly supports them.
    - First check whether `sqlite3` with FTS5 is available.
    - If embedding dependencies like `sentence_transformers`, `faiss`, or `torch` are absent, use a hybrid ranker built from FTS keyword hits, token/trigram overlap, wikilink graph proximity, tags, folder affinity, and recency.
13. For dashboard feature work, verify in layers instead of claiming success after the code patch.
    - Run `py_compile` on the target script.
    - Import the module and exercise the new code path directly.
    - Restart the user service and probe the live HTTP endpoint(s).
    - Do a browser smoke test that confirms the UI surface actually renders the new behavior.
    - If a patched dashboard plugin still serves the old JSON/API shape, rescan dashboard plugins first and restart the dashboard processes if needed before concluding the patch failed.
    - For live dashboard API checks, use an authenticated dashboard-session fetch when needed; do not judge a route from wrapper HTML or unauthenticated responses alone.
    - For "10/10" dashboard claims, also check visual clarity: the primary status must be visible above the fold, unambiguous in the nav label, not clipped/overlapped, and not competing with unrelated default content.
    - For built-in Hermes dashboard Terminal-tab work on this host, patch the live source under `/usr/local/lib/hermes-agent/...`, not the chat cwd under `~/.hermes`.
    - When Dr. Sagar asks for local-only dashboard work, do not push commits or update a PR branch unless he explicitly asks. Treat local verification as the default deliverable until he says to push.
    - When he specifies an exact visualization shape, follow it literally instead of "improving" it into a different layout. Example: if he asks for one chart not two, ship one full-width chart and verify the final DOM/visual structure matches that constraint.
    - For Hermes dashboard frontend builds, run `npm run build` from `/usr/local/lib/hermes-agent/web`; the repo root does not own the Vite build script. Verify the emitted `hermes_cli/web_dist/assets/index-*.js` bundle name after every build.
    - On this host, direct `vite build` can be misclassified by Hermes terminal foreground heuristics; run it as a tracked background job, read the log, and verify the emitted bundle name.
    - When restarting the dashboard on `:9120`, stop the old listener first and then launch a fresh dashboard process separately. Do not bundle stop+start into one tracked background job.
    - For terminal-tab polish, the next-level fixes that materially improve perceived quality are: confirm before local-tab delete, a `Recently closed` restore lane, an in-app rename modal instead of `window.prompt`, and a visible split-width control. See `references/hermes-dashboard-terminal-tab-polish.md`.
    - For built-in Hermes Terminal-page persistence/recovery work, treat backend `screen` sessions as truth, keep localStorage only as UI state, and verify both auto-recovery and manual `Restore all` behavior against live backend sessions. See `references/hermes-dashboard-terminal-session-manager.md`.
    - For Terminal right-rail preset UX on Dr. Sagar's dashboard, do not split header controls into a second row unless explicitly requested. If Search belongs to the Presets header, keep the search input inline in that same header row when expanded rather than rendering a separate filter line below.
    - For editable preset banks, section-level operations should be real UI actions, not implied textarea hacks: support Add section, rename via editable section title, and Delete section from the section editor; then verify browser-local and server-side preference persistence after each mutation.
14. For Dr. Sagar's Hermes usage on a laptop, treat local browser automation as thermally expensive by default.
    - Hermes browser automation commonly launches local headless Chromium and can spike CPU/RAM/GPU enough to worsen thermals.
    - If the user reports the laptop getting very hot, throttling, or abruptly powering off during `browser_*` use, prefer lighter paths first: `web_search`, `web_extract`, or a non-browser workflow.
    - If browser interaction is still required, prefer moving the browser workload off the laptop: remote CDP (`browser.cdp_url`) or a cloud browser provider.
    - Do not casually suggest repeated local browser retries on that machine once the user has reported thermal/power risk.
    - The same thermal caution extends beyond browser automation. On this laptop, sustained local CPU operations (e.g. `pip install llama-cpp-python` / ctransformers compile, `mnemosyne reindex` re-embedding thousands of memories, model fine-tuning runs, large file conversions or batch transcodes) can push the CPU from 65°C to 87-88°C, into the firmware emergency-cutoff range. When Dr. Sagar says the laptop is already hot, add explicit `sleep 60-90` gaps between heavy steps, default to lighter extras (e.g. `mnemosyne-memory[embeddings]` over `[all]`), and prefer running the sustained work when the machine can ventilate rather than chaining it after another hot task in the same session.
15. For Hermes dangerous-command approvals, map the UI button to the actual persisted config/state before answering.
    - `Allow Once` = one command only.
    - `Allow Session` = current Hermes process/session only.
    - `Always Allow` = persistent `command_allowlist` entry in `~/.hermes/config.yaml`.
    - `Deny` = reject the request.
    - Check the live allowlist first instead of guessing. A quick local probe is enough.
    - If the user wants to change or revoke `Always Allow`, edit `command_allowlist` and restart Hermes/gateway or start a fresh session so the in-memory allowlist reloads.
    - If the user wants dashboard support, a good built-in shape is a Config-page `Always Allow` panel with: current patterns, add-pattern input, per-entry delete, edit, copy, exact-match testing, a restart/session hint, a clear-all danger zone, and destructive confirmation.
    - If a dedicated management panel exists for a schema-backed field like `command_allowlist`, do not leave the raw generic field as the primary UX. Either hide the raw field from the form or clearly demote it; otherwise the page feels duplicated and confusing.
    - On Dr. Sagar's dashboard requests, prefer placing secondary operator panels like `Always Allow` below the main config form unless he asks for top placement. He notices when a management card interrupts the primary settings flow.
    - When fixing compact form rows, verify layout with DOM geometry rather than eyeballing only the screenshot. For input/button pairs, check equal heights and aligned top/bottom edges in the live browser before calling it polished.
    - For local API verification, remember the dashboard API is still session-token protected. A raw localhost fetch can 401; fetch `/`, extract `window.__HERMES_SESSION_TOKEN__`, then send `X-Hermes-Session-Token` on the `/api/config/command-allowlist*` requests.
    - If the real allowlist is empty but the UI workflow still needs proof, use an isolated temporary `HERMES_HOME` with a seeded `config.yaml` and run a second dashboard instance on another port to verify list/delete/clear and browser dialogs without mutating the main profile.
    - When restarting the Hermes dashboard during live verification, do not chain `hermes dashboard --stop && hermes dashboard ...` inside one tracked background job. `--stop` can kill the dashboard process tree you are in the middle of launching. Stop first, then start a fresh dashboard command separately and verify the new listener/PID.
    - See `references/hermes-dangerous-command-approval-mapping.md`, `references/hermes-dashboard-always-allow-management.md`, and `references/hermes-dashboard-config-panel-polish.md`.
16. For Hermes TUI complaints over SSH, classify terminal transport before treating it as a Hermes core bug.
    - A quick high-value probe is to launch `hermes --tui` in a real PTY on the host and inject a short test string. If it appears in the composer, the server-side TUI is healthy.
    - Then pivot to the SSH/client path: missing `-t`, embedded/editor terminal quirks, stale terminal state (`reset`, `stty sane`), or tmux/TERM mismatch.
    - Ask for `tty`, `$TERM`, and Python `isatty()` output from the broken session plus the exact client type.
    - If the host already defaults to CLI, offer `hermes --cli` or plain `hermes` as the immediate workaround instead of over-focusing on the TUI.
    - See `references/hermes-tui-over-ssh-and-secret-redaction.md`.
17. For Hermes secret-redaction warnings on Dr. Sagar's setup, prefer safety by default.
    - If `security.redact_secrets` is off, explain plainly that future chat output, session JSON, and logs may contain raw API keys/tokens.
    - Dr. Sagar prefers redaction enabled by default; use `hermes config set security.redact_secrets true` unless he explicitly wants raw-value debugging.
    - Remind him that the change protects future output only and does not scrub old logs/session history; previously exposed tokens may still need rotation.
    - Mention that a fresh session or process restart is needed for the safest effect.
    - See `references/hermes-tui-over-ssh-and-secret-redaction.md`.
18. When cleaning built-in memory while an external provider is active, treat `MEMORY.md` as still-live prompt input.
    - Back it up first.
    - Preserve `USER.md` unless the user explicitly asks to clean profile preferences too.
    - Prefer a short rewrite to durable facts over incremental trimming of stale fragments.
    - Verify the cleaned state both on disk and on the live memory dashboard route.
19. For Dr. Sagar's debug sessions, honor a **concrete retry budget** when he sets one.
    - When he states a number ("if all fail again disable it", "after 3 attempts stop", "if X then Y"), that is the budget — not a suggestion.
    - State the budget up front in the first reply so the count is visible, count attempts as you go, and execute the named fallback action the moment the budget runs out.
    - Do not slip in an extra "let me try one more thing" once the budget is exhausted; that defeats the point of the user setting it.
    - Example shape: 4 attempts on tinyfish MCP OAuth (2026-06-17) — after attempt 4, `hermes config set mcp_servers.tinyfish.enabled false` ran cleanly, no fifth attempt offered.
    - For unblocked debug sessions (no budget set), still default to 2-3 attempts before escalating rather than looping indefinitely.
    - Verify the cleaned state both on disk and on the live memory dashboard route.
40. **Match the user's request literally; do not pre-add security or scope.** When Dr. Sagar asks for a settings page to set thresholds + minutes, he wants the page, the threshold field, and the minute field. He does **not** want auth tokens, `lan_only` gates, masked-secret placeholders, JWT-style "Generate strong token" buttons, `web_auth_token` masking, or LAN-vs-public-IP middleware. Concrete case (2026-06-18, systor v0.2 rework): after the first iteration added 4 auth-related fields + token masking + a "Regenerate token" button to the settings page, his reply was "I just ask for lan and setting for to get notification... Not any threshold... Revert back if you do anything wrong." The auth features were unrequested scope creep; reverting them and rebuilding the settings page around the literal three-field-per-metric model (`enabled` / `value` / `duration_min`) shipped a feature he actually wanted.

41. **Dashboard auth: do not layer nginx auth + hermes auth.** When the user wants hermes dashboard with auth on a public port, use hermes' own `basic_auth` in config.yaml — bind to `0.0.0.0` directly. Do **not** add nginx `auth_basic` in front of it. Double layer = double login prompt = user frustration. Concrete case (2026-06-24): user asked "why 9119 need nginx login then again official auth login" — the fix was removing nginx entirely and letting hermes handle auth on `0.0.0.0:9119` with `basic_auth` in config.yaml.
    - **Post-update basic-auth 500 on `/`:** if `:9119/login` works but `/` returns 500 and logs show `BasicAuthProvider is password-only; there is no OAuth redirect flow`, patch `/usr/local/lib/hermes-agent/hermes_cli/dashboard_auth/middleware.py` `_auto_sso_response()` to return `None` for `provider.supports_password` before constructing `/auth/login`, then `py_compile`, restart `hermes-dashboard.service`, and verify `/` redirects to `/login?next=%2F`.

43. **`--insecure` flag still works despite CLI help saying "DEPRECATED / NO-OP".** The official docs and skill reference confirm `--insecure` still allows binding to `0.0.0.0` without auth. The CLI help output is misleading. Use `--insecure` when you need a no-auth public bind (e.g., port 9120 for LAN access without login). Do not trust the CLI help over the actual documentation.

44. For **Manifest LLM router** (cloud or self-hosted), smoke-test with skill `ai-model-smoke-test` — split **Hermes wiring** vs **upstream** (OpenModel `api_mode`, Manifest `X-Manifest-Model` headers). Self-hosted on this host: **`/mnt/tb/1Apps/manifest`** (default install root for new apps: `/mnt/tb/1Apps/<name>`), LAN `http://192.168.0.222:2099`, public `https://mf.xuup.top`, compose project `mnfst`, volume `manifest_pgdata`. Dual URL auth: keep `BETTER_AUTH_URL` on LAN IP + CF tunnel **HTTP Host header** `192.168.0.222:2099` (`dashboard-ui-operations` → `better-auth-single-trusted-origin-multi-network.md`). After `docker compose pull`, pace if the laptop is hot. Hermes provider uses `http://192.168.0.222:2099/v1` and a **local** `mnfst_` key (not cloud). **Model picker:** Hermes custom-provider selection follows Manifest `GET /v1/models`; if that endpoint returns only `auto`, Hermes will only show `auto` — not a bug. Manifest custom tiers like `x-manifest-tier: bynara` are header-based routes, **not model IDs**, so they do not appear in the Hermes model picker unless exposed as separate endpoints/providers. If Dr. Sagar wants tier-selectable entries in Hermes, prefer separate proxy/base URLs that inject fixed tier headers. Pin favorites with `discover_models: false` + `models:` list when appropriate (`ai-model-smoke-test` → `references/manifest-hermes-model-picker-jun-2026.md`; this skill → `references/manifest-hermes-custom-tier-headers-jun-2026.md`). Dr. Sagar chose self-hosted partly to keep Routing API keys on LAN vs Manifest cloud. **Host network optional:** if provider probes time out inside bridge network, both `manifest` + `postgres` can use `network_mode: host` and `DATABASE_URL` → `127.0.0.1:5432`. **Manifest History dashboard tab** (`manifest-history` plugin): open `/manifest-history` on `:9119` after dashboard restart; archive via Postgres `agent_messages` not `/api/v1/history` (404). **Providers tab:** lists **configured** `tenant_providers` merged with usage — expect more rows than traffic-only (e.g. 9 configured, 3 used). **Models tab (v1.3.3+):** merges `cached_models` routing catalog (~400+) with traffic-used models (~3). Manifest **:2099** still ahead on **Overview timeseries** (`/api/v1/overview` needs browser session; `mnfst_` does not). See `hermes-plugin-development` → `references/manifest-history-plugin.md` and `references/manifest-dashboard-2099-parity.md`. See `ai-model-smoke-test/references/manifest-self-hosted-docker-lan-jun-2026.md` and `/mnt/tb/1Apps/manifest/URLS.md`.

43. **Hermes Desktop connects to `hermes dashboard`, not the gateway.** The desktop app on another PC connects to the `hermes dashboard` process (port 9119), not the gateway (port 8642). It does a REST handshake (`GET /api/status`) then a WebSocket for chat. The dashboard must be running and reachable. For remote PCs outside the LAN, use Tailscale or Cloudflare Tunnel. Session TTL defaults to 12 hours (`session_ttl_seconds: 0`); set to `86400` for 24 hours.
    - **Trigger phrases that mean "stop adding scope":** "just", "I just want X", "revert back if you do anything wrong", "not any threshold" / "not any auth" / "not any X" (a flat rejection of a class of features).
    - **Default-suspicious additions for Dr. Sagar:** auth tokens, password hashing, request signing, IP allowlists, MFA, audit logs, rate limiting, encryption-at-rest for trivial fields, "regenerate secret" buttons, masked-secret placeholders, role-based UI, anything that turns a 3-field form into a 14-field form.
    - **What is welcome:** the requested feature, plain UX matching his wording, a clean visual reference (he gave `hermes-telemetry` port 8009 as the explicit "make it like this" target — `curl` that exact URL first instead of guessing the look).
    - **Default shape of a "settings page" for him:** one row per metric, each row showing threshold + duration in minutes + a checkbox. No tabs, no drawer, no collapsible sections, no inline help that scrolls. The page reads top-to-bottom in 10 seconds.
    - **If you are about to add a third settings field per row, stop and ask.** Likely you are conflating two features into one.
    - **Concrete checklist before shipping any settings UI:**
      1. Did the user name the fields they want? Show exactly those fields.
      2. Did the user name a visual reference? `curl` it and match the palette/structure literally.
      3. Can a non-technical operator set thresholds without reading the README? If no, simplify.
      4. Did you add any auth/security/network-binding field that the user did not mention? If yes, revert it.
    - See `lightweight-monitor-daemon` for the canonical "settings UX in minutes, not samples" schema pattern.
15. For Mission Control feature-port work, prefer incremental restoration/extension over broad redesign rewrites.
    - Port operator features into the built-in Mission Control in a safe order: config snapshot/redaction → diff → health/telemetry/session stats → timeline/notes/checklist → analytics/radar.
    - If a later UI pass accidentally removes an earlier analytics block while helper state still exists, compare against the last known-good bundle and restore the render block rather than rebuilding the whole page.
15. When a user shares a repo that is framed as a Claude Code/Codex/Cursor skill and asks to set it up in Hermes, classify it before installing anything.
    - Check whether the repo is actually Hermes-native, a thin agent-specific wrapper, or a pointer to a reusable MCP/backend integration.
    - For Hermes, prefer wiring the reusable MCP server/backend directly instead of pretending the foreign-agent skill installs unchanged.
    - For stdio MCP servers that need wrapper behavior (for example `xvfb-run`, env bootstrapping, auth export), create a tiny local wrapper script and point `hermes mcp add` at that script instead of forcing complex shell behavior through `--args`.
    - In non-interactive setup flows, remember that `hermes mcp add` prompts for tool enablement; pipe confirmation explicitly, then verify with `hermes mcp list` and `hermes mcp test <name>`.
    - If the permanent runtime server should stay headless but first-run OAuth/login needs a visible browser, use a temporary second MCP entry for auth with GUI environment variables passed through the subprocess (`DISPLAY`, `XAUTHORITY`), complete login there, then remove the helper entry and keep the headless runtime entry.
16. In Hermes dashboard frontend code, treat `timeAgo(...)` as epoch-seconds based.
    - If API fields arrive as ISO datetimes (`next_run_at`, `last_run_at`, `previous_generated_at`), convert with `Math.floor(Date.parse(value) / 1000)` first.
    - Otherwise expect broken UI output like `NaNd ago` during live verification.
16. For unofficial/community Hermes additions, prefer a live inventory workflow over conversational memory.
    - Build the source of truth from installed plugins, installed skills, git repos under `~/.hermes`, and config-linked local repos when detectable.
    - Keep a full inventory artifact for inspection, but make scheduled notifications low-noise and update-only.
    - If the user wants dashboard visibility, a small local dashboard tab is fine; do not turn it into a heavy management surface.
    - Treat the dedicated Discord 3rd Party tracker channel/thread as the operating lane for this work. Keep tracker additions, breakages, verification notes, and follow-up fixes there rather than scattering them across general Hermes threads.
    - When a plugin is installed as a symlink into a git-managed source repo, resolve the symlink target and detect the parent repo before labeling the source unknown. Still keep update automation cautious and explain why the row is manual-only.
17. For Mnemosyne-on-Hermes audits, separate local core health from docs-parity polish and from backup health.
    - First classify runtime: confirm whether the live path is direct/local SQLite or Docker, and verify samefile semantics for `/root/.hermes/...` vs `/mnt/tb/hermes/...` before talking about "two copies".
    - Treat `mnemosyne_diagnose()`, SQLite integrity, `mnemosyne verify`, and live stats as the core-health checks.
    - If Hermes provider wiring works but docs-style surfaces are missing, standardize gently: verify Hermes venv `import mnemosyne`, then expose a shell-level `mnemosyne` CLI if needed without changing the active provider design.
    - Do not call the system perfect if the provider is healthy but backups are failing; report core/provider health separately from backup automation health.
    - For backup-notification complaints, distinguish three things explicitly: schedule time, script success, and message delivery semantics. In `no_agent=True` cron jobs, empty stdout means silent success even when `last_status: ok`.
    - If the user expects a daily post in a backup channel, inspect the script and patch it to print a compact success line on every good run; do not assume `last_status: ok` implies a visible notification was sent.
    - If the existing backup cron uses an LLM prompt only to reformat deterministic script output, prefer replacing it with a small wrapper script plus `no_agent=True`. Let the wrapper run the real backup command, parse stable `KEY=VALUE` / `SAVED` / `PRUNED` lines, and emit the final Discord-ready markdown directly. This is more reliable, more legible, and removes model-format drift for recurring operator posts.
    - For Dr. Sagar, default backup-channel formatting should be glanceable on mobile: strong success/failure header, archive name, human size, file counts, saved destinations, and prune summary; avoid raw `KEY=VALUE` dumps.
    - For Mnemosyne upgrades on this host, first determine the live install shape before changing anything. The current (0.2.0+ / 3.10.x) shape on this box is: `mnemosyne-memory` installed into BOTH `/usr/bin/python3` (system py3.13) AND `/usr/local/lib/hermes-agent/venv` (py3.11), and `mnemosyne-hermes` plugin installed via `pipx` in an isolated venv. Auto-discovery is via `hermes_agent.memory_providers` + `hermes_agent.plugins` entry points — no `~/.hermes/plugins/hermes-mnemosyne/` copy, no manual `config.yaml` plugin list edit, no symlink. The old `vendor repo under ~/.hermes/vendor/mnemosyne` pattern is deprecated.
    - On Debian, system pip refuses installs of `mnemosyne-memory` with `error: externally-managed-environment` (PEP 668). Use `--break-system-packages`. The apt package owns `click` with no RECORD file, so pip aborts on uninstall — add `--ignore-installed click` too. The hermes-agent venv usually has no `pip` binary at all; bootstrap it with `/usr/local/lib/hermes-agent/venv/bin/python -m ensurepip --upgrade` first.
    - For the embeddings path, install `mnemosyne-memory[embeddings]` not `mnemosyne-memory[all]`. The `[all]` extra pulls ctransformers + llama-cpp-python (10-20 min C++ compile, 2-3 GB RAM, hits the 5-min foreground terminal timeout and then some). `[embeddings]` is just fastembed + sqlite-vec + onnxruntime — what the dashboard actually needs.
    - `mnemosyne backup` / `mnemosyne reindex` auto-backup in 3.10.x fails with `no such module: vec0` when the DB has `vec_*` tables. Root cause (upstream): `create_backup()` must load sqlite-vec on **both** the source connection (for `src.backup(dst)`) **and** the in-memory destination (for `dst.iterdump()` introspecting vec0 schema). Symlink alone (`ln -sf .../sqlite_vec/vec0.so /usr/local/lib/vec0.so`) fixes name-based `load_extension('vec0')` but upstream still needs `_load_sqlite_vec(src)` and `_load_sqlite_vec(dst)` in `recovery.py`. Workarounds: `--no-backup` on reindex + manual `cp` of `.db` before upgrade; or symlink + wait for upstream fix. Upstream PR filed: https://github.com/AxDSan/mnemosyne/pull/374 (`SeaXen:fix/backup-load-sqlite-vec`). See `references/mnemosyne-upgrade-debian-pitfalls.md`.
    - `mnemosyne reindex` is a 5-10 min sustained-CPU job for ~3000 memories. On this laptop it pushes the CPU from 65°C to 87-88°C — the firmware emergency-cutoff range. Add explicit `sleep 60-90` gaps before and after it, and prefer running it when the machine can ventilate. Combine with `--no-backup` (see above) and `--yes` (skips confirmation) so the only prompt it can hit is a timeout.
    - Safe upgrade sequence: (1) stop gateway + dashboard (they hold the DB), (2) manual `cp` of the live `.db` to `~/.hermes/mnemosyne/backups/`, (3) cool-down gap, (4) system pip upgrade with `--break-system-packages --ignore-installed click "mnemosyne-memory[embeddings]"`, (5) `ensurepip` + `pip install --upgrade "mnemosyne-memory[embeddings]"` in the hermes-agent venv, (6) `pipx upgrade mnemosyne-hermes` for the plugin, (7) `vec0.so` symlink, (8) reindex with `--no-backup --yes`, (9) restart gateway + dashboard.
    - Verify all three version surfaces separately after upgrade: system pip package, hermes-agent venv package (`/usr/local/lib/hermes-agent/venv/bin/python -c "import mnemosyne; print(mnemosyne.__version__)"`), and live runtime (a freshly-restarted gateway). A running gateway reports the OLD version until restart because the provider module stays loaded in memory.
    - `mnemosyne diagnose` reports `Checks passed: X/31` but only surfaces 2-3 explicit `Key findings` lines. Do not treat the ratio as authoritative — trust the explicit lines, and run a real `SELECT COUNT(*)` on `vec_working` / `working_memory` / `fts_working` to see actual coverage.
18. For standalone/community Mnemosyne dashboards, verify them as a separate surface from Hermes' built-in `/memory` UI.
    - Confirm the active Mnemosyne DB path, the dashboard bind host/port, and the real listening socket before judging install success or LAN reachability.
    - Smoke-test in this order: overview, visualiser, knowledge graph, memories, settings, review, history.
    - If the Knowledge Graph tab is empty, check live diagnostics and a real triple query before calling it broken. `triples: 0` means the graph is data-empty, not necessarily renderer-broken.
    - The standalone/community Mnemosyne dashboard Knowledge Graph reads the SQL `triples` table specifically. Do not assume populated `annotations`, `graph_edges`, `memoria_facts`, or `memoria_kg` will make that graph render.
    - Distinguish triple-backed graph views from other visual surfaces: a Visualiser can render memory-derived structures even when the triple graph is empty.
    - When `working_memory` is populated but `triples` is still zero, explain the ingest semantics plainly: normal remembers do not backfill graph facts unless the write path explicitly uses `mnemosyne_triple_add` or `mnemosyne_remember(... extract=true)`.
    - If a page shows `Password required` while auth status says `auth_enabled: false` and `authenticated: true`, treat it as a route/API inconsistency to debug rather than as user misconfiguration.
    - Check for route-alias drift before touching auth config. In this dashboard, `History` is the `activity` section, so a stale deep link like `?tab=history` can break startup routing and fall into a generic `showLogin()` catch path even when auth is disabled.
    - Fix legacy/deep-link aliases at all three frontend routing layers: canonical tab mapping, section mapping, and subpanel mapping.
    - When verifying a history-route fix, prove canonicalization (`?tab=history` -> `?tab=activity`) and confirm the overlay stays hidden while timeline entries render.
    - Report results in three buckets: working, data-empty-but-honest, and genuinely broken/inconsistent.
    - See `references/mnemosyne-dashboard-live-qa.md` and `references/mnemosyne-dashboard-history-route-alias.md`.
35. **Assuming agy persisted file changes.** When using `agy --print` for dashboard edits, agy frequently produces a detailed plan and claims success without writing anything. Always `grep` / `read_file` the target file after agy finishes to confirm changes landed. If the file is unchanged, use `patch` directly — do not re-run agy expecting different results. This is especially critical for visual/UI work where the user can see the old layout persists.
36. When the user shares a reference image and asks for a "design like this" but the image is just one of several possible design directions, do not stop at the first interpretation. When Dr. Sagar shares a Home Assistant screenshot and says "make it like this", clarify which specific elements he wants borrowed (color palette? spacing? card style? layout?) instead of throwing away the entire existing SeaDash design. The 189-class SeaDash dashboard has years of accumulated structure; a full CSS replacement is a destructive operation that will silently delete ~150 specialized class definitions and break the layout editor, modal Save/Close, auth overlay, and most category/system info components.
  - **Escalation pattern: if the user follows up with "this looks ugly" + a second screenshot after a polish attempt, do not ask for clarification again.** Treat the second screenshot as the new authoritative reference. Move directly to the **layered-card pattern** in `devops/dashboard-ui-operations/references/seadash-nested-layered-card-pattern.md` (the `::before` pseudo overlay + floating zones for icon/badge/actions) — it is the working answer for "make my dashboard beautiful" when the user shows a Homarr / Dashy / HA-style layered card screenshot. Verify the result with `getComputedStyle(el, '::before')` to confirm the pseudo-element actually rendered, plus the standard 9-modal / 39-function save-and-close checks.
37. For SeaDash visual polish on `:9090`, default to the **appended overlay style block** pattern (a second `<style id="refined">` block before `</head>` that overrides only specific visual properties) rather than atomic CSS replacement. The atomic-swap recipe in `software-development/large-file-editing` is correct for full visual rewrites (e.g. retro CRT retrofit) but is **not** the default for "make it look better" requests. See `devops/dashboard-ui-operations/references/seadash-refined-css-overlay.md` for the worked pattern with modal-architecture preservation, `.auth-overlay` rule recovery, and the end-to-end verification script.
38. If Dr. Sagar reports "Save and Close buttons don't work" or "all my design and features look are gone" after a SeaDash CSS edit, treat that as proof that the edit broke the modal architecture or deleted class definitions. Do not assume it is a minor cosmetic issue. Restore from the most recent `index.html.bak.*` backup, then re-apply using the append-overlay pattern. Common specific causes to check in order: (1) a `.modal` rule that also targets `.modal-overlay` and conflates their display semantics, (2) missing `.auth-overlay { display: none }` rule causing the login form to cover the dashboard, (3) blanket `[class*="modal"]` selector overriding both backdrop and panel, (4) blanket replacement of the original 822-line CSS block without preserving the 189 class selectors, (5) the JS at the bottom of the file references a class name that no longer has CSS rules (cosmetic only, but visible).
39. For SeaDash edits on this host, the live process is `seadash.service` → `/usr/bin/python3 /mnt/tb/1Apps/SeaDash/server.py`. Editing `index.html` does **not** require a service restart — the Python static file handler reads from disk on every request. Just refresh the browser. Do not include `systemctl restart seadash` in the verification flow for `index.html` edits.
36. When the user lists multiple access paths and asks "can I access from all of them?", do not stop at the first single-origin limitation. Show the realistic 2-of-N coverage options, then ask whether to (a) pick one canonical URL, (b) layer a tunnel httpHostHeader rewrite, or (c) run a second instance. Same pattern applies to other "must be reachable from everywhere" asks: surface the trade-off matrix, not just the first answer.
20. When the Hermes model picker shows different models across surfaces (Discord vs dashboard vs `hermes model` CLI), the source of truth is `~/.hermes/cache/free_openrouter_catalog.json` (or whatever `model_catalog.providers.openrouter.url` points to). Both Discord/Telegram and the dashboard/CLI use the same `fetch_openrouter_models()` code path — they should show identical lists. If they differ, the catalog file is the first thing to check, then the cron job script at `~/.hermes/scripts/openrouter_free_watch.py`.
21. If a dashboard plugin frontend loads but its custom API path returns the dashboard shell HTML instead of JSON, pivot quickly to static asset delivery for low-frequency tracker data.
    - Write the generated JSON into both the normal reports path and the dashboard plugin's static asset directory.
    - Have the frontend fetch the static JSON asset instead of blocking on backend/plugin-route ambiguity.
20. For tracker-style dashboard tabs, prefer a **live-first / static-fallback** data flow.
    - On initial load, fetch the live plugin/API inventory first.
    - Use static JSON only as fallback or last-known-good data, not as the primary source of truth.
    - If the UI offers refresh/reload, wire it to a real rescan/rebuild action (for example `Scan live`) rather than merely re-reading stale static JSON.
    - When copy buttons expose commands/operators need to run, add a clipboard fallback (`execCommand('copy')` style textarea path) instead of assuming `navigator.clipboard` always works in the dashboard context.
    - Add a small **refresh health** strip (source, generated time, last refresh result, generator path) so operators can tell whether they are looking at live data or a fallback/stale view.
    - Split summary counts into **auto-tracked** versus **manual-only** items; a single total can look correct while still hiding that much of the inventory is weakly tracked.
    - In inventory mode, give operators a **hide/show manual items** toggle so manual/copied rows do not dominate the screen when they are only doing update triage.
    - For copied/manual plugin source discovery, treat inferred upstream links as **heuristics**. Rank candidate URLs by repo-name match first, then generic GitHub links, then docs/provider URLs. Never present a best-effort source link as guaranteed canonical.
    - Add one more safe source-recovery pass before leaving a copied plugin as `unknown`: if its directory name exactly matches a bundled Hermes plugin under the live Hermes source tree, surface the bundled Hermes repo path as the primary source and mark the reason explicitly as a bundled-tree match. This improves honesty for copied mirrors of built-in plugins without pretending broad auto-update support.
    - When a dashboard tab can be reached through both a normal app route and a raw/plugin route, verify the **live tracker behavior on the raw route too**. Auth-gated or cached wrapper routes can mislead you about whether the tab itself is correct.
    - For manual/copied plugin rows, make uncertainty operational instead of hidden: show a confidence label (`exact_repo`, `candidate_repo`, `related_links`, `unknown`), explain **why manual**, and give recovery actions such as `Open source`, `Search more`, `Copy all paths`, and `Copy lookup searches`.
    - If the page is visually good but still feels underfilled or ambiguous, add an **operator lane** near the top with a few high-value action/trust tiles (for example runnable actions, manual review count, weak source confidence, freshness) instead of adding more decorative stats.
    - Rename ambiguous controls to explicit operator verbs: prefer `View updates`, `View inventory`, `Run live scan` over terse labels like `Updates`, `Inventory`, `Scan live`.
    - Persist the current tracker view and manual-item visibility in `localStorage` so the dashboard reopens in the operator's last-used mode.
    - Add a freshness badge and a dedicated `Data freshness` tile so age/staleness is visible without reading timestamps.
    - For bulk/safe-update cards, expose scope before execution: safe runnable count, manual-blocked count, visible command count, and current view. Do not leave `Run all` as a context-light CTA.
    - If the tracker structure is good but the hero still feels heavy or scattered, do a beauty pass with **hierarchy, not feature changes**: strengthen hero/card separation with subtle gradients + top-edge highlight, soften borders, add light depth to operator tiles, demote helper text, and make active/inactive buttons visually distinct.
    - For top-right tracker hero actions, do not leave them as a loose wrapped row once the user asks for a premium pass. Use an explicit action cluster: two side-by-side view buttons on the first row and one wider utility action (for example `Run live scan`) spanning the row beneath. Verify the cluster actually landed with both browser vision and DOM/computed-style checks (`display:grid`, expected columns, primary-action class present).
    - After this polish pass, verify with both DOM markers and browser visual inspection. Useful markers include the top action labels, operator-lane labels, action-cluster layout, and bulk-stat labels. See `references/hermes-third-party-tracker-operator-lane-and-freshness-pass.md`.
21. For `~/.hermes` storage cleanup, audit before deleting.
    - First classify targets into: core state (`config.yaml`, `.env`, `auth.json`, `state.db`, `sessions/`, `skills/`, `plugins/`, `cron/`, `memories/`), low-risk reclaim (`state-snapshots/`, `cache/`, logs, `.bak` files), and custom-but-optional repos/scripts.
    - Prefer reclaim order: old `state-snapshots/` → cache → logs/backups → abandoned profiles → optional script repos.
    - For snapshot cleanup, keep the newest N by date/name sort and verify what remains after deletion.
    - If the user asks for an audit of MCP repo clones under `~/.hermes/scripts`, compare them against active `config.yaml` MCP server references before calling them removable.
    - On this system, check `os.path.samefile()` semantics for `/root/.hermes/...` versus `/mnt/tb/hermes/...` before deleting; they may be the same live directory.
    - If the user wants multiple paths to reflect the same live Hermes home, the safe shape is one real directory plus symlink aliases; verify with `realpath` and `os.path.samefile()`.
    - FUSE/cloud-drive mounts may reject symlink creation with `Input/output error` even when the target path is valid. If a Google Drive or similar mount cannot host symlinks, do not promise a live third alias there; use a normal backup/sync folder instead.
    - For destructive cleanup choices, present the reclaim candidates and ask before deleting anything beyond obvious cache/backups.
21. For Hermes Bitwarden migrations on Dr. Sagar's setup, standardize on the real home before touching secrets.
    - Treat `/root/.hermes` as the canonical Hermes home.
    - Treat `/mnt/tb/hermes` as a symlink alias unless samefile checks prove otherwise.
    - Before blaming missing keys or an "empty" Hermes state, verify `hermes config path`, `hermes config env-path`, runtime service `HERMES_HOME`, and whether a stale alternate home is being referenced.
22. For custom OpenAI-compatible providers in Hermes, prefer env-backed config over plaintext keys.
    - Move provider credentials out of `config.yaml` and into Bitwarden-backed env vars.
    - In `custom_providers`, prefer `key_env: VAR_NAME` over inline `api_key:` for Groq/SambaNova/Together-style providers. The same `key_env` shape applies to keyed entries under top-level **`providers:`** (v12+ schema) — not only the legacy list.
    - After migration, verify two layers separately: (a) Bitwarden is applying the env vars, and (b) `config.yaml` no longer contains plaintext `api_key` values for those providers.
22b. When Dr. Sagar asks why Groq/TokenRouter (or other env-backed endpoints) appear in the model picker but **not** in “remove custom provider”, explain the dual-schema honestly before blaming Manifest.
    - **Picker** merges `providers:` dict + `custom_providers:` list (`get_compatible_custom_providers`).
    - **Remove menu** only deletes **`custom_providers:`** list rows (`_remove_custom_provider`); dict slugs like `api.groq.com` / `tokenrouter` must be removed by editing/deleting that block under `providers:` in `config.yaml` **unless** consolidated into `custom_providers:` (worked Jun 2026: 7 dict rows moved → 10 list rows, `providers: {}`).
    - Only `providers.manifest` is the Manifest router; other slugs in `providers:` are his separate custom endpoints.
    - See `ai-model-smoke-test` → `references/hermes-providers-dict-vs-custom-providers-remove-list-jun-2026.md`.
23. After any secret migration, audit the residual secret surface, not just the active config.
    - Check `.env`, backup files, and ad-hoc config backups for old plaintext keys.
    - Treat generated backups like `config.yaml.pre-...bak` as sensitive until deleted or rotated.
    - Do not call the migration complete if the live config is clean but the fallback backup still contains the old secrets.
24. When the user asks for a command to view current provider keys, prefer narrow local extraction over broad secret dumps.
    - Print only the targeted provider fields from `config.yaml` or only the specific env vars needed.
    - Avoid general Bitwarden secret-list commands in chat guidance because some output modes expose full secret values for unrelated entries.
25. For end-to-end proof of Hermes custom providers, test the runtime resolver directly before blaming auth or config.
    - Prefer Hermes' own venv plus `PYTHONPATH=/usr/local/lib/hermes-agent` and a short Python probe that calls `hermes_cli.env_loader.load_hermes_dotenv()` and `agent.auxiliary_client.resolve_provider_client(provider, model=...)`.
    - Then run a minimal `client.chat.completions.create(...)` with a strict echo prompt like `Reply exactly: PROVIDER_OK`.
    - This proves the real Hermes env-loading + Bitwarden injection + provider client resolution path, without relying on chat-surface extras.
26. If `hermes chat` fails against a custom provider during verification, separate CLI payload issues from provider wiring.
    - A failure about oversized `tools` arrays or other request-shape noise is not proof the API key is wrong.
    - For provider proof, fall back to the direct runtime resolver test above.
27. For OpenAI-compatible provider probes, interpret failure modes precisely.
    - Provider HTTP billing errors like Together `402 credit_limit exceeded` mean Hermes reached the provider successfully; the remaining problem is provider account state, not Bitwarden wiring.
    - For SambaNova-style models, too-small `max_tokens` can yield `finish_reason=length` with empty `content` and reasoning text. Increase token budget before calling it a config/auth failure.
28. For OpenAI Codex pooled-auth questions, separate **configured strategy** from **effective healthy pool** before explaining behavior.
    - Check both the configured strategy (`credential_pool_strategies.openai-codex`) and the live pool entry states.
    - `round_robin` only rotates across **available** entries. `dead` entries never participate, and `exhausted` entries stay out until cooldown/reset passes.
    - If the user says "it only uses one auth", do not blame the strategy first. Inspect the pool for `ok` vs `dead` vs `exhausted` entries and explain the effective usable set.
    - Practical reading rule: one `ok` entry plus the rest `dead`/`exhausted` means the observed behavior is effectively single-auth even under `round_robin`.
    - Good operator answer shape: (1) strategy setting, (2) live per-entry statuses, (3) effective healthy set, (4) exact consequence, (5) re-auth/remove stale dead entries if needed.
    - See `references/openai-codex-pooled-auth-effective-single-entry.md`.
29. For Hermes secret/Bitwarden operator UI, prefer Mission Control → Controls with internal sub-tabs/cards over a new top-level page.
    - Show masked presence/source/health metadata, never raw secret values.
    - If the shipped plugin lacks editable source TS/TSX, patch the served backend/frontend pair together: `plugins/mission-control/dashboard/plugin_api.py` and the bundled `dist/index.js`.
    - Build the payload from live Hermes config plus runtime env after `load_hermes_dotenv()` so Bitwarden-injected keys are reflected, not just on-disk `.env` state.
    - Verify the actual dashboard service/port from the systemd unit before judging plugin/API behavior; wrapper routes or secondary ports can return shell HTML, 401s, or 405s that do not represent the real Mission Control surface.
    - Finish with four checks: syntax/import, direct backend function call, authenticated plugin HTTP probe, and browser UI confirmation on the live dashboard route.
30. When custom dashboard tabs vanish from `:9119` / `:9120` **or** tabs load but show `No such API endpoint` for `/api/plugins/<name>/...`, check **`plugins.enabled` and dashboard restart** before blaming manifests or rebuilds**.
    - `GET /api/dashboard/plugins` filters **user** plugins to names in `plugins.enabled` (not in `plugins.disabled`). Bundled tabs only check `plugins.disabled`.
    - **Sidebar vs API:** enablement updates the nav list live; `plugin_api.py` routes mount **only at dashboard startup**. After `hermes plugins enable`, run `sudo systemctl restart hermes-dashboard.service` (or equivalent) so Memory/Cronalytics/Mission Control backends work.
    - Manifests live at `plugins/<name>/dashboard/manifest.json`; missing nav is often enablement, not deletion.
    - Probe: `curl -s http://127.0.0.1:<port>/api/dashboard/plugins` vs on-disk manifests; grep logs for `Mounted plugin API routes`.
    - Fix: `hermes plugins enable <name>` then **restart dashboard**; hard-refresh browser. `rescan` alone is insufficient for API 404s.
    - See `references/dashboard-user-plugins-enabled-gate.md` and `references/hermes-mission-control-plugin-registration-and-api-mount.md`.
31. For Hermes dashboard plugin registration failures (`did not call register()` / route appears then disappears), debug the manifest, SDK contract, backend route mount, and the ACTUAL live dashboard process separately.
    - Normalize the manifest to the current dashboard shape: stable slug in `name` (for example `mission-control`), user-facing text in `label`, route under `tab.path`, icon in the dashboard's expected case, and `api` pointing to a relative file inside `dashboard/`.
    - Do not assume a plugin backend route is broken from a raw unauthenticated fetch alone. First fetch `/`, extract `window.__HERMES_SESSION_TOKEN__`, then send `X-Hermes-Session-Token` for plugin API probes.
    - In `plugin_api.py`, do not duplicate the global route prefix. Hermes mounts plugin routers under `/api/plugins/<name>` already; if the router itself also uses that prefix, the real endpoint becomes doubled and the frontend will 404.
    - Keep plugin backend imports minimal and runtime-valid for the dashboard server process. A stray import like `from hermes.agent.plugins import ...` can stop route mounting entirely even when the static JS bundle still loads.
    - For plugin frontend API calls inside the dashboard, prefer `window.__HERMES_PLUGIN_SDK__.fetchJSON(...)` or `SDK.api.*` over plain `fetch(...)` so the dashboard session token is attached automatically.
    - Before using SDK widgets, inspect what the injected SDK actually exposes. If components like `TableHead`, `TableRow`, `TabsContent`, or richer table helpers are absent, either rewrite to plain HTML or use only the provided primitives.
    - If the plugin still renders stale empty state after a rebuild, verify four things independently: the served bundle content under `/dashboard-plugins/<name>/dist/index.js`, the plugin manifest returned by `/api/dashboard/plugins`, the live authenticated API response, and whether the browser is still pointed at a stale dashboard process/port.
    - If multiple dashboard processes exist, kill the stale/noncanonical one, restart the real `:9120` process cleanly, and only then judge whether Mission Control is fixed.
    - When restoring/expanding Mission Control, prefer a stable three-lane shape that is more featureful than the stock dashboard without depending on unsupported SDK components: **Continuity** (session queue, search, pinning, transcript preview, resume command), **Ops** (telemetry, top models, provider board, cron health), and **Config** (curated highlights plus raw snapshot lane).
    - For Mission Control specifically, use the host SDK/API for the richer surfaces instead of inventing extra backend endpoints when the existing dashboard APIs already cover them (`getSessions`, `getSessionMessages`, `getSessionLatestDescendant`, `getAnalytics`, `getModelsAnalytics`, `getSkills`, `getToolsets`, `getCronJobs`, `getProfiles`, `getModelInfo`).
31. When Dr. Sagar reports that the Hermes host laptop/server "auto turned off" overnight, default to a power-loss diagnosis before blaming Hermes cron.
    - First classify schedule reality: check the machine timezone and list Hermes cron jobs to see whether anything is even scheduled in the reported window.
    - Then classify shutdown shape from evidence that survives reboot: current boot time, journal boot list, filesystem recovery messages (`EXT4-fs ... recovery complete`), and battery/power-supply telemetry from `/sys/class/power_supply/*`.
    - Strong evidence for abrupt power loss is: rebooted service uptime, ext4 journal recovery, no clean shutdown trail, and a severely degraded battery (`energy_full` far below `energy_full_design`) that cannot bridge a brief AC drop.
    - Do not over-claim thermal shutdown without explicit critical thermal or panic lines in logs.
    - Hermes can still be a contributing load factor: check gateway/service memory footprint and lingering browser/MCP child processes separately from the root-cause call.
    - Frame the answer in three buckets: what Hermes likely did not do (no matching cron), what the host evidence suggests (abrupt power loss), and what should be instrumented next (power/battery logging and process cleanup).
    - For persistent hardware-degradation conditions like battery health stuck far below threshold, do not keep noisy recurring alerts just because the watchdog runs frequently. Prefer keeping the minute-level CSV/logger active while either (a) disabling that chronic alert class behind an explicit script toggle, or (b) moving it to a much longer cadence such as daily. Reserve high-frequency notifications for state changes or acute risk (AC offline, thermal spikes, sustained CPU/RAM stress).
    - See `references/overnight-auto-off-vs-hermes-cron.md` and `references/power-thermal-watch-chronic-alert-tuning.md`.
30. When Telegram/Discord disappear after a gateway restart, do not assume the immediately preceding MCP toggle/edit caused it.
    - First separate **platform config loss** from **secret reinjection loss**.
    - Check whether the restarted gateway came up with only `api_server` or fewer platforms than before.
    - If Bitwarden-backed secrets are enabled, inspect `hermes secrets bitwarden status` and compare that result with `~/.hermes/cache/bws_cache.json`.
    - Important interpretation: a live `401 Unauthorized` from Bitwarden during restart can coexist with a recent disk cache that still contains `TELEGRAM_BOT_TOKEN` and `DISCORD_BOT_TOKEN`.
    - In that case, explain the real chain precisely: cached secrets kept the old process working, cache TTL expired, restart forced a fresh fetch, fresh Bitwarden fetch failed, so Telegram/Discord tokens were not injected into the new gateway process.
    - Separate **Bitwarden-managed secrets** from **direct `.env` fallbacks**. If `TELEGRAM_BOT_TOKEN` / `DISCORD_BOT_TOKEN` are already present in `.env`, gateway/platform health can remain green even while live Bitwarden fetch is dead.
    - When a user says "I changed the token, so this cannot be a token issue", verify three things before agreeing: (1) direct `bws secret list <project_id> --output json --server-url ...`, (2) `.env` token formatting sanity with no quotes/whitespace/CRLF corruption, and (3) whether the current token fingerprint matches the disk-cache key.
    - High-value diagnostic pattern: if the current token fingerprint matches `~/.hermes/cache/bws_cache.json` and that cache timestamp predates the restart, then the same token worked recently and later started 401ing. That points to Bitwarden-side revocation/access/project-scope change after the cache write, not MCP toggles or bad local formatting.
    - Do not over-credit the MCP change itself unless the platform section was actually removed from config. A restart after MCP edits often only **exposes** a pre-existing Bitwarden auth problem.
    - Recovery split: real fix = restore Bitwarden fetch health for the configured token/project; temporary fix = longer Bitwarden cache TTL or direct `.env` tokens for the affected bots.
    - When Dr. Sagar asks for a Bitwarden watchdog, do not stop at `bws secret list ...` success. A useful Hermes watchdog should verify the full chain: **Bitwarden live fetch**, required project secrets (at least `TELEGRAM_BOT_TOKEN` + `DISCORD_BOT_TOKEN`), **gateway runtime** connectivity from `~/.hermes/gateway_state.json`, **dashboard API** connectivity from `http://127.0.0.1:9120/api/status`, and any **runtime/dashboard drift**.
    - Preferred notification policy for that watchdog: **silent on healthy runs**, **silent on recovery unless explicitly requested**, and **post only on new problems/errors** with deduping of unchanged ongoing failures.
    - Preferred alert format: compact mobile-readable Discord markdown with `Time / Project / Server / Dashboard`, then a `Summary` checklist using `✅/❌`, then a short `Problems detected` block. Avoid noisy raw dumps.
    - See `references/gateway-bitwarden-cache-expiry-and-platform-drop.md`, `references/bitwarden-watchdog-escalation-and-drift-checks.md`, and `references/bitwarden-401-after-restart-cache-vs-env.md`.
31. When a Discord slash command is missing even though Hermes source supports it, treat it as a **slash-command sync/cache issue** before claiming the command is unavailable.
    - First inspect the live command definition in source and verify whether the command exists as a `tree.command(...)` registration.
    - Then check gateway logs for Discord sync behavior, especially lines like `Skipping Discord slash command sync: same slash-command fingerprint already synced`.
    - If the command exists in source but not in Discord UI, explain that Discord may still be serving a stale registered set or cached client view.
    - Distinguish **unsupported command** from **registered alias/equivalent**. Example: `/new` and `/reset` can both map to the same internal action, so `/reset` may be a valid immediate workaround while `/new` is absent from the picker.
    - Do not tell the user the command is unsupported unless source and registration evidence both agree.
    - See `references/discord-slash-command-stale-sync.md`.
33. For **Learnables** (research-before-`/learn` on Discord/Telegram), use the user-local package under `~/.hermes/learnables/` plus skill `learnables-workflow` — not a one-off channel prompt in chat memory.
    - Committed skills land in **`~/.hermes/skills/learnables/`** (category `learnables`), not `devops/`, unless the user overrides.
    - Wire channels with `apply_config.py` (`channel_prompts`, `channel_skill_bindings`, Discord `free_response_channels`).
    - Enable `discord` toolset for thread create + `fetch_messages`.
    - Gateway hook rewrites commit-style `/learn` to a queued learnables commit prompt; empty `/learn` in the room is governed by channel_prompt + skill (hook lacks `chat_id` today).
    - See `references/hermes-learnables-channel-workflow.md` and skill `learnables-workflow` → `references/gateway-wiring.md`.
    - **Learnables topic skills (load instead of duplicating here):** `cron-wakeagent-prerun-gates` — LLM cron + pre-run script + last-line `{"wakeAgent": false|true}` to poll often and spend tokens only when state changed; `hermes-gateway-safe-restart` — restart from external shell or `/restart`, verify `status` + journal, TEMPFAIL `reset-failed` recovery (not from inside gateway process).
34. For **gateway restart** on this host (user `hermes-gateway.service`), follow skill `hermes-gateway-safe-restart` end-to-end; after restart, if Telegram/Discord drop, use workflow §30 (Bitwarden cache vs `.env`) before blaming the last config edit.
35. For **frequent cron polls** that need the LLM only on change, use `wakeAgent` gates per `cron-wakeagent-prerun-gates`; use `no_agent=True` only when script stdout is the entire message (see `references/deterministic-backup-cron-formatting.md`).
33. When the Hermes gateway logs show `ERROR gateway.platforms.api_server: [Api_Server] Refusing to start: API_SERVER_KEY is a placeholder or too short (<16 chars)`, the API server endpoint is intentionally disabled — not a connectivity issue.
    - The gateway refuses to start the API server when `API_SERVER_KEY` looks placeholder-ish or is shorter than 16 chars because that endpoint dispatches terminal-capable agent work; a guessable key is treated as remote code execution exposure.
    - Common symptom: gateway is `active (running)`, but API port is NOT listening and dashboard/platform health shows `api_server` disconnected.
    - Fix: generate a strong secret and update it in ALL Hermes config locations:
      ```bash
      NEW_KEY=$(openssl rand -hex 32)
      ```
      Then update in order:
      1. `~/.hermes/.env` → `API_SERVER_KEY=<hex>`
      2. `~/.hermes/config.yaml` → `API_SERVER_KEY: <hex>` under the top-level config section
      3. Each active profile: `~/.hermes/profiles/<name>/.env` and `~/.hermes/profiles/<name>/config.yaml` if they contain `API_SERVER_KEY`
    - **CRITICAL `.env` format note:** inside `.env` files, the line MUST be `API_SERVER_KEY=<value>`, not `API_SERVER_KEY: <value>`. The colon form silently breaks dotenv parsing.
    - `hermes config set api_server_key <hex>` updates the main `config.yaml`, but older versions/configs may still read `API_SERVER_KEY:` instead. After `hermes config set`, grep for BOTH `API_SERVER_KEY:` and `api_server_key:` and normalize to `API_SERVER_KEY:` with a real value.
    - After updating all locations, restart with `hermes gateway restart` and verify with `ss -tlnp | grep <expected-port>` plus a local API probe.
    - See `references/api-server-placeholder-key-refusal.md`.
32. When the dashboard Connected Platforms card shows only `api_server` but the gateway is actually serving Telegram/Discord too, treat it as a **dashboard-process environment mismatch** before blaming the gateway.
    - Verify three layers separately: `hermes status --all`, the gateway runtime status file (`gateway.status.read_runtime_status()`), and the dashboard API response from `/api/status`.
    - If `hermes status --all` and the runtime status file show `telegram`, `discord`, and `api_server` as connected, but `/api/status` reports only `api_server`, the dashboard is under-reporting — the gateway is not the problem.
    - Root cause pattern: the dashboard backend filters runtime platform state through `load_gateway_config().get_connected_platforms()`. If the dashboard process was started without `TELEGRAM_BOT_TOKEN` / `DISCORD_BOT_TOKEN` in its own environment, it believes only `api_server` is configured and strips Telegram/Discord from the API payload even while the gateway itself is connected.
    - Diagnose by comparing the environment of the running dashboard PID(s) versus the gateway PID. Multiple manually started dashboards on different ports are a common clue.
    - Report it precisely as **dashboard state mismatch** or **dashboard lying about connected platforms**, not as a platform outage.
    - Preferred fix: stop stray/manual dashboard processes and relaunch the dashboard from the proper Hermes/Bitwarden-loaded environment so `/api/status` reflects the real gateway runtime.
        - First classify the live CLI path versus the service-unit path. A common failure is `hermes` working from `~/.local/bin/hermes` while systemd units still point at old `/usr/local/bin/hermes` or `/usr/local/lib/hermes-agent/venv/bin/python` paths.
        - `status=203/EXEC` in `systemctl status` is the tell for dead ExecStart targets after an install-layout change.
        - After patching stale `ExecStart` and PATH entries, always `daemon-reload`, restart, and read the journal again. The next blocker may be a packaging/runtime import failure from the new install, which is a second layer and not evidence that the service-unit fix was wrong.
        - A practical second-layer split matters here:
          1. imports/runtime can be fixed by the reinstall (`hermes_cli.dashboard_auth`, `fastapi`, `uvicorn` now import)
        - If journal shows `--skip-build was passed but no web dist found`, treat that as a separate web-asset recovery problem rather than another service-path failure.
        - Report recovery in layers: (1) service path mismatch fixed, (2) imports/runtime fixed, (3) web-dist recovery applied if needed. This keeps the diagnosis honest and avoids conflating the layers.
        - See `references/hermes-uv-tool-service-path-recovery.md` and `references/hermes-reinstall-missing-web-dist-recovery.md`.

## Common Pitfalls
1. Declaring dashboard fixes from static inspection only.
2. Trusting `hermes mcp test` for OAuth servers — it starts fresh flow each run; real chat usage works via cached tokens.
3. Trying bearer-token MCP configs for OAuth-only endpoints (e.g. `cloudflare-api-token` with API key → 400 invalid_token).
4. MCP wrapper scripts reading `.env` instead of Bitwarden-injected env vars — prefer env var, fall back to `.env`.

## Verification Checklist
- procedural or operational notes belong in a skill, not USER.md or MEMORY.md
- risky memory experiments belong in a throwaway profile, not the main one
- SeaDash/Hermes fixes should only be saved after verification

## Common Pitfalls
1. Declaring dashboard fixes from static inspection only.
2. Testing experimental memory providers in the main profile.
3. Saving procedural ops notes into durable memory instead of a skill.
4. Using vague explanations for self-improvement instead of plain language.
5. Installing a renamed third-party Hermes dashboard clone that is not actually the upstream UI.
6. Trusting README claims about a dashboard repo without checking whether it really ships only a theme or also ships plugin/backend code.
7. Treating authenticated dashboard API 401s as proof the plugin route is broken.
8. Editing the wrong Obsidian dashboard path because the running service uses a different script location.
9. Claiming a recall feature works after code changes without checking the live `/api/...` response and browser panel.
10. Reaching for embeddings by default when a local FTS5 + graph/token blend is enough and the environment lacks the heavy dependencies.
11. Using chat history as the primary source of truth for unofficial Hermes installs when the live filesystem/config can be inventoried directly.
12. Shipping a scheduled inventory notifier that dumps the whole list every run instead of only actionable updates.
13. Sticking with a non-working custom dashboard plugin API path when static JSON asset delivery would solve the low-frequency reporting need more simply.
14. For tracker/dashboard tabs, trusting static JSON as the primary source of truth after the live system changed. Fetch live inventory first; use static JSON only as fallback/last-known-good.
15. Wiring a refresh button that only re-reads cached/static data instead of triggering a real rescan/rebuild.
16. Leaving copy-to-clipboard dependent only on `navigator.clipboard`; dashboard/browser contexts may need a textarea + `execCommand('copy')` fallback.
17. Verifying only through an auth-gated or cached wrapper route and then misjudging the real tracker/plugin tab. Check the raw/plugin route too when available.
18. Pretending manual/copied plugin source attribution is authoritative when it is only heuristic. Expose confidence and recovery actions instead.
17. Leaving a stray test/demo dashboard plugin in the live plugin list when it has a manifest but no built assets. If a plugin like `example-dashboard` exists only for test coverage and injects a 404ing `/dashboard-plugins/example/dist/index.js`, prefer hiding it through `dashboard.hidden_plugins` in Hermes config instead of editing Hermes core files.
18. Verifying only through an auth-gated or cached wrapper route and then misjudging the real tracker/plugin tab. Check the raw/plugin route too when available.
19. Pretending manual/copied plugin source attribution is authoritative when it is only heuristic. Expose confidence and recovery actions instead.
20. Leaving CHEAP/paid models in `free_openrouter_catalog.json` — the picker reads ALL entries, not just free ones. Both Discord/Telegram and dashboard use the same `fetch_openrouter_models()` path. If paid models appear in the picker, check the catalog file first.
21. Forgetting that the hourly cron job (`openrouter_free_watch.py`) rebuilds the catalog — manual edits to `free_openrouter_catalog.json` are overwritten unless the script is patched. The cron job preserves CHEAP entries from previous runs (`free_models + cheap_models` on line ~195), so cheap models accumulate unless the script is patched.
22. Unilaterally removing CHEAP models from the catalog without user confirmation. The user may intentionally want both free AND cheap low-cost models available. When the user asks to "fix" model picker discrepancies, ask whether they want cheap models kept or removed before editing. The fix might be making both surfaces use the same catalog, not restricting the catalog to free-only.
34. **Assuming agy wrote the file.** agy frequently produces a plan and claims success without persisting changes. Always verify with `grep`/`read_file`. Fall back to `patch` if agy didn't write.

35. **Discord webhook delivery DNS failures with Tailscale DNS.** The Tailscale DNS resolver (`100.100.100.100`) can intermittently fail to resolve `discord.com`, causing `Cannot connect to host discord.com:443 ssl:default [Temporary failure in name resolution]`. This is an infrastructure issue, not a script bug. Mitigations:
   - Use Telegram as primary delivery (more reliable on this network)
   - Add retry logic to Hermes webhook delivery (requires core change)
   - Consider alternative DNS (Cloudflare 1.1.1.1, Google 8.8.8.8) instead of pure Tailscale DNS
   - Cron jobs showing this error are not "broken" — they ran successfully but couldn't deliver the notification
24. Treating `~/.hermes/scripts/mcp-servers/...` as separate from `/mnt/tb/hermes/scripts/mcp-servers/...` without verifying samefile semantics first. On this system they can be the same live directories, so deleting one path deletes the configured MCP server repo too.
25. Calling an MCP repo clone removable just because it sits under `scripts/`. First compare against active MCP server config; enabled+referenced repos are not cleanup candidates.
26. Deleting high-value Hermes data (`state.db`, `sessions/`, `skills/`, `plugins/`, `memories/`, `cron/`) during storage cleanup when the user only asked for safe reclaim. Prefer snapshots/cache/logs/backups first and ask before broader deletes.
27. Assuming that cleaning Mnemosyne makes built-in memory noise irrelevant. Hermes still loads built-in `MEMORY.md`/`USER.md` alongside the external provider, so stale `MEMORY.md` content remains active until cleaned.
28. Treating a dashboard plugin patch as live just because the files changed on disk. Verify the live route/API, and if the old behavior persists, rescan plugins and restart the dashboard before concluding anything.
28b. Enabling a user dashboard plugin and stopping there when the tab still 404s on `/api/plugins/<name>/...`. Rescan does not remount `plugin_api.py`; restart the dashboard process after enablement.
29. Cleaning the active `config.yaml` but forgetting that `.bak` or pre-migration backups still contain plaintext provider keys.
30. Using broad `bws secret list` output as a convenience check in chat guidance; it can expose unrelated live secret values instead of only the targeted provider key.
31. Answering Hermes approval-button questions generically without mapping them to the actual persisted state. `Always Allow` is not a vague preference toggle; it writes to `command_allowlist`, while `Allow Session` is ephemeral and requires no config edit.
32. Verifying only list/delete/clear on an `Always Allow` dashboard panel and forgetting the create path. If the panel lets users add patterns, prove add semantics too: trim input, reject empty values, dedupe exact duplicates, and restore the live allowlist state after testing.
33. Blaming Hermes cron first when the host auto-powered off overnight. If the reported time window has no matching cron jobs, the battery is badly degraded, and boot evidence shows ext4 recovery, call it what it is: likely abrupt power loss, with Hermes load only a secondary factor until proven otherwise.
34. Suggesting more local Hermes browser retries after Dr. Sagar reports that browser automation overheats the laptop or can trigger sudden shutdown. Pivot to `web_search`/`web_extract`, remote CDP, or a cloud browser instead.
35. For Dr. Sagar's recurring laptop thermal shutdowns at 80–95°C, treat it as a **firmware emergency cutoff**, not a Linux kernel thermal event. Kernel `trip_point_*_temp` critical thresholds on this kind of laptop are 100–115°C, so a hard-cut at 88°C means the BIOS/Intel Tjmax did it. The next investigation step is finding the runaway process, not changing Linux trip points.
    - Default to the minute-level `power_watch.sh` + `boot_watch.sh` instrumentation shape from `systematic-debugging/references/thermal-shutdown-triage.md`. The crash signature in those logs is a stable last-reading temperature across incidents, then a hard gap with no entries, then a new `boot_id`.
    - On Dr. Sagar's DietPi/laptop host with kula + Hermes + many Docker containers, the most common cause is **dockerd + containerd eating 30–40% CPU on control-plane churn** while per-container `docker stats` look idle. The two specific patterns to look for first are: (1) `cloudflared-web` in a parallel-tunnel reconnect loop (4 simultaneous "Failed to dial quic" lines in `journalctl -u docker`), and (2) any container with `docker inspect ... FailingStreak` > 5, indicating an image-defined healthcheck failure loop burning daemon CPU.
    - When the user wants immediate relief, `echo 2000000 > /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq` is the no-install cap-frequency escape hatch. Persistent fix is to stop/remove the runaway container and install `thermald` + `tlp` so the CPU throttles before the firmware cutoff.
    - Reference: `systematic-debugging/references/thermal-shutdown-triage.md` for full triage.
36. Upgrading `mnemosyne-memory` via plain `pip install --upgrade` on this Debian host. PEP 668 blocks system pip, apt owns `click` with no RECORD file, and `[all]` extras take 5+ min to compile from C++ source. The right shape is `pip install --upgrade --break-system-packages --ignore-installed click "mnemosyne-memory[embeddings]"` for system pip, plus a separate `python -m pip install --upgrade "mnemosyne-memory[embeddings]"` inside the hermes-agent venv (after `ensurepip` if the venv has no pip). `[all]` is rarely what you want — `[embeddings]` is what the dashboard needs.
37. Running `mnemosyne reindex` without `--no-backup` on a 3.10.x DB that has `vec_*` virtual tables. Auto-backup fails with `no such module: vec0` unless upstream loads sqlite-vec on **both** src and dst in `create_backup` (see PR #374). Symlink `vec0.so` helps name-based loads; still use `--no-backup` + manual `cp` until upstream merges. Pace with thermal gaps — partial reindex leaves `vec_working` < `working_memory`; FTS5 still full coverage.

## Reference

- `references/aceroute-global-duration-all-time.md` — AceRoute global Settings duration, true all-time (`36500`), Docker rebuild vs static mount, half-empty UI diagnosis.
- `references/hermes-telemetry-dashboard-token-panels.md` — local `hermes-telemetry` token tables + one-chart combined daily token/model breakdown pattern on port 8009, including all-time=last-90-days behavior and verification checks.

- `references/mcp-test-vs-chat-usage.md` — `hermes mcp test` starts fresh OAuth flow each run (false negatives); cached tokens in `/root/.hermes/mcp-tokens/` power actual chat usage; manual JSON-RPC with cached token is the real verification.
- `references/mcp-wrapper-script-bitwarden-secrets.md` — stdio MCP wrapper scripts must prefer Bitwarden-injected env vars over `.env` files; manual JSON-RPC bypasses false-negative test results.
- `references/hermes-dashboard-third-party-audit-and-feature-port.md` — repo classification, live verification, auth-gated plugin checks, and when to pivot from renamed install to feature-porting.
- `references/general-mcp-server-addition.md` — reusable pattern for adding public MCP servers via `hermes mcp add` (uvx/npx/pipx), hook flag placement, auto-confirm tool enablement, OAuth test vs chat caveat, session cookie/env var setup, and new-session requirement.
- `references/mission-control-feature-port-sequencing.md` — recommended Mission Control feature order, regression-restoration pattern, and ISO-datetime → `timeAgo(...)` conversion rule.
- `references/obsidian-dashboard-hybrid-recall.md` — lightweight hybrid recall pattern for the Obsidian read-only dashboard: FTS5, graph/tag/folder/recency reranking, runtime path checks, and verification sequence.
- `references/hermes-third-party-inventory-and-dashboard-tracker.md` — low-noise inventory/update workflow for unofficial Hermes additions, plus the static-JSON dashboard-tab fallback.
- `references/hermes-third-party-tracker-10of10-hardening.md` — practical tracker hardening patterns: raw-route verification, live-first refresh, manual-source confidence labels, operator utility actions, and honest handling of heuristic source attribution.
- `references/openrouter-model-catalog-and-picker.md` — model catalog file map, picker architecture, cron job behavior, and how to fix paid models appearing in the picker.
- `references/hermes-mcp-onboarding-from-agent-specific-repos.md` — how to translate Claude/Codex/Cursor-style skill repos into the correct Hermes MCP/backend setup, including wrapper-script and `hermes mcp add` confirmation pitfalls.
- `references/hermes-home-cleanup-and-mcp-repo-audit.md` — safe reclaim order for `~/.hermes`, snapshot-pruning pattern, MCP repo-clone audit rules, and the `/root/.hermes` vs `/mnt/tb/hermes` samefile pitfall.
- `references/mnemosyne-dashboard-triples-vs-annotations.md` — why the Mnemosyne dashboard graph can stay empty with `triples=0` even when annotations, graph_edges, and MEMORIA stores are populated; includes the operator explanation and empty-state guidance.
- `references/mnemosyne-memory-ui-and-builtin-memory-cleanup.md` — safe `MEMORY.md` cleanup when Mnemosyne is active, plus the minimal read-only dashboard pattern for exposing Mnemosyne data.
- `references/hermes-encrypted-backup-and-test-restore.md` — encrypted full-home backup shape, FUSE/cloud symlink pitfall, and the manual restore-proof workflow using `HERMES_HOME` against the restored tree.
- `references/mnemosyne-local-core-audit-and-backup-staging.md` — direct/local Mnemosyne audit sequence, docs-parity standardization checks, and the `/tmp` tmpfs staging pitfall for large Hermes backups.
- `references/hermes-no-agent-cron-success-notifications.md` — `no_agent=True` cron delivery semantics, why `last_status: ok` can still mean no channel post, and the compact stdout-success pattern for backup channels.
- `references/deterministic-backup-cron-formatting.md` — when a recurring backup post is ugly or model-variable, replace the formatting-only agent cron with a wrapper script plus `no_agent=True` and emit clean Discord-ready markdown directly.
- `references/notebooklm-mcp-auth-on-linux-desktop.md` — NotebookLM-specific Hermes onboarding pattern: classify agent-specific repos correctly, keep a headless runtime wrapper, and use a temporary GUI-capable auth helper MCP entry for first Google login.
- `references/mcp-wrapper-script-bitwarden-secrets.md` — Fix pattern for stdio MCP wrapper scripts that read `.env` files instead of Bitwarden-injected env vars; manual JSON-RPC verification to bypass false-negative `hermes mcp test` results.
- `references/hermes-bitwarden-custom-providers.md` — Bitwarden Secrets Manager workflow for Hermes on Dr. Sagar's setup: canonical `HERMES_HOME`, custom provider `key_env` migration, verification steps, and cleanup caveats for backups that still contain old plaintext keys.
- `references/custom-provider-credential-pools.md` — how to add multiple API keys to one custom provider, set `credential_pool_strategies`, and understand the `/v1/models` picker limitation.
- `references/hermes-desktop-remote-connection.md` — Hermes Desktop app remote connection: how it works, server-side setup, client-side config, CF Tunnel behavior, session TTL.
- `references/mission-control-bitwarden-controls.md` — Mission Control → Controls Bitwarden UI pattern: safe metadata, runtime payload shaping, real-port verification, and live browser/API checks.
- `references/dashboard-user-plugins-enabled-gate.md` — custom dashboard tabs hidden when `plugins.enabled` omits them; API probe and `hermes plugins enable` recovery.
- `references/hermes-mission-control-plugin-registration-and-api-mount.md` — Mission Control/dashboard plugin failure pattern: manifest normalization, doubled API-prefix pitfall, SDK component mismatch, authenticated fetches, and backend import/mount checks.
- `references/dashboard-connected-platforms-env-mismatch.md` — dashboard-only `api_server` symptom when the gateway runtime is healthy but the dashboard process lacks Telegram/Discord env-backed secrets.
- `references/hermes-learnables-channel-workflow.md` — Learnables research rooms: apply_config, channel_prompts, hook limits, Discord toolset
- Skill `learnables/cron-wakeagent-prerun-gates` — `$0` pre-run gates, file/flag/SQL patterns, vs `no_agent`
- Skill `learnables/hermes-gateway-safe-restart` — safe restart workflow, in-gateway refusal, TEMPFAIL recovery
- `references/local-web-service-port-inspection.md` — 5-step recipe (ss -> systemctl show -> curl -> browser_navigate -> browser_vision) for "check X on port Y" requests. Verified on SeaDash `:9090`, generalizes to any local dashboard. — 5-step recipe (ss -> systemctl show -> curl -> browser_navigate -> browser_vision) for "check X on port Y" requests. Verified on SeaDash `:9090`, generalizes to any local dashboard.
- `references/medsea-live-browser-verification.md` — MedSea `:8855` browser pass before claiming exam/flashcards/header done; `fmtDateTime`/exam-engine fatal, SW stale HTML, topic URL probe.
- `references/dietpi-samba-and-cloudflare-smb.md` — Windows `\\192.168.0.222\HDD`, `smbpasswd`, WARP private route for SMB (not HTTP tunnel).

- `references/mcp-browser-leak-diagnostic.md` — host hangs / swap thrashing on memory-constrained hosts; almost always an MCP server with a headless browser pool that did not clean up. Diagnostic order, kill-the-right-order, what NOT to do (pkill chromium blanket, killing MCP parent first).
- `references/overnight-auto-off-vs-hermes-cron.md` — overnight auto-off triage for Dr. Sagar's Hermes host: timezone/cron cross-check, battery-health evidence, ext4 recovery clues, and how to separate root-cause power loss from Hermes load.
- `references/power-thermal-watch-chronic-alert-tuning.md` — how to keep minute-level power/thermal logging while suppressing chronic battery-health spam from no-agent watcher jobs.
- `references/hermes-profile-clone-pitfalls.md` — `hermes profile create --clone-all` copies all runtime state (state.db, cache, logs = 3+ GB); use `--clone` for config/keys/skills only (~100 MB).
- Skill `hermes-project-context-maps` — INDEX.md vs AGENTS.md, curated `/mnt/tb` + Hermes home maps, weekly index cron
- `memory-hygiene` — canonical low-noise save policy for USER.md, MEMORY.md, skills, and Fabric.
- `fabric-writing-policy` — stricter destination-specific policy for Fabric entries.
- `references/mnemosyne-docker-image-issue.md` — Mnemosyne GHCR image is private; use Python package or local build instead
- `references/mnemosyne-upgrade-debian-pitfalls.md` — Debian 13 + DietPi upgrade recipe for mnemosyne-memory / mnemosyne-hermes: PEP 668 + apt-owned `click` workaround, `[embeddings]` vs `[all]` choice, `vec0.so` symlink for the 3.10.x `no such module: vec0` backup bug, hermes-agent venv `ensurepip` bootstrap, multi-Python upgrade sequence, reindex thermal timing.
- `references/termix-docker-deployment.md` — Termix self-hosted SSH/desktop management Docker deployment: correct image (`ghcr.io/lukegus/termix:latest`), port mapping (host:30001 → container:8080), data persistence, Windows app connection via Custom Server URL, Cloudflare Tunnel HTTP/SSH patterns, verification steps, and pitfalls avoided
- `references/rapl-energy-monitoring.md` — RAPL CPU+DRAM energy logging via existing `power_watch.sh` cron + `energy_report.py` daily report; covers what RAPL captures/misses, boot_id reset handling, daily Discord notification cron, and why software-only can't measure wall draw
- `references/ai-gateway-docker-apps.md` — Antigravity Manager (:8045), OmniRoute (:20128), and Manifest (:2099) as Docker `--network host` containers; covers install commands, env vars, pitfalls (secret length, UID 1000 chown, SPA load time), account storage, and comparison table
- `references/hermes-config-set-list-value-pitfall.md` — `hermes config set` writes list-typed keys (`fallback_providers`, etc.) as quoted YAML strings, not sequences. Use `hermes config edit` for list/dict/nested keys. Agent `patch`/`write_file` is blocked on `~/.hermes/config.yaml`. Includes `fallback_providers` model-slug + primary-provider gotchas.

## Verification Checklist
- [ ] Live surface inspected, not just source files
- [ ] Browser/chat probe performed for dashboard or TUI claims
- [ ] Main profile avoided for risky memory experiments
- [ ] Procedural notes kept in skill, not USER.md or MEMORY.md
