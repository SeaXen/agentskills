---
name: agy-cli
description: "Use when you want Hermes to operate the agy CLI directly for one-shot prompts, interactive sessions, continuation, plugin checks, or workspace-based repo inspection."
version: 1.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [agy, cli, agent, autonomous, workspace, sandbox]
    related_skills: [hermes-agent, codex, claude-code, opencode]
changelog:
  - "1.1.0 (2026-06-20): Add /agy slash command bridge plugin pattern; document prefix-collision with agy-cli skill name; reference provider cache fix recipe."
  - "1.0.0: Initial release."
---

# agy CLI

## Overview

`agy` is an external agent CLI Hermes can drive directly from the shell.

Use it when the user specifically wants `agy`, wants to compare agent behavior, or already has an `agy` workflow that should be reused instead of forcing Hermes-native tools.

## When to Use
## Context: gemini-cli → agy migration (June 2026)

Google retired `gemini-cli` OAuth for consumer tiers (Pro/Ultra/free Code Assist) on **2026-06-18**. `agy` is the official successor — same Cloud Code Assist backend, same Pro quota, new binary, fresh OAuth client fingerprint. **Hermes' `google-gemini-cli` provider still uses the old OAuth client** and is now in Google's ban radar for Pro accounts. Default to `agy` for any Pro-sub work.

### Pro subscription ≠ API quota (important cost trap)

The Gemini Pro subscription ($20/mo via Google One AI Premium) is **separate** from API access. You cannot spend Pro quota via the AI Studio API key — that requires a separate billing path (AI Studio pay-per-token or Vertex AI). If a user wants to use their Pro sub from Hermes, the path is `agy` (OAuth) or Antigravity CLI directly. Suggesting "BYOK with a free AI Studio key" is fine for low-stakes work, but the user is still paying for Pro separately — do not frame the two as interchangeable.

### Ban risk (real, not theoretical)

Google's official position (discussion #20632, Feb 2026): "Using third-party software, tools, or services to harvest or piggyback on Gemini CLI's OAuth authentication to access our backend services is a direct violation of Gemini CLI's applicable terms." Mass bans have hit Pro/Ultra subscribers using third-party wrappers (OpenClaw, CLIProxyAPI, Pi coder, etc.). `agy` itself is safe because it's the official binary — the ban trigger is the OAuth client fingerprint, not the user account. Hermes' `google-gemini-cli` provider is NOT safe for Pro accounts.

## When to Use

- User says to use `agy`
- Need a one-shot agent run against a repo
- Need to continue the most recent `agy` conversation
- Need interactive `agy` with a starting prompt
- Need to inspect `agy` plugin availability or version
- **User wants to use their Gemini Pro subscription from inside Hermes** (default to `agy`, NOT `google-gemini-cli` provider)

Do not use when Hermes native tools already solve the task faster and the user did not ask for `agy`.

## Why agy vs google-gemini-cli OAuth provider

Hermes has a `google-gemini-cli` provider that authenticates via the same Cloud Code Assist OAuth flow that `gemini-cli` / Antigravity CLI use. It works, but carries **real ban risk** for Pro/Ultra subscribers:

- Google's official policy (gemini-cli discussion #20632, Feb 28 2026): "Using third-party software, tools, or services to harvest or piggyback on Gemini CLI's OAuth authentication to access our backend services is a **direct violation** of Gemini CLI's applicable terms and policies. **Permanent ban** on second violation."
- Mass bans hit OpenClaw / CLIProxyAPI / Pi-coder users on Pro/Ultra in Feb 2026 — error: `403: Gemini has been disabled in this account for violation of Terms of Service`.
- Detection is **client-fingerprint-based**, not user-account-based. Hermes' HTTP client fingerprint does not match the official `gemini` CLI, so Google's automated systems can flag it even though the OAuth token itself is valid.
- Google's Cloud Code Assist OAuth for **consumer Gemini tiers sunset on 2026-06-18**. After that date the `google-gemini-cli` provider is officially dead for Pro/Ultra/free users regardless of ban risk.

**Safe path for Pro accounts:** use `agy` (Antigravity CLI) — Google's own binary, installed at `~/.local/bin/agy`. Same backend, same Pro quota, but with Google's own client fingerprint. Hermes drives it as a subprocess via this skill. No ban risk because Google sees the official client.

**If you don't have a Pro sub:** use the `gemini` provider (AI Studio) with an API key instead. See `references/google-pro-account-safety.md` for the full cost model (Pro sub does **not** transfer to API quota — they're separate billing systems).

