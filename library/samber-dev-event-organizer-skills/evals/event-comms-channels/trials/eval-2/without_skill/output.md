# DataDays Porto status page: plan review and severity definitions

## Verdict

The plan is sound except for one blocking flaw and one design mistake. Fix those two things and the rest is good.

1. ❌ **Blocking: don't host the status page on the registration server.** If that server goes down or gets swamped, the page that should announce it goes down too.
2. ⚠️ **Design: don't post daily logistics to the status page.** It weakens the page's one job. Details are in the second section below.
3. ✅ The three severity levels, the subscribe form and the public post-mortems are all good ideas.

## Hosting: put the page somewhere independent

**Why it fails.** The registration site is the thing most likely to be under strain on conference days: check-in lookups, QR scans and attendees refreshing on mobile. A status page sharing that server, database, network or DNS goes dark in exactly the incidents it exists for. You already know this from SRE work: the status page must not share a failure domain with what it reports on.

**What to do instead** (cheapest first):

- **Hosted status service with a free tier.** Instatus, Better Stack, Atlassian Statuspage and similar services give you components, subscribers and incident updates with no server to run. Check the current free-tier limits for subscriber counts and email sending before you commit.
- **Static page on separate infrastructure.** Use Cloudflare Pages, GitHub Pages or similar. Build it from a small JSON or Markdown file, and put it on a different provider and, ideally, a different DNS provider than the registration site. It's cheap and fast, but you must build the subscribe flow yourself.

**Also check:**

- **Subdomain.** Use something like `status.<your-domain>`, and make sure its DNS records don't depend on the registration host.
- **Subscribe form.** Don't point it at the registration server either. Use the hosted service's built-in form, or a separate email provider.
- **Alternative channels.** Attendees on venue Wi-Fi may not reach a web page during a network incident. Mirror major-outage notices to at least one channel that works over mobile data: email, SMS, or a messaging channel (Telegram or WhatsApp broadcast).
- **Operators.** Name who can post an update and who is the backup. A status page only one person can edit fails when that person is busy fixing the incident. Give those people access *before* the event, and test that they can post from a phone.
- **Rehearsal.** Run a fake incident the week before. Post it, receive the subscriber email, and resolve it.

## Daily logistics: keep them off the status page

Keeping the page "active" is the wrong goal. An empty page that says "all systems operational" is what a healthy status page looks like.

**Problems with mixing the two:**

- **Alert fatigue.** Subscribers who get a notification about lunch will mute or unsubscribe, and then miss the shuttle outage.
- **Lost signal.** If every post triggers an email, attendees can't tell "the livestream is down" from "badge desk opens at 8:00".
- **Muddied history.** Uptime history and incident metrics mean less when routine posts are mixed in.
- **Post-mortem scope.** Your "post-mortem after any incident" promise works best when the page contains only incidents.

**What to do instead:**

1. Run a separate **"Today at DataDays"** page or feed for lunch, badge-desk hours, room changes and similar notes. Put it on the main conference site or in the event app.
2. Offer it as a **separate opt-in**, for example a "daily briefing" checkbox on the same form. Status subscribers then get only incident notifications by default.
3. Link the two pages to each other.
4. Optionally, show a one-line "Today's info → link" banner on the status page. This is a link, not a post, so it creates no notification.

If you still want logistics on the status page, make them a clearly separate non-incident type that never notifies subscribers by default.

## Other review notes

- **GDPR.** The form collects personal data from EU residents. Use double opt-in, a one-line privacy notice, a working unsubscribe link, and a retention rule (for example, delete the list some weeks after the event).
- **Components.** List what attendees actually depend on. A suggested set:
  - Registration and ticketing
  - Check-in and badge printing
  - Livestream
  - Venue Wi-Fi
  - Shuttle (metro to venue)
  - Event app or schedule
- **Public post-mortems.** They're a good idea. Make them blameless. Review each one before publishing for attendee personal data, security-sensitive details such as credentials, keys, hostnames or unpatched weaknesses, and anything covered by a vendor or venue contract.
- **Livestream viewers** are remote and have no other way to hear from you, so give them a visible link to the page on the stream player.

## Severity definitions

Severity is set **per component**, by **impact on attendees**, not by technical cause. The page-level status is the worst component.

