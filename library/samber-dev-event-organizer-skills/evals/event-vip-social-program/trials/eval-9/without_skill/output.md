# Cascade Summit partner dinner: guest list and invite timeline

I don't know the dinner date or the number of seats, so the timeline counts back from **D** (dinner day). Put the real date in cell B1 of the Timeline tab and the dates fill themselves in.

## 1. Guest-list sheet

### Tab 1: `Guests`

Paste the header row into A1 in Google Sheets, or import the CSV below.

| Col | Header | Type / validation |
|---|---|---|
| A | Name | Text |
| B | Company | Text |
| C | Tier | Dropdown: `Platinum`, `Gold`, `Personal contact` |
| D | Seniority | Dropdown: `C-level`, `VP`, `Director`, `Manager`, `IC` |
| E | Priority (1-5) | Dropdown: 1, 2, 3, 4, 5. **5 = must have in the room, 1 = nice to have.** |
| F | Dietary | Free text. Use "None" when asked and none, so blank means "not asked yet". |
| G | Confirmed y/n | Dropdown: `Y`, `N`, `Pending` |

I recommend adding the columns below. Cut any you don't want. The first seven are your original ones, so the sheet works without these.

| Col | Header | Why |
|---|---|---|
| H | Invite owner | One of your four. Prevents two people chasing the same guest. |
| I | Invite wave | `1`, `2` or `3`. Driven by priority (see timeline). |
| J | Invited on | Date |
| K | Last chased | Date |
| L | Chases sent | Number. Cap at 3. |
| M | Plus-one | `Y` / `N`. Matters for the headcount. |
| N | Allergy-critical | `Y` if the dietary need is a safety issue, not a preference. The venue needs this by D-7. |
| O | Notes | Relationship context, how they like to be reached |

I'd use `Pending` instead of a bare blank in column G. With only y/n, you can't tell "declined" from "hasn't answered", and that is exactly the group you chase.

### Starter CSV (import via File > Import)

```csv
Name,Company,Tier,Seniority,Priority (1-5),Dietary,Confirmed y/n,Invite owner,Invite wave,Invited on,Last chased,Chases sent,Plus-one,Allergy-critical,Notes
Example Person,Example Co,Platinum,VP,5,,Pending,,1,,,0,N,N,
Example Person 2,Example Co 2,Gold,Director,3,,Pending,,2,,,0,N,N,
Example Person 3,Example Co 3,Personal contact,C-level,4,,Pending,,1,,,0,N,N,
```

Delete the three example rows once you've pasted in real names.

### Formulas and formatting

- **Sort:** sort by E (Priority) descending, then C (Tier). Use a filter view per person, so one teammate's sorting doesn't scramble everyone else's.
- **Wave assignment** (I2, fill down):
  `=IF(E2>=4,1,IF(E2=3,2,3))`
- **Conditional formatting on column G:** green for `Y`, red for `N`, amber for `Pending`.
- **Highlight rows to chase** (custom formula on A2:O, amber fill):
  `=AND($G2="Pending",$J2<>"",TODAY()-MAX($J2,$K2)>=4,$L2<3)`
- **Protect columns A to E** so only the list owner edits them. The other three people update G, J, K and L.

### Tab 2: `Dashboard`

| Metric | Formula |
|---|---|
| Seats available | Type the number in B1 |
| Confirmed | `=COUNTIF(Guests!G:G,"Y")` |
| Pending | `=COUNTIF(Guests!G:G,"Pending")` |
| Declined | `=COUNTIF(Guests!G:G,"N")` |
| Plus-ones confirmed | `=COUNTIFS(Guests!G:G,"Y",Guests!M:M,"Y")` |
| Headcount | Confirmed + plus-ones |
| Seats left | Seats available - headcount |
| Platinum confirmed | `=COUNTIFS(Guests!C:C,"Platinum",Guests!G:G,"Y")` |
| Priority 5 confirmed | `=COUNTIFS(Guests!E:E,5,Guests!G:G,"Y")` |
| Allergy-critical | `=COUNTIF(Guests!N:N,"Y")` |

**How many to invite:** invite about 1.3 to 1.5 times your seat count in total. Expect roughly 20 to 30% to drop out between a yes and the night itself. The third wave is your backfill pool, so don't send it until waves 1 and 2 show real decline numbers.

