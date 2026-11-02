# QueueCraft: what's missing before Friday

**Verdict:** two things on your page break the skill's admin gate, and your plan to write the code of conduct later gets the sequence backwards. You can fix both by Friday. Everything else on the list can wait until after launch.

I read `event-first-edition` and its three references, plus the sibling `event-code-of-conduct` skill that it hands the CoC content to. I didn't run the one-question-at-a-time interview, so the assumptions below are labeled.

## 1. Two blockers (admin gate, fix before the announcement)

### Blocker A: your personal Gmail is the public contact

- **Rule:** the public contact must be a dedicated, neutral event alias. Never a personal or company address.
- **Why:** it makes one organizer, or that person's employer, look like the event's owner.
- **Why it matters for you:** your whole credibility rests on four-company neutrality, and a personal address undercuts it on day one.
- **Second problem:** you are the only person who can read it. That is a single point of failure, and it's the same problem as having one person receive conduct reports.
- **Fix, about 30 minutes:**
  1. Register a domain alias such as `hello@queuecraft.<tld>`. Skip this step if the domain already exists.
  2. Forward it to all four organizers, not just you.
  3. Swap it into the landing page, the announcement post, and any form footer.
  4. Open a shared credential vault for the domain, social, and ticketing logins. Don't leave them in your own password manager.

### Blocker B: the CoC must come before the announcement, not after the venue

- **Your reasoning:** "no point publishing rules for an event with no location yet."
- **Why that's backwards:** the CoC is the earliest hard gate in the process the skill sources. DevOpsDays blocks a new event's very first listing on it, ahead of venue and date.
- **What a listing needs:** organizer names, a city, and "coming soon". No date or venue is required, so the CoC doesn't need a location either.
- **Why waiting costs you:**
  - Anyone who sees the post today sees a community conference with no conduct policy.
  - Speakers, sponsors, and the first registrants are the people who judge that.
  - The skill's measure is "CoC published before anything is public", and that date is Friday.
- **A published policy with no pipeline is worse than none.** `event-code-of-conduct` states this directly. So the Friday CoC has to include a working reporting channel and named people, not just a values paragraph.

**Minimum viable CoC for Friday (about 3 to 4 hours of drafting):**

| Part | What to do |
| --- | --- |
| Base text | Adapt an established text (PyCon US or the MLH-style list). Don't adopt one verbatim, and don't write one from scratch. Keep the Creative Commons attribution. |
| Scope clause | Name who is bound: attendees, speakers, volunteers, sponsor and booth staff. Name where: every QueueCraft space, including chat or Slack and the website, plus the event itself, "venue and date to be announced". The venue is the only blank. |
| Reporting channel | The new shared alias, with a confidentiality promise. Reports are confidential, and the reporter's identity stays confidential unless they say otherwise. |
| Named responders | Publish 3 to 4 names, each from a different company, with a recusal rule. This is the pipeline: a report about one organizer must reach the others. |
| Escalation | A path for a report about a responder. Publish individual contacts for at least two people. |
| Response clock | Publish a short one. For example, acknowledge within 24 hours and give an outcome within a published window (the sources run about 1 week to 10 business days). |
| Sanctions ladder | A short honest version of 3 to 4 rungs your team can actually execute. Inventing sanctions after the first incident is how it becomes a governance crisis. |
| Deferred | Visible on-site responders, the rehearsal, and the transparency report. These need a venue and a date, so list them as "to be added once the venue is set". |

**Open decision for you:** does any organizer also hold the budget or sponsor relationships, or act as the headline name? If so, a report about them has no one above them to go to.

- **Promote if so:** an anonymous intake path.
- **Last resort:** an external trust-and-safety contractor, if the most powerful person sits on the team and no independent body exists above them.

This is not legal advice. Sponsor-contract clauses (ejection without refund, sponsor-staff compliance) belong to counsel, via `event-sponsor-agreement`.

## 2. Checks on the other gates

- **Team gate (≥3 organizers from ≥3 organizations, before venue or date is locked):**
  - Four companies pass on paper.
  - ⚠️ Untested elephant: do all four have real weekly hours alongside day jobs? The skill's fix is for each person to state a weekly hour count out loud.
  - If two miss two check-ins running, cut a scope rung.
