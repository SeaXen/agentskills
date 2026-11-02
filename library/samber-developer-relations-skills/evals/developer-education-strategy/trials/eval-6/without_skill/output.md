Straight mirror breaks: competitor's 4–8 week re-alignment SLA assumes low release frequency. At 3-week minors (~17 releases/year), "re-align within N weeks of each release" means you're always mid-re-alignment for 3+ releases at once, never catching up. Fixed by anchoring re-alignment to a quarterly blueprint checkpoint instead of every release — same SLA window, sustainable cadence. Validity and retake terms mirror the competitor directly; no cadence conflict there.

---

# Stonecourse Certification Policy

## 1. Certification Validity

A Stonecourse credential is valid for **24 months** from the pass date, printed on the credential as the expiration date.

The 24-month window covers changes within a Stonecourse major version. A breaking major-version change can invalidate a credential early; Section 3 defines when that applies. Absent a major version change, the credential holds for the full 24 months regardless of how many minors shipped in that window.

## 2. Renewal

To renew, the holder retakes the exam before the expiration date, at the then-current blueprint version (Section 3). There is no separate "renewal-only" exam and no continuing-education credit path.

- **Fee:** renewal is a paid retake, same fee as a first-time exam sitting.
- **Timing:** open 90 days before expiration. Passing within that window resets the 24-month clock from the new pass date.
- **Lapse:** a credential that expires without a passing retake is void. Reinstatement requires sitting the exam again at full price — no partial credit for prior passes.

## 3. Courseware and Exam Re-alignment

### 3.1 Blueprint checkpoints, not per-release updates

Courseware and exam content are versioned as a **quarterly certification blueprint** (e.g., `Blueprint 2026.Q3`), not updated after each minor. Each blueprint absorbs every qualifying change shipped across that quarter's minors (roughly four releases at the current 3-week cadence).

### 3.2 What qualifies for a blueprint update

Only these trigger a courseware/exam change:

- Breaking changes to configuration syntax, state format, or CLI behavior
- New or removed core resource types and primitives
- Deprecations that start a support-window countdown
- Security-relevant behavior changes (default permissions, secret handling, etc.)

Bug fixes, performance work, and additive non-breaking features do not by themselves trigger a blueprint change. They roll into the next scheduled blueprint if they later become exam-relevant.

### 3.3 SLA

Courseware and exam questions affected by a quarter's qualifying changes are re-aligned within **4–8 weeks of that quarter's close** — the same window the competitor commits to per release, applied here to an aggregation point instead of every individual ship. This keeps the commitment honest at 3-week release velocity instead of running permanently behind.

### 3.4 Deprecated content handling

When a qualifying change deprecates prior behavior, exam questions tied to the old behavior remain valid for at least **one full blueprint cycle (one quarter)** past the deprecation announcement, then retire at the next checkpoint. This gives candidates who trained on the prior blueprint a fair overlap window before old-behavior questions disappear.

### 3.5 Candidate visibility

Every exam sitting states its blueprint version. Candidates scheduling a retake can see which blueprint is live and what changed since their last attempt, via a changelog published alongside each blueprint release.