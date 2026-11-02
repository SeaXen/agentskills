**Next action (10 min, today):** send the logistics contact the legal ask in section 2. The panel is the only item that can fail on someone else's clock.

# Ironvale season plan, Oct 26 2026 to Jan 15 2027

## 1. What changed from the product marketing list

| Original item | Verdict | Why |
|---|---|---|
| What's new in 5.1 | Keep, W2 | It is the launch anchor. |
| Customer panel | Keep, W3, with a fallback | Legal is unresolved and nobody has run one. See section 2. |
| 5.2 sneak peek | Merge into "What's next" | A sneak peek and a roadmap talk would cover the same unannounced material twice. One session means one approval pass. |
| Roadmap 2027 | Merge into "What's next", W11 | January fits a 2027 roadmap better than November. |
| Meet the platform team | Fold into "What's next" | Nothing shows demand for a standalone intro. Platform engineers co-present and answer "why" questions instead. |
| Ironvale vs the alternatives | Reframe as "Choosing a queue: where Ironvale fits and where it doesn't", W8 | Developers discount a vendor-only comparison. An honest decision guide gets read and cited. |
| (missing) Consumer lag | Add, W6 | These are the top-voted forum themes. A season that skips them ignores the audience's loudest demand. |
| (missing) Dead-letter handling | Add, W7 | Same reason. |

Live sessions stay at six for two advocates: 5.1, panel, lag, dead-letter, choosing a queue, and what's next. Two product-marketing items merged away and two forum-driven items took their place.

**Shape:** launch-dominated through W4, then evergreen-majority. The lag and dead-letter sessions are the evergreen core. They stay useful after 5.2 ships.

## 2. Customer panel (3 weeks, legal pending, first panel)

### Legal gate

1. **Oct 26–27:** send the customer's contact a one-page ask. List exactly what needs approval:
   - company name and logo
   - panelist names and titles
   - topics
   - any numbers they will quote
   - recording and public posting
   - clips
2. **Hard deadline: Nov 3 (T-9 days).** Ask legal for a yes, a no, or a conditional yes by then.
3. **Nov 4 decision.** Pick one outcome:
   - **Full yes:** run as planned.
   - **Yes, but anonymous or no recording:** run it. Use "a logistics company" in all copy and publish no recording or clips.
   - **No answer or no:** run the fallback panel. Use two forum power users plus one Ironvale platform engineer on the "running it in production" theme. Add one line to the customer's thread asking whether they want to join a later one.
4. **Do not publish the company name until legal signs.** Open registration now as "Customer panel: running Ironvale in production", with panelists listed as "to be announced".

### Panel format (45 min, Thu Nov 12)

- **Panelists:** 3. At least one must be a non-logistics user, so the panel survives a legal no. The logistics rep gets no more than one-third of the airtime.
- **Moderator:** advocate B. Advocate A runs chat and collects audience questions. Do not have both advocates moderate.
- **Run of show:**
  - 5 min intro
  - 30 min for 6 prepared questions
  - 10 min audience Q&A
  - Keep 3 spare questions in case the room goes quiet.
- **Questions:** at least two come from the forum themes. Ask about the worst consumer-lag incident and how dead-letter queues were handled. Include one "what went wrong" question. Skip product-pitch questions.
- **Panelists get the question list 5 days before.** Ask for numbers, not adjectives.

### Panel timeline

| Date | Action |
|---|---|
| Oct 26–27 | Send legal ask. Recruit 2 more panelists from the forum. |
| Nov 3 | Legal deadline. |
| Nov 4 | Go, anonymous, or fallback decision. |
| Nov 6 | Send questions to panelists. |
| Nov 9–10 | 30-min rehearsal call. Test audio and recording consent. |
| Nov 12 | Panel. |
| Nov 13–19 | Send the write-up and clips to the customer for approval before posting. |

**Effort:** about 12 advocate-hours over 3 weeks, mostly in the first week.

## 3. Forum fix (about 400 threads)

1. In W1, one advocate spends 2 hours pulling the top 15 threads by votes. Group them into lag and dead-letter. These are the demand evidence.
2. Reply on the top threads: "Covering this live on [date]. Post your setup here and we'll use real cases." That fills the sessions with real scenarios and pre-seeds the audience.
3. Turn the top 10 into one docs troubleshooting page for lag and one for dead-letter handling. Each talk links to its page. Each page links back to the recording.
4. If 5.1 or 5.2 changes lag or dead-letter behavior, say so in those talks. Check this with product in W1. I could not verify it.

