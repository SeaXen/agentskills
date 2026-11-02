# DevRel radar for Sundermere: draft, nothing verified

**What this is:** a skeleton of your radar plus the rules for filling it. It is not a verified reading list. Two things blocked verification:

- You have no network access, so I couldn't open any URL.
- The skill's own source list (`references/sources.md`) and its people list were denied by the permissions layer, so I didn't read them. They hold the recorded, dated status of each source.

I won't name feeds, newsletters or podcasts from memory and present them as checked. The skill treats an invented source as the worst failure, because it ruins trust in the rest of the list. So this is a skeleton with every slot's status shown honestly.

**Profile**
- Role: developer advocate.
- Pillars owned: advocacy and community.
- Ecosystem: vector databases and AI data infrastructure.
- Segment: B2B, bottom-up, adopted by application engineers.
- Budget: 45 min/week.
- Mediums: text and audio.
- Date: 2026-10-30.
- Ordering: within each section, highest value per attention-minute first.

**Dropped:** all video (channels, talk recordings, YouTube). You ruled it out, so it is deleted, not parked.

## Budget

| Slot | Minutes/week | Pillar |
|---|---|---|
| Newsletter or blog skim (practice) | 10 | advocacy and community |
| Ecosystem release notes and changelogs | 10 | advocacy (feedback loop) |
| Audio, practice-side | 10 | advocacy and community |
| Annual data read, amortised | ~1 | budget argument |
| Peer community (reserved) | 10 | community |
| Slack (unallocated) | ~4 | |

- Spend about 41 minutes and keep the last 10% as slack.
- Under 60 minutes a week, the skill adds a compressor first. That means one weekly DevRel roundup that stands in for following many vendor blogs.
- Audio that rides on a commute or workout counts half. If you have one, you can fit a second episode.

## Weekly core (ordered by efficiency)

1. **Practice roundup newsletter or hub (text).**
   - Pillar: advocacy and community.
   - Selling: varies (agency, vendor or independent).
   - Status: **unfilled**. Pick it from the skill's source list once you can read it.
2. **Competitor and neighbour release notes (text).**
   - Candidates: the changelogs and GitHub releases for pgvector, Qdrant, Weaviate, Milvus, Chroma and LanceDB.
   - Selling: each is a rival vendor or a rival open-source project.
   - Status: **unverified**. They are well-known projects, but I haven't opened any feed. Verify each repo's latest release date.
   - Why it earns a slot: it shows what application engineers are comparing you against, and it feeds your product-feedback loop.
3. **One practice podcast episode (audio).**
   - Pillar: advocacy and community.
   - Status: **unfilled**. Feed dates are the reliable freshness signal, so check the newest episode date in the feed.
4. **Peer community, reserved slot.**
   - Pillar: community.
   - Status: **unfilled**. This is where new sources surface and where you can ask questions against your own situation.

## Monthly

- Skim the Developer Relations Foundation (dev-rel.org, hosted by the Linux Foundation).
  - Why: the skill calls it the field's only vendor-neutral practice body.
  - Selling: nothing, it's a foundation.
  - Status: **unverified**. The skill recommends finding it through its code-host organisation, not a remembered domain.
- Read the benchmark methodology notes in ANN-benchmarks, a public approximate-nearest-neighbour benchmark project.
  - Selling: nothing, it's independent. Status: **unverified**.

## Annual

- An ecosystem survey or community-health report you can cite in budget conversations.
  - Status: **unfilled**.
  - Quote the edition and year every time. A bare statistic ages invisibly.
- DevRelCon.
  - Per the skill, its organiser changed: the agency Hoopy wound down in 2026 and handed it to Major League Hacking.
  - Status: **organiser change taken from the skill text, event dates unverified**.
  - You can't confirm a CFP date or a ticket price offline.

## Bench (verified substitutes)

Empty. Nothing here counts as a substitute until it's verified.

## Totals

- Estimated weekly minutes: about 41, against a 45-minute budget.
- Sections: weekly core 4, monthly 2, annual 2, bench 0.
- Verified-active entries: **0**.
- Pillar coverage: **no**. Advocacy and community each have only unfilled or unverified slots, so the skill's pass bar isn't met yet.
- Dropped: video, because you ruled it out entirely.

## What I need from you

1. **Q4:** are you catching up before a specific moment, or building a standing habit? Catching up promotes the long-form slots, like a second podcast episode, over newsletters.
2. **Q9:** do you need to speak, sponsor or host events this year? If yes, I'd add one CFP target and one event to attend or sponsor, each with a confirmed date and organiser.
3. **Permission:** allow reading the two reference files in the skill's `references/` folder. Then I can fill the unfilled slots with recorded statuses from the skill's last audit and say plainly that I couldn't re-verify them.

## Manual check once you're online (about 10 minutes)

1. Open each URL.
2. Find the newest dated item. Use the feed for podcasts.
3. Confirm who runs it now.
4. Classify it:
   - **Active:** a dated item within about 3 months.
   - **Stale:** newest item older than about 6 months.
   - **Dead:** the domain is parked, for sale, or resolves to an unrelated business.
   - **Unverified:** a 403, a 5xx or a consent wall, which never counts as dead.

Rerun the radar every quarter.