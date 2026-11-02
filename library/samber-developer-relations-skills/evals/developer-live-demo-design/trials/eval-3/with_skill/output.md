**Day 1 action:** get a second, dedicated laptop. Wipe it or buy new. This becomes the only machine Vaneer Sync's demo build ever touches. Nothing else runs on it — no personal accounts, no MDM screen-capture agent unless IT grants a written exception, no cloud sync. That machine is what makes the rest of this plan possible.

## Tier decision

Claim: **"A change made in Vaneer or in the CRM appears in the other, within seconds, in both directions, no re-entry."**

That claim needs live behaviour, not a picture — kills tier 4 (screenshot). It also needs the audience able to believe it isn't faked, so a plain narrated screencast (tier 3) alone won't fully carry a keynote reveal, though it's your fallback.

A "real" CRM (Salesforce/HubSpot/etc.) over the venue network fails legal's rule outright — any live call to a real third-party service is data leaving the laptop before keynote. So tier 1 is off the table too.

Recommendation: **tier 2** — fully local, offline stack. Engineer builds a local, generic-looking mock CRM (seeded, synthetic, on localhost). Zero network dependency means zero embargo risk: nothing to intercept, log, or leak, because nothing leaves the loopback interface. Compliance cost is lowest of any tier for exactly this reason (sources-and-thresholds.md: tier 2 needs no security review a live tenant would trigger).

One exception: segment 2 (see below) runs as a **tier-0 moment inside the tier-2 stack** — live-typed, not scripted — because the claim being tested there is liveness itself ("is that real?"). Skill explicitly allows promoting to tier 0 for that reason, paid for with a golden path, a rehearsed switch, and a tier-3 clip standing by.

Fallback tier: 3 — locally recorded clips. Kept **only** on the demo laptop and the buddy's laptop. No USB key (a lost stick is a leak vector legal did not sign off on), no cloud drive.

## Confirm with legal before you build (blocking)

1. A recording made and stored on the demo laptop, never uploaded, staying physically in the building — compliant with "nothing leaves before keynote"? Get this in writing; the whole fallback plan depends on the answer being yes.
2. Rehearsing in front of the engineer in your own office: fine. Rehearsing at a coworking space, hotel lobby, or on a flight where a stranger can see the screen: treat as equivalent to "leaving the building" even though nothing left physically.
3. Does the corporate laptop's MDM run a screen-capture/AI-notetaker agent (Recall-style)? Needs an explicit exception or use a non-MDM machine.

## 3-week build plan

**Week 1 — build.** You: own claim + segments + legal loop. Engineer: owns the stack.

