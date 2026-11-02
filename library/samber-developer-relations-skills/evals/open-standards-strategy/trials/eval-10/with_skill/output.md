Two judgment calls shaped these drafts, flagging them since you didn't specify either: I read "Streamvane 2 drops half of them" as *v2 formally adopting six of your twelve undocumented fields into the core spec and cutting the other six* — that's the fix the skill's own failure-mode list prescribes for self-inflicted "embrace-extend" drift ("namespace them, document them, propose the useful ones upstream"), and it gives the announcement something real to say instead of just an apology. Second, a flat 60-day wall for 40 implementations that depend on undocumented behavior is the exact setup the skill warns about ("an exit that strands implementers... a replacement has to be shipped and proven before the old version is withdrawn, not alongside it") — I kept your 60-day framing but added an extension escape hatch and an optional compatibility shim, both marked so you can delete them if you don't intend to build either. For Calderwood, the seven-asset check comes out close to even (you hold IP rights, first-mover, and the just-shipped v2; they hold scale, complements, and the brand association integrators are already forming) — that rules out a straight fight for the "real Streamvane" title and points at the framework's prescribed counter instead: a conformance mark plus a truce offer, priced from strength, not retreat.

---

## Document A — Sunset announcement

**Streamvane 2 is here. Here's what changes, and why we're finally writing it all down.**

*Published [date] · Halcyon Grid Engineering*

Three years ago we published Streamvane. Since then, about 40 implementations have shipped against it, and along the way our own implementation grew roughly a dozen fields that never made it into the spec. Customers asked for something, we shipped it fast, and — this is the part we should have caught sooner — nobody wrote it down. If you've been reading our undocumented behavior instead of the spec text to get your integration working, that's on us, not on you.

Streamvane 2 is our fix for that. It's not just a version bump; it's the spec catching up to what implementations actually needed, and drawing an honest line around the rest.

**What's moving into the spec, unchanged.** Six of the twelve fields we'd been shipping quietly are now first-class, documented parts of Streamvane 2:

| Field | Status in v2 | What you need to do |
|---|---|---|
| `[example_field_a]` | Promoted to core spec, §[n] | Nothing — same name, same semantics |
| `[example_field_b]` | Promoted to core spec, §[n] | Nothing — same name, same semantics |
| *(four more — see [full migration guide](#))* | Promoted to core spec | Nothing |

If you were already sending these, you're done. Bump your client version and move on.

**What's going away, and why.** The other six were either superseded by a v2 primitive, never adopted outside our own SDKs, or were workarounds for a gap v2 closes properly:

| Field | Why it's cut | Replace with |
|---|---|---|
| `[example_field_c]` | Superseded by `[v2_primitive]`, which covers the same case without the edge-case bugs `[example_field_c]` had | `[v2_primitive]` — see the [migration guide](#) for a mapping table |
| `[example_field_d]` | Never picked up outside our own tooling; keeping it in the spec would mean certifying a field only we use | Drop it. If you're one of the few relying on it, tell us — see below |
| *(four more — see [full migration guide](#))* | | |

**The timeline.** Streamvane 2 support ships in our cloud today, alongside v1. From today:

- **Day 0 – Day 60 ([date] – November 23, 2026):** both versions run side by side. Migrate at your own pace.
- **Day 60:** v1 support turns off in our cloud, and the v1 spec repository moves to read-only and gets archived. Existing v1 payloads will start failing validation after this date.

Sixty days is enough for most integrations — for six of the twelve fields, it's a version bump and nothing else. It is not enough for everyone, and we'd rather hear from you than have you go dark. **If you need more time, open an issue with your use case and current field usage, and we'll work out a longer runway with you individually.** We are not going to let a calendar date break a production integration that reached out in good faith.

*[Optional — keep only if you're actually building this]* We're also shipping a small compatibility shim that translates the six removed fields into their v2 equivalents at the network edge, so you can point your existing v1 client at it and get a working integration on day one, then migrate the client itself on your own schedule. [Link, when ready.]

**Why we're doing this now, and not differently.** We could have kept the dozen fields forever and called that Streamvane. We didn't, because a spec that's 40% "whatever we happened to ship" isn't a spec anyone else can safely build against — including us, next time we want to change something. Fixing that now, while we still control the migration, is cheaper than fixing it after someone else's dialect becomes the thing everyone actually implements.

Questions, migration help, or "I need more than 60 days": [support channel / issue tracker link].

---

## Document B — Response to Calderwood

**Subject: Streamvane 2, and getting "compatible" back to meaning one thing**

*[Addressed to Calderwood's integration/standards contact — also suitable to publish as an open post]*

We've watched Streamvane grow past anything we expected when we published it three years ago, and a good share of that is your adoption — your integrations are a real part of why "Streamvane" is a name people reach for instead of building a bespoke format per vendor. That's the outcome a spec is supposed to produce, and we don't take it for granted.

We also want to name something plainly, because pretending not to notice it doesn't help either of us: the extra fields you've added on top of the spec are increasingly what integrators mean when they say "Streamvane," rather than what the spec text says. We recognize the pattern, because we did the same thing to our own users first — a dozen fields, never written down, shipped because customers asked and we moved fast. We're in the middle of cleaning that up right now (announcement attached). The difference is scale: when we did it, it fragmented our own implementation. At your size, it risks quietly becoming the de facto spec for everyone, which puts every other implementer — including us — in the position of reverse-engineering your client instead of reading a document.

We'd rather fix the mechanism than argue about whose dialect is more "real." Three concrete things, alongside today's Streamvane 2 release:

1. **Spec text for unknown fields.** Streamvane 2 formally defines how a conforming client handles fields it doesn't recognize — ignore and pass through, never fail closed. That means your extensions, or anyone else's, stop being able to silently redefine what a baseline client has to support to be "compatible." Extensions become additive by construction, not by convention.
2. **A conformance suite and a versioned mark, self-service and free, live at launch.** Any implementation — yours included — can run it and publish the result to a public registry. That gives integrators something to check other than "whoever's biggest." We're not gating it behind a fee or a review queue; the goal is implementer count, not revenue.
3. **An upstream path for your fields.** If integrators are already depending on your extensions, some of them probably belong in the spec, the same way six of our own undocumented fields just did. We'll take a proposal from you through the same process we used on ourselves — named fields, a rationale, and a namespace until they're promoted.

One more thing, and we're saying it now rather than after a fight neither of us would enjoy funding: given your reach into this ecosystem, we're open to moving Streamvane's governance to a neutral foundation-hosted venue rather than a repo we alone control, with you seated at the table from the start. We're proposing this from a position we're actively investing in — v2 ships today, the conformance mark ships with it — not as a concession because your dialect is winning. We'd rather have that conversation now, while it's a design discussion, than in a year, when it's a migration.

We'd like fifteen minutes with whoever owns your Streamvane integration to talk through the extension-namespace proposal and the conformance suite before we publish either publicly. [Proposed date] works on our side — let us know what works on yours.

[Name] · [Title] · Halcyon Grid