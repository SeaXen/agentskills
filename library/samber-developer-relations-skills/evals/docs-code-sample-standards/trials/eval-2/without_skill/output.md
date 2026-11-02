# Sample testing tiers for Voltmesh docs

**CI enforces nothing today, and it can't for six weeks.** With no CI and no engineering time, the Run and Compile-only tiers are off the menu. Every one of the 160 snippets is unverified until a pipeline exists, and building that pipeline comes before any tiering work.

The tiers below are what we commit to once CI exists. I haven't run the census script on the corpus, so I haven't classified the other ~156 snippets. The tiers follow the docs-code-sample-standards skill.

| Sample | Tier | What CI enforces (once built) | Why |
|---|---|---|---|
| (a) Quickstart auth call | **Run** | Executes against a sandbox account with a CI-held test key and asserts the documented output. Runs on every docs PR and on a nightly schedule, so service-side drift turns the build red. | It's the adoption path. A broken quickstart costs a new user their first afternoon. |
| (b) Transcription job at $0.90/min | **Compile-only** | Lint or syntax check, plus a check that the snippet uses a placeholder key and a tiny fixed sample file. No execution, so no spend. | A run bills real money on every CI pass. It has no Run tier whatever the pipeline can do. |
| (c) `kubectl delete namespace voltmesh-dev` | **Compile-only** (lint and guard check) | Shell lint, plus a rule that fails the build if a destructive command lacks a visible warning and a confirmation step or dry-run. Never executed. | A destructive command has no Run tier. A copied-and-pasted delete is a P0 harm, ahead of any ordinary "doesn't work" bug. |
| (d) Post to a third-party partner webhook | **Compile-only** | Lint, plus validation of the payload against its schema. The host must be a reserved-range placeholder (e.g. `example.com`), not the real endpoint. | Running it calls someone else's service, which means their terms and their traffic. It has no Run tier. |

## During the six weeks (no engineering)

These are manual and not CI. Each is a one-time check or a visible label. None needs engineering time.

1. **Run the census once.** Run `scripts/sample-audit.py docs/ --format summary` from the skill. It lists every snippet, flags credential-shaped strings, and takes about an hour of a non-engineer's time.
2. **Fix P0s now.** Check (c) and any live-looking keys by hand. That means a warning line on the delete command and `<YOUR_API_KEY>` placeholders. This is the one thing that shouldn't wait.
3. **Label tiers on the page.** Mark any snippet that is pseudocode or a fragment as "Illustrative: not runnable". An unlabelled illustrative snippet looks broken.
4. **Cut before testing.** Delete redundant, outdated or trivial snippets. A deleted snippet costs readers nothing, and the 160 shrinks before any harness exists.
5. **Name an owner per snippet.** When a sample goes red, someone needs to receive it. Pick one person now, even among three engineers.

## What to tell the team

- Nothing is tested today, and we won't claim otherwise on the pages.
- First CI build (week 7 or later): a Compile-only job for all of (b), (c), (d) and every other snippet that bills, destroys, or calls a third party.
- Second build: a Run job for the quickstart path only, starting with (a).
- Everything else gets a tier after the census, not before.

I chose these tiers from the four descriptions alone. Two facts could change them:
- If you already have a staging account that can safely absorb the transcription cost, (b) could move to Run.
- If readers paste (d) heavily, it earns more attention first.