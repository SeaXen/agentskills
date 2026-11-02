# GoWest inbound partnership triage: what to do with each of the three

I read the event-media-partnerships skill and both its references. I skipped the interview and used what you told me: community-run, in-person, Denver, 700 attendees, October. Where I assume something, I say so.

## Summary

| # | Inbound | Classification | Verdict | Next action |
|---|---|---|---|---|
| 1 | DevSecCon Rockies newsletter swap | ⚠️ Another event, not a media property | ✅ Accept in principle, run it under `cross-event-promotion` | Reply yes, ask for send dates and blurb length |
| 2 | Gophers Denver Discord, CFP link in #general tonight | Community collab | ❌ Don't post tonight | Message the mods first |
| 3 | Cloud Native Weekly: swap, expo table, "official media partner" | Full media-partner tier | 🟠 Don't accept as asked | Counter with the default rung; table only after the Hexacloud check |

## 1. DevSecCon Rockies: accept the swap, but it belongs to a sibling skill

- **Classification:** DevSecCon Rockies is an event. Newsletter swaps between two events fall under `samber/dev-event-organizer-skills@cross-event-promotion`, not this skill. The mechanics are the same, so the structure below carries over.
- **Verdict:** ✅ Yes. It is the cheapest high-value rung in the skill, and a security-conference audience overlaps with Go developers.
- **Next action:** Reply yes, then get these terms in writing:
  1. Each side names its deliverables. For example: one blurb of N words with a tracked link in a named send, plus one reminder line before a named date.
  2. Each side mails only its own list. No subscriber data crosses.
  3. Each side uses a distinct tracked link, so you can measure referrals.
  4. Add the swap to your delivery ledger, including the mention you owe them. Your own promised mentions are the ones most often dropped.
- **Gap:** I haven't read the cross-event skill, so check it for anything specific to event-to-event swaps.

## 2. Gophers Denver Discord: don't drop the link in #general tonight

- **Classification:** A community collab with a Discord community. This is the rung the skill says "needs a warm relationship to not read as spam."
- **Verdict:** ❌ Not as a cold post. A cross-post negotiated with a moderator lands, but the same post dropped in cold "reads as spam and burns the community for future editions." The server's size is the reason to be careful, not the reason to post. 14k Go developers in Denver is your best local audience, so protect that relationship.
- **Next action, tonight:** DM or email the mods from a named organizer, not an event alias. Use the outreach template:
  1. **The event:** GoWest, a community-run Go conference in Denver, 700 attendees, October.
  2. **One specific overlap:** name something real, such as a recent thread or meetup they ran. Generic flattery scores zero.
  3. **The proposed exchange:** the mods post in #general (or an events channel) and you list their server on the GoWest community page with a social thank-you. A joint AMA with a speaker also works.
  4. **The ask:** a yes or no, or a 20-minute call.
- **Fallback:** Ask them how they prefer event posts. Many servers have an #events or #announcements channel, and following their rules is the warm path.
- **Don't offer a talk slot** as a sweetener. The skill rules that out.
- **Tracking:** Use a distinct tracked link for this community.
- **CFP deadline:** If the CFP closes soon and the mods are slow, tell them the deadline when you ask. Don't let urgency push you into a cold post. If the CFP is already closed (you said October, and today is 2026-10-14), pitch attendee registration instead of the CFP.

## 3. Cloud Native Weekly: counter-offer, and don't promise the table yet

This is a full media-partner tier request: a badge, an on-site table, and multi-channel promotion. It is the highest-effort, highest-risk rung, and two issues sit on top of it.

**Issue A: the Hexacloud conflict.**
- Hexacloud, your Gold sponsor, has exclusivity on observability tooling.
- Cloud Native Weekly runs a paid observability jobs board. That is commercial inventory in Hexacloud's category, and observability employers (possibly Hexacloud's competitors) pay to appear on it.
- A Cloud Native Weekly table in the expo hall puts that promotion on the floor, in space and category inventory a paying sponsor may already own. The skill requires the sponsor-exclusivity check (workflow step 7) before any on-site perk is offered. Withdrawing a booth the partner has already announced is hard.
- Whether it breaches the exclusivity depends on the exact wording in Hexacloud's contract. Is it "tooling vendors" or "any observability promotion"? Check the wording. I haven't seen it. Run the check with `event-sponsor-fulfillment`.

**Issue B: "official media partner."** That is a public badge. Hold it until the terms exist in writing, because a badge already announced is hard to retract.

**Verdict:** 🟠 Don't accept as asked. Counter-offer in this order:
1. **Now:** Offer the default rung: a calendar listing plus a logo-and-social swap. Add the newsletter mention swap they proposed, which is the part you want anyway. No table, no badge yet.
2. **After the Hexacloud check:** Decide on the table.
   - **If the exclusivity covers it:** Say no to the table. Offer a non-floor perk, such as a guest slot on their channel or a ticket allocation.
   - **If the exclusivity doesn't cover it:** Offer the table with written limits: no observability jobs-board promotion at the table, no materials for observability tooling vendors, and a placement away from the Hexacloud booth. Tell Hexacloud before you announce it. A Gold sponsor finding out from the expo map will cost you more than the table is worth.
3. **Later:** Promote them to the full tier only if their audience scores well and you want a compounding relationship for future editions. Score them first on the six criteria: fit, size, brand alignment, engagement quality, reciprocity and ease. Ask them for their own open-rate and click numbers.

**Terms to write down for any version of the deal:**
- Countable, dated deliverables in both directions.
- No editorial obligation. You are buying promotional inventory, not coverage.
- No list or audience-data transfer.
- Logo and branding approval before first publication.
- An exit clause.

**If they answer with a rate card:** That means their promo inventory is commercial, not that they refuse to engage. Offer the barter formats they will still do (listing, guest slot) or decline.

**Watch for a mixed deal.** If they later add "and we'll pay a bit for the table," that is a discounted sponsor. The cash goes to the sponsor block at the real rate, and only the barter leg stays here. Hexacloud's Gold exclusivity also makes any paid observability-adjacent sponsorship from them a problem.

## Order of operations

1. Tonight: DM the Gophers Denver mods (item 2). About 10 minutes.
2. Tonight or tomorrow: Reply yes to DevSecCon Rockies and ask for the details (item 1).
3. This week: Pull Hexacloud's exclusivity clause. Then send Cloud Native Weekly the counter-offer (item 3).
4. Open a delivery ledger with one row per promised item in both directions, and set a distinct tracked link per partner.

## Open questions for you

- What does Hexacloud's exclusivity clause say exactly: vendors only, or any observability promotion on site?
- Is the CFP still open? That decides whether the Discord pitch is about the CFP or registration.
- Does Cloud Native Weekly's audience match GoWest's? Their jobs board is observability-heavy, which may be a poor fit for a Go conference.

The skill's scores and rankings are my judgment, not measured results. Your tracked-link data will show what each deal actually returns.