- **Validation gate (real registrations before spending past the Good tier):**
  - A landing page and waitlist only prove stated interest.
  - Hold spend at the Good budget tier until tickets are actually claimed.
  - Don't commit to a venue deposit or paid extras before that.
- **Demand gate (interview Q1):**
  - The skill assumes demand is already validated, and I don't know that for QueueCraft.
  - If there's no waitlist, no community asking for it, and no sold-out precursor meetup, route to `event-market-fit` first.
  - The Friday launch can double as that smoke test if you treat it as one.

## 3. Things to fix or label on the page (cheap, 1 to 2 hours)

- **Name the organizers, with their city and "coming soon":** this is the sourced listing format, and it also shows the neutral multi-company team.
- **Say plainly what's undecided.** "Date and venue to be announced" is honest. Avoid placeholder program details that read as settled once the page looks polished.
- **Link the CoC and the shared alias from the footer** so they're one click from every page.
- **Don't announce a date or ticket price** unless the team has actually decided them.

## 4. What to write down this week (not Friday-blocking)

These come from the skill's launch brief. Each needs an owner and a date.

1. **Appetite and no-gos:** organizer hours per week and money. For example: no international speakers, no second track, no livestream, no expo hall.
2. **Scope tier:** I'd default to a single-focus standalone, meaning one day, one track, own registration. Move to a borrowed edition if demand is only stated-interest. Rule out a multi-city launch outright.
3. **Format and ownership:** I assumed community-run, cross-organization neutral, with sponsor revenue as cost recovery. If instead one company owns this, the team gate relaxes, but you should say so explicitly.
4. **Reverse timeline** (conference-scale, about T-12 months):
   - Venue search kicks off at T-12 months and is the longest-lead item.
   - Budget discussions start at T-10 and the venue is locked at T-9.5.
   - CFP opens around T-7.5, registration around T-6.5, and the program launches around T-3.5.
   - If your target date is sooner than about 12 months out, you need a compression lever: borrow a venue, run an invited-speaker program, or cut a scope rung.
   - Decide whether a larger event lands in Rotterdam near your window.
5. **Go/no-go dates:** at each one, an unready scope item gets cut and the date does not move. Pair them with Good, Better, and Best budget-tier downgrade dates, triggered by sponsorship revenue actually received.
6. **Pre-mortem** (run once team and rough scope exist):
   - Tigers: venue contract falls through, anchor sponsor pays late, lead speaker cancels, nobody volunteers for day-of roles.
   - Paper tiger: "nobody will come because we're unknown".
   - Elephant: team bandwidth.
   - Every launch-blocking risk needs a named owner and a decision date.

## 5. Action list, Wednesday to Friday

1. **Wed:** each of the four organizers states their weekly hours out loud, and you confirm who is on the response team. (30 minutes)
2. **Wed:** register the shared alias, set forwarding to all four organizers, and open the shared vault. (30 minutes)
3. **Wed to Thu:** draft the minimum viable CoC from the table above. Share it with all four organizers for review. (3 to 4 hours)
4. **Thu:** update the landing page and announcement post with the alias, the CoC link, organizer names and city, and "date and venue to be announced". (1 to 2 hours)
5. **Thu:** have counsel or a trusted reviewer read the CoC. (Not legal advice from me.)
6. **Fri:** publish. The CoC goes live at the same time or before the announcement.
7. **After Friday:** join a peer-organizer network (DevOpsDays runs one) and write down the appetite, no-gos, timeline, and pre-mortem.

## Open questions for you

- Is demand validated beyond stated interest (waitlist, an existing community, a precursor meetup)?
- Does any organizer also hold the budget, sponsor relationships, or headline-name status?
- Is there a hard date QueueCraft must land by, and does a larger event fall near that window in Rotterdam?
- Do you already own a venue contact, an employer or sponsor, or a meetup audience?

Answering these would let me turn sections 2 and 4 into a full launch brief. The Friday blockers stand regardless of the answers.