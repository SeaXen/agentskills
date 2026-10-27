# Antigravity Rules & Workflows Guide

## 1. Hierarchical Rules Architecture

Rules enforce behavioral constraints, coding standards, and project guidelines.

### Discovery & Precedence
1. **Workspace Root Rules**: `GEMINI.md` or `AGENTS.md` at project root.
2. **Subdirectory Rules**: `GEMINI.md` located in specific folders (e.g., `frontend/GEMINI.md`) take precedence within that directory tree.
3. **Dedicated Rule Files**: `.agent/rules/*.md` loaded automatically or by trigger.
4. **Global Rules**: `~/.gemini/config/rules/`.

### Trigger Modes

In rule frontmatter:
```yaml
---
trigger: always_on       # Unconditionally loaded on every interaction
---
```
or
```yaml
---
trigger: model_decision  # Loaded only when user prompt matches rule context
description: Coding standards for database migrations and schema changes.
---
```

## 2. Slash Command Workflows

Slash commands (`/command`) provide user-facing shortcuts that trigger structured, multi-step procedures.

### Location:
Stored in `.agent/workflows/<command-name>.md`.

### Workflow File Structure:
```markdown
---
description: Short user-facing summary of the command
---

# /my-command Workflow

## Objective
High-level statement of what this command achieves.

## Step 1: Context Gathering
Instructions for the agent to inspect the current state.

## Step 2: Confirmation / Plan
Points where the agent must stop and present the plan to the user.

## Step 3: Execution & Verification
Commands or file updates, followed by test execution.
```

### Discovery:
Antigravity automatically indexes all `.md` files in `.agent/workflows/` and exposes them as interactive slash commands in the UI.
