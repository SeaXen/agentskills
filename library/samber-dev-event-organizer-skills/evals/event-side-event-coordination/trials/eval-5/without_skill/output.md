# /parties page and submission form

I couldn't tell your site stack, so the page is plain Markdown and the form is plain HTML. Bracketed items are placeholders for you to fill in.

## Before you publish

1. **Check the Bastion Security sponsorship agreement.** Look for exclusivity, competitor, or "no promotion of competing brands" language. You decided to list everyone, and that is a legitimate call. A top-tier sponsor may still read a listed competitor party as a breach, so find out before the page goes live.
2. **Tell Bastion before launch.** A short heads-up is cheaper than an awkward surprise. Suggested line: *"We're publishing a neutral, open list of every unofficial party during the Summit. Anyone who submits is listed, as submitted, with no endorsement. That includes parties hosted by other vendors in your space."*
3. **Don't treat Vaultrun differently, in either direction.** If you drop or bury them, the page stops being "whoever submits." If you highlight them, you have picked a side. Apply the same inclusion rules to all nine and apply them blindly.
4. **List any Bastion-hosted party the same way.** That keeps the page visibly even-handed.

The page doesn't answer attendees' real question, which is which ones are worth going to. That's intentional, and the page says so up front so nobody reads the list as a recommendation.

---

## Page: `/parties`

**Title:** Unofficial parties during Meridian Dev Summit

**Intro (above the table):**

