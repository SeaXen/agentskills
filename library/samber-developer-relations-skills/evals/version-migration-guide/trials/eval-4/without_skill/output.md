# v6 migration tooling: what to build with 3 engineer-weeks

**Recommendation:** don't spend the budget on a codemod plus a flag-based v5 shim. Build tooling that keeps working with nobody maintaining it, and use the one thing leadership hasn't offered, an owner, as the last item in the plan.

I haven't seen the 23 changes. The split below is an assumption, so check it in step 1.

## Why not the team's plan

**The flag-based compat shim is the worst item, and it's worse for auth.**
- It keeps v5 alive as a second code path. Every later change has to work under both behaviours.
- With 23 behavioural forks, the flag combinations can't be tested exhaustively. Bugs will show up in the combinations nobody tried.
- Nobody owns it after the rotation, so it will go stale while users depend on it.
- Users with a "temporarily keep v5" flag have no reason to migrate. The flag becomes permanent.
- Keeping v5 auth behaviour alive means every future security fix has to be applied twice. If the v5 behaviour is what you broke on purpose, the flag is a downgrade switch for attackers.

**An all-in codemod gives false confidence.**
- libcst handles syntax well: renames, moved imports, changed signatures. It can't tell whether `x.fetch()` is called on your `Client` without type inference. You'll end up matching on names heuristically.
- It can't handle semantic changes such as different defaults, return shapes, error types, or auth flow ordering. Those are probably a large share of the 23 in the auth module.
- A codemod that silently handles 60% of cases leaves users to find the other 40% in production.

**A codemod is run-once tooling, so it rots slowly.** It's worth building for the mechanical subset. It just shouldn't take all 15 days.

## Plan (15 engineer-days)

| Days | Item | Why it survives with no owner |
|---|---|---|
| 1 | **Triage the 23 changes** into A, B and C (below). Pull usage data: telemetry, public GitHub code search, support tickets. | One-off analysis. It sets the rest of the scope. |
| 1–2 | **Soften what you can.** For every A-type change, check whether a deprecated alias in v6 removes the break. Remove the aliases in v7 on a published date. | Each alias is about 5 lines and removes a whole item from the tooling backlog. |
| 4 | **Loud v6 errors and migration guide.** Removed names and kwargs raise errors that name the v5 thing, the v6 replacement, and the guide URL. Use module `__getattr__` and explicit `TypeError` messages. The guide has before/after snippets for all 23. | The messages live in the code. No tool needs to run. |
| 1.5 | **Final v5 release (v5.x) with `DeprecationWarning`s** on every call pattern v6 breaks. | Ships once. Users see warnings before the upgrade, not after. |
| 4–5 | **Scoped libcst codemod for category A only.** It's a single-file script run with `uvx`, with a pinned libcst version. It has before/after fixture tests. A `--todo` mode inserts `# TODO(v6): ...` comments at category-B sites. | Finite user base, run once per codebase. Fixture tests double as documentation. |
| 1 | **Validate on 3 real codebases.** Use your own examples and 2 or 3 customers or OSS users. Record the results as a coverage table in the guide. | You find out the real coverage before release, not after. |
| 1 | **Handoff and sunset.** Write a runbook, an issue template, and a dated "codemod unsupported after X" line. Get a named owner. | See below. |
| 0.5 | Buffer. | |

Schedule the guide and error messages first, then the v5 release. If the codemod slips, you've still shipped the parts that matter most.

## Triage categories for step 1

- **A. Mechanical:** renames, moves, changed signatures with a clear mapping. Use an alias if possible, otherwise the codemod.
- **B. Semantic:** changed defaults, return types, error types. Use a v5 deprecation warning, a v6 error message and a guide entry. The codemod only leaves a TODO.
- **C. Removed with no equivalent:** use a loud error and a guide section on alternatives.

**Auth module:** no compat flag. Every auth change gets a loud failure and an explicit guide entry. Auth is where silent v5 fallback does the most damage.

## If leadership insists on a shim

Keep it small and put a hard expiry on it:
- Client changes only, never auth.
- A separate package, for example `rossiter-sdk-v5-compat`, not a flag inside v6.
- Every use emits a `DeprecationWarning`.
- A published removal date, for example 6 months out.
- A named owner for the whole window.

## The real ask: an owner

Nobody maintaining this after the rotation is the central risk. Ask leadership for one of these before approving the budget:
- One named person at about 2 hours a week for 3 months. That covers codemod bugs and migration questions after the release, which is when most of the issues arrive.
- Or an explicit decision that the tooling is unsupported after release day. Then say so in the guide and the README, so users aren't surprised.

## Pushback script for the team

- "The codemod is still in the plan. It's scoped to the changes it can handle correctly."
- "The shim would double our test and security surface for a feature nobody will be assigned to maintain."
- "Loud errors and a guide cost less and keep working after we've moved to streaming."

## Open questions

1. How many of the 23 are A, B and C? If A is under 8, shrink the codemod to about 3 days and put the savings into the guide and validation.
2. Do you have usage data? Without it, rank by gut feel and say so.
3. Is there an owner after the rotation, even part-time?