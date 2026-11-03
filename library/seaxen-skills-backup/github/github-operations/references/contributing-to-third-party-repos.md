# Contributing Features to Third-Party GitHub Repos

## When to use this pattern
User wants to contribute a feature (issue, PR, or both) to an upstream open-source repo.

## Workflow

### 1. Analyze the codebase first
- Clone the repo locally
- Identify existing infrastructure that already solves part of the problem
- Check if the feature partially exists (common — don't reinvent)
- Find the exact gap vs what's already built

### 2. Scope the PR correctly
- Reuse existing primitives (services, utils, types) — don't duplicate
- Keep PRs narrow: one feature surface per PR
- Separate "data model" changes from "UI" changes from "runtime behavior" when possible
- Don't overscope: if runtime behavior already works, the PR may only need API + UI

### 3. Fork + branch workflow
```bash
gh repo fork <owner>/<repo> --clone=false
git remote add fork https://github.com/<user>/<repo>.git
git checkout -b feat/<feature-name>
# make changes
git push fork feat/<feature-name> --force-with-lease
# Confirm default branch: gh repo view <owner>/<repo> --json defaultBranchRef
# decolua/9router uses master, not main
gh pr create --repo <owner>/<repo> --head <user>:<branch> --base master
```

### 4. Issue + comment pattern
Often the best approach:
1. Open issue describing the problem
2. Comment on the issue clarifying scope after analysis
3. Open PR referencing the issue

### 5. PR body style
- Short, GitHub-native
- What / Why / Changes / How it works / Verification
- Reference the issue with `Closes #N`
- Note what already works vs what the PR adds

### 6. Test verification
- Always run `npm run build` (or equivalent) before pushing
- Run the specific test files you changed
- **9router:** from repo root, `npx vitest run --config tests/vitest.config.js tests/unit/<file>.test.js` (avoid relying on `tests/package.json` `/tmp/node_modules` path alone)
- For pre-existing test failures: verify they fail on clean main too
- Document what passed/failed in the PR

## Pitfalls
- Don't assume the feature doesn't exist — check the codebase first
- Pre-existing test harness failures (e.g. localStorage.clear) are not your bug
- LSP errors from missing node_modules are not real errors
- Dynamic imports inside class methods are a code smell — use static imports
- Making new interface fields optional (`keys?:`) is safer for backward compat with existing test mocks
