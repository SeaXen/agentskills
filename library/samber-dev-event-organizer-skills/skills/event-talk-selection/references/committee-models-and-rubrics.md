# Committee models and scoring rubrics

Contents:

- Two documented committee models end to end.
- Both rubrics with their criteria wording.
- The aggregation mechanics.
- A worked positive and negative scoring example.

Three committee-and-rubric pairs are documented in enough detail to reproduce. Treat Models A and B as the two ends of a scale and Model C as a documented middle point between them, not as proof the space in between is now fully mapped - only one point sits there.

## Model A - small consensus committee

This model documents the mechanics not just the policy of organizing single-track conferences.

### Roles

- **Anonymizer** - one or two organizers, optionally with one or two outside helpers. They alone see the raw submission form and spreadsheet, including names, companies and pronouns.

  They **do not review or score any proposal**. This role separation is the whole point: it closes the leak that platform-level anonymization leaves open, where the tool hides the author field but not what the author wrote.

- **Graders** - the remaining four to five organizers, who only ever see anonymized proposals.

### What the anonymizer actually does

- Rewrites identifying details into bracketed placeholders - "[Large Tech Firm]", "[they]".
- Deliberately **preserves** identity where it is essential to the talk's own content. The example given: a submitter's disability status, when the talk is about that. Anonymization applied with judgment, not as a strip-everything filter.
- Assigns each proposal a random ID, so submission-order timing cannot re-identify a submitter.
- Folds financial-assistance requests into the same anonymized form, backed by an explicit organizer promise: "requesting financial assistance will not affect a proposal's chances of acceptance." Anonymization is the enforcement mechanism for that promise, not a gesture.

### Rubric: the letter-grade advocate scale

| Grade | Meaning                                                          |
| ----- | ---------------------------------------------------------------- |
| A     | Will actively advocate for inclusion                             |
| B     | Likes it, won't advocate for it                                  |
| C     | Neutral                                                          |
| D     | Will advocate against inclusion                                  |
| X     | Abstain - the reviewer suspects they have identified the speaker |

Aggregation: grades combine as a **best-worst pair** per proposal - "AC" means one reviewer gave A and another gave C - never as an average. The pair preserves the disagreement that a mean erases, which is exactly what the discussion round is for.

Stated heuristics: "AA talks generally get in immediately. AB talks are usually also admitted." At least one A is the practical floor - a proposal with only B/C/D grades and no advocate cannot get in regardless of how good its average would look.

X is this model's conflict-of-interest mechanic, but it fires only on suspected identity leakage through anonymization. It does not cover a declared employer relationship or a personal connection; pair it with Model B's recusal rule to cover both.

### Selection round

- One synchronous round over a call, discussing graded proposals together. No further asynchronous scoring passes.
- Fill the fixed number of slots, then keep a backup list of about **five talks** as the waitlist for late declines. This is one documented waitlist size.
- Duplicate handling: if one person has multiple accepted proposals, organizers let them choose which to give, or suggest a preference - a per-speaker cap applied after review rather than before submission.

## Model B - multi-tier cascade

This model structures multi-track conferences with large submission volumes.

### Roles

- **Staff** own budget and logistics, not content.
- **Program committee** - volunteer subject-matter experts, selected by the co-chairs, scoring submissions within their own track.
- **Track chairs** - a second evaluation tier.
- **Co-chairs** - contracted, compensated, and rotating every edition; they finalize the program.

### Rubric: four criteria on a five-star scale, half-star increments

1. **Content** - "the relevance and coherence of the session's content, the quality of the proposal, and the likelihood of effective delivery."
2. **Originality** - "the degree to which the session presents new and innovative ideas or approaches, as well as the originality of its delivery."
3. **Relevance** - "the extent to which the session's content provides new and exciting insights or information that is relevant."
4. **Speaker(s)** - "the suitability of the proposed speaker(s) based on their expertise and alignment with the subject matter."

**Written feedback accompanies every rating.** A score with no rationale is not a complete review - it cannot survive being passed to a later tier, and it cannot be turned into decline feedback.

### The cascade

1. Committee members score within their track; scores combine across the track's reviewers. The reviewers-per-submission count is not disclosed.
2. The **top-scoring 30%** advance to track chairs.
3. Track chairs select roughly **30% of those** - about 9% of the original pool - for co-chair review, leaving **mandatory** comments for the co-chairs.
4. Co-chairs make the final selection, combining committee scores, track-chair comments and, at the poster stage explicitly, diversity: "The co-chairs will select up to ten (10) poster sessions, taking the program committee scores and diversity into consideration."

