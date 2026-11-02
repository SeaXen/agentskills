**Verdict: the policy does not hold up.** As drafted, it costs about 6–16 hours a month against your 3. The fix is two changes: build `current` from main, and narrow the backport rule for 4.x and 3.x. Both are below.

Next action: confirm the `ASSUMED` items, especially the 4.x and 3.x support end dates. Then I'll write this up as the policy doc.

## Assumptions (not answered, so I marked them)

- `ASSUMED` 4.x and 3.x support end dates. Treated as "until next major".
- `ASSUMED` 20 min per copy or backport, including review and rebuild (baseline).
- `ASSUMED` 10–20% of fixes qualify for older lines under the narrow rule (baseline).
- `ASSUMED` 25–50% of released-behaviour fixes also apply to 4.x and 3.x under your wide rule.
- `ASSUMED` the one-off migration ceiling is about half a day.
- `ASSUMED` 4.x and 3.x instructions differ from 5.x, so the guides need a selector.
- Unvalidated sections: topology and source layout. You haven't agreed to them yet.

## Why the draft fails

Your numbers: 30 fixes a month, 80% touching released behaviour, so 24 per month. Ceiling: 180 min.

| Term | Math | Hours/month |
| --- | --- | --- |
| Keep 5.x `current` in step (release branch, so every fix is copied from main) | 24 × 20 min | 8 |
| Backport to 4.x and 3.x (wide rule) | 24 × 25–50% × 2 versions × 20 min | 4–8 |
| **Total, mid case** | | **about 12–16** |
| Best case (10 min per copy, 25% overlap) | | about 6 |

Even the best case is 2× over. The cost drivers:

- `current` builds from a release branch while main carries `next`. Every released-behaviour fix is therefore written twice.
- "Applies to a supported version" has no limit. Three supported lines make each fix up to three copies.
- An unpriced rule decays into "backport nothing" within two releases. Readers on 4.x and 3.x would then get silently stale pages.

## Fix 1: build `current` from main

- Main carries 5.3, which is all additive. That is the exact case where a separate `next` site is not worth its cost.
- Build 5.x `current` from main. Mark unreleased content inline: "coming in 5.3".
- Keeping `current` in step then costs 0.
- Tradeoff: the `next` site goes away. Readers see 5.3 features only as inline marks.
- One-off: reconcile docs-only commits on the 5.x release branch into main, then repoint the build. About half a day (`ASSUMED`).
- Reprice when main starts 6.0. At that point, branch `current` from the 5.x release tag.

## Fix 2: narrow the backport rule

The rule combines Django's (latest stable only) and GitLab's (older lines only for exceptions).

- Fixes for released behaviour land on main, which is 5.x `current`. They land once.
- Fixes for 5.3-only features stay on main, marked "coming in 5.3".
- Backport to 4.x or 3.x **only** for security, legal exposure, data loss, or a step that blocks upgrading.
- Never fix frozen or archived versions.
- Tag backport targets in the PR at review time, not after merge.

**New cost:** 30 × 10–20% × 2 versions × 20 min = 2–4 h/month, mid case 3 h.

That fits only at the low end. Use this as the trigger: if two months in a row exceed 3 h, freeze 3.x early. Freezing means a static snapshot, an "unsupported" banner, and no more fixes. Measure for one month, then replace the baselines with real numbers.

## Docs version policy table

| Version | Product status | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- |
| main (5.3) | unreleased, additive | no own site; "coming in 5.3" marks inside `current` | at 5.3 release, marks become "added in 5.3" | n/a |
| 5.x | current, built from main | `current` | `maintained` when 6.0 ships | every released-behaviour fix, via main |
| 4.x | supported | `maintained` | `frozen` at support end | security, legal, data loss, upgrade blockers |
| 3.x | supported | `maintained` | `frozen` at support end (`ASSUMED` earliest) | same as 4.x |

## Topology and layout (unvalidated)

- **Keep the selector.** Three live lines with differing instructions, plus readers pinned to old lines, make it the right rung for now.
- **Rejected:** latest-only with stamps. It leaves 4.x and 3.x readers with no page of their own.
- **Rejected:** per-major frozen sites for 4.x and 3.x. They are supported, so that would cost the selector's backports plus a second deploy.
- **Re-check at the 3.x support end.** Then move 3.x to a frozen snapshot.
- **Layout:** one branch per version, built once. `current` builds from main. 4.x and 3.x build from their release branches.
- Release cut, as a checklist line: `current` becomes `maintained`, the `latest` alias moves, the switcher updates, banners swap.

## PR template

Paste this into `.github/pull_request_template.md`.

```markdown
## What changed and why

<!-- One or two sentences. -->

## Which text is wrong, and where?

Tick every docs line where the old text is wrong.

- [ ] 5.3 only: describes unreleased behaviour. Marked "coming in 5.3". Stays on main.
- [ ] 5.x current: describes released behaviour. Lands once, via main.
- [ ] 4.x (supported)
- [ ] 3.x (supported)

## Backport (required if 4.x or 3.x is ticked)

Pick exactly one. If none applies, untick 4.x and 3.x.

- [ ] Security
- [ ] Legal exposure
- [ ] Data loss
- [ ] Blocks upgrading to a newer version
- [ ] None. Main only.

Backport PRs: <!-- #number per target branch, or "to be opened after approval" -->

## Checks

- [ ] Version stamps updated ("added in", "changed in", "removed in") if behaviour differs between lines.
- [ ] Unreleased content carries a "coming in 5.3" mark.
- [ ] Tutorials, concepts, changelog, and blog pages stay single. No per-version copy.
- [ ] No change targets a frozen or archived version.

## Reviewer

- [ ] Backport targets confirmed at review, before merge.
```

## KPIs

| KPI | Target |
| --- | --- |
| Backport hours per month | at or under 3 h, remeasured after month 1 |
| Share of PRs with a backport class | 100% of PRs that tick 4.x or 3.x |
| Switcher 404s | 0 |
| Sessions landing on a non-current version | falling each quarter |
| Full build time and versions built per deploy | no growth at each release cut |

## Sources

- Django: backport to the latest stable branch only.
- GitLab: older releases only rarely, for legal, security, data-loss, or upgrade-blocking content.
- PostgreSQL: no effort on de-supported versions.
- The minutes per copy and the 10–20% qualifying share are baselines, not sourced figures.

Next: reply with the 4.x and 3.x support end dates. If 3.x ends within about two releases, I'll compare freezing it now against keeping the selector. That could cut the standing cost to about 1.5 h.