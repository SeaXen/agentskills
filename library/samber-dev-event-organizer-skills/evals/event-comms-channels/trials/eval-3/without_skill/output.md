# Sanity check: TechFest Krakow comms plan

**Verdict:** ⚠️ Don't build it as written. The channel split and the Telegram mirror will mostly work with edits. The DM-for-urgent rule will fail on the day.

**Next action:** replace the DM rule with a broadcast path (issue 1 below). It's the only blocker.

## 🔴 Blockers

**1. Urgent messages by DM**
- Whoever is on duty can't DM hundreds of people by hand. A bot that mass-DMs trips Discord's anti-spam and can get the bot or account flagged.
- Many attendees have server DMs off. Telegram-only attendees never see a Discord DM.
- Deciding who counts as "affected" under pressure leads to misses. A room change or a safety issue needs everyone in that room, not a guessed list.
- DMs leave no shared record. Two writers will send different wording, and nobody can check what was said.
- Safety incidents (evacuation, medical, venue closure) must be broadcast. Targeted DMs are the wrong tool.

**Fix:** use a tiered path.
- **Urgent:** a role ping in a read-only `#announcements` channel, mirrored to Telegram within a minute. On-site screens or PA cover safety incidents.
- **Group-specific urgent** (a speaker's room moved): ping the role in that group's channel, not individual DMs.
- **Individual cases:** DM only for a handful of people, such as a speaker whose slot moved.

**2. Channels split by audience type, but messages depend on what people attend**
- A student can be remote and in a workshop. A sponsor rep can be a speaker. Overlapping groups mean duplicated posts or people missing the one that matters.
- Your four tracks have no channel. A "Track B, room change" notice has no obvious home.
- There is no global channel, so venue, schedule, and safety notices have nowhere to live.
- `#talks-only` is ambiguous. It could mean a channel for talk attendees or a channel where only talks are discussed.

## 🟠 Should fix

**3. Telegram mirror of "all announcements"**
- Segmentation is lost. Telegram users get everything in one stream, so half your audience gets the noisy version.
- A group lets members see and message each other, and exposes usernames and sometimes phone numbers. That is a GDPR concern in Poland. Use a **broadcast channel**, not a group.
- The mirror needs one source of truth. Bots lag, and edits or deletions don't propagate. Discord markdown, mentions, and embeds render badly on Telegram. A correction on Discord that never reaches Telegram is worse than no mirror.
- The mirror must carry urgent messages too. The DM plan skips Telegram entirely.
- "About half" is an assumption. Check it in the registration form before you design around it.

**4. Four volunteer writers have no operating model**
- Two days of coverage need a duty rota, a named backup, and a handoff note.
- Without an approval rule, any writer can post anything. Without templates, wording drifts.
- Name one duty lead per shift and make every urgent post go through two people.

**5. Private and public mixing**
- `#speakers` and `#sponsors` must be role-gated and hidden from attendees. Speaker logistics and sponsor chatter shouldn't be visible to 800 people.
- Ticket verification, a code of conduct, and moderators are missing. At 800 people you need at least 3–4 moderators across the two days.

## 🟢 Suggested structure

**Discord**
- `#announcements` (read-only, everyone). Urgent posts get a role ping.
- `#help` and `#lost-and-found` for logistics questions.
- Four track channels (`#track-1` to `#track-4`) for room and time changes and discussion.
- `#workshops` for workshop attendees, with seat and material notices.
- `#remote` for stream links and remote Q&A.
- `#students` for student-specific content.
- `#speakers` and `#sponsors`, private.
- Roles from ticket type plus self-picked tracks, so pings reach the right people.
- Drop or rename `#talks-only` unless you define it.

**Telegram**
- One broadcast channel for `#announcements`, with urgent posts marked 🔴.
- Optional second channel for schedule changes per track if people ask for it.
- No open group chat unless you can moderate it.

**Publishing**
- Write once in a single tool and publish to both. Don't let writers post to each channel by hand.
- Post a correction in both places within the same minute.

## Questions before you build

1. Is the venue wifi reliable enough for Discord to be the primary urgent channel, or do you have an on-site screen/PA path?
2. Is the "half on Telegram" figure measured, or a guess?
3. Are announcements bilingual (Polish and English)? That doubles the writer workload.
4. Can attendees pick several roles, such as student and remote and a workshop?
5. Who owns safety incidents, the writers or the venue/security team?

I can turn the revised structure into a channel-by-channel spec with role permissions and message templates once you've answered.