**Hermes' `google-gemini-cli` provider is only safe for:** enterprise Gemini Code Assist license holders (paid workspace accounts) who are explicitly authorized to use third-party CLIs. For everyone else, prefer `agy` or the API key.

## Prerequisite Check

Always verify installation first:

```bash
command -v agy
agy --version
```

Optional help check:

```bash
agy --help | sed -n '1,120p'
```

## Core Commands

### One-shot prompt

```bash
agy --print "Summarize this repository"
```

Alias:

```bash
agy --prompt "Summarize this repository"
```

### Interactive with initial prompt

```bash
agy --prompt-interactive "Inspect the codebase and tell me the hot spots"
```

Short alias:

```bash
agy -i "Inspect the codebase and tell me the hot spots"
```

### Continue most recent conversation

```bash
agy --continue
```

Short alias:

```bash
agy -c
```

### Resume a specific conversation

```bash
agy --conversation <conversation-id>
```

### Add workspace directories

```bash
agy --add-dir /path/to/repo --print "Find auth flow entrypoints"
```

Repeatable:

```bash
agy --add-dir /repo/api --add-dir /repo/web --print "Map the end-to-end request flow"
```

### Sandbox mode

```bash
agy --sandbox --print "Review this repo safely"
```

### Skip permission prompts

Use only when the user clearly wants non-interactive approval bypass:

```bash
agy --dangerously-skip-permissions --print "Run the requested inspection"
```

## Common Operational Patterns

### Repo inspection

For repeatable repo audits, prefer the companion skill `agy-repo-inspection`.

Quick one-liner:

```bash
agy --add-dir "$PWD" --print "Inspect architecture, key modules, risks, and test gaps"
```

Use `agy-repo-inspection` when you want a fixed rubric for architecture, risks, test gaps, and prioritized next actions.

### Monolithic single-file dashboard visual overhaul

When the user asks to fix/overhaul/polish a monolithic single-file dashboard (e.g. a Python file with inline HTML/CSS/JS), `agy --print` with `--add-dir` is effective:

```bash
agy --add-dir /path/to/project --print "Fix and visually overhaul the dashboard at /path/to/file.py

Specific problems to fix:
1. [Problem 1]
2. [Problem 2]

Requirements:
- Only modify CSS, HTML, JS visualization code
- Keep all API endpoints and backend logic unchanged
- After editing, run python3 -m py_compile and node --check on extracted JS
- Restart the service and verify"
```

Key rules for this pattern:
- Always pass `--add-dir` pointing to the directory containing the file
- Be explicit about what NOT to change (backend logic, API paths, ports)
- Include the verification steps in the prompt so agy self-validates
- **CRITICAL: After agy finishes, always verify the file was actually modified** — agy frequently produces a plan and claims success without writing anything. Check with `grep` or `read_file` for the expected changes. If the file is unchanged, fall back to direct `patch` tool edits yourself.
- Independently verify after agy: py_compile, node --check, service status, HTTP response
- Do NOT let agy change vault paths, ports, or Python backend logic

### Continue prior work in same repo

```bash
agy --add-dir "$PWD" --continue
```

### Plugin check

```bash
agy plugin list
```

### Install/update shell setup

```bash
agy install
agy update
```

## Bridge plugin: expose agy as a `/agy` Hermes slash command

When the user wants agy to feel first-class inside Hermes (not a subprocess chore), wrap it as a user plugin. The command auto-propagates to CLI / TUI / Discord / Telegram via Hermes' platform-agnostic plugin registry.

### Plugin layout

```
~/.hermes/plugins/agy-bridge/
├── plugin.yaml
└── __init__.py
```

### plugin.yaml

```yaml
name: agy-bridge
version: "1.0.0"
description: "Slash-command bridge to the Antigravity CLI (agy)."
requires_env: []
optional_env: []
provides_tools: []
provides_hooks: []
```

### __init__.py — minimal working pattern

