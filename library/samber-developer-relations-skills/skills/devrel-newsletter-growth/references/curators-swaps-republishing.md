# Curators, swaps and republishing

Read this when writing the runbook for item pitches, a swap, unpaid recommendations or republishing.

## Contents

1. What curated developer newsletters publish about selection
2. Item pitch template
3. Swap and recommendation templates, disclosure label
4. Republishing and posting the lead item

## 1. What curated developer newsletters publish about selection

Pitch an item, not your newsletter. Curators link the release notes or the post, not your archive, so the pitch grows your list only if that linked page ends with a signup line carrying its own source tag. Make that line a precondition of every pitch.

Per-newsletter routes, selection rules, timing and limits live in one place, the newsletter-curators reference of samber/developer-relations-skills@tech-press-relations. Check each curator's current page before pitching: these rules change.

## 2. Item pitch template

```
Subject: <what it is> - <the one fact a reader cares about>

Hi <name>,

<Project> <version> <does X>. The part your readers may care about:
<one concrete change, with the number or flag the release notes state>.

Link: <ungated URL to the post or release notes>
Who it's for: <one line>
Disclosure: I work on <project> at <company>.

No reply needed if it doesn't fit.
<name>
```

Keep it to these lines. Curators scan many pitches per issue and read the first two lines.

## 3. Swap and recommendation templates, disclosure label

Check overlap before proposing: same primary reader (language, stack, role), and a peer whose issues you would recommend without the swap. A swap with a list that does not overlap brings subscribers who leave in their first issues.

```
Proposal: we feature <peer> in our <date> issue, you feature us in yours.
Each side writes its own two-line description and approves the other's.
Each side labels it in the issue: "Swap: we recommend <peer>, they recommend us."
Each side tags the link (swap-<peer>) and shares confirmed signups after 30 days.
One swap first; repeat only if the 30-day numbers hold.
```

Unpaid platform recommendations follow the same overlap check. Label the recommendations you publish ("Newsletters we recommend, some of which recommend us"), and confirm the platform's signup choice names your newsletter, unticked.

Label every swap, recommendation exchange or paid recommendation you publish. A reciprocal deal is very likely a material connection under the US endorsement guides even with no money, UK and EU advertising rules also want a label, and readers who find an undisclosed swap stop trusting the editorial picks around it.

## 4. Republishing and posting the lead item

- Republish a full issue only where you can set a canonical link to the archive page. dev.to supports a `canonical_url` front-matter field; check each other platform's current settings before relying on one.
- Where no canonical link can be set, post an excerpt of the lead item plus a link to the archive.
- Read each community's self-promotion rule before posting there; many forums and subreddits ban newsletter links outright.
- End every republished copy with the signup line and its own source tag (`republish-<platform>`).
- Republish only after the archive page is live.
