---
name: github-operations
description: "Use when working across the GitHub lifecycle: auth, repositories, issues, pull requests, reviews, releases, and gh-vs-REST fallbacks."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [github, git, gh, pull-requests, issues, repositories, auth, reviews, releases]
    related_skills: [smart-git-commit, requesting-code-review]
---

# GitHub Operations

## Overview

This is the class-level umbrella for GitHub work in Hermes. Load it when the user needs anything spanning GitHub authentication, repository setup, issue triage, pull request lifecycle, code review, CI/release operations, or when you need to choose between `gh`, plain `git`, and direct REST/API calls.

The main consolidation rule: do not think in narrow subskills first. Start from the full operator workflow and then drop into the relevant subsection below.

## When to use
- The user asks to work with a GitHub repo, fork, issue, PR, review, release, or CI run.
- You need to decide whether to use `gh`, `git`+credential helper, or `curl` against the GitHub API.
- You are preparing a repo for later issue/PR/review work and need auth + identity + remote sanity first.
- The task spans multiple GitHub surfaces in one session.

## Core rule
Always normalize three prerequisites before deeper GitHub work:
1. **Authentication path** — `gh` authenticated, or token/SSH-backed `git`
2. **Git identity** — `user.name` and `user.email`
3. **Repo context** — owner/repo, base branch, and remote URL

Do not treat issue/PR/review commands as standalone. Most failures come from skipping one of those three checks.

## Workflow map

### 1. Authentication and capability detection
- Prefer `gh` when installed and authenticated.
- Fall back to plain `git` + PAT/SSH for repository operations.
- Fall back to REST/API calls when `gh` is absent but API-side actions are still needed.
- Verify git identity even if `gh auth status` is green.

### 2. Repository setup and management
Use this branch for:
- clone / fork / create / sync / remotes
- release-first install triage from GitHub releases
- repo settings, branch protection, Actions, and releases

### 3. Issue operations
Use this branch for:
- issue creation from a bug report or feature request
- triage, labels, assignees, comments, and close/reopen
- converting issue context into a working branch or PR plan

### 4. Pull request lifecycle
Use this branch for:
- branch creation
- commit / push / PR open
- CI monitoring and fix loops
- merge or auto-merge

### 5. Code review
Use this branch for:
- pre-push local diff review
- remote PR review with inline comments
- approve / comment / request-changes decisions
- structured review summaries grouped by severity

## Section-specific durable lessons

### Auth subsection
- `gh` success does **not** imply git identity is configured.
- PAT/SSH are still first-class paths; do not over-assume `gh`.
- When `gh` is missing, keep moving with `git` + REST instead of stopping early.

