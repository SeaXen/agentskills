Next action: swap the Google Meet tech checks for checks on the licensed broadcast platform. Do this before you send any more invites.

## 1. Move tech checks to the broadcast platform

- Meet proves mic, camera and bandwidth. It does not prove the speaker can join the green room, share a screen, hear the producer, or see their slides on the platform.
- Run the check on the real platform, in the real speaker role, in the browser they will use on the day.
- The "one less account" saving is mostly false. Speakers need the platform link on the day anyway. Most broadcast platforms use guest links, so check whether yours needs an account.
- Keep Meet only as a backup channel if you want it.
- Check pass list, per speaker:
  1. Joins from the speaker link and enters the green room.
  2. Mic, camera and headphones work. Echo test passes.
  3. Screen share works at the platform's resolution and frame rate.
  4. Producer cues and countdown are visible to the speaker.
  5. Speaker knows how to rejoin after a drop.
- Time-box it to 20 to 30 minutes. Re-book anyone who fails.

## 2. The two staging-API demos

Highest risk in the event. Treat each as its own project.

1. **Freeze staging.** No deploys, migrations or data resets from rehearsal through the event, except planned ones. Name one owner for staging uptime on the day.
2. **Network path.** Check IP allowlists, VPN or corporate firewall, CORS, auth tokens and rate limits from each speaker's home or office network. Test from there, not from your office.
3. **Credentials.** Give each demo a dedicated staging account with seeded data and a token that expires after the event. Nothing real on screen.
4. **Fallback recording.** Record each demo segment as a short screencast. Load them in the platform's media player so the producer can roll one in about 20 seconds. This works around a dead API, a dead Wi-Fi and a dead laptop.
5. **Failure rule.** One repair attempt, about 20 seconds. Then switch to the recording and say a short pre-written line ("staging is being slow, here is the run from this morning"). Rehearse the switch, not just the demo.
6. **Restore points.** Make each segment startable alone, with no dependence on the previous segment's live output. Give each speaker one reset command.
7. **Screen legibility.** Terminal at 24pt or larger. Notifications off, fresh browser profile, shell history cleared. Check how it looks after platform video compression.
8. **Pass test.** Run the full demo through the platform's screen share. Do it three times in a row without a manual repair. Do one run with the fallback switch.
9. **Buddy.** Give each demo speaker a backup person with the repo, the deck and the recordings, ready to take over.

## 3. Auckland speaker at 03:00

Do not default to 03:00. Offer these, best first.

1. **Different time for her.** Check the platform in her evening or morning. Move the staff member's time before hers. The producer can cover an odd hour. The speaker should not.
2. **Pre-record her talk.** Record it with her, edit it, and play it in her session slot. Run Q&A live or through async questions. Ask her which she prefers.
3. **Her session slot.** Check what local time her live session lands on. If it is the middle of her night, pre-recording is probably the right fix for the event itself, not just the check.
4. **Only if she chooses the 03:00 slot.** Make the check shorter, and still run it on the platform.

If she demos live, add the latency from Auckland to staging as a test item.

**Clock changes.** NZ is on daylight time (UTC+13). The EU changes clocks on 25 Oct and the US on 1 Nov, so some offsets move before the event. Put every invite and the run of show in UTC with local times beside it, and re-check anyone near a clock-change boundary.

## 4. Everything else for all 14 speakers

1. **Speaker brief (one page, sent this week).** Include the platform link, the date and time in UTC and local, the contact for the day, and the slide deadline and format. Add the hard time limit and who cuts at zero, plus the recording and release terms.
2. **Run of show.** One producer owns it. It lists each speaker's call time, which is 30 minutes before their slot, with a countdown plan. Add a backchannel outside the platform, such as Slack or Signal, so a speaker can reach the producer when the platform drops.
3. **Speaker hardware.** Ask for a wired connection if possible, otherwise sitting near the router. Add a phone hotspot as backup, a headset, a second device logged in as a spare, and a quiet room.
4. **Content.** Slides in a shared file as backup. Ask for captions or a transcript plan, large type, and high contrast. Get recording consent in writing.
5. **Q&A and after.** Name a moderator and a question-screening method. Agree the replay timeline. Send thank-you notes and a follow-up with the recording.

## 5. Order of work

1. **Today:** cancel or reschedule the Meet slots and re-invite on the platform. Message the Auckland speaker with options 1 and 2 above.
2. **This week:** staging freeze, demo accounts, recordings of the two demos, and the speaker brief out.
3. **Next week:** tech checks, the demo pass test (three cold runs plus a fallback switch), and a final run of show.

Time estimate: re-booking checks takes about 1 hour. The demo hardening takes about 1 to 2 days of work for each of the two demo speakers.

## Open questions

- What is the event date? Clock changes may affect the plan.
- What is the platform? Does it need accounts, and can it roll pre-recorded video?
- Does the Auckland speaker demo, and what local time is her live session?

Next: answer the date and platform, then I draft the speaker brief.