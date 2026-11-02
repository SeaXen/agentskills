# CloudNative Porto: volunteer budget review

I read `event-volunteers/SKILL.md` and its three references, plus the sibling `event-volunteer-experience` skill, because the post-event thank-you belongs to that sibling. I haven't run the full interview yet. I assume a built program: 600 people, two days, probably multi-room. If you have a payroll events team and a staffing budget, this skill is the wrong tool and you should procure the labour instead (`event-vendor-sourcing`).

## Verdict

| Your idea | Verdict |
|---|---|
| EUR 50 cash per volunteer per day | ❌ Drop it |
| Skip the t-shirts to fund it | ❌ Keep the shirts |
| Publish names and photos the morning after | ⚠️ Only with prior, per-person consent |
| 4-hour shifts, lunch on your own | ❌ Feed them |

## 1. Cash stipend: remove it

The skill deletes a cash stipend from the recognition menu outright. It does not demote it. Volunteer programmes at technical events do not pay stipends, and that uniformity is itself the signal.

- ⚠️ Paying volunteers changes what the arrangement is. The status question that follows cannot be undone mid-edition once the first payment has gone out.
- ⚠️ EUR 50 for a 4-hour shift works out to EUR 12.50 an hour. That looks like wages, which is the opposite of what you want.
- ⚠️ Ask a Portuguese accountant or lawyer before paying anyone. I'm not asserting the specific tax or labour rules.
- ℹ️ The sibling skill deletes any reward with real cash value too, such as raffle prizes, travel grants and comped tickets to other events. Swapping the cash for one of those doesn't fix it.

## 2. What makes people feel valued

The skill's recognition ranking is by value (shifts finished and people who come back):

1. **Feeding them properly.** This is the top value rung.
2. **Access in exchange for the shift.** Examples are a saved seat in the session they staff, or front-row seats for room leads.
3. **A t-shirt they keep.**
4. Shift-linked status perks.
5. Thanks by name at the end of the shift (spoken, not published).

Your plan skips the top two and cuts the third. The budget is better spent in this order:

1. **Food at the post.** A 4-hour shift is past the roughly 3-hour mark where the skill promotes feeding. Cover:
   - Drinks and snacks at the desks.
   - A meal or voucher for any shift that spans lunch.
   - Full meals for setup and teardown crews, who work longest.
2. **Access.** Put a "talk you want to see" question on the sign-up form and match posts to the answers. This is free.
3. **The shirt.**
   - It is how an attendee finds a volunteer in a corridor.
   - It also makes volunteers identifiable for the code-of-conduct front line, because any shirted volunteer is someone a distressed attendee will walk up to.
   - FOSDEM keeps colour-coded shirts through budget cuts for this reason. A cheap shirt, or even a coloured lanyard or vest, covers the need.

## 3. Shifts of 4 hours

The skill's anchor is 2-3 hour shifts, so 4 hours is long.

- **Shorter shifts.** Consider 2-3 hour shifts, or a 4-hour shift with a guaranteed break at a post that can be covered.
- **Arrival buffer.** Put it inside the published time: 15 minutes, or 30 for first-timers. A "09:00-13:00" shift is really 08:45-13:00.
- **Replacement rule.** Nobody leaves a post without confirmation of a replacement. Publish this with the grid.
- **Referent.** Name one referent per shift who owns live direction for that shift's posts.

## 4. Names and photos on a thank-you page

A published thank-you is the sibling skill's territory (`event-volunteer-experience`), and it has a consent gate. "Naming people publicly without asking" is a listed failure mode. Consent completeness is a hard gate: every person named must have agreed, with no exceptions.

1. Ask at sign-up, and ask again before publishing.
2. Ask for name and photo as two separate consents.
3. Offer an opt-out that needs no explanation.
4. Keep the page opt-in. Never publish "everyone" by default.
5. A photo is personal data, and a public page in the EU brings GDPR into play. Name an owner, a retention rule and a takedown path before the first form goes out.
6. Don't use the same message for the end-of-shift spoken thanks and the published page. If you do, the consent gate never gets asked.

Publishing the morning after is fine as long as consent was collected before the event.

## 5. Sizing

I can't give a headcount from "600 people". The skill refuses attendee ratios. The only circulating ratio comes from an event that closed describing its own load as past responsible limits.

Size it bottom-up:

```
shift-slots(post) = people at once × hours covered ÷ shift length
volunteers = Σ slots ÷ shifts per volunteer (from your sign-up form) + floater reserve
```

Include:
- Registration and badge desk.
- Info desk.
- A lead for each room running at once.
- Cloakroom.
- Floaters (a real post, not slack).
- AV support.
- The entrance during any public closing session.
- Setup and teardown.
- The named code-of-conduct response roster.

## 6. Recruitment

My default ranking is a past-volunteer call-back plus a registration-gated sign-up form. This default is re-ranked by your answers to the questions below.

- Publish the role catalog before sign-up opens.
- Open sign-up six or more weeks out.
- Confirm every sign-up individually, by name, against a named coordinator.
- A call with no coordinator and no confirmation step is deleted outright.

## 7. Briefing

Brief every volunteer before their first shift on three things: their post's choreography, who they escalate to and on which channel, and the five-step code-of-conduct escalation script. The script includes the line that they are not required to confront anyone.

## Questions for you

Please answer these before I build the grid:

1. What date is the event, and what fixes the roster deadline (shirt order, badge print, briefing)?
2. Does a run of show or schedule exist, with room count and a registration desk?
3. Who is the named volunteer lead?
4. Which posts handle cash, payments or registration records? Those get named people and a short training gate.
5. Is this a one-off or a recurring event?
6. What do you already have: last edition's volunteer list, a local user group or student chapter that could send a block of people, or a registration system that could carry a sign-up flow?
7. What are the real budget and coordinator hours? If you give me the EUR 50 × volunteers × 2 days figure, I'll show what it buys in food and shirts.