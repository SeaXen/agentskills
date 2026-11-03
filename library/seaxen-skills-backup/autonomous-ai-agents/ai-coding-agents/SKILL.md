---
name: ai-coding-agents
description: "Orchestrate external AI coding agents (Claude Code, Codex, OpenCode) from Hermes - delegation patterns, PTY management, parallel execution, PR reviews, and cost control."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [coding-agent, claude-code, codex, opencode, delegation, pty, automation, pr-review]
    related_skills: [hermes-agent, delegate_task, subagent-driven-development, systematic-debugging, test-driven-development]
---

# AI Coding Agents — Unified Orchestration

Use this skill when you need to delegate coding tasks to external AI coding agent CLIs. Covers all three major agents with unified patterns for one-shot execution, interactive PTY sessions, parallel worktrees, PR reviews, and cost/performance optimization.

## Agent Comparison & Selection

| Agent | Provider | Best For | Auth | Print Mode | Interactive PTY |
|-------|----------|----------|------|------------|-----------------|
| **Claude Code** | Anthropic | Complex refactoring, code review, multi-step reasoning | OAuth (Pro/Max) or `ANTHROPIC_API_KEY` | `claude -p` ✅ | tmux + `claude` ✅ |
| **Codex** | OpenAI | Feature building, batch issue fixing, PR automation | `OPENAI_API_KEY` or Codex OAuth | `codex exec` ✅ | `codex` (TUI) ✅ |
| **OpenCode** | Provider-agnostic (OpenRouter, etc.) | Flexible model choice, open-source, custom providers | `OPENROUTER_API_KEY` etc. or `opencode auth` | `opencode run` ✅ | `opencode` (TUI) ✅ |

**Selection heuristic:**
- Need deepest reasoning + largest context? → **Claude Code (Opus/Sonnet 4)**
- OpenAI ecosystem, ChatGPT plan, want Codex OAuth? → **Codex**
- Want model flexibility, open-source, multiple providers? → **OpenCode**
- CI/CD scripting, one-shot tasks? → **Print mode** (all three)
- Long iterative sessions? → **Interactive PTY** (all three)

---

## Common Orchestration Patterns

### 1. One-Shot Tasks (Print Mode) — Preferred for Automation

All agents support non-interactive print mode that exits cleanly with structured output.

```bash
# Claude Code
terminal(command="claude -p 'Add error handling to all API calls in src/' --allowedTools 'Read,Edit' --max-turns 10", workdir="/path/to/project", timeout=120)

# Codex
terminal(command="codex exec 'Add error handling to all API calls' --full-auto", workdir="/path/to/project", pty=true, timeout=120)

# OpenCode
terminal(command="opencode run 'Add error handling to all API calls' --model openrouter/anthropic/claude-sonnet-4", workdir="/path/to/project", timeout=120)
```

**When to use print mode:**
- One-shot coding tasks (bug fix, feature, refactor)
- CI/CD automation and scripting
- Structured data extraction with JSON schema (Claude Code)
- Piped input processing (`cat file | agent -p "analyze this"`)
- Any task not needing multi-turn conversation

**Key flags for reliability:**
- `--max-turns N` — prevent runaway loops (Claude Code, Codex, OpenCode)
- `--allowedTools` / `--disallowedTools` — restrict capabilities (Claude Code)
- `--full-auto` — auto-approve file changes (Codex)
- `--model provider/model` — force specific model (OpenCode)

### 2. Interactive PTY Sessions — Multi-Turn Iterative Work

Use tmux to orchestrate TUI-based interactive sessions for all three agents.

```bash
# Start a tmux session
terminal(command="tmux new-session -d -s agent-work -x 140 -y 40")

# Launch the agent
terminal(command="tmux send-keys -t agent-work 'cd /path/to/project && claude' Enter")  # or 'codex' or 'opencode'

# Wait for startup (~3-5s), then send task
terminal(command="sleep 5 && tmux send-keys -t agent-work 'Refactor the auth module to use JWT tokens' Enter")

# Monitor progress
terminal(command="sleep 15 && tmux capture-pane -t agent-work -p -S -50")

# Send follow-up
terminal(command="tmux send-keys -t agent-work 'Now add unit tests for the new JWT code' Enter")

# Exit cleanly
terminal(command="tmux send-keys -t agent-work '/exit' Enter")  # Claude Code
# terminal(command="tmux send-keys -t agent-work C-c")  # Codex (Ctrl+C)
# terminal(command="tmux send-keys -t agent-work C-c")  # OpenCode (Ctrl+C, NOT /exit)
```

