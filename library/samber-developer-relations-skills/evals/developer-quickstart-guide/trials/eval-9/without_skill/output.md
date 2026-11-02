## Automated quickstart verification for Palisade

Both incidents share one root cause: **the quickstart's correctness depends on things outside the quickstart's own release cycle** — a config key that changed in *your* minor release, and a default that changed in *someone else's* release. Testing the quickstart once, at doc-authoring time, catches neither. You need a recurring, environment-realistic check.

### 1. Extract the quickstart into a real, runnable artifact

Stop letting the doc page hold hand-typed code. Keep the quickstart as an actual file in the repo (`examples/quickstart/`), and have the docs page **embed** it (snippet-include), never copy-paste. This doesn't catch drift by itself, but it guarantees the thing you test is the thing customers read — no second, silently-diverging copy.

### 2. Run it twice, on a schedule, against different dependency resolutions

Run the extracted quickstart in CI two ways:

1. **Pinned run** — exact SDK + dependency versions the docs currently declare. This is your baseline; it should always pass. If it doesn't, the harness is broken, not the product.
2. **Floating run** — install SDK `latest` and upstream deps unpinned, exactly how a new user's `npm install`/`go get` resolves today. This is the one that would have caught both real incidents.

Diff the two runs' output. A break that shows up only in the floating run, with a new SDK version, is case 1 (your minor release). A break that shows up with the *same* SDK version but a newer upstream dep, is case 2. **This diff tells you whose fault it is automatically** — no engineer has to bisect after a customer reports it.

Trigger the floating run:
- On every Palisade release (block or at minimum hard-flag the release if it breaks — a config rename shouldn't ship without someone seeing "this breaks the quickstart" on the same PR).
- On a **daily schedule independent of your releases**, since upstream dependency drift has nothing to do with when you ship.

### 3. Assert on the documented output, not just exit code

The contract you're breaking isn't "the command errors" — it's "the customer doesn't see what the page promised." Assert the test's output matches the literal success output shown on the page. A silently-different response body is exactly what a renamed config key produces (no crash, wrong behavior).

### 4. Catch the config-key case at the source, before it ever reaches docs

A renamed config key is a contract break hiding inside a minor release. Add a small fixture — the documented config keys, in a file the SDK's own config parser actually validates in a unit test. Renaming a key without touching that fixture fails CI **at the PR that renames it**, days before the quickstart job would ever notice. This is cheaper than catching it downstream and it's the fix that matches your own semver discipline (a rename like this arguably shouldn't be a minor release at all).

### 5. Route failures to the person who can fix them

A failing quickstart test should auto-file a ticket against the SDK area owner (CODEOWNERS on the config/dependency surface), **not the technical writer** — she can't fix a code regression, and looping her in on-call for it just adds to the backlog you're trying to fix. She gets pulled in for the resulting prose/example fix, after.

---

## Who should own writing these pages

Right now one role is carrying two different jobs that want different skills: **staying correct as the SDK changes** (needs someone who knows the moment a key gets renamed — that's the engineer making the change) and **staying clear, consistent, and well-structured** (that's the writer's actual strength). Funneling both through one person is why she's three weeks behind, and it's also *why* nobody caught either break — the person who knew about the change wasn't the person responsible for reflecting it.

**Recommendation: split by responsibility, not by page.**

- **Engineers own first-draft accuracy for anything they change.** If a PR renames a config key, changes a default, or bumps a dependency that the quickstart touches, the PR must update the relevant doc/example in the same diff. Enforce this mechanically: a CI check that greps `docs/` for the old key name and fails if it's removed from code but still referenced in docs. This is the same principle as commit-linked docs changes — the person with the context writes the change while they still have it, not three weeks later from a ticket.
- **The writer owns clarity, structure, consistency, and the final pass** — editing engineer-submitted drafts for tone and IA, not originating every technical fact from scratch. This is the standard split at doc-led orgs (Stripe, Twilio): engineers draft accurate, writers make it read well.
- **Split her queue into two lanes.** "Page is currently wrong" (correctness bugs, like the two incidents) is P0 and bypasses her normal queue — engineer fixes same-day, she reviews after. "New tutorial / polish / restructuring" stays in the normal drafting backlog. Right now both probably sit in the same three-week queue, which is why a customer-facing break waits as long as a nice-to-have rewrite.
- **If headcount allows, formalize a rotating "docs on-call" engineer** rather than leaving correctness solely dependent on individual PR discipline. It's a small ask per person and removes the single point of failure that made both incidents possible.

Net effect: the writer's backlog stops absorbing work that was never really writing work — it was engineering work mislabeled as a docs problem because she was the only person assigned to "docs."