# SeaXen Skills Backup

**Private backup of the complete `/root/.hermes/skills/` tree from SeaXen's Hermes Agent.**

## What's in here

The full collection of skills, learnables, and verbatim references used by the agent.
Includes skills from **255+ upstream repos**, ~27,500 files, ~365 MB (trimmed 2026-08-22:
repo clones stripped to skill-shaped files only — SKILL.md + references/scripts/templates/assets).

## Layout

```
learnables/              # GitHub-cloned repos, each with real SKILL.md (+ refs/scripts)
  ├── antigravity-awesome-skills/   # 4,333-skill mega-collection
  ├── forgecat/, hermes-agency/, ECC/, claude-skills-345/   # multi-skill bundles
  └── <255 repo-skills>
<category>/              # Hermes core categories: devops/, productivity/, research/, etc.
INDEX.md                 # Categorized index (auto-regenerated weekly)
_verbatim-manifest.json  # Flat manifest of every repo + leaf count
```

## Skill quality standard

Every `learnables/<name>/SKILL.md` is a real, loadable skill — frontmatter + full body,
agent-agnostic (Hermes / Claude Code / Codex / Cursor install paths included where relevant).
11 previously-stub skills were re-learned from live upstream sources on 2026-08-22.

## Restore

```bash
git clone https://github.com/SeaXen/skills-backup.git ~/.hermes/skills
```

Hermes discovers all skills on next start.

## Maintenance policy

- **Incremental sync** — rsync diff → commit → push. Never force-push / full snapshot.
- Private, single-operator backup · MIT-licensed · manual push
- Excludes runtime state: `.hub/`, `.curator_backups/`, `*.log`, `.archive/`, `.usage.json*`
- See skill `devops/skills-backup-incremental` for the exact workflow.

## History note

2026-08-21 commit (`59d28a40`, 231 repos) was overwritten by a full-snapshot force-push on
2026-08-22 — old history is not in main's lineage but remains recoverable via GitHub API
(`commits/59d28a40`) for ~90 days. From 2026-08-22 onward this repo is incrementally synced only.
