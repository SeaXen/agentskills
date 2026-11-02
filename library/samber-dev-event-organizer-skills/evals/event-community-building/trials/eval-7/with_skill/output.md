# FjordSec off-season plan: voice guide and quarterly meetup

I followed `event-community-building`. Two parts of your request run into its rules, so here is what I did with each.

- **Voice guide.** I wrote it as a between-editions *expression* of FjordSec's existing register, not as a second voice. The skill says "never invent a quieter off-season voice": identity is fixed and only its expression changes. A cosier tone is fine, but a separate personality for the Discord would drift away from the stage.
- **Quarterly meetup.** I did not design the format. A touchpoint that needs a venue, a schedule and a speaker is an event property. That call belongs to `event-portfolio-strategy`, where a quarterly meetup feeding the flagship is its low-cadence, small-format rung. Section 6 gives you the inward-facing brief to take there.

**Not yet confirmed.** I couldn't ask the interview questions, so the plan rests on these assumptions. Correct any that are wrong and I'll re-rank:

- Q1: annual event.
- Q2: a Discord already exists.
- Q4: your register is *sober, precise, formal*, which is how you described the stage. This is provisional until `event-cultural-identity` confirms it.
- Q5: one city (Oslo), with no independently run local groups.
- Q8: unknown. This is the question that decides the cadence.

Nothing member-visible should change until you approve each section below.

---

## 1. Cadence posture and owner

**Recommendation: occasional pulse, on the condition that one named person holds recurring hours in the quiet months (Q8). If nobody does, choose dormant-but-open.**

This assumes a volunteer team recovering from an edition. A vendor-run team with someone on payroll for the quiet season could go further.

| Rung | Verdict |
|---|---|
| Dormant-but-open | Fallback. Needs a dated notice (template below). |
| **Occasional pulse** | **Pick, if an owner exists.** One digest or spotlight on a rhythm the owner can hold all gap. |
| Continuous light | Rejected. Someone would need something to say every cycle with no edition to talk about. |
| Continuous heavy | Rejected. It needs a funded moderator roster, and it becomes a standing meetup series. |
| Close and reopen each year | Rejected. It throws away the member list and the archive. |

Pulse plan, filled from material that already exists:

| Slot | Artifact | Owner |
|---|---|---|
| Post-edition | Talks archived and linked, thank-you | {Name} |
| Mid-gap 1 | Digest: what members shipped or wrote | {Name} |
| Mid-gap 2 | Spotlight: one member, one thing they made | {Name} |
| Build-up opens | Handback of the live member list to next edition's channels | {Name} + channel designer |

Dormancy notice, if you fall back to it:

> **This space is quiet until {build-up month}.**
> The archive stays open and searchable.
> Nobody moderates day to day. {Name} owns the space and reads reports at {route}.
> You will hear from us here when FjordSec {year} opens.
> Posted {date}.

## 2. Off-season voice guide for mods

This is the deliverable you asked for. It is a delta against the stage register, so it stays auditable.

### What stays fixed

Mods are the same people the stage audience trusted. Three things carry over unchanged:

- **Sober about substance.** We never make security stakes a punchline.
- **Precise about claims.** Casual tone never makes a technical statement looser.
- **Signed by a person.** Mods write as themselves, not as "the FjordSec team".

### What changes

| Register attribute (provisional) | Stage expression | Off-season expression |
|---|---|---|
| Sober | No humor, no memes | Warm and light between people. Humor aims at ourselves, our tools and our own mistakes. |
| Precise | Exact, cited | Same exactness in the claim, relaxed wording around it. If unverified, say "not verified" in plain words. |
| Formal | Full sentences, titles | First names, contractions, short sentences, a few emoji as punctuation. |

### Rules for banter

1. **Punch at ideas and tools.** Never at a person, a vendor, a victim or a newcomer's question.
2. **No jokes on a live incident or breach.** No jokes about a named organization's compromise or about people affected.
3. **No vulnerability details or exploit code in banter threads.** Disclosure questions go to the existing route.
4. **A question stays a question.** A beginner's answer gets a real answer first, joke second or never.
5. **Banter never replaces moderation.** Conduct reports follow the `event-code-of-conduct` route unchanged, and the enforcement ladder comes from `developer-community-moderation`.

### Emoji

Use a small set, each doing a job. I chose faceless emoji on purpose so nothing reads as mockery. Whether to allow face emoji is the team's call.

| Emoji | Use |
|---|---|
| 🔐 | security topic, neutral |
| ✅ | confirmed or done |
| ℹ️ | note, context |
| ⚠️ | caution, unverified |
| 🧵 | thread worth reading |
| 🎟️ | ticket and edition news |

Limit: at most 2 per message, and none in a reply to a report or an incident.

### Memes

You said no memes on stage, and you asked for banter and emoji, not memes. I left them out. Treat them as an explicit team decision, not a default.

### Examples