**Dialog handling for Claude Code interactive (critical):**
```bash
# Launch with permissions bypass
terminal(command="tmux send-keys -t agent-work 'claude --dangerously-skip-permissions \"your task\"' Enter")

# Handle trust dialog (Enter = "Yes, I trust this folder")
terminal(command="sleep 4 && tmux send-keys -t agent-work Enter")

# Handle permissions dialog (Down then Enter = "Yes, I accept")
terminal(command="sleep 3 && tmux send-keys -t agent-work Down && sleep 0.3 && tmux send-keys -t agent-work Enter")
```

**Exit commands by agent:**
- **Claude Code**: `/exit` or `Ctrl+D`
- **Codex**: `Ctrl+C`
- **OpenCode**: `Ctrl+C` (NOT `/exit` — opens agent selector)

### 3. Parallel Execution with Worktrees

Run multiple independent agents simultaneously on different tasks using git worktrees for isolation.

```bash
# Create worktrees
terminal(command="git worktree add -b fix/issue-78 /tmp/issue-78 main", workdir="/path/to/project")
terminal(command="git worktree add -b fix/issue-99 /tmp/issue-99 main", workdir="/path/to/project")

# Launch agents in parallel (background + notify)
terminal(command="claude -p 'Fix issue #78: <description>' --max-turns 10", workdir="/tmp/issue-78", background=true, notify_on_complete=true, timeout=180)
terminal(command="codex exec 'Fix issue #99: <description>' --full-auto", workdir="/tmp/issue-99", background=true, pty=true, notify_on_complete=true, timeout=180)
terminal(command="opencode run 'Add parser regression tests'", workdir="/tmp/issue-100", background=true, notify_on_complete=true, timeout=180)

# Monitor all
process(action="list")

# After completion, push and create PRs
terminal(command="cd /tmp/issue-78 && git push -u origin fix/issue-78")
terminal(command="gh pr create --repo user/repo --head fix/issue-78 --title 'fix: ...' --body '...'")

# Cleanup
terminal(command="git worktree remove /tmp/issue-78", workdir="/path/to/project")
```

### 4. PR Review Workflows

| Pattern | Command |
|---------|---------|
| **Quick review (print mode)** | `git diff main...feature | claude -p 'Review for bugs/security' --max-turns 1` |
| **Deep review (interactive + worktree)** | `claude -w pr-review --tmux` creates isolated worktree + tmux |
| **Codex review** | `codex review --base origin/main` in PR checkout |
| **OpenCode review** | `opencode pr 42` or `opencode run 'Review PR vs main' -f <files>` |
| **Batch review** | `git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'` then parallel agents |

### 5. Cost & Performance Control

| Control | Claude Code | Codex | OpenCode |
|---------|-------------|-------|----------|
| Turn limit | `--max-turns N` | `--max-turns N` (via env) | `--max-turns N` |
| Budget cap | `--max-budget-usd N` | N/A | N/A |
| Effort/Reasoning | `--effort low/medium/high/max/auto` | N/A | `--variant minimal/high/max` |
| Model fallback | `--fallback-model haiku` | N/A | `--model provider/model` |
| Bare/minimal mode | `--bare` | N/A | N/A |
| Tool restriction | `--allowedTools Read,Edit` | N/A | N/A |
| Streaming JSON | `--output-format stream-json` | `--format json` | `--format json` |

**Critical:** Always set `--max-turns` in print mode to prevent infinite loops.

---

## Agent-Specific Reference

### Claude Code (Anthropic)

**Install:** `npm install -g @anthropic-ai/claude-code`
**Auth:** `claude auth login` (OAuth) or `ANTHROPIC_API_KEY`

**Key subcommands:**
| Command | Purpose |
|---------|---------|
| `claude -p "task"` | Print mode (non-interactive) |
| `claude -c` | Continue most recent session |
| `claude -r "id"` | Resume specific session |
| `claude auth status` | Check login (JSON with `--text`) |
| `claude doctor` | Health check |
| `claude mcp add <name> -- <cmd>` | Add MCP server |
| `claude --bare -p "task"` | CI mode (skip hooks/plugins/MCP) |

**Unique features:**
- JSON schema structured output (`--json-schema`)
- Streaming bidirectional (`stream-json` input/output)
- Session resumption with `--resume`, `--continue`, `--fork-session`
- Worktree integration: `claude -w <name> --tmux`
- Slash commands: `/compact`, `/review`, `/plan`, `/cost`, custom commands
- Custom subagents in `.claude/agents/`
- Hooks for automation: `PreToolUse`, `PostToolUse`, `Stop`, etc.
- Rules directory: `.claude/rules/*.md`

