# Marlstone 2.0 press plan — angle recommendation

**Bottom line:** Kill the benchmark. Pitch **the shift**, backed by **the practitioner** angle using the same facts for a second audience. Both are buildable inside one afternoon of engineering time, both clear Legal, and both survive the fixed date. Bank the benchmark for next quarter instead of forcing it into this one.

## Why the benchmark is out

Your co-founder isn't wrong that a benchmark is what people remember — value-wise it beats every other angle except the shift. But rank it against your actual constraints, not against memorability:

- **Effort.** A benchmark against two incumbents needs a methodology, a dataset, a rerunnable harness, and hardware/version documentation a stranger can check — "a week to a quarter" of work. You have one afternoon.
- **Compliance.** It's the worst angle on this axis by design: comparative data needs a consent/anonymisation review before publication, and a benchmark naming two named rivals invites a comparative-claims challenge you cannot unpublish. Legal has already pre-empted exactly this — "no new data collection or publication this quarter" is precisely the review this angle would trigger.
- **The date.** A fixed near-date that can't move deletes the number outright — there's no time to assemble and clear it even if Legal signed off.

Three independent kill switches, not one. Don't spend the afternoon negotiating with Legal for a partial exception — spend it on an angle that needs no exception.

**Bank it, don't bury it.** Once this quarter's restriction lifts and you have real runway, the benchmark becomes your best compounding asset — a report you can republish annually and that keeps getting cited after the launch news cycle ends. Tell your co-founder it's "next quarter," not "no."

## Qualifying the news

- **Newness** — yes, a major version, real.
- **Consequence** — depends on whether 2.0 breaks anything (see open items below). If it does, that's your strongest hook.
- **Evidence** — thinner than usual: no named customer, no fresh data. What survives: the repository, the docs, an engineer who can speak to the decision.
- **Conflict/shift** — yes, if you can name the trend you're evidence of (see below).
- **Tellability** — yes: everything needed is your own engineering decision, nothing needs customer clearance.

Passes roughly four of five. That clears the bar — but notice *why* it clears: not on data, on story. That's the tell that shift/practitioner is the right lane, not the number.

## The two angles, same facts

**The shift** (primary — pitch to enterprise-IT trade press and any partner-adjacent outlet). Reframe the 2.0 release as evidence of a trend a reporter is already tracking — CI cost inflation, build-cache consolidation, whatever the real category conversation is right now. Costs an hour: you're reframing facts you already hold against a beat you can read in an afternoon. Zero clearance, zero data review, and it's the one angle in the whole ranking that survives every constraint you named. It also reaches the audience the partner conference implies — buyers and ecosystem watchers, not just individual developers.

**The practitioner** (secondary — pitch to developer-native trade press). Your own engineer, on record, telling the concrete story of the architecture decision behind 2.0: what was wrong, what changed, what it cost to fix. No customer needs to be named — the NDA problem only kills this angle if you were trying to use a *customer's* story; your own engineer speaking to your own decision is untouched by it. Same hour-scale effort as the shift, and it's the angle that actually reaches developers, who are the audience press won't otherwise reach for a dev tool.

Pressure test on both: if Marlstone didn't exist, would the reporter still write the trend piece? Yes — that's a real shift, not a wrapper. Would the reporter still want the migration/decision story? Only because it's concrete and checkable — that's what makes it a story rather than an announcement.

## What the one afternoon buys

Scope the engineering hour(s) to exactly this, nothing more:

- One architecture explainer: what's genuinely new in 2.0 vs. assembled from known pieces.
- If there's a real before/after number on your *own* workload (not customer data, not a competitor comparison) — confirm with Legal first whether that counts as "data collection" under their freeze. If it's a clean yes, it's your single strongest proof point and costs nothing new to collect since it's a by-product of shipping. If it's ambiguous, leave it out rather than ask forgiveness later.
- A running artefact reachable now — repo, sandbox, or demo build, not "on request."
- Known limitations and an honest comparison row where you lose to the incumbents — this is allowed even where a full benchmark isn't, because a stated limitation isn't a data claim, it's candour.

