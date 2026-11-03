# Repo-pass discipline

Use this when the task belongs to an existing repo but the session cwd may be elsewhere.

## Core pattern

1. Identify the real repo root.
2. Use that root as `workdir` for all repo-sensitive commands:
   - `git status`, `git diff`, `git add`, `git commit`, `git push`
   - tests and syntax checks
   - build/redeploy commands
   - file sync steps between generated/static/public assets
3. Finish the current feature pass cleanly before starting the next one.
4. Re-check `git status --short --branch` immediately before final answer.

## Why

A task can start with the right file edits and still drift later:
- tests run from the wrong directory
- Docker commands target the wrong compose context
- `git add .` sweeps unrelated files
- an old untracked directory gets mistaken for task output

## Practical guardrails

- If the user says "continue this repo" and the session cwd is `/root`, do not rely on ambient cwd after the first command.
- Treat commit boundaries as part of workspace discipline: commit/push the stabilized pass before beginning fresh follow-up work.
- If `git status` shows unrelated untracked paths, call them out explicitly and leave them out unless the user asked for them.

## Example shape

- Repo root: `/mnt/tb/1Apps/liquidrisk`
- Session cwd: `/root`
- Correct move: run edits, tests, Docker redeploy, browser verification, commit, and push with `workdir=/mnt/tb/1Apps/liquidrisk`
- Final scope check: confirm functional files are committed, and note any unrelated leftovers like local `docs/` separately instead of silently including them.
