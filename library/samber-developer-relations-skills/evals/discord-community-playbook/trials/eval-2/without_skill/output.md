# Ledgerline support migration plan: GitHub Discussions and Discord #help (November 2026)

**Recommendation:** run the migration as a gated, reversible plan. Don't shut Discussions down in November. I haven't verified the VP's premise, and the plan's first job is to test it.

## 1. Premise check

- ℹ️ **Discoverable** is Discord's in-app server directory. It has nothing to do with Google.
- ⚠️ I can't confirm that Google indexes Discord server messages. I found no way to verify it from here. Treat the claim as unproven until Week 1 tests it.
- ⚠️ Even if some Discord content is indexed, Ledgerline would have no control over titles, canonical URLs, schema, or redirects. GitHub Discussions are indexed today, and they accumulate ranking pages.
- ⚠️ Disabling Discussions would likely 404 those pages and lose that traffic. Test this on a scratch repo before anyone relies on it.
- 🎯 **Real SEO consolidation:** promote solved answers into docs pages Ledgerline owns, so Ledgerline controls the ranking page.

## 2. Risks specific to Ledgerline

- 🔐 **Payments:** members paste request IDs, partial card data, and API keys into help threads. A public, possibly indexed channel is a worse place for that than Discussions.
- ⚠️ **GDPR:** about 70% of members are in DE, FR, and NL. Public support messages are personal data, so you need a privacy notice, a retention rule, and an erasure process. Ask your DPO before any shutdown.
- ⚠️ **Language:** an English-only #help channel disadvantages most of the audience.
- ⚠️ **Peak season:** Black Friday is Nov 27 and Cyber Monday is Nov 30. Payment integration questions spike then, so a channel change in that window is a bad idea.
- ⚠️ **Tooling gap:** Discord has no assignment, no SLA tracking, and no linking to GitHub issues or fixes.
- ⚠️ **Migration:** there is no automated Discussions-to-Discord migration. Unanswered threads need hand-carrying.

## 3. Timeline

| Week | Dates | Work | Output |
|---|---|---|---|
| 1 | Nov 2–6 | Test the premise, take baselines, check legal | Go/no-go inputs |
| 2 | Nov 9–13 | Build the Discord help flow | Ready, but unannounced |
| 3 | Nov 16–20 | Soft launch, Discussions stay open | Early data |
| 4 | Nov 23–27 | Freeze: no channel changes, monitor only | Peak-season data |
| 5 | Nov 30 | Review against the gates in section 4 | Decision |

### Week 1: verify and baseline

1. Pick 10 recent resolved #help threads. Search an exact phrase from each, plus `site:discord.com`. Repeat after 7 days. Record how many appear.
2. Test what disabling Discussions does to URLs on a scratch repo, to see whether pages 404 or hide.
3. Pull Discussions baselines for the last 90 days:
   - volume per week
   - answered rate
   - median first response
   - top Google landing pages, from repo Insights referrers or Search Console if you have it
4. Pull #help baselines: volume and median first response.
5. Export all Discussions through the GraphQL API into a private archive.
6. Send the DPO the privacy and retention questions.

### Week 2: build the Discord side, unannounced

1. Convert #help to a **forum channel** with tags for product area, language, and status.
2. Add a post template: API version, request ID, and "never paste keys or card data".
3. Set up AutoMod regexes for API-key patterns and card numbers, plus a moderator redaction and key-rotation runbook.
4. Create DE, FR, and NL tags or channels, each with a named responder.
5. Write a rota with first-response targets that match or beat the Week 1 Discussions baseline.
6. Define the answer-promotion loop: each solved thread gets a docs or FAQ entry. Name an owner and a weekly slot.

### Week 3: soft launch

1. Add a Discussions pinned notice and a new-post template that point to Discord, so members choose with full information.
2. Keep Discussions fully open. Don't lock, delete, or disable anything.
3. Track both channels against the same metrics.

### Week 4: freeze

No channel changes while Black Friday and Cyber Monday traffic runs. Monitor only.

## 4. Go/no-go gates (Nov 30)

All gates must pass before Discussions go read-only. Any single fail means no-go for now.

| Gate | Pass condition |
|---|---|
| Indexing claim | At least 7 of 10 test threads appear in Google after 7 days. If the claim fails, the SEO rationale is gone and this migration has no justification. |
| Response time | Discord median first response is no worse than the Discussions baseline |
| Resolution | Discord answered rate is at least the Discussions baseline |
| Safety | No unredacted secret survived longer than 1 hour, and rotation ran for every leak |
| Languages | DE, FR, and NL each have staffed coverage |
| Legal | The DPO has signed off on retention and erasure |

## 5. If the gates pass

1. **No earlier than Dec 7:** make Discussions read-only for new posts.
2. Keep the pages up and add a pointer banner.
3. After 90 days of stable metrics, decide on disabling. Never delete, because the archive and the ranking pages are the asset.
4. **Rollback:** reopen Discussions. Rollback triggers are a missed response-time gate for 2 consecutive weeks, or any secret-exposure incident.

## 6. What to tell the VP

- The goal (consolidating SEO) is sound, but the mechanism is unproven.
- Discussions already rank today. Discord indexing is unverified, and it would trade away control of titles, URLs, and redirects.
- The safe path is a one-week test, a reversible soft launch, and a gated decision after the Black Friday and Cyber Monday peak.
- The stronger consolidation play is turning solved threads into owned docs pages.

## 7. Open questions

- Do you have Search Console on the docs site and repo traffic access?
- What is the current Discussions volume per week?
- Who staffs DE, FR, and NL responses?
- Does legal already have a stance on public support data?