### Repo subsection
- For install requests from GitHub, inspect release assets before cloning/building.
- Asset names can mislead; inspect the artifact type before declaring platform compatibility.
- Inspect the installer script itself before trusting repo identity. Some projects have branding/repo splits where docs and the public source repo use one owner/org, but the release installer downloads from a different repo via an internal default like `REPO="owner/name"`. When install/auth behavior looks inconsistent, check the script's embedded release source instead of assuming the docs repo is the artifact source.
- Secrets management is dramatically easier with `gh`; say so plainly when the REST fallback becomes cumbersome.
- When turning a local project into a **public GitHub repo**, do a publication pass before the first push: remove stale/dead files that no longer represent the active runtime, normalize `.gitignore` for secrets/runtime state (`.env`, data dirs, caches, archives), and inspect the staged diff for secret-like content before committing.
- For small self-hosted apps, a good public-release minimum is: accurate `README.md`, `LICENSE`, small `CHANGELOG.md`, screenshot assets checked into the repo, and an initial semver-ish tag (for example `v0.1.0`). Do not call the repo "ready" if it still lacks the basic install/runtime truth the next operator needs.
- When generating screenshots for a repo README, prefer **real app captures** over mockups. If one browser path fails, pivot — for example use Playwright Chromium with a temporary no-auth or test port for authenticated surfaces — then verify the images are actually the intended UI before committing them.
- For public-repo screenshots, do a **sensitivity pass** before committing: avoid screenshots that expose live chat IDs, tokens/placeholders, LAN/Tailscale addresses, runtime PIDs, notification history, or other environment-specific admin details. If a screen is operationally useful but too revealing, omit it from the README rather than normalizing leaks into repo assets.
- Headless Chromium is a durable fallback for README asset generation on Linux hosts when richer browser automation is unavailable: `chromium --headless=new --no-sandbox --disable-gpu --hide-scrollbars --window-size=<W>,<H> --screenshot=<path> <url>`. This is especially useful for quickly capturing real dashboard/app surfaces from localhost.
- After the first public push, verify the remote truth, not just local git state: confirm the README renders on GitHub, required files exist remotely, and the release tag actually reached `origin`.
- If the GitHub web UI returns 404 during remote verification, check repo visibility before treating it as a broken README or missing asset. A private repo will make otherwise-correct GitHub page and raw asset checks look broken from unauthenticated/browser paths.
- Important release pitfall: a pushed git tag is **not** the same thing as a published GitHub Release entry. For public-release work, explicitly check whether the Release object exists (`gh release view <tag>` or equivalent). If it does not, create it with real release notes instead of assuming the tag page is enough.
- **When adding a new GitHub Actions workflow for image publishing or CI, verify platform-side execution separately from YAML validity.** Good sequence after push: (1) `gh workflow list` to confirm GitHub indexed the workflow, (2) `gh run list --workflow <file-or-name>` to see whether a run actually started, (3) if nothing runs, inspect Actions policy with `gh api repos/<owner>/<repo>/actions/permissions/workflow`. If manual dispatch `gh workflow run ...` fails with `HTTP 422: Actions has been disabled for this user`, treat it as a repo/account Actions-permissions problem, not a bad workflow file. Fix in GitHub settings by enabling Actions for the repo/user and granting workflow token write access when the workflow needs package publishing.
- **GHCR verification pitfall:** probing `https://ghcr.io/v2/<owner>/<image>/tags/list` anonymously can return `401 Unauthorized`; that does not prove the package is missing. Verify publication via authenticated `gh`/GitHub package surfaces or after a confirmed successful workflow run.
- When polishing a public repo README after release work, do a contradiction pass for stale statements that may have been invalidated by earlier changes (for example a lingering note that says no license exists after `LICENSE` was added).
- **GitHub Pages product landing** (static marketing site, not the app runtime): put `docs/index.html` + `docs/.nojekyll` + assets under `docs/`, document enable path in README, push, then `gh api -X POST repos/<owner>/<repo>/pages` with `source[branch]=main` and `source[path]=/docs`. Expect `https://<user>.github.io/<repo>/` to 404 briefly after first deploy. See `references/github-pages-product-landing.md`.
- **Check PR state before pushing to same branch:** `gh pr view <num> --repo <owner>/<repo> --json state,mergedAt` — if merged, create new branch for new work; pushing to merged branch only updates fork, not upstream.

See `references/public-repo-publication-and-release-baseline.md`, `references/github-pages-product-landing.md`, and `references/github-release-installer-repo-split.md`.

### Dashboard subsection
- For dashboard PRs (API + frontend), see `references/dashboard-pr-patterns.md` for common pitfalls: handler param passing, frontend fetch params, fragile SQL string replacement, integer division truncation, chart window mismatch.

### Issues subsection
- Treat issue triage as a workflow, not just label edits: read, classify, label, assign, then comment if needed.
- Explicit issue templates improve later agent execution because repro steps become machine-usable.
- For upstream OSS requests, separate **provider requests** from **cross-cutting feature requests**: use the project's provider-request discussion thread when maintainers ask for provider additions there, but open a real Issue for generic capabilities like multi-credential support, pooling, failover, or auth/routing architecture changes. Do not bury a platform-wide feature request inside a provider-request thread.
- When a user asks you to open an issue/PR because 'you did it before', do not hedge endlessly — first verify `gh auth status`, then act if auth is available. The useful caution is to verify before claiming success, not to talk abstractly about what might be possible.

