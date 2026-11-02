# GoNorth social: what to change

I read the skill and both references. I couldn't ask the interview questions, so the answer rests on stated assumptions. They're listed at the end.

**Scope.** I don't change the marketing plan's weight, dates or targets, and I don't redo your positioning or voice. Post-event clips and articles go to `event-content-repurposing`.

## 1. Account control: one owner, one request path

Your sponsor request got lost for a structural reason. Three people hold the password and requests land in five inboxes.

1. **Name one account owner per account.** Only that person posts. Pick the person with the most weekly hours (Q7). Nobody else needs the password.
2. **Rotate the password now.** The two other password-holders lose access. If the platform offers per-person roles, use those instead of sharing a login. Check current platform mechanics; don't assume.
3. **Create one request path.** Use a shared inbox or a single channel, such as `social@<your-domain>`. Everyone who needs a post, from speakers and sponsors to the five co-organizers, goes through it.
4. **Publish the path.**
   - Put it in the speaker confirmation email.
   - Put it in the sponsor onboarding form.
   - Co-organizers forward anything they receive to it instead of handling it themselves.
5. **State a turnaround and a cut-off.** Example: "answered within X days; nothing new is accepted after Y." This stops the chasing. Set X and Y yourselves. They are your choice, not a benchmark.
6. **Add a doors-eve rule.** Put "check the request path" into the run of show for the day before doors. That is the exact moment last edition's request died.
7. **State what doesn't get posted.** At the community pole you have no neutrality policy to enforce, so don't import CNCF's allow-list. Keep one line on what you decline, for example unpublished agenda items.

## 2. Platforms: stop cross-posting and adapt for each audience

Your audience answer meets the promotion condition. LinkedIn reaches the managers who approve travel budgets. Mastodon reaches the practitioners who want the talks. Those are two different audiences with different reasons to attend. Move from home-plus-mirror to **two natively adapted** accounts. Identical text works for neither group. This is a judged ranking, not a measured one.

| | LinkedIn (managers) | Mastodon (practitioners) |
|---|---|---|
| Angle | "Why your team should be there": what the day gives their engineers, and why it justifies travel | The talk's real claim, with no sales framing |
| Format | Longer text, one image | Short, reply-friendly. Threads for the agenda release |
| Strongest phases | Announcement, CFP open, early-bird close, final push | Speaker reveals, agenda release, live |
| Sponsor angle | Sponsor thank-yous land well here | Optional |

- **One message on both.** Both carry the same positioning sentence from `event-positioning`. Rewrite the format and the angle, never the promise.
- **Hours.** This option costs more hours than cross-posting. If your owner has under about two hours a week (Q7), the two accounts will drift into disuse. A stale account subtracts credibility. In that case drop to a single home platform, and decide which one your actual goal needs.
- **Don't open more accounts.** Delete any third-platform idea. Abandoned accounts hurt more than missing ones.

### Hashtags (decide before the first post)
- **Edition tag:** one dedicated campaign tag for GoNorth this edition. Fix it before the first post. Changing it mid-campaign splits the archive permanently. This is your measurement tag.
- **Topic or community tag:** one broad Go-community tag for reach.
- **Optional:** a track-level tag.
- **Reporting.** Never report the community tag's volume as your reach. Most of it belongs to other people.
- **Mastodon.** Hashtags are the main discovery route there, so check current behaviour before settling the set.

## 3. Sponsor handle: use what you already collect

Your onboarding form already asks for a handle, so the sponsor thank-you costs only minutes. Add it as a rung, and make three tweaks:

1. **Ask for two fields.** Replace the single "handle" with a LinkedIn page and a Mastodon handle, both optional. One field can't serve two platforms.
2. **Frame it as optional goodwill.** DevOpsDays' own wording is "very optional". Present it as a thank-you, not a deliverable.
3. **Check each sponsor agreement first.** If it contracts a social mention, the post becomes a fulfilment item owned by `event-sponsor-fulfillment`, and missing it is a breach. Check before posting, because a public post can't be taken back.

Thank-you template: "Thanks to [sponsor] for backing GoNorth this year – [one true, specific sentence about what their support pays for]."

## 4. Amplification and the five organizers

1. **Build the kit once.** Do it before the first speaker confirms, with these contents:
   - speaker cards
   - a short copy block with the positioning sentence
   - the hashtags, labelled by purpose
   - the tracked link
   - one or two venue images
   - a "don't announce before the schedule is public" line
2. **Send the per-speaker ask at confirmation.** It rides on an email already going out.
   - Attach the card.
   - Name the date your own post goes out.
   - Make the opt-out explicit.
   - Include the request-path address.
3. **Ask each of the five organizers** whether they'll post from a personal account. Record who agreed, and never assume it. Give them the same kit.
4. **Add the partner push later.** Add it only once the marketing plan weights partner channels and a deal already exists.

## 5. Tracked links and measurement

Create these before launch, because they can't be added retroactively:

- one tracked link per platform
- one per organizer's personal account

The marketing plan reads them. Personal-versus-event-page clicks on the same post will show you which reaches more people in your own audience. I set no numeric engagement target. Judge the channel on whether the dated posts shipped and whether the tracked links moved.

## 6. Live coverage and the day itself

- **Default:** the single recap, which is cheap and leaves a usable archive.
- **Promote to a roving poster** as soon as a volunteer is named in the run of show. This person must not be an on-duty organizer that day.
- **Photo rules.** Settle the badge-carried photo opt-out (`event-accessibility-inclusion`) and the speaker recording and quoting rules before the day.
- **Archive.** Keep one shared folder, named per session. It is the handover to `event-content-repurposing`.
- **Full live desk.** Only if a sponsor contracts live coverage or you have a remote audience.

## Posts mapped to phases

I can't fix the dates without the marketing plan's calendar. The skeleton, per phase:

- **Announcement.** Positioning sentence, date, city, link, posted natively on each platform.
- **CFP open and close.** Topics wanted, support offered, then a link-only countdown for the close.
- **Speaker reveals.** One card per speaker, not a carousel. Reveals are the posts with a built-in second audience.
- **Agenda release.** The shape of the day plus two anchor talks.
- **Early-bird close.** A countdown against the real cutoff.
- **Final push.** Practical detail, plus the sponsor thank-you round.
- **Live and wrap.** The recap, the thank-yous, then the archive handover.

Don't invent a posts-per-week number. Pin every post to a real campaign date. Re-check any batched or scheduled post whenever the plan's dates move.

## Order of work

1. **Today.** Rotate the password and name the owner or owners.
2. **This week.** Set up the request inbox, add it to the confirmation email and onboarding form, and split the sponsor handle field in two.
3. **Before the next post.** Fix the edition hashtag and create the tracked links.
4. **Before the first speaker confirms.** Build the kit and the ask email.
5. **Before sponsors' posts go out.** Check the sponsor agreements for contracted mentions.

## What I assumed

- **Governance.** Community-run, so no neutrality policy applies.
- **Marketing plan.** I assumed it exists and I've seen none of it. If it doesn't, stop and run `event-marketing-plan` first.
- **Opt-out.** I assumed you want promotion. Strange Loop-style "no marketing" would change everything, but 700 attendees and a sponsor program suggest otherwise.
- **Unknowns that would change the answer:**
  - doors date and runway
  - one edition versus a compounding account
  - owner hours per week
  - whether sponsor agreements contract mentions
  - your badge photo opt-out

If you answer those, I'll turn this into a dated calendar.