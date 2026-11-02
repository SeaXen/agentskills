No web access granted, so I'll build this from standard CFP conventions — you'll want to check ScaleNorth's actual submission form for exact word limits and adjust the fill lengths below accordingly. Here's the complete deliverable.

---

# Your ScaleNorth submission

## The angle

Don't submit "how we reduced alert fatigue." That's the most oversubscribed abstract shape in SRE conferences right now — every CFP reader has seen twelve versions this cycle. The differentiators you actually have:

1. **The number is unusually good.** 340→51 is an 85% cut. Most "we fixed our alerting" talks report going from bad to less-bad. Yours reads like you actually solved it.
2. **Freight is not SaaS.** Reviewers are exhausted by web-app war stories. A logistics company running physical operations against a pager gives you texture nobody else in the CFP pile has.
3. **You don't need a hot take to be spicy.** The number does the provocation for you. Frame the talk as a **case study, not a manifesto** — "here's what happened when we did this, in our context" rather than "here's how alerting should work, fight me." That's the move that solves your Q&A fear and wins the CFP simultaneously: reviewers pick concrete, receipts-backed stories over opinion pieces, and a story about your own system can't be "grilled" the way a general position can — nobody can tell you your own incident history is wrong.

**Recommended thesis:** alert volume was never a monitoring problem — it was an accountability problem. Every alert without an owner and a runbook is noise wearing a signal's badge. You didn't buy new tooling. You made 289 alerts a week justify their own existence, and most of them couldn't.

Don't claim this generalizes to every org. Scope it hard to your context (freight/logistics, physical+digital ops, your team size). That scoping is your Q&A armor — covered below.

## Title (pick one)

1. **"We Deleted 85% of Our Alerts on Purpose"** — recommended. Audacious number as the hook, no opinion to defend.
2. "Alert Bankruptcy: What Was Left Standing After We Killed 289 Alerts a Week" — "alert bankruptcy" is a known SRE term; signals fluency to reviewers who've done this before.
3. "340 to 51: A Freight Company's Pager Diet" — plainest, safest, still solid if 1 and 2 feel too bold.

## Abstract (fill-in-the-blanks, ~200 words — trim to whatever ScaleNorth's form allows)

> Six months ago, my on-call rotation at Northwind Freight got paged 340 times a week. Most of those pages didn't need a human. Some didn't need to exist.
>
> We didn't buy a better observability platform. We didn't hire more SREs. We declared alert bankruptcy: every existing alert had to justify itself with a named owner and a runbook, or it got deleted. [ONE SPECIFIC EXAMPLE: e.g. "One alert had fired 4,000 times in a year and never once preceded an incident. It fired on a dashboard nobody looked at."] We moved from static thresholds to symptom-based alerting on the things that actually predicted customer impact — [ONE CONCRETE MECHANISM: SLO burn rate / duplicate-alert consolidation / escalation policy rework — whichever was your real lever].
>
> Six weeks later: 51 alerts a week. Same incident detection time. [FILL IN: MTTA/MTTR delta if you have it, even directionally — "nothing we cared about got slower to catch."]
>
> This talk is the specific, sometimes uncomfortable playbook: the audit process, the political fight over whose alert gets cut first, the one alert we deleted and immediately regretted, and the backstop we built so a false negative never becomes a 2am surprise. It's not a universal theory of alerting — it's what worked running physical freight operations against a pager, and what I'd steal if I were starting over.

**Fill in the two bracketed specifics before you submit** — a single real anecdote (the 4,000-fires alert, or whatever your equivalent is) does more for selection odds than any amount of polished framing. Reviewers select stories with texture, not templates.

## One-line summary (if the form asks for it separately)

> We cut pager volume 85% at a freight company by deleting alerts instead of adding tools — here's the audit, the political fight, and the one we regretted killing.

## Speaker bio (~60 words)

> [Your name] is a Staff SRE at Northwind Freight, where [he/she/they] [keep pronoun to what you use] spend more time deleting monitoring than adding it. Over six months, [he/she/they] led an alert audit that cut the team's weekly pager volume from 340 to 51 without slowing incident detection. This is [his/her/their] first conference talk — expect a case study, not a keynote.