### PR subsection
- CI repair is an iterative loop: inspect failed checks, fix locally, push, re-check, repeat.
- Keep the PR body honest about what was tested and what remains follow-up.
- See `references/contributing-to-third-party-repos.md` for the full fork-and-PR workflow when contributing features to upstream repos (not just bug fixes). Includes the pattern: clone locally → analyze existing infrastructure → find the gap → narrow PR scope → fork → branch → push → create PR. Also covers how to verify pre-existing vs introduced test failures.
- **Verify your regression test actually catches the bug.** A test that passes with the fix in place is necessary but not sufficient — it must also *fail* without the fix, and ideally with the exact production error. Cheap negative-verification recipe: (1) write fix + test, (2) run the new test → must pass, (3) `git stash push <fixed-file>` (or `git checkout` to revert just that file), (4) run the new test → must fail with the production error, (5) `git stash pop` to restore the fix, (6) re-run → pass again. State steps 2/4/6 in the PR body so reviewers don't have to re-derive the proof.
- **Fork-and-PR workflow when upstream push denied:** `gh repo fork <owner>/<repo> --clone=false`, add fork remote, push branch to fork, `gh pr create --repo <owner>/<repo> --head <fork-user>:<branch> --base main`.
- **Upstream bug PR (library, not Hermes):** fork `gh repo fork owner/repo --clone=true`, reproduce on live data, add regression test if repo has `tests/`, push `SeaXen:fix/...`, `gh pr create --repo owner/repo --head SeaXen:branch`. Example: Mnemosyne `create_backup` must `sqlite_vec.load()` on **both** src and dst — https://github.com/AxDSan/mnemosyne/pull/374. Narrow scope; note follow-up bugs in PR body.
- **If an earlier PR is still open and new local work builds on it, check whether the earlier PR head is a real upstream branch before trying to stack a new PR on top of it.** If the upstream repo does not have that head branch as a base, `gh pr create` can fail with errors like `Base ref must be a branch` / `No commits between ...`. In that case either push the follow-up onto the existing PR branch, or create a new PR against `main` that explicitly supersedes/includes the earlier PR.
- **PR review feedback loop:** If maintainer or bot requests changes, address ALL items (blockers + refactoring suggestions) before considering PR ready. Common misses: handler not passing params to called function, frontend fetch not including query params, fragile string replacement in SQL, integer division truncation. For auto-review and inline-comment repair patterns, use `references/pr-review-handling.md`.
- **When a PR shows `mergeable: CONFLICTING`, resolve it locally against the PR base branch and re-verify the actual changed path(s), not just the conflict file.** Good pattern: fetch the base branch, merge/rebase it into the PR branch, inspect the conflicting file *plus any touched helper/test files that encode the same behavior*, resolve by preserving both the upstream fix and the PR-specific fix, run the narrowest high-signal regression test for that area, then push and confirm `gh pr view --json mergeable,headRefOid,updatedAt` flips back to `MERGEABLE`.
- **When review says the PR scope drifted, split it immediately instead of arguing the review.** Safe pattern:
  1. preserve the broader follow-up work on a separate branch (`git branch <new-branch> <current-head>`)
  2. hard-reset the reviewed PR branch back to the last in-scope commit(s)
  3. rerun lint/tests on the reduced branch
  4. `git push --force-with-lease` the PR branch
  5. open a separate PR for the deferred work with the migration/tests/docs the maintainer asked for
  6. reply on the original PR with the exact split and link the follow-up PR
  This is especially important when the review calls out schema drift or branch contents no longer matching the PR title/body.
- **Issue-style PR comments are a separate surface from review comments.** If `gh pr view --comments` does not show the maintainer note, check `gh api repos/<owner>/<repo>/issues/<pr>/comments` for top-level PR conversation comments, and `gh api repos/<owner>/<repo>/pulls/<pr>/reviews/<review_id>` for the full review body.
- **Use review-id filtering when a PR has multiple review rounds:** `gh api repos/<owner>/<repo>/pulls/<pr>/comments --paginate | jq '.[] | select(.pull_request_review_id==<review_id>)'`. This is the fastest way to isolate the latest inline comments when the browser anchor is noisy or truncated.
- **After a maintainer force-pushes or co-authors a replacement head commit, re-evaluate the PR against the CURRENT head before assuming earlier asks still apply.** Check `gh pr view <pr> --json headRefOid,updatedAt,commits,files,mergeable,statusCheckRollup` and compare the current `headRefOid` / latest commit(s) to the commit ids attached to older bot or maintainer reviews/comments. If the old review was anchored to an earlier head and the current commit message or changed files explicitly absorb those fixes, treat the earlier review as potentially stale and avoid redundant follow-up pushes/comments. This is especially important when the maintainer force-pushes a reconstructed branch and CI is already green.
- **When a maintainer changes the PR base branch and the PR becomes conflicting, do not blindly rebase if the branch was originally cut from a different integration branch.** First fetch the exact base ref (`git fetch upstream <base>:refs/remotes/upstream/<base>`), inspect `git diff --name-only upstream/<base>...HEAD`, and watch for unrelated files/CI commits entering the PR. If rebase drags upstream-only commits into the diff, rebuild cleanly: create a backup branch, `git reset --hard upstream/<base>`, cherry-pick only the intended PR commit(s), rerun the focused test, then `git push --force-with-lease`.
- **When a fix is real but only covers one surface, open a follow-up PR for the adjacent surfaces instead of quietly widening the reviewed PR.** Good pattern: keep the original PR narrow and mergeable, audit the remaining raw render/API paths, cut a fresh branch from the target release/base branch, add the minimum shared field/resolver needed (for example a server-side `providerDisplay`), cover it with a focused regression test, and link the new PR as a follow-up. This is the right move when analytics is fixed but log/detail views still leak raw IDs, or any similar “same concept, different surface” gap remains.
- **For maintainer review repairs, satisfy the exact requested architecture path when reasonable, not just an equivalent abstraction.** If the maintainer says “use existing `getProviderNodes()` via `@/models`,” prefer that over inventing a new helper even if the helper is technically clean. It reduces review friction and proves the route follows project conventions.
- **Treat stale bot inline comments as evidence to verify, not as proof the bug remains.** After pushing a fix, compare the comment’s `commit_id` and line to the current head, read the current file around the line, and rerun the regression. If the current code already has the requested branch/guard and CI is green, leave a short maintainer-facing reply with commit, exact fix, and verification instead of churning code to appease a stale bot comment.
- **Fallback when `gh pr edit` fails from GraphQL Projects classic deprecation:** update the PR body through REST instead of getting stuck. Pattern:
  1. write the desired Markdown body to a temp file
  2. JSON-wrap it safely: `python3 - <<'PY' ... json.dumps({'body': body}) ... PY`
  3. patch with `gh api -X PATCH repos/<owner>/<repo>/pulls/<pr> --input /tmp/pr_patch.json`
  4. verify with `gh pr view <pr> --json body,headRefOid,state,url`
  This avoids the `repository.pullRequest.projectCards` GraphQL deprecation path while preserving normal GitHub auth.