1. **`git init`** empty demo repo, fresh identity, no history from the real product repo.
2. Engineer builds local mock CRM: generic branding (not a real vendor's actual UI — trademark risk), contacts/deals/pipeline, REST endpoint matching whatever interface Vaneer Sync's real CRM connector already expects. Bind `127.0.0.1` only.
3. Map a real-looking hostname (`crm.demo.local`) to `127.0.0.1` via hosts file, so the URL bar doesn't say "localhost" on stage.
4. Generate synthetic fixture data (faker-style). Hand-check company/contact names against the real customer list — random generators do collide with real names often enough to matter here.
5. Seed 3 checkpoint states as fixture files, tag each with **`demo-checkpoints.sh save 1 baseline`** / `save 2 ...` / `save 3 ...`.
6. Engineer writes **`./demo reset`** — idempotent, restores both Vaneer's local instance and the mock CRM to segment-1 state, target under 5s.
7. Record the two tier-3 fallback clips on the demo laptop. Save locally only — **disable iCloud Photos / Google Drive / OneDrive / Dropbox sync** on that machine before recording anything.
8. Harden the laptop: fresh OS account, **Wi-Fi and Bluetooth off**, custom shell prompt (no hostname/path), fresh browser profile with exactly 2 tabs, `.env` placeholders only.

**Week 2 — rehearse + verify.**

9. Segment-by-segment timing. Cut whatever runs long; budget each segment at ~2x its rehearsed time.
10. Enter each segment directly from its checkpoint, skipping the ones before it — this is what catches a segment secretly depending on a prior one's live output.
11. Drill the top 3 risks (below) until each switch lands under 20s.
12. Walk legal through the live build, in the building, on the demo laptop, no recording sent anywhere. Get sign-off before Week 3.
13. First clean cold run, full end-to-end, network off. Log it.
14. Identify and brief the buddy — colleague, front row, second demo-only laptop, holding the repo clone + deck + clips.

**Week 3 — freeze + travel + stage.**

15. Repeat cold runs until **3 consecutive clean ones** logged (skill baseline: two could be luck, three exposes a flaky step).
16. One full run at actual venue resolution, once the room's available.
17. **Freeze the build.** No further changes to the demo path after this point without a full re-verify.
18. Travel with the demo laptop as hand luggage, controlled at all times — for the embargo's purposes, it now *is* the building.
19. On-site tech rehearsal: real projector, real mirroring, real mic, one full cold run before the room opens.
20. Keynote day: pre-flight checklist in the green room. Wi-Fi stays off. Buddy in position. Go.

## Runbook

```
Demo:          Vaneer Sync — keynote reveal
Claim:         A change made in Vaneer or the CRM appears in the other within
               seconds, both directions, no manual re-entry.
Venue/format:  Stage — user conference keynote
Budget:        6 min  /  Measured: <fill after first cold run>
Tier:          2, fully local/offline; segment 2 runs live-typed (tier-0 moment)
Fallback tier: 3 — clips stored on demo laptop + buddy laptop only, never uploaded
Network:       Offline. Wi-Fi/Bluetooth off for the full 3-week window, not just on stage.
Data:          Synthetic fixtures only, checked against the real customer list.
Buddy:         <name> — clone of repo, deck, clips, on a second demo-only laptop.
Owner:         <you> + <engineer>
Last verified: <date of last clean cold run before travel> on <build/commit>
Re-verify:     after any change to the sync path, and again the keynote morning
```

**Segments**

| # | Proves | Enter from | Runs | Budget | Droppable | Fallback |
|---|---|---|---|---|---|---|
| 1 | Vaneer edit reaches CRM, no export step | tag `demo/step-1` | scripted paste, 1 field edit | 45s | no | `01-outbound.mp4` |
| 2 | CRM edit reaches Vaneer, live | tag `demo/step-2` | live-typed, audience picks 1 of 3 pre-approved fields | 60s | no | `02-inbound.mp4`, same golden path |
| 3 | Simultaneous edits don't collide | tag `demo/step-3` | scripted near-simultaneous edit both sides | 45s | yes | `03-noconflict.png` |

Total scripted run ≈2.5 min against a 6 min budget — under half (skill baseline), leaves room for intro/outro and one full recovery.

Segment 2's "audience picks a field" is the golden path: bounded to 3 pre-vetted safe fields (e.g. deal amount, deal stage, company name), never open-ended. Rehearsed range, not rehearsed value.

**Reset:** **`./demo reset`** — one command, idempotent, rehearsed cold.
**Pre-provisioned:** both local services started and warm before walking on stage. Never install/build on stage.

**Top 3 risks, drilled**

1. Any pre-keynote data egress (cloud sync, screen-capture agent, stray Wi-Fi join) → machine hardening above; this is the risk that matters most given legal's ask.
2. Segment 2 live-typed edit freezes or errors → one repair attempt, ~20s (skill baseline), then switch to `02-inbound.mp4`.
3. Checkpoint/reset leaves wrong state → named checkpoints, `./demo reset` rehearsed from cold, never from a machine that already ran the demo twice.

**Recovery lines**

- Segment 2 hiccup: "That's a new one — let's watch it do the same trick, recorded an hour ago." Switch to clip 02.
- Any error: "Not going to debug this at you — here's the same run." Switch to fallback.
- Overrun: "I'll skip the conflict case — it's in the deep-dive session right after this."

**Pre-flight (green room, before walking out)**

```
[ ] Wi-Fi and Bluetooth off, confirmed off
[ ] Cloud sync (iCloud/Drive/OneDrive/Dropbox) confirmed disabled
[ ] Demo profile only — no personal mail/chat/calendar/browser
[ ] ./demo reset run once; demo left at segment 1
[ ] Both fallback clips one keystroke away, playing locally
[ ] Buddy in position with clone of repo, deck, clips
[ ] Terminal 24pt+, high-contrast theme, block cursor
[ ] Nothing embargoed beyond Vaneer Sync itself visible on any screen, menu, or tooltip
[ ] .env holds placeholders only
[ ] Safe screen ready on a known hotkey; recovery lines rehearsed out loud
```

**Rehearsal log** — fill in as Week 2–3 runs happen. Needs 3 consecutive clean cold runs, one full offline run, one at venue resolution, before this is done.

Next: get the second laptop and confirm the 3 legal questions above — everything else in Week 1 depends on both.