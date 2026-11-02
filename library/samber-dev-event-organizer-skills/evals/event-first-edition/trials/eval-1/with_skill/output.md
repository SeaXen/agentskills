# StreamSummit: launch plan status

**Verdict: I can't give you the full plan yet.** The skill's first step is a demand gate, and you don't pass it. Venue, program, budget and marketing would all be built on a guess. Below is the gate result, what to do about it, and the parts of the plan that don't depend on the answer.

## 1. Demand gate: not passed ❌

- **What you have:** "Streaming is exploding" and a decision made yesterday. That is level 1 on the validation ladder (opinion).
- **What you need:** level 3, which means real registrations such as waitlist signups, claimed early-bird tickets or deposits. The ladder runs opinion, then stated interest, then claimed ticket, then actually shows up.
- **Why it matters:** market growth isn't demand for your event. Your event needs a specific audience that will travel and pay for a day from an organizer nobody knows yet.
- **Where it goes:** the skill routes unvalidated demand to `samber/dev-event-organizer-skills@event-market-fit` before anything else. That skill also owns the attendee sizing from your existing community.

**Cheap validation, about 2-3 weeks of part-time work:**
1. Put up a one-page interest site with a waitlist. No date or venue is needed. This is the smoke test.
2. Ask 15-20 streaming engineers directly. Use Parqet's user community and meetups, but also people outside it.
3. Ask them whether they'd pay or commit, not whether they'd "be interested".
4. Write down the pass threshold before you look at the numbers. I won't invent one here.

If you can't get two outside people to co-organize, that fails the demand check and the team gate below at once.

## 2. The success metrics don't fit edition 1 ⚠️

Viral coefficient, CAC/LTV and month-over-month cohort retention measure sustained usage over time, and one edition can't produce that data. With one event and a few hundred attendees:
- There is no LTV, because there is no repeat purchase yet.
- There is no monthly cohort series to retain.
- A viral coefficient from one registration wave is noise.

That vocabulary belongs to `event-growth-strategy`, for edition 2 and later.

**Replace it with measures you can fix before the event:**
- Decide the pass/fail rubric now. Iterate, Okta's separate developer conference, set its post-event survey rubric before the event.
- Suggested inputs: registrations claimed versus show-up rate, a post-event survey score, share of sponsors and speakers who say they'd return, and how many attendees ask for edition 2.
- Keep the edition 1 data clean (source of each registration, survey consent) so edition 2 can compute cohort and referral numbers.

## 3. Ownership: "independent" or Parqet's? ⚠️

Two organizers from one company fail the team gate, which needs at least 3 organizers from 3 different organizations. The gate exists to block single-company events.

You have to pick one model:
- **Community-run:**
  - You need at least two outside co-organizers before locking a venue or date.
  - Sponsor revenue covers costs, and credibility comes from neutrality.
  - Parqet becomes one sponsor among others, with no Parqet email alias or branding as the owner.
  - The Parqet team has to tolerate competitors on stage.
- **Company-run:**
  - Be honest about it. The team gate relaxes by design, and budget replaces volunteer time as the limit.
  - You lose the neutrality advantage. Calling it "independent" while Parqet runs it is a credibility risk with this audience.

I recommend deciding this first, because it changes team, budget, speakers and sponsor strategy. Which is it?

## 4. What I can fix now, whichever way demand comes out

**Timeline variant:** conference-scale, about 12 months from venue search to doors-open. Don't borrow the 4-9 month hackathon timeline. Venue search is the longest-lead item, and starting it is exactly what the demand gate postpones. A realistic date depends on your answers to the questions below.

**Scope tier (provisional):**
- **Single-focus standalone** is the default. That means one day, a single track, no expo and no multi-city.
- **Borrowed edition** applies if validation stays at stated interest. Run it as a special session of an existing meetup or community with a borrowed venue.
- **Full-footprint** needs evidence of several hundred real attendees, or committed company budget plus an existing audience.
- **Ruled out for edition 1:** multi-city, livestream, custom app.

**Administrative first steps, before any public announcement:**
1. Publish the code of conduct. It is the earliest hard gate, ahead of venue and date.
2. Set up a neutral shared email alias, not a Parqet or personal address.
3. Set up a shared credential vault.
4. Join a peer-organizer network.

**Pre-mortem seeds (to be completed once team and scope exist):**

| Risk | Category | Note |
|---|---|---|
| "Nobody will come, we're unknown" | Paper tiger | Only a paper tiger once the baseline sizing exists. Today it's unmeasured. |
| Venue contract or deposit falls through | Tiger | Owner and date still to assign. |
| Sponsor payment arrives after deposits are due | Tiger | Owner and date still to assign. |
| Keynote cancels | Tiger | Owner and date still to assign. |
| Two organizers' bandwidth next to day jobs | Elephant | Each of you states weekly hours out loud. |
| Parqet seen as owner of an "independent" event | Elephant | Resolve via section 3. |

**Marked not yet decided:**
- Venue
- Date and city
- Program, speakers and CFP versus invitations
- Ticket price
- Budget figures and the Good/Better/Best downgrade dates
- Marketing channels

I haven't filled these in because anything I wrote would look settled and wouldn't be.

## 5. Questions to answer, one at a time

1. Is StreamSummit community-run (neutral, outside co-organizers) or Parqet-run?
2. Is there a hard date it must land by, or is the date free?
3. Is edition 1 a one-off bet or the start of an annual event?
4. What are your weekly organizer hours and your budget appetite?
5. Which city do you have in mind, and what big events (Kafka Summit, Flink Forward and so on) fall near your window?
6. What assets do you have: an existing Parqet community or meetup, a venue through Parqet, or warm sponsors?

**Useful side step:** ask an organizer who has run a larger streaming or data event what they actually spent. That is better than any template for setting your appetite.

## 6. Next step

After the demand check passes, send me your answers to section 5 and the validation numbers. I'll then produce the full brief section by section: appetite and no-gos, scope tier, team against the gate, reverse timeline with go/no-go dates, budget tiers and the completed pre-mortem.

Nothing was written to disk or sent anywhere.