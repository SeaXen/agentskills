**Verdict: don't publish it as-is. Your gut is right — the problem isn't roadmaps, it's dated quarters on high-risk, sequentially-dependent work from a 4-person team.**

**What's actually bothering you**

A public roadmap with quarters attached is a promise, not a preview. Enterprise buyers don't read "Q3: managed cloud" as intent — they read it as a commitment they'll hold you to in the RFP, the renewal call, and the next competitive eval. That's fine when you're confident in the date. Here you're not, for three compounding reasons:

- **Storage engine rewrites are the single riskiest category of software project to put a date on.** Migrations, backward compat, data-loss vectors — they slip more often than almost anything else in engineering, and you're proposing to do it first, publicly, as the foundation the next two milestones depend on.
- **The three items are sequential, not parallel, for a team of four.** Storage engine → managed cloud → v3 GA in three quarters means if the first one slips (likely), the other two cascade. You're not risking one broken promise, you're risking three, stacked.
- **Managed cloud is a new business, not a feature.** You're a self-hosted product today. Standing up a hosted offering is ops, security, billing, SLAs — a different muscle than shipping agent features. Dating it alongside a storage rewrite is two unknowns compounding, not one.

**Why the marketing argument doesn't actually hold**

"Enterprise buyers need to see we're serious" is a real concern — but dated public commitments are a weak way to address it, because the payoff is asymmetric. Hit the date, and a sophisticated buyer shrugs, that's what's supposed to happen. Miss it — statistically the likely outcome here — and it's the specific thing procurement remembers and uses against you in the next negotiation. Enterprise security/procurement teams that evaluate self-hosted observability vendors have seen vendors miss roadmap dates before; some now explicitly ask for track record instead of forward promises, because they've learned dated roadmaps are marketing, not engineering. You'd be handing them a liability, not evidence.

There's a second cost marketing isn't pricing in: a public dated roadmap is also a strategy leak to competitors, in a market where you're small enough (60 teams, 4 engineers) that a well-timed competitive move against your announced Q2/Q3 plans could hurt.

**What to do instead**

1. **Ship the roadmap page, drop the quarters.** Now / Next / Later columns, themed not dated. This is the standard pattern for exactly this reason — it signals direction without creating a paper trail of promises. It still answers "do you have a future" without answering "will you hit these exact dates."
2. **Put real dates where they belong: in the sales motion, not the marketing site.** Enterprise buyers who need date confidence get it in a briefing or NDA'd roadmap deck, where sales can caveat, update per-deal, and walk it back privately if reality changes. That's literally lower blast radius and it's the tool built for this job.
3. **If you want one dated public item, pick the lowest-risk one and only one** — not the storage engine rewrite. Something closer to done, that you're genuinely confident won't slip.
4. **Answer "are we serious" with evidence of execution, not promises about the future** — changelog, release cadence, uptime, security posture, case studies from your 60 teams. That's a credibility signal a broken date can't undo later.

Tell marketing: the roadmap page ships, the theme framing gets them what they actually want (buyer confidence), and the specific dates move to sales conversations where the team can control and adjust them — instead of onto a page that turns three of your riskiest engineering bets into public commitments you're both counting on hitting in order.