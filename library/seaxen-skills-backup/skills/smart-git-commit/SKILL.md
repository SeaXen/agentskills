---
name: smart-git-commit
description: Use when the user asks to commit, push, prepare a PR, or clean up git history. Produces disciplined commits with diff review, selective staging, test checks, secret awareness, and concise rationale.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [git, commit, github, pull-request, conventional-commits, safety]
    related_skills: [github-pr-workflow, github-code-review]
---

# Smart Git Commit

## Overview

Use this skill when the user wants code changes recorded cleanly in git.

This is a **Hermes-safe, lean version** of a stricter commit workflow. It keeps the useful parts:
- inspect before committing
- avoid blind staging
- check for obvious secrets
- run relevant tests when available
- split unrelated changes when necessary
- write commit messages that explain what changed and why

It intentionally does **not** instruct the agent to read or modify persistent agent-policy files like `CLAUDE.md` or similar tool-specific control files.

## When to Use

Use when the user says things like:
- "commit this"
- "save my changes"
- "push this branch"
- "open a PR"
- "clean up these commits"
- "write a better commit message"

Do not use for:
- non-git tasks
- publishing directly to protected branches without explicit user intent
- repos with unrelated dirty worktree changes you have not analyzed yet

## Workflow

### 1. Inspect first
Run:
```bash
git status
git diff --stat
git diff
git log --oneline -5
```

Goal:
- understand changed files
- see whether changes are one concern or many
- catch accidental edits before staging

### 2. Check for obviously sensitive material
Before commit, inspect the diff for:
- API keys
- tokens
- private keys
- `.env` content
- passwords or connection strings

Minimum checks:
```bash
git diff | grep -E 'AKIA|ghp_|gho_|ghs_|sk_live_|sk_test_|BEGIN .* PRIVATE KEY|password=|DATABASE_URL' || true
git status --short
```

If a secret appears:
- stop
- unstage the file if staged
- replace secret with env/config reference
- confirm cleanup before proceeding

### 3. Run the relevant tests when practical
Use the repo's normal test command if obvious.
Common patterns:
```bash
npm test
python -m pytest
cargo test
go test ./...
make test
```

Rules:
- if tests exist and are fast enough, run them before commit
- if tests fail, fix first or tell the user exactly what failed
- if no test path is obvious, say that clearly in the final summary
- if you use `uv run --with ...` for disposable verification, inspect `git status` afterward; uv may create `uv.lock`, which should not be committed unless the repo intentionally tracks uv lockfiles

### 4. Split mixed concerns
If the diff mixes unrelated work, split it.
Examples:
- feature + formatting cleanup
- bug fix + dependency bump
- implementation + unrelated docs sweep

Preferred approach:
- make atomic commits
- stage specific files or hunks
- keep each commit explainable on its own

Useful commands:
```bash
git add <file>
git add -p
git diff --cached --stat
git diff --cached
```

Never default to blind `git add .` when the worktree contains mixed or unreviewed changes.

### 5. Write a strong commit message
Preferred subject format:
```text
<type>(<scope>): <imperative summary>
```

Common types:
- `feat`
- `fix`
- `refactor`
- `docs`
- `test`
- `chore`
- `perf`
- `ci`

Subject rules:
- imperative mood
- no trailing period
- aim for <= 72 chars
- reflect the actual change, not vague activity

When a richer body is justified, use this structure:
```text
CONTEXT: What was wrong or missing before this change.
CHANGE: What was changed.
WHY: Why this approach was chosen.
IMPACT: User, system, or maintenance effect.
```

Example:
```text
fix(auth): preserve redirect target after login

CONTEXT: Login flow always redirected users to the dashboard and discarded
requested destination pages.
CHANGE: Preserve and validate the next parameter during login redirect.
WHY: This keeps protected deep links usable without introducing open redirect behavior.
IMPACT: Users return to the page they originally requested after authenticating.
```

### 6. Commit carefully
After selective staging, verify before commit:
```bash
git diff --cached --stat
git diff --cached
```

Then commit:
```bash
git commit
```
or:
```bash
git commit -m "<subject>"
```
Use a body when the change is not obvious from the diff alone.

### 7. Push safely
Before push:
```bash
git branch --show-current
git remote -v
```

