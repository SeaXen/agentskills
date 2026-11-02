Both items trigger named failure modes in this skill (teardown-as-proof on the sandbox claim, rebuild-the-artefact on the layout) — scoped the roadmap items to close the gap without importing those mistakes. Draft below, ready to paste into the roadmap.

---

# Roadmap draft: Windlass docs vs Beacontree — 2 items

Observed 2026-09-20 · Peer set: Beacontree (single competitor, user-supplied) · **Peer set of one — see caveat below**

## What changes because of this

1. Beacontree's in-browser sandbox is a real, worth-closing gap, but the "signups went up a lot" claim is one line from a podcast, not data. Roadmap the sandbox with a validation step in front of the build step, not as a single close-by-EOQ item.
2. The three-column layout is a rendering of a deeper practice (live code samples wired to a runnable backend), not a CSS/design task. Fold it into the sandbox initiative instead of shipping it as a standalone redesign — otherwise it lands as a page skin with a dead code panel.

---

## Item 1 — Interactive "run in browser" sandbox on Windlass docs

**Gap:** Beacontree ships a runnable sandbox on every docs page. Windlass ships none. *(not observable from outside which pages, exactly — see validation step 1.)*

**Why this isn't a straight "close, ship it" row:** the only evidence is a podcast soundbite claiming signups rose after launch — no number, no time window, no control for what else shipped that quarter. That's a hypothesis a teardown produced, not a validated pattern. Treat it as a lead, not a spec.

**Roadmap entry — split into two phases:**

| Phase | Action | Owner | Target date |
|---|---|---|---|
| 1. Validate | Pull the podcast episode, get the actual number and time window cited. Run a timed pass through Beacontree's own quickstart (~1 hr) to see what "sandbox" means in practice: fully client-side, or a spun-up container; which languages; latency. Cross-check Windlass's own funnel for drop-off on docs pages pre-signup — if that friction doesn't show up in our own data, the Beacontree anecdote doesn't transfer here regardless of whether it's true for them. | DX lead | 2026-10-03 (1 week) |
| 2. Build | Scoped to the getting-started / quickstart page only, not "every page" — cost of a full-site runnable sandbox (ephemeral execution, per-language runtimes, sandboxing/security) is genuinely unknowable from outside and is very unlikely to be a low-cost item. Expand page coverage only after Phase 1 confirms the friction point and Phase 2's MVP shows movement. | Eng (Docs infra) + DX lead | Scope + estimate by 2026-10-17; build date set after that |

**Verdict:** close, conditional — gate the "ship everywhere by end of quarter" ask behind Phase 1. If "end of quarter" means 2026-09-30 (10 days out), that's not enough runway for even a scoped MVP of a runnable sandbox — confirm whether you mean Q3 (Sep 30) or Q4 (Dec 31) before this goes on a public roadmap with a date attached.

---

## Item 2 — Three-column docs layout (nav / content / code panel)

**Gap:** Beacontree's docs run nav, content and a live code panel side by side. Windlass's layout is *(not stated — confirm current layout before scoping)*.

**Why this isn't its own roadmap line:** a three-column layout with a code panel is almost certainly the same runnable-sandbox engine from Item 1, surfaced inline instead of as a separate widget. Roadmapping it as a design/frontend task risks shipping the visual frame with an empty or dead code panel — the visible surface (layout) sits on the same backend practice as Item 1, not on CSS.

**Roadmap entry:**

| Action | Owner | Target date |
|---|---|---|
| Merge into Item 1's initiative as "interactive docs experience" — do not schedule as a standalone redesign. Once Phase 1/2 above confirm the sandbox engine and page scope, the three-column shell is a content-layout task on top of it (nav + content already exist; the code panel is the sandbox's existing output surface reflowed inline). | Docs + DX lead | Scoped alongside Item 1, Phase 2 |
| Before committing design time: 1–2 hr audit of whether Beacontree's docs actually cover all four modes (tutorial / how-to / reference / explanation) per feature, or whether the three-column layout is dressing up reference-only content. A pretty layout over thin content won't move signups; thin content over a plain layout might still be the real gap. | Docs | 2026-10-03 |

**Verdict:** close, re-scoped — folded into Item 1, not a separate line item.

---

## Method and limits

- Based on two unvalidated, user-relayed observations, not a fielded benchmark: no URLs, no dated screenshots, no independent confirmation of either claim.
- Peer set of one (Beacontree only). One competitor's practice can be a strong lead but shouldn't set the whole docs roadmap — worth naming one or two more peers before this becomes the standing justification for the spend.
- The "signups went up" figure has no source better than a podcast mention — labelled here as **unvalidated, single source**, not as evidence, per this skill's rule against teardown-as-proof.
- Both build-cost estimates are marked unknown on purpose — an outside read can't size backend sandbox infrastructure, and inventing a number here would be worse than leaving it blank.
- What would change this: the podcast claim checks out with a real number attached → strengthens Item 1's priority. Beacontree's docs turn out reference-only under the mode audit → the layout copy (Item 2) stops being worth it on its own.