## 2. Invite timeline

Put the dinner date in `Timeline!B1`. Column C is `=$B$1 - offset`. Weekdays only, mornings in the guest's local time zone.

| When | Action | Who |
|---|---|---|
| **D-8 weeks** | Lock the guest list, seat count and venue hold. Assign an invite owner to every row. | Whole team |
| **D-7 weeks** | Send a save-the-date to waves 1 and 2: date, city, "formal invite follows". Personal note for Platinum and priority 5. | Owners |
| **D-6 weeks** | **Wave 1 invites** (priority 4-5). Individual, not mass mail. One line on why this guest and who else will be there. RSVP deadline = D-4 weeks. | Owners |
| **D-5 weeks** | **Wave 2 invites** (priority 3). Same format. Deadline = D-3 weeks. | Owners |
| **D-5 weeks +3 days** | **Chase 1, wave 1 non-responders.** Short, personal, a different angle from the invite (say who's confirmed). | Owners |
| **D-4 weeks** | **RSVP deadline, wave 1.** Chase 2 for anyone still pending, with a direct ask: "Can I hold a seat for you?" For priority 5, call or text in place of email. | Owners |
| **D-4 weeks +3 days** | **Chase 1, wave 2.** | Owners |
| **D-3 weeks** | **RSVP deadline, wave 2.** Chase 2 for wave 2. Review the dashboard. Send **wave 3** (priority 1-2) to fill the seats declined waves left empty. | Whole team |
| **D-3 weeks +3 days** | **Final chase** for wave 1 and 2: a clean "last call, releasing your seat Friday". Then mark `N` and release the seat. | Owners |
| **D-2 weeks** | Wave 3 deadline. Release any remaining pending seats. Waitlist backfill is allowed from here. | Whole team |
| **D-10 days** | Send the **confirmation + dietary form** to every `Y`. Ask for dietary needs, allergies and plus-one details. | List owner |
| **D-7 days** | **Hard stop for dietary info.** Send the final dietary list and headcount to the venue. Chase missing dietary replies by phone. | List owner |
| **D-3 days** | Logistics email: address, arrival time, dress code, who's hosting, a direct contact number. | Owners |
| **D-1 day** | Short reminder text from the owner. Confirm the final headcount with the venue. | Owners |
| **D+1 day** | Thank-you note to attendees. Note to no-shows ("sorry we missed you"). Update the sheet. | Owners |
| **D+3 days** | Personal follow-up with next steps. Log the outcomes. | Owners |

### Chase rules

- **Three chases maximum** per guest, spaced about 3 to 4 days apart. After the third, mark `N` and release the seat.
- **Change the angle each time.** Chase 1 is a gentle nudge, chase 2 gives a reason to come (who's confirmed, what the evening is), chase 3 is a clean deadline.
- **Escalate channel with priority.** Priority 5 and Platinum: the relationship owner follows up by call or direct message after chase 1. Priority 1 to 3: email only.
- **Update column K and L the same day** you send a chase, or the highlight formula will lie to you.
- **Ask for a "no" as well as a "yes".** An early decline is worth more than silence, because it frees a seat for wave 3.

## 3. Team working agreements

- **One owner per guest** (column H). No one contacts a guest they don't own without telling the owner.
- **One list owner** edits columns A to E. Everyone else updates only status columns.
- **Check the sheet's version history** weekly. Drive keeps it, and it's your undo.
- **15-minute standup** at each deadline (D-4 weeks, D-3 weeks, D-2 weeks) to review the dashboard and decide on backfill.
- **Keep private details out of the sheet** if it's shared beyond the four of you. Dietary and allergy data is personal data: share the sheet only with the team, and delete the dietary column after the event.

## 4. Questions to answer before you send anything

1. **Dinner date and seat count?** This fixes every date above.
2. **Is the dinner hosted by one company or several?** That changes who signs the invites.
3. **Does each Platinum partner get a guaranteed seat?** If so, mark them priority 5 and exclude them from the 1.3 to 1.5x overbooking.
4. **Are plus-ones allowed?** If not, remove column M.
5. **Which time zone are guests in?** Send invites to land at about 9:00 local time on the send day.

Tell me the date and seat count and I'll fill the Timeline tab with actual dates.