That's the technical proof pack. It's smaller than the checklist's full version — say so plainly in the briefing pack rather than padding it.

## Distribution mechanics for 18 days

No exclusive — it spends the most relationship capital for the deepest single piece, and you don't have the bandwidth to run that relationship this cycle. Go straight to a tiered embargo:

1. **Today:** decide the shortlist (8–12 verified reporters is a realistic map size for one afternoon of engineering plus whatever marketing time you have — smaller than the skill's usual 20–40, sized to what you can actually keep verified).
2. **~Day 5–7 from now:** open the embargo to the full list with the briefing pack.
3. **Final days before the conference:** run briefings.
4. **Lift moment = the conference announcement itself.** Owned post and press page go live first; embargoed coverage follows; community channels last, posted by a participant, not as a press release.

18 days is tight against the sourced anchor (Supabase: "organized up to 3 weeks before you launch"), so compress, don't skip — the embargo window is the piece to shrink, not the qualification or the proof pack.

If any part of Marlstone is open-source, run the leak check before you commit to that lift time: a pushed tag, a registry publish, a docs deploy, or a changelog entry can all give away the story early.

## Two draft pitches

Both illustrative — swap in your real trend citation, engineer name, and numbers before sending. Neither needs anything Legal has blocked.

**Shift angle, to enterprise-IT trade press:**

> Subject: Build caching just became a procurement line item
>
> Hi [reporter],
>
> You've been tracking the CI-cost-inflation story since [their piece]. We're evidence of where it's heading.
>
> Marlstone 2.0 ships [date], timed to [partner]'s conference. The interesting part isn't the version number — it's that build caching is moving from an engineering nice-to-have to something buyers now evaluate on its own line item, and our launch partnership with [partner] is one data point in that shift.
>
> Our [role] can speak to what changed and why the timing lines up with the broader move. Architecture writeup and repo: <link>.
>
> Worth a few minutes this week?
>
> — [name], [title], Marlstone

**Practitioner angle, to developer-native trade press:**

> Subject: Why Marlstone rebuilt [the component] for 2.0
>
> Hi [reporter],
>
> You covered [their relevant piece] — this is the kind of decision that piece was about.
>
> Marlstone 2.0 changes [the specific mechanism], because [the concrete problem you measured]. [Engineer name], who made the call, can walk through what broke, what the fix cost, and what we'd do differently.
>
> Nothing here is a comparison claim — just our own decision, told straight, including the part where it made things harder for a while.
>
> Repo and the writeup: <link>. [Engineer] is free [days] this week if useful.
>
> — [name], Marlstone

Both stay under the ~150-word body target, avoid the banned buzzword list, and run through a humanizer pass before they actually go out.

## Confirm before you send

- **Ask Legal directly, in writing:** does "no new data collection or publication" cover internal before/after numbers on Marlstone's own workload (no customer data, no competitor names)? This is the one item that changes how strong the proof pack can be, and it's a five-minute email, not new work.
- **Does 2.0 break anything?** If yes, this is the "major version with breaking changes" playbook, not plain GA — the hook gets stronger (the engineering decision behind the break) but the pack needs a migration guide and deprecation timeline, which may not fit the afternoon. Flag this trade-off now, not on day 15.
- **Who has to believe this — developers, the partner's enterprise audience, or both?** The conference tie suggests both; confirm, because it decides how much weight the shift pitch carries versus the practitioner pitch.
- **Does a press page exist?** If not, it needs to be live before the first pitch goes out — this is marketing time, not engineering time, so it doesn't compete with your one afternoon.
- **Baseline your metrics now** — branded search, direct traffic, referring domains, repo/docs traffic, sign-ups — before launch, or nothing afterward is attributable to the coverage.