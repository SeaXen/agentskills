# Cascade Summit partner dinner: guest list and invitation timeline

I followed `event-vip-social-program`. It says to interview you one question at a time and get approval section by section. You asked for the finished deliverable, so I made assumptions, listed below, and changed some of your columns. Both are explained first.

## What I changed from your column list, and why

| You asked for | In the sheet | Why |
|---|---|---|
| tier (platinum / gold / personal contact) | **Who put the name forward** (Platinum sponsor, Gold sponsor, host, speaker, team) | The skill treats a tier column as the tier itself. It also lets you cite the same rule to every asking party. |
| seniority | dropped | The skill says seniority never decides a seat, and the list never records a judgment about a person. |
| priority 1-5 | **Why this seat exists** (one sentence) | A rank invites disputes and does real harm if the sheet leaks. A row whose reason you have to invent comes off the list. |
| dietary | **Access requirements** (only if the guest supplied them) | Dietary answers make the sheet a named-person record, so it needs a deletion date. |
| confirmed y/n | **Answer given** (Offered / Accepted / Declined / No reply) plus date | "Offered" and "confirmed" are different states, and mixing them is how a room gets over-promised. |

## Sheet 1: Seat list (owner-only tab)

Paste into Google Sheets as a header row and one row per guest. The two example rows are placeholders.

```
Name | Company | Why this seat exists (1 sentence) | Put forward by | Date put forward | Answer given | Date of answer | Access requirements (only if supplied) | Invitation sent (date)
Jane Example | Example Corp | Needs a private talk with <named person> about <named topic> | Platinum sponsor | <date> | Offered | <date> | Vegetarian (supplied by guest) | <date>
Sam Example | Personal contact | <one sentence> | Host | <date> | No reply | <date> | | <date>
```

Rules for the sheet:
- **Owner:** one named person holds this tab, edits it and sends every invitation. Name them here: `________`.
- **No tier, rank or seniority column.** Don't add one later.
- **Deletion date:** set it now. The default is the day post-event follow-ups go out. Date: `________`. The owner confirms deletion.
- **Circulation by need.** The other three team members don't get the full tab. Give the door person a second tab with names in alphabetical order and nothing else. The other two see only their own sponsor's asks.
- **Capacity:** write the seat count and who set it (venue, budget or conversation) in a cell above the table. I haven't invented a number. Capacity is a limit, not a reason to pick someone.

## Sheet 2: Asks log (owner-only)

```
Asking party | What they asked for (their words) | Date | Rule cited | Answer sent | Date answered | Alternative offered
```

Every asking party needs an answer, and the same rule goes to each. A party with no recorded answer is a failure on the skill's measurement list.

## Seat rule, written before the first ask

The skill defaults to a host list plus a capped number of nominations per asking party. That fits you because Platinum and Gold sponsors are already asking.

> "The dinner seats what the room seats. Each sponsor has the same stated allowance of `<N>` seats, and the host fills the rest. We can't add seats beyond that. Here is what we can do instead: `<introduction during a break / a scheduled conversation / the general evening>`."

Decide `<N>` yourself, per party, and agree it as a number before anyone asks. If a sponsor's agreement already promises seats, those seats are a deliverable. Take them off this list and route them to `event-sponsor-fulfillment`.

## Invitation timeline

I haven't invented lead times, so every date is a placeholder you fill in. Set **D = dinner date** and **R = your RSVP deadline**.

| Step | When | Who | Action |
|---|---|---|---|
| 1 | Before anything goes out | Owner | Confirm the room, capacity and deletion date. Write the seat rule and refusal lines. |
| 2 | Before any invitation | Owner | Tell each asking party its allowance, as a number, in writing. |
| 3 | Wave 1: once the host list and allowances are final | Owner only | Send individual, private invitations to host-nominated guests and each sponsor's nominees. Never use a group thread and never let anyone else invite. |
| 4 | Same day as each send | Owner | Mark "Offered" and the date in the sheet. |
| 5 | Chase 1: a few days before R, for "No reply" | Owner | One short personal message restating date, place and how to decline. |
| 6 | Chase 2: at R, for "No reply" | Owner | A second message, or a call for a guest with a close relationship. Offer the easy "no". |
| 7 | After R | Owner | Treat silence as a decline. Release the seat to the next name, using the same rule for every party. |
| 8 | Day before D | Owner | Send a final note with the room and the way in. Give one name and one contact. |
| 9 | D | Owner | One door person holds the alphabetical page. An unlisted name gets "the owner will come to you", never an explanation. Nobody says "VIP". |
| 10 | Deletion date | Owner | Delete the sheets. The door page goes back to the owner, not into a bin. |

Each invitation says:
- what the dinner is, in plain words
- when and where, and how to find the door
- who else is there, in shape rather than by name
- what the guest misses on the public programme
- how to decline easily
- one name and one way to reach them

For the wording, aim for something like "a small dinner so you can talk to the people you came to talk to". Add one line saying this is a relationship dinner, not a meeting arranged for a sponsor. That guards against it looking like seats sold for access.

## Open items I couldn't ask

1. **Has `event-vip-management` run, and did it find anyone in scope?** If not, run it first.
2. **What does the dinner do that the general evening can't?** If you can't answer, the skill's default is no separate dinner. A named companion would walk each guest through the general evening and make the intros you'd planned.
3. **Did any guest ask not to be identified, listed or photographed?** If so, use no wristband and no programme listing.
4. **Is the dinner promised in a prospectus or sponsor agreement?** If yes, it's a deliverable and the published-criteria rule applies.
5. **Is the owner also running the main event that day?** If so, don't plan a separate-venue dinner.
6. **Who owns it by name?** Put the name in the sheet header.
7. **Catering and drink** go to `event-hospitality`. Access needs go to `event-accessibility-inclusion`.

Tell me the answers to 1 to 6 and I'll re-rank the seat rule and placement.