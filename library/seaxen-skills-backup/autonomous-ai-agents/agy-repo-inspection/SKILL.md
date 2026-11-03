---
name: agy-repo-inspection
description: "Use when you want Hermes to run agy for repeatable repository inspection with a fixed audit rubric and structured output."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [agy, repo-inspection, codebase, audit, architecture]
    related_skills: [agy-cli, codebase-inspection, systematic-debugging]
---

# agy Repo Inspection

## Overview

Use this skill when the goal is not just "run agy", but to run it against a repo with a consistent inspection rubric.

This separates **tool operation** from **inspection method**:
- `agy-cli` = how to drive agy
- `agy-repo-inspection` = what to ask agy and how to evaluate the output

## When to Use

- User asks for repo inspection using `agy`
- Need a fast first-pass audit of an unfamiliar codebase
- Need a repeatable prompt for architecture, risks, and gaps
- Need comparable inspections across multiple repos

Do not use when the user wants line-by-line code review of a specific diff or PR. Use a review-specific workflow for that.

## Prerequisites

First verify `agy` exists:

```bash
command -v agy
agy --version
```

For repo work, always provide the workspace explicitly:

```bash
agy --add-dir "$PWD" --print "..."
```

## Standard Inspection Prompt

Base prompt:

```text
Inspect this repository and return a structured report with these sections:
1. Purpose: what the project does
2. Architecture: main components, runtime boundaries, key entrypoints
3. Critical paths: auth, data flow, background jobs, external integrations
4. Risks: security, reliability, scaling, operational hazards
5. Code quality issues: coupling, dead zones, missing abstractions, fragile areas
6. Test posture: existing coverage signals, obvious gaps, what should be tested first
7. Maintainer priorities: top 5 changes worth making next
Be concrete. Name files, modules, and likely hotspots. If uncertain, label uncertainty.
```

## One-Shot Recipes

### Default repo inspection

```bash
agy --add-dir "$PWD" --print "Inspect this repository and return a structured report with these sections:
1. Purpose: what the project does
2. Architecture: main components, runtime boundaries, key entrypoints
3. Critical paths: auth, data flow, background jobs, external integrations
4. Risks: security, reliability, scaling, operational hazards
5. Code quality issues: coupling, dead zones, missing abstractions, fragile areas
6. Test posture: existing coverage signals, obvious gaps, what should be tested first
7. Maintainer priorities: top 5 changes worth making next
Be concrete. Name files, modules, and likely hotspots. If uncertain, label uncertainty."
```

### Focus on architecture only

```bash
agy --add-dir "$PWD" --print "Map this repository's architecture. Identify entrypoints, subsystems, data flow, external dependencies, and files that control bootstrapping/configuration."
```

### Focus on risk audit

```bash
agy --add-dir "$PWD" --print "Audit this repository for practical risks: auth mistakes, unsafe defaults, secrets exposure paths, brittle runtime assumptions, weak error handling, and operational blind spots. Rank by severity and name files."
```

### Focus on test gaps

```bash
agy --add-dir "$PWD" --print "Inspect this repository's test posture. Infer coverage from structure and files. Identify highest-risk untested paths and propose the first 5 tests to add, with target files if possible."
```

## Hermes Usage Notes

- Use foreground `terminal` for short `agy --print` runs.
- Use `pty=true` only if running interactive `agy` modes.
- After agy returns, Hermes should verify high-impact claims against actual files before presenting them as fact.
- For large mono-repos, consider multiple scoped passes instead of one vague whole-repo pass.

## Output Handling

Treat agy output as a draft audit, not ground truth.

Hermes should separate:
- **Verified facts**: confirmed from files, commands, or APIs
- **Agy claims**: plausible but not yet verified
- **Open questions**: where inspection found likely issues but evidence is incomplete

Good final structure:
- Repo purpose
- Architecture
- Top risks
- Test gaps
- Recommended next actions
- Uncertainty / needs verification

## Common Pitfalls

1. Using repo inspection without `--add-dir`, which weakens workspace context.
2. Asking agy for "review everything" with no structure, which causes vague output.
3. Reporting agy guesses as confirmed facts without checking files.
4. Trying to use this skill for PR review instead of whole-repo inspection.
5. Using one huge prompt on a large monorepo when subsystem-specific passes would be sharper.

## Verification Checklist

- [ ] `agy` installation verified
- [ ] Repo path passed with `--add-dir`
- [ ] Prompt scope chosen: full audit, architecture, risks, or tests
- [ ] Output includes concrete files/modules, not just generic claims
- [ ] High-impact claims verified before final reporting
- [ ] Uncertainty explicitly labeled
