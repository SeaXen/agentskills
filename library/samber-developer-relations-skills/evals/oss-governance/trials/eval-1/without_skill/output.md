# Quillrope Steering Council — Draft Charter

Below is a complete draft, structured like `GOVERNANCE.md` + an `ELECTIONS.md` companion, adapted from PEP 13 (council shape, authority, employer-diversity rule) and the Kubernetes Steering Committee model (staggered terms, Election Officer, electorate-by-activity). One judgment call up front, stated plainly rather than buried: **PEP 13 and the Kubernetes model both assume an electorate of dozens-to-thousands of people choosing among a pool of credible candidates. Quillrope has 3 people with merge rights and 9 external contributors last year, 6 of whom fixed a typo.** A literal copy of either model produces a 5-seat "election" with 3 candidates and no real electorate — a formality, not a governance mechanism. The draft below keeps the 5-seat, 2-year-staggered structure you asked for, but resolves that gap explicitly (Section 3 and the Bootstrap Plan) instead of pretending it doesn't exist. Change it if you disagree — that's a real fork in the design, not a detail.

---

## GOVERNANCE.md

### 1. Purpose

The Quillrope Steering Council is the project's final decision-making body. It exists to:

- Resolve disputes that maintainers can't settle among themselves.
- Own release policy, MSRV policy, and breaking-change (SemVer) decisions.
- Grant and revoke merge/commit access.
- Enforce the Code of Conduct at the escalation tier.
- Hold and account for any project funds, trademarks, or foundation relationships.

The Council should use this authority rarely. Day-to-day review, triage, and merge decisions stay with maintainers (commit-right holders), exactly as they work today. The Council is a backstop and a legitimacy mechanism, not a new layer of code review.

### 2. Composition

- Five seats.
- Each seat is one person, not an organization.
- No more than two sitting members may share the same employer at the time of election. If an employer-affiliation change during a term would put a sitting Council over this limit, the Council resolves it by lot among the affected members before the next scheduled meeting (mirrors PEP 13's employer-diversity clause — the point is preventing one company from steering a crate that 41,000 crates depend on, not policing anyone's job).
- Current merge-right holders (you, Dara, Sasha) are eligible to run like anyone else. Holding merge rights is not a Council seat, and a Council seat does not itself grant merge rights — the Council *decides* who holds merge rights, as one of its powers (Section 1).

### 3. Electorate

This is the section that actually determines whether the election means anything. Given how thin the contributor base is, "anyone who's opened a merged PR" is not a workable electorate — restricting the vote to that group returns something close to the current 3-person status quo wearing an election costume.

A person is an eligible voter if, in the trailing 12 months, they meet **any** of:

- Authored a merged commit.
- Triaged or labeled 10+ issues in a way a maintainer later confirmed as accurate (tracked via a `triaged-by` label or equivalent).
- Authored or substantively co-authored an accepted RFC/design doc.
- Maintain a crate with 100+ reverse-dependencies that depends on Quillrope, and have filed at least one substantive issue or design comment (not a bug report alone) in the window. This seat-at-the-table for downstream maintainers matters specifically *because* the dependent graph (41k crates) is Quillrope's real stakeholder base, not just people who submit patches.
- Are a current or immediate-past (within 12 months) Council member or merge-right holder.

Publish the electorate roll publicly two weeks before nominations open, with a correction window, so the list itself isn't a surprise on voting day.

### 4. Terms

- Two years, staggered.
- Five is odd, so seats split unevenly across the stagger: **Class A (3 seats)** and **Class B (2 seats)**.
- After the founding election, Class A serves a 2-year term; Class B serves a 1-year initial term only, to seed the stagger, then reverts to 2 years at its next election.
- From year 2 onward, elections alternate: 2 seats up one year, 3 the next. No more than 3 seats (a bare majority) turn over in any single cycle.
- Assign which winners land in Class A vs. B **by lot, drawn by the Election Officer**, not by vote rank. Ranking-based assignment quietly tells 4th/5th place "you got the short term because you were less popular," which is a bad incentive to build into a 5-person body that needs all 5 pulling together.

### 5. Election Officer

