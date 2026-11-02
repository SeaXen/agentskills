Numbers first, because they drive the fix: 310 EUR/month is about one evening of a mid-rate freelance dev's time. It buys goodwill, not a support contract, not a queue position, not a claim on your time. Anyone treating it as the latter is wrong on the math, not just on etiquette — say so plainly rather than half-apologizing.

**Kill the entitlement at the source, not per-DM**

Add a short, unambiguous line to the Sponsors page and README, once, publicly:

> Sponsorship funds maintenance in general. It does not buy priority support, guaranteed fixes, or SLAs. This project ships under [MIT/Apache-2.0], "as is," same as every other dependency you don't pay for. If you need guaranteed turnaround, that's a separate paid support arrangement — ask.

That sentence does the work so you never have to write it again per-person. If you keep publishing income, publish this next to it — the number without the disclaimer is what invites the "I paid, so..." framing.

**Reply once to the two people, then stop engaging on it**

> Thanks for sponsoring — it genuinely helps keep the project alive. It's not a support contract though, so I can't commit to fixing anything on a timeline. Happy to look at your issue in normal triage order, or if you need it fixed faster, I can quote paid work separately.

Don't argue the point twice. If they push back after this, that's information about them, not a problem you need to solve.

**Separate "sponsor" from "paid support" as two different products**

Right now one tier (GitHub Sponsors) is absorbing two different asks: goodwill funding and guaranteed fixes. Split them:

- Sponsors tier — funding, thanks, badge, nothing owed.
- A real paid-support tier or standalone consulting offer, priced like actual hourly work, for anyone who wants a real SLA.

This isn't a growth tactic, it's a release valve — it gives the two entitled sponsors a legitimate path that doesn't run through your free time.

**Stop triaging 180 issues by hand — change the intake, not your effort**

- Issue template requiring repro + version. No repro after 14 days → auto-close, one canned comment, no debate.
- Labels: `needs-repro`, `confirmed`, `help-wanted`, `wontfix`. Bulk-triage in one sitting weekly, not continuously.
- DMs for feature requests get one canned reply: "Please open a GitHub Discussion — I don't track requests from DMs." Repeat this without exception; the inconsistency (sometimes answering DMs, sometimes not) is what trains people to keep DMing.
- Freeze new feature intake explicitly for a stated period: a pinned issue titled "Stability focus through [date] — feature requests welcome in Discussions, won't be scheduled before then." Public, dated, so it's a policy, not a mood.

**Recruit triage help, not code contributors**

You don't have a Rust-contributor problem, you have a labeling-and-first-response problem — a much lower bar. Ask openly (in your next weekly post) for one or two people to do issue triage only: reproduce, label, close stale, answer FAQs. That role attracts differently than "come write service-mesh internals," and it's the single highest-leverage hire-for-free available to you right now.

**Give yourself a written SLA — it's for you as much as for them**

One sentence, pinned: "Nights-and-weekends project, one maintainer. Expect a first response within two weeks, not less." Once it's written down, a slow response stops being a personal failure and starts being the documented, expected behavior of the project. This is the actual root fix — you don't have a communication problem with two sponsors, you have an absence of a stated boundary that anyone could reasonably bump into.

**Keep posting, change what you post**

Don't stop the weekly cadence — that's your growth engine and it's working. Alternate feature posts with "state of the project" posts: this triage policy, the stability freeze, the call for a triage co-maintainer. Transparency about the bottleneck reads as credible, not weak, and it's the post most likely to produce the co-maintainer you actually need.