## 4. Calendar

| Week (Mon) | Slot | Surface | Owner | Reviewer | Evidence or anchor |
|---|---|---|---|---|---|
| W1 Oct 26 | Prep: legal ask, forum triage, 5.1 demo | internal | A + B | Eng lead | Panel clock |
| W2 Nov 2 | **What's new in 5.1** (live) | webinar, blog, changelog | A | 5.1 release engineer | Launch anchor |
| W3 Nov 9 | **Customer panel** (Nov 12) | webinar | B moderates | Product marketing + customer legal | Fixed date |
| W4 Nov 16 | Panel write-up and clips. Draft lag guide. | blog, video, docs | B (write-up), A (lag guide) | Eng lead | Follow-up for both anchors |
| W5 Nov 23 | No live session (US holiday week). Build the lag demo. | docs | A | Eng lead | Slack |
| W6 Nov 30 | **Consumer lag: diagnose and fix** (live) | webinar, docs page, repo | A | Support engineer | Top-voted forum theme |
| W7 Dec 7 | **Dead-letter handling patterns** (live) | webinar, docs page, repo | B | Support engineer | Top-voted forum theme |
| W8 Dec 14 | **Choosing a queue: where Ironvale fits and where it doesn't** (live plus written guide) | blog, webinar | A | Product + legal (any competitor claim) | Prior-art request |
| Dec 21–Jan 3 | Break. No publishing. | | | | |
| W10 Jan 4 | Prep "What's next". Product signs off the public-safe list. | internal | B | Product lead | Gate |
| W11 Jan 11 | **What's next: 5.2 and 2027, with the platform team** (live) | webinar, blog | B + 2 platform engineers | Product lead + legal | Roadmap anchor |
| W12 Jan 18 | Season recap, metrics review, buffer | blog | A | none | Slack |

**Owners and reviewers:** "A" and "B" are your two advocates. Put real names on the reviewer roles before this is final. Reviewer passes are what limits this plan, not advocate hours.

## 5. Rules per session

- **Choosing a queue (W8):**
  - Name where alternatives win.
  - Use workload-based criteria, such as ordering, throughput, and operations burden.
  - Publish only benchmarks others can reproduce.
  - Product and legal approve any named competitor claim.
- **What's next (W11):**
  - Product publishes a short "safe to discuss" list before prep.
  - Anything not on it stays out.
  - No dates for unreleased features.
  - Open with a "plans may change" statement.
- **Every live session:**
  - Record it.
  - Write a post within 5 working days.
  - Pull 2–3 clips.
  - Link the docs page.

## 6. Capacity check

- Six live sessions across 8 working weeks. W5 and W12 are slack, so committed work stays under 80% of capacity.
- The heaviest advocate weeks are W2–W3 (5.1 plus panel) and W6–W8 (three sessions back to back). Do not add anything to those weeks.
- 5.2 date unknown. If 5.2 ships before Jan 11, turn W11 into "What's new in 5.2" with the roadmap as a 15-minute second half.

## 7. Monthly review (first Friday: Nov 6, Dec 4, Jan 8)

Ask three questions:

1. What shipped versus slotted?
2. Did attendance and forum activity follow the lag and dead-letter sessions?
3. Which session earned a follow-up?

Cut rules:

- If W2 slips past Nov 6, drop the 5.1 live session and ship the blog and changelog only. Keep the panel date.
- If the panel's legal decision is still open on Nov 4, run the fallback.
- If the W8 competitor claims are not approved by Dec 7, ship the decision guide without named competitors.

## 8. Assumptions to confirm (I couldn't ask)

- **5.1:** released or releasing within 1 week.
- **Product marketing:** no objection to the merges and additions. Confirm in W1.
- **Dec 21–Jan 3:** a normal break for your audience.
- **Panel:** the date is about Nov 12.
- **Forum:** the two top themes are lag and dead-letter, order unknown. I put lag first.

**Next:** send the legal ask to the logistics contact today, then book the forum triage for tomorrow.