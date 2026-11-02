Three things about your setup change the risk profile here, and each one has gaps your three items don't cover yet:

- **Work laptop** ≠ a dedicated demo profile. It has your real accounts, real history, real hostname.
- **Whole screen**, not a window/app share — everything on that machine is potentially on the projector and in the recording, not just your demo app.
- **Recorded to YouTube** — anything that leaks isn't a bad five minutes, it's permanent and searchable.

And the audience is security professionals — the group most likely to actually look for a token in an autocomplete dropdown or try a URL you put on screen.

Here's what to close before you go on stage, roughly in order of how likely it is to bite you:

## Notifications (Slack alone isn't the full surface)

- Quit — don't just background — email, calendar, Teams/Zoom chat, any other IM. A quit app can't pop a toast; a backgrounded one still can.
- Turn off calendar/reminder popups specifically — DND doesn't always suppress these, and a reminder firing mid-demo names a meeting, a person, or a deal.
- Silence phone *and* watch if either mirrors notifications from your work accounts — a wrist buzz still gets caught on camera or spoken about.
- Corporate agents: VPN client, MDM/EDR, cloud-sync (OneDrive/Drive), auto-update — all of these throw modal dialogs at the worst moment and are easy to forget because they're not "apps you use."

## Since it's your work laptop, not a clean profile

- Open a fresh browser window/profile for the demo: no saved passwords, no autofill, no bookmarks bar, no signed-in personal or work mail/calendar tabs sitting in another tab.
- Clear shell history and editor recent-files/project-switcher lists — both surface real project names and paths in a dropdown you didn't mean to open.
- Set a custom shell prompt with no username, hostname, or company domain in it — the default prompt is a small biography on every command.
- If the demo repo is cloned from your real work repo, `git log`/`git blame` will show your real name, email, and possibly real ticket/customer references in commit messages — use a clean clone or a repo with no inherited history.
- `.env` and any config shown on screen: placeholders only (`API_KEY=demo_key_123`), even for a local/offline stack. A real key sitting unused is still a real key on the recording.

## Because you're sharing the whole screen, not a window

- Desktop, dock/taskbar, menu bar, wallpaper, and app-switcher are all fair game the moment you alt-tab or something steals focus — walk through what each one currently shows.
- If the AV setup allows it, ask whether you can share an application/window instead of the full screen — it's the single cheapest risk reduction available and worth one email to the organizers before you assume it's not possible.
- If it genuinely has to be full-screen (common with hardware AV capture over HDMI), rehearse the demo assuming every window you might touch — including a stray email client icon bounce — is visible.

## Because it's a security-conference audience and it's permanent on YouTube

- If any part of the demo hits a live, reachable endpoint, expect someone to try it the moment the URL is on screen. Prefer a local/offline stack or a sandbox tenant with read-only, least-privilege credentials over anything real reachable from the internet.
- Don't just rename customers — re-check emails, internal URLs, bucket/project names, ticket numbers, and any colleague's name left in a code comment. "Anonymized" isn't "synthetic"; one leftover real identifier re-identifies the rest.
- Confirm no embargoed or unreleased feature is reachable from any menu, settings panel, or admin screen the demo might expose, even by accident.
- Do a full pass through every screen state the demo can show — error states, empty states, autocomplete dropdowns, the next slide — not just the happy path. Hidden screens leak the same as visible ones when a click goes wrong.

## Panic button, since this is one-shot and recorded

- Have a "Demo paused" full-screen slide ready on one keystroke, and know your stop-sharing shortcut on their specific AV/conferencing setup before you're on stage, not during a failure.
- One rehearsed recovery line for "something breaks" (name it out loud once before the talk) — improvising this live is where speakers lose the most time and composure.
- If a colleague is in the room, have them hold a working clone of the repo/deck as backup for the failure mode nothing else survives: your laptop or the mirroring itself dying.

Do this pass **the day before**, not in the green room — a rushed run-through at the venue is exactly when a leftover tab or a live credential gets missed.