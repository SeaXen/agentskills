**Recommendation:** Host the spec as a new specification project under the **Linux Foundation's Joint Development Foundation (JDF)**, with an **RF (royalty-free) patent policy** — perpetual, irrevocable, worldwide, non-assertion, scoped to conforming implementations.

## Why not the other five options

- **Own repo (Caldmere's)** — dead. Tarn already vetoed this in writing. No further debate needed.
- **W3C** — wrong body. W3C's entire process (horizontal review, browser-vendor consensus, TAG sign-off) exists to protect the web platform. Nobody here ships a browser feature. You'd pay full process cost for zero relevant scrutiny.
- **IETF** — wrong shape. IETF wants rough consensus from a broad, open community building internet-wide protocols. A 3-vendor manifest format doesn't need or want that many hands on the wheel — you'd cede control you currently have for a legitimacy you don't need.
- **ISO number** — wrong tool for the job you have. ISO's main payoff for a private spec is procurement/regulatory recognition. Nobody here sells to government, so that payoff is close to zero, and ISO's timeline (12–36 months via a national body or fast-track submitter) blows past a Thursday-driven, engineers-already-staffed effort.
- **OASIS** — legitimate, not wrong, just heavier than needed. OASIS Technical Committees work fine at 3 members and its IPR policy is flexible (RF, RAND, non-assert, selectable at charter time). But chartering a TC takes longer and carries more procedural overhead than JDF for the same IP outcome. Keep it in your back pocket as the fallback if JDF's governance model doesn't fit once you're in it.

## Why JDF specifically

- Purpose-built for exactly this: 2–5 companies, no legacy patent portfolio, want a neutral home fast. Turnkey legal templates (modeled on the Open Web Foundation Agreement) mean no drafting an IP policy from scratch.
- Neutral by construction — satisfies Tarn's objection outright, since the spec lives under LF, not under any founding company's org.
- Fast to stand up: days to weeks, not months. Matches your timeline.
- Gives the two committed engineers a durable, named governance seat (steering committee), not just contributor status — matches a 2-year staffing commitment better than an informal repo would.

## Patent terms to give the lawyer

- **Royalty-free (RF)**, not RAND. You hold no patents and have never licensed IP — RAND buys you nothing to monetize and only adds adoption friction for what's meant to be a universal interchange format.
- Perpetual, irrevocable, worldwide grant of necessary claims, scoped to implementations of the spec.
- Standard defensive-suspension clause (grant terminates against anyone who sues a member over the spec) — protects all three of you symmetrically.
- Delivered via JDF's standard Specification Agreement: each founding company signs once, covering both copyright contribution and the patent grant.

## Governance to propose to the other two vendors

1. Steering committee: one seat per founding company, consensus voting (unanimity among founders, simple majority once the group grows).
2. Spec name and trademark held by the JDF project, not by any member — closes the door on any future "whose spec is this really" dispute.
3. Contribution path: engineers commit via the JDF CLA, which bundles the RF patent grant — no separate side agreements needed per contributor.

## Non-blocking, do independently of the body decision

- Register an IANA provisional media type for the manifest format (e.g. `application/vnd.caldmere-lineage+json`). Cheap, doesn't require IETF standards-track process, and is useful regardless of which body hosts the spec.
- Revisit ISO later, not now: if the spec matures and a future customer or regulatory driver needs the badge, submit the stable v1 via a fast-track path (the way OASIS's ODF or Ecma's C#/OOXML specs later became ISO standards). Nothing about choosing JDF today forecloses that.

**One-line answer for the lawyer:** Linux Foundation's Joint Development Foundation; royalty-free, perpetual, irrevocable, worldwide patent non-assert scoped to the spec.