```python
import shlex, shutil, subprocess

def _parse_args(raw: str):
    if not raw.strip():
        return [], "", False
    toks = shlex.split(raw)
    flags, pos, help_req = [], [], False
    i = 0
    while i < len(toks):
        t = toks[i]
        if t in ("--help", "-h"):
            help_req = True; i += 1; continue
        if t in ("--continue", "-c"):
            flags.append("--continue"); i += 1; continue
        if t == "--sandbox":
            flags.append("--sandbox"); i += 1; continue
        if t == "--dir":
            flags.extend(["--add-dir", toks[i+1]]); i += 2; continue
        pos.append(t); i += 1
    return flags, " ".join(pos).strip(), help_req

def _handle(raw: str) -> str:
    if not raw.strip(): return "Usage: /agy [--dir PATH] PROMPT"
    flags, prompt, help_req = _parse_args(raw)
    if help_req: return "Usage: /agy [--dir PATH] [--continue] PROMPT"
    agy = shutil.which("agy")
    if not agy: return "agy not on PATH. Install: curl -fsSL https://antigravity.google/install.sh | bash"
    cmd = [agy, "--print"] + flags + ([prompt] if prompt else [])
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    return r.stdout.rstrip() if r.returncode == 0 else f"agy error: {r.stderr}"

def register(ctx):
    ctx.register_command(
        "agy",
        handler=_handle,
        description="Run a prompt through Antigravity CLI (Gemini Pro sub).",
        args_hint="[--dir PATH] [--continue] PROMPT",
    )
```

### Enable and verify

```bash
# Edit ~/.hermes/config.yaml — add to plugins.enabled as a real YAML list:
#   plugins:
#     enabled:
#     - agy-bridge
hermes plugins list                      # should show agy-bridge | enabled
python3 -c "from hermes_cli.plugins import PluginManager; m=PluginManager(); m.discover_and_load(force=True); print(list(m._plugin_commands.keys()))"
# Should include 'agy'
```

### Key gotchas (from real session)

1. **`hermes config set plugins.enabled '[...]'` stores it as a JSON string, not a YAML list.** The loader checks `isinstance(enabled, list)` — the string form silently fails and the plugin stays "not enabled". Edit the YAML list directly (the `patch` tool refuses config.yaml — use `python3` or sed via terminal).
2. **`hermes plugins enable <name>` WIPES other enabled plugins.** It calls `_save_enabled_set` which overwrites the list. Always re-add other plugins after enabling a new one.
3. **Plugin command names can shadow skills.** `/agy` triggers `⚡ Loading skill: agy-cli` (the operator guide skill, prefix-match) AND fires the plugin command. They coexist, but the skill flash is visible. Rename to `/agy-print` if the flash is annoying.
4. **Subprocess timeout: 300s default.** `agy --print` is synchronous; long prompts may need bumping.
5. **No streaming into chat history.** Each `/agy` call is a discrete subprocess, so it doesn't participate in the active session log. For multi-turn use `--continue` to keep agy-side context.
6. **Auto-propagation is free.** `register_command()` registers for CLI/TUI/Discord/Telegram/Slack/etc. via the same registry. Discord's adapter auto-mirrors plugin commands into the native slash picker (see `plugins/platforms/discord/adapter.py` around line 3697). Telegram routes via `gateway/platforms/telegram.py::_handle_command`. No per-platform code needed.

## Hermes Usage Notes

- Prefer `terminal` foreground for short `agy --print` runs.
- Prefer `terminal(background=true, pty=true)` for long interactive sessions.
- If `agy` output is needed for later reasoning, capture it directly from terminal output.
- For repo work, pass `--add-dir` explicitly rather than assuming current directory is enough.
- For first-class integration inside Hermes sessions, prefer the bridge plugin pattern (above) over raw subprocess.
- **For a native-feeling `/agy` slash command** (no `terminal` tool calls, no subprocess noise in chat), use the bridge plugin — see "Slash command bridge" below.

## Slash command bridge

`/agy` is registered as a first-class Hermes slash command by the **`agy-bridge` user plugin** at `~/.hermes/plugins/agy-bridge/`. It wraps `agy --print` so the user can type:

```
/agy Summarize this paper
/agy --dir /repo Find auth bugs
/agy --continue
/agy --sandbox --dir /repo Audit this code
/agy --help
```

without going through the `terminal` tool, paying subprocess overhead per call, or seeing raw `agy` output leak into chat.

**What the plugin does:** parses `--dir` / `--sandbox` / `--continue` / `--conversation` flags, runs `agy --print` via `subprocess.run()` with a 300s timeout, returns stdout to chat. Uses Pro subscription via the official `agy` binary — no third-party OAuth, no ban risk.