That last line ("first conference talk") is doing real work — naming it disarms some of the room's adversarial energy before you've said a word, and reviewers often actively want to give first-timers a slot.

## Private notes-to-organizers field (not public — use it)

Most CFP forms have one. Use it:

> First-time speaker. Would appreciate knowing the Q&A format in advance (open mic vs. moderated/Slido) so I can prepare accordingly. Happy to do a 20-min talk + 5-min Q&A or whatever fits the track.

This is a completely normal ask. Organizers answer it, and knowing the format in advance is most of what will calm you down.

---

## Your 4 hours, budgeted

| Time | Task |
|---|---|
| 45 min | Fill the two bracketed specifics in the abstract above with your real numbers/anecdote |
| 60 min | Rewrite the abstract in your own voice — read it aloud, cut anything that sounds like it came from a template |
| 30 min | Bio + notes-to-organizers field |
| 45 min | Read the whole thing aloud once more, cut 15–20% — CFP readers reward density |
| 60 min | Buffer: send to one colleague who was in the room for the alert cuts, ask "does this sound like what actually happened" |

Submit with a day or two of margin before the 9-day deadline — don't burn the buffer on the deadline itself.

---

## The Q&A defense kit (do this after acceptance, not now)

Your actual fear isn't public speaking — it's being cornered on a position. The scoped, case-study framing above already does most of the defusing. For what's left, memorize three bridges, not twelve answers:

1. **"Fair challenge — in our specific context, [X]. I'd genuinely love to dig into the general case with you after."** Use this for any "but does this generalize" question. It's not a dodge, it's the accurate answer — you scoped the talk this way on purpose.
2. **"I don't have that number in front of me — let's connect after and I'll follow up."** Use for anything with a number you don't know cold. Nobody remembers exact MTTR percentiles under pressure, and saying so is normal, not weak.
3. **"That's outside what today's story covers, but here's the adjacent thing we do know: [X]."** Use when someone tries to drag you into a broader alerting-philosophy debate. You're not there to defend a theory of alerting — you're there to report what happened.

Specific hostile questions worth pre-loading answers for, since you already know your material better than anyone in the room:

- *"Isn't this survivorship bias — the one time a real incident's alert gets deleted, you're exposed."* → Describe whatever backstop/re-add process you built (there almost always is one after an audit like this). If you don't have one, that's worth building before the talk, not just for Q&A — it's a real gap.
- *"What if you just got lucky during a quiet period?"* → Whatever incident/SLO-breach data you have before vs. after, even rough. If you truly have none, say so plainly — "we tracked pages, not yet incident correlation — that's the next thing I'd measure" is an honest, defensible answer.
- *"Did anyone push back when their alert got cut?"* → This one isn't an attack, it's an invitation. Tell the story. It'll be your best moment in the room.

Ask organizers (via the notes field above) whether questions come through Slido/text instead of open mic — many mid-size conferences already do this, and it alone removes most of the "cornered on stage" feeling.

---

## Milking it: after ScaleNorth accepts

1. **Ask for the recording explicitly** when you confirm your slot — don't assume it's automatic, some tracks are opt-in.
2. **Reuse the identical accepted abstract** for other CFPs immediately — don't rewrite per venue. Target: regional DevOpsDays chapters, local SRE/platform-engineering meetups, and observability-vendor community conferences, which all run adjacent circuits to ScaleNorth and skew toward first-time-speaker-friendly, lower-stakes rooms than you might expect from a "grilling" standpoint. Check each one's current CFP window yourself — don't rely on a list from me, conference calendars move fast and I don't have live data on them right now.
3. **Blog post timing:** write it within a week of the *first* delivery, while the talk is fresh and before you've given it four more times and started saying it on autopilot. Structure: same case-study arc as the talk, but with the one thing talks can't do well — the actual before/after numbers and a config/runbook snippet, if you can share one without leaking internal specifics. Link the recording once it's up; cross-post to wherever your Northwind Freight eng blog syndicates, plus the SRE community spaces where a receipts-heavy post (not a hot take) reads as valuable rather than self-promotional.
4. **Second and third deliveries get easier, not just because of practice** — you'll also accumulate real Q&A questions from ScaleNorth to fold into the talk as pre-empted content next time, shrinking your genuine surprise surface with each rerun.