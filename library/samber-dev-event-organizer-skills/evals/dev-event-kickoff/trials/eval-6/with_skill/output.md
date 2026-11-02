# MarmotConf: skills for the paper track and for the bilingual programme

**Neither request has a dedicated skill.** The kickoff router lists both as coverage gaps in § 8:

- **Proceedings and a paper track:** "peer review ending in a published paper rather than a stage slot."
- **Running the programme in two languages:** "translated tracks, a bilingual host, per-language labelling."

I won't stretch a nearby skill to cover them. Below is what to load for the parts that are covered, and where each gap sits.

## 1. Peer-reviewed paper track with proceedings and DOIs

**Load, in this order:**

| # | Skill | What it covers | What it does not cover |
|---|---|---|---|
| 1 | `event-cfp-design` | The published call: timeline worked back from the event date, submission fields, anonymization posture (blind review can be mandatory), review criteria stated in the call. | The paper-specific parts below. |
| 2 | `event-talk-selection` | The review machinery: committee composition, blind review execution, rubrics, multi-round cascades, conflict-of-interest recusal, accept/decline/waitlist emails. | It reviews talk proposals only, so it has no camera-ready stage. |
| 3 | `event-schedule-design` | Placing accepted papers into the grid, after selection returns an accepted list. | |

**The gap is everything past the accept decision:**
- the proceedings publisher or series
- DOI minting
- camera-ready and copyright or licence workflow
- indexing
- the author-notification-to-publication chain

Plan these outside the collection. There is no sibling-repo recommendation for it. `developer-relations-skills` is for developer content, docs and open-source strategy, and `developer-platform-skills` is for APIs and SDKs. Neither matches academic publishing.

**Two things to settle before loading the skills above:**
- **Timeline:** a peer-review cycle with revisions runs longer than a talks CFP. Feed that into `event-cfp-design` and `event-planning-timeline`.
- **Format:** if papers are presented in dedicated sessions, that is a shape decision for `event-format-selection`.

## 2. Whole programme in French and English

**Load:**

| Skill | Use it for | Limit |
|---|---|---|
| `event-format-selection` | Deciding the track count with language in mind. | It owns the shape, track count and session mix. |
| `event-accessibility-inclusion` | Interpretation and captioning, but only as access provisions offered on request. | The router says it does not cover "a second language as a design choice." |
| `event-schedule-design` | Laying out parallel language tracks, room matching and clash handling. | It has no language-aware logic. |
| `event-production` | Interpreter booths, headsets and the signal path. | Only if you use simultaneous interpretation. |
| `event-run-of-show` | Cueing the MC and session handoffs. | |

**The gap is the bilingual design itself:**
- which sessions are translated and which are delivered natively
- interpreter sourcing
- per-language labelling
- the bilingual MC's role

Plan these yourselves. Language doubles room, interpreter and AV needs, so it feeds back into the venue, budget and track count.

## Gating and next step

- **Format gate:** in-person is fixed. Track count is not, and parallel language tracks change it. Under § 3, an unfixed format means routing to `event-format-selection` and stopping, so the gated rows stay shut. That includes `event-venue-sourcing`, because the room count depends on the track count. Do that first.
- **Edition:** this is edition one, so `event-first-edition` is the natural rung-1 route, along with `event-format-selection`. The router also expects a short cold-start interview, which I haven't run.
- **Not created:** I did not create `event-context.md`, since this repo is not the MarMotConf project. Run the kickoff in the event's own project to produce it.