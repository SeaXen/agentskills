# DataForge Summit: date announcement plan

## Verdict: do not publish Monday ❌

The skill treats one gate as non-negotiable: **you cannot announce a date until you know you have a way to handle money.** Your own message says that gate is open:

| Gate item | Status |
|---|---|
| Way to receive money (ticketing, processor, entity that can invoice sponsors) | ❌ No ticketing platform. LLC still being filed. |
| Named person accountable for the money | ❓ Not stated |
| Date decided internally | ✅ Third week of September |
| Calendars checked or marked outstanding | ❌ None checked yet |
| Competing events scanned and each marked dodge or piggyback | ❌ Only a rumor so far |
| Trigger precondition met (signed venue contract) | ❌ Verbal yes only |

The skill documents that teams who published before payment handling existed had to reschedule or cancel. A published date is a promise. Yours would be a first-edition promise from an LLC that doesn't exist yet, backed by a venue that hasn't signed.

The skill says to decide the date internally, publish nothing, and bring the announcement menu back once money handling exists. So I'm not ranking announcement options for Monday.

## Why "claim the slot" doesn't need a blog post ℹ️

A public date doesn't reserve anything. The contested resources are the venue, hotel blocks, sponsor budgets, and speakers. A signed contract secures the venue, and a blog post doesn't. If the competitor is real and well-funded, they win a race of announcements. They don't win a race against your contract.

## What to do Monday instead (private, no public date)

1. **Get the verbal yes in writing.** Ask the venue for an email or a written hold on the window until the contract is signed. This is the real slot-claim.
2. **Name the money owner** and the fastest path to a working payment method. Options: an existing entity that can invoice, a ticketing platform that accepts a pending entity, or waiting for the LLC. Pick the fastest.
3. **Pick the ticketing platform this week.** It is the longest unknown on your path.
4. **Draft the blog post and the social posts now, and don't publish them.** They will be ready the day the gates clear.
5. **Run the competing-event scan** (below). The rumor is unverified, and the scan will confirm or kill it.

## Day type

- **Weekday.** A 300-person data-engineering conference is an employer-time audience.
- Source: DevOpsDays organizing guide ("weekends are typically used for refreshing energy with family").
- ⚠️ This is my assumption, because Q1 is unanswered. If you target students or hobbyists, the rule flips to a weekend (MLH guide). Don't average the two with a Friday compromise.

## Candidate windows

- "Third week of September" is ambiguous. If this is September 2027, the Monday-to-Friday weeks starting Sept 13 or Sept 20 both qualify. Tell me which you mean.
- You have one window, and the skill wants three to five. Your venue conversation should carry options:
  - the week before and the week after, as alternates
  - the venue's own quiet periods (ask them)
- Unless an external constraint forces the window (a venue with one open date, a sponsor deadline). If so, write down what fixes it and who could move it, and skip generating alternates.
- Season is a hypothesis. You have no prior edition to test it against.

## Calendars

I have not checked any of these, and I won't guess dates from memory.

| Category | Status |
|---|---|
| Attendees' employer quarter-end and fiscal-year-end freezes | ⏳ Outstanding |
| School holidays for attendees' children | ⏳ Outstanding |
| US public holidays and bridge days for the exact year | ⏳ Outstanding |
| Religious and cultural observances (many move each year) | ⏳ Outstanding |
| Ecosystem anchor dates (flagship data conferences, major releases) | ⏳ Outstanding |
| Austin civic events (festivals, marathons, trade fairs, sports) | ⏳ Outstanding |
| Attendees' travel-approval cycles | ⏳ Outstanding, test with 2-3 prospects |
| Multi-geography observances | ⏳ Outstanding, promote this rung if attendees fly in from several countries (Q2) |

Check each one against an authoritative source for the specific year, such as an official holiday page or a published academic calendar. "Probably fine" counts as outstanding.

## The competitor rumor

- **Status:** unverified. Don't build a public timeline on it.
- **Scan, in order:**
  1. Event networks and homepages that list scheduled editions.
  2. Adjacent-topic conferences from different organizers. Most real conflicts come from here.
  3. A cross-topic calendar such as confs.tech. Absence from it proves nothing.
  4. CFP aggregators, which surface events that have claimed a window but not announced it.
  5. Austin non-topical events.
  6. Ask 2-3 prospective attendees and sponsors what else they plan to attend. This is usually the highest-yield ten minutes.
- **Decision per event:** dodge or piggyback.
  - Dodge if they compete for the same sponsors, speakers, or venue in the same quarter.
  - Piggyback if they draw the same travelers and the other event is complementary.
  - A same-month data conference in the same city, aimed at your audience, leans toward dodge on sponsor budgets. But I won't call it without the facts.
- **Alternative:** if the rumor is confirmed and the slot is genuinely contested (Q9), that changes which announcement trigger is defensible once the gates clear (see below).

## Announcement plan: dormant until the gates clear

**Release conditions, all required:**
- ✅ Money handling works (platform live, entity able to receive payment).
- ✅ Named money owner.
- ✅ Calendar checks done or explicitly listed as outstanding, and you've seen that list.
- ✅ Dodge-or-piggyback decided for every competing event found.
- ✅ Trigger precondition met.

**Trigger choice, made when the gates clear:** your timeline suggests the money gate may clear before the venue contract does. The skill allows publishing before signature only when a slot is contested and early claiming is worth a real retraction risk, or when the venue relationship makes the signature near-certain. A first-edition event has no track record, so a bare date persuades nobody. Consult `event-first-edition` on whether to wait for an anchor speaker or an open CFP. The call is yours, and I'd make it then with the facts in hand.

**Content skeleton to draft now (don't publish):**

| Day | Asset |
|---|---|
| T0 | Blog post: date, city, one-line reason to attend, and a way to register interest. Pin the same date on the site. |
| T0 | Socials: same-day post on your main channels. Link the blog post. |
| T+1 to T+4 | One post per day on one angle each (the problem, the audience, the venue, the "why Austin"). |
| T+5 | A call to action: mailing list, CFP interest, sponsor inquiry. |

Don't include a ticket-on-sale promise until the platform is chosen. Don't write a fake urgency line about the competitor.

## Questions I need answered 🎯

1. Who is the audience: employers' staff, students, or a real mix?
2. Do attendees travel from one city, one country, or several countries?
3. Is September 2027 correct, and is the window forced by the venue, or can it move a week either way?
4. Who will be accountable for the money, and what is the fastest path to a working payment method?
5. What is the evidence for the competitor rumor, and where did it come from?
6. Does the venue relationship make the signature near-certain, or is it still negotiable?

## Handoffs

- `event-venue-sourcing`: carry the candidate windows into the venue conversation.
- `event-first-edition`: launch gates for a first edition's announcement.
- `event-planning-timeline`: the work-back schedule once the date is locked and published.
- `event-risk-management`: the competitor conflict, carried as a hazard if the window turns out to be forced.

Once the gates clear, I can finalize the blog and social drafts.