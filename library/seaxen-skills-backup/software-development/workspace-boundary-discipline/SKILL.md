---
name: workspace-boundary-discipline
description: Keep plans, scaffolds, and edits inside the correct project boundary when the shell cwd and task ownership differ.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [workspace, planning, repo-hygiene, multi-project, artifact-placement]
---

# Workspace Boundary Discipline

## When to use

Use this when:
- the host has multiple app repos side by side
- the current shell cwd may be unrelated to the task
- you are creating plans, scaffolds, Docker apps, or other project artifacts
- the user is asking about Hermes itself while the cwd points at some other app

## Core rule

Do **not** let current cwd decide artifact placement by accident.

Decide artifact location from **task ownership** first:
- Hermes-global task -> save under global Hermes paths like `/root/.hermes/...`
- standalone new app task -> save inside that app root
- existing project task -> save inside that project root

If cwd and task ownership disagree, trust **task ownership**, not cwd.

## Required checks before writing anything

1. Identify the real target project/app.
2. Identify whether the task is:
   - global Hermes work
   - standalone new app work
   - existing project work
3. Compare that target to current cwd.
4. State the chosen save root clearly before or when writing.
5. For existing repo work, set that repo root as `workdir` for every mutating command, plus every verification command whose result depends on repo state (`git`, tests, build, Docker, file sync).
6. Before any commit/push, inspect `git status` from the target repo root and confirm unrelated untracked paths are not being swept in.

## Durable pitfalls

### Pitfall: doing correct work in the wrong shell context

On multi-repo hosts, it is easy to inspect or edit the right files once, then let later commands fall back to the session cwd. That silently breaks verification and can pollute commits.

Fix:
- once the target repo is known, use its root as `workdir` on every related command, not just the first edit
- keep git checks, tests, build/redeploy steps, and file-sync steps anchored to that same root
- if you are finishing one pass and starting another, make the clean commit/push first, then begin the next pass
- re-check `git status --short --branch` before finalizing so unrelated untracked directories stay out of the commit

### Pitfall: saving Hermes plans into an unrelated repo-local `.hermes/`

This happens when the shell is sitting in another app repo and the planning workflow defaults to workspace-relative storage.

Fix:
- for Hermes dashboard / Hermes terminal / Hermes-agent planning, prefer `/root/.hermes/plans` unless the user explicitly wants project-local storage
- do not write Hermes planning artifacts into an unrelated app repo just because cwd happens to be there

### Pitfall: overcorrecting and forcing everything into global Hermes paths

For a new standalone app requested at a specific path, project-local storage is correct.

Example:
- user asks to create `/mnt/tb/1Apps/Rexterm`
- plans and scaffolding for that app should live under `/mnt/tb/1Apps/Rexterm/...`, not `/root/.hermes/...`

## Practical decision table

- User asks about Hermes feature, dashboard, terminal, plugin, profile, skill, memory, gateway -> default to global Hermes paths
- User asks to create a new named app at a specific filesystem location -> use that app root
- User asks to modify an existing repo and names the repo/path -> use that repo root
- User does not name the target and cwd is ambiguous -> clarify before writing

## Pitfall: changing a cloned repo when the real target is the installed/live copy

Common trap:
- user pastes a GitHub repo URL for a Hermes plugin or app already installed locally
- you clone to `/tmp` and edit that checkout
- the live system keeps using `~/.hermes/plugins/...` or another installed path, so the requested change did not actually reach the running app

Required handling:
1. Treat the repo URL as source context, not automatic proof that the clone is the real target.
2. Check whether the same project already exists in the live install location (for Hermes plugins, usually `~/.hermes/plugins/<name>`).
3. If the user asked to "update" the app rather than prepare a patch/PR, prefer mutating the installed/live copy.
4. If you touch a throwaway clone for inspection, explicitly mirror the final change into the real installed path before claiming success.
5. Verify against the live surface, not just the clone: inspect the installed file, check the effective default value, and hit the actual listening port/process when applicable.
6. For risky settings/auth changes, do NOT flip the production config just to test the flow. Spin up a temporary instance from the repo clone on a different localhost port with a small throwaway config, browser-verify the behavior there, then deploy the code to the live install with the feature still disabled by default.

Good response pattern:
- `The GitHub repo was useful for inspection, but the live target is ~/.hermes/plugins/<name>, so I changed that installed copy and verified the running service there.`
- `I verified the auth flow on a temporary localhost instance with a throwaway config first, then synced the code into the live install without changing the production setting by default.`

## Safe verification pattern for auth / security / access-control changes

When a feature changes login behavior, route protection, or access mode:
- keep the real service on its current port and current user-visible settings during development
- write tests first for redirects, login success, and public/private behavior
- run a temporary instance from the repo clone on an alternate localhost port with a minimal test config
- browser-test the protected route redirect, successful login, logout, and the allowed public route(s)
- only after that, sync code into the live install and restart the real service
- leave the new security feature disabled by default unless the user explicitly asked to turn it on immediately

This avoids locking the user out of the real dashboard during verification and keeps repo-state testing separate from installed-state verification.

## Project organization preference for standalone apps

When the user asks to keep a standalone app organized, prefer the lowest-clutter layout that matches the app style they ask for. Do not assume a frontend/backend split is wanted just because the app has UI + server code.

Two acceptable patterns:

### Split layout, only if requested or already clearly established

```text
<App>/
├── backend/
├── frontend/
├── docker-compose.yml
├── README.md
├── .env.example
└── .gitignore
```

### Single-root layout, preferred when the user says “like many app, one root for all”

```text
<App>/
├── app/
├── static/
├── data/
├── tests/
├── _archive/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── .dockerignore
```

Rules:
- Ask/interpret whether the user wants split root or single-root before reorganizing when ambiguous.
- Before moving folders or reorganizing a working app, create a timestamped full backup outside the project root and record its checksum.
- Do not delete old docs/scripts/plans/backups/unused frontend code/vendor caches; move them under `_archive/` unless the user explicitly asks for deletion.
- For Docker apps, update compose paths and add `.dockerignore` so runtime state, archives, sockets, and large unused folders do not enter the build context.
- After reorg, rebuild and live-verify the app still works; also verify persistent/runtime data where relevant.

## Response pattern

When path choice matters, say it explicitly and early:
- `Current cwd is X, but this task belongs to Y, so I will save under Y.`
- `I will also run git/tests/build from Y so verification and commits stay inside the same repo boundary.`

That prevents silent misplacement and makes corrections less likely.

## References

- `references/repo-pass-discipline.md` — concise pattern for repo-root anchoring, clean pass boundaries, and pre-commit scope checks.
