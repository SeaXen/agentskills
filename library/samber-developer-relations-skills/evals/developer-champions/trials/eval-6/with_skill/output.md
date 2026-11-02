## The actual disagreement isn't "for life vs. expiry" — it's "title vs. active status"

Your co-founder is right about one thing and wrong about another, and the fix is to stop treating "Insider" as a single object.

**He's right:** recognition for work already done shouldn't be revocable by a clock. Taking away a status someone earned, just because they went quiet for two quarters, does read as insulting — and it's not even a fringe opinion. MongoDB Champions and GitHub Stars both run public **alumni rosters** — people who earned the title once keep it, permanently, dated. That's not a soft compromise invented for this conversation; it's how two of the more mature programs in this space already work.

**He's wrong that this means no lifecycle at all.** "For life, no expiry, only removable for genuinely bad behaviour" applied to the *entire membership* — perks included — is how a roster becomes a graveyard. Nobody ever executes a manual removal (nobody wants to be the one who tells a quiet, inoffensive person "you're out"), so the active list just accumulates people who stopped being champions three years ago. At that point the title stops signalling anything, which is the exact failure his own argument is trying to avoid — an inflated, undifferentiated list is *also* an insult to the people still actively earning it.

So split the object in two.

## Two statuses, not one

**1. Insider (the title) — permanent, for life, exactly as he wants it.**
Once someone earns it, it's theirs. Dated ("Insider since 2026"), never silently erased, listed on a public alumni roster if they go inactive. The only way to lose the *title itself* is a conduct violation — and that decision should run through your moderation/CoC process, not be a unilateral call by either of you. This is the part where you should just agree with him outright.

**2. Active Insider (the membership) — term-based, renews on activity, this is what actually has a cost.**
This is the tier that carries perks: roadmap access, private channel with your engineers, early builds, whatever you're putting behind the title. It runs on a fixed term (12 months is the usual default for a vendor program — self-set convention, not a benchmark; CNCF runs ~2-year dated cohorts, HashiCorp rebuilds its roster annually). At the end of a term, renewal is judged against the same published criteria over *that* term only — not reputation, not "well they were great in 2024." No visible activity for a set window (commonly 2 consecutive terms, or 6 months for a faster-moving program) moves someone from Active to alumni. That's not a penalty. It's a lapse, worded that way publicly: "no longer active" reads completely differently from "removed."

This is the actual resolution to your disagreement: **inactivity costs someone their seat at the table, never their name on the wall.**

## Why the perks side can't be "for life" regardless of behaviour

Separate from the insult argument, there's a plain operational one: roadmap access, engineer time, executive briefings, funding — these are recurring costs *you* pay every month someone holds them. A "for life, no expiry" active membership isn't just a recognition question, it's an unbounded, ever-growing standing commitment with no mechanism to right-size it as the program scales. Ten insiders with a monthly roadmap call is fine. A hundred, because nobody ever moved anyone to alumni in six years, is not a program anymore — it's a support obligation with a badge attached. That's the actual reason "no expiry" fails operationally, independent of whether anyone behaved badly.

## The pieces to fix before you publish anything

- **Term length for Active status.** Pick one (12 months is the common default) and put an end date on it day one. Without a dated term, the only exit is manual removal, which — as you've probably already sensed — nobody actually does.
- **Renewal test.** Judge only against the last term, against published criteria. Never "grandfather" someone in on past reputation — that's exactly how the bar quietly erodes.
- **Notice.** Tell people their renewal window is coming, with the activity record you're judging them on, before the decision — never announce a lapse as a surprise.
- **Pause, not lapse.** Parental leave, a job change, illness, burnout — offer an explicit pause so life events don't read as failure to perform.
- **Inactivity clause, worded as a status change, not a punishment.** E.g. "No visible activity for two consecutive terms moves an Insider to alumni status." Public, in the charter, agreed before anyone's actual case tests it.
- **Conduct removal is a separate path entirely**, decided by whoever runs your CoC/moderation process — not the program owner, and definitely not one co-founder's judgment call in the moment. This is the "genuinely bad" exit your co-founder wants, and it should be the *only* thing that can strip the title itself.
- **Alumni is a first-class status, not a demotion page.** Keep the dated title, keep them in a low-frequency channel, give them a real role if you want (nominating new cohorts, reviewing applications) so it doesn't read as a quiet exile.

## What to tell him

He doesn't have to give up "for life" — he just has to agree it applies to the *name*, not the *seat*. Nobody loses recognition for work they already did. People do lose the active perks if they stop showing up, because those perks cost you something every single month, and the only way "genuinely bad behaviour" stays the sole removal criterion for the *title* is if inactivity is handled as a separate, non-judgmental lapse rather than a removal at all.

One thing I don't have yet that would sharpen the specific numbers (term length, inactivity window, what's in the active-only perk tier): rough headcount today, who's actually running this day to day, and whether Kestrelboard Insiders is aimed mostly at individual developers or at engineers inside customer companies — that last one changes how much weight funding/travel perks should carry versus pure access. Happy to turn this into the full charter once you've got those.