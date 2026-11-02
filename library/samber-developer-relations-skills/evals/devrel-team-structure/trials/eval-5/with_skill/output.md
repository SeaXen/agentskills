**Fold docs into DevRel. Structure below. But 3 unstated facts change the shape — confirm before you execute.**

## Assumptions used (no interview run — final answer requested, not a dialogue)

- Combined DevRel (2) + docs team headcount: **under 10 total** — confirm. Everything below breaks if docs team alone is 6+.
- Funded driver for DevRel: **developer adoption/awareness** (you're CMO, own it) — confirm.
- No political block stated on moving docs' headcount budget from Engineering to you. **Check with VP Eng before you announce this** — headcount moves are the #1 way re-orgs get sabotaged quietly.
- API reference: assumed hand-authored or lightly generated, not fully auto-generated from code. If it's pulled straight from OpenAPI/code annotations, ownership question changes to "who owns the annotation pipeline," not "who writes prose."

## Why this fight has run 3 months

Not a reporting-line problem. Two symptoms stacked:

1. **Split-by-focus below its floor.** Skill's own floor for split-by-focus: ~8 people minimum per side to be a viable team. You have DevRel(2) + docs(small) — nowhere close. Splitting enablement content across two under-staffed teams with different managers guarantees boundary fights.
2. **No declared interlock.** Nobody ever wrote down: who owns API reference, who owns tutorials, who arbitrates when it's unclear. Result: the arbiter became you, weekly, by default. That's the actual bug.

Merging fixes #1. It does NOT fix #2 unless you explicitly name owners — see Coverage below. Do both, not just the re-org.

## Candidates considered

- **Embedded, hub-and-spoke** — deleted. Both need floors (hub: 2-3 + 2 spokes; embedded: 1 per host team + craft owner) your headcount doesn't support at this size, no stated multi-product-line need either.
- **Candidate B — no re-org, fix the interlock only.** Keep docs under Engineering, DevRel under you. Name one owner per surface, one arbiter, one review cadence. Cheaper, reversible, preserves docs' proximity to source code. Costs: doesn't remove the two-manager, two-calendar problem long-term; still needs real discipline to hold.
- **Candidate A — centralize (recommended).** Merge docs into DevRel, one manager, reports to you. Matches the skill's own baseline: under ~10 FTE, centralized is the only shape that doesn't spend headcount on coordination you can't afford.

Recommend A because you're already below the split-by-focus floor and the fight is costing you weekly attention. B is the fallback if VP Eng refuses to move headcount.

## The merge (Candidate A)

**Reporting line**

> DevRel + docs report to CMO, because the funded driver is developer adoption and you own it. This starves proximity to Engineering — API reference accuracy depends on catching API changes early, and that signal currently comes from docs sitting inside Engineering. Named engineering interlock (below) covers that gap. Review at +6 months.

**Shape:** Centralized. One team, one manager, one budget. New name suggestion: "Developer Experience," so docs writers aren't relabeled as generic marketing.

**Coverage — name an owner per surface today, not after the merger settles**

| Function | State |
|---|---|
| API reference | Owned — assign to current docs lead (needs code fluency), 1 named backup |
| Tutorials | Owned — assign to a DevRel person (narrative/adoption fit), 1 named backup |
| Advocacy | Owned by DevRel, unchanged |
| Community management | Owned by DevRel, unchanged (confirm someone actually holds this) |
| Developer marketing | Confirm state — often silently unowned at this size |
| Developer-experience engineering | Likely unowned at 120-engineer scale — say so in writing, don't hide it |

This is the fix for the actual fight: API reference and tutorials get one owner *each*, not one team fighting over both.

**Engineering interlock — the piece that actually stops the escalations**

`Engineering — X-as-a-service — API-change notifications + review queue on public-surface PRs — arbiter: new DevExp manager + a named Eng lead, biweekly sync`

Write this down. The current arbiter is you, by accident, every week — that stops the day this line exists.

**Ladder:** Decide now — docs writers move to a DevRel-specific ladder or stay adjacent to marketing's. If nobody decides, they get promoted against criteria that don't fit their work — a retention leak, not a visible failure.

**Budget:** Headcount for both moves to you. Program budget (events, tooling) — confirm it was already yours for DevRel; docs' tooling budget likely needs to fold in too.

## Transition — do in this order

1. **Week 1:** Confirm docs headcount + VP Eng sign-off on the headcount move. Do not announce before this.
2. **Week 1:** Name the two surface owners (API reference, tutorials) + their backups, in writing.
3. **Month 1:** Stand up the Engineering interlock (PR notification + biweekly sync). This is what actually ends the weekly escalations — do it before anything else feels "done."
4. **Month 1:** Decide the ladder. Communicate it to docs writers directly — ambiguity here is what makes a merge feel like a demotion.
5. **Quarter 1:** Re-check capacity against 70% of stated hours (skill baseline, adjustable) — a merge that just relabels two overloaded people fixes nothing.

## Re-org triggers — reopen this if:

- Combined headcount crosses 10 → shape choice reopens, other shapes become affordable.
- API reference or tutorials sit at bus-factor 1 for a quarter.
- The Engineering interlock stays in ad-hoc "collaboration" mode past month 1 instead of settling into the X-as-a-service pattern above.
- A third team starts touching either surface without a declared interlock.

**Next: confirm docs headcount + get VP Eng's yes on the headcount move — do that before naming owners.**