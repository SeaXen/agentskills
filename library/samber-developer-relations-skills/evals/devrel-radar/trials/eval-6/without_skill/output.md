Don't drop them. Undated doesn't mean abandoned. I couldn't check live (my web fetch was denied), so the details below come from memory and are unverified.

**Do now (about 10 minutes, 3 to 4 minutes each):**
1. Find the source repo for each site and read its last commit date. For diataxis.fr, that is the `evidenceon/diataxis-documentation-framework` repo. For opensource.guide, it is `github/opensource.guide`. Run `gh api repos/<owner>/<repo> --jq .pushed_at`.
2. Open each site's `/sitemap.xml` and look for `<lastmod>`. Many undated sites still publish it.
3. Check web.archive.org for each URL. If the content changed between snapshots, it is maintained.
4. For developerrelations.com guides, find the publisher's newsletter, changelog or social account. Check whether guides still appear there.

**Likely results:**
- **diataxis.fr:** a framework, not a feed. It is undated on purpose and changes slowly. I believe it is stable and widely adopted (Canonical and Django use it). Absence of dates is weak evidence here.
- **opensource.guide:** evergreen content. I believe it is community-maintained with sporadic updates and translations. Stale in places, but the core advice on maintainers and community holds.
- **developerrelations.com guides:** I can't judge this one from memory. It is the real unknown, so verify it first.

**Decision rule:** drop a source only if the repo has no commits for 18 months or more AND the Wayback snapshots show no content changes. Otherwise keep it, and mark it "reference, undated" in your list. A source with no data yet stays on probation, not dropped.

**Weekly budget (my estimate; these are references, not feeds):**

| Source | Minutes/week | Why |
|---|---|---|
| diataxis.fr | 0 steady, plus 90 once | Read it once and apply it to Pellier's docs structure. Re-reading adds nothing. Revisit when you restructure docs. |
| opensource.guide | 5 | Skim one guide per week against your community practice (contributing, triage, governance). |
| developerrelations.com guides | 10 for 4 weeks, then 5 or drop | Verify quality while it is unproven, then settle. |

Steady state is about 10 minutes a week, 20 during the probation month. That fits a docs-and-community owner, because your own backlog beats reading.

Next: run step 1 for all three repos (3 minutes). Paste the dates and I'll give you the keep or drop call.