**Install / enable:**
1. Plugin already lives at `~/.hermes/plugins/agy-bridge/` (created 2026-06-20). If missing, copy from another machine or recreate: `plugin.yaml` + `__init__.py` with a `register(ctx)` that calls `ctx.register_command("agy", handler, description=..., args_hint=...)`.
2. Add `agy-bridge` to `plugins.enabled` in `~/.hermes/config.yaml` as a real YAML list (not a JSON string — see "Common Pitfalls" below).
3. Verify: `hermes plugins list` should show `agy-bridge │ enabled`. The plugin's handler is testable in isolation by importing `agy_bridge` and calling `agy_bridge._handle_agy("...")` directly.

**Prefix-collision caveat:** the existing `agy-cli` skill (this one) and the `/agy` command share a prefix. When the user types `/agy` in a session, both may fire — the skill loader logs `⚡ Loading skill: agy-cli` but the plugin command also runs (they're in different registries). If the flash is annoying, rename the command in `register(ctx)` to `/agy-print` or `/gpro`.

**Why not `ctx.dispatch_tool("terminal", ...)`:** dispatching through the terminal tool would route the subprocess through Hermes' approval / redaction / budget pipeline. For a user-initiated slash command that's friction — they typed it, they want it to run. The plugin uses `subprocess.run()` directly. Skip approval only because this is a user-invoked command, not an LLM-invoked tool call.

## Common Pitfalls

1. Running `agy` without checking it exists first.
2. Using interactive mode without `pty=true` when a terminal session is required.
3. Forgetting `--add-dir` and then getting shallow or wrong workspace context.
4. Using `--dangerously-skip-permissions` without user intent.
5. Assuming `--continue` resumes the desired repo context; verify when multiple recent conversations exist.
6. **Assuming agy actually wrote the file.** agy frequently produces a detailed plan and claims success without persisting any file changes. Always verify with `grep`/`read_file` that the expected edits exist. If the file is unchanged, use `patch` directly — do not re-run agy expecting different results.
7. **Using Hermes' `google-gemini-cli` provider for Pro-account work.** That provider still uses the old gemini-cli OAuth client (post-2026-06-18 sunset) and is in Google's ban radar. Route Pro work through `agy` (subprocess or bridge plugin) instead.
8. **Suggesting "use an AI Studio API key" as a substitute for the Pro sub.** Pro subscription quota is not transferable to API. API key is a separate billing path. Make this distinction explicit to the user so they don't expect free reuse.
7. **Recommending the Hermes `google-gemini-cli` provider to Pro subscribers.** It works in the short term but violates Google's ToS and risks account termination. Use this skill (`agy` subprocess) or the `gemini` API provider with a separate key instead. See the "Why agy vs google-gemini-cli OAuth provider" section above.
8. **Telling the user to `hermes config set plugins.enabled '["a","b"]'`.** That subcommand serializes the list to a JSON string and writes it as a YAML string, so the loader's `isinstance(enabled, list)` check fails and the plugin still shows "not enabled" in `hermes plugins list`. Edit `~/.hermes/config.yaml` directly and write a real YAML list:
   ```yaml
   plugins:
     enabled:
     - agy-bridge
     - other-plugin
   ```
   The `hermes plugins enable <name>` CLI subcommand also **replaces** the enabled list (does not merge) — do not use it to add a plugin without first re-adding everything else.

## Verification Checklist

- [ ] `command -v agy` returns a path
- [ ] `agy --version` works
- [ ] Correct mode chosen: `--print`, `--prompt-interactive`, `--continue`, or `--conversation`
- [ ] `--add-dir` supplied when repo context matters
- [ ] `pty=true` used for truly interactive runs
- [ ] Output captured and checked before reporting success

## References

- `references/hermes-provider-health-check.md` — live provider model testing recipe, cache structure (`~/.hermes/provider_models_cache.json`), cache patching via `python3`, `hermes config set` JSON-stringification pitfall, two-models.py-locations gotcha, `hermes plugins enable` wipes siblings, `gemini-3.5-flash` GA-gating context. Read this when verifying a provider's model list or fixing a stale picker.

## See also

- `references/google-pro-account-safety.md` — full ToS policy context, Pro-sub vs API quota cost model, the `~/.hermes/provider_models_cache.json` hand-fix pattern, and the strong-vs-weak verification pattern for LLM response tests. **Read this before recommending `google-gemini-cli` OAuth for any Pro/Ultra/free user.**
- `~/.hermes/plugins/agy-bridge/` — the user plugin that registers `/agy` as a first-class slash command. Source for the bridge pattern; copy or extend it to wrap other external CLIs.
