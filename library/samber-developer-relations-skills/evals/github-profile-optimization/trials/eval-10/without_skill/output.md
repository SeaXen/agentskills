**Primary:**
Tideglass diffs your Postgres schema and writes the migration — same binary whether you run it solo on a laptop or wire it into a bank's release pipeline.

**Alternates:**
- Diffs your Postgres schema, writes the exact migration to apply it. Install and run, or gate it in a regulated pipeline.
- One tool, one behavior: `tideglass diff` on your laptop is the same code path a bank runs in CI.

**Why this shape, not a "we're stable/trustworthy" line:** promising longevity directly ("won't disappear," "enterprise-grade") reads as defensive and is exactly the kind of claim a skeptical platform team discounts. "Same binary, solo laptop or bank CI" earns that trust by implication — no separate free/toy vs. paid/real split to abandon, one code path both audiences run. Solo devs read speed and simplicity into it; platform teams read "no bait-and-switch, no fork to get orphaned in." One line does both jobs without addressing either audience by name in a way that excludes the other.

Drop the bank/laptop pairing if it feels too cute for a bio field — the plain function-first alternate carries the same precision without the contrast device.