## The rule you're actually applying

SERP overlap is a proxy for what Google's ranking algorithm has already decided about query intent — if two queries keep surfacing the same URLs, Google's classifier thinks they're the same search need, and fighting that with two separate pages usually gets you cannibalization, not two rankings. The standard industry heuristic (Ryan Jones' SERP-overlap clustering method, since adopted by most clustering tools) uses **top-10 overlap** with a threshold around **3 shared URLs (30%)**:

- **≥30–40% overlap → one page.** Google already treats these as the same topic.
- **15–29% → borderline.** Needs a manual look, not a blanket rule.
- **≤10–15% → separate pages.** Different enough that merging would dilute both.

Overlap count alone isn't the whole test — always sanity-check against **intent** (informational vs. commercial vs. transactional vs. navigational). High overlap with mismatched intent usually means "pillar page + a subsection," not a full merge.

## Your four pairs, called

| Pair | Overlap | Verdict | Label | Why |
|---|---|---|---|---|
| A — connection drops / disconnects randomly | 8/10 (80%) | **Merge — one page** | *Duplicate cluster* | Near-identical SERPs. Google has already decided these are the same query. Pick the higher-volume term as the primary, fold the other in as a synonym/H2 variant. |
| B — reconnect strategy / exponential backoff | 5/10 (50%) | **Merge, but structure it** | *Pillar-with-section* | Well above the merge threshold, but "backoff" is a specific technique *within* "reconnect strategy," not a synonym for it. One page, with exponential backoff as a clearly-anchored H2/section (own heading, own anchor link) rather than blended prose — that keeps you eligible for a jump-link sitelink and a featured snippet on the narrower query. |
| C — presence api / who is online | 2/10 (20%) | **Keep separate** | *Adjacent, not identical* | Below the merge threshold, and the intent split explains why: "presence api" is developer/reference intent (docs page), "who is online" is a product-capability/informational query (could be a blog explainer or feature page). Interlink them, don't merge them. |
| D — message ordering / pricing per connection | 1/10 (10%) | **Keep separate — not even close** | *Unrelated* | Barely any overlap, and intent is worlds apart (technical/dev doc vs. commercial/pricing). This pair barely needed the data — treat "wildly different intent" as a free pre-filter next time before you even bother pulling SERPs. |

## Handling the other 60 without losing your mind

**1. Pull all 60 SERPs in one batch, same settings.** Same location, device, language, logged-out/incognito, same result count (top 10). Overlap comparisons are meaningless if half your pulls are personalized and half aren't — that's the #1 way this kind of audit quietly goes wrong.

**2. Put it in one sheet, not 60 tabs.** Columns: `keyword_A | keyword_B | url1..url10_A | url1..url10_B`. One row per candidate pair.

**3. Compute overlap with a formula, not by eyeballing 60 lists.** In Sheets/Excel:
```
=SUMPRODUCT(ISNUMBER(MATCH(A_urls, B_urls, 0)))
```
Add a `%` column (`overlap / 10`) and conditional-format it: green ≥40%, yellow 15–39%, red <15%.

**4. Auto-decide the green and red rows — only look at yellow by hand.** That's the whole point of the threshold: it should collapse ~80% of your 60 into an obvious call, leaving maybe 10–15 pairs that need a human glance at actual titles/intent.

**5. For yellow (borderline) rows, check two things before deciding, in this order:**
   - **Same exact URL or just same domain?** Two different pages from the same site ranking for both queries is a much weaker merge signal than the literal same URL appearing twice.
   - **Same intent?** If overlap is borderline *and* intent matches → merge. If overlap is borderline and intent diverges → separate, interlink.

**6. For green (high-overlap) rows, still spot-check intent** the way you did for pair B — high overlap tells you *whether* to merge, not *how* to structure the merged page. A pillar-page-with-anchored-sections is often the right shape when one keyword is clearly a sub-technique of the other.

**7. Don't re-derive the threshold per pair.** Decide the cutoff once (30% is the defensible industry default), write it at the top of the sheet, and apply it mechanically. The temptation on pair-by-pair review is to rationalize a merge you want — the automated tiering is what keeps 60 rows from turning into 60 individual judgment calls.