# Assessment: Corvex User Groups (Milan, Krakow, Manchester, Austin)

## Short answer

No — not as designed. The instinct to start company-staffed is correct given your constraints. But the plan as described (staff-run evenings, two internal talks plus roadmap, volunteers who only book rooms, all under a "User Group" brand) reproduces the exact failure pattern this skill documents as a named anti-pattern, almost line for line:

> "A vendor's DevRel team launches 'the \<Product> User Group' in four cities. Each evening is two talks by company engineers plus a roadmap update. Local 'organizers' are volunteers recruited to book rooms, with no say in the program. Attendance is strong for three editions, then halves; the volunteers stop replying."

Three failures named there apply directly to your plan today:

1. **The room is told "user group" (independent) but given a company-staffed series.** Naming it "Corvex User Groups" claims a model you're not running.
2. **The local recruits get organizer workload with helper authority.** Booking rooms and being called "organizers" is exactly the mismatch called out.
3. **No edition has a speaker with no stake in Corvex.** Two Corvex talks plus a roadmap update is 100% company content — the skill treats a non-host speaker slot as a structural requirement, not a nice-to-have, "or accept that attendance decays to customers only."

That third one is the mechanism behind the failure pattern's timeline: attendance holds while the roadmap is still new information, then decays once it isn't. With four simultaneous evening series and only two of you flying out, you'll hit that wall in all four cities around the same time.

## What's actually right about your plan

- **Starting staffed given a fixed date and zero volunteers is the sanctioned move**, not a shortcut you should feel bad about: "Promote it when the date is fixed and no local organizer exists yet, then convert to a chapter later." Six weeks out with no local network is precisely that case.
- **The sanctioned path from here is staffed → vendor-backed chapter**, not staffed → independent in one jump: "a staffed series can hand over to volunteers, but a chapter cannot be un-handed." Handoff is designed-in from day one or it doesn't happen organically.

## The strategic fork you haven't resolved yet

"Independent community groups" and "vendor-backed volunteer chapter" are not two points on the same ladder — they're different destinations with different endings for you:

| | Vendor-backed chapter | Independent |
|---|---|---|
| Brand | Stays "Corvex User Group" | Drops your name — becomes e.g. "Milan Observability Meetup" |
| Program control | Yours, within guidelines you set | Fully the local organizers' — no Corvex veto |
| Corvex on stage | Regular, favored slot | One speaker among competitors, no guarantee |

Pick one now, out loud, because it changes what you're willing to hand over later. If the real goal is "resilient, locally-run, still ours," target the chapter model — that's a smaller, more achievable jump from where you are, and it still solves your actual problem (staff can't sustain four cities forever). If you genuinely mean fully neutral communities where Corvex becomes just another vendor in the room, say that in the charter now, because it means the branding and speaker-neutrality policy you set at edition 1 will need to unwind later — cheaper to build it right than to renegotiate it with a room that already exists.

My recommendation: **target the vendor-backed chapter**, not full independence, unless you have a specific reason to want your name off it eventually. It matches your stated goal ("graduate... into independent... groups" reads as "runs itself," which the chapter model delivers) without asking you to give up brand and program control you're currently funding.

## Fixes before you lock this in, in priority order

**1. Rename what the local recruits are, and give them a real (small) job now.**
They're not organizers yet — on the ladder (attendee → regular → lightning speaker → volunteer → co-organizer), venue-booking is a volunteer-level contribution. Call them local hosts or volunteers. Give them one piece of real program input immediately — e.g., choosing between two candidate non-Corvex speakers, or owning the door count and local promotion — so they're being onboarded onto the ladder, not left on a rung with the wrong label. Promote formally to co-organizer once they're actually doing organizer work.

**2. Get one non-Corvex voice into every city, starting as early as possible — not eventually.**
With six weeks and zero local community, a full external speaker per city may not be reachable for edition 1. If it isn't, say so plainly in the charter ("edition 1 is fully staffed by design; a non-Corvex slot is required by edition 2") rather than let it quietly become permanent. Fastest paths given your timeline, ranked by the skill's own sourcing yield:
- Regional conference speakers — someone who's already given a related talk can repeat it locally with no new prep.
- A current customer's engineer talking about their own production setup, not your product.
- Local companies solving observability problems, invited to talk about their problem, not your SDK.

**3. Cap your own roadmap segment like a sponsor slot.**
CNCF's ceiling for any non-content pitch is ≤15 minutes (sourced). Treat the roadmap update the same way even though you're the host — it's the single most repeatable reason a room stops coming back once the novelty wears off.

**4. Don't commit to monthly, in four cities, staffed by two people, indefinitely.**
That's a standing job with no slack — one of you gets sick or changes roles and two cities go dark simultaneously. Cadence needs to survive a tired month (interview Q7), not just the launch. Consider bi-monthly per city until a local co-organizer is actually running part of the evening, then increase. CNCF's inactivity line is >90 days between events (sourced) — that's your outer bound, not your target.

**5. Design the staffed → chapter handoff now, not as a reaction to burnout.**
Concretely: name, per city, what authority moves to the local volunteer-turned-co-organizer and on what trigger (e.g., "after edition 3, if repeat attendance ≥40% and a second local person has stepped up, hand them the speaker pipeline"). Shared listing/mailing-list/socials access from day one, so no single Corvex departure locks an account.

## What I'd still need from you to finish the charter

I can't fill these from what you've given me — they gate format and cadence specifics per the skill's interview:

- Who's in the room per city — seniority, and do they attend on work time or their own time? (Changes whether this reads as B2D adoption content or needs an ecosystem angle.)
- Do you have a named non-Corvex candidate speaker, even provisional, for any of the four cities today?
- What's the actual standing hours ceiling for your two engineers on a tired month, once travel is factored in across four cities?

## Draft charter shape (fill the blanks per city)

```
# <City> Corvex Observability Meetup   [not "Corvex User Group" until program control actually transfers]

Room: <TBD - seniority, work-time vs own-time>
Host model: company-staffed series (Corvex), explicit intent to convert to vendor-backed volunteer chapter
Purpose: adoption + local advocate pipeline for observability SDK (name the one outcome that wins if they conflict)
Format: anchor (Corvex talk, 25 min) + lightning slots; roadmap segment capped at 15 min like a sponsor slot
Rhythm: <bi-monthly recommended>, fixed weekday/time per city
Program decisions: Corvex staff for edition 1-2; local host gets a real vote from edition 1 on speaker/venue choice
Organizers: <2 Corvex staff>, <local host - name, not yet co-organizer>
We don't: let roadmap exceed 15 min, run an edition with zero non-Corvex content beyond edition 1, call volunteers organizers before they hold real program input
Handoff trigger: <named condition per city, e.g. "2nd local co-organizer identified + repeat attendance ≥40%">
```

Track per city against the pass threshold this skill sets: two organizers from two employers, a non-host speaker every edition from edition 2 on, and no gap over 90 days. As designed today, your plan fails the organizer-spread line by construction (both "organizers" are Corvex) — that's the one to fix first, since it's also the one that determines whether "graduate to independent" is even reachable later.