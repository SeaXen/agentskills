Using the `oss-governance` skill. Sandglass is two maintainers, a "stadium" project (many users, almost no outside contributors), and the trigger isn't a dispute — it's a coverage gap: Nadia's out for five months, you're often unreachable too. That's a step-1 (as-is) + step-7 (succession/availability) problem, written up as the smallest step-4 document. No council, no election, no federation — those need three-plus maintainers or a legitimacy problem you don't have. No foundation section — no money, no vendor-neutrality question. That's most of what a "constitution" would contain, and all of it is correctly absent here.

I inferred a few things you didn't state (who holds npm publish rights, whether anyone outside the two of you has merge access). Flagged below where that matters — check before you commit this.

## The document

```markdown
# Governance

## Scope

Samuel Berthe and Nadia <surname> maintain Sandglass. It stays a date-formatting
library; new scope (i18n backends, a CLI, a plugin system) is out unless both agree.

## Roles

- Maintainers: Samuel, Nadia. Merge, release, and decide direction.
- Release keys: both hold npm publish rights and GitHub org admin.
- Contributors: anyone with a merged change.

## Decisions

Routine changes (bug fixes, docs, dependency bumps, new format tokens that don't
break existing ones): one maintainer approves, either may merge. If only one
maintainer is reachable, a pending change may merge after 7 days with no objection.

Anything that changes public API behaviour, scope, or the license: both maintainers
agree, in a public issue, with a 7-day comment window. If one maintainer is on leave
or unreachable, this class is paused, not decided solo — it waits.

Security fixes: either maintainer may act alone — patch, release, publish — without
waiting for the other, and notifies them as soon as they're back.

Disagreement that survives one week: the change is not made, and the issue records why.

## Reduced availability

Both maintainers travel or take extended leave at times. Either may be
unreachable for weeks at a stretch; that's normal, not a governance failure.
During a known absence, the other maintainer keeps the project running under the
rules above: routine work continues, breaking/scope/license changes wait.

If a maintainer is unreachable with no stated return for six months, they move to
emeritus (see below) and we look for a second maintainer.

## Adding a maintainer

Three months of sustained review activity on Sandglass, then both current
maintainers agree. New maintainers get merge rights immediately, npm publish
rights after one release cycle.

## Stepping back

A maintainer who moves to emeritus keeps credit in MAINTAINERS.md; their
credentials are rotated within 30 days. If both step back with no successor, we
archive the repository publicly rather than leave it silently unmaintained.

## Changing this document

Both maintainers agree, in a pull request open at least 7 days.
```

That's the whole thing — about a page. The two sections carrying the actual weight are **Decisions** (the "pause non-routine changes, keep routine ones moving, security is always solo-authorized" split) and **Reduced availability** (which exists specifically because of January).

## What's left out, and why

- **No council/vote thresholds/quorum** — that machinery earns its cost at 3+ maintainers. At two, "both agree" is the whole voting system you need.
- **No elected committee or federation** — no legitimacy problem (nobody's contesting who decides) and no separate sub-communities to federate.
- **No meetings section** — you don't have standing meetings; inventing one to fill the template would be fiction the first time it's skipped.
- **No trademark/neutrality section** — nothing here suggests a company or vendor-control question. If Sandglass is ever adopted by a company that starts dictating direction, revisit.
- **No foundation/fiscal-host section** — no money changing hands. Add this only if you start taking sponsorship.
- **No named parental leave in the text** — I wrote "reduced availability" instead of Nadia's actual situation. A public GOVERNANCE.md is not the place to announce her leave unless she wants that stated; confirm the wording with her before you commit it. Track the real dates privately (shared calendar, not the repo).
- **No published minutes/transparency section** — you have no meetings to keep minutes of. Would matter only under a council or committee.

## Before you commit it

- Verify you *both* actually hold npm publish rights and GitHub org admin today — if only one of you does, fix that before January, since the "either may act alone on security" clause is empty otherwise.
- If anyone besides you two has merge rights, add them to Roles now — the doc above assumes it's only the two of you.
- Put a note in your calendar to revisit this when Nadia's back — six months out from a two-person doc is exactly when it should get re-read, not left to rot.