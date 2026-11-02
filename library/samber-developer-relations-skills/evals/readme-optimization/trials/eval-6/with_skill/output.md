## Diagnosis

The current README isn't hiding the license — it's *sequencing* it wrong. `## License - AGPL-3.0, see LICENSE` at the very bottom passes the minimum bar (named, linked to the file) but fails the sharper part of that same check: **a non-permissive license buried at the bottom is the fastest possible disqualifier for a reader deciding whether to deploy something, so it belongs near the top, not the end.** Right now the page makes a reader read the whole thing, install it, and run it before they hit the one fact that could have changed their decision.

AGPL makes this worse than a normal copyleft license would. Most developers pattern-match "AGPL-3.0" against MIT/Apache — a familiar-looking OSS badge — and don't know it carries a network-use clause (source-disclosure trigger for running it as a service) until someone in security or legal asks about it later. That's the actual mechanism behind "issue opens three weeks in, after deployment": nothing on the page told them there was a question to ask *before* they deployed. A commercial exception that requires emailing you compounds it — it's not just "what license," it's "does my use case need to email someone," and that's currently undiscoverable without reading a single line at the very bottom of a long page.

64% of respondents to GitHub's 2017 Open Source Survey rated the license as very important to their adoption decision — the highest-rated documentation element in that survey. Treat it accordingly: as a top-of-funnel decision input, not a footer formality.

## Recommended structure

This is a self-hosted service, so the section order should follow that shape — but with licensing pulled forward, out of its default last-place slot, because it's the disqualifying fact here:

1. Name, one-line description
2. What it does, who it's for
3. **Licensing — read before you deploy** *(moved up from the bottom)*
4. Why this over [the alternative/hosted option]
5. Try it — one-command run
6. Requirements
7. Install and first-run config
8. Architecture (short paragraph)
9. Security and data-handling posture
10. Status, release cadence, upgrade notes
11. Support channels, contributing pointer, full license reference

Keep it short — five sentences, plain English, then link out. Don't turn it into a legal essay; that's overflow, and overflow gets a link, not inline text.

## Drafted copy for the new section

```markdown
## Licensing — read before you deploy

Gridwarden is [AGPL-3.0](./LICENSE). If you run it as a network service — the normal
way to run a metrics store — the AGPL requires you to make the complete source of
your running version available to anyone who uses that service, including any
modifications you've made.

If that doesn't work for you (embedding Gridwarden in a product you distribute,
running it inside a company that can't offer source access to users, or reselling
it as part of a hosted offering), we sell a commercial license that removes that
requirement. Email <licensing@fenwick-analytics.example> before you deploy, not
after — we'd rather have that conversation once than field a support ticket about
it post-launch.
```

Then trim the existing bottom section to a one-line pointer, since the substance now lives up top and the bottom slot exists mainly for the customary place tooling expects it:

```markdown
## License

AGPL-3.0. See [Licensing](#licensing--read-before-you-deploy) above, and the full text in [LICENSE](./LICENSE).
```

## Why this fixes the specific pattern you described

- It converts a fact the reader currently discovers *empirically* (three weeks in, via their own legal/security review) into a fact they read in the first screen, at the exact moment they're deciding whether to spin it up.
- It answers the actual question people file issues about — "do I need to talk to you?" — as a yes/no branch, instead of making them infer it from a bare SPDX identifier.
- It doesn't remove the license badge if you keep one (a badge is fine as an assessment signal — it confirms the SPDX id at a glance) but a badge alone can't carry a conditional business rule like "email us if X." That needs prose; keep both.

One caveat worth setting expectations on: this reduces the pattern, it doesn't eliminate it. Some readers doing a quick spike still won't loop in legal until later regardless of what the README says up top — the fix makes the fact discoverable at evaluation time, it can't force someone to read it. Track the "licensing question" issue count for 4–6 weeks after shipping this; that's the metric this kind of fix should move, and it's cheap to watch (just count that issue category per month — don't expect it at week one, a short window reads as noise).

I don't have read access to the actual repository, so I can't run the mechanical audit or verify the rest of the page against source (install steps, other claims) — this is structural/positioning guidance based on the facts you gave. If you want the full scorecard on the rest of the README, point me at the repo.