### Operational 🟢

**Definition:** the component works as intended for essentially everyone.

- No incident is open.
- Normal variance doesn't count. A single user's problem, or a brief blip that fixed itself in under 5 minutes with no one affected, stays at operational.

### Degraded 🟠

**Definition:** the component works, but attendees are noticeably slowed down, inconvenienced or partially affected, and a workaround exists.

Use degraded when **any** of these is true:

- Some attendees are affected, or some functions fail, but most people can still complete the task.
- The service is slow enough to cause queues or complaints, but still works.
- A fallback exists and staff or attendees can use it right now.

Event examples:

| Component | Degraded example |
|---|---|
| Registration | Confirmation emails delayed, or ticket lookup is slow |
| Check-in / badges | One of several badge printers is down; queue over about 10 minutes |
| Livestream | Reduced quality, or occasional buffering, or one language or one room's stream is down |
| Wi-Fi | Slow or patchy in one area; works elsewhere |
| Shuttle | Running late (for example 15+ minutes between buses) or reduced frequency |
| Event app | Schedule is stale or search is broken, but the PDF or printed schedule is correct |

### Major outage 🔴

**Definition:** the component is unusable for most or all attendees, or a critical function fails with no workable fallback.

Use major outage when **any** of these is true:

- Most users can't complete the main task.
- A time-critical function fails during its window, for example the livestream is down during a keynote, or check-in is stopped during the morning rush.
- There is a safety or access risk, for example the shuttle isn't running at all at arrival time.
- Data is being lost or exposed (also follow your security incident process).

Event examples:

| Component | Major outage example |
|---|---|
| Registration | Site is down, or tickets can't be retrieved or checked |
| Check-in / badges | No badges can be printed or scanned; no manual fallback active |
| Livestream | Main track stream is down or showing the wrong content |
| Wi-Fi | Venue-wide failure |
| Shuttle | No service at all |
| Event app | Unavailable and no alternate schedule published |

### Rules for choosing a level

1. **When in doubt, pick the higher level.** You can lower it later; underclaiming costs trust.
2. **Time matters.** Raise the level if the failure hits a high-stakes moment (opening keynote, first-morning check-in, last shuttle).
3. **A working workaround lowers severity only if attendees know about it.** Post the workaround in the incident update.
4. **Downgrade only after verification**, not after a fix is deployed. Move from major to degraded when the core function is back, and to operational only after 15 minutes of stable service (adjust this window to the component).

### Response targets

| | Degraded | Major outage |
|---|---|---|
| First public post | Within 15 min of confirmation | Within 10 min of confirmation |
| Update cadence | Every 30 min (or at each change) | Every 15 min (or at each change), even if just "still investigating" |
| Resolved post | When stable (see rule 4) | When stable, with a short summary of what attendees should do next |
| Post-mortem | Only if the incident lasted over 60 min or hit a keynote or main track | Always |

Adjust the numbers to what your team can realistically staff. A target you miss during the event damages trust more than a slower one you hit.

### Update template

Use the same four fields every time, so updates are quick to write and easy to scan:

- **Status:** Investigating / Identified / Monitoring / Resolved
- **Impact:** who is affected and how, in plain words
- **What to do:** workaround or where to go (for example, "Use the manual badge desk at Hall B")
- **Next update:** a clock time

### Post-mortem commitments

- **Timing.** Publish within 5 business days. If an incident happens on day 2, the post-mortem will appear after the event, so say that in the incident's resolved post.
- **Contents.** Include:
  - Summary and impact (who was affected, for how long)
  - Timeline
  - Root cause
  - What went well and what didn't
  - Action items with owners
- **Tone.** Blameless, with no individual names unless the person agrees.
- **Review before publishing.** Check for personal data and security-sensitive details, as noted above.

## Next steps

1. Pick the hosting option above and set up the status page on separate infrastructure. About 1–2 hours with a hosted service.
2. Move logistics to a separate page or feed with its own opt-in.
3. Create the components and paste in these definitions as the page's "How we classify incidents" text.
4. Add the GDPR notice and double opt-in to the subscribe form.
5. Run a rehearsal incident about a week before the event.

If you tell me the stack for the registration site and your preferred hosting route, I can draft the page copy and the subscribe-form text next.