**Environment variables:**
- `ANTHROPIC_API_KEY` — API key auth
- `CLAUDE_CODE_EFFORT_LEVEL` — default effort
- `MAX_THINKING_TOKENS` — cap thinking (0 = disable)
- `MAX_MCP_OUTPUT_TOKENS` — cap MCP output
- `CLAUDE_CODE_NO_FLICKER=1` — alt-screen rendering

---

### Codex (OpenAI)

**Install:** `npm install -g @openai/codex`
**Auth:** `OPENAI_API_KEY` or Codex OAuth (`~/.codex/auth.json` or Hermes-managed)
**Requirement:** Must run inside a git repository

**Key commands:**
| Command | Purpose |
|---------|---------|
| `codex exec "task"` | One-shot execution, exits |
| `codex exec --full-auto "task"` | Auto-approves file changes |
| `codex exec --yolo "task"` | No sandbox, no approvals |
| `codex review` | Built-in PR review |
| `codex --version` | Check version |

**Background execution:**
```bash
terminal(command="codex exec --full-auto 'task'", workdir="~/project", background=true, pty=true)
# Returns session_id
process(action="poll", session_id="<id>")
process(action="submit", session_id="<id>", data="yes")  # Answer prompts
process(action="kill", session_id="<id>")
```

**Unique features:**
- Git worktree parallel issue fixing pattern
- Batch PR review via `git fetch origin '+refs/pull/*/head...'`
- Session stats: `codex stats --days 7`

**Pitfalls:**
- Requires `pty=true` for interactive sessions
- Must run in git repo (use `mktemp -d && git init` for scratch)
- Auth diagnostics: see `references/auth-diagnostics.md` for `NoneType` error

---

### OpenCode (Provider-Agnostic)

**Install:** `npm i -g opencode-ai@latest` or `brew install anomalyco/tap/opencode`
**Auth:** `opencode auth login` or provider env vars (`OPENROUTER_API_KEY`, etc.)

**Key commands:**
| Command | Purpose |
|---------|---------|
| `opencode run "task"` | One-shot, no pty needed |
| `opencode` | Interactive TUI (requires pty) |
| `opencode run -f file1 -f file2 "task"` | Attach context files |
| `opencode run --model provider/model "task"` | Force specific model |
| `opencode pr 42` | Built-in PR review |
| `opencode -c` | Continue last session |
| `opencode -s <id>` | Resume specific session |
| `opencode session list` | List past sessions |
| `opencode stats` | Token usage/costs |

**Interactive TUI keybindings:**
| Key | Action |
|-----|--------|
| `Enter` | Submit (may need twice) |
| `Tab` | Switch agents (build/plan) |
| `Ctrl+P` | Command palette |
| `Ctrl+X L/M/N/E` | Switch session/model/new/edit |
| `Ctrl+C` | Exit (NOT `/exit`) |

**Unique features:**
- Provider-agnostic (OpenRouter, Anthropic, OpenAI, etc.)
- Model switching mid-session (`Ctrl+X M`)
- Binary resolution: check `which -a opencode` if behavior differs
- `opencode stats --days 7 --models <model>` for cost tracking
- `--thinking` flag to show model reasoning blocks

**Pitfalls:**
- Interactive TUI requires `pty=true`; `run` subcommand does not
- `/exit` is NOT a valid command — opens agent selector
- PATH mismatch may select wrong binary; pin with `$HOME/.opencode/bin/opencode`
- Enter may need double-press to submit

---

## Verification & Smoke Tests

```bash
# All agents
claude -p "Respond with exactly: CLAUDE_OK" --max-turns 1
codex exec "Respond with exactly: CODEX_OK"
opencode run "Respond with exactly: OPENCODE_OK"

# Expected: output includes the marker, exits cleanly, no auth errors
```

---

## Common Pitfalls & Solutions

| Pitfall | Solution |
|---------|----------|
| Interactive mode hangs | Use tmux + `capture-pane` for monitoring; check for `❯` prompt |
| Runway loops / cost overruns | Always set `--max-turns` in print mode |
| Auth failures | Verify provider keys/OAuth; check `auth status` commands |
| PATH/binary confusion | Pin explicit binary paths; check `which -a <agent>` |
| Context degradation | Monitor with `/context` (Claude); use `--max-turns`; start fresh sessions |
| Parallel collision | Always use separate workdirs/worktrees |
| Dialog handling (Claude) | Print mode skips dialogs; interactive: Enter for trust, Down+Enter for permissions |
| Wrong exit command | Claude: `/exit`; Codex: `Ctrl+C`; OpenCode: `Ctrl+C` (not `/exit`) |
| Session resumotion lost | Use `--resume <session_id>` (Claude), `-c`/`-s` (OpenCode), `--continue` (Codex) |