- **Fallback when `gh pr view --comments` or review listing breaks on the same GraphQL Projects classic deprecation:** pivot to REST issue/PR endpoints instead of treating the PR as unreadable.
  - top-level PR comments: `gh api repos/<owner>/<repo>/issues/<pr>/comments`
  - inline review comments: `gh api repos/<owner>/<repo>/pulls/<pr>/comments --paginate`
  - review summaries: `gh api repos/<owner>/<repo>/pulls/<pr>/reviews`
  This is the reliable path when the normal `gh pr view` comment surface fails even though plain PR metadata still works.
### Review subsection
- Review diffs at two levels: big-picture scope first, then file-by-file context.
- Diffs alone are insufficient for subtle bugs; open changed files with full context when needed.
- Distinguish blocking issues from suggestions so the final review state is legible.
- **PR reply style**: When drafting replies to maintainer comments on PRs, keep them short and GitHub-native. 2-3 lines max. Address the question directly without filler, preamble, or over-explanation. Just answer the concern and offer next steps if relevant. Example:
  > Yes — it's for longer-term context. 30d is useful, but it misses slower trends and month-over-month / year-over-year comparisons. 90d + 365d make the analytics page more useful without changing the default behavior.
  Do NOT draft verbose, formal, or explanatory responses unless the user explicitly asks for a detailed technical justification.
- **When posting a PR/issue comment through `gh`, do not inline rich text directly inside a shell-quoted `--body` string if it contains backticks, bracketed literals, or other shell-significant characters.** Use `--body-file` with a temp file or a single-quoted heredoc instead. Otherwise Bash may eat code spans like `` `isPrivateHostname` `` or bracketed examples like `` `[::1]` ``, producing a mangled public comment even though `gh` itself succeeds. After posting, verify the rendered body with `gh api repos/<owner>/<repo>/issues/<num>/comments` (or equivalent); if the comment was mangled, delete it and repost cleanly instead of leaving noisy repair comments.

## Decision defaults
- **Need GitHub API ergonomics?** Try `gh` first.
- **Need pure repo movement?** `git` is enough.
- **Need PR/issue/review automation without `gh`?** Use REST/curl, not hand-waving.
- **Need end-to-end GitHub work?** Follow auth → repo context → issue/branch/PR/review in that order.

## Common pitfalls
1. Starting PR or review work before confirming owner/repo and base branch.
2. Assuming `gh` auth means commits will attribute correctly.
3. Treating issue management, review, and PR handling as separate islands instead of one lifecycle.
4. Recommending source builds from GitHub before checking release assets.
5. Stopping at a plan when the real deliverable is a created issue, opened PR, posted review, or verified release action.

## Verification checklist
- [ ] Auth path confirmed (`gh` vs token/SSH)
- [ ] Git identity confirmed
- [ ] Owner/repo and base branch confirmed
- [ ] Correct GitHub surface chosen (repo / issue / PR / review / release)
- [ ] If side effects were requested, the actual GitHub action was executed and verified
- [ ] If CI or review was involved, findings are backed by actual diff/check output
