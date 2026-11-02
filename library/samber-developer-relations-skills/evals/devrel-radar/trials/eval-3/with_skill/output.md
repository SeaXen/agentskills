# DevRel inherited-source triage (2026-10-30)

**What this is:** a verdict on the five sources you checked, based on your browser results plus the skill's recorded audit. It is not a monitoring service. Nothing here alerts you when a source dies.

**What I could not do:** WebFetch permission was denied, so I did not re-fetch anything live. The "recorded" evidence below comes from the skill's source audit, which was last verified in Aug–Sep 2026, about 2 months ago and inside the ~6-month window. Your own checks this morning are the only live evidence here.

## Verdicts

| Source | What you saw | Verdict | Why |
|---|---|---|---|
| **devrelx.com** | Loads, but it's a brewing company | **Bin ❌** (dead) | The skill's audit records the same thing: the domain 301s to `showmebrewing.com`, an unrelated business. A resolving URL is not a live source. Remove it and don't link it. |
| **karlhughes.com** | "Domain for sale" parking page | **Bin the URL ❌, keep the person** | The domain is dead. The skill's audit finds Karl Hughes's agency, **Draft.dev** (`draft.dev/learn`), publishing actively in 2026. It covers technical content marketing and devtool GTM. A parked personal domain says nothing about the person, so he is unverified through that URL, not inactive. Replace it with draft.dev (marketing pillar). The skill's audit says he isn't named on the pages it fetched, so you'd be following the agency, not him by name. |
| **devrelfoundation.org** | DNS error | **Bin the URL ❌, keep the organisation** | This is a guessed domain, and a DNS failure is evidence about the guess. The real **Developer Relations Foundation** lives at **dev-rel.org** (code host: `github.com/DevRel-Foundation`). The skill's audit records it as verified-active: a Linux Foundation project, a governance commit on 28 Aug 2026, and bi-weekly community calls from 2 Sep 2026. Swap in dev-rel.org. It is the field's only vendor-neutral practice body, so it belongs near the top if you distrust vendor content. |
| **developerweek.com** | HTTP 403 | **Keep, as unverified ⚠️** | A 403 is a bot block, not a death certificate. The skill treats 403, 5xx and consent walls as unverified, never dead. Open it in your browser. If it shows a current-year event with a date, promote it. It matters only if you speak, sponsor or host this year. |
| **Scaling DevTools podcast** | HTTP 403 on the site | **Keep ✅** (verified-active per the audit) | The site blocks fetchers, but the feed is the datable surface: `feeds.transistor.fm/scaling-devtools`. The audit saw Ep 197 on 20 Aug 2026. Host is Jack Bridger. It covers devtool growth, DevRel and developer marketing. Add the feed to a podcast app and check the newest episode date yourself. Anything over ~3 months old means downgrade it. |

## What this leaves you with

- **Keep:** Scaling DevTools (feed), dev-rel.org, Draft.dev.
- **Keep, unverified:** DeveloperWeek, until your browser shows a dated event.
- **Bin:** devrelx.com, karlhughes.com, devrelfoundation.org. The last two are bad URLs for sources that are still alive elsewhere.

## What they're selling

- **Scaling DevTools:** a podcast plus a community and sponsorships.
- **Draft.dev:** a content agency.
- **dev-rel.org:** nothing, it's a foundation.
- **DeveloperWeek:** conference tickets and sponsorships (Informa Connect).

## Caveats

- **Five of an unknown number.** You only gave me five sources from the inherited list. Send the rest and I'll triage them the same way. Before running any check, search the code host for the organisation name and read its declared website field instead of guessing domains.
- **No full radar yet.** The skill's interview (role, pillars you own, weekly time budget, mediums, ecosystem, event plans) is needed to build a ranked watch list. I haven't asked it, because you only asked what to keep and what to bin.
- **My checks of your 403s.** Treat my statuses for DeveloperWeek and Scaling DevTools as recorded, not re-observed today.

## Manual check for the keepers (about 5 minutes)

1. Open the Scaling DevTools feed and read the newest episode date. Active means within ~3 months.
2. Open dev-rel.org, or the `DevRel-Foundation` GitHub organisation, and confirm a recent commit.
3. Open developerweek.com in your browser. Find a dated 2026 or 2027 event and confirm the organiser.

If you share the rest of the inherited list and your role, pillars and weekly time budget, I'll turn this into the full ranked watch list.