> Meridian Dev Summit runs [dates] in Barcelona. Around the Summit, other companies and community groups host their own parties.
>
> **These events are not organized, endorsed, or vetted by Meridian Dev Summit.** We list every party that is submitted to us, exactly as the host describes it. A listing is not a recommendation. Check each event's own page for details, capacity, and registration.
>
> Hosting something? [Submit your event](#submit). Spot a mistake? [Tell us](mailto:[comms-address]).
>
> *Last updated: [date, time CEST]*

**Table:**

| Name | Date & time | Venue | Link |
|---|---|---|---|
| [Party name] | [Day, start–end, CEST] | [Venue name, address or neighborhood] | [Event page](https://) |
| Vaultrun After Hours | [Day, start–end, CEST] | [Venue as submitted] | [Event page](https://) |
| … | … | … | … |

Table rules:
- Sort by date and start time, not alphabetically and not by submission order. This is the only neutral ordering that is also useful to attendees.
- Show the host's own wording for name, venue, and time. Don't rewrite descriptions.
- Add no badges, "featured" labels, or sponsor logos.

**Footer note:**

> Parties are run by their hosts. Meridian Dev Summit is not responsible for their content, capacity, or conduct. Our [Code of Conduct](https://) is [expected / encouraged] at every event connected to the Summit. To report a problem at a party, contact [safety contact].

---

## Submission form

**Heading:** Host a party? List it here.

**Helper text:** *We list every event that meets the rules below. Listings are published as submitted, usually within one business day.*

| Field | Type | Required | Notes |
|---|---|---|---|
| Event name | Text, 80 chars | Yes | Shown publicly |
| Hosting organization or group | Text | Yes | Shown publicly if you tick the box below |
| Date | Select: Day 1 / Day 2 / Day 3 / Other (explain) | Yes | |
| Start time | Time (CEST) | Yes | |
| End time | Time (CEST), or "late" | Yes | |
| Venue name | Text | Yes | Shown publicly |
| Venue address or neighborhood | Text | Yes | Shown publicly |
| Event link | URL | Yes | Registration or info page. Must load without login. |
| Open to | Select: Anyone / Registration required / Invite only | Yes | Shown as a short tag next to the link |
| Contact name | Text | Yes | Private |
| Contact email | Email | Yes | Private, used only to confirm and for corrections |
| Confirm | Checkbox | Yes | "I am authorized to submit this event, and the details are accurate." |
| Consent | Checkbox | Yes | "I agree to the event details above being published on the Summit site." |

**Listing rules (shown under the form):**
1. The event takes place during the three days of the Summit, in the Barcelona area.
2. It has a working public link with the date, time, and venue.
3. The submitter is the host or is authorized by them.
4. It follows our Code of Conduct and Spanish law.
5. We may remove or edit a listing if the details are wrong or misleading, if the link is dead or the event is cancelled, if the host asks, or if the event violates the rules above. We never remove a listing because of who the host competes with.

**After submit:**

> Thanks. We'll email you at [address] once the listing is live. To change or cancel it, reply to that email.

**Privacy line:**

> We use your contact details only to confirm and update your listing, and delete them within [30] days after the Summit. Controller: [legal entity]. Contact: [privacy address].

### HTML

```html
<form id="submit" action="[FORM_ENDPOINT]" method="post">
  <h2>Host a party? List it here.</h2>
  <p>We list every event that meets the rules below. Listings are published as submitted, usually within one business day.</p>

  <label>Event name <input name="event_name" maxlength="80" required></label>
  <label>Hosting organization or group <input name="host_org" required></label>

  <label>Date
    <select name="day" required>
      <option value="">Select</option>
      <option>Day 1 – [date]</option>
      <option>Day 2 – [date]</option>
      <option>Day 3 – [date]</option>
      <option>Other (explain in event link page)</option>
    </select>
  </label>
  <label>Start time (CEST) <input type="time" name="start" required></label>
  <label>End time (CEST) <input name="end" placeholder="e.g. 23:00 or late" required></label>

  <label>Venue name <input name="venue_name" required></label>
  <label>Venue address or neighborhood <input name="venue_address" required></label>
  <label>Event link <input type="url" name="url" required></label>

  <label>Open to
    <select name="access" required>
      <option>Anyone</option>
      <option>Registration required</option>
      <option>Invite only</option>
    </select>
  </label>

  <label>Contact name (private) <input name="contact_name" required></label>
  <label>Contact email (private) <input type="email" name="contact_email" required></label>

  <label><input type="checkbox" name="authorized" required> I am authorized to submit this event, and the details are accurate.</label>
  <label><input type="checkbox" name="consent" required> I agree to the event details above being published on the Summit site.</label>

  <!-- Honeypot: hidden from humans, bots fill it -->
  <input name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">

  <button type="submit">Submit event</button>
  <p><small>Listing rules: [link or inline list]. Privacy: [text above].</small></p>
</form>
```

---

## Runbook for your comms lead

**Setup (once, about 30 minutes):**
1. Point `[FORM_ENDPOINT]` at any form tool that writes to a shared spreadsheet and emails the comms lead on each submission.
2. Give the sheet these columns: the form fields, plus `status` (new / listed / removed), `published_at`, and `notes`.
3. Make the public table a copy of the `listed` rows, sorted by date and start time.

**Per submission (about 5 minutes):**
1. Check it against the five listing rules and nothing else.
2. Open the link and confirm it loads and matches the date, time, and venue.
3. Mark it `listed`, update the page and the "Last updated" stamp, and email the host.
4. Reject only on rule failures, and tell the host which rule failed.

**During the week:**
- Sweep all links once each morning and at midday for dead links and cancellations.
- Keep a log of every edit or removal with the reason (the `notes` column).
- Handle attendee questions of the form "which one is good?" with a fixed reply: *"We don't rank or recommend parties. Check each event's page."*

**If a sponsor or host objects to a listing:**
- Answer with the rules, not with a judgment about the host.
- Escalate to you before any removal that isn't one of the rule-based reasons.

---

## Two things to decide

1. **Cap or no cap on submissions?** Nine is manageable. If it grows past about 20, the table gets long. Sorting by date keeps it usable, and I'd still avoid filters.
2. **Submission deadline?** I'd suggest accepting submissions until the first day of the Summit and corrections throughout. Parties that appear mid-week can go through the same form.