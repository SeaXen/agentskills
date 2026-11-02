Here's where I landed, and why it isn't a URL list.

## I can't hand you verified sponsorship URLs right now — and fabricating them would be worse than not answering

Step 4 of this skill is explicit: *"Verify every funding link resolves before it enters the list... Never present a funding link from model memory; funding pages 404 and maintainers leave programs."* That rule exists precisely for this situation — six real payments, going out today, off a link nobody re-checked. This session has no working network access (WebSearch, WebFetch, and `gh api`/`curl` against GitHub all came back denied), so I have no way to actually resolve `quillnet`, `stashline`, `mortar-rs`, `pinchpoint`, `tessera-log`, or `bolthole` to a live `.github/FUNDING.yml`, Sponsors page, or Open Collective link this turn. I don't recognize these six well enough from memory to trust a guessed owner/URL with real money, and guessing is exactly the failure mode this skill is designed to prevent — a stale or wrong link fails silently, and you'd only find out when the card doesn't post correctly or the money lands on a namesquatter.

## What to run yourself, per maintainer (2 minutes each, in this order — Step 4)

1. Open the repo → check for the **Sponsor** button (top right). It's driven by `.github/FUNDING.yml` on the default branch.
2. No button → check the **owner's** `.github` repo (`github.com/<owner>/.github`) for an org-level `FUNDING.yml` fallback.
3. Still nothing → check the package registry page (npm/crates.io/PyPI, whichever hosts it) for a funding field.
4. Still nothing → that's one of your two no-button cases. Confirmed no destination exists — see below, don't invent one.

## Tier to pick, once you have a live link (Step 6)

You're paying maintainers of things in your stack — that's a **supply-chain mandate**, and this skill is specific about it: *"the smallest recurring amount is usually correct across many projects; coverage is the goal, not prominence."* So for each of the four with a real Sponsors page: **pick the lowest recurring tier on their published ladder**, not a headline tier. Only go custom/higher if one of these six is genuinely load-bearing and hard to replace for you — if that's true for any of them, say which and I'll help build the case for an above-ladder amount instead of the floor tier.

If the actual intent behind this payout is reach/visibility rather than dependency coverage, that flips the tier pick entirely (you'd want the tier with a real traffic surface, not the cheapest one) — flag that if it's the case, since I defaulted to supply-chain given "owners of" six projects reads as a dependency list.

## The two with no sponsor button

This isn't a "pick a cheaper tier" problem — per Step 4, *"a project with no verified destination is not a target."* Don't estimate or reserve an amount for them today. Pay the four verified ones now; when the other two set up a Sponsors page or Open Collective, come back with the link and I'll verify it and size the tier then. Don't pressure them past a plain ask — Step 8's rule is *"no pressure on a maintainer to accept money, to advertise the sponsorship, or to produce gratitude on a schedule."*

## Payment mechanics that will actually bite you this afternoon (Step 7)

- Six small recurring tiers by **card** is fine — the $5,000-minimum-per-invoice rule only applies to **invoiced** corporate billing, not card.
- If your org is already on invoiced billing, **do not switch billing mode today** — switching cancels every existing sponsorship on that org, and each one gets a cancellation email.
- Personal-account sponsorships pass through fee-free; **organization** sponsorships by card carry up to 6% (3% processing + 3% service) — check which one your card is actually running through.

Send me the six repo URLs (or owner/repo) once you've clicked through, ideally with what each ladder shows — I'll turn that into the final verified table (project, destination, tier, $/yr) in one pass.