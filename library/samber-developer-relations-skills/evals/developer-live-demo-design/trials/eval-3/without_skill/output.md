## Big picture

Don't fake the feature — isolate the environment. Build a small, realistic-looking mock CRM as the "other side," wire your *real* Vaneer Sync engine against it through the same connector interface it'll use in production, and run the entire thing offline on a dedicated, locked-down machine that never touches cloud storage or a public remote until the keynote starts. That gets you a demo that's actually true (real sync code, real two-way behavior) while keeping every embargo risk (leaked recording, synced screenshot, pushed commit, curious support ticket at a real CRM vendor) off the table by construction, not by discipline alone.

Three weeks with one engineer is enough if you scope the demo narrowly: one entity type, one clean story arc, one memorable "prove it's real" beat.

---

## 1. What the "real-looking CRM" should actually be

Don't connect to a real third-party CRM (Salesforce, HubSpot, etc.) for this demo. Reasons:
- Conference wifi becomes a single point of failure.
- API calls against a real vendor's infra pre-announcement can leave traces you don't control (their logs, their support team, their rate limits).
- You don't need it — the audience can't tell the difference between a real CRM and a well-seeded mock one on a projector.

Instead: build a small local web app that looks like a CRM (contact list, record detail pane, activity feed), seeded with realistic but fake data (fake companies, fake names — never real customer data). Point the actual Vaneer Sync connector at it through the exact same interface it'll use against the real thing in production. The sync logic on stage is 100% real; only the target system is a stand-in. This is the standard pattern for embargoed keynote demos at companies your size and bigger — nobody in the audience needs to know it's not Salesforce.

## 2. Containment — nothing leaves the laptop

Treat this as an infosec problem, not a discipline problem. Defaults leak things; don't rely on remembering not to.

- Use a **dedicated demo machine**, not your daily laptop — fresh OS install, no personal cloud accounts logged in.
- **Disable iCloud Drive / OneDrive / Dropbox / Google Drive sync** machine-wide, not just on the demo folder. One default save location is enough to silently sync a screenshot.
- **Disable Spotlight/Recall-style OS screen-indexing features** and any AI tool with screen access (Claude for Chrome, Copilot, OS "AI" screen search) on that machine.
- **Turn off crash reporting and telemetry** for the OS and every app in the demo stack — crash reporters routinely upload a screenshot of the crashed window.
- **Keep the git repo local only.** No `git push` to any remote — even a private one — until after the keynote starts. If the engineer needs to collaborate remotely, pair over voice with screen-share off, or accept a private org-owned repo only after checking with legal whether that counts as "leaving the building" under their policy — that's their call, not an engineering one.
- No cloud-recording tools for rehearsals (Zoom cloud recording, Loom). If you screen-record a rehearsal, save it locally on the same locked-down machine or an **encrypted external drive** you keep on your person.
- Run the whole demo **offline** — mock CRM and sync engine both local processes, zero external network calls. This also kills "conference wifi died" as a failure mode, which is a bonus, not just a security win.
- Physical: demo laptop in carry-on, never left unattended, short screen-lock timeout.
- ⚠️ You're currently discussing this feature with a cloud AI assistant. If you use Claude Code or any AI coding tool for the actual build, check your org's data-retention/training settings before you feed it real Vaneer Sync code — worth a two-minute check with whoever owns that contract, not an assumption.
- Confirm the engineer is under the same embargo/NDA obligation as everyone else with early access — flag it to legal explicitly rather than assuming it's implied.

## 3. Three-week plan (one engineer)

- **Week 1** — Build the mock CRM: seeded fixture data, a UI clean enough to read on a projector (big fonts, no localhost:3000 URL bar, no dev-tool chrome visible). Wire the real sync connector against it for one entity type. Get one-way sync working in each direction independently.
- **Week 2** — Get true two-way sync working with the actual story arc: edit side A → appears on side B live; edit side B → flows back to A. Add a live conflict-resolution moment (same field edited on both sides near-simultaneously, resolved on stage) — that's the beat a canned video can't fake, and it's what makes the audience believe it's real. Build a **one-command reset script** that restores both sides to the known seed state, so you can re-run the demo dozens of times without manual cleanup.
- **Week 3** — Rehearse the real 6-minute script daily, offline, on the actual demo machine, ideally in a room shaped like the venue. Build a **fallback**: a locally-stored recording of a perfect run, triggerable by a single keystroke to go full-screen if live sync breaks. Run a full dry run with the actual presenter, not just the engineer — typing speed and click order under stage nerves differ from an engineer's rehearsal.

## 4. Demo script shape (6 minutes)

- 0:00–0:30 — frame the problem, both systems on screen side by side.
- 0:30–2:00 — create a record on the CRM side, show it land on the Vaneer side live.
- 2:00–3:30 — edit it back on the CRM side, show it flow the other way — this is the "two-way" proof.
- 3:30–5:00 — the conflict-resolution beat.
- 5:00–6:00 — one summary slide, land the takeaway line.

Keep every beat to a single clean action — one click, one keystroke. Multi-step UI flows are where live demos die on stage.

## 5. Pre-keynote risk checklist

- ⚠️ Notifications/screensaver/OS update prompts firing mid-demo — disable all of them, disable sleep.
- ⚠️ Seed data drifting after repeated rehearsals — run the reset script before every rehearsal and again right before walking on stage.
- ⚠️ "Is this a real CRM?" from the audience — give the presenter a plain, prepared one-liner ("this is a demo environment we built to show the sync live rather than a canned video") rather than leaving it to improvisation.
- ⚠️ Engineer isn't in the room during the keynote — the presenter alone must be able to run the reset script and trigger the fallback video without help.