- One person, not a candidate, not a sitting merge-right holder for the cycle they're running.
- Recruit from outside the current 3, ideally someone with prior CIVS/Condorcet election experience elsewhere in the Rust ecosystem — ask the Rust Foundation or a rust-lang team contact for a referral before defaulting to a Quillrope community member, since neutrality is the entire point of the role.
- Responsibilities: certify the electorate and candidate rolls, run the vote, publish results, adjudicate disputes about process (not about outcomes — they don't get a tiebreak vote).
- Role rotates every cycle. The same person can serve twice, but not three times running, so the process doesn't quietly become "whoever ran it last time owns it."

### 6. Nomination

- Self-nomination only, open to anyone on the electorate roll.
- One-week nomination window.
- Each candidate publishes a short statement (position on release cadence, MSRV policy, or whatever the live issues of the moment are) — no debates, no interviews, keep the bar to run low given the size of the pool.

### 7. Voting method

Schulze (Condorcet) method, run through CIVS or equivalent — same mechanism PEP 13 and the Kubernetes Steering Committee both use. It matters here for a boring, mechanical reason: Condorcet methods resist bloc voting and tactical ranking better than plurality, which is more important, not less, when the electorate is small enough that 4-5 coordinated ballots can otherwise decide a seat.

### 8. Vacancies

- A vacated seat is filled by the next-highest finisher from that seat's most recent election, if one exists and the term has more than 6 months remaining.
- Otherwise, the remaining Council appoints a replacement to serve out the term, by majority vote among themselves.
- A Council member who goes unresponsive for 60 days (no maintainer activity, no response to Council business) can be removed by a 4-of-5 vote of the remaining members.

### 9. Decisions

- Ordinary Council business: simple majority of the 5.
- Amending this charter, or removing a sitting member outside Section 8: 4-of-5 supermajority.
- Members recuse from votes involving their own employer's commercial interests in Quillrope.

### 10. Relationship to maintainers

Merge rights are granted/revoked by Council vote, on nomination by any existing maintainer or Council member. This is the one place the two structures touch: the Council can expand the maintainer group faster than an election cycle if the patch/review load demands it — useful given 120 issues/month across effectively 3 reviewers today.

---

## Bootstrap plan for the founding council (target: seated before the March 2.0 release)

Running a fully contested election for all 5 seats *right now*, with the electorate rule in Section 3 applied cold, will surface a handful of real candidates beyond the current 3 — but probably not 5 credible ones yet. Two honest options:

- **Option A — full election, thin field.** Run Section 3-6 exactly as written. If fewer than 5 people file, the unopposed candidates are seated without a contest (still Council-approved, still on the record, no shame in it). Simple, no special-casing, but a majority of the founding Council is effectively appointed-by-default rather than chosen.
- **Option B — split founding term.** Seat the 3 current merge-right holders by ratification (an up/down confirmation vote from the Section 3 electorate, not a contest) as Class A. Run a genuinely contested election for the 2 Class B seats, open to everyone *except* the 3 founders, specifically to pull in a downstream-maintainer or active-triager perspective from outside the existing group. Revisit at the next election whether to keep the founder/at-large split or open all 5.

Recommendation: **Option B.** It's what Kubernetes actually did for its own first Steering Committee — the founding roster wasn't produced by an open contest against a large field, because that electorate didn't exist yet either; it grew into full elections over subsequent cycles. Pretending Quillrope's electorate is bigger than it is doesn't make the council more legitimate, it just makes the first election a formality with extra steps.

Timeline, working backward from a March 2027 2.0 release:

| Date (2026/27) | Milestone |
|---|---|
| Oct 1 | Publish this charter for community comment (RFC-style, 2-week window) |
| Oct 15 | Current 3 maintainers ratify final charter text |
| Oct 22 | Recruit and announce Election Officer |
| Oct 29 | Publish electorate roll (2-week correction window) |
| Nov 12 | Nominations open (Class B seats only, per Option B) |
| Nov 19 | Nominations close, candidate statements published |
| Nov 26 – Dec 10 | Voting period (2 weeks, Schulze/CIVS) |
| Dec 14 | Results certified, Class A ratification vote closes |
| Dec 14 | Founding Council seated (3 Class A @ 2yr, 2 Class B @ 1yr, lot-drawn only if Option A is used instead) |
| Jan–Feb 2027 | Council's first act: ratify 2.0 scope/timeline, publish MSRV and SemVer policy |
| March 2027 | 2.0 ships, under a seated Council rather than 3 informal maintainers |

This leaves roughly 6–10 weeks of Council runway before the release, enough for it to have actually made one real decision (the 2.0 scope ratification) before being asked to weather one.

---

Two things need your explicit sign-off before this goes anywhere, since they're the parts I made a judgment call on rather than just transcribing:

1. **Option A vs. B** for the founding term (full-election-with-thin-field vs. ratify-3-elect-2).
2. **The electorate definition in Section 3** — particularly the downstream-maintainer clause, which is the part with no direct precedent in either PEP 13 or the Kubernetes docs and is the piece most likely to need tightening once you see who it actually qualifies.