Rules:
- prefer pushing feature branches
- do not push directly to `main` / `master` unless the user explicitly wants that
- do **not** push or update a PR just because local fixes are complete; if the user did not explicitly ask for a push/PR update in this turn, stop after the local commit and report status first
- if upstream is unset:
```bash
git push --set-upstream origin <branch>
```

### 8. PR follow-through
If the user wants a PR:
- ensure branch is pushed
- summarize the change clearly
- include test status
- link issue if known

If GitHub CLI is available, use it. Otherwise use Hermes GitHub tools.

## Decision Rules

- **Small trivial change:** short conventional subject is enough
- **Risky or subtle change:** add commit body
- **Multiple concerns:** split commits
- **Failed tests:** do not pretend the commit is production-ready
- **Secrets in diff:** hard stop

## Secret-Safe Staging and Diagnostics

Prefer scanning the **staged index** rather than the entire working directory, which may contain ignored live runtime state:

```bash
git diff --cached --name-only --diff-filter=ACMR
git diff --cached --check
git diff --cached
```

Before committing, explicitly reject staged paths such as `.env`, runtime `data/`, archives, generated account/session files, cookies, and backups. Scan staged text for private-key headers and provider-token formats.

Do not print rendered configuration from a live secret-bearing environment into chat or CI logs. Commands such as `docker compose config` interpolate `.env` values. For diagnostics, use a temporary source copy plus synthetic `.env`, override all secret variables, or redirect to a restricted temporary file and extract only non-secret fields.

If a real token appears in output, treat it as compromised: rotate it immediately, remove rendered temporary files, reload dependent services, and verify the replacement without printing it. A one-way password hash generally does not require password rotation unless the password itself was exposed.

## Remote CI Follow-Through

After pushing a PR branch:

- `no checks reported` is **not** a pass;
- inspect `gh run list`, PR `statusCheckRollup`, Actions permissions, and workflow registration;
- validate new workflows locally with `actionlint` (including embedded ShellCheck) before blaming GitHub;
- explicit workflow dispatch may return `404` until a newly introduced workflow is registered on the default branch;
- do not merge solely to manufacture a green check—report the platform limitation and preserve the review boundary unless the user explicitly authorized merge.

When a CI Docker job claims to test hardened Compose behavior, it should start the actual Compose stack and execute one real application feature. A syntax-only `docker compose config` or weaker ad-hoc `docker run` is not equivalent.

## PR Reply Style
When replying to maintainer comments on GitHub PRs:
- **Short and GitHub-native** — no fluff, no markdown headers, just plain text that reads like a native maintainer response
- No greetings, no sign-offs, no pleasantery
- Lead with the answer, then brief justification if needed
- User explicitly prefers this style: "short and GitHub-native"
- Always use `--body-file` (or API JSON input) for replies that include backticks, paths, or multi-line lists so the shell cannot mangle the comment

## Common Pitfalls

1. **Blind staging**
   `git add .` without review often captures unrelated files.

2. **Vague subjects**
   Avoid messages like `fix stuff`, `update code`, `wip`.

3. **Skipping tests when a test path is obvious**
   If a repo clearly uses pytest/npm/cargo/go test, check it.

4. **One giant mixed commit**
   Separate refactor, feature, docs, and generated artifacts when possible.

5. **Assuming a local fix should be pushed immediately**
   Finishing the code is not permission to push. If the user did not explicitly ask to push or update a PR in the current turn, commit locally and ask/report first.

6. **Pushing to the default branch casually**
   Feature branch first unless the user clearly wants otherwise.

7. **Staging unrelated local edits with the intended fix**
   When fixing a review item, inspect `git diff` for auto-refresh defaults, cache-interval experiments, or other workspace nits; revert them before commit so the PR stays single-concern.

8. **Cherry-pick conflict leftovers**
   After cherry-picking onto newer main, search the tree for merge markers before committing. CHANGELOG Unreleased sections are frequent offenders.

## Verification Checklist

- [ ] Reviewed `git status` and diff before staging
- [ ] Checked for obvious secrets in the diff
- [ ] Ran relevant tests or explicitly noted why not
- [ ] Split unrelated changes if needed
- [ ] Verified staged diff before commit
- [ ] Wrote a specific commit subject
- [ ] Added body/rationale when useful
- [ ] Pushed safely to the intended branch
