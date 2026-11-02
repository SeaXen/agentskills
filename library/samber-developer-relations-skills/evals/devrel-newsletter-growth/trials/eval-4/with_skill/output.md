# Tessellate v2.0: tips for This Week in Rust, KubeWeekly/CNCF and Cooperpress

I wrote one short tip per newsletter, not the press release or the $300 note. I haven't checked any newsletter's live page, so confirm each route before sending.

## Two things I refused

| Ask | Verdict | Why | Instead |
|---|---|---|---|
| $300 to each newsletter "to make sure we get included" | ❌ Trust and law | Paying for an editorial pick is a hidden paid placement. The skill and `tech-press-relations` say never to offer payment, a gift or reciprocity for a pick. US endorsement rules and UK/EU ad rules also want paid placements labelled. TWiR is volunteer-run, and a cash offer would likely get you ignored. | An editorial tip with no money attached. A labelled sponsorship is a separate purchase (see the last section). |
| One press release sent to all of them | ❌ Trust | Curators reject press releases with no technical substance. This Week in Rust (TWiR) wants an item "more informative than just a changelog". | A short tip per newsletter, matched to that newsletter's route. |

## Three blockers before you send anything

1. **The link must be ungated.** Curators reject email-gated pages (the skill's refusal table has the same row). Publish the v2.0 announcement openly, with the benchmark numbers and methodology on the page. The report download can stay behind the form as an optional extra.
2. **Keep newsletter consent out of the benchmark form.** The report download must not bundle or pre-tick a Tarnwick Dispatch subscription.
3. **Add a tagged signup line at the end of the announcement.** Curators link your post, not your newsletter, so this line is the only way an inclusion grows the Dispatch. Use a hidden `source` field per route, for example `pitch-twir-v2-0` and `pitch-cooperpress-v2-0`. TWiR forbids tracking parameters in links, so put the tag on the form, not the URL.

Suggested line: *"Release notes and breaking changes by email, monthly from the Tarnwick team: [latest issue] · [subscribe, unticked box] · [privacy notice]."* Only state a cadence the Dispatch really holds.

## Tips to send

Send each within a day of the post going live. Send one tip per curator for this release only. Run each through your humanizer first, and make sure a human wrote the underlying post, since TWiR refuses LLM-written articles.

### This Week in Rust

Route: a pull request to the draft issue. Project updates go through r/rust only, so post there first.

1. Post a short, human-written r/rust thread on the v2.0 release. Disclose that you work on it.
2. Open a PR to the current draft issue, if the thread qualifies. Use link text equal to the page title, the canonical URL and no tracking parameters.

The r/rust post:

```
Title: Tessellate 2.0: <the one change a reader cares about>

I work on tessellate at Tarnwick. 2.0 <does X>: <one concrete change with the
number or flag from the notes, e.g. "queries N% faster on <dataset>; breaking:
<API change>">. Methodology and numbers in the post, no signup needed:
<ungated canonical URL>

Feedback welcome, especially on the migration path.
```

### KubeWeekly / CNCF

Heads-up: KubeWeekly ended as a weekly, and the old form may be dead. The current route is `marketing@cncf.io`. CNCF wants items of interest beyond one commercial platform, from the last month, and not gated. A Rust spatial index with no Kubernetes angle probably doesn't fit. Send only if you have a real cloud-native story, such as a geo-indexing use case in a cluster workload. Otherwise skip it and tell me, and I'll swap in a better-fitting newsletter.

```
Subject: Tessellate 2.0 - <one fact>, <cloud-native use case>

<One sentence: what the post shows, with the number.>
Link: <ungated canonical URL>
Disclosure: I work on tessellate at Tarnwick.
```

### Cooperpress newsletters

Route: reply to the latest issue email of the newsletter you pick. It has no published criteria, and submissions are worked weekly.

Pick by reader fit. Cooperpress doesn't obviously run a Rust title, so check the current list for the closest match. One tip per title, and none where readers don't overlap. Waiting one full weekly cycle before reading silence as an answer.

```
Subject: Tessellate 2.0 - <one fact a reader cares about>

<One sentence: what the post shows, with the number or decision in it.>
Link: <ungated canonical URL>
Disclosure: I work on tessellate at Tarnwick.
```

## Optional: a separate sponsorship inquiry

If you want a guaranteed placement, buy it as a labelled ad. Only send this to a newsletter that sells sponsorships, which Cooperpress does. TWiR doesn't sell slots. Keep it fully separate from the editorial tip, and don't promise or imply an editorial link.

```
Subject: Sponsorship rates and availability

Hi <name>,

We're Tarnwick, maker of the tessellate Rust crate. We'd like to book a
labelled sponsored slot in <newsletter> around <date>. Could you send rates,
formats and availability?

This is separate from any editorial submission.
```

## Gate status and open questions

| Gate item | Status |
|---|---|
| Programme: named owner and backup, last 3 issues on time | ⚠️ Unproven. I need the Dispatch's owner and cadence. |
| Consent: where the 900 subscribers came from | ⚠️ Unproven. I need the collection source per segment, and where subscribers live. |
| Sources distinguishable | ⚠️ Not yet. It depends on adding the hidden `source` field to the form. |

If the programme or consent items fail, fix them first. Sending traffic to a thin or ownerless newsletter turns new subscribers into the first complaints.

Open questions:
- What are the v2.0 numbers (headline benchmark, breaking change, version), so I can fill the placeholders?
- Is the announcement post itself behind the form, or only the report?
- Is there a Kubernetes or cloud-native angle for CNCF?
- Which Cooperpress titles do your readers match?

Once the Dispatch has about 30 confirmed signups per source, rank the routes by those numbers. Don't rank on fewer.