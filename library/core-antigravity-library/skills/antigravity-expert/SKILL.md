---
name: antigravity-expert
description: Complete mastery of Google Antigravity platform architecture. Use when authoring or debugging Antigravity skills, hierarchical rules (GEMINI.md, AGENTS.md), slash command workflows, subagent orchestration, lifecycle hooks, and Model Context Protocol (MCP) integrations.
allowed-tools: Read, Write, Edit, Glob, Grep
version: 1.0
category: core-antigravity
---

# Google Antigravity Expert

> **Platform Architecture, Customizations, Skills, Rules & Subagent Orchestration**

---

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Follow progressive disclosure:

| File | Description | When to Read |
|------|-------------|--------------|
| `skills-guide.md` | Skill authoring, progressive disclosure, frontmatter, directory layout | Creating/editing agent skills |
| `rules-and-workflows.md` | Hierarchical rules, trigger modes (`always_on`, `model_decision`), slash commands | Managing GEMINI.md, AGENTS.md, workflows |
| `mcp-and-hooks.md` | MCP server configuration (`mcp_config.json`), lifecycle hooks (`hooks.json`) | Integrating external tools or lifecycle automation |
| `subagent-orchestration.md` | Antigravity native subagents, parallel agents, background tasks | Coordinating multi-agent workflows |

---

## 🏗️ Core Principles

| Principle | Rule |
|-----------|------|
| **Progressive Disclosure** | The root context only loads frontmatter metadata (`name`, `description`). Deep runbooks must live in sub-files. |
| **Local Library Pattern** | Maintain mass skill archives (>70 skills) in `.agent/library/` and promote to `.agent/skills/` on demand to prevent system prompt saturation. |
| **P0 > P1 > P2 Precedence** | Priority order: Project Rules (`GEMINI.md`) > Agent definitions (`.agent/agents/`) > Skills (`.agent/skills/`). |
| **Token Conservation** | Never overwhelm the prompt window. Keep `SKILL.md` concise and modularize via tables and reference files. Use `/usage` to monitor. |
| **UTF-8 Output on Windows** | Reconfigure `sys.stdout` to UTF-8 (`sys.stdout.reconfigure(encoding='utf-8')`) in all Python agent scripts to avoid Windows `cp1252` encoding crashes. |
| **Native Tooling** | Use Antigravity's native primitives (subagents, background tasks, artifacts) rather than unmonitored shell hacks. |

---

## 📋 Decision Checklist

Before creating or editing an Antigravity customization:

- [ ] Identified the right customization type (Rule vs. Skill vs. Workflow vs. Hook vs. MCP)?
- [ ] Frontmatter YAML contains exact `name` and actionable `description`?
- [ ] Description specifies both **what** the capability is and **when** the agent should trigger it?
- [ ] Detailed procedures placed in sub-markdown files under the skill folder?
- [ ] Registered in `ARCHITECTURE.md` and wired to corresponding agents in `.agent/agents/`?

---

## ❌ Anti-Patterns

- ❌ **Bloated Context**: Inlining hundreds of lines of reference manuals directly in `SKILL.md`.
- ❌ **Vague Descriptions**: Writing `description: A skill for Antigravity` instead of describing triggers and tasks.
- ❌ **Duplicate Declarations**: Re-declaring rules that already exist in `GEMINI.md`.
- ❌ **Ignoring Token Limits**: Reading entire directories or running recursive grep without file filters.
