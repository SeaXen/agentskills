# "Migrating from v2 to v3" — Script v2

**[SCREEN: v2 config file, full frame, 2 seconds]**

**VO:** This is a v2 config. Nothing wrong with it — until you run it from a monorepo.

**[SCREEN: highlight the `paths` block]**

**VO:** The v2 loader resolved paths relative to the working directory. Run the build from `/apps/web`, it works. Run the exact same command from the repo root, it breaks.

**[SCREEN: split screen — same command, two directories, two different outcomes]**

**VO:** Same config. Same command. Different answer depending on where your shell happened to be standing.

**[SCREEN: v3 resolver diagram — file walks up to nearest config, not cwd]**

**VO:** Here's the fix: the v3 resolver walks up from the file itself, not from your shell. It finds the nearest config and stops. Your terminal's location stops mattering.

**[SCREEN: same split-screen test, now both sides match]**

**VO:** Run it from the root. Run it from three folders deep. Same result, every time. That's what "deterministic" means here — not faster, not smarter. Predictable.

**[SCREEN: cache key diagram — v2 (absolute path) vs v3 (content hash)]**

**VO:** The cache got the same treatment. v2 keyed the cache off the absolute path. Two developers, same commit, two different machines, two different cache keys — so the cache never hit. v3 hashes the resolved config content instead. Same input, same key, every machine.

**[SCREEN: CTA card — v3 migration guide link]**

**VO:** Full migration guide is linked below. Update your loader, delete your `.cache` folder once, and you're on v3.

---

Two things I changed on purpose, flagging both:

- **Cut the Windows path bug.** It's real and worth documenting, but it doesn't belong in the middle of the resolver explanation — it breaks the "same result everywhere" beat you're trying to land. Put it in the video description or a pinned comment instead ("Known issue: UNC paths on Windows — tracking issue #___"), not in the narration.
- **Dropped the "4x faster" claim.** Nothing in the beats you gave me supports a specific multiplier, and an unverified performance number in a migration video is the kind of claim that gets screenshotted and thrown back at you in an issue thread. If you have a benchmark (before/after, same repo, same machine), give me the numbers and I'll write the line around them. Otherwise I'd cut it entirely and let "deterministic" carry the win — it's the more defensible and more specific claim anyway.