# Sponsor track wording: Forgeworks Hack × Meridian Cloud

## Decision first

⚠️ **I can't write "every team must use the Meridian API, no exceptions" yet.** The skill treats it as the "sole substrate" rung and has a hard gate on it:

| Gate | Status |
|---|---|
| One sponsor funds the whole pool, event billed as theirs | ✅ Met |
| Someone on your team built a small thing end to end against the API | ❌ Nobody has |
| Sandbox or offline fallback confirmed **in writing** | ❌ Not in writing |
| Rate-limit headroom for your team count confirmed **in writing** | ❌ Only a verbal "fine for a few hundred users" |

"Great docs" and "fine for a few hundred users" are the partner manager's claims. They also measure the wrong thing. 200 hackers in one room, all hitting the API in the same 48 hours, is a burst from one venue, not a few hundred spread-out users. If the API stalls at hour 30, every team stalls, and a mandatory rule means no team can legitimately route around it.

So there are two versions of the wording. **Version A** is safe to publish now. **Version B** replaces it only after the gates clear.

---

## Version A: publish now (optional bonus challenge, "Built on Meridian" branding kept)

> **Built on Meridian: sponsor challenge track**
>
> Forgeworks Hack is **Built on Meridian**. Meridian Cloud funds the entire prize pool. Every challenge track awards a prize, and the Meridian challenge track is the featured one.
>
> **How tracks work.** Your team submits one project. That project may enter the general challenge track and the Meridian challenge track at the same time. Entering the Meridian track does not forfeit the general prize.
>
> **Context.** [Two or three sentences, written as a problem and not as marketing copy: who has a problem that Meridian's `[capability]` could address, and why it isn't solved today. Meridian drafts it, then confirms your rewrite.]
>
> **The challenge.** [One sentence ending in a question mark. Example shape: "How can `[user]` do `[task]` without `[pain]`, using Meridian's `[capability]`?"]
>
> **Constraints.** To enter the Meridian track, your submission must make at least one working call to the Meridian API and use the response in a visible feature. Describe what the call does, not which brand it uses, so a judge can check it. Do not commit your API key to a public repository.
>
> **Resources provided.**
> - Keys: [where and when teams get them. Recommended: issued at check-in, one per team.]
> - Rate limit: [Meridian's confirmed per-key figure, in writing.]
> - Docs: [link].
> - Meridian mentors on site: [hours]. Help desk: [location or channel].
> - Not provided: [anything Meridian does not supply, such as sample datasets or paid-tier features.]
>
> **Minimum viable submission.** One user action that triggers one real Meridian call and shows the result on screen. A working single flow counts. A diagram with no running call does not.
>
> **If Meridian is unavailable.** If the Meridian API or your keys are down or rate-limited through no fault of your team, you are judged on your design and your documented integration plan, not on a working call. Tell a Forgeworks organizer at the help desk, who will log the time. This applies to every team equally.
>
> **Prize.** The Meridian challenge track awards a prize funded by Meridian Cloud.

---

## Version B: publish only after the gates clear (required for all teams)

Use this only if all five conditions below are true. Swap it in for the Constraints paragraph and the intro.

> **Every project at Forgeworks Hack is built on Meridian.** To be eligible for any prize, your project must make at least one working call to the Meridian API and use the response in a visible feature. Use of other services and libraries alongside Meridian is allowed and expected. This requirement is part of the published rules, and organizers will not grant individual exemptions.
>
> The one exception is the platform-unavailable rule: if the Meridian API or your keys are down or rate-limited through no fault of your team, you are judged on your design and documented integration plan. Tell a Forgeworks organizer, who will log the time. This applies to every team equally.

The line "no exceptions" is only honest with that carve-out. Without it, an outage forces you to either disqualify everyone or improvise a favour, and the teams that finished before the outage will say it was a favour.

**Conditions before Version B:**
1. ✅ Someone on your team **builds a small thing end to end** against the API, using the real docs and a real key. About half a day, and it catches doc gaps before 200 people do.
2. Meridian confirms **in writing** the per-key rate limit, and that it holds for [team count] simultaneous teams from one venue network. Ask for a limit that is per key, not per account.
3. Meridian confirms **in writing** a sandbox or offline fallback (mock server, recorded responses, or a stubbed SDK mode).
4. Meridian provides one key per team (or per hacker) before kickoff, plus on-site engineers and a named escalation contact for the weekend.
5. Your signed sponsorship agreement already commits to a named challenge track. If it only says "branding", Version A is the honest one.

---

## What to do with Meridian this week

Tell the partner manager the branding stays either way, and that the requirement becomes mandatory once the written confirmations exist. The ask is a short list, not a refusal: sandbox, rate limits, keys, mentors. A sponsor who really has good docs and headroom can say yes to all four quickly. If they won't put it in writing, that tells you how much to trust the verbal claim.

## Notes on what I left out

- **No prize figures.** The cash amounts belong to the cash-prize decision and are not printed in the brief.
- **No IP or ownership clause.** If Meridian asks for one, route it to counsel through the sponsor agreement. Don't draft it here.
- **Placeholders in `[brackets]`.** I don't know what the Meridian API does, so the context, challenge question and capability are for Meridian to supply, as a problem and not a feature list. They confirm your rewrite.
- **Not yet decided:** your team-size cap, the hacking start and end times, and the submission deadline. The brief needs all three before it passes the seven-item publication check. Judging weights stay out of this section.

I skipped the interview and used your message as the answers. If any assumption is wrong, say so and I'll revise. In particular: does the signed agreement name a challenge track, and what is the team-size cap?