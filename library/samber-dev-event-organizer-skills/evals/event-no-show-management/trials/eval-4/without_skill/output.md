# Kestrel Conf: 09:45 seat release with waitlist SMS

**Verdict:** the idea works, but I'd change two things before you build it. The 09:45 cutoff and the 30-minute claim window will fill fewer seats than you expect. And you can get most of the benefit earlier and more cheaply with a reconfirmation step. The setup below includes both.

I haven't seen your ticketing tool, so I can't confirm its automation features. Steps 1 and 2 check whether it can do what you need.

## Problems to fix first

1. **Day-of release is late.** A waitlister who gets a text at 09:46 has to hear it, travel and queue by 10:15. Many won't make it, and seat 114 goes empty anyway. Day-of release works only for waitlisters who are already nearby or on standby.
2. **Late arrivals lose their seats.** Someone stuck in the badge queue or on a delayed train at 09:45 gets bumped, then shows up angry. Add a grace rule (see step 6).
3. **Do you assign seats?** "Seat 114" only makes sense with a numbered seating chart. If seating is general admission, you're managing a headcount, not seats. The SMS should say "a place is yours", and the release logic should count scanned-in people against 250.
4. **Day 2 is a different problem.** Day 1 no-shows are known. Day 2 should be released from Day 1 scan data, and the release can run the evening before. See step 7.
5. **SMS needs a phone number and consent.** Check that registration collects a mobile number, with an explicit "text me if a seat opens" checkbox. Under GDPR/ePrivacy that opt-in should be separate and specific. A waitlist join form is the right place to ask for it.

## Setup, in order

**Step 1: Check the ticketing tool (30 min)**

Confirm it supports all of these. If any is missing, it needs a small script or a Zapier/Make/n8n bridge.

- Waitlist with a mobile-number field and SMS opt-in
- A timed claim window you can set to a custom duration (not just 24–48h)
- Automation triggered at a specific time, or via API or webhook
- A way to mark a registrant as "checked in" from outside, or to import scans
- A "release ticket" action that frees a seat and triggers the waitlist

**Step 2: Check how scanners write back (30 min)**

This is the likely weak point.

- Do the scanners sync live to the ticketing tool, or only export a CSV at the end?
- If they sync live, you're nearly done. If not, you need a live check-in list at 09:44, not a CSV at noon.
- Test with 5 fake registrants and 2 phones before the event. Send a real SMS and time how long it takes to arrive.

**Step 3: Pre-event reconfirmation (the biggest lever)**

This does more than the 09:45 release. Registration is free, so commitment is low.

- **T-7 days:** email and SMS saying "Confirm you're coming or release your seat. One click."
- **T-2 days:** reminder to anyone who hasn't confirmed.
- **T-1 day, noon:** anyone still unconfirmed is released. Waitlisters get 12 hours to claim, which is long enough to plan travel.
- Also consider **overbooking registration** to about 280–300, using last year's 24% no-show rate as the planning figure. This is the standard fix for free events. Decide your rule for a full room: waitlist or overflow room.

**Step 4: Waitlist rules**

- Collect a mobile number and a "can you come at short notice?" checkbox.
- Order the waitlist by sign-up time, but you could flag "local, can arrive in 30 min" people for the day-of release.
- Set the **claim window to the shortest time that still works**. For the day-of release, 30 minutes is tight. For the T-1 day release, 12 hours is fine.
- The SMS should be short and tell people what to do: "Kestrel Conf: a place opened up for you. Reply YES in the next 30 min to claim it, then come to the main entrance by 10:15 with ID. Reply NO to pass."
- Add an automatic cascade. If the first person doesn't reply, move to the next one, with each step waiting its own claim window.

**Step 5: Scanner hardware and door flow**

- Pre-print or email QR badges to every registrant, and test the scanners with the exact QR format.
- Use at least 4 scanner lanes for 250 people, and open them by 08:30.
- Keep one manual lookup desk for lost QR codes (search by name or email).
- Assign someone to watch the scan count on a screen, so you can see the real number before 09:45.

**Step 6: The 09:45 rule**

- At 09:45, list registered attendees with no scan. Do not release automatically. A person reviews the list for 5 minutes, then confirms.
- Skip anyone who emailed to say they're late, and any speaker or sponsor.
- If you release someone and they arrive later, the desk should have a rule. A good one: admit them if there's room, or put them first in the next overflow queue.
- The automation then releases each seat and texts the top waitlister.
- Keep the 10:15 cutoff, but accept that this will only fill part of the gap.

**Step 7: Day 2**

- At the end of Day 1, export the list of registered people who never scanned.
- Email and SMS them that evening: "Keep your Day 2 seat? Reply YES by 21:00."
- Release non-responders at 21:00 and let the waitlist claim overnight until 08:00.
- Run the 09:45 release again on Day 2, using the same review step.

**Step 8: Dry run (1 hour, a week before)**

- Make 10 test registrants, 3 test waitlisters with real phones, and run the whole flow end to end at your venue.
- Check: scan appears in the ticket tool within seconds, release triggers, SMS arrives, claim reply works, cascade moves to the next person.
- Write down who owns each step on the day. One person owns the release decision.

## What to measure afterwards

- Registered, confirmed, scanned, and the room fill at 10:00 and 11:00 (not just the scan total)
- How many of the 60 expected no-shows you recovered
- Waitlist claim rate and how many claimers actually arrived
- Late arrivals who were bumped

Compare against last year's 24% no-show rate. If the reconfirmation step alone cuts that substantially, the day-of release matters much less.

## Realistic effort

The SMS wiring and automation can be an afternoon, if your tool supports live scan sync and timed claims. The full version (reconfirmation, consent, dry run, Day 2) is more like two to three days spread over the weeks before the event. Start step 1 and step 2 today, because everything else depends on their answers.

Tell me which ticketing tool you use and whether the scanners sync live, and I'll turn this into exact settings or a small script.