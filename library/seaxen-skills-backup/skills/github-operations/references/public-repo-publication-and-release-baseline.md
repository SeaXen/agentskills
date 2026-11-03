# Public repo publication and release baseline

Use this when a local app or tool needs to be turned into a clean public GitHub repository.

## Goal
Ship a repo that matches reality:
- active runtime files only
- no secrets or local junk
- usable install/docs surface
- basic release metadata present

## Minimal publication sequence
1. Identify the real runtime entrypoints and remove or archive stale alternatives that misrepresent the app.
2. Read existing `README`, `.gitignore`, env examples, compose files, startup scripts, and license state before rewriting docs.
3. Normalize ignores for public safety:
   - `.env`
   - runtime `data/`
   - caches
   - local archives/backups
   - editor/OS junk
4. Stage only intended publishable files first; inspect the staged diff/stat before the first commit.
5. Scan staged content for secret-like values and runtime leftovers.
6. Commit the first clean baseline.
7. Push to GitHub.
8. Add release metadata if missing:
   - `LICENSE`
   - `CHANGELOG.md`
   - screenshots in `docs/screenshots/`
   - semantic-ish tag like `v0.1.0`
9. Push the tag.
10. Verify the remote repo, not just local git:
   - README renders
   - screenshots exist remotely
   - LICENSE exists remotely
   - CHANGELOG exists remotely
   - tag exists on origin

## Screenshot rule
README screenshots should be captures of the real running app.

If the normal browser path is awkward:
- use a temporary test port or a no-auth test instance for non-sensitive surfaces
- use Playwright Chromium when Firefox/headless paths are flaky
- verify the generated images visually before committing them

## Self-hosted app doc truth
For self-hosted tools, the README should answer the operator questions directly:
- what runs the app
- host mode vs Docker mode
- what gets auto-created on first run
- whether `.env` is required or only recommended
- where runtime state is stored
- what auth/recovery path exists

## Pitfalls
- Publishing a repo that still contains dead/stale framework files from an older architecture.
- Calling the repo ready before `.gitignore` protects runtime state and secrets.
- Committing screenshots that do not actually show the intended app surface.
- Pushing tags/docs without verifying they exist on GitHub.
