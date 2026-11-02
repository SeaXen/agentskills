Two quick framing calls I made, both flagged inline below so you can override them:

- **Sunset post**: I don't have your actual dozen field names or your data-retention policy for the six being dropped, so those are bracketed placeholders — everything else is ready to publish as-is.
- **Calderwood post**: I did *not* name Calderwood. Publicly naming a much larger vendor in a spec dispute usually backfires (you look defensive, you hand them the attention, and if you're wrong about their intent it's hard to walk back). Instead the post reasserts spec conformance as the differentiator and proposes a governance fix that neutralizes the "de facto standard" problem without a fight. If you want it sharper and want Calderwood named, say so and I'll rewrite it — but ship this version first if you're unsure.

---

# 1. Sunset announcement

**Suggested title:** Sunsetting Streamvane v1: what's changing and your 60-day migration window
**Suggested channels:** blog (primary), changelog, email to every v1 API key holder, pinned issue on the v1 repo

---

> **TL;DR**
> We're retiring our Streamvane v1 implementation in favor of Streamvane 2. You have until **Monday, November 23, 2026** (60 days) to move your integration. Six of our old v1-only fields are now part of the official Streamvane 2 spec — no work needed there beyond upgrading. Six others are being dropped. After November 23, v1 API calls in our cloud will stop working and the v1 repo moves to read-only/archived. Full field-by-field breakdown below.

## Why we're doing this

Streamvane has been the spec for [what your product does] since Halcyon Grid published it three years ago, and it's now implemented by roughly 40 teams across the ecosystem. Ours has always tracked the spec closely — with one exception: over the last three years, customers asked for things the spec didn't cover yet, and we shipped a dozen extension fields on top of v1 to meet real requests. We never wrote them down as a formal extension; they just accumulated.

Streamvane 2 changes that calculus. Halcyon Grid's new release folds in several capabilities the ecosystem clearly needed — including, encouragingly, half of what we'd already built as one-off extensions. That's validation that those fields solved a real problem, not just our problem. The other half didn't make it into the spec, and we don't want to keep maintaining a v1 implementation with undocumented, non-standard behavior once v2 is out. So we're doing a full cutover, not a field-by-field patch.

## What happens to the fields we added

| Field | Status in Streamvane 2 | What you need to do |
|---|---|---|
| `[custom_field_1]` | ✅ Now a native v2 field (`[v2_equivalent_name]`) | Rename in your integration; behavior is unchanged |
| `[custom_field_2]` | ✅ Now a native v2 field (`[v2_equivalent_name]`) | Rename in your integration; behavior is unchanged |
| `[custom_field_3]` | ✅ Now a native v2 field (`[v2_equivalent_name]`) | Rename in your integration; behavior is unchanged |
| `[custom_field_4]` | ❌ Not in v2, no successor | [Export existing values via `X` / stop relying on this before Nov 23] |
| `[custom_field_5]` | ❌ Not in v2, no successor | [Export existing values via `X` / stop relying on this before Nov 23] |
| `[custom_field_6]` | ❌ Not in v2, no successor | [Export existing values via `X` / stop relying on this before Nov 23] |

*(Full 12-field table with real names goes in the published version — this is the pattern to fill in.)*

⚠️ If you don't use any of the fields above, you still need to migrate — this is a full v1 → v2 cutover, not just a field deprecation.

## What happens to your existing data

[State your actual policy here — the two common options are: (a) historical values in dropped fields remain readable via export/API through a fixed date even after v1 shuts off, or (b) they stop being returned entirely on the sunset date. Pick one and say so explicitly; this is the detail customers will ask about first.]

## Timeline

| Date | What happens |
|---|---|
| **Sep 24, 2026** | This announcement. v2 is available now — you can start migrating today. |
| **Sep 24 – Nov 23** | Both v1 and v2 work. Migrate at your own pace. |
| **Nov 9, 2026** (2 weeks out) | Final reminder to any account still sending v1 traffic. |
| **Nov 23, 2026** | v1 endpoints in our cloud return `410 Gone`. The v1 repo is archived (read-only) on GitHub. |

## How to migrate

1. Read the [v2 migration guide](#) — covers the six renamed fields and any response-shape changes.
2. Upgrade to SDK version `[X.Y.Z]` or later, which targets v2 by default.
3. Point staging traffic at the v2 endpoint and diff responses against your current integration.
4. Cut production over. v1 and v2 run in parallel until Nov 23, so there's no hard switchover moment required on your end.

## Need more time or hitting a blocker?

This is a hard external deadline because it's tied to when we can safely stop maintaining two parallel implementations — but if six weeks genuinely isn't enough for your integration, talk to us before Nov 23, not after. Reach us at [support channel/email] or open an issue on the v1 repo before it's archived.

---

# 2. Response to the "Calderwood is becoming Streamvane" problem

**Suggested title:** Streamvane isn't any one implementation's to define
**Suggested channels:** blog (primary); consider cross-posting to wherever Halcyon Grid or the Streamvane working group has a presence, so it reads as a contribution to the spec community rather than a shot at a competitor

---

## The ecosystem is growing — that's the good part

Streamvane now has something like 40 independent implementations. More vendors building extensions on top of the spec is a healthy sign: it means the spec solved a real problem well enough that people want to push past its edges. We've done exactly that ourselves — for three years we ran a dozen undocumented extension fields on our own v1 implementation because customers needed things the spec hadn't caught up to yet.

We just retired half of those fields, not because they failed, but because Streamvane 2 absorbed them into the actual spec. That's the outcome we want *every* useful extension to have eventually: not permanent vendor-specific behavior, but a path into the spec itself, so "Streamvane" keeps meaning the same thing no matter whose implementation you're pointed at. [See our v1 → v2 migration notes â†’](#)

## Why this matters right now

As more vendors ship their own extensions, "Streamvane" risks quietly splitting into "whatever the biggest implementation does" rather than what Halcyon Grid actually publishes. That's bad for integrators specifically: it means the code you write against one vendor's Streamvane implementation may silently stop working against another's, which is the exact interoperability problem the spec existed to prevent in the first place.

We don't think that's any single vendor's fault — it's what happens by default when a spec has no lightweight process for turning a useful extension into a standard one. Extensions fill real gaps faster than a spec body can move. The fix isn't asking vendors to stop innovating ahead of the spec; it's giving that innovation a route back in.

## What we're proposing

1. **We're asking Halcyon Grid to stand up a formal extension-track process** — a lightweight RFC path so any implementer's field or behavior can be proposed, reviewed, and either adopted into the spec or explicitly marked as non-standard. Streamvane 2 already proved this works: several of our own extensions made it in through exactly this kind of validation.
2. **We're committing to submit every extension we ship from here forward** through that track, rather than letting it live as undocumented vendor-specific behavior the way our old fields did.
3. **We're publishing our conformance test results against the official Streamvane 2 spec** [link], and we'd like every implementation — ours included — to be checkable against the same suite, so "Streamvane-compatible" means something verifiable rather than something you find out by trial and error in production.

## To other implementers

If you're building Streamvane extensions of your own, we'd genuinely like to see them go through a shared process rather than each of us defining "Streamvane" a little differently. We're raising this with Halcyon Grid directly and we'll share what we hear back.

The spec is what makes 40 different implementations interchangeable in the first place. That's worth protecting on purpose, not by default.