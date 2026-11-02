# DevRel reporting line — decision memo for Friday's offsite

## Verdict

**DevRel stays under VP Marketing.** Reopen the question the day the funded driver changes — not before.

> DevRel reports to marketing, because the funded driver is developer adoption and VP Marketing owns it. This line starves the product/engineering feedback loop. A named, capped interlock with VP Engineering covers that gap, reviewed at the next major fundraise or when the team crosses ~8 FTE.

That's the shape of the decision the skill this is built on requires — driver, leader, starved pillar, named cover, review date. Anything short of that form is a decision nobody can check later, which is exactly how this fight comes back in six months.

## Why neither VP is currently making a real argument

Neither of them has named a **funded driver** — the actual thing that should decide this. They've each argued from identity instead:

- **VP Engineering:** "DevRel is an engineering function" is a category claim, not a driver claim. No metric, no named gap, six weeks of tenure. That's the single weakest form of argument this decision can be made on — read literally, it would put DevRel under engineering at *any* company, which is obviously false (only 19.9% of teams report to engineering; 33.1% report to marketing — *State of Developer Relations 2024*, DevRel.Agency, 310 respondents). No line holds a majority; placement is a trade-off, never a default.
- **VP Marketing:** "It's working" for two years is a status-quo claim, not evidence either, unless you can point to what "working" means numerically. If she can't name the metric in the room Friday, her argument is exactly as weak as his — she's just had two years' head start on being unchallenged.

Don't let either side win on rhetoric. Ask both, in the room: **what is DevRel funded to produce, and who signs off that it's happening?** That answer decides this, not the org chart preference.

## The fast read, given what's already known

Payments infrastructure, Series A, 60 people — a company at this stage is almost always funded to get developers to *find and trust* the product before the next round, not yet funded to deepen integration quality for an existing large developer base. That points the funded driver at **developer adoption**, which VP Marketing owns. Two things reinforce this:

- Engineering lines are wrong "when the program has to justify itself to a non-technical exec next quarter" — true here by construction: you're the COO settling this for a leadership offsite, and there's a board behind you that will want an adoption number, not a technical-depth number, at the next raise.
- The team is **3 people**. Under the ~10-person line, centralized is the only defensible shape — there's no floor to split, embed, or hub-and-spoke this team. So even if VP Engineering's instinct were partly right, the answer isn't "move the team," it's "add an interlock." Splitting a 3-person team by parent is not a structure, it's two people reporting nowhere.

**Confirm this before Friday, in one hour, not in the meeting:** pull the last quarter of DevRel's actual hours across docs, quickstarts, blog/talks/community (outbound reach) versus sample apps, SDK issue triage, and roadmap-facing feedback (product input). If the time is mostly outbound reach, marketing is confirmed. If it's already mostly product-facing and the real complaint is that feedback isn't reaching engineering, VP Engineering has a real point — but the fix is still the interlock below, not necessarily a reporting-line move at 3 people.

## What actually resolves VP Engineering's complaint

He's very likely not wrong that engineering isn't seeing developer feedback — that's the **named, starved pillar**, and it's the thing to fix explicitly rather than paper over:

`VP Engineering — collaboration during launches, X-as-a-service otherwise — developer feedback and integration pain in, roadmap and release dates out — arbiter: Head of Product or VP Engineering (name one).`

Put a standing bi-weekly slot on the calendar where DevRel brings raw developer/integration feedback to engineering. Cap it — collaboration mode with no end date quietly becomes the operating model and DevRel turns interrupt-driven. If this slot already exists informally and is failing, that's the actual agenda item for Friday, not the reporting line.

## What's still unconfirmed — resolve these, don't guess

- **Coverage.** Advocacy is almost certainly covered by 3 people; community, technical writing, developer education, and DX engineering are unconfirmed. Nationally, DX engineering is staffed on only 27.4% of teams — if nobody owns it at Mosswell, that's very possibly the real thing VP Engineering is reacting to, and it's a coverage gap to name and assign, not a reporting-line argument.
- **Budget split.** "She's had the budget" — headcount budget and program budget are usually different owners (60% of programs exclude salaries from the program budget). Confirm which one she actually holds; it changes what moving the line would even mean operationally.
- **Ladder.** Three people reporting to VP Marketing are almost certainly leveled on the marketing ladder. If any of them is closer to an engineering-facing role (SDK maintenance, sample apps), that's a real promotion-criteria mismatch worth fixing independent of this fight.

## Re-org triggers — name these now so the fight doesn't restart in Q1

- The funded driver shifts from adoption to integration depth/enablement (e.g., post-raise, once the sales motion depends on technical trust more than top-of-funnel reach).
- The interlock above lapses — VP Engineering stops getting the feedback slot, or it silently becomes ad hoc.
- DevRel crosses ~8 people — at that size, split-by-focus (one team in product/engineering, one in marketing, à la Couchbase's documented split) becomes staffable and worth relitigating.
- A second, undeclared group starts doing DevRel-shaped work inside engineering without this interlock.

## What to say Friday

"We're not deciding this on whose department DevRel *feels* like. We're deciding it on who owns the number DevRel is funded to move. Right now that's developer adoption, and that's marketing's. What's real in your complaint," — to VP Engineering — "is that you're not seeing developer feedback. We're fixing that with a standing bi-weekly slot, not by moving three people's reporting line. We revisit this the day the funded driver changes or the team doubles."