| Situation | Too stage-formal | On-guide | Off-guide |
|---|---|---|---|
| Welcoming someone | "Welcome to the FjordSec community server." | "Hi Mari, glad you're here 🔐 Say what you work on if you like, or just lurk. Both are fine." | "Yo new blood!! 🔥🔥" |
| Nothing has happened | *(silence)* | "Quiet month, nothing to announce. Next post: the digest, {date}." | "Big things coming soon!! 🎉" |
| Someone shares a CVE | "Please cite your source." | "Thanks for posting. Link to the advisory? ⚠️ I can't verify the severity from here." | "lol another day another RCE" |
| A mod gets something wrong | "Correction issued." | "I got that wrong. Fixed above, thanks for catching it ✅" | *(deleting the message)* |

### Drift check

Once a quarter, the mod lead reads ten random mod messages and asks: *would someone who watched the stage recognize these people?* A "no" means the expression moved the identity, so tighten it.

If the off-season expression feels too far from the stage, adjust the delta table. Don't add a second voice.

## 3. Conversion mechanism

**Pick: single re-engagement touchpoint.** It is one contact to last edition's attendees, timed to the next edition's opening. It reaches the whole list and costs the least.

- Name something that happened, such as a talk people remember, not the edition being sold.
- Give one cheap ask (call for talks, a topic request, "are you coming?"), not only "buy".
- Sign it with a person's name, in the register above.

Rejected for now:

- **Participation ladder.** Not worth it at the cost it would add. Revisit once you have a compounding plan and a named owner.
- **Auto-enrolling every registrant into the space.** Never do this. It spends a ticketing consent basis on a purpose nobody granted.

Scope is non-volunteer members only. Past volunteers belong to `event-volunteer-experience`.

## 4. Local posture

If the audience is Oslo only, there is no local cohort. Animating that audience is section 1's job.

If anyone outside your team has asked to run something under the FjordSec name, that is governance. Neither of the two closest sibling skills covers it, so stop there.

## 5. Member list and handoff

| Item | Decision needed from you |
|---|---|
| List owner | A named living person |
| Basis | What members were told at sign-up |
| Scope | "Announce FjordSec editions" only, unless members were told more |
| Review or deletion date | A date, set before the gap starts |

Name no jurisdiction here, and take the actual retention decision to your own counsel.

**Handoff page.** Write it now, not when someone leaves. Cover every account, admin role, invite link and domain. Name the holder today and the holder after.

- **Highest risk:** a Discord server owned by a personal account.
- **Order of operations:** transfer ownership of record first, then add admins.
- **Admins:** keep at least two.

## 6. Quarterly meetup: brief for `event-portfolio-strategy`

I am not designing this. The inputs I can hand over from the community side:

**What the Discord does around a meetup**
- It announces the date as content you deliver. It does not take on the venue, schedule or speaker work.
- It hands attendee lists back to the live member list, with consent basis stated.

**Questions for the portfolio decision**
- Is a quarterly event worth the effort for the same people who run FjordSec? Quarterly means three extra events a year.
- With 40 seats against a larger member list, how do you choose who gets in without it reading as a clique? This is the "ladder whose entry condition is being noticed" failure.
- Does a borrowed office bring conduct or content limits from the lender? Sponsor and venue conduct limits live in `developer-meetup-program`.
- Is one invited speaker per quarter a pipeline you can sustain? That is also `developer-meetup-program` territory.

**Success measure.** Carry rate is the number that answers whether the gap is bridged. That is the share of one edition's attendees who register for the next. A busier Discord does not count, and neither does meetup attendance on its own.

**Next step.** Run `event-portfolio-strategy` first. If it says yes, hand the format to `developer-meetup-program`.

## 7. Thresholds and gates

All thresholds are self-set, not industry benchmarks. Fix them before the gap starts.

| Measure | Type | Rule |
|---|---|---|
| Carry rate | Self-set | Fix a target before the gap. For context only, one 2025 trade-show source puts blended retention across all event types barely above 30%, which says nothing about a technical conference. |
| Cadence kept | Gate | Posts made versus planned. Two missed cycles means move down a rung, not try harder. |
| List integrity | Gate | Named owner and written retention decision on day one of the gap. |
| Handoff readiness | Gate | The access page exists, is dated, and names a living holder for every account. Check it on a schedule. |

## Rejected, for the record

- A distinct "cosy Discord" personality.
- Memes by default.
- Continuous light and heavy cadence.
- Designing the meetup inside this plan.
- Auto-enrolling registrants.

## What I need from you

1. **Who owns the gap months, and how many hours do they have?** This one answer picks between pulse and dormant.
2. Is the register really *sober, precise, formal*? If not, I'll route you to `event-cultural-identity` first.
3. Who owns the Discord account, and what were members told at sign-up?
4. Approve sections 1 to 5 one at a time, and tell me whether to proceed to `event-portfolio-strategy` for section 6.