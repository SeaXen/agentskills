# ShipIt Conf Discord: what I'd change

Don't clone the hackathon template as-is. It fits a multi-day, team-based event with mentors. ShipIt Conf is a one-day, single-track conference, so most of what made last year work doesn't apply.

## 1. Cut the hackathon channels

| Channel | Verdict | Why |
|---|---|---|
| #team-formation | ❌ Cut | One track, no teams. |
| #ask-mentors | ❌ Cut | No mentors at a conference. |
| #mentors-internal | ❌ Cut | Same reason. It's also a private channel that leaks if the permissions are wrong. |
| #introductions | ✅ Keep | Pre-event warm-up. |
| #random | ✅ Keep | Cheap and harmless. |
| #carpool-search | ⚠️ Keep, rename | Make it `#travel-and-carpool` and cover trains, hotels and arrival times too. Add a safety note: no home addresses in public, use threads per city. |
| #ask-organizers | ✅ Keep | Make it the single help desk. |
| #admin | ✅ Keep, private | Organizers only. |

## 2. Add what a conference needs

1. **#announcements** (read-only): the one source of truth for schedule changes, doors, Wi-Fi and food. Only you two can post.
2. **#live-talk**: one channel for the one track. Use slow mode and one thread per talk for questions. A single track means a single conversation.
3. **#hallway**: breaks, lunch and after-party meetups. This replaces team-formation as the networking channel.
4. **#speakers** (private): logistics and last-minute changes.
5. **#report-an-issue**: how to reach a human privately for code-of-conduct or safety problems. Pin the code of conduct next to it.
6. **#volunteers** (private), if you have volunteers.
7. **#feedback**: opens after the event.

That makes about 10 visible channels for 300 people. Don't go higher. Two moderators can't keep many channels alive.

## 3. Staffing: two people is thin

- **Assign roles for the day.** One person owns Discord, and the other is on the floor. Swap at fixed times.
- **Name an escalation path** for safety reports that doesn't depend on one person being online.
- **Recruit 2–3 volunteer moderators** for event day, with a mod-only channel.
- **Turn on AutoMod and slow mode** for spam and link floods.
- **Add a written rule for the owner:** if you can't staff it, close the channel.

## 4. Access: gate by ticket

You've sold tickets, so use them.

- **Send the invite only to ticket holders**, in the confirmation email.
- **Add a verification step** that grants an Attendee role, plus Speaker and Organizer roles.
- **Don't post the invite publicly.** Otherwise #random becomes a spam target.
- **Use Discord's Welcome Screen and channel topics** as the in-app guide.

## 5. The channels page: don't build a new microsite

- **Two pages will drift.** Your marketing lead already maintains a comms hub on the main event site. Add a "Discord channels" section there. Or, if the microsite is a must, link it from the hub and have one person own both.
- **A fresh microsite has no search authority or traffic.** Ticket holders will find the page through the email and the hub, not through search.
- **Keep private channels off the public page.** Don't list #admin, #mentors-internal or #speakers. List only attendee-facing channels.
- **Write each channel's purpose once**, in the Discord channel topic, and copy it to the page. That keeps the page and the server in sync.

## 6. Timeline

1. **Now:** finalize the channel list, roles and permissions. Check privately that attendee accounts can't see the private channels.
2. **T-3 weeks:** open the server, send invites with the ticket email, and seed #introductions.
3. **T-1 week:** post the schedule and the travel/carpool threads.
4. **Event day:** run the staffing plan from section 3.
5. **T+1 week:** open #feedback, then archive or lock the live channels.

## Questions for you

1. What made last year's server work: mentors, team-formation, or something else? That tells us what to keep.
2. Do you have speakers who'll be around and active on Discord?
3. Do you have any volunteers who could act as mods?