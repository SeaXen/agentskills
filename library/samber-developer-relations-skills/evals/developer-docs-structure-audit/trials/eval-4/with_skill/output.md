**Bad plan. Two rule violations, both named as hard failures in the audit skill.**

1. **Empty scaffolding.** Wiring 4 new top-level sections into the sidebar *before* content exists is the exact thing Diátaxis calls out by name: "It certainly does not mean that you should create empty structures for tutorials/howto guides/reference/explanation with nothing in them. Don't do that. It's horrible." Readers hit empty or near-empty sections for a full quarter while you backfill.

2. **Teardown reflex.** "Rip the band-aid off, quarter of downtime" is a full-site rewrite in disguise. Skill's wording: "Rewrite the docs site is not a recommendation, it is an abdication. Keep the documentation useful at every step of the remediation." A quarter where 90 pages sit half-migrated is not "useful at every step" — it's the failure mode the audit exists to prevent.

**Do this instead — same destination, shippable path:**

1. Inventory all 90 pages first (`docs-inventory.py` if you have repo access, else build by hand from nav + open pages). Classify each: mode, confidence, mixed-mode flag, current section.
2. Rank moves by reader-need-fixed-per-hour, not by "does it fit the new taxonomy": split mixed pages first (a day each, no SME needed), then merge contradictory duplicates, then move well-placed-but-misfiled pages, then write confirmed gaps, then rename sections last.
3. Ship one item at a time. Publish after each. A section goes live in the sidebar only once it holds real content — not on day one of the sprint.
4. Before locking "exactly these 4 top-level sections," run a tree test or card sort if you can (Step 7). If current nav already scores well there (~80% task success, ~60% direct-path), the restructure itself is the wrong spend — budget goes to gap-filling instead.

**Answer this before locking scope:**
- Who executes remediation, how many hours/week — engineer-only team makes every writing-heavy item (missing pages) expensive, changes the order.
- Can you ship redirects? If not, every "move" and "rename" is off the table entirely (broken links).
- One-off cleanup or governed long-term? Changes whether you invest in CI content-type checks / CODEOWNERS now.
- Audience: self-serve devs, enterprise eval teams, or both? Determines mode balance (heavy tutorial vs heavy reference).

Next: run the inventory pass (script or manual) and paste/share it — that's what turns "90 pages are a mess" into a ranked queue instead of a plan to blow up the sidebar for a quarter.