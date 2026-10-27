# Antigravity Skills Authoring Guide

## 1. Directory Structure

A valid Antigravity skill directory must reside in a customization root (`.agent/skills/` or `.agents/skills/` or global `~/.gemini/config/skills/`):

```text
skills/<skill-name>/
├── SKILL.md            # (Mandatory) Index file with YAML frontmatter
├── scripts/            # (Optional) Executable scripts (Python, PowerShell, Bash)
├── references/         # (Optional) Detailed guides, specifications, runbooks
└── resources/          # (Optional) Templates, sample configs, schemas
```

## 2. YAML Frontmatter Specification

Every `SKILL.md` must start with a YAML frontmatter block:

```markdown
---
name: my-skill-name
description: >-
  Action-oriented description specifying capabilities and precise triggers.
  E.g.: "Use when managing Docker containers, writing multi-stage Dockerfiles, or debugging compose stacks."
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
---
```

### Critical Guidelines for `description`:
- The primary model reads **only** this description when selecting skills.
- Use third-person, clear action verbs.
- State explicitly **when** and **under what conditions** the agent should load this skill.

## 3. Progressive Disclosure Architecture

To avoid exhausting context window limits:
1. **Index (`SKILL.md`)**: Contains metadata, a selective reading navigation table, core principles, checklist, and anti-patterns.
2. **Sub-Markdown Files**: In-depth explanations, code snippets, and procedures live in separate `.md` files in the skill directory or `references/`.
3. **Selective Reading**: The agent reads the table of contents in `SKILL.md` and only views the sub-document relevant to the current user turn.

## 4. Best Practices

- **Self-Documenting**: Scripts in `scripts/` should accept standard `--help` arguments.
- **Verification**: Always include a checklist or validation command that the agent can execute to confirm success.
- **Avoid Duplication**: Do not restate generic programming knowledge. Focus strictly on project or domain-specific workflows.