Step 4 shows a final round mixing a quantitative score with a qualitative program-fit overlay instead of a pure rank cutoff. Beyond "scores plus diversity", the mechanics of a balance pass are undocumented; anything more specific you build is your own design and should be labeled that way.

### Conflict of interest

Reviewers are told to **skip the question** - abstain rather than score and disclose - for submissions from colleagues they work closely with, or from people and organizations they are associated with or in competition with. The framing is an identity check: review wearing the event's hat, not an employer's. It is a self-administered honour-system recusal with no registry and no audit step.

## Model C - distributed reviewer pool

PyConDE & PyData's own published reviewer guidelines document this model end to end: a single review tier run through a review platform (Pretalx), rather than Model B's multi-tier cascade, and a numeric scale rather than Model A's advocate letters or Model B's star rating.

### Roles

- **Reviewers** - volunteers who register a track preference and are then assigned submissions by the platform. Any reviewer may pick up additional submissions beyond their assignment.
- **Program committee** - meets after the review window closes to make final accept/reject decisions from the collected scores and comments; not a second scoring tier, since reviewers do not hand off to a track-chair layer the way Model B's do.

### Assignment mechanic

Submissions are distributed to reviewers by track preference. Once a submission has **three or more reviews**, the platform stops actively surfacing it for further review unless a reviewer has something particularly important to add - a real, sourced answer to the reviewers-per-proposal question Models A and B leave open (Model A: four to five graders per proposal at small scale; Model B: undisclosed).

### Rubric: 0-3 numeric scale

| Score | Meaning                                                         |
| ----- | --------------------------------------------------------------- |
| 0     | No, strong - would argue against accepting                      |
| 1     | No, indifferent - doesn't support it, wouldn't argue against it |
| 2     | Yes, indifferent - supports it, wouldn't argue strongly for it  |
| 3     | Yes, strong - would argue strongly in favor                     |

**A comment justifying the score is mandatory on every review** - the same non-negotiable Model B applies to its star ratings, enforced here on a numeric scale instead. Reviewers evaluate against a fixed set of guiding questions (is the topic current and relevant, how detailed is the submission, what problem does it address, what are the takeaways) plus a named positive/negative list: ethics discussion, open-source tooling and practical methodology score positively; a submission whose main aim is selling a product or service, closed-source software, or a talk already given at very similar conferences score negatively.

### Conflict of interest

A reviewer who is the submission's author, or helped write it, clicks **Abstain** and is instructed not to read the other reviews on it. Reviewers who continue despite a lesser conflict (same employer as the author, a friendship, a personal bias on the topic) must disclose it in the review text itself - a documented middle ground between Model A's identity-suspicion abstain and Model B's skip-the-question recusal: an explicit disclosure obligation neither of the other two rubrics carries.

## Worked example: scoring one proposal

Proposal, anonymized: _"Why our build cache kept lying to us"_ - a 25-minute talk on debugging a distributed build cache that silently served stale artifacts for months. Context field: the speaker ran the incident and has not spoken publicly before.

**Positive - Model B scoring, done correctly:**

> Content 4.0 - clear failure narrative with a concrete debugging arc; the outline shows the talk actually reaches a resolution rather than stopping at "it was hard". Originality 4.5 - cache-correctness bugs are common but almost never presented; no similar talk in this year's pool. Relevance 3.5 - narrower than our platform track's median, but the failure mode generalizes to anyone running remote caching. Speaker 3.0 - first-time speaker, no prior recordings to assess delivery from; the incident ownership is a strong fit signal even without a track record. Recommend advancing; if accepted, pair with speaker support.

Every criterion is scored separately, the low score is explained rather than hidden, and the comment gives the next tier something to act on.

**Negative - the same proposal, reviewed the way it usually goes wrong:**

> 3.5 stars. Interesting but not sure about the speaker.

Three defects, and each one costs something concrete:

- It collapses four criteria into a single number, so no later tier can tell whether the reservation was about the topic or the person.
- It leaves "not sure about the speaker" unexamined, the most common route by which a first-time-speaker penalty enters a process that claims to favour new voices.
- It produces nothing usable as decline feedback, which is what forces an organizer to write the decline from scratch or send a form note instead.
