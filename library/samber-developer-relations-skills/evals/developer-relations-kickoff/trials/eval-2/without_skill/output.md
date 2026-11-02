**Next action:** draft 1.0 changelog entry + breaking-change list today. Send to VP Eng for sign-off first — nothing else can move before that clears.

**Window:** 26 days to 2026-10-15. At 6h/week ceiling, ~22h total budget. Tight, not impossible.

## Gate check — is 1.0 ready to announce

Don't push wide comms until these hold:

1. Quickstart rewrite done (currently 60%) — this IS the "1.0 onboarding works" claim. Announcing before it's live means new arrivals hit stale docs on day one.
2. Breaking-change list exists (pre-1.0 → 1.0). Unknown to me — need from you or platform team.
3. Headline features for 1.0 named — also unknown to me.

⚠️ Items 2-3 block writing real copy. Everything below assumes placeholders until you fill those in.

## Priority stack (fits ~22h)

1. **Finish quickstart rewrite** — 6-10h. Gating item, do first.
2. **Changelog/release-notes entry** — 3h. Structure: Added/Changed/Breaking/Fixed, semver framing, stability promise ("1.0 = SemVer starts now, breaking changes require major bump going forward").
3. **GitHub Release page** — 1h. Reuse changelog, add highlights + contributor thanks. This is your durable owned asset — GitHub Releases count as owned, no extra infra needed.
4. **Docs "what 1.0 means" page** — 2h. Stability commitment, versioning guidance, breaking-change migration steps if any.
5. **Discord announcement + pinned FAQ thread** — 1h.

Total: 13-17h core. Leaves 5-9h buffer for platform-team merge delay on docs PRs — budget that delay now, don't discover it on day 25.

**If time remains:** one rented-channel push (r/rust or Show HN), 2h prep + launch-day monitoring. Matches "major update = full campaign" — but only after the 5 above ship. Single one-time push, not a channel to maintain.

## Channels — stay inside what you own

Owned surfaces: docs.kestrelqueue.dev, Discord. No blog, no email list, no social presence listed. Don't invent a new channel for one release — that's a maintenance debt with no owner after Oct 15.

- GitHub Release = primary announcement, compounding asset (matches your stated preference over one-off wins).
- Docs page = durable reference.
- Discord = real-time push to existing 1,400 members.
- Hosted control plane (private beta): one line max, link to waitlist, no more. Different buyer (org, post-1.0), different motion. Mixing it into core OSS 1.0 messaging dilutes both. Needs VP sign-off either way since it's release-train-adjacent.

## VP Eng sign-off — do this early, not day-of

Send draft changelog + breaking-change list as soon as drafted (target: day 5-7 of window). Sign-off review time is not devrel hours but it eats calendar days — a late draft means a rushed or missed sign-off.

## Measurement — work inside the blind spot, don't build new tooling

No signup attribution, no eng support to fix that now. Cheapest option:

- Snapshot weekly active docs readers + Discord message volume the week before Oct 15.
- Snapshot again the week after.
- Log delta in session log. Directional signal, not a funnel — good enough given constraints.

## Open questions (need answers from you, not guessable)

1. What's the actual breaking-change list, pre-1.0 → 1.0?
2. What are the 1.0 headline features/fixes worth naming in the release notes?

## Out of scope for this check-in

User conference 2027 — open decision, not time-critical against Oct 15. Revisit after release ships.

**Next:** finish quickstart rewrite, or answer the two open questions above — whichever unblocks faster.