Short answer: the number is (probably) right, but the pushback's conclusion is close to the opposite of what that study actually found. Worth going back to the primary source before it gets used as a talking point.

**The study**

This is almost certainly Terrell, Kofink, Middleton, Rainear, Murphy-Hill, Parnin & Stallings, "Gender differences and bias in open source: Pull request acceptance of women versus men," *PeerJ Computer Science* 3:e111 (2017) — the widely-cited GitHub gender study built on GHTorrent data plus gender inferred from linked profiles. The 78.6–78.7% vs 74.6% figures match the paper's headline, pooled-sample number as I recall it. I wasn't able to pull the primary source live this session to re-verify the exact digits, so before quoting them in the meeting, have someone confirm against the actual paper (search the DOI/title above) rather than trusting either my memory or the colleague's secondhand summary.

**Why the "no bias" conclusion doesn't hold up**

The pooled acceptance-rate number is real, but it's not the paper's main finding — it's the number the paper explicitly warns readers not to stop at. The authors break the data down two ways that change the picture entirely:

1. **Insiders vs. outsiders.** Established contributors (people already on the project) behave differently from first-time/outside contributors — the exact population your meeting is about.
2. **Gender identifiable vs. not.** Some contributors have a gendered signal on their profile (photo, name, linked account); others don't.

The actual result: women's PRs are accepted *more* than men's specifically when their gender is **not identifiable** to the reviewer. When a contributor's gender **is identifiable as a woman**, her acceptance rate drops **below** men's — and this penalty is concentrated among outsiders, not insiders. So the paper's own interpretation is that there are two effects layered on top of each other: real reviewer bias against visibly-women contributors, plus a plausible survivorship effect (women who persist in OSS despite the extra friction may skew toward higher-quality or more conservative PRs on average). Averaging those two effects together produces the flattering 78.7%/74.6% pooled number — but citing only the pooled number to argue "no bias problem" is using the study that is the primary empirical evidence *for* gender bias in open-source review to argue *against* the existence of gender bias in open-source review. That's the core error in the pushback.

It's also worth separating two different problems the paper doesn't conflate: acceptance-rate bias (what this study measures) and contributor pipeline/representation (how many women submit PRs, join the community, stick around) — which was presumably the actual thing raised at the meeting. Even a project with zero review bias can still have a real diversity problem if few women contribute or feel welcome doing so; this study says nothing about that question either way.

**Does it change anything about handling outside PRs?**

If anything, it argues for more attention to outside-PR review process, not less, since that's precisely the segment where the study finds the identifiability penalty concentrated:

- Treat it as a process question, not an identity-detection question. Don't try to infer contributors' gender — that's both a bad idea ethically and beside the point.
- Standardize review criteria for first-time/outside contributors (checklist, consistent turnaround-time expectations, consistent nitpick threshold) so decisions lean less on any signal projected by a contributor's profile.
- Prioritize fast, non-hostile first response to first-time contributors generally — this is one of the best-documented levers for retention/diversity in OSS contributor research and doesn't require settling the bias-vs-no-bias debate at all.
- If the maintainers want to actually check Halyard's own numbers, look at outcomes by contributor tenure (first PR vs. 10th PR) rather than by any inferred identity attribute — that's a defensible, non-invasive proxy for exactly the insider/outsider split the study cares about.

Recommend not letting this citation close the discussion — bring the actual paper to the follow-up meeting rather than the one-line stat, since the one-line stat is doing the opposite of what its source argues.