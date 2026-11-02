**Do this first (20 min):** add the sponsorship statement below to your README. It's the single fastest fix for the "you owe me" DMs — it ends the ambiguity that lets people frame sponsorship as a support contract.

## What's actually going on

Mapped against the practice's own failure signals, not vibes:

- **Issues outgrew contributors** (14→180 vs. you+1). That's the named cue to *pause posting and fix an artifact* — not to post more, not to feel guilty about capacity.
- **Stars outgrew everything that matters** (900→6.8k). Stars are the signal to ignore; they don't track adoption, contribution, or funding.
- **Publishing income without a boundary statement invites entitlement** — this is a documented grey zone for solo maintainers, not a personal failing. The fix isn't stopping disclosure, it's pairing it with a written statement of what the money does and doesn't buy.
- **DMs full of feature requests** is a routing problem: every private answer is a one-time cost with zero reuse. Public routing makes each answer reusable.

None of this means stop posting. It means the weekly cadence and the unscoped revenue disclosure are now costing more than they buy. Below is the fix, then the standing charter.

## Assumptions I made (correct any of these and I'll adjust)

- Solo maintainer, no co-founder/investor consent chain — you said "basically me."
- Audience is both individual Rust/infra developers *and* platform teams inside companies (service mesh is infra — even a solo picker usually reports to a team).
- No deadline — this is an ongoing archive, not a launch push.
- Real monthly capacity unknown — you said "not sustainable," which I've read as *currently negative*. The cadence line below needs your real number once you have it.

## Ship today

1. **Post the sponsorship statement** (below) to README/SPONSORS — 20 min.
2. **Reply to both entitlement DMs** with the boundary reply (below) — 10 min.
3. **Add a scope + response-time line to README, plus a feature-request issue template.** Stop answering feature requests in DMs starting now — 30 min.
4. **Label 5–10 open issues "good first issue."** Direct lever on the goal you actually want (contributors), not more readers — 20 min.
5. **Confirm your real hours/month in a bad month.** The cadence line in the charter below is a placeholder until you give me this.

### Sponsorship statement (README/SPONSORS)

> Sponsorship currently runs about €310/month. It funds continued maintenance of mesh-router in general — it does not buy priority on a specific issue, a support SLA, or influence over the roadmap beyond a public vote like anyone else's. [Sponsor perk if any, e.g. name in SPONSORS.md — fill in your real one.] If you need contracted support or guaranteed fix times, that's a different arrangement than sponsorship, and I don't currently offer one.

### Boundary reply (for the two "you owe me" DMs)

> Sponsorship funds my time on mesh-router in general — it isn't a support contract tied to any one issue, and I don't take feature requests to order. [link to the statement above] covers what it does and doesn't buy. Happy to look at your issue in the public queue like everyone else's: [link].

### Standard DM redirect (for the rest)

> This is a good fit for a public issue so others hitting the same thing can find it and vote: [link]. I don't work from DMs — it's also the fastest way to get it actually looked at. Scope and response-time target: [README link].

## The charter

```markdown
# Build-in-public charter - mesh-router

Goal          Contributors first (the project needs to survive past one
              person). Sustainable sponsorship second. Explicitly not
              adoption-at-any-cost — stars already outran everything
              else and that's the current problem, not a target.

Context       Solo maintainer. No co-founder, investor, or customer
              consent chain. Only claim on the numbers is your own.

Audience      Individual Rust/infra developers choosing a service-mesh
              sidecar, plus platform teams evaluating it for company
              use. Both need release-cadence and response-time
              evidence; only the individual track needs personal
              narrative and failure posts.

Rung          Rungs 1-3 (shipping log, decisions, failures) stays the
              backbone — this is what converts readers into
              contributors, keep it. Add rung 4 monthly: contributor
              count, first-response time, open-vs-closed issue trend.
              Rung 5 narrows: sponsorship total (€/month) stays public
              but moves out of weekly posts into the monthly rung-4
              update, always paired with the "what this buys"
              statement. No runway, no per-sponsor breakdown, ever.

Stop          Revenue line stops the day a second maintainer or paid
condition     contributor gets a claim on it — the number stops being
              a personal milestone at that point, same reason Damon
              Chen gives for his own stop. Also stops if a sponsor
              asks not to be identifiable through the aggregate.
              When it stops: one post, plain reason, changelog/
              roadmap/quarterly report stay up, past numbers stay
              archived and undeleted.

Boundaries    Hard block, no exception: nothing about an unpatched
              mesh-router vulnerability — no commit message, no
              "chasing a weird bug" post — until a fixed release
              exists. A sidecar sits in the request path; this rule
              outranks every other rule here.
              Hard block: no named user's traffic, config, or
              deployment details without written consent.
              Decided: sponsorship stays public, paired with the
              statement above, every time.
              Decided: no dated roadmap — direction and sequencing
              only ("service discovery integration is next," never
              "ships March").
              Pre-publish check on every post and fast reply: (1)
              unpatched vuln, directly or by hint? (2) someone else's
              data/name without consent? (3) commits to a date/number
              you don't control? (4) fine if a hostile commenter
              quotes this sentence alone? Any yes: rewrite or delay.

Cadence       Release spine — one post per release, no release no
              post — plus one monthly rung-4/5 roundup. [Placeholder:
              lock the per-post time budget once you confirm real
              hours/month; target under a tenth of your maintenance
              time.]

Surfaces      Anchor: CHANGELOG / release notes in the repo. Amplify
              only on whatever channel your existing weekly posts
              already run on — confirm which, and cut any channel you
              don't personally read. Feature requests move to GitHub
              Discussions / issue template, never DMs.

Support plan  README states: solo, part-time maintenance, response-
              time target, in-scope vs out-of-scope. Every feature
              request routed to the public tracker. Both entitlement
              DMs get the same boundary reply, not individual
              apologies.

Measurement   Quarterly: contributor count (first-time and repeat),
              first-response time on issues, sponsor count. Stars and
              raw issue count are the explicit signal to ignore —
              6.8k stars and 180 issues already proved they don't
              track what you need.

Pause rule    If the release-spine cadence is missed twice running, or
              issue volume grows two months straight while contributor
              count doesn't, drop to the monthly roundup only and say
              so in one line at the top of the next post: "Slowing to
              monthly — clearing the backlog first." No fade-out.
```

**Next:** send me your real hours/month in a bad month, and I'll lock the Cadence line.