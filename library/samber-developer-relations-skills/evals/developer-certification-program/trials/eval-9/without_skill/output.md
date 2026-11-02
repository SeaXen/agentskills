Don't ship the plan yet. Next, pull the Q3 form B export and split pass rate by partner vs non-partner (about 1 hour).

## Why not ship it yet

- **No cause is proven.** The jump has at least four explanations, and your plan fixes only one.
- **Form A is your control.** It stayed at ~60%, so the cause is probably specific to form B, not general AI use. If AI cheating were the driver, form A would rise too, unless partners mostly sat B.
- **Your three actions are irreversible or punitive.** Do them after the data, not before.

## Candidate causes

1. **Form B leaked.** Sandbox grading is deterministic, so answers or command sequences are easy to share.
2. **Form B changed.** A task got easier, the grader loosened, a cutoff moved, or a sandbox bug accepts wrong answers.
3. **Partner coaching.** The resellers run prep on B-like labs. This is legitimate if tasks test the real job.
4. **Proxy or AI test-taking.** Partners may have an incentive: if certified headcount counts toward their tier, they gain from passes.

## Data to pull

1. Form B pass rate: partner vs non-partner Q3 candidates.
2. Form A pass rate for partner candidates. Partners passing A at ~60% but B at 91% points to the form, not the people.
3. Item-level pass rate Q1 vs Q3. A few tasks jumped = leak. All tasks jumped = grader or difficulty change.
4. Time-to-complete and score distributions. Look for a cluster at the ceiling, near-identical command sequences, and very short sessions.
5. Account metadata. Look for shared IPs or devices, many logins from one network, and paste or automation patterns.

Also check the changelog: did anything in form B or the grader change between Q1 and Q3?

## Your three actions

- **Reset all Q3 form B badges: don't.**
  - It punishes honest candidates and has no evidence behind it.
  - It is outward-facing and hits two paying partners.
  - Check your certification agreement first. It must allow revocation.
  - Instead, mark affected badges "under review". Offer a free proctored hands-on re-verification (about 45 minutes). Revoke only on fail or no-show.
- **Proctored multiple choice: wrong fix.**
  - "Edge Operator" is a hands-on credential. MCQ measures recall, not operating skill, so you lose validity.
  - The problem is delivery integrity, not format.
  - Keep hands-on tasks. Randomize parameters per candidate (hostnames, configs, values) so shared answers fail. Rotate from a task pool. Proctor remotely if you need to.
- **Strict no-AI rule: unenforceable unproctored.**
  - It only catches the honest.
  - Decide first whether operators use AI on the job. If yes, allow it and write tasks AI can't pass alone, such as state-dependent debugging.
  - If no, enforce it with proctoring, not a rule.

## Decision by finding

- **Only partner candidates jumped, on B only:** run the re-verification for the partner cohort. Talk to partner managers privately first.
- **Everyone jumped on B, a few items drive it:** leak. Retire those items, randomize, and re-verify the affected passers.
- **Everyone jumped on B, all items:** grader or difficulty change. Fix B. Don't punish anyone. Ask whether the 91% cohort meets the bar.
- **A and B both rose for partners:** coaching or proxy-taking. Add proctoring for hands-on, and review the partner contract.

## Steps

1. Pull the per-candidate Q3 export for forms A and B (about 1 hour).
2. Run the 5 checks above (about half a day).
3. Pick a branch from the decision list.
4. Announce nothing until step 3.

Next: check whether form B or its grader changed between Q1 and Q3. That takes about 10 minutes and may settle this.