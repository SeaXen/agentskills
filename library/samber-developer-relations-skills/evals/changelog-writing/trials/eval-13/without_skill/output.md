I looked through this repo (everything outside `skill-wip/`, which I left untouched as instructed) and there's no Ferrymill project here — this repo (`example-repo`) is entirely affiliate-marketing content: `affiliation-programs/`, `sponsors/`, `telemetry/`, `research/`. No `pyproject.toml` anywhere outside `skill-wip/`, no ORM code, nothing named Ferrymill.

So I'm stuck on two fronts, and I'd rather flag that than hand you a fabricated changelog:

**1. I don't know what the six breaking changes actually are.** Your message names the deliverable shape (before/after, codemod, deprecation timeline × 6, plus Added/Fixed) but not the content — what actually changed in Ferrymill's API. I could invent six plausible-sounding ORM breaking changes, but then the before/after code, the codemod snippets, and the deprecation dates would all be fiction dressed up as your real 4.0.0 release notes. If someone runs a codemod I made up against real code, it does nothing useful at best and silently mangles something at worst.

**2. I can't find the real `pyproject.toml` to bump, or a repo to tag.** It's not here outside `skill-wip/`, and I'm not going to touch that directory per your instruction. If Ferrymill lives in a different local path or a separate repo, point me at it.

What I need from you to actually write this:

- For each of the six breaking changes: what the old API looked like, what it looks like now (even a rough signature is enough — I'll flesh out the code and prose).
- When each one was first flagged as deprecated (version + rough date), so the timelines are real.
- The current version in `pyproject.toml` (to confirm the 3.x → 4.0.0 bump) and where that file lives.
- Anything you want called out under Added / Fixed since the last release.

Send me those and I'll write the full 4.0.0 notes in one pass — no back-and-forth needed after that — and do the version bump + tag once I can see the actual file.